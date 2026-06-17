import sys
import os
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from MDI.mdiRun import run_mdi_sims

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


def run_mdi_network(topo, cfg, runtimes=10, workers=None, switch_loss_db=SWITCH_LOSS_DB):
    """
    Run MDI-QKD over all N(N-1)/2 pairs in topo.

    topo:           Topology with relay_pos set
    cfg:            dict from load_config()
    runtimes:       Monte Carlo runs per pair
    workers:        parallel workers per pair (default: 80% of CPU cores)
    switch_loss_db: extra node loss (dB) for cross-cluster pairs (passive optical router)

    Returns dict with per-pair results and network-level aggregates.
    """
    if topo.relay_pos is None:
        raise ValueError("MDI network requires relay positions in topology")

    pair_rates = {}
    pair_qbers = {}
    pairs   = topo.all_pairs()
    n_pairs = len(pairs)

    print(f"MDI network: {topo.N} users, {topo.K} relays, {n_pairs} pairs")

    for idx, (i, j) in enumerate(pairs):
        alice_km, bob_km, charlie_idx, cross_cluster = topo.mdi_link(i, j)
        total_km    = alice_km + bob_km
        charlie_pos = alice_km / total_km if total_km > 0 else 0.5
        node_loss   = cfg["node_loss_db"] + (switch_loss_db if cross_cluster else 0.0)

        _, _, rates, qbers = run_mdi_sims(
            runtimes     = runtimes,
            fibreLen     = total_km,
            charliePos   = charlie_pos,
            lenLoss      = cfg["fibre_loss_db_per_km"],
            initLoss     = cfg["init_loss"],
            detectorEffZ = cfg["detector_efficiency"],
            darkCount    = cfg["dark_count_rate"],
            nodeLossDb   = node_loss,
            sourceErrRate= cfg["source_error_rate"],
            dephasingRate= cfg["dephasing_rate"],
            bsEff        = cfg["bs_eff"],
            workers      = workers,
        )
        pair_rates[(i, j)] = rates
        pair_qbers[(i, j)] = qbers
        tag = " [cross]" if cross_cluster else ""
        print(f"  [{idx+1}/{n_pairs}] pair ({i},{j}): {total_km:.2f} km, charlie={charlie_idx}{tag}")

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
