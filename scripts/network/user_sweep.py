"""
Experiment 2 — user count sweep.

Fixed K relays (positions optimised at ref-N), vary user count N. Plots average key rate vs N
for BB84 and MDI-QKD. Relay positions are re-optimised per seed when --seeds > 1.
Error bars show std across Monte Carlo runs (--seeds 1) or across random topologies (--seeds N).
Topology visualisation only produced when --seeds 1.

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
    --error          Error style: bars (default) or shade
    --workers INT    Worker processes (default: 80% of CPU cores; use nproc in command line to see maximum)
    --save PATH      Save figure to file instead of displaying

Examples:
    python scripts/network/user_sweep.py --k 3 --n-max 20 --runtimes 20
    python scripts/network/user_sweep.py --seeds 5 --seed 42 --save results/user.png
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
from lib.db import DEFAULT_DB_PATH
from lib.progress import Progress
from topology import place_users, optimise_relays, Topology
from bb84_network import run_bb84_network
from mdi_network import run_mdi_network
from visualise_network import draw_mdi, draw_bb84


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
    parser.add_argument("--error",    type=str,   default="bars", choices=["bars", "shade"])
    parser.add_argument("--save",     type=str,   default=None, help="Save path for results figure")
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

    bb84_per_seed   = {N: [] for N in N_values}
    mdi_per_seed    = {N: [] for N in N_values}
    bb84_ok_per_seed  = {N: [] for N in N_values}
    mdi_ok_per_seed   = {N: [] for N in N_values}
    bb84_fibre_per_seed = {N: [] for N in N_values}
    mdi_fibre_per_seed  = {N: [] for N in N_values}

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
            user_pos  = place_users(N, area_km=args.area, seed=seed)
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

            bp = _pair_avgs(bb84_res["pair_rates"])
            mp = _pair_avgs(mdi_res["pair_rates"])

            bb84_per_seed[N].append(np.mean(bp) if bp else 0.0)
            mdi_per_seed[N].append(np.mean(mp)  if mp else 0.0)
            bb84_ok_per_seed[N].append(bb84_res["success_rate"] * 100)
            mdi_ok_per_seed[N].append(mdi_res["success_rate"] * 100)
            bb84_fibre_per_seed[N].append(bb84_res["total_fibre_km"])
            mdi_fibre_per_seed[N].append(mdi_res["total_fibre_km"])

            step += 1
            prog.update(step, f"User count: {N}/{N_values[-1]}  BB84 {bb84_per_seed[N][-1]/1000:.2f} | MDI {mdi_per_seed[N][-1]/1000:.2f} kbps")

        prog.stop()
        m, s = divmod(int(time.time() - seed_start), 60)
        print(f"✓ Seed {s_idx+1}/{args.seeds} complete  {m}m {s:02d}s")

    m, s = divmod(int(time.time() - total_start), 60)
    print(f"✓ complete  total {m}m {s:02d}s")

    N_arr_final = [N for N in N_values if bb84_per_seed[N]]
    bb84_means  = [np.mean(bb84_per_seed[N])      for N in N_arr_final]
    bb84_stds   = [np.std(bb84_per_seed[N])       for N in N_arr_final]
    bb84_ok     = [np.mean(bb84_ok_per_seed[N])   for N in N_arr_final]
    bb84_fibre  = [np.mean(bb84_fibre_per_seed[N]) for N in N_arr_final]
    mdi_means   = [np.mean(mdi_per_seed[N])       for N in N_arr_final]
    mdi_stds    = [np.std(mdi_per_seed[N])        for N in N_arr_final]
    mdi_ok      = [np.mean(mdi_ok_per_seed[N])    for N in N_arr_final]
    mdi_fibre   = [np.mean(mdi_fibre_per_seed[N]) for N in N_arr_final]

    N_arr  = np.array(N_arr_final)
    b_mean = np.array(bb84_means) / 1000
    b_std  = np.array(bb84_stds)  / 1000
    m_mean = np.array(mdi_means)  / 1000
    m_std  = np.array(mdi_stds)   / 1000

    bb84_ref = b_mean[0] if b_mean[0] > 0 else 1.0

    # --- Figure 1: key rate vs N ---
    fig, ax1 = plt.subplots(figsize=(8, 5))

    if args.error == "bars":
        ax1.errorbar(N_arr, b_mean, yerr=b_std, label="BB84", color="#377eb8",
                     linestyle="--", capsize=4, lw=1.5)
        ax1.errorbar(N_arr, m_mean, yerr=m_std, label="MDI", color="#e41a1c",
                     marker="o", capsize=4, lw=1.5)
    else:
        ax1.plot(N_arr, b_mean, '--', color="#377eb8", lw=1.5, label="BB84")
        ax1.fill_between(N_arr, b_mean - b_std, b_mean + b_std, alpha=0.2, color="#377eb8")
        ax1.plot(N_arr, m_mean, color="#e41a1c", marker="o", lw=1.5, label="MDI")
        ax1.fill_between(N_arr, m_mean - m_std, m_mean + m_std, alpha=0.2, color="#e41a1c")

    ax1.set_yscale("log")
    ax1.set_xlabel("User count N")
    ax1.set_ylabel("Avg key rate (kbps)")
    ax1.set_xticks(N_arr)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()
    ax2.plot(N_arr, b_mean / bb84_ref, alpha=0)
    ax2.plot(N_arr, m_mean / bb84_ref, alpha=0)
    ax2.set_ylabel("Relative key rate")
    ax2.set_yscale("log")

    seed_label = f"seed={args.seed}" if args.seeds == 1 else f"{args.seeds} seeds (base={args.seed})"
    plt.title(
        f"Key rate vs user count  (K={args.k}, area={args.area}×{args.area} km, {seed_label})",
        fontsize=10
    )
    plt.tight_layout()

    if args.save:
        plt.savefig(args.save, dpi=150)
        print(f"Saved to {args.save}")
    else:
        plt.show()

    # --- Figure 2: topology at midpoint N (single seed only) ---
    if args.seeds == 1:
        N_mid      = N_arr_final[len(N_arr_final) // 2]
        user_mid   = place_users(N_mid, area_km=args.area, seed=seeds[0])
        ref_mid    = place_users(ref_n, area_km=args.area, seed=seeds[0])
        topo_mid   = Topology(user_mid, optimise_relays(ref_mid, args.k, seed=seeds[0]))

        fig2, (axA, axB) = plt.subplots(1, 2, figsize=(12, 5))
        draw_mdi(axA, topo_mid)
        draw_bb84(axB, topo_mid)
        plt.suptitle(
            f"Network topology at N={N_mid}  (K={args.k}, {seed_label})",
            fontsize=11
        )
        plt.tight_layout()

        if args.save:
            topo_path = args.save.rsplit(".", 1)
            topo_save = f"{topo_path[0]}_topology.{topo_path[1]}"
            plt.savefig(topo_save, dpi=150)
            print(f"Topology saved to {topo_save}")
        else:
            plt.show()


if __name__ == "__main__":
    main()
