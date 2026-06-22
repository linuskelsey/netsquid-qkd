"""
Experiment 1 — relay count sweep.

Fixed N users, vary relay count K. Plots average key rate vs K for BB84 and MDI-QKD.
Error bars show std across Monte Carlo runs (--seeds 1) or across random topologies (--seeds N).
Topology visualisation only produced when --seeds 1.

Usage:
    python scripts/network/relay_sweep.py [options]

Options:
    --n INT          Number of users (default: 20)
    --k-min INT      Min relay count (default: 1)
    --k-max INT      Max relay count (default: 8)
    --area FLOAT     Area side length in km (default: 10.0)
    --seed INT       Base random seed; random if omitted
    --seeds INT      Random topologies to average over (default: 1)
    --runtimes INT   Monte Carlo runs per pair (default: 20)
    --config PATH    JSON config preset
    --error          Error style: bars (default) or shade
    --workers INT    Worker processes (default: 80% of CPU cores)
    --save PATH      Save figure to file instead of displaying

Examples:
    python scripts/network/relay_sweep.py --n 20 --k-max 6 --runtimes 20
    python scripts/network/relay_sweep.py --seeds 5 --seed 42 --save results/relay.png
"""
import argparse
import sys
import os
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
    """Mean key rate per pair (valid runs only). Returns list over pairs."""
    avgs = []
    for rates in pair_rates.values():
        valid = [r for r in rates if r != "nan"]
        if valid:
            avgs.append(sum(valid) / len(valid))
    return avgs


def main():
    parser = argparse.ArgumentParser(description="Relay count sweep (Experiment 1)")
    parser.add_argument("--n",        type=int,   default=20,   help="Number of users (fixed)")
    parser.add_argument("--k-min",    type=int,   default=1,    help="Min relay count")
    parser.add_argument("--k-max",    type=int,   default=8,    help="Max relay count")
    parser.add_argument("--area",     type=float, default=10.0, help="Area side length (km)")
    parser.add_argument("--seed",     type=int,   default=None, help="Base random seed (random if omitted)")
    parser.add_argument("--seeds",    type=int,   default=1,    help="Number of random topologies to average over")
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
    K_values = list(range(args.k_min, args.k_max + 1))

    if args.seeds == 1:
        seeds = [args.seed]
    else:
        rng   = np.random.default_rng(args.seed)
        seeds = rng.integers(0, 100_000, size=args.seeds).tolist()

    bb84_per_seed    = []
    bb84_ok_per_seed = []
    mdi_per_seed     = {K: [] for K in K_values}
    mdi_ok_per_seed  = {K: [] for K in K_values}

    for s_idx, seed in enumerate(seeds):
        print(f"\n--- Seed {s_idx + 1}/{args.seeds}  (seed={seed}) ---")
        user_pos = place_users(args.n, area_km=args.area, seed=seed)

        print("  Running BB84 (relay-independent)...")
        topo_bb84  = Topology(user_pos)
        bb84_res   = run_bb84_network(topo_bb84, cfg, runtimes=args.runtimes, workers=args.workers)
        bp         = _pair_avgs(bb84_res["pair_rates"])
        _s_bb84    = np.mean(bp) if bp else 0.0
        _s_bb84_ok = bb84_res["success_rate"] * 100
        bb84_per_seed.append(_s_bb84)
        bb84_ok_per_seed.append(_s_bb84_ok)

        for K in K_values:
            relay_pos  = optimise_relays(user_pos, K, seed=seed)
            topo       = Topology(user_pos, relay_pos)
            mdi_res    = run_mdi_network(topo, cfg, runtimes=args.runtimes, workers=args.workers)
            mp         = _pair_avgs(mdi_res["pair_rates"])
            _s_mdi     = np.mean(mp) if mp else 0.0
            _s_mdi_ok  = mdi_res["success_rate"] * 100
            mdi_per_seed[K].append(_s_mdi)
            mdi_ok_per_seed[K].append(_s_mdi_ok)

            print(f"  K={K:2d}  BB84 {_s_bb84:.1f} bps ({_s_bb84_ok:.1f}% ok) | "
                  f"MDI {_s_mdi:.1f} bps ({_s_mdi_ok:.1f}% ok)")

    bb84_means = [np.mean(bb84_per_seed)] * len(K_values)
    bb84_stds  = [np.std(bb84_per_seed)]  * len(K_values)
    bb84_ok    = [np.mean(bb84_ok_per_seed)] * len(K_values)

    mdi_means = [np.mean(mdi_per_seed[K])    for K in K_values]
    mdi_stds  = [np.std(mdi_per_seed[K])     for K in K_values]
    mdi_ok    = [np.mean(mdi_ok_per_seed[K]) for K in K_values]

    K_arr  = np.array(K_values)
    b_mean = np.array(bb84_means) / 1000   # bps → kbps
    b_std  = np.array(bb84_stds)  / 1000
    m_mean = np.array(mdi_means)  / 1000
    m_std  = np.array(mdi_stds)   / 1000

    bb84_ref = b_mean[0] if b_mean[0] > 0 else 1.0  # normalise relative axis to BB84

    # --- Figure 1: results ---
    fig, ax1 = plt.subplots(figsize=(8, 5))

    # BB84 — always dotted, no markers, shaded error
    ax1.plot(K_arr, b_mean, '--', color="#377eb8", lw=1.5, label="BB84")
    ax1.fill_between(K_arr, b_mean - b_std, b_mean + b_std, alpha=0.2, color="#377eb8")

    # MDI — solid with markers, error controlled by --error flag
    if args.error == "bars":
        ax1.errorbar(K_arr, m_mean, yerr=m_std, label="MDI", color="#e41a1c",
                     marker="o", capsize=4, lw=1.5)
    else:
        ax1.plot(K_arr, m_mean, color="#e41a1c", marker="o", lw=1.5, label="MDI")
        ax1.fill_between(K_arr, m_mean - m_std, m_mean + m_std, alpha=0.2, color="#e41a1c")

    ax1.set_yscale("log")
    ax1.set_xlabel("Relay count K")
    ax1.set_ylabel("Avg key rate (kbps)")
    ax1.set_xticks(K_arr)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()
    ax2.plot(K_arr, b_mean / bb84_ref, alpha=0)
    ax2.plot(K_arr, m_mean / bb84_ref, alpha=0)
    ax2.set_ylabel("Relative key rate")
    ax2.set_yscale("log")

    seed_label = f"seed={args.seed}" if args.seeds == 1 else f"{args.seeds} seeds (base={args.seed})"
    plt.title(
        f"Key rate vs relay count  (N={args.n}, area={args.area}×{args.area} km, {seed_label})",
        fontsize=10
    )
    plt.tight_layout()

    if args.save:
        plt.savefig(args.save, dpi=150)
        print(f"Saved to {args.save}")
    else:
        plt.show()

    # --- Figure 2: topology at midpoint K (single seed only) ---
    if args.seeds == 1:
        K_mid      = K_values[len(K_values) // 2]
        topo_users = place_users(args.n, area_km=args.area, seed=seeds[0])
        topo_mid   = Topology(topo_users, optimise_relays(topo_users, K_mid, seed=seeds[0]))

        fig2, (axA, axB) = plt.subplots(1, 2, figsize=(12, 5))
        draw_mdi(axA, topo_mid)
        draw_bb84(axB, topo_mid)
        plt.suptitle(
            f"Network topology at K={K_mid}  (N={args.n}, {seed_label})",
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
