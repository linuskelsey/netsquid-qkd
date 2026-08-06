"""
GP Surrogate Model — Speed vs Accuracy Benchmark
=================================================
Trains a Gaussian Process surrogate on a coarse (fibre_len x detector_eff) grid,
then evaluates on a dense grid to benchmark speedup against NetSquid simulations.

The 2D input space (distance, detector efficiency) captures the most impactful
parameter pair: distance drives exponential loss; detector_eff enters linearly
for BB84 and quadratically for MDI.

Usage:
    python scripts/P2P/surrogate.py [--runtimes INT] [--workers INT] [--protocol STR] [--output-dir DIR]

Examples:
    python scripts/P2P/surrogate.py --runtimes 20 --output-dir docs/figures
    python scripts/P2P/surrogate.py --protocol bb84 --runtimes 30
"""

import os
import sys
import time
import argparse
from itertools import product

import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel, ConstantKernel

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from BB84.BB84_run import run_BB84_sims
from MDI.mdiRun import run_mdi_sims

# ── Coarse training grid (overridden by --grid-size at runtime) ───────────────
_DISTANCES = [5, 15, 30, 50, 70, 90]        # km — spans metropolitan range
_DET_EFFS  = [0.20, 0.35, 0.50, 0.65, 0.80, 0.95]   # realistic SNSPD range


def _make_grid(n):
    """Replace default grid with an n×n uniform grid over the same ranges."""
    global _DISTANCES, _DET_EFFS
    _DISTANCES = list(np.linspace(5, 90, n).round(1))
    _DET_EFFS  = list(np.linspace(0.20, 0.95, n).round(3))

# Dense evaluation grid (GP only — no simulations run here)
_D_DENSE   = np.linspace(1, 100, 100)
_ETA_DENSE = np.linspace(0.10, 1.00, 100)

# Fixed realistic defaults (all parameters except the two swept ones)
_FIXED = dict(
    qDelay=0, qSpeed=0.8, photonCount=1024, sourceFreq=1e7,
    lenLoss=0.2, initLoss=0.1, darkCount=100,
    nodeLossDb=2.0, sourceErrRate=0.005, dephasingRate=3.2e-7,
    db_path=None,
)


def _mean_key_rate(KA, KR):
    """Mean key rate (bps) over successful runs; 0.0 if none succeed."""
    raw = [r for kA_i, r in zip(KA, KR) if kA_i != "nan" and r > 0]
    return sum(raw) / len(raw) if raw else 0.0


def run_grid(protocol, runtimes, workers):
    """Simulate coarse (distance × detector_eff) grid. Returns X (N×2), y (N,)."""
    X, y = [], []
    pts = list(product(_DISTANCES, _DET_EFFS))
    for i, (d, eta) in enumerate(pts):
        print(f"  [{i+1}/{len(pts)}] {protocol}  d={d:3}km  η_d={eta:.2f}", flush=True)
        if protocol == "BB84":
            KA, _, KR, _ = run_BB84_sims(
                runtimes=runtimes, fibreLen=d, detectorEffZ=eta,
                workers=workers, **_FIXED,
            )
        else:
            KA, _, KR, _ = run_mdi_sims(
                runtimes=runtimes, fibreLen=d, detectorEffZ=eta,
                bsEff=0.97, charliePos=0.5, workers=workers, **_FIXED,
            )
        X.append([d, eta])
        y.append(_mean_key_rate(KA, KR))
    return np.array(X), np.array(y)


def fit_gp(X, y):
    """
    Fit GP in log10(key_rate) space — handles the orders-of-magnitude range.
    Zero-rate points are given a floor (10x below min positive) so log is defined.
    Returns (gp, y_floor) where y_floor has zeros replaced.
    """
    min_pos = y[y > 0].min() if (y > 0).any() else 1.0
    y_floor = np.where(y > 0, y, min_pos * 0.1)
    log_y   = np.log10(y_floor)

    # Separate length scales: distance (0-100 km) and detector_eff (0-1)
    kernel = ConstantKernel(1.0, (1e-3, 1e3)) \
             * RBF([15.0, 0.3], [(1.0, 100.0), (0.05, 2.0)]) \
             + WhiteKernel(1e-2, (1e-5, 1.0))
    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=8, normalize_y=True)
    gp.fit(X, log_y)
    return gp, y_floor


def gp_predict_dense(gp):
    """Predict log10(key_rate) on the dense grid. Returns (DD, EE, Z_pred, Z_std)."""
    DD, EE = np.meshgrid(_D_DENSE, _ETA_DENSE)
    X_dense = np.column_stack([DD.ravel(), EE.ravel()])
    log_pred, log_std = gp.predict(X_dense, return_std=True)
    Z_pred = 10 ** log_pred.reshape(DD.shape)
    Z_std  = log_std.reshape(DD.shape)
    return DD, EE, Z_pred, Z_std


def measure_speedup(protocol, runtimes, workers, gp):
    """
    Time one simulation call vs GP inference on the full dense grid.
    Returns (sim_s, gp_ms, speedup_factor).
    """
    # Sim: one grid point at typical metropolitan params
    t0 = time.perf_counter()
    if protocol == "BB84":
        run_BB84_sims(runtimes=runtimes, fibreLen=40.0, detectorEffZ=0.65,
                      workers=workers, **_FIXED)
    else:
        run_mdi_sims(runtimes=runtimes, fibreLen=40.0, detectorEffZ=0.65,
                     bsEff=0.97, charliePos=0.5, workers=workers, **_FIXED)
    sim_s = time.perf_counter() - t0

    # GP: all 10,000 dense-grid points at once
    DD, EE = np.meshgrid(_D_DENSE, _ETA_DENSE)
    X_dense = np.column_stack([DD.ravel(), EE.ravel()])
    t0 = time.perf_counter()
    gp.predict(X_dense, return_std=True)
    gp_ms = (time.perf_counter() - t0) * 1e3

    # Speedup: sim cost per point vs GP cost per point
    n_dense  = len(X_dense)
    gp_per_pt_s = (gp_ms / 1e3) / n_dense
    speedup = sim_s / gp_per_pt_s
    return sim_s, gp_ms, speedup


def plot_surrogate(protocol, X_train, y_train, DD, EE, Z_pred, Z_std,
                   sim_s, gp_ms, speedup, output_dir):
    n_train   = len(X_train)
    n_dense   = DD.size
    ok        = y_train > 0

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

    # ── Left: predicted surface ──────────────────────────────────────────────
    ax = axes[0]
    Z_log = np.log10(np.clip(Z_pred, 1e-6, None))
    levels = np.linspace(Z_log.min(), Z_log.max(), 22)
    cf  = ax.contourf(DD, EE, Z_log, levels=levels, cmap="viridis")
    plt.colorbar(cf, ax=ax, label=r"$\log_{10}$(key rate / bps)")
    ax.scatter(X_train[ok,  0], X_train[ok,  1], c="white",  s=40,
               zorder=5, label=f"training pts (success, n={ok.sum()})")
    ax.scatter(X_train[~ok, 0], X_train[~ok, 1], c="red", marker="x", s=50,
               zorder=5, label=f"training pts (rate=0, n={(~ok).sum()})")
    ax.set_xlabel("Distance (km)")
    ax.set_ylabel(r"Detector efficiency $\eta_d$")
    ax.set_title(f"{protocol} — GP surrogate: key rate surface\n"
                 f"Trained on {n_train} pts, predicts {n_dense:,} pts")
    ax.legend(fontsize=8, loc="lower left")

    # ── Right: uncertainty + speedup annotation ──────────────────────────────
    ax = axes[1]
    cf2 = ax.contourf(DD, EE, Z_std, levels=20, cmap="plasma")
    plt.colorbar(cf2, ax=ax, label=r"GP std $\sigma$ (log$_{10}$ scale)")
    ax.set_xlabel("Distance (km)")
    ax.set_ylabel(r"Detector efficiency $\eta_d$")
    ax.set_title(f"{protocol} — GP uncertainty (free from posterior)\n"
                 f"High σ = where more simulation is most needed")

    fig.suptitle(
        f"{protocol} surrogate  |  sim: {sim_s:.1f}s/pt  ·  GP: {gp_ms:.1f}ms/{n_dense:,}pts  "
        f"·  {speedup:,.0f}× speedup",
        fontsize=10, y=1.01,
    )
    fig.tight_layout()

    if output_dir:
        path = os.path.join(output_dir, f"surrogate_{protocol.lower()}.png")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        print(f"  Saved: {path}")
    return fig


def _grid_path(grid_dir, protocol):
    return os.path.join(grid_dir, f"grid_{protocol.lower()}.npz")


def save_grid(grid_dir, protocol, X, y):
    os.makedirs(grid_dir, exist_ok=True)
    path = _grid_path(grid_dir, protocol)
    np.savez(path, X=X, y=y)
    print(f"  Grid saved: {path}")


def load_grid(grid_dir, protocol):
    path = _grid_path(grid_dir, protocol)
    data = np.load(path)
    print(f"  Grid loaded: {path}  ({len(data['y'])} points)")
    return data["X"], data["y"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="GP surrogate model speedup benchmark for BB84 / MDI-QKD.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--runtimes",   type=int, default=20,
                        help="MC runs per training grid point")
    parser.add_argument("--workers",    type=int, default=None,
                        help="Worker processes (default: 80%% of CPU cores)")
    parser.add_argument("--protocol",   choices=["bb84", "mdi", "both"], default="both")
    parser.add_argument("--output-dir", metavar="DIR", default=None,
                        help="Save figures to directory instead of displaying")
    parser.add_argument("--grid-size",  type=int, default=None,
                        help="Use an N×N uniform grid instead of the default 6×6")
    parser.add_argument("--save-grid",  metavar="DIR", default=None,
                        help="Save (X, y) grid arrays to DIR after simulating")
    parser.add_argument("--load-grid",  metavar="DIR", default=None,
                        help="Load (X, y) grid arrays from DIR; skip simulation")
    args = parser.parse_args()

    if args.grid_size:
        _make_grid(args.grid_size)

    if args.output_dir:
        os.makedirs(args.output_dir, exist_ok=True)

    protos = []
    if args.protocol in ("bb84", "both"):
        protos.append("BB84")
    if args.protocol in ("mdi", "both"):
        protos.append("MDI")

    n_grid = len(_DISTANCES) * len(_DET_EFFS)

    for proto in protos:
        print(f"\n{'='*60}")

        if args.load_grid:
            print(f"  {proto}: loading grid from {args.load_grid}")
            X, y = load_grid(args.load_grid, proto)
        else:
            print(f"  {proto}: simulating {n_grid} training points "
                  f"({args.runtimes} runs each)")
            print(f"{'='*60}")
            X, y = run_grid(proto, args.runtimes, args.workers)
            if args.save_grid:
                save_grid(args.save_grid, proto, X, y)

        print(f"\n  Fitting GP ({(y>0).sum()}/{len(y)} points have positive key rate)...")
        gp, y_floor = fit_gp(X, y)
        print(f"  Optimised kernel: {gp.kernel_}")

        print(f"\n  Predicting dense grid ({len(_D_DENSE)*len(_ETA_DENSE):,} points)...")
        DD, EE, Z_pred, Z_std = gp_predict_dense(gp)

        print(f"\n  Measuring speedup (1 sim call vs GP dense eval)...")
        sim_s, gp_ms, speedup = measure_speedup(proto, args.runtimes, args.workers, gp)
        print(f"  Simulation (1 pt, {args.runtimes} runs): {sim_s:.2f}s")
        print(f"  GP         ({DD.size:,} pts):            {gp_ms:.1f}ms")
        print(f"  Speedup:   {speedup:,.0f}×")

        plot_surrogate(proto, X, y, DD, EE, Z_pred, Z_std,
                       sim_s, gp_ms, speedup, args.output_dir)

    if not args.output_dir:
        plt.show()
