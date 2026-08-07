"""
Timing study 2 — wall-clock time per pair per single sim vs geographic area.

Fixed user count; area side length swept from area-min to area-max. For each
area, times run_bb84_network and run_mdi_network; reports wall-clock divided by
n_pairs * runtimes = time for one pair to complete one simulation run. CPU
utilisation is sampled at 250 ms intervals during each network call. Secondary
axis shows mean pair distance (km) to reveal whether link length drives cost.

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
    --output-dir DIR Save figure bundle {plot.png, plot.tex, assumptions.md} to directory instead of displaying

Examples:
    python scripts/network/time/time_vs_area.py --n 8 --area-max 50
    python scripts/network/time/time_vs_area.py --seeds 5 --output-dir results/time_area
"""
import argparse
import os
import sys
import time
import threading
import numpy as np
import matplotlib.pyplot as plt
import psutil

_root    = os.path.join(os.path.dirname(__file__), "../../..")
_network = os.path.join(_root, "network")
sys.path.insert(0, _root)
sys.path.insert(0, _network)

from lib.plotting import apply_thesis_style, save_bundle
from lib.functions import load_config
from lib.progress import Progress
from topology import place_users, optimise_relays, Topology
from bb84_network import run_bb84_network
from mdi_network import run_mdi_network

apply_thesis_style()


def _fmt(seconds):
    seconds = int(seconds)
    if seconds < 60:
        return f"{seconds}s"
    m, s = divmod(seconds, 60)
    if m < 60:
        return f"{m}m {s:02d}s"
    h, m = divmod(m, 60)
    return f"{h}h {m:02d}m {s:02d}s"


def _timed_run(fn, *args, **kwargs):
    """Run fn(*args, **kwargs); return (result, wall_seconds, avg_cpu_pct)."""
    stop_ev = threading.Event()
    samples = []

    def _sample():
        while not stop_ev.is_set():
            samples.append(psutil.cpu_percent(interval=None))
            time.sleep(0.25)

    psutil.cpu_percent(interval=None)   # discard first reading (always 0.0)
    t = threading.Thread(target=_sample, daemon=True)
    t.start()
    t0     = time.time()
    result = fn(*args, **kwargs)
    wall   = time.time() - t0
    stop_ev.set()
    t.join()
    avg_cpu = float(np.mean(samples)) if samples else 0.0
    return result, wall, avg_cpu


def _mean_pair_dist(topo):
    pairs = topo.all_pairs()
    if not pairs:
        return 0.0
    return np.mean([topo.bb84_link(i, j) for (i, j) in pairs])


def main():
    parser = argparse.ArgumentParser(description="Timing study: wall-clock per pair per sim vs area")
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
    parser.add_argument("--output-dir", type=str,  default=None, help="Save figure bundle to directory instead of displaying")
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

    bb84_tpp  = {a: [] for a in areas}
    mdi_tpp   = {a: [] for a in areas}
    bb84_cpu  = {a: [] for a in areas}
    mdi_cpu   = {a: [] for a in areas}
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
            _, bb84_wall, bb84_pct = _timed_run(
                run_bb84_network, topo_bb84, cfg,
                runtimes=args.runtimes, workers=args.workers,
            )
            bb84_tpp[area].append(bb84_wall / n_pairs / args.runtimes)
            bb84_cpu[area].append(bb84_pct)

            # MDI
            prog.update(step, f"area={area:.1f} km  MDI  ({n_pairs} pairs)...")
            _, mdi_wall, mdi_pct = _timed_run(
                run_mdi_network, topo_mdi, cfg,
                runtimes=args.runtimes, workers=args.workers,
            )
            mdi_tpp[area].append(mdi_wall / n_pairs / args.runtimes)
            mdi_cpu[area].append(mdi_pct)

            step += 1
            prog.update(
                step,
                f"area={area:.1f} km  BB84 {bb84_tpp[area][-1]:.3f}s/sim {bb84_cpu[area][-1]:.0f}%CPU"
                f"  MDI {mdi_tpp[area][-1]:.3f}s/sim {mdi_cpu[area][-1]:.0f}%CPU",
            )

        prog.stop()
        m, s = divmod(int(time.time() - seed_start), 60)
        print(f"✓ Seed {s_idx+1}/{args.seeds} complete  {m}m {s:02d}s")

    m, s = divmod(int(time.time() - total_start), 60)
    print(f"✓ complete  total {m}m {s:02d}s")

    # ── Aggregate ─────────────────────────────────────────────────────────────
    area_arr      = np.array(areas)
    bb84_mean     = np.array([np.mean(bb84_tpp[a]) for a in areas])
    bb84_std      = np.array([np.std(bb84_tpp[a])  for a in areas])
    bb84_cpu_mean = np.array([np.mean(bb84_cpu[a]) for a in areas])
    bb84_cpu_std  = np.array([np.std(bb84_cpu[a])  for a in areas])
    mdi_mean      = np.array([np.mean(mdi_tpp[a])  for a in areas])
    mdi_std       = np.array([np.std(mdi_tpp[a])   for a in areas])
    mdi_cpu_mean  = np.array([np.mean(mdi_cpu[a])  for a in areas])
    mdi_cpu_std   = np.array([np.std(mdi_cpu[a])   for a in areas])
    dist_mean     = np.array([np.mean(mean_dist[a]) for a in areas])

    # ── Summary table ─────────────────────────────────────────────────────────
    print(f"\n{'area (km)':>10}  {'mean dist (km)':>14}  {'BB84 s/sim':>11}  {'BB84 %CPU':>10}  {'MDI s/sim':>11}  {'MDI %CPU':>10}")
    print("-" * 76)
    for i, a in enumerate(areas):
        print(f"{a:>10.1f}  {dist_mean[i]:>14.2f}  {bb84_mean[i]:>11.3f}  {bb84_cpu_mean[i]:>10.1f}  {mdi_mean[i]:>11.3f}  {mdi_cpu_mean[i]:>10.1f}")

    # ── Correlation check ─────────────────────────────────────────────────────
    bb84_corr = float(np.corrcoef(dist_mean, bb84_mean)[0, 1])
    mdi_corr  = float(np.corrcoef(dist_mean, mdi_mean)[0, 1])
    print(f"\nCorrelation (mean pair dist vs time/sim):  BB84 r={bb84_corr:.3f}  MDI r={mdi_corr:.3f}")
    if max(abs(bb84_corr), abs(mdi_corr)) < 0.3:
        print("  → Timing is largely distance-independent (spawn/overhead dominated)")
    else:
        print("  → Timing correlates with pair distance")

    # ── Extrapolation to N=100 ────────────────────────────────────────────────
    pairs_100      = 100 * 99 // 2   # 4950
    sweep_points   = 10              # data points per protocol (e.g. detector efficiency)
    sweep_seeds    = 10
    sweep_runtimes = 100             # runtimes/pair/seed → 1000 effective per data point

    tpp_bb84 = float(np.mean(bb84_mean))
    tpp_mdi  = float(np.mean(mdi_mean)) if mdi_mean.size else tpp_bb84

    # tpp already reflects parallel speedup (measured with n_workers_display workers)
    # true sequential = tpp × workers; true parallel = tpp × new_pairs × new_runtimes
    one_bb84_seq = tpp_bb84 * pairs_100 * args.runtimes * n_workers_display
    one_mdi_seq  = tpp_mdi  * pairs_100 * args.runtimes * n_workers_display
    one_bb84_par = tpp_bb84 * pairs_100 * args.runtimes
    one_mdi_par  = tpp_mdi  * pairs_100 * args.runtimes

    # device-param sweep: 10 pts × both protocols × 10 seeds × 100 runtimes
    bb84_pt_par = tpp_bb84 * pairs_100 * sweep_runtimes
    mdi_pt_par  = tpp_mdi  * pairs_100 * sweep_runtimes
    sweep_total = (bb84_pt_par + mdi_pt_par) * sweep_points * sweep_seeds

    print(f"\n── Extrapolation: N=100, {pairs_100} pairs ──")
    print(f"  Single run (×{args.runtimes} runtimes)  BB84: seq {_fmt(one_bb84_seq)}  par {_fmt(one_bb84_par)}  ({n_workers_display} workers)")
    print(f"  Single run (×{args.runtimes} runtimes)  MDI:  seq {_fmt(one_mdi_seq)}  par {_fmt(one_mdi_par)}  ({n_workers_display} workers)")
    print(f"\n── Device-param sweep  ({sweep_points} pts × both protocols × {sweep_seeds} seeds × {sweep_runtimes} runtimes = {sweep_runtimes * sweep_seeds} effective) ──")
    print(f"  BB84 per data point: {_fmt(bb84_pt_par)}  |  MDI per data point: {_fmt(mdi_pt_par)}  ({n_workers_display} workers)")
    print(f"  Total sweep:         {_fmt(sweep_total)}")

    # ── Plot ──────────────────────────────────────────────────────────────────
    fig, (ax1, ax_cpu) = plt.subplots(
        2, 1, figsize=(8, 7), sharex=True,
        gridspec_kw={"height_ratios": [3, 1.5]},
    )
    fig.subplots_adjust(hspace=0.08)
    title = "Wall-Clock Time vs Area"
    fig.suptitle(title, fontsize=10)

    ax1.errorbar(area_arr, bb84_mean, yerr=bb84_std,
                 label="BB84", color="#377eb8", linestyle="--", capsize=4, lw=1.5, marker="s")
    ax1.errorbar(area_arr, mdi_mean, yerr=mdi_std,
                 label="MDI", color="#e41a1c", capsize=4, lw=1.5, marker="o")
    ax1.set_ylabel("Wall-clock per pair per sim (s)")
    ax1.legend(loc="upper left")
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()
    ax2.plot(area_arr, dist_mean, color="gray", linestyle=":", lw=1.2, label="mean pair dist")
    ax2.set_ylabel("Mean pair distance (km)", color="gray")
    ax2.tick_params(axis="y", labelcolor="gray")
    ax2.legend(loc="upper right")

    ax_cpu.errorbar(area_arr, bb84_cpu_mean, yerr=bb84_cpu_std,
                    label="BB84", color="#377eb8", linestyle="--", capsize=4, lw=1.5, marker="s")
    ax_cpu.errorbar(area_arr, mdi_cpu_mean, yerr=mdi_cpu_std,
                    label="MDI", color="#e41a1c", capsize=4, lw=1.5, marker="o")
    ax_cpu.axhline(100, color="gray", linestyle=":", lw=1.0)
    ax_cpu.set_ylabel("Avg CPU util. (%)")
    ax_cpu.set_xlabel("Area side length (km)")
    ax_cpu.set_ylim(0, 110)
    ax_cpu.set_xticks(areas[::2] if len(areas) > 6 else areas)
    ax_cpu.grid(True, alpha=0.3)
    ax_cpu.legend(loc="lower right", fontsize=8)

    if args.output_dir:
        save_bundle(
            fig, args.output_dir, "time_vs_area",
            title=title,
            assumptions={
                "Fixed user count": args.n,
                "MDI relays": K,
                "Area sweep range": f"{args.area_min}-{args.area_max} km (step {args.area_step})",
                "Runtimes per pair": args.runtimes,
                "Random topologies averaged": args.seeds,
                "Workers": n_workers_display,
                "Mean pair-distance correlation (BB84)": f"r={bb84_corr:.3f}",
                "Mean pair-distance correlation (MDI)": f"r={mdi_corr:.3f}",
            },
            notes=["Top: wall-clock per pair per simulation vs area, with mean pair distance on secondary axis.",
                   "Bottom: average CPU utilisation vs area."],
        )
        print(f"Saved to {os.path.join(args.output_dir, 'time_vs_area')}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
