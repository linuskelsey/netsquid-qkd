"""
Relay placement analysis.

Experiment 1 — single cluster, K=1 relay.
    Sweeps relay position over a grid for several user counts.
    Validates that centroid placement maximises average MDI-QKD key rate.

Experiment 2 — two clusters, K=2 relays.
    Fixed cluster geometry, sweeps total user count N.
    Compares centroid placement (relay at cluster centroid) vs
    boundary placement (relay displaced 1σ toward opposing cluster).
    Run for MDI-QKD.

Usage:
    python scripts/network/relay_placement.py --exp 1 [options]
    python scripts/network/relay_placement.py --exp 2 [options]

Options (shared):
    --area FLOAT       Area side length in km (default: 10.0)
    --seed INT         Random seed (random if omitted)
    --runtimes INT     Monte Carlo runs per pair (default: 10)
    --config PATH      JSON config preset
    --workers INT      Worker processes (default: 80% of CPU cores)
    --save PATH        Save figure to file instead of displaying

Experiment 1 options:
    --n-values INTS    Comma-separated user counts to sweep (default: 5,10,15,20)
    --grid INT         Grid resolution for relay position sweep (default: 8)

Experiment 2 options:
    --n-min INT        Min total users (default: 6)
    --n-max INT        Max total users (default: 30)
    --n-step INT       Step size (default: 2)
    --seeds INT        Random topologies to average over (default: 5)
    --spread FLOAT     Cluster Gaussian std in km (default: area/5)

Examples:
    python scripts/network/relay_placement.py --exp 1 --n-values 5,10,20 --grid 10
    python scripts/network/relay_placement.py --exp 2 --n-max 40 --seeds 10 --save results/placement.png
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

from lib.plotting import apply_thesis_style, save_bundle
from lib.functions import load_config
from topology import Topology
from mdi_network import run_mdi_network

apply_thesis_style()


# ─── shared ────────────────────────────────────────────────────────────────────

def _avg_rate(pair_rates):
    valid = [r[0] for r in pair_rates.values() if r[0] != "nan"]
    return sum(valid) / len(valid) if valid else 0.0


# ─── Experiment 1 ──────────────────────────────────────────────────────────────

def exp1_grid(n, area, grid_res, cfg, runtimes, seed, workers):
    """
    Sweep relay position over a grid_res×grid_res grid for K=1, N users.
    Returns (xs, ys, mdi_grid, centroid, user_pos).
    """
    rng = np.random.default_rng(seed)
    user_pos = rng.uniform(0, area, size=(n, 2))
    centroid = user_pos.mean(axis=0)

    xs = np.linspace(0, area, grid_res)
    ys = np.linspace(0, area, grid_res)
    mdi_grid = np.zeros((grid_res, grid_res))
    total = grid_res * grid_res

    for ix, rx in enumerate(xs):
        for iy, ry in enumerate(ys):
            topo    = Topology(user_pos, np.array([[rx, ry]]))
            mdi_res = run_mdi_network(topo, cfg, runtimes=runtimes, workers=workers,
                                      p2p_db_path=None, net_db_path=None)
            mdi_grid[iy, ix] = _avg_rate(mdi_res["pair_rates"])
            done = ix * grid_res + iy + 1
            print(f"  [{done:3d}/{total}] ({rx:.1f},{ry:.1f})  "
                  f"MDI={mdi_grid[iy,ix]/1000:.2f}k bps", end="\r")

    print()
    return xs, ys, mdi_grid, centroid, user_pos


def plot_exp1(results_by_n, area, output_dir, grid_res, runtimes):
    n_vals = list(results_by_n.keys())
    fig, axes = plt.subplots(1, len(n_vals), figsize=(4 * len(n_vals), 4))
    if len(n_vals) == 1:
        axes = [axes]

    for col, n in enumerate(n_vals):
        xs, ys, mdi_grid, centroid, user_pos = results_by_n[n]
        extent = [0, area, 0, area]

        ax = axes[col]
        im = ax.imshow(mdi_grid / 1000, origin="lower", extent=extent, aspect="auto", cmap="viridis")
        plt.colorbar(im, ax=ax, label="kbps")
        ax.scatter(user_pos[:, 0], user_pos[:, 1], c="white", s=20, zorder=3,
                   edgecolors="grey", linewidths=0.5, label="Users")
        ax.scatter(*centroid, marker="*", s=200, c="red", zorder=5, label="Centroid")
        peak_iy, peak_ix = np.unravel_index(np.argmax(mdi_grid), mdi_grid.shape)
        ax.scatter(xs[peak_ix], ys[peak_iy], marker="X", s=150, c="yellow",
                   zorder=6, label="Peak")
        ax.set_title(f"N={n}")
        ax.set_xlabel("x (km)")
        ax.set_ylabel("y (km)")
        if col == 0:
            ax.legend(fontsize=7)

    title = "MDI-QKD: Relay Position Sweep"
    plt.suptitle(title, fontsize=12)
    plt.tight_layout()

    if output_dir:
        save_bundle(
            fig, output_dir, "relay_placement_exp1",
            title=title,
            assumptions={
                "Experiment": "1 — single cluster, K=1 relay",
                "User counts swept": n_vals,
                "Area": f"{area} x {area} km",
                "Grid resolution": f"{grid_res} x {grid_res}",
                "Runtimes per grid point": runtimes,
            },
            notes=["Validates that centroid placement maximises average MDI-QKD key rate."],
        )
    else:
        plt.show()


# ─── Experiment 2 ──────────────────────────────────────────────────────────────

def _place_two_clusters(n_total, area, spread, seed):
    """Two equal Gaussian clusters at area/4 and 3*area/4 along x-axis."""
    rng    = np.random.default_rng(seed)
    n_each = n_total // 2
    c0     = np.array([area / 4, area / 2])
    c1     = np.array([3 * area / 4, area / 2])
    pos0   = rng.normal(c0, spread, size=(n_each, 2)).clip(0, area)
    pos1   = rng.normal(c1, spread, size=(n_total - n_each, 2)).clip(0, area)
    labels = np.array([0] * n_each + [1] * (n_total - n_each))
    return np.vstack([pos0, pos1]), labels


def _relay_centroid(user_pos, labels):
    return np.array([user_pos[labels == k].mean(axis=0) for k in [0, 1]])


def _relay_boundary(user_pos, labels):
    """Each relay displaced 1σ from its cluster centroid toward the opposing cluster."""
    c0 = user_pos[labels == 0].mean(axis=0)
    c1 = user_pos[labels == 1].mean(axis=0)
    direction = (c1 - c0) / np.linalg.norm(c1 - c0)
    s0 = float(np.std(user_pos[labels == 0]))
    s1 = float(np.std(user_pos[labels == 1]))
    return np.array([
        c0 + s0 * direction,
        c1 - s1 * direction,
    ])


def exp2(n_values, area, spread, cfg, runtimes, seed, n_seeds, workers):
    """
    Sweep N, compare centroid vs boundary relay placement for MDI-QKD.
    Returns dict: strategy → list[list[float]] (seeds × N).
    """
    rng   = np.random.default_rng(seed)
    seeds = rng.integers(0, 100_000, size=n_seeds).tolist()

    data = {
        strat: {"mdi": [[] for _ in n_values]}
        for strat in ("centroid", "boundary")
    }

    for s_idx, s in enumerate(seeds):
        print(f"\n--- Seed {s_idx+1}/{n_seeds} (seed={s}) ---")
        for ni, n in enumerate(n_values):
            user_pos, labels = _place_two_clusters(n, area, spread, s)

            for strat, relay_fn in [("centroid", _relay_centroid), ("boundary", _relay_boundary)]:
                relay_pos = relay_fn(user_pos, labels)
                topo      = Topology(user_pos, relay_pos)

                mdi_res = run_mdi_network(topo, cfg, runtimes=runtimes, workers=workers,
                                          p2p_db_path=None, net_db_path=None)

                data[strat]["mdi"][ni].append(_avg_rate(mdi_res["pair_rates"]))

            print(f"  N={n:3d}  "
                  f"MDI  cent={np.mean(data['centroid']['mdi'][ni])/1000:.2f}k  "
                  f"bnd={np.mean(data['boundary']['mdi'][ni])/1000:.2f}k bps")

    return data


def plot_exp2(data, n_values, output_dir, area, spread, runtimes, n_seeds):
    N      = np.array(n_values)
    colors = {"centroid": "#e41a1c", "boundary": "#377eb8"}
    labels = {"centroid": "Centroid", "boundary": "Boundary (1 std toward opposing cluster)"}

    fig, ax = plt.subplots(figsize=(7, 5))

    for strat in ("centroid", "boundary"):
        means = np.array([np.mean(data[strat]["mdi"][i]) for i in range(len(N))]) / 1000
        stds  = np.array([np.std( data[strat]["mdi"][i]) for i in range(len(N))]) / 1000
        ax.errorbar(N, means, yerr=stds, label=labels[strat],
                    color=colors[strat], marker="o" if strat == "centroid" else "s",
                    capsize=4, lw=1.5)
    ax.set_xlabel("Total users N")
    ax.set_ylabel("Avg key rate (kbps)")
    ax.set_title("MDI-QKD")
    ax.legend()
    ax.grid(True, alpha=0.3)

    title = "Relay Placement: Centroid vs Boundary"
    plt.suptitle(title, fontsize=12)
    plt.tight_layout()

    if output_dir:
        save_bundle(
            fig, output_dir, "relay_placement_exp2",
            title=title,
            assumptions={
                "Experiment": "2 — two clusters, K=2 relays",
                "User count sweep range": f"{n_values[0]}-{n_values[-1]}",
                "Area": f"{area} x {area} km",
                "Cluster spread (std)": f"{spread:.2f} km",
                "Runtimes per pair": runtimes,
                "Random topologies averaged": n_seeds,
            },
            notes=["Boundary strategy displaces each relay 1 std toward the opposing cluster."],
        )
    else:
        plt.show()


# ─── main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Relay placement analysis")
    parser.add_argument("--exp",      type=int,   required=True, choices=[1, 2],
                        help="Experiment number")
    parser.add_argument("--area",     type=float, default=10.0,  help="Area side length (km)")
    parser.add_argument("--seed",     type=int,   default=None,  help="Random seed")
    parser.add_argument("--runtimes", type=int,   default=10,    help="Monte Carlo runs per pair")
    parser.add_argument("--config",   type=str,   default=None,  help="JSON config preset")
    parser.add_argument("--workers",  type=int,   default=None,  help="Worker processes")
    parser.add_argument("--output-dir", type=str, default=None,  help="Save figure bundle to directory instead of displaying")

    # Exp 1
    parser.add_argument("--n-values", type=str, default="5,10,15,20",
                        help="Comma-separated user counts (exp 1)")
    parser.add_argument("--grid",     type=int, default=8,
                        help="Grid resolution for relay position sweep (exp 1)")

    # Exp 2
    parser.add_argument("--n-min",   type=int,   default=6,    help="Min users (exp 2)")
    parser.add_argument("--n-max",   type=int,   default=30,   help="Max users (exp 2)")
    parser.add_argument("--n-step",  type=int,   default=2,    help="User count step (exp 2)")
    parser.add_argument("--seeds",   type=int,   default=5,    help="Topologies to average (exp 2)")
    parser.add_argument("--spread",  type=float, default=None, help="Cluster std in km (exp 2)")

    args = parser.parse_args()

    if args.seed is None:
        args.seed = int.from_bytes(os.urandom(4), "big") % 100_000

    cfg = load_config(args.config)

    if args.exp == 1:
        n_values = [int(x) for x in args.n_values.split(",")]
        results  = {}
        for n in n_values:
            print(f"\n=== Exp 1: N={n}, grid={args.grid}×{args.grid} ===")
            results[n] = exp1_grid(n, args.area, args.grid, cfg, args.runtimes,
                                   args.seed, args.workers)
        plot_exp1(results, args.area, args.output_dir, args.grid, args.runtimes)

    else:
        spread   = args.spread if args.spread is not None else args.area / 5
        n_values = list(range(args.n_min, args.n_max + 1, args.n_step))
        print(f"\n=== Exp 2: N={n_values[0]}..{n_values[-1]}, spread={spread:.1f} km, "
              f"{args.seeds} seeds ===")
        data = exp2(n_values, args.area, spread, cfg, args.runtimes,
                    args.seed, args.seeds, args.workers)
        plot_exp2(data, n_values, args.output_dir, args.area, spread, args.runtimes, args.seeds)


if __name__ == "__main__":
    main()
