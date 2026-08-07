"""
Trend Analysis: Speedup vs Scale
=================================
Two analyses:

1. GP Surrogate — speedup vs evaluation grid size
   Load saved training grid, fit GP once, time inference at increasing grid
   sizes. Shows speedup scales linearly with evaluation density.

2. Adaptive MC — wall-clock saving vs simulation budget (BB84 only)
   Run fixed vs adaptive at one stable-regime distance across increasing
   max_runs budgets. Shows saving grows as budget increases (more internal
   spawns to amortise).

Usage:
    python scripts/P2P/time/trend_analysis.py [--load-grid DIR] [--workers INT]
                                              [--output-dir DIR]
                                              [--skip-surrogate] [--skip-adaptive]

Examples:
    python scripts/P2P/time/trend_analysis.py --load-grid data/surrogate_grids --output-dir docs/figures/July
    python scripts/P2P/time/trend_analysis.py --load-grid data/surrogate_grids --skip-adaptive --output-dir docs/figures/July
"""

import os
import sys
import time
import argparse

import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel, ConstantKernel

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from lib.plotting import apply_thesis_style, save_bundle
from BB84.BB84_run import run_BB84_sims

apply_thesis_style()

# ── Surrogate trend parameters ────────────────────────────────────────────────
_EVAL_SIZES = [100, 500, 1_000, 5_000, 10_000, 50_000, 100_000]

# ── Adaptive MC trend parameters ──────────────────────────────────────────────
_BUDGETS      = [100, 200, 500, 1_000, 2_000]
_TREND_DIST   = 5.0   # km — stable regime; adaptive should converge early here
_BATCH        = 100
_REL_TOL      = 0.10
_MIN_RUNS     = 100

_FIXED_KWARGS = dict(
    qDelay=0, qSpeed=0.8, photonCount=1024, sourceFreq=1e7,
    lenLoss=0.2, initLoss=0.1, detectorEffZ=0.65, detectorEffX=0.85,
    darkCount=100, nodeLossDb=2.0, sourceErrRate=0.005, dephasingRate=3.2e-7,
    db_path=None,
)


# ═══════════════════════════════════════════════════════════════════════════════
# Surrogate trend
# ═══════════════════════════════════════════════════════════════════════════════

def _fit_gp(X, y):
    min_pos = y[y > 0].min() if (y > 0).any() else 1.0
    y_floor = np.where(y > 0, y, min_pos * 0.1)
    log_y   = np.log10(y_floor)
    kernel  = ConstantKernel(1.0, (1e-3, 1e3)) \
              * RBF([15.0, 0.3], [(1.0, 100.0), (0.05, 2.0)]) \
              + WhiteKernel(1e-2, (1e-5, 1.0))
    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=8, normalize_y=True)
    gp.fit(X, log_y)
    return gp


def surrogate_trend(grid_dir, sim_runtimes, workers):
    """
    Load BB84 grid, fit GP, time inference at each eval size.
    Times one real sim call to get sim_time_per_pt for apples-to-apples speedup.
    Returns (eval_sizes, gp_times_ms, speedups, sim_time_per_pt_s).
    """
    path = os.path.join(grid_dir, "grid_bb84.npz")
    data = np.load(path)
    X, y = data["X"], data["y"]
    n_train = len(y)
    print(f"  Loaded BB84 grid: {n_train} training points")

    print(f"  Timing one sim call ({sim_runtimes} runtimes, d=40km)...", flush=True)
    t0 = time.perf_counter()
    run_BB84_sims(runtimes=sim_runtimes, fibreLen=40.0, workers=workers, **_FIXED_KWARGS)
    sim_time_per_pt_s = time.perf_counter() - t0
    print(f"  Sim time per point: {sim_time_per_pt_s:.2f}s")

    print(f"  Fitting GP...", flush=True)
    gp = _fit_gp(X, y)
    print(f"  Kernel: {gp.kernel_}")

    gp_times_ms = []
    speedups     = []
    rng = np.random.default_rng(42)

    for n_eval in _EVAL_SIZES:
        # Random points within training range
        d_range   = X[:, 0].max() - X[:, 0].min()
        eta_range = X[:, 1].max() - X[:, 1].min()
        X_eval = np.column_stack([
            rng.uniform(X[:, 0].min(), X[:, 0].max(), n_eval),
            rng.uniform(X[:, 1].min(), X[:, 1].max(), n_eval),
        ])

        # Warm-up pass (avoid JIT / cache effects on first call)
        if n_eval == _EVAL_SIZES[0]:
            gp.predict(X_eval[:10])

        t0 = time.perf_counter()
        gp.predict(X_eval, return_std=True)
        elapsed_ms = (time.perf_counter() - t0) * 1e3

        # Speedup: total sim cost for n_eval points vs GP inference
        sim_total_s = n_eval * sim_time_per_pt_s
        speedup     = sim_total_s / (elapsed_ms / 1e3)

        gp_times_ms.append(elapsed_ms)
        speedups.append(speedup)
        print(f"    n_eval={n_eval:>7,}  GP={elapsed_ms:7.1f}ms  "
              f"equiv_sim={sim_total_s/3600:.1f}h  speedup={speedup:,.0f}×")

    return _EVAL_SIZES, gp_times_ms, speedups, sim_time_per_pt_s


def plot_surrogate_trend(eval_sizes, gp_times_ms, speedups, sim_s_per_pt, output_dir):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Left: GP inference time vs eval size
    ax1.plot(eval_sizes, gp_times_ms, "o-", color="steelblue", lw=2, ms=7)
    ax1.set_xscale("log")
    ax1.set_yscale("log")
    ax1.set_xlabel("Evaluation grid size")
    ax1.set_ylabel("GP inference time (ms)")
    ax1.set_title("GP Inference Time Scaling")
    ax1.grid(True, which="both", alpha=0.3)

    # Right: speedup vs eval size
    ax2.plot(eval_sizes, [s / 1e6 for s in speedups], "s-", color="darkorange", lw=2, ms=7)
    ax2.set_xscale("log")
    ax2.set_xlabel("Evaluation grid size")
    ax2.set_ylabel(r"Speedup vs simulation ($\times 10^6$)")
    ax2.set_title("Speedup vs Grid Size")
    ax2.grid(True, which="both", alpha=0.3)

    fig.suptitle("GP Surrogate Speedup Trend", fontsize=11)
    fig.tight_layout()

    if output_dir:
        save_bundle(
            fig, output_dir, "trend_surrogate_speedup",
            title="GP Surrogate Speedup Trend",
            assumptions={
                "Evaluation grid sizes": eval_sizes,
                "Simulation time per point": f"{sim_s_per_pt:.2f} s",
                "GP training points": 256,
            },
            notes=["Left: GP inference wall-clock time vs evaluation grid size (log-log).",
                   "Right: speedup of GP inference vs equivalent simulation cost."],
        )
    return fig


# ═══════════════════════════════════════════════════════════════════════════════
# Adaptive MC trend
# ═══════════════════════════════════════════════════════════════════════════════

def _successful_rates(KA, KR):
    return [r for kA_i, r in zip(KA, KR) if kA_i != "nan" and r > 0]


def _run_batch(n, workers):
    KA, _, KR, _ = run_BB84_sims(
        runtimes=n, fibreLen=_TREND_DIST, workers=workers, **_FIXED_KWARGS,
    )
    return _successful_rates(KA, KR)


def _time_fixed(budget, workers):
    t0 = time.perf_counter()
    _run_batch(budget, workers)
    return time.perf_counter() - t0


def _time_adaptive(budget, workers):
    all_rates  = []
    runs_used  = 0
    fail_streak = 0
    t0 = time.perf_counter()

    while runs_used < budget:
        this_batch = min(_BATCH, budget - runs_used)
        rates = _run_batch(this_batch, workers)
        all_rates.extend(rates)
        runs_used += this_batch

        if not rates:
            fail_streak += 1
            if fail_streak >= 2:
                break
            continue
        fail_streak = 0

        if runs_used >= _MIN_RUNS and len(all_rates) >= 3:
            mean = np.mean(all_rates)
            std  = np.std(all_rates)
            if mean > 0 and std / mean < _REL_TOL:
                break

    elapsed = time.perf_counter() - t0
    return elapsed, runs_used


def adaptive_trend(workers):
    """
    For each budget, time fixed vs adaptive at _TREND_DIST.
    Returns (budgets, fixed_times, adapt_times, adapt_runs, savings_pct).
    """
    fixed_times, adapt_times, adapt_runs_used = [], [], []

    n = len(_BUDGETS)
    for i, budget in enumerate(_BUDGETS):
        print(f"  [{i+1}/{n}] budget={budget}", flush=True)

        t_fix = _time_fixed(budget, workers)
        t_ada, used = _time_adaptive(budget, workers)
        saving = (1 - t_ada / t_fix) * 100

        fixed_times.append(t_fix)
        adapt_times.append(t_ada)
        adapt_runs_used.append(used)
        print(f"    fixed={t_fix:.1f}s  adaptive={t_ada:.1f}s  "
              f"runs_used={used}/{budget}  saving={saving:.1f}%")

    savings_pct = [(1 - a / f) * 100 for f, a in zip(fixed_times, adapt_times)]
    return (_BUDGETS, np.array(fixed_times), np.array(adapt_times),
            adapt_runs_used, savings_pct)


def plot_adaptive_trend(budgets, fixed_times, adapt_times, adapt_runs,
                        savings_pct, output_dir):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Left: wall-clock time vs budget
    ax1.plot(budgets, fixed_times, "s--", color="tomato",    lw=2, ms=7, label="Fixed baseline")
    ax1.plot(budgets, adapt_times, "o-",  color="steelblue", lw=2, ms=7, label="Adaptive")
    ax1.set_xlabel("Simulation budget (max runs)")
    ax1.set_ylabel("Wall-clock time (s)")
    ax1.set_title("BB84 Wall-Clock vs Budget")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Annotate actual runs used
    for b, used, t in zip(budgets, adapt_runs, adapt_times):
        ax1.annotate(f"{used}", (b, t), textcoords="offset points",
                     xytext=(0, 8), ha="center", fontsize=8, color="steelblue")

    # Right: wall-clock saving vs budget
    colors = ["tomato" if s < 0 else "steelblue" for s in savings_pct]
    ax2.bar(range(len(budgets)), savings_pct, color=colors, width=0.5)
    ax2.axhline(0, color="gray", lw=1.0, ls="--")
    ax2.set_xticks(range(len(budgets)))
    ax2.set_xticklabels(budgets)
    ax2.set_xlabel("Simulation budget (max runs)")
    ax2.set_ylabel("Wall-clock saving (%)")
    ax2.set_title("Wall-Clock Saving vs Budget")
    ax2.grid(True, alpha=0.3, axis="y")

    fig.suptitle("Adaptive MC Speedup Trend", fontsize=11)
    fig.tight_layout()

    if output_dir:
        save_bundle(
            fig, output_dir, "trend_adaptive_mc",
            title="Adaptive MC Speedup Trend",
            assumptions={
                "Protocol": "BB84",
                "Distance": f"{_TREND_DIST:.0f} km (stable regime)",
                "Simulation budgets": budgets,
                "Adaptive batch size": _BATCH,
                "Convergence threshold (rel_tol)": _REL_TOL,
                "Min runs before convergence check": _MIN_RUNS,
                "Fixed simulation params": _FIXED_KWARGS,
            },
            notes=["Left: wall-clock time, fixed baseline vs adaptive, annotated with actual runs used.",
                   "Right: wall-clock saving (%) of adaptive vs fixed at each budget."],
        )
    return fig


# ═══════════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Trend analysis: speedup vs scale for GP surrogate and adaptive MC.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--load-grid",      metavar="DIR", default=None,
                        help="Directory with saved grid_bb84.npz (required for surrogate trend)")
    parser.add_argument("--sim-runtimes",   type=int, default=500,
                        help="MC runs for the single sim timing call — match your training grid runtimes")
    parser.add_argument("--workers",        type=int, default=None,
                        help="Worker processes (default: 80%% of CPU cores)")
    parser.add_argument("--output-dir",     metavar="DIR", default=None,
                        help="Save figures to directory instead of displaying")
    parser.add_argument("--skip-surrogate", action="store_true",
                        help="Skip surrogate speedup trend")
    parser.add_argument("--skip-adaptive",  action="store_true",
                        help="Skip adaptive MC budget trend")
    args = parser.parse_args()

    if args.output_dir:
        os.makedirs(args.output_dir, exist_ok=True)

    if not args.skip_surrogate:
        if not args.load_grid:
            print("ERROR: --load-grid required for surrogate trend. "
                  "Use --skip-surrogate to skip.")
            sys.exit(1)
        print(f"\n{'='*60}")
        print("  Surrogate: speedup vs evaluation grid size")
        print(f"{'='*60}")
        eval_sizes, gp_times, speedups, sim_s = surrogate_trend(args.load_grid, args.sim_runtimes, args.workers)
        plot_surrogate_trend(eval_sizes, gp_times, speedups, sim_s, args.output_dir)

    if not args.skip_adaptive:
        print(f"\n{'='*60}")
        print(f"  Adaptive MC: wall-clock saving vs budget  (d={_TREND_DIST}km, BB84)")
        print(f"{'='*60}")
        budgets, fixed_t, adapt_t, adapt_runs, savings = adaptive_trend(args.workers)
        plot_adaptive_trend(budgets, fixed_t, adapt_t, adapt_runs, savings, args.output_dir)

    if not args.output_dir:
        plt.show()
