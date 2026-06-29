"""
Timing study 1 — wall-clock time per pair per single sim vs user count.

Fixed geographic area; user count swept from n-min to n-max. For each N,
times run_bb84_network and run_mdi_network; reports wall-clock divided by
n_pairs * runtimes = time for one pair to complete one simulation run.
CPU utilisation is sampled at 250 ms intervals during each network call.
Secondary axis shows n_pairs to make O(N^2) scaling visible. Prints
extrapolated estimates for a single N=100 run and a 10-point relay sweep.

Usage:
    python scripts/network/time/time_vs_users.py [options]

Options:
    --n-min INT      Min user count (default: 4)
    --n-max INT      Max user count (default: 14)
    --n-step INT     Step size (default: 2)
    --area FLOAT     Fixed area side length in km (default: 10.0)
    --k INT          Number of MDI relays (default: 3)
    --runtimes INT   Monte Carlo runs per pair (default: 5)
    --seeds INT      Random topologies to average over (default: 3)
    --seed INT       Base random seed (random if omitted)
    --config PATH    JSON config preset
    --workers INT    Worker processes (default: 80% of CPU cores)
    --save PATH      Save figure to file instead of displaying

Examples:
    python scripts/network/time/time_vs_users.py --n-max 14 --seeds 3
    python scripts/network/time/time_vs_users.py --workers 1 --save results/time_users.png
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


def main():
    parser = argparse.ArgumentParser(description="Timing study: wall-clock per pair per sim vs user count")
    parser.add_argument("--n-min",    type=int,   default=4,    help="Min user count")
    parser.add_argument("--n-max",    type=int,   default=14,   help="Max user count")
    parser.add_argument("--n-step",   type=int,   default=2,    help="User count step size")
    parser.add_argument("--area",     type=float, default=10.0, help="Area side length (km)")
    parser.add_argument("--k",        type=int,   default=3,    help="Number of MDI relays")
    parser.add_argument("--runtimes", type=int,   default=5,    help="Monte Carlo runs per pair")
    parser.add_argument("--seeds",    type=int,   default=3,    help="Random topologies to average over")
    parser.add_argument("--seed",     type=int,   default=None, help="Base random seed (random if omitted)")
    parser.add_argument("--config",   type=str,   default=None, help="Path to JSON config")
    parser.add_argument("--workers",  type=int,   default=None, help="Worker processes (default: 80%% of CPU cores)")
    parser.add_argument("--save",     type=str,   default=None, help="Save figure to file instead of displaying")
    args = parser.parse_args()

    if args.seed is None:
        args.seed = int.from_bytes(os.urandom(4), "big") % 100_000

    cfg      = load_config(args.config)
    N_values = list(range(args.n_min, args.n_max + 1, args.n_step))
    n_workers_display = args.workers if args.workers is not None else max(1, int(os.cpu_count() * 0.8))

    rng   = np.random.default_rng(args.seed)
    seeds = rng.integers(0, 100_000, size=args.seeds).tolist()

    bb84_tpp = {N: [] for N in N_values}
    mdi_tpp  = {N: [] for N in N_values}
    bb84_cpu = {N: [] for N in N_values}
    mdi_cpu  = {N: [] for N in N_values}

    total_start = time.time()

    for s_idx, seed in enumerate(seeds):
        print(f"\n--- Seed {s_idx+1}/{args.seeds}  (seed={seed}) ---")
        seed_start = time.time()
        prog       = Progress(len(N_values))
        step       = 0

        for N in N_values:
            n_pairs = N * (N - 1) // 2
            K       = min(args.k, N - 1)

            prog.update(step, f"N={N}  building topology...")
            user_pos  = place_users(N, area_km=args.area, seed=seed)
            topo_bb84 = Topology(user_pos)

            prog.update(step, f"N={N}  BB84 ({n_pairs} pairs)...")
            _, bb84_wall, bb84_pct = _timed_run(
                run_bb84_network, topo_bb84, cfg,
                runtimes=args.runtimes, workers=args.workers,
            )
            bb84_tpp[N].append(bb84_wall / n_pairs / args.runtimes)
            bb84_cpu[N].append(bb84_pct)

            if N > K and K >= 1:
                relay_pos = optimise_relays(user_pos, K, seed=seed)
                topo_mdi  = Topology(user_pos, relay_pos)
                prog.update(step, f"N={N}  MDI  ({n_pairs} pairs)...")
                _, mdi_wall, mdi_pct = _timed_run(
                    run_mdi_network, topo_mdi, cfg,
                    runtimes=args.runtimes, workers=args.workers,
                )
                mdi_tpp[N].append(mdi_wall / n_pairs / args.runtimes)
                mdi_cpu[N].append(mdi_pct)

            step += 1
            prog.update(
                step,
                f"N={N}  BB84 {bb84_tpp[N][-1]:.3f}s/sim {bb84_cpu[N][-1]:.0f}%CPU"
                + (f"  MDI {mdi_tpp[N][-1]:.3f}s/sim {mdi_cpu[N][-1]:.0f}%CPU" if mdi_tpp[N] else ""),
            )

        prog.stop()
        m, s = divmod(int(time.time() - seed_start), 60)
        print(f"✓ Seed {s_idx+1}/{args.seeds} complete  {m}m {s:02d}s")

    m, s = divmod(int(time.time() - total_start), 60)
    print(f"✓ complete  total {m}m {s:02d}s")

    # ── Aggregate ─────────────────────────────────────────────────────────────
    N_bb84 = [N for N in N_values if bb84_tpp[N]]
    N_mdi  = [N for N in N_values if mdi_tpp[N]]

    bb84_mean     = np.array([np.mean(bb84_tpp[N]) for N in N_bb84])
    bb84_std      = np.array([np.std(bb84_tpp[N])  for N in N_bb84])
    bb84_cpu_mean = np.array([np.mean(bb84_cpu[N]) for N in N_bb84])
    bb84_cpu_std  = np.array([np.std(bb84_cpu[N])  for N in N_bb84])
    mdi_mean      = np.array([np.mean(mdi_tpp[N])  for N in N_mdi])
    mdi_std       = np.array([np.std(mdi_tpp[N])   for N in N_mdi])
    mdi_cpu_mean  = np.array([np.mean(mdi_cpu[N])  for N in N_mdi])
    mdi_cpu_std   = np.array([np.std(mdi_cpu[N])   for N in N_mdi])

    # ── Summary table ─────────────────────────────────────────────────────────
    print(f"\n{'N':>4}  {'pairs':>6}  {'BB84 s/sim':>11}  {'BB84 %CPU':>10}  {'MDI s/sim':>11}  {'MDI %CPU':>10}")
    print("-" * 60)
    for i, N in enumerate(N_bb84):
        if N in N_mdi:
            mi = N_mdi.index(N)
            mdi_str = f"{mdi_mean[mi]:>11.3f}  {mdi_cpu_mean[mi]:>10.1f}"
        else:
            mdi_str = f"{'n/a':>11}  {'n/a':>10}"
        print(f"{N:>4}  {N*(N-1)//2:>6}  {bb84_mean[i]:>11.3f}  {bb84_cpu_mean[i]:>10.1f}  {mdi_str}")

    # ── Extrapolation to N=100 ────────────────────────────────────────────────
    pairs_100 = 100 * 99 // 2   # 4950
    tpp_bb84  = float(np.mean(bb84_mean))
    tpp_mdi   = float(np.mean(mdi_mean)) if mdi_mean.size else tpp_bb84

    # one full network call at N=100 (all pairs × runtimes)
    one_bb84_seq = tpp_bb84 * pairs_100 * args.runtimes
    one_mdi_seq  = tpp_mdi  * pairs_100 * args.runtimes
    one_bb84_par = one_bb84_seq / n_workers_display
    one_mdi_par  = one_mdi_seq  / n_workers_display

    # 10-point relay sweep (10 K values, 1 seed)
    sweep_bb84_par = one_bb84_par * 10
    sweep_mdi_par  = one_mdi_par  * 10

    print(f"\n── Extrapolation: N=100, {pairs_100} pairs, {args.runtimes} runtimes/pair ──")
    print(f"  Single run  BB84: seq {_fmt(one_bb84_seq)}  par {_fmt(one_bb84_par)}  ({n_workers_display} workers)")
    print(f"  Single run  MDI:  seq {_fmt(one_mdi_seq)}  par {_fmt(one_mdi_par)}  ({n_workers_display} workers)")
    print(f"  10-pt sweep BB84: {_fmt(sweep_bb84_par)}  |  MDI: {_fmt(sweep_mdi_par)}  (parallel, 1 seed)")

    # ── Plot ──────────────────────────────────────────────────────────────────
    fig, (ax1, ax_cpu) = plt.subplots(
        2, 1, figsize=(8, 7), sharex=True,
        gridspec_kw={"height_ratios": [3, 1.5]},
    )
    fig.subplots_adjust(hspace=0.08)
    fig.suptitle(
        f"Wall-clock time per pair per sim vs user count\n"
        f"(area={args.area}×{args.area} km, runtimes={args.runtimes}, "
        f"{args.seeds} seed{'s' if args.seeds > 1 else ''}, {n_workers_display} workers)",
        fontsize=10,
    )

    ax1.errorbar(N_bb84, bb84_mean, yerr=bb84_std,
                 label="BB84", color="#377eb8", linestyle="--", capsize=4, lw=1.5, marker="s")
    if N_mdi:
        ax1.errorbar(N_mdi, mdi_mean, yerr=mdi_std,
                     label="MDI", color="#e41a1c", capsize=4, lw=1.5, marker="o")
    ax1.set_ylabel("Wall-clock per pair per sim (s)")
    ax1.legend(loc="upper left")
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()
    n_pairs_arr = [N * (N - 1) // 2 for N in N_bb84]
    ax2.plot(N_bb84, n_pairs_arr, color="gray", linestyle=":", lw=1.2, label="N(N−1)/2 pairs")
    ax2.set_ylabel("Number of pairs  N(N−1)/2", color="gray")
    ax2.tick_params(axis="y", labelcolor="gray")
    ax2.legend(loc="upper right")

    ax_cpu.errorbar(N_bb84, bb84_cpu_mean, yerr=bb84_cpu_std,
                    label="BB84", color="#377eb8", linestyle="--", capsize=4, lw=1.5, marker="s")
    if N_mdi:
        ax_cpu.errorbar(N_mdi, mdi_cpu_mean, yerr=mdi_cpu_std,
                        label="MDI", color="#e41a1c", capsize=4, lw=1.5, marker="o")
    ax_cpu.axhline(100, color="gray", linestyle=":", lw=1.0)
    ax_cpu.set_ylabel("Avg CPU util. (%)")
    ax_cpu.set_xlabel("User count N")
    ax_cpu.set_ylim(0, 110)
    ax_cpu.set_xticks(N_values)
    ax_cpu.grid(True, alpha=0.3)
    ax_cpu.legend(loc="lower right", fontsize=8)

    if args.save:
        plt.savefig(args.save, dpi=150, bbox_inches="tight")
        print(f"Saved to {args.save}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
