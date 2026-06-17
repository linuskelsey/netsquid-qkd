import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from BB84.BB84_run import run_BB84_sims


def run_bb84_network(topo, cfg, runtimes=10, workers=None):
    """
    Run BB84 over all N(N-1)/2 direct pairs in topo.

    topo:     Topology (no relay_pos needed)
    cfg:      dict from load_config()
    runtimes: Monte Carlo runs per pair
    workers:  parallel workers per pair (default: 80% of CPU cores)

    Returns dict with per-pair results and network-level aggregates.
    """
    pair_rates = {}
    pair_qbers = {}
    pairs  = topo.all_pairs()
    n_pairs = len(pairs)

    print(f"BB84 network: {topo.N} users, {n_pairs} pairs")

    for idx, (i, j) in enumerate(pairs):
        fibre_len = topo.bb84_link(i, j)
        _, _, rates, qbers = run_BB84_sims(
            runtimes     = runtimes,
            fibreLen     = fibre_len,
            lenLoss      = cfg["fibre_loss_db_per_km"],
            initLoss     = cfg["init_loss"],
            detectorEffZ = cfg["detector_efficiency"],
            darkCount    = cfg["dark_count_rate"],
            nodeLossDb   = cfg["node_loss_db"],
            sourceErrRate= cfg["source_error_rate"],
            dephasingRate= cfg["dephasing_rate"],
            workers      = workers,
        )
        pair_rates[(i, j)] = rates
        pair_qbers[(i, j)] = qbers
        print(f"  [{idx+1}/{n_pairs}] pair ({i},{j}): {fibre_len:.2f} km")

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
