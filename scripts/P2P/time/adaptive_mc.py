"""
Adaptive Monte Carlo Benchmark
================================
Compares fixed-N Monte Carlo (baseline) against adaptive early stopping.

Strategy: run simulations in batches; after each batch check whether the
running mean key rate has converged (rel. std < threshold). Stop early in
the stable regime; allow full budget near the QBER cutoff where variance is
highest.

Outputs two plots:
  1. Runs used vs distance — shows where savings are made
  2. Relative error vs fixed baseline — shows accuracy cost of early stopping

Usage:
    python scripts/P2P/adaptive_mc.py [--max-runs INT] [--batch INT]
                                      [--rel-tol FLOAT] [--protocol STR]
                                      [--workers INT] [--output-dir DIR]

Examples:
    python scripts/P2P/adaptive_mc.py --protocol bb84 --output-dir docs/figures
    python scripts/P2P/adaptive_mc.py --max-runs 200 --batch 10 --rel-tol 0.08
"""

import os
import sys
import time
import argparse

import numpy as np
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from BB84.BB84_run import run_BB84_sims
from MDI.mdiRun import run_mdi_sims

# ── Sweep parameters ──────────────────────────────────────────────────────────
_DISTANCES = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Realistic defaults (layer 5 equivalent — same as network sims)
_FIXED = dict(
    qDelay=0, qSpeed=0.8, photonCount=1024, sourceFreq=1e7,
    lenLoss=0.2, initLoss=0.1, detectorEffZ=0.65, detectorEffX=0.85,
    darkCount=100, nodeLossDb=2.0, sourceErrRate=0.005, dephasingRate=3.2e-7,
    db_path=None,
)


def _successful_rates(KA, KR):
    return [r for kA_i, r in zip(KA, KR) if kA_i != "nan" and r > 0]


def _run_batch(protocol, fibre_len, runtimes, workers):
    if protocol == "BB84":
        KA, _, KR, _ = run_BB84_sims(
            runtimes=runtimes, fibreLen=fibre_len, workers=workers, **_FIXED,
        )
    else:
        KA, _, KR, _ = run_mdi_sims(
            runtimes=runtimes, fibreLen=fibre_len,
            bsEff=0.97, charliePos=0.5, workers=workers, **_FIXED,
        )
    return _successful_rates(KA, KR), runtimes


def run_fixed(protocol, fibre_len, max_runs, workers):
    """Run exactly max_runs sims. Returns (mean_key_rate, runs_used, time_s)."""
    t0 = time.perf_counter()
    rates, n = _run_batch(protocol, fibre_len, max_runs, workers)
    elapsed = time.perf_counter() - t0
    mean_kr = float(np.mean(rates)) if rates else 0.0
    return mean_kr, n, elapsed


def run_adaptive(protocol, fibre_len, max_runs, batch_size, rel_tol, min_runs, workers):
    """
    Run in batches of batch_size. Stop when:
      - running rel. std < rel_tol  (converged, stable regime), OR
      - two consecutive all-fail batches  (at/past QBER cutoff), OR
      - runs_used >= max_runs  (budget exhausted)

    Returns (mean_key_rate, runs_used, n_successful, time_s).
    """
    all_rates  = []
    runs_used  = 0
    fail_streak = 0
    t0 = time.perf_counter()

    while runs_used < max_runs:
        this_batch = min(batch_size, max_runs - runs_used)
        batch_rates, n = _run_batch(protocol, fibre_len, this_batch, workers)
        all_rates.extend(batch_rates)
        runs_used += n

        if not batch_rates:
            fail_streak += 1
            # two consecutive all-fail batches → past cutoff, no point continuing
            if fail_streak >= 2:
                break
            continue
        fail_streak = 0

        if runs_used >= min_runs and len(all_rates) >= 3:
            mean = np.mean(all_rates)
            std  = np.std(all_rates)
            if mean > 0 and std / mean < rel_tol:
                break

    elapsed = time.perf_counter() - t0
    mean_kr = float(np.mean(all_rates)) if all_rates else 0.0
    return mean_kr, runs_used, len(all_rates), elapsed


def sweep(protocol, max_runs, batch_size, rel_tol, min_runs, workers):
    """
    Sweep distances. Returns lists of:
      fixed_rates, fixed_times,
      adapt_rates, adapt_runs_used, adapt_times
    """
    fixed_rates, fixed_times = [], []
    adapt_rates, adapt_runs,  adapt_times = [], [], []

    n = len(_DISTANCES)
    for i, d in enumerate(_DISTANCES):
        print(f"  [{i+1}/{n}] d={d:3}km", end="  ", flush=True)

        kr_f, _, t_f = run_fixed(protocol, d, max_runs, workers)
        print(f"fixed={kr_f:.1f}bps/{t_f:.1f}s", end="  ", flush=True)

        kr_a, used, n_ok, t_a = run_adaptive(
            protocol, d, max_runs, batch_size, rel_tol, min_runs, workers
        )
        print(f"adaptive={kr_a:.1f}bps  used={used}/{max_runs}  t={t_a:.1f}s")

        fixed_rates.append(kr_f);  fixed_times.append(t_f)
        adapt_rates.append(kr_a);  adapt_runs.append(used);  adapt_times.append(t_a)

    return (np.array(fixed_rates), np.array(fixed_times),
            np.array(adapt_rates),  np.array(adapt_runs), np.array(adapt_times))


def _rel_error(fixed, adaptive):
    """Relative error |adaptive - fixed| / fixed; NaN where both zero."""
    with np.errstate(invalid="ignore", divide="ignore"):
        err = np.where(
            fixed > 0,
            np.abs(adaptive - fixed) / fixed,
            np.where(adaptive == 0, 0.0, np.nan),
        )
    return err


def plot_results(protocol, max_runs, batch_size, rel_tol,
                 fixed_rates, fixed_times,
                 adapt_rates, adapt_runs, adapt_times,
                 output_dir):

    rel_err    = _rel_error(fixed_rates, adapt_rates) * 100   # percent
    run_saving = (1 - adapt_runs / max_runs) * 100            # percent
    time_saving = (1 - adapt_times / fixed_times) * 100

    total_fixed = fixed_times.sum()
    total_adapt = adapt_times.sum()
    overall_saving = (1 - total_adapt / total_fixed) * 100

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

    # ── Left: runs used per distance ─────────────────────────────────────────
    ax = axes[0]
    ax.bar(_DISTANCES, adapt_runs, width=4, color="steelblue",
           alpha=0.8, label="Adaptive runs used")
    ax.axhline(max_runs, color="tomato", lw=1.5, ls="--",
               label=f"Fixed baseline ({max_runs} runs)")
    ax.axhline(batch_size, color="gray", lw=1.0, ls=":",
               label=f"Batch size ({batch_size})")
    ax.set_xlabel("Distance (km)")
    ax.set_ylabel("Runs used")
    ax.set_xticks(_DISTANCES)
    ax.set_xticklabels(_DISTANCES, fontsize=8)
    ax.set_ylim(0, max_runs * 1.15)
    ax.legend(fontsize=8)
    ax.set_title(
        f"{protocol} — Adaptive MC: runs used vs distance\n"
        f"rel_tol={rel_tol}, batch={batch_size}  |  "
        f"overall run saving: {run_saving.mean():.0f}%"
    )

    # ── Right: relative error vs fixed baseline ───────────────────────────────
    ax2 = axes[1]
    valid = ~np.isnan(rel_err)
    ax2.bar(np.array(_DISTANCES)[valid], rel_err[valid], width=4,
            color="darkorange", alpha=0.8)
    ax2.axhline(rel_tol * 100, color="tomato", lw=1.5, ls="--",
                label=f"Convergence threshold ({rel_tol*100:.0f}%)")
    ax2.set_xlabel("Distance (km)")
    ax2.set_ylabel("Relative error vs fixed baseline (%)")
    ax2.set_xticks(_DISTANCES)
    ax2.set_xticklabels(_DISTANCES, fontsize=8)
    ax2.legend(fontsize=8)
    ax2.set_title(
        f"{protocol} — Accuracy cost of early stopping\n"
        f"wall-clock saving: {overall_saving:.0f}%  "
        f"({total_fixed:.0f}s → {total_adapt:.0f}s)"
    )

    fig.tight_layout()

    if output_dir:
        path = os.path.join(output_dir, f"adaptive_mc_{protocol.lower()}.png")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        print(f"  Saved: {path}")
    return fig


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Adaptive Monte Carlo early-stopping benchmark.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--max-runs",  type=int,   default=100,
                        help="Fixed baseline run count (= adaptive budget cap)")
    parser.add_argument("--batch",     type=int,   default=10,
                        help="Simulations per adaptive batch")
    parser.add_argument("--rel-tol",   type=float, default=0.10,
                        help="Convergence threshold: stop when std/mean < rel_tol")
    parser.add_argument("--min-runs",  type=int,   default=20,
                        help="Minimum runs before convergence check begins")
    parser.add_argument("--protocol",  choices=["bb84", "mdi", "both"], default="both")
    parser.add_argument("--workers",   type=int,   default=None,
                        help="Worker processes (default: 80%% of CPU cores)")
    parser.add_argument("--output-dir", metavar="DIR", default=None,
                        help="Save figures to directory instead of displaying")
    args = parser.parse_args()

    if args.output_dir:
        os.makedirs(args.output_dir, exist_ok=True)

    protos = []
    if args.protocol in ("bb84", "both"):
        protos.append("BB84")
    if args.protocol in ("mdi", "both"):
        protos.append("MDI")

    for proto in protos:
        print(f"\n{'='*60}")
        print(f"  {proto}: fixed={args.max_runs} runs  |  "
              f"adaptive: batch={args.batch}, tol={args.rel_tol}, min={args.min_runs}")
        print(f"{'='*60}")

        results = sweep(proto, args.max_runs, args.batch,
                        args.rel_tol, args.min_runs, args.workers)
        fixed_rates, fixed_times, adapt_rates, adapt_runs, adapt_times = results

        total_run_saving = (1 - adapt_runs.sum() / (args.max_runs * len(_DISTANCES))) * 100
        total_time_saving = (1 - adapt_times.sum() / fixed_times.sum()) * 100
        print(f"\n  Summary ({proto}):")
        print(f"    Total run reduction:  {total_run_saving:.1f}%")
        print(f"    Wall-clock saving:    {total_time_saving:.1f}%")
        print(f"    Mean relative error:  "
              f"{np.nanmean(_rel_error(fixed_rates, adapt_rates))*100:.1f}%")

        plot_results(proto, args.max_runs, args.batch, args.rel_tol,
                     fixed_rates, fixed_times,
                     adapt_rates, adapt_runs, adapt_times,
                     args.output_dir)

    if not args.output_dir:
        plt.show()
