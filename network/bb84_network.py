import sys
import os
import statistics
from multiprocessing import get_context
from datetime import datetime
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from lib.db import init_db, insert_p2p_rows, insert_network_row, new_run_id, DEFAULT_DB_PATH


def _sample_link_tortuosity(rng, mean, n):
    """Sample n per-link tortuosity factors: truncated normal(mean, 0.1), min 1.0."""
    if mean <= 1.0:
        return np.ones(n)
    return np.maximum(1.0, rng.normal(mean, 0.1, size=n))


_BATCH = 100  # matches BB84/BB84_run.py's run_BB84_sims — caps trials any one
              # worker runs before its pool is torn down and respawned, so a
              # per-trial NetSquid leak (sim_reset() not fully releasing state)
              # can't accumulate across an entire N/protocol call unbounded.


def _bb84_pair_task(args):
    i, j, fibre_len, runtimes, lenLoss, initLoss, detectorEffZ, darkCount, nodeLossDb, sourceErrRate, dephasingRate = args
    from BB84.BB84_run import _bb84_chunk
    kA, kB, kR, kQ = _bb84_chunk((
        runtimes, fibre_len, 0, 0.8, 1024, 1e7,
        lenLoss, initLoss, detectorEffZ, None,
        darkCount, nodeLossDb, sourceErrRate, dephasingRate,
    ))
    kL = [len(a) if a != "nan" else None for a in kA]
    return (i, j), kR, kQ, kL


def run_bb84_network(topo, cfg, runtimes=10, workers=None, verbose=False,
                     p2p_db_path=DEFAULT_DB_PATH, net_db_path=DEFAULT_DB_PATH,
                     experiment=None, seed=None, area_km=None, config_preset=None):
    """
    Run BB84 over all N(N-1)/2 direct pairs in topo.

    topo:     Topology (no relay_pos needed)
    cfg:      dict from load_config()
    runtimes: Monte Carlo runs per pair
    workers:  parallel worker processes — pairs run in parallel (default: 80% of CPU cores)

    Returns dict with per-pair results and network-level aggregates.
    """
    pairs   = topo.all_pairs()
    n_pairs = len(pairs)

    if verbose:
        print(f"BB84 network: {topo.N} users, {n_pairs} pairs")

    # Per-link tortuosity: one factor per cable (each BB84 pair has its own dedicated link)
    t_mean   = cfg.get("tortuosity_mean", 1.0)
    topo_rng = np.random.default_rng(seed)
    t_link   = _sample_link_tortuosity(topo_rng, t_mean, n_pairs)
    link_km  = [topo.bb84_link(i, j) * t_link[k] for k, (i, j) in enumerate(pairs)]

    n_workers = max(1, int(os.cpu_count() * 0.8)) if workers is None else workers
    n_workers = min(n_workers, n_pairs) if n_pairs > 0 else 1

    net_run_id    = new_run_id()
    run_timestamp = datetime.now().isoformat()

    # Run in rounds of <=_BATCH trials/pair, fresh pool per round: caps how many
    # trials any one worker executes before its pool is torn down and respawned,
    # bounding per-worker accumulation of any per-trial NetSquid leak instead of
    # letting one worker run the full `runtimes` count for many pairs unbounded.
    pair_rates = {(i, j): [] for (i, j) in pairs}
    pair_qbers = {(i, j): [] for (i, j) in pairs}
    pair_lens  = {(i, j): [] for (i, j) in pairs}

    remaining = runtimes
    while remaining > 0:
        batch = min(remaining, _BATCH)
        remaining -= batch

        tasks = [
            (i, j, link_km[k], batch,
             cfg["fibre_loss_db_per_km"], cfg["init_loss"], cfg["detector_efficiency"],
             cfg["dark_count_rate"], cfg["node_loss_db"], cfg["source_error_rate"], cfg["dephasing_rate"])
            for k, (i, j) in enumerate(pairs)
        ]
        with get_context('spawn').Pool(n_workers) as pool:
            raw = pool.map(_bb84_pair_task, tasks)

        for (i, j), kR, kQ, kL in raw:
            pair_rates[(i, j)].extend(kR)
            pair_qbers[(i, j)].extend(kQ)
            pair_lens[(i, j)].extend(kL)

    if verbose:
        for idx, (i, j) in enumerate(pairs):
            print(f"  [{idx+1}/{n_pairs}] pair ({i},{j}): {link_km[idx]:.2f} km")

    all_valid  = [r for rates in pair_rates.values() for r in rates if r != "nan"]
    total_runs = sum(len(rates) for rates in pair_rates.values())

    pair_distances    = link_km
    avg_pair_dist     = sum(pair_distances) / len(pair_distances) if pair_distances else 0.0
    avg_key_rate      = sum(all_valid) / len(all_valid) if all_valid else 0.0
    std_key_rate      = statistics.stdev(all_valid) if len(all_valid) > 1 else 0.0
    success_rate      = len(all_valid) / total_runs if total_runs else 0.0

    if p2p_db_path is not None or net_db_path is not None:
        db_path = p2p_db_path or net_db_path
        conn = init_db(db_path)

        if p2p_db_path is not None:
            for k, (i, j) in enumerate(pairs):
                params = {
                    "protocol": "BB84", "fibre_len": link_km[k], "photon_count": 1024,
                    "source_freq": 1e7, "q_speed": 0.8, "q_delay": 0,
                    "len_loss": cfg["fibre_loss_db_per_km"], "init_loss": cfg["init_loss"],
                    "detector_eff_z": cfg["detector_efficiency"],
                    "dark_count": cfg["dark_count_rate"], "node_loss_db": cfg["node_loss_db"],
                    "source_err_rate": cfg["source_error_rate"], "dephasing_rate": cfg["dephasing_rate"],
                    "runtimes": runtimes,
                }
                insert_p2p_rows(conn, new_run_id(), run_timestamp, params,
                                pair_lens[(i, j)], pair_rates[(i, j)], pair_qbers[(i, j)],
                                net_run_id=net_run_id)

        if net_db_path is not None:
            insert_network_row(
                conn, net_run_id, run_timestamp, experiment, "BB84",
                topo.N, None, area_km, seed, runtimes, config_preset,
                n_pairs, sum(pair_distances), avg_pair_dist, None,
                avg_key_rate, std_key_rate, success_rate,
                min(all_valid) if all_valid else 0.0,
                max(all_valid) if all_valid else 0.0,
            )

        conn.close()

    return {
        "pair_rates":     pair_rates,
        "pair_qbers":     pair_qbers,
        "avg_key_rate":   avg_key_rate,
        "success_rate":   success_rate,
        "min_key_rate":   min(all_valid) if all_valid else 0.0,
        "max_key_rate":   max(all_valid) if all_valid else 0.0,
        "total_fibre_km": sum(pair_distances),
        "n_links":        n_pairs,
        "n_sources":      topo.N,
        "n_spd":          2 * topo.N,
        "net_run_id":     net_run_id,
    }
