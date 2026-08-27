"""
BT real-topology case study — Appendix "Real-World Deployment Considerations"
(sec:appendix_bt). See docs/figures/August/final-figs/bt_case_study/spec.md for
the full figure spec and the modelling decisions this script implements.

One fixed real topology (data/real_topologies/bt.json: Slough, West End, City
of London — K=3), synthetic users anchored on those 3 real relay sites, grown
incrementally (organic growth, relay placement fixed at the real sites, never
re-optimised). Not averaged over drawn seeds — this is one topology, not a
distribution over them.

Two independent user-count sweeps, since cost is cheap (pure geometry) but key
rate needs actual NetSquid trials:
    --rate-n-*  (default 5-15 step 1): key_rate/ and efficiency/ (NetSquid-simulated)
    --cost-n-*  (default 5-40 step 5): cost/ and cost_ratio_rho/ (deterministic,
                no simulation — network/fibre_length.py replicates the exact
                tortuosity-weighted fibre length the NetSquid runners compute
                internally, without paying for their Monte Carlo trials)
Both sweeps take prefixes of the same underlying user draw, so positions are
consistent across every figure regardless of which sweep produced them.

Produces 5 figure bundles under --output-dir, in dependency order so the cheap,
inspectable figures land first and the expensive NetSquid-dependent ones land
last:
    topology_map/    — named real sites + full-N placement, orientation only
    cost/             — deployment cost vs N, illustrative £ prices (deterministic)
    cost_ratio_rho/    — empirical C_relay/C_BB84 vs N swept over rho, vs closed-form N*
    key_rate/         — BB84 vs MDI vs TBB84 key rate vs N (NetSquid-simulated)
    efficiency/       — key rate per unit cost vs N (needs key_rate/, so runs last)

Usage:
    python scripts/network/bt_case_study.py --output-dir docs/figures/August/final-figs/bt_case_study
"""
import argparse
import os
import sqlite3
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

_root    = os.path.join(os.path.dirname(__file__), "../..")
_network = os.path.join(_root, "network")
sys.path.insert(0, _root)
sys.path.insert(0, _network)

from lib.plotting import apply_thesis_style, save_bundle
from lib.functions import load_config
from lib.progress import Progress
from lib.db import DEFAULT_DB_PATH
from topology import grow_catchments, assign_nearest_catchment, Topology
from bb84_network import run_bb84_network
from mdi_network import run_mdi_network
from trusted_bb84_network import run_trusted_bb84_network
from real_topology import load_real_topology, _label_nodes
from visualise_network import draw_mdi
from cost_model import cost_bb84, cost_relay, nstar_closed
from fibre_length import total_fibre_bb84, total_fibre_relay

apply_thesis_style()

PROTO_COLORS     = {"BB84": "#377eb8", "MDI": "#e41a1c", "TBB84": "#4daf4a"}
PROTO_MARKERS    = {"BB84": "o", "MDI": "s", "TBB84": "^"}
PROTO_LINESTYLES = {"BB84": "--", "MDI": "-", "TBB84": ":"}


def build_placement(args, rt_topo, meta):
    """Shift the real relay anchors so the whole placement area has >= args.margin_km
    of clearance on all 4 sides of the relay bounding box, then draw the shared
    user pool (10km catchment discs, nearest-anchor reassignment) once, wide
    enough to cover both the rate and cost N ranges as prefixes of one draw.

    Without this shift, load_real_topology's origin-at-min-lat/lon convention
    puts the relay bbox flush against the placement box's south/west edge, so
    _reflect_into_box folds every "south"/"west" draw back north/east instead
    — the observed north-bunching artefact. Shifting the anchors so the relay
    bbox sits >= margin_km away from every box edge makes the fold a no-op
    (catchment_radius_km < margin_km, so no draw can ever reach an edge).
    """
    w, h = meta["bbox_km"]  # relay bbox: x in [0,w], y in [0,h] (relay-only file)
    area_km  = max(w, h) + 2 * args.margin_km
    x_offset = (area_km - w) / 2
    y_offset = (area_km - h) / 2
    shifted_anchors = rt_topo.relay_pos + np.array([x_offset, y_offset])

    n_min_all = min(args.rate_n_min, args.cost_n_min)
    n_max_all = max(args.rate_n_max, args.cost_n_max)
    user_pos_full, _drawn, anchors = grow_catchments(
        n_min_all, n_max_all, rt_topo.K, area_km, spread_km=15.0, seed=args.seed,
        anchors=shifted_anchors, catchment_radius_km=args.catchment_radius)
    labels_full = assign_nearest_catchment(user_pos_full, anchors, min_covered=n_min_all)

    return anchors, area_km, user_pos_full, labels_full


def fig_topology_map(args, meta, anchors, user_pos_full, labels_full, output_dir):
    N = args.cost_n_max  # largest N across every figure — full real node set
    topo = Topology(user_pos_full[:N], anchors, user_relay=labels_full[:N])

    fig, ax = plt.subplots(figsize=(9, 5))
    draw_mdi(ax, topo, strategy=None, seed=None)  # straight lines in the viz; tortuosity still applies to cost/sim fibre lengths
    _label_nodes(ax, topo, meta)
    ax.set_title(f"BT Real Topology — N={topo.N} users, K={topo.K} relays (full sweep count)")
    plt.tight_layout()
    save_bundle(
        fig, output_dir, "topology_map",
        title="BT Real Topology Map",
        assumptions={
            "Real topology": "data/real_topologies/bt.json (Slough, West End, City of London)",
            "K (relays)": topo.K,
            "N (users, full sweep count)": topo.N,
            "Catchment radius (km)": args.catchment_radius,
            "Placement-area margin (km, all 4 sides of relay bbox)": args.margin_km,
            "Catchment assignment": "nearest-anchor reassignment after 10km-disc draw "
                                     "(assign_nearest_catchment), not fixed-at-draw membership",
            "Seed": args.seed,
        },
        notes=["Orientation figure only — no numerical result attached. Relay positions "
               "are the real BT site coordinates (shifted uniformly so the placement area "
               "has margin_km clearance on every side; relative geometry unchanged), never "
               "re-optimised. User positions are synthetic (no real user-site data exists), "
               "anchored on the 3 real sites."],
    )
    return topo


def compute_cost_fibre(N_values, user_pos_full, labels_full, anchors, K, args):
    """Cheap, no-NetSquid total_fibre_km per N (BB84 mesh + MDI hub/spoke), via
    network/fibre_length.py — bit-identical to what the real NetSquid runners
    compute internally, for whatever N list is asked (rate-N or cost-N)."""
    fibre = {"BB84": {}, "MDI": {}}
    for N in N_values:
        topo_bb84 = Topology(user_pos_full[:N])
        topo_mdi  = Topology(user_pos_full[:N], anchors, user_relay=labels_full[:N])
        fibre["BB84"][N] = total_fibre_bb84(topo_bb84, args.tortuosity, args.seed)
        fibre["MDI"][N]  = total_fibre_relay(topo_mdi, args.tortuosity, args.seed)
    return fibre


def fig_cost(cost_N_values, fibre_cost, prices, K, output_dir, args):
    c_s, c_d, c_f = prices
    cost = {"BB84": {}, "MDI": {}, "TBB84": {}}
    for N in cost_N_values:
        cost["BB84"][N]  = cost_bb84(N, fibre_cost["BB84"][N], c_s, c_d, c_f) / 1e6
        cost["MDI"][N]   = cost_relay(N, K, fibre_cost["MDI"][N], c_s, c_d, c_f) / 1e6
        cost["TBB84"][N] = cost["MDI"][N]  # identical by construction — see cost_model.py docstring

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(cost_N_values, [cost["BB84"][N] for N in cost_N_values], PROTO_LINESTYLES["BB84"],
            color=PROTO_COLORS["BB84"], marker=PROTO_MARKERS["BB84"], markersize=4, lw=1.5, label="BB84")
    ax.plot(cost_N_values, [cost["MDI"][N] for N in cost_N_values], PROTO_LINESTYLES["MDI"],
            color=PROTO_COLORS["MDI"], marker=PROTO_MARKERS["MDI"], markersize=4, lw=2.5, label="MDI")
    ax.plot(cost_N_values, [cost["TBB84"][N] for N in cost_N_values], PROTO_LINESTYLES["TBB84"],
            color=PROTO_COLORS["TBB84"], marker=PROTO_MARKERS["TBB84"], markersize=4, lw=1.5,
            label="TBB84 (coincides with MDI)")
    ax.set_xlabel("User count N")
    ax.set_ylabel("Deployment cost (£M)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_title("BT Real Topology — Deployment Cost vs User Count")
    plt.tight_layout()
    save_bundle(
        fig, output_dir, "cost",
        title="BT Real Topology — Deployment Cost vs User Count",
        assumptions={
            "Illustrative prices": f"c_s=£{c_s:,.0f} (source), c_d=£{c_d:,.0f} (detector module), "
                                    f"c_f=£{c_f:,.0f}/km (new-build dark fibre install)",
            "Cost formula": "N*c_s + {N or K}*c_d + total_fibre_km*c_f, multi-channel-detector-module "
                             "simplification (eq:nstar_closed derivation), real fibre lengths "
                             "(network/fibre_length.py, no NetSquid simulation needed)",
            "K (relays)": K,
            "User count sweep (deterministic, no NetSquid)": f"{cost_N_values[0]}-{cost_N_values[-1]} "
                                                               f"(step {args.cost_n_step})",
            "Cost (£M) per protocol per N": cost,
        },
        notes=["TBB84 cost is defined identically to MDI's (same formula, same component count "
               "under the multi-channel simplification, same real fibre length reused directly) "
               "since the two protocols differ only in trust assumptions, not component count — "
               "the two curves coincide exactly by construction, not by coincidence.",
               "All prices are illustrative, not vendor-quoted, per the existing symbolic-vs-numeric "
               "cost-model hedge in sec:results_cost."],
    )
    return cost


def fig_cost_ratio_rho(cost_N_values, fibre_cost, prices, K, rhos, output_dir, args):
    c_s, _, c_f = prices
    N_max = cost_N_values[-1]
    d_bar_bb84 = fibre_cost["BB84"][N_max] / (N_max * (N_max - 1) / 2)

    fig, ax = plt.subplots(figsize=(9, 6))
    cmap = cm.get_cmap("viridis")
    ratio_data = {}
    nstar_data = {}
    for idx, rho in enumerate(rhos):
        color = cmap(idx / max(len(rhos) - 1, 1))
        c_d_eff = rho * c_f * d_bar_bb84
        ratio = []
        for N in cost_N_values:
            c_bb84  = cost_bb84(N, fibre_cost["BB84"][N], c_s, c_d_eff, c_f)
            c_relay = cost_relay(N, K, fibre_cost["MDI"][N], c_s, c_d_eff, c_f)
            ratio.append(c_relay / c_bb84)
        ratio_data[rho] = dict(zip(cost_N_values, ratio))
        ax.plot(cost_N_values, ratio, color=color, marker="o", markersize=3, lw=1.3, label=fr"$\rho={rho}$")

        n_star = nstar_closed(rho, K)
        nstar_data[rho] = n_star
        ax.scatter([n_star], [1.0], marker="|", s=200, color=color, zorder=5)

    ax.axhline(1.0, color="grey", ls="--", lw=0.8)
    ax.set_xlabel("User count N")
    ax.set_ylabel(r"$C_\mathrm{relay} / C_\mathrm{BB84}$")
    ax.legend(ncol=2, fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_title(r"BT Real Topology — Cost Ratio vs User Count, swept over $\rho$ ($K{=}3$)")
    plt.tight_layout()
    save_bundle(
        fig, output_dir, "cost_ratio_rho",
        title="BT Real Topology — Cost Ratio vs User Count, swept over rho",
        assumptions={
            "rho values": rhos,
            "K (relays)": K,
            "d_bar_BB84 (km, mean real pairwise distance at N_max)": round(d_bar_bb84, 4),
            "User count sweep (deterministic, no NetSquid)": f"{cost_N_values[0]}-{cost_N_values[-1]} "
                                                               f"(step {args.cost_n_step})",
            "Cost ratio per rho per N": ratio_data,
            "Closed-form N*(rho, K=3)": nstar_data,
        },
        notes=["Vertical tick marks on the y=1 line show the closed-form N*(rho,3) "
               "(Equation eq:nstar_closed) for each rho, for direct comparison against "
               "where each empirical (real-distance) curve actually crosses 1.0. Since "
               "N* is provably confined to (K,K+1) regardless of rho, these ticks cluster "
               "tightly just above N=K — expected, not a plotting error.",
               "Deterministic given N, K, rho and the fixed real distances — no NetSquid "
               "simulation, no MC noise."],
    )


_DB_PROTOCOL_NAME = {"BB84": "BB84", "MDI": "MDI", "TBB84": "trusted_BB84"}


def _db_lookup(protocol, N, args):
    """Look for a completed network_results row matching this exact run
    (experiment/protocol/N/seed/runtimes) so a crashed-and-restarted sweep
    can resume without re-simulating N values it already finished. Returns
    (avg_key_rate, success_rate) or None if no match."""
    if args.no_db:
        return None
    try:
        conn = sqlite3.connect(f"file:{DEFAULT_DB_PATH}?mode=ro", uri=True)
        row = conn.execute(
            """SELECT avg_key_rate, success_rate FROM network_results
               WHERE experiment=? AND protocol=? AND n_users=? AND seed=? AND runtimes=?
               ORDER BY run_timestamp DESC LIMIT 1""",
            ("bt_case_study", _DB_PROTOCOL_NAME[protocol], N, args.seed, args.runtimes),
        ).fetchone()
        conn.close()
    except sqlite3.OperationalError:
        return None
    return row  # (avg_key_rate, success_rate) or None


def run_rate_sweep(rate_N_values, user_pos_full, labels_full, anchors, cfg, args):
    results = {"BB84": {}, "MDI": {}, "TBB84": {}}
    ok_rate = {"BB84": {}, "MDI": {}, "TBB84": {}}

    prog = Progress(len(rate_N_values))
    total_start = time.time()
    for step, N in enumerate(rate_N_values):
        user_pos = user_pos_full[:N]
        labels   = labels_full[:N]
        topo_bb84 = Topology(user_pos)
        topo_mdi  = Topology(user_pos, anchors, user_relay=labels)
        p2p_db_path = None if args.no_db else DEFAULT_DB_PATH
        net_db_path = None if args.no_db else DEFAULT_DB_PATH

        for proto, run_fn, topo in (("BB84", run_bb84_network, topo_bb84),
                                     ("MDI", run_mdi_network, topo_mdi),
                                     ("TBB84", run_trusted_bb84_network, topo_mdi)):
            cached = _db_lookup(proto, N, args)
            if cached is not None:
                prog.update(step, f"N={N}/{rate_N_values[-1]}  {proto} resumed from DB...")
                results[proto][N], ok_rate[proto][N] = cached[0], cached[1] * 100
                continue
            prog.update(step, f"N={N}/{rate_N_values[-1]}  {proto} running...")
            res = run_fn(topo, cfg, runtimes=args.runtimes, workers=args.workers,
                         p2p_db_path=p2p_db_path, net_db_path=net_db_path,
                         experiment="bt_case_study", seed=args.seed, area_km=None)
            results[proto][N] = res["avg_key_rate"]
            ok_rate[proto][N] = res["success_rate"] * 100

        prog.update(step + 1,
                    f"N={N}/{rate_N_values[-1]}  BB84={results['BB84'][N]/1000:.2f}  "
                    f"MDI={results['MDI'][N]/1000:.2f}  TBB84={results['TBB84'][N]/1000:.2f} kbps")
    prog.stop()
    m, s = divmod(int(time.time() - total_start), 60)
    print(f"Rate sweep complete: {m}m {s:02d}s")
    return results, ok_rate


def fig_key_rate(rate_N_values, results, ok_rate, args, output_dir):
    fig, ax = plt.subplots(figsize=(8, 5))
    for proto in ("BB84", "MDI", "TBB84"):
        rates = np.array([results[proto][N] for N in rate_N_values]) / 1000
        ax.plot(rate_N_values, rates, PROTO_LINESTYLES[proto], color=PROTO_COLORS[proto],
                marker=PROTO_MARKERS[proto], lw=1.5, label=proto)
    ax.set_yscale("log")
    ax.set_xlabel("User count N")
    ax.set_ylabel("Avg key rate (kbps)")
    ax.set_xticks(rate_N_values)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_title("BT Real Topology — Key Rate vs User Count (single fixed topology)")
    plt.tight_layout()
    save_bundle(
        fig, output_dir, "key_rate",
        title="BT Real Topology — Key Rate vs User Count",
        assumptions={
            "Real topology": "data/real_topologies/bt.json, K=3 (Slough, West End, City of London)",
            "User count sweep (NetSquid-simulated)": f"{rate_N_values[0]}-{rate_N_values[-1]} "
                                                       f"(step {args.rate_n_step})",
            "Catchment radius (km)": args.catchment_radius,
            "Seed": args.seed,
            "Runtimes per pair": args.runtimes,
            "Tortuosity mean": args.tortuosity,
            "Success rate (%) per protocol per N": {p: ok_rate[p] for p in ("BB84", "MDI", "TBB84")},
            "Key rate (bps) per protocol per N": {p: results[p] for p in ("BB84", "MDI", "TBB84")},
        },
        notes=["Single fixed real topology, not averaged over drawn seeds — see the "
               "topology-sensitivity paragraph in sec:simulation_limitations.",
               "N range kept narrow relative to cost/cost_ratio_rho: NetSquid wall-clock "
               "cost grows sharply past N~20 (Appendix sec:appendix_netsquid)."],
    )


def fig_efficiency(rate_N_values, results, user_pos_full, labels_full, anchors, K, prices, output_dir, args):
    fibre_rate = compute_cost_fibre(rate_N_values, user_pos_full, labels_full, anchors, K, args)
    c_s, c_d, c_f = prices
    cost_at_rate_N = {"BB84": {}, "MDI": {}, "TBB84": {}}
    for N in rate_N_values:
        cost_at_rate_N["BB84"][N]  = cost_bb84(N, fibre_rate["BB84"][N], c_s, c_d, c_f) / 1e6
        cost_at_rate_N["MDI"][N]   = cost_relay(N, K, fibre_rate["MDI"][N], c_s, c_d, c_f) / 1e6
        cost_at_rate_N["TBB84"][N] = cost_at_rate_N["MDI"][N]

    fig, ax = plt.subplots(figsize=(8, 5))
    eff = {"BB84": {}, "MDI": {}, "TBB84": {}}
    for proto in ("BB84", "MDI", "TBB84"):
        for N in rate_N_values:
            eff[proto][N] = (results[proto][N] / 1000) / cost_at_rate_N[proto][N]  # kbps / £M
        ax.plot(rate_N_values, [eff[proto][N] for N in rate_N_values], PROTO_LINESTYLES[proto],
                color=PROTO_COLORS[proto], marker=PROTO_MARKERS[proto], lw=1.5, label=proto)
    ax.set_xlabel("User count N")
    ax.set_ylabel("Key rate per unit cost (kbps / £M)")
    ax.set_xticks(rate_N_values)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_title("BT Real Topology — Key Rate per Unit Cost vs User Count")
    plt.tight_layout()
    save_bundle(
        fig, output_dir, "efficiency",
        title="BT Real Topology — Key Rate per Unit Cost vs User Count",
        assumptions={
            "Derived from": "key_rate/ (NetSquid-simulated) and its own cost computation "
                             "at the same (narrower) rate-N values",
            "User count sweep": f"{rate_N_values[0]}-{rate_N_values[-1]} (step {args.rate_n_step})",
            "Efficiency (kbps/£M) per protocol per N": eff,
        },
        notes=["Capped at the rate-sweep's N range (not the wider cost-sweep range): "
               "efficiency needs a simulated key rate at every N, which only exists where "
               "NetSquid was actually run.",
               "Cost-efficiency ranks protocols in the reverse order of their trust guarantees: "
               "TBB84 (least trustless) most cost-efficient, MDI (most trustless) least — ties to "
               "the Level 0-3 trust hierarchy in sec:results_cost / Deployment Recommendations."],
    )


def main():
    parser = argparse.ArgumentParser(description="BT real-topology case study (Appendix sec:appendix_bt)")
    parser.add_argument("--real",       type=str,   default="bt")
    parser.add_argument("--rate-n-min",  type=int, default=5,  help="Key-rate sweep min N (NetSquid-simulated)")
    parser.add_argument("--rate-n-max",  type=int, default=15, help="Key-rate sweep max N")
    parser.add_argument("--rate-n-step", type=int, default=1,  help="Key-rate sweep step")
    parser.add_argument("--cost-n-min",  type=int, default=5,   help="Cost sweep min N (deterministic, no NetSquid)")
    parser.add_argument("--cost-n-max",  type=int, default=40,  help="Cost sweep max N")
    parser.add_argument("--cost-n-step", type=int, default=5,   help="Cost sweep step")
    parser.add_argument("--catchment-radius", type=float, default=10.0,
                        help="Catchment disc radius (km) for the initial draw, before nearest-anchor reassignment")
    parser.add_argument("--margin-km",  type=float, default=15.0,
                        help="Placement-area clearance (km) on all 4 sides of the relay bounding box")
    parser.add_argument("--seed",       type=int,   default=42, help="Single fixed seed (one topology, not averaged)")
    parser.add_argument("--runtimes",   type=int,   default=1000, help="Monte Carlo runs per pair")
    parser.add_argument("--tortuosity", type=float, default=1.2)
    parser.add_argument("--config",     type=str,   default=None)
    parser.add_argument("--workers",    type=int,   default=None)
    parser.add_argument("--no-db",      action="store_true",
                        help="Skip DB logging (p2p_db_path/net_db_path=None); DB logging is on by default")
    parser.add_argument("--c-s",        type=float, default=250_000, help="Photon source module price (£)")
    parser.add_argument("--c-d",        type=float, default=100_000, help="Detector module price (£)")
    parser.add_argument("--c-f",        type=float, default=10_000,  help="New-build dark fibre install price (£/km)")
    parser.add_argument("--rhos",       type=str,   default="0.5,1,2,3,4,6,8,10",
                        help="Comma-separated rho values for the cost-ratio sweep")
    parser.add_argument("--output-dir", type=str,   required=True,
                        help="Directory to save the 5 figure bundles into")
    args = parser.parse_args()

    rhos   = [float(r) for r in args.rhos.split(",")]
    prices = (args.c_s, args.c_d, args.c_f)
    rate_N_values = list(range(args.rate_n_min, args.rate_n_max + 1, args.rate_n_step))
    cost_N_values = list(range(args.cost_n_min, args.cost_n_max + 1, args.cost_n_step))

    cfg = load_config(args.config)
    cfg["tortuosity_mean"] = args.tortuosity

    rt_path = os.path.join(_root, "data", "real_topologies", f"{args.real}.json")
    rt_topo, meta = load_real_topology(rt_path)
    K = rt_topo.K
    print(f"Real topology '{args.real}': K={K}, relays={meta['relay_names']}")

    anchors, area_km, user_pos_full, labels_full = build_placement(args, rt_topo, meta)
    print(f"Placement area: {area_km:.1f}x{area_km:.1f} km "
          f"(>= {args.margin_km} km clearance on every side of the relay bbox)")

    os.makedirs(args.output_dir, exist_ok=True)

    # cheap figures first, so placement/cost can be sanity-checked before the
    # expensive NetSquid-dependent figures (key_rate, efficiency) run
    fig_topology_map(args, meta, anchors, user_pos_full, labels_full, args.output_dir)
    print("Saved topology_map/")

    fibre_cost = compute_cost_fibre(cost_N_values, user_pos_full, labels_full, anchors, K, args)
    cost = fig_cost(cost_N_values, fibre_cost, prices, K, args.output_dir, args)
    print("Saved cost/")

    fig_cost_ratio_rho(cost_N_values, fibre_cost, prices, K, rhos, args.output_dir, args)
    print("Saved cost_ratio_rho/")

    results, ok_rate = run_rate_sweep(rate_N_values, user_pos_full, labels_full, anchors, cfg, args)
    fig_key_rate(rate_N_values, results, ok_rate, args, args.output_dir)
    print("Saved key_rate/")

    fig_efficiency(rate_N_values, results, user_pos_full, labels_full, anchors, K, prices, args.output_dir, args)
    print("Saved efficiency/")

    print(f"All 5 figure bundles saved under {args.output_dir}/")


if __name__ == "__main__":
    main()
