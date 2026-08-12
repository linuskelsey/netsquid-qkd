"""
Experiment 1 — relay count sweep.

Fixed N users, vary relay count K. Plots average key rate vs K for BB84
(SNSPD and SPAD detector variants) and MDI-QKD. Error bars show std across
Monte Carlo runs (--seeds 1) or across random topologies (--seeds N).
Topology visualisation is produced for every seed x K combination.

BB84 is relay-independent (direct mesh) and is run once per seed, per
detector variant. MDI uses the relay topology and is re-run per K.

Usage:
    python scripts/network/relay_sweep.py [options]

Options:
    --n INT          Number of users (default: 20)
    --k-min INT      Min relay count (default: 1)
    --k-max INT      Max relay count (default: 8)
    --area FLOAT     Area side length in km (default: 10.0)
    --seed INT       Base random seed; random if omitted
    --seeds INT      Random topologies to average over (default: 1)
    --runtimes INT   Monte Carlo runs per pair (default: 20)
    --config PATH    JSON config preset
    --protocol STR   Which protocol(s) to run: bb84, mdi, or both (default: both)
    --detector-eff FLOAT  Override detector efficiency for BOTH protocols with a single custom
                     value, in isolation (skips the baked-in SNSPD/SPAD BB84 pair, runs one
                     BB84 line at this value; also sets it for MDI)
    --tortuosity FLOAT  Mean fibre tortuosity, cable/Euclidean ratio (default: 1.2; 1.0 = off)
    --error          Error style: bars (default), shade (±1σ fill), or iqr (Q1/Q3 fill)
    --workers INT    Worker processes (default: 80% of CPU cores)
    --output-dir DIR Save figure bundle {plot.png, plot.tex, assumptions.md} to directory instead of displaying

Examples:
    python scripts/network/relay_sweep.py --n 20 --k-max 6 --runtimes 20
    python scripts/network/relay_sweep.py --seeds 5 --seed 42 --output-dir results/
    python scripts/network/relay_sweep.py --protocol bb84 --config configs/layer9_spad.json
"""
import argparse
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

_root    = os.path.join(os.path.dirname(__file__), "../..")
_network = os.path.join(_root, "network")
sys.path.insert(0, _root)
sys.path.insert(0, _network)

import time
from lib.plotting import apply_thesis_style, save_bundle
from lib.functions import load_config
from lib.db import DEFAULT_DB_PATH
from lib.progress import Progress
from topology import place_users, optimise_relays, Topology
from bb84_network import run_bb84_network
from mdi_network import run_mdi_network
from visualise_network import draw_mdi, draw_bb84

apply_thesis_style()

# BB84 detector variants swept on every run: (label, detector_efficiency)
DETECTOR_VARIANTS = [("SNSPD", 0.90), ("SPAD", 0.20)]
BB84_COLORS = {"SNSPD": "#377eb8", "SPAD": "#ff7f00"}


def _pair_avgs(pair_rates):
    """Mean key rate per pair (valid runs only). Returns list over pairs."""
    avgs = []
    for rates in pair_rates.values():
        valid = [r for r in rates if r != "nan"]
        if valid:
            avgs.append(sum(valid) / len(valid))
    return avgs


def main():
    parser = argparse.ArgumentParser(description="Relay count sweep (Experiment 1)")
    parser.add_argument("--n",        type=int,   default=20,   help="Number of users (fixed)")
    parser.add_argument("--k-min",    type=int,   default=1,    help="Min relay count")
    parser.add_argument("--k-max",    type=int,   default=8,    help="Max relay count")
    parser.add_argument("--area",     type=float, default=10.0, help="Area side length (km)")
    parser.add_argument("--seed",     type=int,   default=None, help="Base random seed (random if omitted)")
    parser.add_argument("--seeds",    type=int,   default=1,    help="Number of random topologies to average over")
    parser.add_argument("--runtimes", type=int,   default=20,   help="Monte Carlo runs per pair")
    parser.add_argument("--config",     type=str,   default=None, help="Path to JSON config")
    parser.add_argument("--protocol",   type=str,   default="both", choices=["bb84", "mdi", "both"],
                        help="Which protocol(s) to run")
    parser.add_argument("--detector-eff", type=float, default=None,
                        help="Override detector efficiency with a single custom value for both "
                             "protocols, in isolation (replaces the baked-in SNSPD/SPAD BB84 pair)")
    parser.add_argument("--tortuosity", type=float, default=1.2,
                        help="Mean fibre tortuosity (cable/Euclidean ratio). 1.0 = Euclidean; ~1.2 typical urban.")
    parser.add_argument("--error",     type=str,   default="bars", choices=["bars", "shade", "iqr"])
    parser.add_argument("--output-dir", type=str,   default=None, help="Directory to save figures into (skips interactive display)")
    parser.add_argument("--no-figure", action="store_true", help="Skip all figure output (no show, no save)")
    parser.add_argument("--no-p2p-db", action="store_true", help="Disable P2P DB writing")
    parser.add_argument("--no-net-db", action="store_true", help="Disable network DB writing")
    parser.add_argument("--workers",   type=int,   default=None, help="Worker processes (default: 80%% of CPU cores)")
    args = parser.parse_args()

    if args.seed is None:
        args.seed = int.from_bytes(os.urandom(4), "big") % 100000

    cfg      = load_config(args.config)
    cfg["tortuosity_mean"] = args.tortuosity
    K_values = list(range(args.k_min, args.k_max + 1))

    if args.detector_eff is not None:
        cfg["detector_efficiency"] = args.detector_eff
        variants = [(f"eta{args.detector_eff:.2f}", args.detector_eff)]
    else:
        variants = DETECTOR_VARIANTS

    if args.seeds == 1:
        seeds = [args.seed]
    else:
        rng   = np.random.default_rng(args.seed)
        seeds = rng.integers(0, 100_000, size=args.seeds).tolist()

    run_bb84 = args.protocol in ("bb84", "both")
    run_mdi  = args.protocol in ("mdi", "both")

    bb84_per_seed        = {v: [] for v, _ in variants}
    bb84_ok_per_seed     = {v: [] for v, _ in variants}
    bb84_fibre_per_seed  = {v: [] for v, _ in variants}
    mdi_per_seed         = {K: [] for K in K_values}
    mdi_ok_per_seed      = {K: [] for K in K_values}
    mdi_fibre_per_seed   = {K: [] for K in K_values}

    seed_total  = (len(variants) if run_bb84 else 0) + (len(K_values) if run_mdi else 0)
    total_start = time.time()

    _user_pos_by_seed  = {}
    _relay_pos_by_seed = {}

    for s_idx, seed in enumerate(seeds):
        print(f"\n--- Seed {s_idx+1}/{args.seeds}  (seed={seed}) ---")
        seed_start = time.time()
        prog = Progress(seed_total)
        step = 0
        user_pos = place_users(args.n, area_km=args.area, seed=seed)
        _user_pos_by_seed[seed] = np.round(user_pos, 3).tolist()

        if run_bb84:
            topo_bb84 = Topology(user_pos)
            for variant, det_eff in variants:
                prog.update(step, f"BB84-{variant} reference running...")
                cfg_v = dict(cfg)
                cfg_v["detector_efficiency"] = det_eff
                bb84_res = run_bb84_network(
                    topo_bb84, cfg_v, runtimes=args.runtimes, workers=args.workers,
                    p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                    net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                    experiment="relay_sweep", seed=seed, area_km=args.area,
                    config_preset=args.config)
                bp = _pair_avgs(bb84_res["pair_rates"])
                _s_bb84    = np.mean(bp) if bp else 0.0
                _s_bb84_ok = bb84_res["success_rate"] * 100
                bb84_per_seed[variant].append(_s_bb84)
                bb84_ok_per_seed[variant].append(_s_bb84_ok)
                bb84_fibre_per_seed[variant].append(bb84_res["total_fibre_km"])
                step += 1
                prog.update(step, f"BB84-{variant} {_s_bb84/1000:.2f} kbps  ({_s_bb84_ok:.0f}% ok)")

        if run_mdi:
            for K in K_values:
                prog.update(step, f"Relay count: {K}/{K_values[-1]}  MDI running...")
                relay_pos  = optimise_relays(user_pos, K, seed=seed)
                _relay_pos_by_seed.setdefault(seed, {})[K] = np.round(np.array(relay_pos), 3).tolist()
                topo       = Topology(user_pos, relay_pos)

                if args.output_dir and not args.no_figure:
                    _topo_dir = os.path.join(args.output_dir, f"relay_sweep_N{args.n}", f"seed{seed}", "topologies")
                    os.makedirs(_topo_dir, exist_ok=True)
                    fig_m, ax_m = plt.subplots(figsize=(6, 5))
                    draw_mdi(ax_m, topo, tortuosity_mean=args.tortuosity, seed=seed)
                    plt.tight_layout()
                    fig_m.savefig(os.path.join(_topo_dir, f"K{K}_mdi.png"), dpi=150, bbox_inches="tight")
                    plt.close(fig_m)

                    fig_b, ax_b = plt.subplots(figsize=(6, 5))
                    draw_bb84(ax_b, topo, tortuosity_mean=args.tortuosity, seed=seed)
                    plt.tight_layout()
                    fig_b.savefig(os.path.join(_topo_dir, f"K{K}_bb84.png"), dpi=150, bbox_inches="tight")
                    plt.close(fig_b)

                mdi_res    = run_mdi_network(topo, cfg, runtimes=args.runtimes, workers=args.workers,
                                 p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                                 net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                                 experiment="relay_sweep", seed=seed, area_km=args.area,
                                 config_preset=args.config)
                mp         = _pair_avgs(mdi_res["pair_rates"])
                _s_mdi     = np.mean(mp) if mp else 0.0
                _s_mdi_ok  = mdi_res["success_rate"] * 100
                mdi_per_seed[K].append(_s_mdi)
                mdi_ok_per_seed[K].append(_s_mdi_ok)
                mdi_fibre_per_seed[K].append(mdi_res["total_fibre_km"])
                step += 1
                prog.update(step, f"Relay count: {K}/{K_values[-1]}  MDI {_s_mdi/1000:.2f} kbps")

        prog.stop()
        m, s = divmod(int(time.time() - seed_start), 60)
        print(f"✓ Seed {s_idx+1}/{args.seeds} complete  {m}m {s:02d}s")

        if args.output_dir and not args.no_figure:
            fig_s, ax_s = plt.subplots(figsize=(8, 5))
            _seed_assumptions = {
                "Seed": seed,
                "User count (fixed)": args.n,
                "Relay count sweep range": f"{args.k_min}-{args.k_max}",
                "Area": f"{args.area} x {args.area} km",
                "Tortuosity mean": args.tortuosity,
                "Runtimes per pair": args.runtimes,
            }
            if run_bb84:
                for variant, _ in variants:
                    seed_bb84 = [bb84_per_seed[variant][s_idx]] * len(K_values)
                    ax_s.plot(K_values, np.array(seed_bb84) / 1000, '--', color=BB84_COLORS.get(variant, "#4daf4a"),
                              lw=1.5, label=f"BB84-{variant}")
                    _seed_assumptions[f"BB84-{variant} key rate (bps)"] = seed_bb84[0]
            if run_mdi:
                seed_mdi = [mdi_per_seed[K][s_idx] for K in K_values]
                ax_s.plot(K_values, np.array(seed_mdi) / 1000, color="#e41a1c", marker="o", lw=1.5, label="MDI")
                _seed_assumptions["MDI key rate (bps) per K"] = dict(zip(K_values, seed_mdi))
            ax_s.set_yscale("log")
            ax_s.set_xlabel("Relay count K")
            ax_s.set_ylabel("Avg key rate (kbps)")
            ax_s.set_xticks(K_values)
            ax_s.legend()
            ax_s.grid(True, alpha=0.3)
            ax_s.set_title(f"Key Rate vs Relay Count (seed={seed})", fontsize=10)
            plt.tight_layout()
            save_bundle(
                fig_s, os.path.join(args.output_dir, f"relay_sweep_N{args.n}"), f"seed{seed}",
                title=f"Key Rate vs Relay Count (seed={seed})",
                assumptions=_seed_assumptions,
            )

    m, s = divmod(int(time.time() - total_start), 60)
    print(f"✓ complete  total {m}m {s:02d}s")

    _headers = ["K"] + ([f"BB84-{v} kbps" for v, _ in variants] if run_bb84 else []) + (["MDI kbps"] if run_mdi else [])
    print("\n" + "  ".join(f"{h:>13}" for h in _headers))
    print("-" * (15 * len(_headers)))
    for K in K_values:
        row = [f"{K:>13}"]
        if run_bb84:
            for variant, _ in variants:
                row.append(f"{np.mean(bb84_per_seed[variant])/1000:>13.2f}")
        if run_mdi:
            row.append(f"{np.mean(mdi_per_seed[K])/1000:>13.2f}")
        print("  ".join(row))

    K_arr = np.array(K_values)

    bb84_stats = {}
    if run_bb84:
        for variant, _ in variants:
            bb84_stats[variant] = {
                "mean": np.array([np.mean(bb84_per_seed[variant])] * len(K_values)) / 1000,
                "std":  np.array([np.std(bb84_per_seed[variant])]  * len(K_values)) / 1000,
                "q1":   np.array([np.percentile(bb84_per_seed[variant], 25)] * len(K_values)) / 1000,
                "q3":   np.array([np.percentile(bb84_per_seed[variant], 75)] * len(K_values)) / 1000,
            }

    if run_mdi:
        mdi_means = [np.mean(mdi_per_seed[K]) for K in K_values]
        mdi_stds  = [np.std(mdi_per_seed[K])  for K in K_values]
        m_mean = np.array(mdi_means) / 1000
        m_std  = np.array(mdi_stds)  / 1000
        m_q1   = np.array([np.percentile(mdi_per_seed[K], 25) for K in K_values]) / 1000
        m_q3   = np.array([np.percentile(mdi_per_seed[K], 75) for K in K_values]) / 1000

    _ref_variant = variants[0][0]
    bb84_ref = (bb84_stats[_ref_variant]["mean"][0] if run_bb84 and bb84_stats[_ref_variant]["mean"][0] > 0
                else (m_mean[0] if run_mdi and m_mean[0] > 0 else 1.0))

    # --- Figure 1: results ---
    fig, ax1 = plt.subplots(figsize=(8, 5))

    if run_bb84:
        for variant, _ in variants:
            st = bb84_stats[variant]
            ax1.plot(K_arr, st["mean"], '--', color=BB84_COLORS.get(variant, "#4daf4a"), lw=1.5, label=f"BB84-{variant}")
            if args.error == "iqr":
                ax1.fill_between(K_arr, st["q1"], st["q3"], alpha=0.2, color=BB84_COLORS.get(variant, "#4daf4a"))
            else:
                ax1.fill_between(K_arr, st["mean"] - st["std"], st["mean"] + st["std"], alpha=0.2, color=BB84_COLORS.get(variant, "#4daf4a"))

    if run_mdi:
        if args.error == "bars":
            ax1.errorbar(K_arr, m_mean, yerr=m_std, label="MDI", color="#e41a1c",
                         marker="o", capsize=4, lw=1.5)
        elif args.error == "shade":
            ax1.plot(K_arr, m_mean, color="#e41a1c", marker="o", lw=1.5, label="MDI")
            ax1.fill_between(K_arr, m_mean - m_std, m_mean + m_std, alpha=0.2, color="#e41a1c")
        else:  # iqr
            ax1.plot(K_arr, m_mean, color="#e41a1c", marker="o", lw=1.5, label="MDI")
            ax1.fill_between(K_arr, m_q1, m_q3, alpha=0.2, color="#e41a1c")

    ax1.set_yscale("log")
    ax1.set_xlabel("Relay count K")
    ax1.set_ylabel("Avg key rate (kbps)")
    ax1.set_xticks(K_arr)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()
    if run_bb84:
        ax2.plot(K_arr, bb84_stats["SNSPD"]["mean"] / bb84_ref, alpha=0)
    if run_mdi:
        ax2.plot(K_arr, m_mean / bb84_ref, alpha=0)
    ax2.set_ylabel("Relative key rate")
    ax2.set_yscale("log")

    seed_label = f"seed={args.seed}" if args.seeds == 1 else f"{args.seeds} seeds (base={args.seed}): {seeds}"
    plt.title("Key Rate vs Relay Count", fontsize=10)
    plt.tight_layout()

    if not args.no_figure:
        if args.output_dir:
            _assumptions = {
                "User count (fixed)": args.n,
                "Relay count sweep range": f"{args.k_min}-{args.k_max}",
                "Area": f"{args.area} x {args.area} km",
                "Seed": seed_label,
                "Tortuosity mean": args.tortuosity,
                "Runtimes per pair": args.runtimes,
                "Error display": args.error,
                "Protocol(s) run": args.protocol,
                "Fibre loss / detector / dark count / etc": "see configs/ preset used (--config)",
                "Final user positions (km, per seed)": _user_pos_by_seed,
            }
            if run_mdi:
                _assumptions["Relay positions (km, per seed per K)"] = _relay_pos_by_seed
            if run_bb84:
                for variant, _ in variants:
                    _assumptions[f"BB84-{variant} key rate (bps) per seed"] = dict(zip(seeds, bb84_per_seed[variant]))
            if run_mdi:
                _assumptions["MDI key rate (bps) per K per seed"] = {
                    K: dict(zip(seeds, mdi_per_seed[K])) for K in K_values
                }
            save_bundle(
                fig, args.output_dir, f"relay_sweep_N{args.n}",
                title="Key Rate vs Relay Count",
                assumptions=_assumptions,
            )
            print(f"Saved to {os.path.join(args.output_dir, f'relay_sweep_N{args.n}')}")
        else:
            plt.show()

    if args.output_dir and not args.no_figure:
        print(f"Per-seed plots + topologies saved under {os.path.join(args.output_dir, f'relay_sweep_N{args.n}')}/seed<seed>/")


if __name__ == "__main__":
    main()
