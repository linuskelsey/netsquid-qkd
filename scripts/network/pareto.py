"""
Pareto analysis — cost vs key rate frontier.

For a fixed user count N, sweeps relay count K over [k_min, k_max].
Each (K, seed) configuration produces one (deployment cost, avg key rate)
point per protocol. The Pareto frontier — configurations not dominated on
both cost and rate — is extracted per protocol and plotted.

Two deployment questions are answered from the frontier:
  --r-min FLOAT  : given this minimum key rate (bps), find cheapest config
  --c-max FLOAT  : given this budget (USD), find highest-rate config

BB84 is K-independent (direct mesh); it appears as a reference cluster.

Usage:
    python scripts/network/pareto.py [options]

Options:
    --n INT              Fixed user count (default: 15)
    --k-min INT          Min relay count (default: 1)
    --k-max INT          Max relay count (default: 8)
    --area FLOAT         Area side length km (default: 10.0)
    --seed INT           Base random seed (random if omitted)
    --seeds INT          Topologies to average over (default: 5)
    --runtimes INT       MC runs per pair (default: 50)
    --r-min FLOAT        Annotate minimum key rate constraint (bps)
    --c-max FLOAT        Annotate maximum budget constraint (USD)
    --config PATH        JSON config preset
    --detector-tech TECH SPAD | InGaAs | SNSPD
    --source-tech TECH   QD | NV | hSPDC | ideal
    --source-cost FLOAT  USD per source (overrides --source-tech cost)
    --spd-cost FLOAT     USD per SPD (overrides --detector-tech cost)
    --bs-cost FLOAT      USD per beam splitter at MDI relay
    --fibre-cost FLOAT   USD per km of installed fibre
    --sweep-detectors    Sweep all detector tech presets (SPAD, InGaAs, SNSPD)
                           instead of using a single --detector-tech value
    --sweep-sources      Sweep all source tech presets (QD, NV, hSPDC, ideal)
                           instead of using a single --source-tech value
    --workers INT        Worker processes (default: 80% of cores)
    --save PATH          Save figure to file instead of displaying
    --cost-only          Skip simulation; compute cost from topology geometry only

When --sweep-detectors or --sweep-sources are set, the Pareto frontier is
computed over all (K, det_tech, src_tech) combinations for the given N.
This reflects the real deployment decision: choosing relay count AND hardware
technology jointly to minimise cost or maximise rate.

Examples:
    python scripts/network/pareto.py --n 15 --k-min 1 --k-max 8 --seeds 5 --runtimes 50
    python scripts/network/pareto.py --n 20 --sweep-detectors --sweep-sources --r-min 500 --save results/pareto.png
"""
import argparse
import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

_root    = os.path.join(os.path.dirname(__file__), "../..")
_network = os.path.join(_root, "network")
sys.path.insert(0, _root)
sys.path.insert(0, _network)

from lib.functions import load_config
from lib.db import DEFAULT_DB_PATH
from lib.progress import Progress
from topology import place_users, optimise_relays, Topology
from bb84_network import run_bb84_network
from mdi_network import run_mdi_network
from trusted_bb84_network import run_trusted_bb84_network
from cost import component_counts, total_cost, DETECTOR_TECH, SOURCE_TECH, DEFAULT_COSTS


def _compute_cost(res, N, K, protocol, cost_kw):
    counts = component_counts(N, K, protocol)
    return total_cost(counts, res["total_fibre_km"], **cost_kw)["total_usd"]


def _fibre_km_bb84(topo):
    return sum(topo.bb84_link(i, j) for (i, j) in topo.all_pairs())


def _fibre_km_mdi(topo):
    user_relay = sum(
        float(np.linalg.norm(topo.user_pos[i] - topo.relay_pos[topo.user_relay[i]]))
        for i in range(topo.N)
    )
    relay_relay = sum(
        float(np.linalg.norm(topo.relay_pos[k1] - topo.relay_pos[k2]))
        for k1 in range(topo.K) for k2 in range(k1 + 1, topo.K)
    )
    return user_relay + relay_relay


def pareto_frontier(costs, rates):
    """Return indices of non-dominated points, sorted by cost ascending."""
    pts = sorted(enumerate(zip(costs, rates)), key=lambda x: x[1][0])
    frontier_idx = []
    max_rate = -np.inf
    for idx, (c, r) in pts:
        if r > max_rate:
            frontier_idx.append(idx)
            max_rate = r
    return frontier_idx


def answer_constraints(frontier_costs, frontier_rates, r_min=None, c_max=None):
    """Print deployment answers from the Pareto frontier."""
    fc = np.array(frontier_costs)
    fr = np.array(frontier_rates)
    if r_min is not None:
        mask = fr >= r_min
        if mask.any():
            idx = np.argmin(fc[mask])
            c_opt = fc[mask][idx]
            r_opt = fr[mask][idx]
            print(f"  R_min={r_min:.1f} bps  →  cheapest config: ${c_opt/1e6:.3f}M at {r_opt:.2f} bps")
        else:
            print(f"  R_min={r_min:.1f} bps  →  no config on frontier meets this rate")
    if c_max is not None:
        mask = fc <= c_max
        if mask.any():
            idx = np.argmax(fr[mask])
            c_opt = fc[mask][idx]
            r_opt = fr[mask][idx]
            print(f"  C_max=${c_max/1e6:.3f}M  →  best-rate config: {r_opt:.2f} bps at ${c_opt/1e6:.3f}M")
        else:
            print(f"  C_max=${c_max/1e6:.3f}M  →  no config on frontier fits this budget")


def main():
    parser = argparse.ArgumentParser(description="Pareto analysis — cost vs key rate")
    parser.add_argument("--n",            type=int,   default=15)
    parser.add_argument("--k-min",        type=int,   default=1)
    parser.add_argument("--k-max",        type=int,   default=8)
    parser.add_argument("--area",         type=float, default=10.0)
    parser.add_argument("--seed",         type=int,   default=None)
    parser.add_argument("--seeds",        type=int,   default=5)
    parser.add_argument("--runtimes",     type=int,   default=50)
    parser.add_argument("--r-min",        type=float, default=None, help="Min key rate constraint (bps)")
    parser.add_argument("--c-max",        type=float, default=None, help="Max budget constraint (USD)")
    parser.add_argument("--config",       type=str,   default=None)
    parser.add_argument("--detector-tech",    type=str,   default=None, choices=list(DETECTOR_TECH))
    parser.add_argument("--source-tech",      type=str,   default=None, choices=list(SOURCE_TECH))
    parser.add_argument("--sweep-detectors",  action="store_true", help="Sweep all detector tech presets")
    parser.add_argument("--sweep-sources",    action="store_true", help="Sweep all source tech presets")
    parser.add_argument("--source-cost",  type=float, default=None)
    parser.add_argument("--spd-cost",     type=float, default=None)
    parser.add_argument("--bs-cost",      type=float, default=None)
    parser.add_argument("--fibre-cost",   type=float, default=None)
    parser.add_argument("--workers",      type=int,   default=None)
    parser.add_argument("--save",         type=str,   default=None)
    parser.add_argument("--cost-only",    action="store_true")
    args = parser.parse_args()

    if args.seed is None:
        args.seed = int.from_bytes(os.urandom(4), "big") % 100_000

    cfg = load_config(args.config)
    K_values = list(range(args.k_min, args.k_max + 1))

    bs_usd    = args.bs_cost    if args.bs_cost    is not None else DEFAULT_COSTS["bs_usd"]
    fibre_usd = args.fibre_cost if args.fibre_cost is not None else DEFAULT_COSTS["fibre_per_km_usd"]

    # Build hardware configuration grid: list of (det_label, src_label, spd_usd, source_usd, det_efficiency)
    det_options = list(DETECTOR_TECH.keys()) if args.sweep_detectors else [args.detector_tech or "_custom"]
    src_options = list(SOURCE_TECH.keys())   if args.sweep_sources   else [args.source_tech   or "_custom"]

    hw_configs = []
    for det in det_options:
        for src in src_options:
            det_p   = DETECTOR_TECH.get(det, {})
            src_p   = SOURCE_TECH.get(src, {})
            spd_c   = args.spd_cost    if args.spd_cost    is not None else det_p.get("cost_usd",  DEFAULT_COSTS["spd_usd"])
            src_c   = args.source_cost if args.source_cost is not None else src_p.get("cost_usd",  DEFAULT_COSTS["source_usd"])
            det_eff = det_p.get("efficiency", cfg.get("detector_efficiency", 0.85))
            hw_configs.append(dict(det=det, src=src, spd_usd=spd_c, source_usd=src_c,
                                   det_eff=det_eff, bs_usd=bs_usd, fibre_per_km_usd=fibre_usd))

    rng   = np.random.default_rng(args.seed)
    seeds = rng.integers(0, 100_000, size=args.seeds).tolist()

    # points keyed by (K, det, src) → list of (bb84_cost, bb84_rate, mdi_cost, mdi_rate, trusted_cost, trusted_rate)
    all_pts = {}  # (K, det, src) → [(bb84_cost, bb84_rate, mdi_cost, mdi_rate, trusted_cost, trusted_rate), ...]

    total_start = time.time()
    n_steps = args.seeds * len(hw_configs) * (1 + len(K_values))
    prog = Progress(n_steps)
    step = 0

    for s_idx, seed in enumerate(seeds):
        user_pos  = place_users(args.n, area_km=args.area, seed=seed)
        topo_bb84 = Topology(user_pos)

        for hw in hw_configs:
            cfg_hw = dict(cfg)
            cfg_hw["detector_efficiency"] = hw["det_eff"]
            cost_kw = dict(source_usd=hw["source_usd"], spd_usd=hw["spd_usd"],
                           bs_usd=hw["bs_usd"], fibre_per_km_usd=hw["fibre_per_km_usd"])
            det_lbl = hw["det"]
            src_lbl = hw["src"]

            # BB84 — K-independent, one run per (seed, hw)
            prog.update(step, f"seed {s_idx+1}/{args.seeds}  det={det_lbl} src={src_lbl}  BB84...")
            if args.cost_only:
                bb84_fibre    = _fibre_km_bb84(topo_bb84)
                bb84_cost_val = total_cost(component_counts(args.n, 0, "BB84"), bb84_fibre, **cost_kw)["total_usd"]
                bb84_rate_val = float("nan")
            else:
                bb84_res      = run_bb84_network(
                    topo_bb84, cfg_hw, runtimes=args.runtimes, workers=args.workers,
                    p2p_db_path=DEFAULT_DB_PATH, net_db_path=DEFAULT_DB_PATH,
                    experiment="pareto", seed=seed, area_km=args.area,
                    config_preset=args.config)
                bb84_cost_val = _compute_cost(bb84_res, args.n, 0, "BB84", cost_kw)
                bb84_rate_val = bb84_res["avg_key_rate"]
            step += 1

            for K in K_values:
                prog.update(step, f"seed {s_idx+1}/{args.seeds}  det={det_lbl} src={src_lbl}  K={K}...")
                relay_pos = optimise_relays(user_pos, K, seed=seed)
                topo_mdi  = Topology(user_pos, relay_pos)

                if args.cost_only:
                    mdi_fibre        = _fibre_km_mdi(topo_mdi)
                    mdi_cost_val     = total_cost(component_counts(args.n, K, "MDI"),         mdi_fibre, **cost_kw)["total_usd"]
                    trusted_cost_val = total_cost(component_counts(args.n, K, "trusted_BB84"), mdi_fibre, **cost_kw)["total_usd"]
                    mdi_rate_val = trusted_rate_val = float("nan")
                else:
                    mdi_res     = run_mdi_network(
                        topo_mdi, cfg_hw, runtimes=args.runtimes, workers=args.workers,
                        p2p_db_path=DEFAULT_DB_PATH, net_db_path=DEFAULT_DB_PATH,
                        experiment="pareto", seed=seed, area_km=args.area,
                        config_preset=args.config)
                    trusted_res = run_trusted_bb84_network(
                        topo_mdi, cfg_hw, runtimes=args.runtimes, workers=args.workers,
                        p2p_db_path=DEFAULT_DB_PATH, net_db_path=DEFAULT_DB_PATH,
                        experiment="pareto", seed=seed, area_km=args.area,
                        config_preset=args.config)
                    mdi_cost_val     = _compute_cost(mdi_res,     args.n, K, "MDI",         cost_kw)
                    trusted_cost_val = _compute_cost(trusted_res, args.n, K, "trusted_BB84", cost_kw)
                    mdi_rate_val     = mdi_res["avg_key_rate"]
                    trusted_rate_val = trusted_res["avg_key_rate"]

                key = (K, det_lbl, src_lbl)
                all_pts.setdefault(key, []).append(
                    (bb84_cost_val, bb84_rate_val,
                     mdi_cost_val, mdi_rate_val,
                     trusted_cost_val, trusted_rate_val))
                step += 1

    prog.stop()
    m, s = divmod(int(time.time() - total_start), 60)
    print(f"✓ complete  total {m}m {s:02d}s")

    # Average over seeds per (K, det, src) config
    configs = sorted(all_pts.keys())  # (K, det, src)

    def _mean_col(pts_list, idx):
        vals = [p[idx] for p in pts_list if not np.isnan(p[idx])]
        return np.mean(vals) if vals else float("nan")

    avg = {}
    for key in configs:
        pts = all_pts[key]
        avg[key] = dict(
            bb84_cost=_mean_col(pts, 0), bb84_rate=_mean_col(pts, 1),
            mdi_cost =_mean_col(pts, 2), mdi_rate =_mean_col(pts, 3),
            tbb84_cost=_mean_col(pts,4), tbb84_rate=_mean_col(pts, 5),
        )

    mdi_costs     = np.array([avg[k]["mdi_cost"]   for k in configs])
    mdi_rates     = np.array([avg[k]["mdi_rate"]   for k in configs])
    trusted_costs = np.array([avg[k]["tbb84_cost"] for k in configs])
    trusted_rates = np.array([avg[k]["tbb84_rate"] for k in configs])
    bb84_costs    = np.array([avg[k]["bb84_cost"]  for k in configs])
    bb84_rates    = np.array([avg[k]["bb84_rate"]  for k in configs])

    # Pareto frontiers over all (K, det, src) configurations
    mdi_fidx     = pareto_frontier(mdi_costs,     mdi_rates)
    trusted_fidx = pareto_frontier(trusted_costs, trusted_rates)
    bb84_fidx    = pareto_frontier(bb84_costs,    bb84_rates)

    mdi_fc,     mdi_fr     = mdi_costs[mdi_fidx],     mdi_rates[mdi_fidx]
    trusted_fc, trusted_fr = trusted_costs[trusted_fidx], trusted_rates[trusted_fidx]
    bb84_fc,    bb84_fr    = bb84_costs[bb84_fidx],   bb84_rates[bb84_fidx]

    if args.r_min is not None or args.c_max is not None:
        print("\nMDI Pareto answers:")
        answer_constraints(mdi_fc, mdi_fr, args.r_min, args.c_max)
        print("Trusted BB84 Pareto answers:")
        answer_constraints(trusted_fc, trusted_fr, args.r_min, args.c_max)
        print("BB84 Pareto answers:")
        answer_constraints(bb84_fc, bb84_fr, args.r_min, args.c_max)

    # --- Figure ---
    fig, ax = plt.subplots(figsize=(10, 6))

    det_list = det_options
    src_list = src_options
    det_markers = {"SPAD": "o", "InGaAs": "s", "SNSPD": "^", "_custom": "D"}
    src_cmaps   = {"QD": "#e41a1c", "NV": "#ff7f00", "hSPDC": "#984ea3",
                   "ideal": "#a65628", "_custom": "#888888"}

    # Scatter averaged points per (K, det, src): colour by det, marker by src
    for i, key in enumerate(configs):
        K, det, src = key
        col    = src_cmaps.get(src, "#888888")
        marker = det_markers.get(det, "o")
        ax.scatter(avg[key]["mdi_cost"]   / 1e6, avg[key]["mdi_rate"],
                   color=col, marker=marker, s=60, edgecolors="k", linewidths=0.5,
                   zorder=4, alpha=0.85)
        ax.scatter(avg[key]["tbb84_cost"] / 1e6, avg[key]["tbb84_rate"],
                   color=col, marker=marker, s=60, edgecolors="k", linewidths=0.5,
                   zorder=4, alpha=0.45)
        ax.scatter(avg[key]["bb84_cost"]  / 1e6, avg[key]["bb84_rate"],
                   color="#377eb8", marker=marker, s=60, edgecolors="k", linewidths=0.5,
                   zorder=4, alpha=0.45)
        # Annotate K on MDI points only
        ax.annotate(f"K={K}", (avg[key]["mdi_cost"] / 1e6, avg[key]["mdi_rate"]),
                    textcoords="offset points", xytext=(3, 3), fontsize=6, color=col)

    # Pareto frontiers
    if not args.cost_only:
        ax.step(mdi_fc / 1e6,     mdi_fr,     where="post", color="#e41a1c", lw=2.5,
                label="MDI Pareto frontier",          zorder=6)
        ax.step(trusted_fc / 1e6, trusted_fr, where="post", color="#4daf4a", lw=2.5,
                label="Trusted BB84 Pareto frontier", zorder=6)
        ax.step(bb84_fc / 1e6,    bb84_fr,    where="post", color="#377eb8", lw=2.5,
                ls="--", label="BB84 Pareto frontier", zorder=6)

    # Constraint annotations
    if args.r_min is not None:
        ax.axhline(args.r_min, color="grey", lw=1, ls="--", alpha=0.7, zorder=3)
        ax.text(ax.get_xlim()[1] if ax.get_xlim()[1] > 0 else 1,
                args.r_min, f"  $R_{{\\min}}$={args.r_min:.1f} bps",
                va="bottom", fontsize=8, color="grey")
    if args.c_max is not None:
        ax.axvline(args.c_max / 1e6, color="grey", lw=1, ls="--", alpha=0.7, zorder=3)
        ax.text(args.c_max / 1e6, ax.get_ylim()[1] if ax.get_ylim()[1] > 0 else 1,
                f"$C_{{\\max}}$=${args.c_max/1e6:.2f}$M",
                va="top", ha="left", fontsize=8, color="grey")

    # Legend
    legend_handles = [
        plt.Line2D([0], [0], color="#e41a1c", lw=2.5, label="MDI frontier"),
        plt.Line2D([0], [0], color="#4daf4a", lw=2.5, label="Trusted BB84 frontier"),
        plt.Line2D([0], [0], color="#377eb8", lw=2.5, ls="--", label="BB84 frontier"),
    ]
    if args.sweep_sources:
        for src, col in src_cmaps.items():
            if src in src_options:
                legend_handles.append(
                    plt.Line2D([0], [0], marker="o", color=col, lw=0, markersize=7,
                               label=f"src={src}"))
    if args.sweep_detectors:
        for det, mk in det_markers.items():
            if det in det_options:
                legend_handles.append(
                    plt.Line2D([0], [0], marker=mk, color="grey", lw=0, markersize=7,
                               label=f"det={det}"))

    ax.legend(handles=legend_handles, fontsize=8, loc="upper left", ncol=2)
    ax.grid(True, alpha=0.3)

    seed_label = f"{args.seeds} seeds (base={args.seed})"
    hw_label   = ("det∈{" + ",".join(det_options) + "}  src∈{" + ",".join(src_options) + "}"
                  if (args.sweep_detectors or args.sweep_sources) else
                  f"det={det_options[0]}  src={src_options[0]}")
    ax.set_xlabel("Total deployment cost (M$\\$$)", fontsize=11)
    ax.set_ylabel("Average key rate (bps)",          fontsize=11)
    ax.set_title(
        f"Cost–rate Pareto frontier  |  N={args.n}, "
        f"K∈[{args.k_min},{args.k_max}], {args.area}×{args.area} km, {seed_label}\n"
        f"{hw_label}  |  filled=MDI, faded=Trusted BB84/BB84",
        fontsize=8
    )
    fig.tight_layout()

    if args.save:
        fig.savefig(args.save, dpi=150)
        print(f"Saved {args.save}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
