"""
Experiment 2 — user count sweep.

Fixed K relays (positions optimised at ref-N), vary user count N. Plots average key rate vs N
for BB84, MDI-QKD, and trusted-node BB84. Relay positions are re-optimised per seed when
--seeds > 1. Error bars show std across Monte Carlo runs (--seeds 1) or across random
topologies (--seeds N). Topology visualisation only produced when --seeds 1.

MDI and trusted-node BB84 share the same relay topology per N; BB84 uses a direct mesh.

Usage:
    python scripts/network/user_sweep.py [options]

Options:
    --k INT          Number of relays fixed for sweep (default: 3)
    --ref-n INT      N used to optimise relay positions (default: n-max)
    --n-min INT      Min user count (default: 4)
    --n-max INT      Max user count (default: 20)
    --n-step INT     User count step size (default: 2)
    --area FLOAT     Area side length in km (default: 10.0)
    --seed INT       Base random seed; random if omitted
    --seeds INT      Random topologies to average over (default: 1)
    --runtimes INT   Monte Carlo runs per pair (default: 20)
    --config PATH    JSON config preset
    --error          Error style: bars (default), shade (±1σ fill), or iqr (Q1/Q3 fill)
    --workers INT    Worker processes (default: 80% of CPU cores; use nproc in command line to see maximum)
    --output-dir DIR Save figures to directory instead of displaying
    --placement STR  User placement mode: random (default) or clustered
                     (clustered: each user drawn uniformly within the
                      Voronoi-aware catchment circle of a randomly chosen relay)

Examples:
    python scripts/network/user_sweep.py --k 3 --n-max 20 --runtimes 20
    python scripts/network/user_sweep.py --seeds 5 --seed 42 --output-dir results/
    python scripts/network/user_sweep.py --placement clustered --k 3 --n-max 20
"""
import argparse
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

_root    = os.path.join(os.path.dirname(__file__), "../..")
_network = os.path.join(_root, "network")
sys.path.insert(0, _root)
sys.path.insert(0, _network)

import time
from lib.functions import load_config
from lib.db import DEFAULT_DB_PATH, update_network_cost
from lib.progress import Progress
from topology import place_users, place_users_clustered, optimise_relays, Topology
from bb84_network import run_bb84_network
from mdi_network import run_mdi_network
from trusted_bb84_network import run_trusted_bb84_network
from visualise_network import draw_mdi, draw_bb84
from cost import component_counts, total_cost


def _pair_avgs(pair_rates):
    avgs = []
    for rates in pair_rates.values():
        valid = [r for r in rates if r != "nan"]
        if valid:
            avgs.append(sum(valid) / len(valid))
    return avgs


def main():
    parser = argparse.ArgumentParser(description="User count sweep (Experiment 2)")
    parser.add_argument("--k",        type=int,   default=3,    help="Number of relays (fixed)")
    parser.add_argument("--ref-n",    type=int,   default=None, help="N used to optimise relay positions (default: n-max)")
    parser.add_argument("--n-min",    type=int,   default=4,    help="Min user count")
    parser.add_argument("--n-max",    type=int,   default=20,   help="Max user count")
    parser.add_argument("--n-step",   type=int,   default=2,    help="User count step size")
    parser.add_argument("--area",     type=float, default=10.0, help="Area side length (km)")
    parser.add_argument("--seed",     type=int,   default=None, help="Base random seed (random if omitted)")
    parser.add_argument("--seeds",    type=int,   default=1,    help="Number of random topologies to average over")
    parser.add_argument("--runtimes", type=int,   default=20,   help="Monte Carlo runs per pair")
    parser.add_argument("--config",   type=str,   default=None, help="Path to JSON config")
    parser.add_argument("--error",     type=str,   default="bars", choices=["bars", "shade", "iqr"])
    parser.add_argument("--output-dir", type=str,   default=None, help="Directory to save figures into (skips interactive display)")
    parser.add_argument("--placement",  type=str,   default="random", choices=["random", "clustered"],
                        help="User placement mode: random (uniform grid) or clustered (Voronoi catchment areas)")
    parser.add_argument("--no-figure", action="store_true", help="Skip all figure output (no show, no save)")
    parser.add_argument("--no-p2p-db", action="store_true", help="Disable P2P DB writing")
    parser.add_argument("--no-net-db", action="store_true", help="Disable network DB writing")
    parser.add_argument("--workers",  type=int,   default=None, help="Worker processes (default: 80%% of CPU cores)")
    args = parser.parse_args()

    if args.seed is None:
        args.seed = int.from_bytes(os.urandom(4), "big") % 100000

    cfg      = load_config(args.config)
    N_values = list(range(args.n_min, args.n_max + 1, args.n_step))
    ref_n    = args.ref_n if args.ref_n is not None else args.n_max

    if args.seeds == 1:
        seeds = [args.seed]
    else:
        rng   = np.random.default_rng(args.seed)
        seeds = rng.integers(0, 100_000, size=args.seeds).tolist()

    bb84_per_seed        = {N: [] for N in N_values}
    mdi_per_seed         = {N: [] for N in N_values}
    trusted_per_seed     = {N: [] for N in N_values}
    bb84_ok_per_seed     = {N: [] for N in N_values}
    mdi_ok_per_seed      = {N: [] for N in N_values}
    trusted_ok_per_seed  = {N: [] for N in N_values}
    bb84_fibre_per_seed  = {N: [] for N in N_values}
    mdi_fibre_per_seed   = {N: [] for N in N_values}
    trusted_fibre_per_seed = {N: [] for N in N_values}

    seed_total  = len(N_values)
    total_start = time.time()

    for s_idx, seed in enumerate(seeds):
        print(f"\n--- Seed {s_idx+1}/{args.seeds}  (seed={seed}) ---")
        seed_start = time.time()
        prog = Progress(seed_total)
        step = 0
        ref_pos   = place_users(ref_n, area_km=args.area, seed=seed)
        relay_pos = optimise_relays(ref_pos, args.k, seed=seed)

        for N in N_values:
            if N < args.k:
                step += 1
                continue

            prog.update(step, f"User count: {N}/{N_values[-1]}  Both protocols running...")
            if args.placement == "clustered":
                user_pos = place_users_clustered(N, relay_pos, area_km=args.area, seed=seed + N)
            else:
                user_pos = place_users(N, area_km=args.area, seed=seed)
            topo_bb84 = Topology(user_pos)
            topo_mdi  = Topology(user_pos, relay_pos)

            bb84_res = run_bb84_network(topo_bb84, cfg, runtimes=args.runtimes, workers=args.workers,
                              p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                              net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                              experiment="user_sweep", seed=seed, area_km=args.area,
                              config_preset=args.config)
            mdi_res  = run_mdi_network(topo_mdi,  cfg, runtimes=args.runtimes, workers=args.workers,
                                       p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                                       net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                                       experiment="user_sweep", seed=seed, area_km=args.area,
                                       config_preset=args.config)
            trusted_res = run_trusted_bb84_network(topo_mdi, cfg, runtimes=args.runtimes, workers=args.workers,
                                       p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                                       net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                                       experiment="user_sweep", seed=seed, area_km=args.area,
                                       config_preset=args.config)

            bp = _pair_avgs(bb84_res["pair_rates"])
            mp = _pair_avgs(mdi_res["pair_rates"])
            tp = _pair_avgs(trusted_res["pair_rates"])

            bb84_per_seed[N].append(np.mean(bp) if bp else 0.0)
            mdi_per_seed[N].append(np.mean(mp)  if mp else 0.0)
            trusted_per_seed[N].append(np.mean(tp) if tp else 0.0)
            bb84_ok_per_seed[N].append(bb84_res["success_rate"] * 100)
            mdi_ok_per_seed[N].append(mdi_res["success_rate"] * 100)
            trusted_ok_per_seed[N].append(trusted_res["success_rate"] * 100)
            bb84_fibre_per_seed[N].append(bb84_res["total_fibre_km"])
            mdi_fibre_per_seed[N].append(mdi_res["total_fibre_km"])
            trusted_fibre_per_seed[N].append(trusted_res["total_fibre_km"])

            _det_eff  = cfg["detector_efficiency"]
            _db_path  = None if args.no_net_db else DEFAULT_DB_PATH
            _bc = total_cost(component_counts(N, 0,       "BB84"),        bb84_res["total_fibre_km"], _det_eff)
            _mc = total_cost(component_counts(N, args.k,  "MDI"),         mdi_res["total_fibre_km"],  _det_eff)
            _tc = total_cost(component_counts(N, args.k,  "trusted_BB84"),trusted_res["total_fibre_km"], _det_eff)
            update_network_cost(_db_path, bb84_res.get("net_run_id"),    _det_eff, _bc["hardware_gbp"], _bc["fibre_gbp"], _bc["total_gbp"])
            update_network_cost(_db_path, mdi_res.get("net_run_id"),     _det_eff, _mc["hardware_gbp"], _mc["fibre_gbp"], _mc["total_gbp"])
            update_network_cost(_db_path, trusted_res.get("net_run_id"), _det_eff, _tc["hardware_gbp"], _tc["fibre_gbp"], _tc["total_gbp"])

            step += 1
            prog.update(step, f"User count: {N}/{N_values[-1]}  BB84 {bb84_per_seed[N][-1]/1000:.2f} | MDI {mdi_per_seed[N][-1]/1000:.2f} | TBB84 {trusted_per_seed[N][-1]/1000:.2f} kbps")

        prog.stop()
        m, s = divmod(int(time.time() - seed_start), 60)
        print(f"✓ Seed {s_idx+1}/{args.seeds} complete  {m}m {s:02d}s")

    m, s = divmod(int(time.time() - total_start), 60)
    print(f"✓ complete  total {m}m {s:02d}s")

    N_arr_final    = [N for N in N_values if bb84_per_seed[N]]
    bb84_means     = [np.mean(bb84_per_seed[N])         for N in N_arr_final]
    bb84_stds      = [np.std(bb84_per_seed[N])          for N in N_arr_final]
    bb84_ok        = [np.mean(bb84_ok_per_seed[N])      for N in N_arr_final]
    bb84_fibre     = [np.mean(bb84_fibre_per_seed[N])   for N in N_arr_final]
    mdi_means      = [np.mean(mdi_per_seed[N])          for N in N_arr_final]
    mdi_stds       = [np.std(mdi_per_seed[N])           for N in N_arr_final]
    mdi_ok         = [np.mean(mdi_ok_per_seed[N])       for N in N_arr_final]
    mdi_fibre      = [np.mean(mdi_fibre_per_seed[N])    for N in N_arr_final]
    t_means        = [np.mean(trusted_per_seed[N])      for N in N_arr_final]
    t_stds         = [np.std(trusted_per_seed[N])       for N in N_arr_final]
    t_ok           = [np.mean(trusted_ok_per_seed[N])   for N in N_arr_final]
    t_fibre        = [np.mean(trusted_fibre_per_seed[N]) for N in N_arr_final]

    print(f"\n{'N':>3}  {'BB84 kbps':>10}  {'MDI kbps':>9}  {'TBB84 kbps':>11}  {'BB84 ok%':>9}  {'MDI ok%':>8}  {'TBB84 ok%':>10}  {'BB84 km':>8}  {'MDI km':>7}  {'TBB84 km':>9}")
    print("-" * 102)
    for N, b_r, m_r, t_r, b_ok, m_ok, t_ok_, b_km, m_km, t_km in zip(
            N_arr_final, bb84_means, mdi_means, t_means,
            bb84_ok, mdi_ok, t_ok, bb84_fibre, mdi_fibre, t_fibre):
        print(
            f"{N:>3}  {b_r/1000:>10.2f}  {m_r/1000:>9.2f}  {t_r/1000:>11.2f}  "
            f"{b_ok:>8.0f}%  {m_ok:>7.0f}%  {t_ok_:>9.0f}%  "
            f"{b_km:>8.1f}  {m_km:>7.1f}  {t_km:>9.1f}"
        )

    N_arr  = np.array(N_arr_final)
    b_mean = np.array(bb84_means) / 1000
    b_std  = np.array(bb84_stds)  / 1000
    b_q1   = np.array([np.percentile(bb84_per_seed[N], 25) for N in N_arr_final]) / 1000
    b_q3   = np.array([np.percentile(bb84_per_seed[N], 75) for N in N_arr_final]) / 1000
    m_mean = np.array(mdi_means)  / 1000
    m_std  = np.array(mdi_stds)   / 1000
    m_q1   = np.array([np.percentile(mdi_per_seed[N], 25) for N in N_arr_final]) / 1000
    m_q3   = np.array([np.percentile(mdi_per_seed[N], 75) for N in N_arr_final]) / 1000
    t_mean = np.array(t_means)    / 1000
    t_std  = np.array(t_stds)     / 1000
    t_q1   = np.array([np.percentile(trusted_per_seed[N], 25) for N in N_arr_final]) / 1000
    t_q3   = np.array([np.percentile(trusted_per_seed[N], 75) for N in N_arr_final]) / 1000

    bb84_ref = b_mean[0] if b_mean[0] > 0 else 1.0

    # --- Figure 1: key rate vs N ---
    fig, ax1 = plt.subplots(figsize=(8, 5))

    if args.error == "bars":
        ax1.errorbar(N_arr, b_mean, yerr=b_std, label="BB84", color="#377eb8",
                     linestyle="--", capsize=4, lw=1.5)
        ax1.errorbar(N_arr, m_mean, yerr=m_std, label="MDI", color="#e41a1c",
                     marker="o", capsize=4, lw=1.5)
        ax1.errorbar(N_arr, t_mean, yerr=t_std, label="Trusted BB84", color="#4daf4a",
                     marker="s", capsize=4, lw=1.5)
    elif args.error == "shade":
        ax1.plot(N_arr, b_mean, '--', color="#377eb8", lw=1.5, label="BB84")
        ax1.fill_between(N_arr, b_mean - b_std, b_mean + b_std, alpha=0.2, color="#377eb8")
        ax1.plot(N_arr, m_mean, color="#e41a1c", marker="o", lw=1.5, label="MDI")
        ax1.fill_between(N_arr, m_mean - m_std, m_mean + m_std, alpha=0.2, color="#e41a1c")
        ax1.plot(N_arr, t_mean, color="#4daf4a", marker="s", lw=1.5, label="Trusted BB84")
        ax1.fill_between(N_arr, t_mean - t_std, t_mean + t_std, alpha=0.2, color="#4daf4a")
    else:  # iqr
        ax1.plot(N_arr, b_mean, '--', color="#377eb8", lw=1.5, label="BB84")
        ax1.fill_between(N_arr, b_q1, b_q3, alpha=0.2, color="#377eb8")
        ax1.plot(N_arr, m_mean, color="#e41a1c", marker="o", lw=1.5, label="MDI")
        ax1.fill_between(N_arr, m_q1, m_q3, alpha=0.2, color="#e41a1c")
        ax1.plot(N_arr, t_mean, color="#4daf4a", marker="s", lw=1.5, label="Trusted BB84")
        ax1.fill_between(N_arr, t_q1, t_q3, alpha=0.2, color="#4daf4a")

    ax1.set_yscale("log")
    ax1.set_xlabel("User count N")
    ax1.set_ylabel("Avg key rate (kbps)")
    ax1.set_xticks(N_arr)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()
    ax2.plot(N_arr, b_mean / bb84_ref, alpha=0)
    ax2.plot(N_arr, m_mean / bb84_ref, alpha=0)
    ax2.plot(N_arr, t_mean / bb84_ref, alpha=0)
    ax2.set_ylabel("Relative key rate")
    ax2.set_yscale("log")

    seed_label = f"seed={args.seed}" if args.seeds == 1 else f"{args.seeds} seeds (base={args.seed})"
    plt.title(
        f"Key rate vs user count  (K={args.k}, area={args.area}×{args.area} km, {seed_label})",
        fontsize=10
    )
    plt.tight_layout()

    if not args.no_figure:
        if args.output_dir:
            os.makedirs(args.output_dir, exist_ok=True)
            fn = os.path.splitext(os.path.basename(__file__))[0] + ".png"
            save_path = os.path.join(args.output_dir, fn)
            plt.savefig(save_path, dpi=150, bbox_inches="tight")
            print(f"Saved to {save_path}")
        else:
            plt.show()

    # --- Figure 2: topology at midpoint N (single seed only) ---
    if args.seeds == 1 and not args.no_figure:
        N_mid      = N_arr_final[len(N_arr_final) // 2]
        ref_mid    = place_users(ref_n, area_km=args.area, seed=seeds[0])
        relay_mid  = optimise_relays(ref_mid, args.k, seed=seeds[0])
        if args.placement == "clustered":
            user_mid = place_users_clustered(N_mid, relay_mid, area_km=args.area, seed=seeds[0] + N_mid)
        else:
            user_mid = place_users(N_mid, area_km=args.area, seed=seeds[0])
        topo_mid   = Topology(user_mid, relay_mid)

        fig2, (axA, axB) = plt.subplots(1, 2, figsize=(12, 5))
        draw_mdi(axA, topo_mid)
        draw_bb84(axB, topo_mid)
        plt.suptitle(
            f"Network topology at N={N_mid}  (K={args.k}, {seed_label})",
            fontsize=11
        )
        plt.tight_layout()

        if args.output_dir:
            topo_fn = os.path.splitext(os.path.basename(__file__))[0] + "_topology.png"
            topo_save = os.path.join(args.output_dir, topo_fn)
            plt.savefig(topo_save, dpi=150, bbox_inches="tight")
            print(f"Topology saved to {topo_save}")
        else:
            plt.show()


if __name__ == "__main__":
    main()
