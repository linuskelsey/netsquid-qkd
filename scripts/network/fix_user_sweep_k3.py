"""
One-off repair for the user_sweep K-mismatch bug (see network/topology.py
assign_nearest_catchment / grow_catchments): every K in --k used to draw its
own independent user layout, so K=2 and K=3 curves weren't a like-for-like
relay-count comparison. BB84 and MDI K=2 used K_ref's draw and are correct
as-is; only MDI K=3 needs redoing on that same K_ref layout.

Does NOT touch BB84 or MDI K=2 data (pulled straight from the existing
top-level assumptions.md), and does NOT delete anything from the DB — the old
mismatched K=3 rows are left in place (harmless for other purposes, they just
don't feed the dissertation figures). Only recomputes MDI K=3, inserting
fresh rows, and rewrites the K=3 topology PNGs plus the per-seed and
top-level plot bundles.

Usage:
    python scripts/network/fix_user_sweep_k3.py \
        --output-dir docs/figures/August/final-figs/user_sweep_K2-3
"""
import argparse
import ast
import os
import re
import sqlite3
import sys

import numpy as np
import matplotlib.pyplot as plt

_root    = os.path.join(os.path.dirname(__file__), "../..")
_network = os.path.join(_root, "network")
sys.path.insert(0, _root)
sys.path.insert(0, _network)

from lib.plotting import apply_thesis_style, save_bundle
from lib.functions import load_config
from lib.db import DEFAULT_DB_PATH
from topology import grow_catchments, catchment_anchors, assign_nearest_catchment, RELAY_STRATEGIES, Topology
from mdi_network import run_mdi_network
from visualise_network import draw_mdi

apply_thesis_style()

DETECTOR_VARIANTS = [("SNSPD", 0.90), ("SPAD", 0.20)]
BB84_COLORS = {"SNSPD": "#377eb8", "SPAD": "#ff7f00"}
MDI_COLORS  = ["#e41a1c", "#984ea3", "#a65628", "#f781bf", "#999999"]
MDI_MARKERS = ["o", "s", "^", "D", "v"]

K_BAD = 3  # the mis-drawn K to redo


def _pair_avgs(pair_rates):
    """Same statistic user_sweep.py uses: mean-of-means (average per pair
    first, filtering failed "nan" runs, then average across pairs) — NOT a
    flat pool of every individual run, so it matches the BB84/K_ref numbers
    pulled from assumptions.md."""
    avgs = []
    for rates in pair_rates.values():
        valid = [r for r in rates if r != "nan"]
        if valid:
            avgs.append(sum(valid) / len(valid))
    return avgs


def parse_assumptions(md_path):
    """Pull the {label: value} pairs back out of a save_bundle assumptions.md.
    Values were written via f"{value}", which for dict/list literals is a
    valid Python literal (ast.literal_eval round-trips it)."""
    out = {}
    pattern = re.compile(r"^- \*\*(.+?)\*\*: (.*)$")
    with open(md_path) as f:
        for line in f:
            m = pattern.match(line.rstrip("\n"))
            if not m:
                continue
            label, raw = m.group(1), m.group(2)
            try:
                out[label] = ast.literal_eval(raw)
            except (ValueError, SyntaxError):
                out[label] = raw  # plain string field, keep as-is
    return out


def bootstrap_from_db(seed_dirs, N_values, area_km, K_ref):
    """Reconstruct BB84-SNSPD/SPAD + MDI K_ref per-seed-per-N data straight
    from the DB, for when no top-level assumptions.md exists yet (e.g. the
    run crashed before finishing all seeds).

    Must match the exact statistic used everywhere else (_pair_avgs then
    mean): average within each pair first (successful MC runs only), then
    average those per-pair means across pairs. network_results.avg_key_rate
    is a DIFFERENT statistic (flat pool of every individual run) and would
    silently introduce a methodology mismatch against the freshly-simulated
    K=3 curve — so this recomputes from p2p_results directly instead.
    Each pair's MC runs share one run_id (see insert_p2p_rows); the variant
    isn't stored on network_results directly, but every row in a given
    net_run_id shares one detector_eff_z, so that identifies SNSPD (0.90)
    vs SPAD (0.20).
    """
    conn = sqlite3.connect(DEFAULT_DB_PATH)
    net_q = """
        SELECT net_run_id, protocol, k_relays,
               (SELECT detector_eff_z FROM p2p_results pr WHERE pr.net_run_id = nr.net_run_id LIMIT 1) as det_eff
        FROM network_results nr
        WHERE nr.experiment='user_sweep' AND nr.area_km=? AND nr.seed=? AND nr.n_users=?
        ORDER BY nr.row_id
    """
    pair_mean_q = """
        SELECT AVG(key_rate) FROM p2p_results
        WHERE net_run_id=? AND status='success'
        GROUP BY run_id
    """
    bb84 = {v: {N: {} for N in N_values} for v, _ in DETECTOR_VARIANTS}
    mdi_k2 = {N: {} for N in N_values}
    missing = []
    for seed in seed_dirs:
        for N in N_values:
            net_rows = conn.execute(net_q, (area_km, seed, N)).fetchall()
            got = {v: False for v, _ in DETECTOR_VARIANTS}
            got_k2 = False
            for net_run_id, protocol, k_relays, det_eff in net_rows:
                pair_means = [r[0] for r in conn.execute(pair_mean_q, (net_run_id,)).fetchall() if r[0] is not None]
                rate = sum(pair_means) / len(pair_means) if pair_means else 0.0
                if protocol == "BB84":
                    for variant, eff in DETECTOR_VARIANTS:
                        if det_eff is not None and abs(det_eff - eff) < 1e-6:
                            bb84[variant][N][seed] = rate
                            got[variant] = True
                elif protocol == "MDI" and k_relays == K_ref:
                    mdi_k2[N][seed] = rate
                    got_k2 = True
            if not all(got.values()) or not got_k2:
                missing.append((seed, N))
    conn.close()
    if missing:
        sys.exit(f"bootstrap_from_db: missing BB84/MDI K={K_ref} rows for (seed, N) = {missing} "
                  f"— can't reconstruct without a completed assumptions.md")
    return bb84, mdi_k2


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", required=True,
                    help="e.g. docs/figures/August/final-figs/user_sweep_K2-3")
    p.add_argument("--dry-run", action="store_true",
                    help="Print what would be recomputed, run nothing")
    p.add_argument("--workers", type=int, default=8, help="Worker processes (default: 8, matching original run)")
    p.add_argument("--seeds", type=str, default=None,
                    help="Comma-separated subset of seeds to (re)simulate, e.g. --seeds 39660. "
                         "Default: all seeds found on disk. Other seeds' data is pulled unchanged "
                         "from the existing assumptions.md.")
    args = p.parse_args()

    bundle_dir = args.output_dir.rstrip("/")
    top_md = os.path.join(bundle_dir, "assumptions.md")
    if not os.path.exists(top_md):
        sys.exit(f"Top-level assumptions.md not found at {top_md} — run hasn't finished yet?")

    A = parse_assumptions(top_md)

    K_list = A["Relay counts (K)"]
    K_ref  = K_list[0]
    K_tag  = "-".join(str(k) for k in K_list)
    if K_BAD not in K_list:
        sys.exit(f"K={K_BAD} not in this run's K_list {K_list} — nothing to fix")

    n_lo, n_hi_step = A["User count sweep range"].split("-")
    n_min = int(n_lo)
    n_max, step_str = n_hi_step.split(" (step ")
    n_max = int(n_max)
    n_step = int(step_str.rstrip(")"))
    N_values = list(range(n_min, n_max + 1, n_step))

    area_km  = float(A["Area"].split("×")[0])
    strategy = A["Relay placement"].split(" via ")[1].split(",")[0]
    spread_str = A["Catchment shape"]
    spread_km = float(spread_str.split("std ")[1].split(" km")[0]) if "std" in spread_str else area_km / 5
    tortuosity = float(A["Tortuosity mean"])
    runtimes   = int(A["Runtimes per pair"])
    error_style = A["Error display"]

    # seeds: discover from the per-seed subfolders actually on disk
    seed_dirs = sorted(
        int(d[4:]) for d in os.listdir(bundle_dir)
        if d.startswith("seed") and os.path.isdir(os.path.join(bundle_dir, d))
    )
    sim_seeds = sorted(int(s) for s in args.seeds.split(",")) if args.seeds else seed_dirs
    unknown = set(sim_seeds) - set(seed_dirs)
    if unknown:
        sys.exit(f"--seeds {sorted(unknown)} not found on disk (have {seed_dirs})")

    print(f"Seeds found on disk: {seed_dirs}")
    print(f"Seeds being (re)simulated this run: {sim_seeds}"
          + (f"  (rest pulled unchanged from {top_md})" if sim_seeds != seed_dirs else ""))
    print(f"K_list={K_list}  K_ref={K_ref}  N_values={N_values}  area={area_km}  "
          f"spread={spread_km}  strategy={strategy}  runtimes={runtimes}  tortuosity={tortuosity}")

    if args.dry_run:
        print(f"\n--dry-run: would run MDI K={K_BAD} for {len(sim_seeds)} seeds x "
              f"{len(N_values)} N-values = {len(sim_seeds) * len(N_values)} sim points, "
              f"runtimes={runtimes} each. No sim run, no writes.")
        return

    # --- pull the already-correct BB84 + MDI K_ref data straight from assumptions.md ---
    bb84_per_seed = {}
    for variant, _ in DETECTOR_VARIANTS:
        bb84_per_seed[variant] = A[f"BB84-{variant} key rate (bps) per N per seed"]
    mdi_per_seed = {K_ref: A[f"MDI K={K_ref} key rate (bps) per N per seed"]}

    cfg = load_config(None)
    cfg["tortuosity_mean"] = tortuosity

    # Baseline K_BAD data: pull from the existing assumptions.md if this is a
    # patch run (--seeds given), so untouched seeds keep their prior (already
    # correct) values; missing/first-run fields default to empty.
    existing_k3 = A.get(f"MDI K={K_BAD} key rate (bps) per N per seed", {})
    mdi_per_seed[K_BAD] = {N: dict(existing_k3.get(N, {})) for N in N_values}
    mdi_ok_per_seed  = {N: {} for N in N_values}
    mdi_fibre_per_seed = {N: {} for N in N_values}
    relay_pos_by_seed = dict(A.get("Final relay positions (km, per seed, per K)", {}).get(K_BAD, {}))
    user_pos_by_seed = dict(A.get("Final user positions (N=n_max, km, per seed, K_ref draw)", {}))

    for seed in sim_seeds:
        print(f"\n--- seed {seed}: recomputing MDI K={K_BAD} ---")
        ref_user_pos, _, _ = grow_catchments(n_min, n_max, K_ref, area_km, spread_km, seed)
        user_pos_by_seed[seed] = np.round(ref_user_pos, 3).tolist()

        anchors = catchment_anchors(K_BAD, area_km)
        labels  = assign_nearest_catchment(ref_user_pos, anchors, min_covered=n_min)
        relay_pos = RELAY_STRATEGIES[strategy](ref_user_pos[:n_min], labels[:n_min], K_BAD)
        relay_pos_by_seed[seed] = np.round(np.array(relay_pos), 3).tolist()

        topo_dir = os.path.join(bundle_dir, f"seed{seed}", "topologies", f"K{K_BAD}")
        os.makedirs(topo_dir, exist_ok=True)

        for N in N_values:
            topo = Topology(ref_user_pos[:N], relay_pos, user_relay=labels[:N])

            fig, ax = plt.subplots(figsize=(6, 5))
            draw_mdi(ax, topo, tortuosity_mean=tortuosity, strategy=strategy.capitalize(), seed=seed)
            plt.tight_layout()
            fig.savefig(os.path.join(topo_dir, f"N{N}_mdi.png"), dpi=150, bbox_inches="tight")
            plt.close(fig)

            res = run_mdi_network(
                topo, cfg, runtimes=runtimes, workers=args.workers,
                p2p_db_path=DEFAULT_DB_PATH, net_db_path=DEFAULT_DB_PATH,
                experiment="user_sweep", seed=seed, area_km=area_km, config_preset=None,
            )
            pb = _pair_avgs(res["pair_rates"])
            rate = np.mean(pb) if pb else 0.0
            mdi_per_seed[K_BAD][N][seed] = rate
            mdi_ok_per_seed[N][seed] = res["success_rate"] * 100
            mdi_fibre_per_seed[N][seed] = res["total_fibre_km"]
            print(f"  N={N:2d}  MDI K={K_BAD}  {rate/1000:.2f} kbps")

    # --- rebuild per-seed bundles ---
    for seed in seed_dirs:
        fig_s, ax_s = plt.subplots(figsize=(8, 5))
        seed_assumptions = {
            "Seed": seed,
            "Relay counts (K)": K_list,
            "User count sweep range": A["User count sweep range"],
            "Area": A["Area"],
            "Relay strategy": strategy,
            "Catchment shape": spread_str,
            "Tortuosity mean": tortuosity,
            "Runtimes per pair": runtimes,
            "Repair note": f"K={K_BAD} recomputed on the K={K_ref} user layout "
                            f"(see scripts/network/fix_user_sweep_k3.py); BB84/K={K_ref} unchanged.",
        }
        for variant, _ in DETECTOR_VARIANTS:
            seed_bb84 = [bb84_per_seed[variant][N][seed] for N in N_values]
            ax_s.plot(N_values, np.array(seed_bb84) / 1000, '--', color=BB84_COLORS[variant],
                      lw=1.5, label=f"BB84-{variant}")
            seed_assumptions[f"BB84-{variant} key rate (bps) per N"] = dict(zip(N_values, seed_bb84))
        for ki, K in enumerate(K_list):
            seed_mdi = [mdi_per_seed[K][N][seed] for N in N_values]
            ax_s.plot(N_values, np.array(seed_mdi) / 1000, color=MDI_COLORS[ki % len(MDI_COLORS)],
                      marker=MDI_MARKERS[ki % len(MDI_MARKERS)], lw=1.5, label=f"MDI K={K}")
            seed_assumptions[f"MDI K={K} key rate (bps) per N"] = dict(zip(N_values, seed_mdi))
        ax_s.set_yscale("log")
        ax_s.set_xlabel("User count N")
        ax_s.set_ylabel("Avg key rate (kbps)")
        ax_s.set_xticks(N_values)
        ax_s.legend()
        ax_s.grid(True, alpha=0.3)
        ax_s.set_title(f"Key Rate vs User Count (seed={seed})", fontsize=10)
        plt.tight_layout()
        save_bundle(fig_s, bundle_dir, f"seed{seed}",
                    title=f"Key Rate vs User Count (seed={seed})", assumptions=seed_assumptions)

    # --- rebuild top-level bundle ---
    bb84_stats = {}
    for variant, _ in DETECTOR_VARIANTS:
        vals = {N: list(bb84_per_seed[variant][N].values()) for N in N_values}
        bb84_stats[variant] = {
            "mean": [np.mean(vals[N]) for N in N_values],
            "std":  [np.std(vals[N])  for N in N_values],
        }
    mdi_stats = {}
    for K in K_list:
        vals = {N: list(mdi_per_seed[K][N].values()) for N in N_values}
        mdi_stats[K] = {
            "mean": [np.mean(vals[N]) for N in N_values],
            "std":  [np.std(vals[N])  for N in N_values],
        }

    N_arr = np.array(N_values)
    fig, ax1 = plt.subplots(figsize=(8, 5))

    def plot_series(mean, std, color, marker, linestyle, label):
        mean = np.array(mean) / 1000
        std  = np.array(std) / 1000
        ax1.plot(N_arr, mean, linestyle, color=color, marker=marker, lw=1.5, label=label)
        if error_style == "shade":
            ax1.fill_between(N_arr, mean - std, mean + std, alpha=0.2, color=color)
        elif error_style == "bars":
            ax1.errorbar(N_arr, mean, yerr=std, color=color, marker=marker,
                         linestyle=linestyle, capsize=4, lw=1.5)

    for variant, _ in DETECTOR_VARIANTS:
        st = bb84_stats[variant]
        plot_series(st["mean"], st["std"], BB84_COLORS[variant], None, "--", f"BB84-{variant}")
    for ki, K in enumerate(K_list):
        st = mdi_stats[K]
        plot_series(st["mean"], st["std"], MDI_COLORS[ki % len(MDI_COLORS)],
                    MDI_MARKERS[ki % len(MDI_MARKERS)], "-", f"MDI K={K}")

    ax1.set_yscale("log")
    ax1.set_xlabel("User count N")
    ax1.set_ylabel("Avg key rate (kbps)")
    ax1.set_xticks(N_arr)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    plt.title("Key Rate vs User Count", fontsize=10)
    plt.tight_layout()

    assumptions = dict(A)  # keep all original fields
    assumptions["Growth model"] = ("one user at a time, uniform-random catchment "
                                    "(K_ref draw); other K values relabelled by nearest anchor "
                                    "on the SAME user layout (like-for-like comparison)")
    assumptions["Repair note"] = (f"K={K_BAD} recomputed via scripts/network/fix_user_sweep_k3.py "
                                    f"after discovering per-K draws used mismatched user layouts. "
                                    f"BB84 and MDI K={K_ref} are the original, unaffected data.")
    for K in [K_BAD]:
        assumptions[f"MDI K={K} key rate (bps) per N per seed"] = {
            N: mdi_per_seed[K][N] for N in N_values
        }
    assumptions["Final user positions (N=n_max, km, per seed, K_ref draw)"] = user_pos_by_seed
    assumptions.setdefault("Final relay positions (km, per seed, per K)", {})[K_BAD] = relay_pos_by_seed

    save_bundle(fig, os.path.dirname(bundle_dir), os.path.basename(bundle_dir),
                title="Key Rate vs User Count", assumptions=assumptions)
    print(f"\nRewrote {bundle_dir}/plot.png, assumptions.md, and per-seed bundles.")


if __name__ == "__main__":
    main()
