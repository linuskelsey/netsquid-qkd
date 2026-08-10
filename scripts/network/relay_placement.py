"""
Relay placement analysis.

Experiment 1 — single cluster, K=1 relay.
    Provider-growth model: users are drawn once from a single incremental
    stream (K=1's catchment is the whole area) so N -> N+1 adds a user rather
    than re-rolling an unrelated sample. Sweeps relay position over a grid at
    each N to validate that centroid/grid-search-peak placement maximises
    average MDI-QKD key rate, and additionally freezes the peak found at the
    smallest N to show how far it drifts from the true optimum as N grows.

Experiment 2 — two clusters, K=2 relays.
    Provider-growth model: draws n_min users into 2 randomly-assigned catchments,
    places relays via the chosen strategies, then FREEZES relay position and
    grows the network one user at a time (uniform-random catchment) up to
    n_max. Measures how each strategy's initial placement degrades under
    organic, unplanned growth rather than continuous re-optimisation.
    Compares centroid, boundary (1σ toward the other catchment), and
    Weiszfeld (backbone-coupled geometric median) placement, for MDI-QKD.

Usage:
    python scripts/network/relay_placement.py --exp 1 [options]
    python scripts/network/relay_placement.py --exp 2 [options]

Options (shared):
    --area FLOAT       Area side length in km (default: 10.0)
    --seed INT         Random seed (random if omitted)
    --runtimes INT     Monte Carlo runs per pair (default: 10)
    --config PATH      JSON config preset
    --workers INT      Worker processes (default: 80% of CPU cores)
    --output-dir DIR   Save figure bundle {plot.png, plot.tex, assumptions.md} to directory instead of displaying

Experiment 1 options:
    --n-values INTS    Comma-separated user counts to sweep (default: 5,10,15,20)
    --grid INT         Grid resolution for relay position sweep (default: 8)

Experiment 2 options:
    --n-min INT        Min total users (default: 6)
    --n-max INT        Max total users (default: 30)
    --n-step INT       Step size (default: 2)
    --seeds INT        Random topologies to average over (default: 5)
    --spread FLOAT     Cluster Gaussian std in km (default: area/5); ignored if --catchment-radius given
    --catchment-radius FLOAT  Hard catchment radius in km (uniform disc instead of Gaussian spread)
    --error STR        Error style: bars (default), shade (±1σ fill), or iqr (Q1/Q3 fill)

Examples:
    python scripts/network/relay_placement.py --exp 1 --n-values 5,10,20 --grid 10
    python scripts/network/relay_placement.py --exp 2 --n-max 40 --seeds 10 --output-dir results/placement
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
from topology import Topology, grow_catchments, RELAY_STRATEGIES
from mdi_network import run_mdi_network
from visualise_network import draw_mdi, draw_bb84

apply_thesis_style()


# ─── shared ────────────────────────────────────────────────────────────────────

def _avg_rate(pair_rates):
    valid = [r[0] for r in pair_rates.values() if r[0] != "nan"]
    return sum(valid) / len(valid) if valid else 0.0


# ─── Experiment 1 ──────────────────────────────────────────────────────────────

def exp1_grid(user_pos, area, grid_res, cfg, runtimes, workers):
    """
    Sweep relay position over a grid_res×grid_res grid for K=1, given users.
    Returns (xs, ys, mdi_grid, centroid, user_pos).
    """
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


def exp1(n_values, area, grid_res, cfg, runtimes, seed, workers):
    """
    Provider-growth model: users are drawn once from a single incremental RNG
    stream (K=1's catchment is the whole area, so growth is just continued
    uniform sampling), so N -> N+1 adds a user rather than re-rolling an
    unrelated sample. Each N still runs its own independent grid search (this
    is the validation that centroid/median placement is instantaneously
    optimal), but the grid-search peak found at the smallest N is also frozen
    and re-evaluated at every larger N, to show how much a relay sized for the
    initial user graph drifts from the true (re-optimised) optimum as organic
    growth happens.
    Returns (results_by_n, frozen_pos, frozen_rate).
    """
    rng = np.random.default_rng(seed)
    all_user_pos = rng.uniform(0, area, size=(n_values[-1], 2))

    results_by_n = {}
    frozen_pos   = None
    frozen_rate  = {}

    for n in n_values:
        user_pos = all_user_pos[:n]
        print(f"\n=== Exp 1: N={n}, grid={grid_res}×{grid_res} ===")
        xs, ys, mdi_grid, centroid, _ = exp1_grid(user_pos, area, grid_res, cfg, runtimes, workers)
        results_by_n[n] = (xs, ys, mdi_grid, centroid, user_pos)

        if frozen_pos is None:
            peak_iy, peak_ix = np.unravel_index(np.argmax(mdi_grid), mdi_grid.shape)
            frozen_pos        = np.array([xs[peak_ix], ys[peak_iy]])
            frozen_rate[n]    = float(mdi_grid[peak_iy, peak_ix])
        else:
            topo    = Topology(user_pos, np.array([frozen_pos]))
            mdi_res = run_mdi_network(topo, cfg, runtimes=runtimes, workers=workers,
                                      p2p_db_path=None, net_db_path=None)
            frozen_rate[n] = _avg_rate(mdi_res["pair_rates"])

    return results_by_n, frozen_pos, frozen_rate


def plot_exp1(results_by_n, area, output_dir, grid_res, runtimes, seed, frozen_pos=None, frozen_rate=None):
    n_vals = list(results_by_n.keys())
    fig, axes = plt.subplots(1, len(n_vals), figsize=(4 * len(n_vals), 4))
    if len(n_vals) == 1:
        axes = [axes]

    _user_pos_by_n = {}
    _centroid_by_n = {}
    _peak_by_n     = {}

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
        if frozen_pos is not None:
            ax.scatter(*frozen_pos, marker="D", s=90, c="black", zorder=7,
                       edgecolors="white", linewidths=0.8,
                       label=f"Frozen (N={n_vals[0]})" if col == 0 else None)
        ax.set_title(f"N={n}")
        ax.set_xlabel("x (km)")
        ax.set_ylabel("y (km)")
        if col == 0:
            ax.legend(fontsize=7)

        _user_pos_by_n[n] = np.round(user_pos, 3).tolist()
        _centroid_by_n[n] = np.round(centroid, 3).tolist()
        peak_pos          = np.array([xs[peak_ix], ys[peak_iy]])
        _peak_by_n[n]     = [round(float(peak_pos[0]), 3), round(float(peak_pos[1]), 3)]

        if output_dir:
            _topo_dir = os.path.join(output_dir, "relay_placement_exp1", "topologies")
            os.makedirs(_topo_dir, exist_ok=True)
            topo_peak = Topology(user_pos, np.array([peak_pos]))
            fig_m, ax_m = plt.subplots(figsize=(6, 5))
            draw_mdi(ax_m, topo_peak)
            plt.tight_layout()
            fig_m.savefig(os.path.join(_topo_dir, f"N{n}_peak_mdi.png"), dpi=150, bbox_inches="tight")
            plt.close(fig_m)

            fig_b, ax_b = plt.subplots(figsize=(6, 5))
            draw_bb84(ax_b, topo_peak)
            plt.tight_layout()
            fig_b.savefig(os.path.join(_topo_dir, f"N{n}_peak_bb84.png"), dpi=150, bbox_inches="tight")
            plt.close(fig_b)

    title = "MDI-QKD: Relay Position Sweep"
    plt.suptitle(title, fontsize=12)
    plt.tight_layout()

    if output_dir:
        save_bundle(
            fig, output_dir, "relay_placement_exp1",
            title=title,
            assumptions={
                "Experiment": "1 — single cluster, K=1 relay, provider-growth model",
                "User counts swept": n_vals,
                "Growth model": "single incremental RNG stream (uniform over whole area, "
                                "K=1's catchment is the whole area)",
                "Area": f"{area} x {area} km",
                "Grid resolution": f"{grid_res} x {grid_res}",
                "Runtimes per grid point": runtimes,
                "Seed": seed,
                "User positions per N (km)": _user_pos_by_n,
                "Centroid per N (km)": _centroid_by_n,
                "Peak grid position per N (km)": _peak_by_n,
                "Frozen relay position (peak at N=n_min, km)":
                    np.round(frozen_pos, 3).tolist() if frozen_pos is not None else None,
                "Frozen-position achieved MDI rate by N (kbps)":
                    {n: round(frozen_rate[n] / 1000, 3) for n in n_vals} if frozen_rate else None,
            },
            notes=["Validates that centroid placement maximises average MDI-QKD key rate at each N "
                   "independently (Peak marker), and separately shows how much the peak found for "
                   "the smallest N (Frozen marker) drifts from the true optimum as N grows."],
        )
    else:
        plt.show()


# ─── Experiment 2 ──────────────────────────────────────────────────────────────

_STRATEGIES = list(RELAY_STRATEGIES.items())
_STRAT_COLOR  = {"centroid": "#e41a1c", "boundary": "#377eb8", "weiszfeld": "#4daf4a"}
_STRAT_MARKER = {"centroid": "o",       "boundary": "s",       "weiszfeld": "^"}
_STRAT_LABEL  = {
    "centroid":  "Centroid",
    "boundary":  "Boundary (1 std toward opposing cluster)",
    "weiszfeld": "Weiszfeld (backbone-coupled)",
}


def exp2(n_values, area, spread, cfg, runtimes, seed, n_seeds, workers, output_dir=None,
         catchment_radius=None):
    """
    Provider-growth model: relay placed once at n_min per strategy, then frozen;
    network grows one user at a time (uniform-random catchment) up to n_max.
    Compares centroid vs boundary vs weiszfeld relay placement for MDI-QKD.
    Returns dict: strategy → list[list[float]] (seeds × N).
    """
    rng   = np.random.default_rng(seed)
    seeds = rng.integers(0, 100_000, size=n_seeds).tolist()

    data = {
        strat: {"mdi": [[] for _ in n_values]}
        for strat, _ in _STRATEGIES
    }
    graph_data = {}
    n_min = n_values[0]
    n_max = n_values[-1]

    for s_idx, s in enumerate(seeds):
        print(f"\n--- Seed {s_idx+1}/{n_seeds} (seed={s}) ---")
        user_pos_full, labels_full, _ = grow_catchments(n_min, n_max, 2, area, spread, s,
                                                          catchment_radius_km=catchment_radius)

        relay_by_strat = {
            strat: relay_fn(user_pos_full[:n_min], labels_full[:n_min], 2)
            for strat, relay_fn in _STRATEGIES
        }

        for ni, n in enumerate(n_values):
            user_pos = user_pos_full[:n]
            labels   = labels_full[:n]

            for strat, _ in _STRATEGIES:
                relay_pos = relay_by_strat[strat]
                topo      = Topology(user_pos, relay_pos, user_relay=labels)

                if output_dir:
                    _topo_dir = os.path.join(output_dir, "relay_placement_exp2", f"seed{s}", "topologies")
                    os.makedirs(_topo_dir, exist_ok=True)
                    fig_m, ax_m = plt.subplots(figsize=(6, 5))
                    draw_mdi(ax_m, topo, strategy=strat.capitalize())
                    plt.tight_layout()
                    fig_m.savefig(os.path.join(_topo_dir, f"N{n}_{strat}_mdi.png"), dpi=150, bbox_inches="tight")
                    plt.close(fig_m)

                    fig_b, ax_b = plt.subplots(figsize=(6, 5))
                    draw_bb84(ax_b, topo, strategy=strat.capitalize())
                    plt.tight_layout()
                    fig_b.savefig(os.path.join(_topo_dir, f"N{n}_{strat}_bb84.png"), dpi=150, bbox_inches="tight")
                    plt.close(fig_b)

                mdi_res = run_mdi_network(topo, cfg, runtimes=runtimes, workers=workers,
                                          p2p_db_path=None, net_db_path=None)

                data[strat]["mdi"][ni].append(_avg_rate(mdi_res["pair_rates"]))

            if n == n_max:
                graph_data[s] = {
                    "user_positions": np.round(user_pos, 3).tolist(),
                    "cluster_labels": labels.tolist(),
                    **{
                        f"relay_positions_{strat}": np.round(relay_by_strat[strat], 3).tolist()
                        for strat, _ in _STRATEGIES
                    },
                }

            print(f"  N={n:3d}  MDI  " + "  ".join(
                f"{strat}={np.mean(data[strat]['mdi'][ni])/1000:.2f}k" for strat, _ in _STRATEGIES
            ) + " bps")

        if output_dir:
            seed_vals = {
                strat: [data[strat]["mdi"][ni][s_idx] for ni in range(len(n_values))]
                for strat, _ in _STRATEGIES
            }
            fig_s, ax_s = plt.subplots(figsize=(7, 5))
            for strat, _ in _STRATEGIES:
                ax_s.plot(n_values, np.array(seed_vals[strat]) / 1000,
                          marker=_STRAT_MARKER[strat], color=_STRAT_COLOR[strat],
                          label=_STRAT_LABEL[strat])
            ax_s.set_xlabel("Total users N")
            ax_s.set_ylabel("Avg key rate (kbps)")
            ax_s.set_title(f"MDI-QKD (seed={s})")
            ax_s.legend()
            ax_s.grid(True, alpha=0.3)
            plt.tight_layout()
            save_bundle(
                fig_s, os.path.join(output_dir, "relay_placement_exp2"), f"seed{s}",
                title=f"Relay Placement: Centroid vs Boundary vs Weiszfeld (seed={s})",
                assumptions={
                    "Seed": s,
                    "User count sweep range": f"{n_values[0]}-{n_values[-1]}",
                    "Area": f"{area} x {area} km",
                    "Catchment shape": (f"hard disc, radius {catchment_radius:.1f} km"
                                         if catchment_radius is not None
                                         else f"Gaussian, std {spread:.2f} km"),
                    "Runtimes per pair": runtimes,
                    **{
                        f"MDI key rate (bps) — {strat}": dict(zip(n_values, seed_vals[strat]))
                        for strat, _ in _STRATEGIES
                    },
                },
            )

    return data, seeds, graph_data


def plot_exp2(data, n_values, output_dir, area, spread, runtimes, n_seeds, seed, seeds, graph_data,
              error="bars", catchment_radius=None):
    N = np.array(n_values)

    fig, ax = plt.subplots(figsize=(7, 5))

    for strat, _ in _STRATEGIES:
        means = np.array([np.mean(data[strat]["mdi"][i]) for i in range(len(N))]) / 1000
        if error == "bars":
            stds = np.array([np.std(data[strat]["mdi"][i]) for i in range(len(N))]) / 1000
            ax.errorbar(N, means, yerr=stds, label=_STRAT_LABEL[strat],
                        color=_STRAT_COLOR[strat], marker=_STRAT_MARKER[strat],
                        capsize=4, lw=1.5)
        elif error == "shade":
            stds = np.array([np.std(data[strat]["mdi"][i]) for i in range(len(N))]) / 1000
            ax.plot(N, means, color=_STRAT_COLOR[strat], marker=_STRAT_MARKER[strat],
                    lw=1.5, label=_STRAT_LABEL[strat])
            ax.fill_between(N, means - stds, means + stds, alpha=0.2, color=_STRAT_COLOR[strat])
        else:  # iqr
            q1 = np.array([np.percentile(data[strat]["mdi"][i], 25) for i in range(len(N))]) / 1000
            q3 = np.array([np.percentile(data[strat]["mdi"][i], 75) for i in range(len(N))]) / 1000
            ax.plot(N, means, color=_STRAT_COLOR[strat], marker=_STRAT_MARKER[strat],
                    lw=1.5, label=_STRAT_LABEL[strat])
            ax.fill_between(N, q1, q3, alpha=0.2, color=_STRAT_COLOR[strat])
    ax.set_xlabel("Total users N")
    ax.set_ylabel("Avg key rate (kbps)")
    ax.set_title("MDI-QKD")
    ax.legend()
    ax.grid(True, alpha=0.3)

    title = "Relay Placement: Centroid vs Boundary vs Weiszfeld"
    plt.suptitle(title, fontsize=12)
    plt.tight_layout()

    if output_dir:
        save_bundle(
            fig, output_dir, "relay_placement_exp2",
            title=title,
            assumptions={
                "Experiment": "2 — two clusters, K=2 relays, provider-growth model",
                "User count sweep range": f"{n_values[0]}-{n_values[-1]}",
                "Relay placement": f"computed once at N={n_values[0]} per strategy, then frozen",
                "Growth model": "one user at a time, uniform-random catchment, "
                                "catchment membership fixed once assigned",
                "Area": f"{area} x {area} km",
                "Cluster spread (std)": f"{spread:.2f} km",
                "Runtimes per pair": runtimes,
                "Random topologies averaged": n_seeds,
                "Error display": error,
                "Seed (base)": seed,
                "Seeds used": seeds,
                "Final graph per seed (N=n_max, km)": graph_data,
                "MDI key rate (bps) per strategy, N, seed": {
                    strat: {n_values[ni]: dict(zip(seeds, data[strat]["mdi"][ni]))
                            for ni in range(len(n_values))}
                    for strat, _ in _STRATEGIES
                },
            },
            notes=["Relay position is computed once at N=n_min per strategy and held fixed as "
                   "N grows to n_max — models a provider sizing infrastructure for an initial "
                   "deployment and serving subsequent organic growth without re-optimising.",
                   "Boundary strategy displaces each relay 1 std toward the other catchment.",
                   "Weiszfeld strategy is the backbone-coupled geometric median (Equation eq:generalized_weiszfeld), "
                   "starting from each catchment's centroid, with catchment membership held fixed."],
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
    parser.add_argument("--catchment-radius", type=float, default=None,
                        help="Hard catchment radius in km, uniform disc instead of Gaussian spread (exp 1+2)")
    parser.add_argument("--error",   type=str,   default="bars", choices=["bars", "shade", "iqr"],
                        help="Error style: bars (default), shade (+-1 std fill), or iqr (Q1/Q3 fill) (exp 2)")

    args = parser.parse_args()

    if args.seed is None:
        args.seed = int.from_bytes(os.urandom(4), "big") % 100_000

    cfg = load_config(args.config)

    if args.exp == 1:
        n_values = sorted(int(x) for x in args.n_values.split(","))
        results, frozen_pos, frozen_rate = exp1(n_values, args.area, args.grid, cfg,
                                                 args.runtimes, args.seed, args.workers)
        plot_exp1(results, args.area, args.output_dir, args.grid, args.runtimes, args.seed,
                  frozen_pos=frozen_pos, frozen_rate=frozen_rate)

    else:
        spread   = args.spread if args.spread is not None else args.area / 5
        n_values = list(range(args.n_min, args.n_max + 1, args.n_step))
        print(f"\n=== Exp 2: N={n_values[0]}..{n_values[-1]}, spread={spread:.1f} km, "
              f"{args.seeds} seeds ===")
        data, seeds, graph_data = exp2(n_values, args.area, spread, cfg, args.runtimes,
                    args.seed, args.seeds, args.workers, output_dir=args.output_dir,
                    catchment_radius=args.catchment_radius)
        plot_exp2(data, n_values, args.output_dir, args.area, spread, args.runtimes, args.seeds,
                  args.seed, seeds, graph_data, error=args.error, catchment_radius=args.catchment_radius)


if __name__ == "__main__":
    main()
