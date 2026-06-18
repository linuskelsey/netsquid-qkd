"""
Experiment 2 — user count sweep.
Fixed K relays (positions optimised at ref-N), vary user count N.
Plots avg key rate vs N for BB84 and MDI-QKD.
Also saves a topology visualisation at the midpoint N.
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

from lib.functions import load_config
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
    parser.add_argument("--seed",     type=int,   default=None, help="Random seed (random if omitted)")
    parser.add_argument("--runtimes", type=int,   default=20,   help="Monte Carlo runs per pair")
    parser.add_argument("--config",   type=str,   default=None, help="Path to JSON config")
    parser.add_argument("--error",    type=str,   default="bars", choices=["bars", "shade"])
    parser.add_argument("--save",     type=str,   default=None, help="Save path for results figure")
    parser.add_argument("--workers",  type=int,   default=None, help="Worker processes (default: 80%% of CPU cores)")
    args = parser.parse_args()

    if args.seed is None:
        args.seed = int.from_bytes(os.urandom(4), "big") % 100000
        print(f"Seed: {args.seed}")

    cfg      = load_config(args.config)
    N_values = list(range(args.n_min, args.n_max + 1, args.n_step))
    ref_n    = args.ref_n if args.ref_n is not None else args.n_max

    # Optimise relay positions once at ref_n — fixed for entire sweep
    print(f"Optimising {args.k} relay positions at N={ref_n}...")
    ref_pos      = place_users(ref_n, area_km=args.area, seed=args.seed)
    relay_pos    = optimise_relays(ref_pos, args.k, seed=args.seed)

    bb84_means, bb84_stds, bb84_ok = [], [], []
    mdi_means,  mdi_stds,  mdi_ok  = [], [], []
    bb84_fibre, mdi_fibre          = [], []

    for N in N_values:
        if N < args.k:
            print(f"N={N} < K={args.k} — skipping (fewer users than relays)")
            continue

        user_pos  = place_users(N, area_km=args.area, seed=args.seed)
        topo_bb84 = Topology(user_pos)
        topo_mdi  = Topology(user_pos, relay_pos)

        bb84_res = run_bb84_network(topo_bb84, cfg, runtimes=args.runtimes, workers=args.workers)
        mdi_res  = run_mdi_network(topo_mdi,  cfg, runtimes=args.runtimes, workers=args.workers)

        bp = _pair_avgs(bb84_res["pair_rates"])
        mp = _pair_avgs(mdi_res["pair_rates"])

        bb84_means.append(np.mean(bp) if bp else 0.0)
        bb84_stds.append(np.std(bp)   if bp else 0.0)
        bb84_ok.append(bb84_res["success_rate"] * 100)
        bb84_fibre.append(bb84_res["total_fibre_km"])

        mdi_means.append(np.mean(mp)  if mp else 0.0)
        mdi_stds.append(np.std(mp)    if mp else 0.0)
        mdi_ok.append(mdi_res["success_rate"] * 100)
        mdi_fibre.append(mdi_res["total_fibre_km"])

        print(f"N={N:3d}  BB84 {bb84_means[-1]:.1f} bps ({bb84_ok[-1]:.1f}% ok, {bb84_fibre[-1]:.1f} km) | "
              f"MDI {mdi_means[-1]:.1f} bps ({mdi_ok[-1]:.1f}% ok, {mdi_fibre[-1]:.1f} km)")

    N_arr  = np.array(N_values)
    b_mean = np.array(bb84_means) / 1000
    b_std  = np.array(bb84_stds)  / 1000
    m_mean = np.array(mdi_means)  / 1000
    m_std  = np.array(mdi_stds)   / 1000

    bb84_ref = b_mean[0] if b_mean[0] > 0 else 1.0

    # --- Figure 1: key rate vs N ---
    fig, ax1 = plt.subplots(figsize=(8, 5))

    ax1.plot(N_arr, b_mean, '--', color="#377eb8", lw=1.5, label="BB84")
    ax1.fill_between(N_arr, b_mean - b_std, b_mean + b_std, alpha=0.2, color="#377eb8")

    if args.error == "bars":
        ax1.errorbar(N_arr, m_mean, yerr=m_std, label="MDI", color="#e41a1c",
                     marker="o", capsize=4, lw=1.5)
    else:
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

    plt.title(
        f"Key rate vs user count  (K={args.k}, area={args.area}×{args.area} km, seed={args.seed})",
        fontsize=10
    )
    plt.tight_layout()

    if args.save:
        plt.savefig(args.save, dpi=150)
        print(f"Saved to {args.save}")
    else:
        plt.show()

    # --- Figure 2: topology at midpoint N ---
    N_mid    = N_values[len(N_values) // 2]
    user_mid = place_users(N_mid, area_km=args.area, seed=args.seed)
    topo_mid = Topology(user_mid, relay_pos)

    fig2, (axA, axB) = plt.subplots(1, 2, figsize=(12, 5))
    draw_mdi(axA, topo_mid)
    draw_bb84(axB, topo_mid)
    plt.suptitle(
        f"Network topology at N={N_mid}  (K={args.k}, seed={args.seed})",
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
