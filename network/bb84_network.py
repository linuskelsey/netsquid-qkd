import sys
import os
import statistics
from multiprocessing import get_context
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from lib.db import init_db, insert_p2p_rows, insert_network_row, new_run_id, DEFAULT_DB_PATH


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

    n_workers = max(1, int(os.cpu_count() * 0.8)) if workers is None else workers
    n_workers = min(n_workers, n_pairs) if n_pairs > 0 else 1

    tasks = [
        (i, j, topo.bb84_link(i, j), runtimes,
         cfg["fibre_loss_db_per_km"], cfg["init_loss"], cfg["detector_efficiency"],
         cfg["dark_count_rate"], cfg["node_loss_db"], cfg["source_error_rate"], cfg["dephasing_rate"])
        for (i, j) in pairs
    ]

    net_run_id    = new_run_id()
    run_timestamp = datetime.now().isoformat()

    with get_context('spawn').Pool(n_workers) as pool:
        raw = pool.map(_bb84_pair_task, tasks)

    pair_rates = {}
    pair_qbers = {}
    for (i, j), kR, kQ, kL in raw:
        pair_rates[(i, j)] = kR
        pair_qbers[(i, j)] = kQ

    if verbose:
        for idx, (i, j) in enumerate(pairs):
            print(f"  [{idx+1}/{n_pairs}] pair ({i},{j}): {topo.bb84_link(i, j):.2f} km")

    all_valid  = [r for rates in pair_rates.values() for r in rates if r != "nan"]
    total_runs = sum(len(rates) for rates in pair_rates.values())

    pair_distances    = [topo.bb84_link(i, j) for (i, j) in pairs]
    avg_pair_dist     = sum(pair_distances) / len(pair_distances) if pair_distances else 0.0
    avg_key_rate      = sum(all_valid) / len(all_valid) if all_valid else 0.0
    std_key_rate      = statistics.stdev(all_valid) if len(all_valid) > 1 else 0.0
    success_rate      = len(all_valid) / total_runs if total_runs else 0.0

    if p2p_db_path is not None or net_db_path is not None:
        db_path = p2p_db_path or net_db_path
        conn = init_db(db_path)

        if p2p_db_path is not None:
            for task_args, (_, kR, kQ, kL) in zip(tasks, raw):
                _, _, fibre_len, _, lenLoss, initLoss, detEff, darkCount, nodeLoss, srcErr, deph = task_args
                params = {
                    "protocol": "BB84", "fibre_len": fibre_len, "photon_count": 1024,
                    "source_freq": 1e7, "q_speed": 0.8, "q_delay": 0,
                    "len_loss": lenLoss, "init_loss": initLoss, "detector_eff_z": detEff,
                    "dark_count": darkCount, "node_loss_db": nodeLoss,
                    "source_err_rate": srcErr, "dephasing_rate": deph, "runtimes": runtimes,
                }
                insert_p2p_rows(conn, new_run_id(), run_timestamp, params, kL, kR, kQ,
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
