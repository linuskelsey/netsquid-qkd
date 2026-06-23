import sys
import os
from multiprocessing import get_context
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def _bb84_pair_task(args):
    i, j, fibre_len, runtimes, lenLoss, initLoss, detectorEffZ, darkCount, nodeLossDb, sourceErrRate, dephasingRate = args
    from BB84.BB84_run import _bb84_chunk
    kA, kB, kR, kQ = _bb84_chunk((
        runtimes, fibre_len, 0, 0.8, 1024, 1e7,
        lenLoss, initLoss, detectorEffZ, None,
        darkCount, nodeLossDb, sourceErrRate, dephasingRate,
    ))
    return (i, j), kR, kQ


def run_bb84_network(topo, cfg, runtimes=10, workers=None, verbose=False):
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

    with get_context('spawn').Pool(n_workers) as pool:
        raw = pool.map(_bb84_pair_task, tasks)

    pair_rates = {}
    pair_qbers = {}
    for (i, j), kR, kQ in raw:
        pair_rates[(i, j)] = kR
        pair_qbers[(i, j)] = kQ

    if verbose:
        for idx, (i, j) in enumerate(pairs):
            print(f"  [{idx+1}/{n_pairs}] pair ({i},{j}): {topo.bb84_link(i, j):.2f} km")

    all_valid  = [r for rates in pair_rates.values() for r in rates if r != "nan"]
    total_runs = sum(len(rates) for rates in pair_rates.values())

    return {
        "pair_rates":     pair_rates,
        "pair_qbers":     pair_qbers,
        "avg_key_rate":   sum(all_valid) / len(all_valid) if all_valid else 0.0,
        "success_rate":   len(all_valid) / total_runs     if total_runs else 0.0,
        "min_key_rate":   min(all_valid)                  if all_valid  else 0.0,
        "max_key_rate":   max(all_valid)                  if all_valid  else 0.0,
        "total_fibre_km": sum(topo.bb84_link(i, j) for i, j in pairs),
        "n_links":        n_pairs,
    }
