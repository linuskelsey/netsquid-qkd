"""
Relay placement analysis.

Experiment 1 — single cluster, K=1 relay.
    Provider-growth model: draws n_min users into a single catchment (the
    whole area), places the relay once via the chosen strategies (centroid,
    Weiszfeld — the plain single-facility geometric median at K=1, no backbone
    term), then FREEZES relay position and grows the network one user at a
    time (uniform-random within the catchment) up to n_max. Same growth model
    and output format as Experiment 2, restricted to K=1 (no boundary
    strategy — it needs a second catchment to displace toward).

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

Experiment 2 options:
    --n-min INT        Min total users (default: 6)
    --n-max INT        Max total users (default: 30)
    --n-step INT       Step size (default: 2)

Experiment 1+2 options:
    --seeds INT        Random topologies to average over (default: 5)
    --spread FLOAT     Catchment Gaussian std in km (default: area/5); ignored if --catchment-radius given
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


# ─── shared growth-comparison core (K-general) ──────────────────────────────────

_STRAT_COLOR  = {"centroid": "#e41a1c", "boundary": "#377eb8", "weiszfeld": "#4daf4a"}
_STRAT_MARKER = {"centroid": "o",       "boundary": "s",       "weiszfeld": "^"}
_STRAT_LABEL  = {
    "centroid":  "Centroid",
    "boundary":  "Boundary (1 std toward other catchment)",
    "weiszfeld": "Weiszfeld (backbone-coupled)",
}


def _strat_label(strat, K):
    """Weiszfeld has no backbone term at K=1 — it's the plain geometric median there."""
    if strat == "weiszfeld" and K == 1:
        return "Weiszfeld (geometric median)"
    return _STRAT_LABEL[strat]


def _growth_comparison(n_values, area, spread, cfg, runtimes, seed, n_seeds, workers, K, strategy_names,
                        output_dir=None, output_subdir="relay_placement", catchment_radius=None):
    """
    Provider-growth model, K-general: relay(s) placed once at n_min per
    strategy, then frozen; network grows one user at a time (uniform-random
    catchment) up to n_max. Compares the given strategies for MDI-QKD.
    Returns dict: strategy → list[list[float]] (seeds × N).
    """
    strategies = [(name, RELAY_STRATEGIES[name]) for name in strategy_names]
    rng   = np.random.default_rng(seed)
    seeds = rng.integers(0, 100_000, size=n_seeds).tolist()

    data = {
        strat: {"mdi": [[] for _ in n_values]}
        for strat, _ in strategies
    }
    graph_data = {}
    n_min = n_values[0]
    n_max = n_values[-1]

    for s_idx, s in enumerate(seeds):
        print(f"\n--- Seed {s_idx+1}/{n_seeds} (seed={s}) ---")
        user_pos_full, labels_full, _ = grow_catchments(n_min, n_max, K, area, spread, s,
                                                          catchment_radius_km=catchment_radius)

        relay_by_strat = {
            strat: relay_fn(user_pos_full[:n_min], labels_full[:n_min], K)
            for strat, relay_fn in strategies
        }

        for ni, n in enumerate(n_values):
            user_pos = user_pos_full[:n]
            labels   = labels_full[:n]

            for strat, _ in strategies:
                relay_pos = relay_by_strat[strat]
                topo      = Topology(user_pos, relay_pos, user_relay=labels)

                if output_dir:
                    _topo_dir = os.path.join(output_dir, output_subdir, f"seed{s}", "topologies")
                    os.makedirs(_topo_dir, exist_ok=True)
                    fig_m, ax_m = plt.subplots(figsize=(6, 5))
                    draw_mdi(ax_m, topo, strategy=strat.capitalize(), seed=s)
                    plt.tight_layout()
                    fig_m.savefig(os.path.join(_topo_dir, f"N{n}_{strat}_mdi.png"), dpi=150, bbox_inches="tight")
                    plt.close(fig_m)

                    fig_b, ax_b = plt.subplots(figsize=(6, 5))
                    draw_bb84(ax_b, topo, strategy=strat.capitalize(), seed=s)
                    plt.tight_layout()
                    fig_b.savefig(os.path.join(_topo_dir, f"N{n}_{strat}_bb84.png"), dpi=150, bbox_inches="tight")
                    plt.close(fig_b)

                mdi_res = run_mdi_network(topo, cfg, runtimes=runtimes, workers=workers,
                                          p2p_db_path=None, net_db_path=None)

                data[strat]["mdi"][ni].append(_avg_rate(mdi_res["pair_rates"]))

            if n == n_max:
                graph_data[s] = {
                    "user_positions": np.round(user_pos, 3).tolist(),
                    "catchment_labels": labels.tolist(),
                    **{
                        f"relay_positions_{strat}": np.round(relay_by_strat[strat], 3).tolist()
                        for strat, _ in strategies
                    },
                }

            print(f"  N={n:3d}  MDI  " + "  ".join(
                f"{strat}={np.mean(data[strat]['mdi'][ni])/1000:.2f}k" for strat, _ in strategies
            ) + " bps")

        if output_dir:
            seed_vals = {
                strat: [data[strat]["mdi"][ni][s_idx] for ni in range(len(n_values))]
                for strat, _ in strategies
            }
            fig_s, ax_s = plt.subplots(figsize=(7, 5))
            for strat, _ in strategies:
                ax_s.plot(n_values, np.array(seed_vals[strat]) / 1000,
                          marker=_STRAT_MARKER[strat], color=_STRAT_COLOR[strat],
                          label=_strat_label(strat, K))
            ax_s.set_xlabel("Total users N")
            ax_s.set_ylabel("Avg key rate (kbps)")
            ax_s.set_title(f"MDI-QKD (seed={s})")
            ax_s.legend()
            ax_s.grid(True, alpha=0.3)
            plt.tight_layout()
            save_bundle(
                fig_s, os.path.join(output_dir, output_subdir), f"seed{s}",
                title=f"Relay Placement: {' vs '.join(_STRAT_LABEL[n].split(' (')[0] for n in strategy_names)} (seed={s})",
                assumptions={
                    "Seed": s,
                    "K (relays)": K,
                    "User count sweep range": f"{n_values[0]}-{n_values[-1]}",
                    "Area": f"{area} x {area} km",
                    "Catchment shape": (f"hard disc, radius {catchment_radius:.1f} km"
                                         if catchment_radius is not None
                                         else f"Gaussian, std {spread:.2f} km"),
                    "Runtimes per pair": runtimes,
                    **{
                        f"MDI key rate (bps) — {strat}": dict(zip(n_values, seed_vals[strat]))
                        for strat, _ in strategies
                    },
                },
            )

    return data, seeds, graph_data


def _plot_growth_comparison(data, n_values, output_dir, area, spread, runtimes, n_seeds, seed, seeds,
                             graph_data, K, strategy_names, output_subdir="relay_placement",
                             error="bars", catchment_radius=None):
    N = np.array(n_values)
    strategies = [(name, RELAY_STRATEGIES[name]) for name in strategy_names]

    fig, ax = plt.subplots(figsize=(7, 5))

    for strat, _ in strategies:
        means = np.array([np.mean(data[strat]["mdi"][i]) for i in range(len(N))]) / 1000
        if error == "bars":
            stds = np.array([np.std(data[strat]["mdi"][i]) for i in range(len(N))]) / 1000
            ax.errorbar(N, means, yerr=stds, label=_strat_label(strat, K),
                        color=_STRAT_COLOR[strat], marker=_STRAT_MARKER[strat],
                        capsize=4, lw=1.5)
        elif error == "shade":
            stds = np.array([np.std(data[strat]["mdi"][i]) for i in range(len(N))]) / 1000
            ax.plot(N, means, color=_STRAT_COLOR[strat], marker=_STRAT_MARKER[strat],
                    lw=1.5, label=_strat_label(strat, K))
            ax.fill_between(N, means - stds, means + stds, alpha=0.2, color=_STRAT_COLOR[strat])
        else:  # iqr
            q1 = np.array([np.percentile(data[strat]["mdi"][i], 25) for i in range(len(N))]) / 1000
            q3 = np.array([np.percentile(data[strat]["mdi"][i], 75) for i in range(len(N))]) / 1000
            ax.plot(N, means, color=_STRAT_COLOR[strat], marker=_STRAT_MARKER[strat],
                    lw=1.5, label=_strat_label(strat, K))
            ax.fill_between(N, q1, q3, alpha=0.2, color=_STRAT_COLOR[strat])
    ax.set_xlabel("Total users N")
    ax.set_ylabel("Avg key rate (kbps)")
    ax.set_title("MDI-QKD")
    ax.legend()
    ax.grid(True, alpha=0.3)

    strat_title = " vs ".join(_STRAT_LABEL[n].split(" (")[0] for n in strategy_names)
    title = f"Relay Placement: {strat_title}"
    plt.suptitle(title, fontsize=12)
    plt.tight_layout()

    if output_dir:
        save_bundle(
            fig, output_dir, output_subdir,
            title=title,
            assumptions={
                "Experiment": f"K={K} relay(s), provider-growth model",
                "Strategies compared": strategy_names,
                "User count sweep range": f"{n_values[0]}-{n_values[-1]}",
                "Relay placement": f"computed once at N={n_values[0]} per strategy, then frozen",
                "Growth model": "one user at a time, uniform-random catchment, "
                                "catchment membership fixed once assigned",
                "Area": f"{area} x {area} km",
                "Catchment shape": (f"hard disc, radius {catchment_radius:.1f} km"
                                     if catchment_radius is not None
                                     else f"Gaussian, std {spread:.2f} km"),
                "Runtimes per pair": runtimes,
                "Random topologies averaged": n_seeds,
                "Error display": error,
                "Seed (base)": seed,
                "Seeds used": seeds,
                "Final graph per seed (N=n_max, km)": graph_data,
                "MDI key rate (bps) per strategy, N, seed": {
                    strat: {n_values[ni]: dict(zip(seeds, data[strat]["mdi"][ni]))
                            for ni in range(len(n_values))}
                    for strat, _ in strategies
                },
            },
            notes=["Relay position is computed once at N=n_min per strategy and held fixed as "
                   "N grows to n_max — models a provider sizing infrastructure for an initial "
                   "deployment and serving subsequent organic growth without re-optimising."] +
                  (["Boundary strategy displaces each relay 1 std toward the other catchment(s)."]
                   if "boundary" in strategy_names else []) +
                  ([("Weiszfeld strategy is the backbone-coupled geometric median "
                     "(Equation eq:generalized_weiszfeld), starting from each catchment's centroid, "
                     "with catchment membership held fixed."
                     ) if K > 1 else
                    ("Weiszfeld strategy is the plain single-facility geometric median "
                     "(Equation eq:weiszfeld) — no backbone term exists at K=1.")]
                   if "weiszfeld" in strategy_names else []),
        )
    else:
        plt.show()


# ─── Experiment 1 — single cluster, K=1 ─────────────────────────────────────────

def exp1(n_values, area, spread, cfg, runtimes, seed, n_seeds, workers, output_dir=None,
         catchment_radius=None):
    return _growth_comparison(n_values, area, spread, cfg, runtimes, seed, n_seeds, workers,
                               K=1, strategy_names=["centroid", "weiszfeld"], output_dir=output_dir,
                               output_subdir="relay_placement_exp1", catchment_radius=catchment_radius)


def plot_exp1(data, n_values, output_dir, area, spread, runtimes, n_seeds, seed, seeds, graph_data,
              error="bars", catchment_radius=None):
    _plot_growth_comparison(data, n_values, output_dir, area, spread, runtimes, n_seeds, seed, seeds,
                             graph_data, K=1, strategy_names=["centroid", "weiszfeld"],
                             output_subdir="relay_placement_exp1", error=error,
                             catchment_radius=catchment_radius)


# ─── Experiment 2 — two clusters, K=2 ───────────────────────────────────────────

def exp2(n_values, area, spread, cfg, runtimes, seed, n_seeds, workers, output_dir=None,
         catchment_radius=None):
    return _growth_comparison(n_values, area, spread, cfg, runtimes, seed, n_seeds, workers,
                               K=2, strategy_names=["centroid", "boundary", "weiszfeld"],
                               output_dir=output_dir, output_subdir="relay_placement_exp2",
                               catchment_radius=catchment_radius)


def plot_exp2(data, n_values, output_dir, area, spread, runtimes, n_seeds, seed, seeds, graph_data,
              error="bars", catchment_radius=None):
    _plot_growth_comparison(data, n_values, output_dir, area, spread, runtimes, n_seeds, seed, seeds,
                             graph_data, K=2, strategy_names=["centroid", "boundary", "weiszfeld"],
                             output_subdir="relay_placement_exp2", error=error,
                             catchment_radius=catchment_radius)


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

    # Exp 2
    parser.add_argument("--n-min",   type=int,   default=6,    help="Min users (exp 2)")
    parser.add_argument("--n-max",   type=int,   default=30,   help="Max users (exp 2)")
    parser.add_argument("--n-step",  type=int,   default=2,    help="User count step (exp 2)")

    # Exp 1+2
    parser.add_argument("--seeds",   type=int,   default=5,    help="Topologies to average")
    parser.add_argument("--spread",  type=float, default=None, help="Catchment std in km (default: area/5)")
    parser.add_argument("--catchment-radius", type=float, default=None,
                        help="Hard catchment radius in km, uniform disc instead of Gaussian spread")
    parser.add_argument("--error",   type=str,   default="bars", choices=["bars", "shade", "iqr"],
                        help="Error style: bars (default), shade (+-1 std fill), or iqr (Q1/Q3 fill)")

    args = parser.parse_args()

    if args.seed is None:
        args.seed = int.from_bytes(os.urandom(4), "big") % 100_000

    cfg    = load_config(args.config)
    spread = args.spread if args.spread is not None else args.area / 5

    if args.exp == 1:
        n_values = sorted(int(x) for x in args.n_values.split(","))
        run_fn, plot_fn = exp1, plot_exp1
    else:
        n_values = list(range(args.n_min, args.n_max + 1, args.n_step))
        run_fn, plot_fn = exp2, plot_exp2

    print(f"\n=== Exp {args.exp}: N={n_values[0]}..{n_values[-1]}, spread={spread:.1f} km, "
          f"{args.seeds} seeds ===")
    data, seeds, graph_data = run_fn(n_values, args.area, spread, cfg, args.runtimes,
                args.seed, args.seeds, args.workers, output_dir=args.output_dir,
                catchment_radius=args.catchment_radius)
    plot_fn(data, n_values, args.output_dir, args.area, spread, args.runtimes, args.seeds,
            args.seed, seeds, graph_data, error=args.error, catchment_radius=args.catchment_radius)


if __name__ == "__main__":
    main()
