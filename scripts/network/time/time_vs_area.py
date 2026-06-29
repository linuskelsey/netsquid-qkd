"""
Timing study 2 — wall-clock time per pair vs geographic area.

Fixed user count; area side length swept from area-min to area-max. For each
area, times run_bb84_network and run_mdi_network and reports wall-clock time
divided by n_pairs. Secondary axis shows mean pair distance (km) to reveal
whether link length drives simulation cost.

Usage:
    python scripts/network/time/time_vs_area.py [options]

Options:
    --n INT          Fixed user count (default: 8)
    --k INT          Number of MDI relays (default: 3)
    --area-min FLOAT Min area side length in km (default: 5.0)
    --area-max FLOAT Max area side length in km (default: 50.0)
    --area-step FLOAT Step size in km (default: 5.0)
    --runtimes INT   Monte Carlo runs per pair (default: 5)
    --seeds INT      Random topologies to average over (default: 3)
    --seed INT       Base random seed (random if omitted)
    --config PATH    JSON config preset
    --workers INT    Worker processes (default: 80% of CPU cores)
    --save PATH      Save figure to file instead of displaying

Examples:
    python scripts/network/time/time_vs_area.py --n 8 --area-max 50
    python scripts/network/time/time_vs_area.py --seeds 5 --save results/time_area.png
"""
import argparse
import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt

_root    = os.path.join(os.path.dirname(__file__), "../../..")
_network = os.path.join(_root, "network")
sys.path.insert(0, _root)
sys.path.insert(0, _network)

from lib.functions import load_config
from lib.progress import Progress
from topology import place_users, optimise_relays, Topology
from bb84_network import run_bb84_network
from mdi_network import run_mdi_network


def _fmt(seconds):
    seconds = int(seconds)
    if seconds < 60:
        return f"{seconds}s"
    m, s = divmod(seconds, 60)
    if m < 60:
        return f"{m}m {s:02d}s"
    h, m = divmod(m, 60)
    return f"{h}h {m:02d}m {s:02d}s"


def _mean_pair_dist(topo):
    pairs = topo.all_pairs()
    if not pairs:
        return 0.0
    return np.mean([topo.bb84_link(i, j) for (i, j) in pairs])


def main():
    parser = argparse.ArgumentParser(description="Timing study: wall-clock per pair vs area")
    parser.add_argument("--n",         type=int,   default=8,    help="Fixed user count")
    parser.add_argument("--k",         type=int,   default=3,    help="Number of MDI relays")
    parser.add_argument("--area-min",  type=float, default=5.0,  help="Min area side length (km)")
    parser.add_argument("--area-max",  type=float, default=50.0, help="Max area side length (km)")
    parser.add_argument("--area-step", type=float, default=5.0,  help="Area step size (km)")
    parser.add_argument("--runtimes",  type=int,   default=5,    help="Monte Carlo runs per pair")
    parser.add_argument("--seeds",     type=int,   default=3,    help="Random topologies to average over")
    parser.add_argument("--seed",      type=int,   default=None, help="Base random seed (random if omitted)")
    parser.add_argument("--config",    type=str,   default=None, help="Path to JSON config")
    parser.add_argument("--workers",   type=int,   default=None, help="Worker processes (default: 80%% of CPU cores)")
    parser.add_argument("--save",      type=str,   default=None, help="Save figure to file instead of displaying")
    args = parser.parse_args()

    if args.seed is None:
        args.seed = int.from_bytes(os.urandom(4), "big") % 100_000

    cfg = load_config(args.config)
    K   = min(args.k, args.n - 1)
    if K < 1:
        print(f"ERROR: n={args.n} too small for k={args.k} relays (need n > k)")
        sys.exit(1)

    n_pairs    = args.n * (args.n - 1) // 2
    area_steps = int(round((args.area_max - args.area_min) / args.area_step)) + 1
    areas      = [round(args.area_min + i * args.area_step, 6) for i in range(area_steps)]
    n_workers_display = args.workers if args.workers is not None else max(1, int(os.cpu_count() * 0.8))

    rng   = np.random.default_rng(args.seed)
    seeds = rng.integers(0, 100_000, size=args.seeds).tolist()

    # per-seed timing storage: {area: [time_per_pair, ...]}
    bb84_tpp  = {a: [] for a in areas}
    mdi_tpp   = {a: [] for a in areas}
    mean_dist = {a: [] for a in areas}

    total_start = time.time()

    for s_idx, seed in enumerate(seeds):
        print(f"\n--- Seed {s_idx+1}/{args.seeds}  (seed={seed}) ---")
        seed_start = time.time()
        prog       = Progress(len(areas))
        step       = 0

        for area in areas:
            prog.update(step, f"area={area:.1f} km  building topology...")
            user_pos  = place_users(args.n, area_km=area, seed=seed)
            relay_pos = optimise_relays(user_pos, K, seed=seed)
            topo_bb84 = Topology(user_pos)
            topo_mdi  = Topology(user_pos, relay_pos)
            mean_dist[area].append(_mean_pair_dist(topo_bb84))

            # BB84
            prog.update(step, f"area={area:.1f} km  BB84 ({n_pairs} pairs)...")
            t0        = time.time()
            run_bb84_network(topo_bb84, cfg, runtimes=args.runtimes, workers=args.workers)
            bb84_wall = time.time() - t0
            bb84_tpp[area].append(bb84_wall / n_pairs)

            # MDI
            prog.update(step, f"area={area:.1f} km  MDI  ({n_pairs} pairs)...")
            t0       = time.time()
            run_mdi_network(topo_mdi, cfg, runtimes=args.runtimes, workers=args.workers)
            mdi_wall = time.time() - t0
            mdi_tpp[area].append(mdi_wall / n_pairs)

            step += 1
            prog.update(
                step,
                f"area={area:.1f} km  BB84 {bb84_tpp[area][-1]:.2f}s/pair"
                f"  MDI {mdi_tpp[area][-1]:.2f}s/pair",
            )

        prog.stop()
        m, s = divmod(int(time.time() - seed_start), 60)
        print(f"✓ Seed {s_idx+1}/{args.seeds} complete  {m}m {s:02d}s")

    m, s = divmod(int(time.time() - total_start), 60)
    print(f"✓ complete  total {m}m {s:02d}s")

    # ── Aggregate ─────────────────────────────────────────────────────────────
    area_arr  = np.array(areas)
    bb84_mean = np.array([np.mean(bb84_tpp[a]) for a in areas])
    bb84_std  = np.array([np.std(bb84_tpp[a])  for a in areas])
    mdi_mean  = np.array([np.mean(mdi_tpp[a])  for a in areas])
    mdi_std   = np.array([np.std(mdi_tpp[a])   for a in areas])
    dist_mean = np.array([np.mean(mean_dist[a]) for a in areas])

    # ── Summary table ─────────────────────────────────────────────────────────
    print(f"\n{'area (km)':>10}  {'mean dist (km)':>14}  {'BB84 s/pair':>12}  {'MDI s/pair':>12}")
    print("-" * 54)
    for i, a in enumerate(areas):
        print(f"{a:>10.1f}  {dist_mean[i]:>14.2f}  {bb84_mean[i]:>12.3f}  {mdi_mean[i]:>12.3f}")

    # ── Correlation check ─────────────────────────────────────────────────────
    bb84_corr = float(np.corrcoef(dist_mean, bb84_mean)[0, 1])
    mdi_corr  = float(np.corrcoef(dist_mean, mdi_mean)[0, 1])
    print(f"\nCorrelation (mean pair dist vs time/pair):  BB84 r={bb84_corr:.3f}  MDI r={mdi_corr:.3f}")
    if max(abs(bb84_corr), abs(mdi_corr)) < 0.3:
        print("  → Timing is largely distance-independent (spawn/overhead dominated)")
    else:
        print("  → Timing correlates with pair distance")

    # ── Plot ──────────────────────────────────────────────────────────────────
    fig, ax1 = plt.subplots(figsize=(8, 5))

    ax1.errorbar(area_arr, bb84_mean, yerr=bb84_std,
                 label="BB84", color="#377eb8", linestyle="--", capsize=4, lw=1.5, marker="s")
    ax1.errorbar(area_arr, mdi_mean, yerr=mdi_std,
                 label="MDI", color="#e41a1c", capsize=4, lw=1.5, marker="o")

    ax1.set_xlabel("Area side length (km)")
    ax1.set_ylabel("Wall-clock time per pair (s)")
    ax1.legend(loc="upper left")
    ax1.grid(True, alpha=0.3)
    ax1.set_xticks(areas[::2] if len(areas) > 6 else areas)

    # secondary axis: mean pair distance
    ax2 = ax1.twinx()
    ax2.plot(area_arr, dist_mean, color="gray", linestyle=":", lw=1.2, label="mean pair dist")
    ax2.set_ylabel("Mean pair distance (km)", color="gray")
    ax2.tick_params(axis="y", labelcolor="gray")
    ax2.legend(loc="upper right")

    plt.title(
        f"Wall-clock time per pair vs area\n"
        f"(N={args.n} users, K={K} relays, runtimes={args.runtimes}, "
        f"{args.seeds} seed{'s' if args.seeds>1 else ''}, {n_workers_display} workers)",
        fontsize=10,
    )
    plt.tight_layout()

    if args.save:
        plt.savefig(args.save, dpi=150)
        print(f"Saved to {args.save}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
