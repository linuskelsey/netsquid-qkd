"""
Reconstruct a network key-rate figure from results.db.

Figure structure mirrors the network sweep scripts (scripts/network/relay_sweep.py,
user_sweep.py): dual y-axis (absolute left / relative right), matching colours
(#377eb8 BB84, #e41a1c MDI), BB84 always dashed+shaded, MDI error controlled
by --error flag with linear std bands.

Usage:
    python scripts/analyse/network.py                            # n_users sweep, avg key rate
    python scripts/analyse/network.py --x k_relays              # relay count sweep
    python scripts/analyse/network.py --y success_rate          # success rate plot
    python scripts/analyse/network.py --n-users 10 --k-relays 1 --area 25
    python scripts/analyse/network.py --seed 1638               # single seed + MDI topology figure
    python scripts/analyse/network.py --x k_relays --n-users 15 --area 50 --error bars

Omit --seed to aggregate across all seeds. Pass --seed to pin a specific
random placement; this also produces a second MDI topology figure.
"""
import argparse
import math
import os
import sys
import time
import traceback

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../network"))
sys.path.insert(0, os.path.dirname(__file__))

from lib.plotting import apply_thesis_style, save_bundle
from db import ERROR_MODES, NET_X_COLS, NET_Y_COLS, NET_Y_LABELS, query_network

apply_thesis_style()

_SHORT_Y = {
    "avg_key_rate": "Avg Key Rate",
    "success_rate": "Success Rate",
    "min_key_rate": "Min Key Rate",
    "max_key_rate": "Max Key Rate",
}

_BB84_COL  = "#377eb8"
_MDI_COL   = "#e41a1c"

_RATE_COLS = {"avg_key_rate", "min_key_rate", "max_key_rate"}

def _y_scale(y_col):
    if y_col in _RATE_COLS: return "rate"      # log scale, bps → kbps (÷1000)
    return "fraction"                           # linear, no conversion
_TOPO_COLOURS = [
    "#e41a1c", "#377eb8", "#4daf4a", "#984ea3",
    "#ff7f00", "#a65628", "#f781bf", "#999999",
]


def _parse() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Plot network key rate sweep from results.db",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--x",         default="n_users",      choices=NET_X_COLS,
                   help="X-axis column")
    p.add_argument("--y",         default="avg_key_rate",  choices=NET_Y_COLS,
                   help="Y-axis column")
    p.add_argument("--protocols", nargs="+", default=["BB84", "MDI"],
                   choices=["BB84", "MDI"], metavar="PROTO")
    p.add_argument("--error",     default="shade",         choices=ERROR_MODES,
                   help="Error mode for MDI series (BB84 always uses shade with linear std)")
    p.add_argument("--n-users",   type=int,   default=None, metavar="N",
                   help="Fix n_users (ignored when --x n_users)")
    p.add_argument("--k-relays",  type=int,   default=None, metavar="K",
                   help="Fix k_relays (ignored when --x k_relays)")
    p.add_argument("--area",      type=float, default=25.0, metavar="km",
                   help="Network area in km")
    p.add_argument("--seed",      type=int,   default=None,
                   help="Pin to a single seed. Omit to aggregate all seeds. "
                        "When set, also produces an MDI topology figure.")
    p.add_argument("--output-dir", metavar="DIR",
                   help="Save key-rate figure bundle to directory instead of displaying")
    return p.parse_args()


def _fixed(args: argparse.Namespace) -> dict:
    return {
        "n_users":  args.n_users,
        "k_relays": args.k_relays,
        "area_km":  args.area,
        "seed":     args.seed,
    }


# ── topology visualisation ────────────────────────────────────────────────────
# Inlined from visualise_network.py — that module has a broken import.

def _draw_mdi_topo(ax, topo) -> None:
    def _col(k): return _TOPO_COLOURS[k % len(_TOPO_COLOURS)]
    for i in range(topo.N):
        r = int(topo.user_relay[i])
        ax.plot([topo.user_pos[i][0], topo.relay_pos[r][0]],
                [topo.user_pos[i][1], topo.relay_pos[r][1]],
                color=_col(r), lw=0.8, alpha=0.6)
    for k1 in range(topo.K):
        for k2 in range(k1 + 1, topo.K):
            ax.plot([topo.relay_pos[k1][0], topo.relay_pos[k2][0]],
                    [topo.relay_pos[k1][1], topo.relay_pos[k2][1]],
                    "k--", lw=0.8, alpha=0.4)
    for i in range(topo.N):
        ax.scatter(*topo.user_pos[i], color=_col(int(topo.user_relay[i])), s=60, zorder=3)
    for k in range(topo.K):
        ax.scatter(*topo.relay_pos[k], marker="s", s=100, color=_col(k), zorder=4)
    ax.scatter([], [], marker="o", color="grey", s=60, label="User")
    ax.scatter([], [], marker="s", color="grey", s=100, label="Relay")
    ax.set_xlabel("x (km)")
    ax.set_ylabel("y (km)")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_aspect("equal")


def _topology_fig(x_col: str, data: dict, fixed_dict: dict, seed: int,
                  output_dir=None) -> None:
    """
    Build an MDI topology figure for the given seed, using the median x-value
    to pick n_users or k_relays when that is the sweep axis.
    """
    try:
        from topology import Topology, optimise_relays, place_users  # type: ignore
        all_x  = sorted({xv for d in data.values() for xv in d["x"]})
        mid_x  = int(all_x[len(all_x) // 2]) if all_x else None
        topo_n = mid_x if x_col == "n_users"  else fixed_dict.get("n_users")
        topo_k = mid_x if x_col == "k_relays" else fixed_dict.get("k_relays")
        if topo_n is None or topo_k is None:
            print("[network] Cannot determine n_users/k_relays for topology — skipping.")
            return
        area      = fixed_dict.get("area_km") or 25.0
        user_pos  = place_users(int(topo_n), area_km=area, seed=seed)
        relay_pos = optimise_relays(user_pos, int(topo_k), seed=seed)
        topo      = Topology(user_pos, relay_pos)
        fig2, ax2 = plt.subplots(figsize=(6, 6))
        _draw_mdi_topo(ax2, topo)
        fig2.suptitle(f"MDI-QKD Topology (N={topo_n}, K={topo_k})")
        fig2.tight_layout()
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            topo_path = os.path.join(output_dir, "network_topology.png")
            fig2.savefig(topo_path, dpi=150)
            print(f"[network] topology saved to {topo_path}")
    except ImportError:
        print("[network] topology.py not importable — skipping topology figure.")
    except Exception:
        traceback.print_exc()


# ── plotting ──────────────────────────────────────────────────────────────────

def _sc(scale: str) -> float:
    return 1000 if scale == "rate" else 1


def _plot_bb84(ax, d: dict, scale: str) -> None:
    if not d["x"]:
        return
    sc  = _sc(scale)
    x   = np.array(d["x"])
    y   = np.array([v / sc for v in d["mean"]])
    std = np.array([v / sc for v in d["std"]])
    ax.plot(x, y, '--', color=_BB84_COL, lw=1.5, label="BB84")
    ax.fill_between(x, y - std, y + std, alpha=0.2, color=_BB84_COL)


def _plot_proto(ax, d: dict, error_mode: str, scale: str,
                label: str, color: str, marker: str) -> None:
    if not d["x"]:
        return
    sc  = _sc(scale)
    x   = np.array(d["x"])
    y   = np.array([v / sc for v in d["mean"]])
    std = np.array([v / sc for v in d["std"]])

    if error_mode == "bars":
        ax.errorbar(x, y, yerr=std, label=label, color=color,
                    marker=marker, capsize=4, lw=1.5)
    elif error_mode == "iqr":
        lo = np.array([max(y[i] - d["q25"][i] / sc, 0) for i in range(len(x))])
        hi = np.array([max(d["q75"][i] / sc - y[i], 0) for i in range(len(x))])
        ax.errorbar(x, y, yerr=[lo, hi], label=label, color=color,
                    marker=marker, capsize=4, lw=1.5)
    elif error_mode == "sem":
        sem = np.array([v / sc for v in d["sem"]])
        ax.errorbar(x, y, yerr=sem, label=label, color=color,
                    marker=marker, capsize=4, lw=1.5)
    else:
        ax.plot(x, y, color=color, marker=marker, lw=1.5, label=label)
        ax.fill_between(x, y - std, y + std, alpha=0.2, color=color)


def main() -> None:
    args    = _parse()
    fixed   = _fixed(args)
    protos  = args.protocols

    t0   = time.time()
    data = query_network(args.x, args.y, fixed, protos)
    dt   = time.time() - t0
    scale = _y_scale(args.y)

    seed_label = f"seed={args.seed}" if args.seed is not None else "all seeds"
    print(
        f"[network] Q={dt:.2f}s  x={args.x}  y={args.y}  "
        f"error={args.error}  {seed_label}  protocols={protos}"
    )

    if not any(d["x"] for d in data.values()):
        print("[network] No data matches filter. Check --n-users / --k-relays / --area / --seed.")
        return

    fig, ax1 = plt.subplots(figsize=(8, 5))

    if "BB84" in protos:
        _plot_bb84(ax1, data.get("BB84", {"x": []}), scale)
    if "MDI" in protos:
        _plot_proto(ax1, data.get("MDI", {"x": []}), args.error, scale,
                    label="MDI", color=_MDI_COL, marker="o")
    # Collect stats for axis decoration
    sc     = _sc(scale)
    all_x  = sorted({xv for d in data.values() for xv in d["x"]})
    all_ns = [n for d in data.values() for n in d["n"]]
    all_y_mean = [v / sc for d in data.values() for v in d["mean"]]
    ref_y = all_y_mean[0] if all_y_mean else 1.0

    if scale == "rate":
        ax1.set_yscale("log")
    ax1.set_xlabel(args.x.replace("_", " ").title())
    ax1.set_ylabel(NET_Y_LABELS[args.y])
    if all_x and isinstance(all_x[0], int):
        ax1.set_xticks(all_x)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Relative scale on right (invisible ghost lines — same pattern as network scripts)
    ax2 = ax1.twinx()
    for proto, d in data.items():
        if d["x"]:
            y_rel = [v / sc / ref_y for v in d["mean"]]
            ax2.plot(d["x"], y_rel, alpha=0)
    ax2.set_ylabel("Relative value")
    if scale == "rate":
        ax2.set_yscale("log")

    # Title
    lo_n, hi_n   = (min(all_ns), max(all_ns)) if all_ns else (0, 0)
    count_str    = f"n={lo_n} MC runs/point" if lo_n == hi_n else f"n={lo_n}–{hi_n} MC runs/point"
    fixed_n      = fixed.get("n_users")  if args.x != "n_users"  else "sweep"
    fixed_k      = fixed.get("k_relays") if args.x != "k_relays" else "sweep"
    area         = fixed.get("area_km") or 25.0
    fixed_label  = (f"N={fixed_n}"  if args.x == "k_relays" else f"K={fixed_k}") \
                   if (fixed_n or fixed_k) else ""
    x_label_long = "User Count" if args.x == "n_users" else "Relay Count"
    short_title  = f"{_SHORT_Y[args.y]} vs {x_label_long}"
    plt.title(short_title, fontsize=10)
    plt.tight_layout()

    if args.seed is not None:
        _topology_fig(args.x, data, fixed, args.seed, output_dir=args.output_dir)

    if args.output_dir:
        save_bundle(
            fig, args.output_dir, f"network_{args.x}_{args.y}",
            title=short_title,
            assumptions={
                "X axis": args.x,
                "Y axis": args.y,
                "Fixed n_users":  fixed_n,
                "Fixed k_relays": fixed_k,
                "Area": f"{area} x {area} km",
                "Seed": seed_label,
                "Protocols": protos,
                "Error display": args.error,
                "MC runs per point": count_str,
            },
            notes=["Reconstructed from results.db (not a fresh simulation run)."],
        )
        print(f"[network] saved to {os.path.join(args.output_dir, f'network_{args.x}_{args.y}')}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
