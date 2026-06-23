import sys
import os
from multiprocessing import get_context
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

SWITCH_LOSS_DB = 1.0  # insertion loss for cross-cluster passive optical router


def _mdi_fibre_cost(topo):
    """Total fibre deployed (km): N user-relay links + K(K-1)/2 relay-relay links."""
    user_relay_km = sum(
        float(np.linalg.norm(topo.user_pos[i] - topo.relay_pos[topo.user_relay[i]]))
        for i in range(topo.N)
    )
    relay_relay_km = sum(
        float(np.linalg.norm(topo.relay_pos[k1] - topo.relay_pos[k2]))
        for k1 in range(topo.K) for k2 in range(k1 + 1, topo.K)
    )
    return user_relay_km + relay_relay_km


def _mdi_pair_task(args):
    i, j, total_km, charlie_pos, runtimes, lenLoss, initLoss, detectorEffZ, darkCount, nodeLossDb, sourceErrRate, dephasingRate, bsEff = args
    from MDI.mdiRun import _mdi_chunk
    kA, kB, kR, kQ = _mdi_chunk((
        runtimes, total_km, 0, 0.8, 1024, 1e7,
        lenLoss, initLoss, detectorEffZ, None,
        darkCount, nodeLossDb, sourceErrRate, dephasingRate, bsEff, charlie_pos,
    ))
    return (i, j), kR, kQ


def run_mdi_network(topo, cfg, runtimes=10, workers=None, switch_loss_db=SWITCH_LOSS_DB, verbose=False):
    """
    Run MDI-QKD over all N(N-1)/2 pairs in topo.

    topo:           Topology with relay_pos set
    cfg:            dict from load_config()
    runtimes:       Monte Carlo runs per pair
    workers:        parallel worker processes — pairs run in parallel (default: 80% of CPU cores)
    switch_loss_db: extra node loss (dB) for cross-cluster pairs (passive optical router)

    Returns dict with per-pair results and network-level aggregates.
    """
    if topo.relay_pos is None:
        raise ValueError("MDI network requires relay positions in topology")

    pairs   = topo.all_pairs()
    n_pairs = len(pairs)

    if verbose:
        print(f"MDI network: {topo.N} users, {topo.K} relays, {n_pairs} pairs")

    n_workers = max(1, int(os.cpu_count() * 0.8)) if workers is None else workers
    n_workers = min(n_workers, n_pairs) if n_pairs > 0 else 1

    tasks = []
    for (i, j) in pairs:
        alice_km, bob_km, charlie_idx, cross_cluster = topo.mdi_link(i, j)
        total_km    = alice_km + bob_km
        charlie_pos = alice_km / total_km if total_km > 0 else 0.5
        node_loss   = cfg["node_loss_db"] + (switch_loss_db if cross_cluster else 0.0)
        tasks.append((
            i, j, total_km, charlie_pos, runtimes,
            cfg["fibre_loss_db_per_km"], cfg["init_loss"], cfg["detector_efficiency"],
            cfg["dark_count_rate"], node_loss, cfg["source_error_rate"],
            cfg["dephasing_rate"], cfg["bs_eff"],
        ))

    with get_context('spawn').Pool(n_workers) as pool:
        raw = pool.map(_mdi_pair_task, tasks)

    pair_rates = {}
    pair_qbers = {}
    for (i, j), kR, kQ in raw:
        pair_rates[(i, j)] = kR
        pair_qbers[(i, j)] = kQ

    if verbose:
        for idx, (i, j) in enumerate(pairs):
            alice_km, bob_km, charlie_idx, cross_cluster = topo.mdi_link(i, j)
            tag = " [cross]" if cross_cluster else ""
            print(f"  [{idx+1}/{n_pairs}] pair ({i},{j}): {alice_km+bob_km:.2f} km, charlie={charlie_idx}{tag}")

    all_valid  = [r for rates in pair_rates.values() for r in rates if r != "nan"]
    total_runs = sum(len(rates) for rates in pair_rates.values())

    return {
        "pair_rates":     pair_rates,
        "pair_qbers":     pair_qbers,
        "avg_key_rate":   sum(all_valid) / len(all_valid) if all_valid else 0.0,
        "success_rate":   len(all_valid) / total_runs     if total_runs else 0.0,
        "min_key_rate":   min(all_valid)                  if all_valid  else 0.0,
        "max_key_rate":   max(all_valid)                  if all_valid  else 0.0,
        "total_fibre_km": _mdi_fibre_cost(topo),
        "n_links":        topo.N + topo.K * (topo.K - 1) // 2,
    }
