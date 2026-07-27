import os
import statistics
from collections import defaultdict
from datetime import datetime
from multiprocessing import get_context

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from lib.db import init_db, insert_p2p_rows, insert_network_row, new_run_id, DEFAULT_DB_PATH


def _dist(a, b):
    import numpy as np
    return float(np.linalg.norm(a - b))


def _link_task(args):
    """
    Run runtimes BB84 simulations for one link (user→relay or relay→relay).
    Returns (link_id, kR, kQ, kL).
    """
    link_id, fibre_len, runtimes, lenLoss, initLoss, detEff, darkCount, nodeLoss, srcErr, deph = args
    from BB84.BB84_run import _bb84_chunk
    kA, kB, kR, kQ = _bb84_chunk((
        runtimes, fibre_len, 0, 0.8, 1024, 1e7,
        lenLoss, initLoss, detEff, None,
        darkCount, nodeLoss, srcErr, deph,
    ))
    kL = [len(a) if a != "nan" else None for a in kA]
    return link_id, kR, kQ, kL


def run_trusted_bb84_network(topo, cfg, runtimes=10, workers=None, verbose=False,
                              p2p_db_path=DEFAULT_DB_PATH, net_db_path=DEFAULT_DB_PATH,
                              experiment=None, seed=None, area_km=None, config_preset=None):
    """
    Trusted-node BB84 network over the same relay topology as MDI-QKD.

    Each user runs BB84 with their assigned relay. Cross-relay pairs additionally
    use the relay-relay backbone link. End-to-end pair rate = min of constituent
    link rates, with backbone rate divided by the number of cross-relay pairs
    sharing that backbone link (option B: realistic key dilution).

    p2p_results rows are written for user-relay links only (N rows).
    network_results row written with protocol "trusted_BB84".

    Returns dict with same keys as run_bb84_network / run_mdi_network.
    """
    N, K  = topo.N, topo.K
    pairs = topo.all_pairs()
    n_pairs = len(pairs)

    link_params = (
        cfg["fibre_loss_db_per_km"], cfg["init_loss"], cfg["detector_efficiency"],
        cfg["dark_count_rate"], cfg["node_loss_db"], cfg["source_error_rate"], cfg["dephasing_rate"],
    )

    # Build tasks: user-relay links first, then backbone links
    tasks = []
    for i in range(N):
        ri   = int(topo.user_relay[i])
        dist = _dist(topo.user_pos[i], topo.relay_pos[ri])
        tasks.append((("u", i), dist, runtimes) + link_params)
    for j in range(K):
        for k in range(j + 1, K):
            dist = _dist(topo.relay_pos[j], topo.relay_pos[k])
            tasks.append((("b", j, k), dist, runtimes) + link_params)

    n_links   = len(tasks)
    n_workers = max(1, int(os.cpu_count() * 0.8)) if workers is None else workers
    n_workers = min(n_workers, n_links) if n_links > 0 else 1

    net_run_id    = new_run_id()
    run_timestamp = datetime.now().isoformat()

    with get_context('spawn').Pool(n_workers) as pool:
        raw = pool.map(_link_task, tasks)

    # Parse link results
    user_rates = {}  # i → mean rate (bps)
    user_raw   = {}  # i → (kR, kQ, kL) for DB
    bb_rates   = {}  # (j,k) → mean rate (bps)

    for link_id, kR, kQ, kL in raw:
        valid = [r for r in kR if r != "nan"]
        mean  = sum(valid) / len(valid) if valid else 0.0
        if link_id[0] == "u":
            user_rates[link_id[1]]            = mean
            user_raw[link_id[1]]              = (kR, kQ, kL)
        else:
            bb_rates[(link_id[1], link_id[2])] = mean

    # Count cross-relay pairs sharing each backbone link
    cross_count = defaultdict(int)
    for (i, l) in pairs:
        ri, rl = int(topo.user_relay[i]), int(topo.user_relay[l])
        if ri != rl:
            cross_count[(min(ri, rl), max(ri, rl))] += 1

    # End-to-end rate per pair
    pair_rates = {}
    for (i, l) in pairs:
        ri, rl = int(topo.user_relay[i]), int(topo.user_relay[l])
        if ri == rl:
            rate = min(user_rates[i], user_rates[l])
        else:
            bb_key    = (min(ri, rl), max(ri, rl))
            bb_shared = bb_rates[bb_key] / cross_count[bb_key]
            rate      = min(user_rates[i], bb_shared, user_rates[l])
        pair_rates[(i, l)] = [rate] if rate > 0 else ["nan"]

    # Aggregate
    all_valid    = [r[0] for r in pair_rates.values() if r[0] != "nan"]
    avg_key_rate = sum(all_valid) / len(all_valid) if all_valid else 0.0
    std_key_rate = statistics.stdev(all_valid) if len(all_valid) > 1 else 0.0
    success_rate = len(all_valid) / n_pairs if n_pairs > 0 else 0.0

    # Fibre: N user-relay links + K(K-1)/2 backbone links
    user_relay_fibre = sum(_dist(topo.user_pos[i], topo.relay_pos[int(topo.user_relay[i])]) for i in range(N))
    backbone_fibre   = sum(_dist(topo.relay_pos[j], topo.relay_pos[k])
                           for j in range(K) for k in range(j + 1, K))
    total_fibre_km   = user_relay_fibre + backbone_fibre

    # Average chain length per pair (sum of link distances traversed)
    def _chain_km(i, l):
        ri, rl = int(topo.user_relay[i]), int(topo.user_relay[l])
        d_i = _dist(topo.user_pos[i], topo.relay_pos[ri])
        d_l = _dist(topo.user_pos[l], topo.relay_pos[rl])
        return d_i + d_l if ri == rl else d_i + _dist(topo.relay_pos[ri], topo.relay_pos[rl]) + d_l

    avg_pair_dist = sum(_chain_km(i, l) for (i, l) in pairs) / n_pairs if n_pairs > 0 else 0.0
    cross_ratio   = sum(1 for (i, l) in pairs
                        if int(topo.user_relay[i]) != int(topo.user_relay[l])) / n_pairs if n_pairs > 0 else 0.0

    # DB writes
    if p2p_db_path is not None or net_db_path is not None:
        conn = init_db(p2p_db_path or net_db_path)

        if p2p_db_path is not None:
            for i in range(N):
                ri   = int(topo.user_relay[i])
                dist = _dist(topo.user_pos[i], topo.relay_pos[ri])
                kR, kQ, kL = user_raw[i]
                params = {
                    "protocol": "BB84", "fibre_len": dist, "photon_count": 1024,
                    "source_freq": 1e7, "q_speed": 0.8, "q_delay": 0,
                    "len_loss": cfg["fibre_loss_db_per_km"], "init_loss": cfg["init_loss"],
                    "detector_eff_z": cfg["detector_efficiency"],
                    "dark_count": cfg["dark_count_rate"], "node_loss_db": cfg["node_loss_db"],
                    "source_err_rate": cfg["source_error_rate"], "dephasing_rate": cfg["dephasing_rate"],
                    "runtimes": runtimes,
                }
                insert_p2p_rows(conn, new_run_id(), run_timestamp, params, kL, kR, kQ,
                                net_run_id=net_run_id)

        if net_db_path is not None:
            insert_network_row(
                conn, net_run_id, run_timestamp, experiment, "trusted_BB84",
                topo.N, topo.K, area_km, seed, runtimes, config_preset,
                n_pairs, total_fibre_km, avg_pair_dist, cross_ratio,
                avg_key_rate, std_key_rate, success_rate,
                min(all_valid) if all_valid else 0.0,
                max(all_valid) if all_valid else 0.0,
            )

        conn.close()

    if verbose:
        print(f"trusted_BB84: {N} users, {K} relays, {n_links} links, "
              f"{avg_key_rate/1000:.2f} kbps avg, {success_rate*100:.0f}% ok")

    return {
        "pair_rates":     pair_rates,
        "avg_key_rate":   avg_key_rate,
        "success_rate":   success_rate,
        "min_key_rate":   min(all_valid) if all_valid else 0.0,
        "max_key_rate":   max(all_valid) if all_valid else 0.0,
        "total_fibre_km": total_fibre_km,
        "n_links":        n_links,
        "n_sources":      N + K,
        "n_spd":          2 * K,
        "net_run_id":     net_run_id,
    }
