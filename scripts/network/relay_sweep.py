"""
Experiment 1 — relay count sweep.
Fixed N users, vary K relays. Plots avg key rate and success rate vs K for BB84 and MDI-QKD.
Also saves a topology visualisation at the midpoint K.
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
    parser.add_argument("--seed",     type=int,   default=None, help="Random seed (random if omitted)")
    parser.add_argument("--runtimes", type=int,   default=20,   help="Monte Carlo runs per pair")
    parser.add_argument("--config",   type=str,   default=None, help="Path to JSON config")
    parser.add_argument("--error",    type=str,   default="bars", choices=["bars", "shade"])
    parser.add_argument("--save",     type=str,   default=None, help="Save path for results figure")
    args = parser.parse_args()

    if args.seed is None:
        args.seed = int(np.random.randint(0, 100000))
        print(f"Seed: {args.seed}")

    cfg      = load_config(args.config)
    user_pos = place_users(args.n, area_km=args.area, seed=args.seed)
    K_values = list(range(args.k_min, args.k_max + 1))

    # BB84 is independent of relay count — run once and reuse
    print("Running BB84 (once, relay-independent)...")
    topo_bb84 = Topology(user_pos)
    bb84_res  = run_bb84_network(topo_bb84, cfg, runtimes=args.runtimes)
    bp        = _pair_avgs(bb84_res["pair_rates"])
    _bb84_mean = np.mean(bp) if bp else 0.0
    _bb84_std  = np.std(bp)  if bp else 0.0
    _bb84_ok   = bb84_res["success_rate"] * 100

    bb84_means = [_bb84_mean] * len(K_values)
    bb84_stds  = [_bb84_std]  * len(K_values)
    bb84_ok    = [_bb84_ok]   * len(K_values)

    mdi_means, mdi_stds, mdi_ok = [], [], []

    for K in K_values:
        relay_pos = optimise_relays(user_pos, K, seed=args.seed)
        topo      = Topology(user_pos, relay_pos)
        mdi_res   = run_mdi_network(topo, cfg, runtimes=args.runtimes)
        mp        = _pair_avgs(mdi_res["pair_rates"])

        mdi_means.append(np.mean(mp) if mp else 0.0)
        mdi_stds.append(np.std(mp)   if mp else 0.0)
        mdi_ok.append(mdi_res["success_rate"] * 100)

        print(f"K={K:2d}  BB84 {_bb84_mean:.1f} bps ({_bb84_ok:.1f}% ok) | "
              f"MDI {mdi_means[-1]:.1f} bps ({mdi_ok[-1]:.1f}% ok)")

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

    plt.title(
        f"Key rate vs relay count  (N={args.n}, area={args.area}×{args.area} km, seed={args.seed})",
        fontsize=10
    )
    plt.tight_layout()

    if args.save:
        plt.savefig(args.save, dpi=150)
        print(f"Saved to {args.save}")
    else:
        plt.show()

    # --- Figure 2: topology at midpoint K ---
    K_mid     = K_values[len(K_values) // 2]
    topo_mid  = Topology(user_pos, optimise_relays(user_pos, K_mid, seed=args.seed))

    fig2, (axA, axB) = plt.subplots(1, 2, figsize=(12, 5))
    draw_mdi(axA, topo_mid)
    draw_bb84(axB, topo_mid)
    plt.suptitle(
        f"Network topology at K={K_mid}  (N={args.n}, seed={args.seed})",
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
