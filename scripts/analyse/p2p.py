"""
Reconstruct a P2P key-rate sweep figure from results.db.

Figure structure mirrors the compare scripts (scripts/P2P/compare/*.py):
dual y-axis (absolute left / relative right), regime shading bands,
LaTeX parameter subtitle. Identical error-mode logic.

Usage:
    python scripts/analyse/p2p.py                               # distance sweep, all defaults
    python scripts/analyse/p2p.py --sweep len_loss              # fibre loss sweep
    python scripts/analyse/p2p.py --sweep fibre_len --error bars --protocols BB84
    python scripts/analyse/p2p.py --sweep fibre_len --detector-eff-z 0.5
    python scripts/analyse/p2p.py --sweep dark_count --protocols MDI --error iqr

Fixed params default to the same values as lib/functions.py DEFAULTS.
"""
import argparse
import math
import os
import sys
import time

import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, os.path.dirname(__file__))

from db import COL_DEFAULTS, ERROR_MODES, SWEEP_COLS, count_p2p, query_p2p

_MARKERS = {"BB84": "o-", "MDI": "s-"}
_COLOURS = {"BB84": "tab:blue", "MDI": "tab:orange"}

# xlabel per sweep column — matches compare scripts exactly
_XLABEL = {
    "fibre_len":       "Separation between Alice and Bob in km",
    "len_loss":        "Fibre attenuation in dB / km",
    "init_loss":       "Insertion loss (linear fraction)",
    "detector_eff_z":  "Detector efficiency ratio",
    "dark_count":      "Dark count rate (cps)",
    "node_loss_db":    "Node/connector loss (dB)",
    "source_err_rate": r"Source error rate $\varepsilon_s$",
    "detector_eff_x":  r"X-basis detector efficiency $\eta_X$",
    "dephasing_rate":  r"Fibre dephasing rate $\beta$ (per km)",
    "bs_eff":          r"Beam splitter efficiency $\eta_{bs}$",
}

# Per sweep col: which fixed-param cols appear on each title subtitle line
# Matches the exact layout used in the corresponding compare script
_TITLE_META = {
    "fibre_len":       ("Key rate vs distance: BB84 and MDI-QKD",
                        ["len_loss", "detector_eff_z", "dark_count"],
                        ["init_loss", "node_loss_db", "source_err_rate", "dephasing_rate", "bs_eff"]),
    "len_loss":        ("Key rate vs fibre attenuation: BB84 and MDI-QKD",
                        ["fibre_len", "detector_eff_z", "dark_count"],
                        ["init_loss", "node_loss_db", "source_err_rate", "dephasing_rate", "bs_eff"]),
    "init_loss":       ("Key rate vs insertion loss: BB84 and MDI-QKD",
                        ["fibre_len", "len_loss", "detector_eff_z", "dark_count"],
                        ["node_loss_db", "source_err_rate", "dephasing_rate", "bs_eff"]),
    "detector_eff_z":  ("Key rate vs detector efficiency: BB84 and MDI-QKD",
                        ["fibre_len", "len_loss", "dark_count"],
                        ["init_loss", "node_loss_db", "source_err_rate", "dephasing_rate", "bs_eff"]),
    "dark_count":      ("Key rate vs dark count rate: BB84 and MDI-QKD",
                        ["fibre_len", "len_loss", "detector_eff_z"],
                        ["init_loss", "node_loss_db", "source_err_rate", "dephasing_rate", "bs_eff"]),
    "node_loss_db":    ("Key rate vs node/connector loss: BB84 and MDI-QKD",
                        ["fibre_len", "len_loss", "detector_eff_z", "dark_count"],
                        ["init_loss", "source_err_rate", "dephasing_rate", "bs_eff"]),
    "source_err_rate": ("Key rate vs source error rate: BB84 and MDI-QKD",
                        ["fibre_len", "len_loss", "detector_eff_z", "dark_count"],
                        ["init_loss", "node_loss_db", "dephasing_rate", "bs_eff"]),
    "detector_eff_x":  ("Key rate vs detector basis bias: BB84 and MDI-QKD",
                        ["detector_eff_z", "fibre_len", "len_loss", "dark_count"],
                        ["init_loss", "node_loss_db", "source_err_rate", "dephasing_rate", "bs_eff"]),
    "dephasing_rate":  ("Key rate vs fibre dephasing rate: BB84 and MDI-QKD",
                        ["fibre_len", "len_loss", "detector_eff_z", "dark_count"],
                        ["init_loss", "node_loss_db", "source_err_rate", "bs_eff"]),
    "bs_eff":          ("Key rate vs beam splitter efficiency: BB84 and MDI-QKD",
                        ["fibre_len", "len_loss", "detector_eff_z", "dark_count"],
                        ["init_loss", "node_loss_db", "source_err_rate", "dephasing_rate"]),
}

# LaTeX formatter per column
_LATEX = {
    "fibre_len":       lambda v: f"$L$={v} km",
    "len_loss":        lambda v: f"$\\alpha$={v} dB/km",
    "init_loss":       lambda v: f"$L_i$={v}",
    "detector_eff_z":  lambda v: f"$\\eta_d$={v}",
    "dark_count":      lambda v: f"$d_c$={v} cps",
    "node_loss_db":    lambda v: f"$L_n$={v} dB",
    "source_err_rate": lambda v: f"$\\varepsilon_s$={v}",
    "detector_eff_x":  lambda v: f"$\\eta_X$={v}",
    "dephasing_rate":  lambda v: f"$\\beta$={v} /km",
    "bs_eff":          lambda v: f"$\\eta_{{bs}}$={v}",
}


def _build_title(sweep_col: str, fixed: dict) -> str:
    meta = _TITLE_META.get(sweep_col)
    if not meta:
        return f"Key rate vs {sweep_col}: BB84 and MDI-QKD"
    title, cols2, cols3 = meta
    line2 = "  |  ".join(_LATEX[c](fixed[c]) for c in cols2 if c in fixed and c in _LATEX)
    line3 = "  |  ".join(_LATEX[c](fixed[c]) for c in cols3 if c in fixed and c in _LATEX)
    return title + "\n" + line2 + "\n" + line3


def _add_regime_shading(ax1, sweep_col: str, x_data: list) -> None:
    """Add regime/hardware shading bands — mirrors each compare script exactly."""
    _ticks  = ax1.get_xticks()
    _xlim   = ax1.get_xlim()
    _dx     = 0.012 * abs(_xlim[1] - _xlim[0])
    _inv    = _xlim[0] > _xlim[1]
    _ha_l   = 'left'  if _inv else 'right'
    _ha_r   = 'right' if _inv else 'left'

    def _vline(x):
        ax1.axvline(x, color='black', linestyle=':', linewidth=1.2)

    def _vlbl(xv, lbl, ha, mid):
        if not any(abs(xv - t) < max(abs(xv), 1e-9) * 1e-3 + 1e-9 for t in _ticks):
            xp = xv - _dx if xv < mid else xv + _dx
            ax1.text(xp, 0.01, lbl, transform=ax1.get_xaxis_transform(),
                     ha=ha, va='bottom', fontsize=7, color='dimgray')

    def _rlbl(x, lbl, col):
        ax1.text(x, 0.97, lbl, transform=ax1.get_xaxis_transform(),
                 ha='center', va='top', fontsize=7, color=col, alpha=0.7, style='italic')

    if sweep_col == "fibre_len":
        METRO_MIN, METRO_MAX, LONG_MIN = 5, 50, 80
        ax1.axvspan(METRO_MIN, METRO_MAX, alpha=0.08, color='red',   zorder=0)
        ax1.axvspan(LONG_MIN,  _xlim[1],  alpha=0.08, color='green', zorder=0)
        ax1.set_xlim(_xlim)
        for xv in (METRO_MIN, METRO_MAX, LONG_MIN):
            _vline(xv)
        _vlbl(METRO_MIN, "5",  _ha_l, (METRO_MIN + METRO_MAX) / 2)
        _vlbl(METRO_MAX, "50", _ha_r, (METRO_MIN + METRO_MAX) / 2)
        _vlbl(LONG_MIN,  "80", _ha_l, (LONG_MIN + (x_data[-1] if x_data else _xlim[1])) / 2)
        _rlbl((METRO_MIN + METRO_MAX) / 2, "Metropolitan regime", "darkred")
        if x_data and x_data[-1] > LONG_MIN:
            _rlbl(LONG_MIN + 0.6 * (x_data[-1] - LONG_MIN), "Long-range regime", "darkgreen")

    elif sweep_col == "detector_eff_z":
        S1, S2 = 0.80, 0.95
        P1, P2 = 0.15, 0.30
        ax1.axvspan(S1, S2, alpha=0.08, color='green', zorder=0)
        ax1.axvspan(P1, P2, alpha=0.08, color='red',   zorder=0)
        ax1.set_xlim(_xlim)
        for xv in (S1, S2, P1, P2):
            _vline(xv)
        _vlbl(S1, "0.80", _ha_l, (S1 + S2) / 2)
        _vlbl(S2, "0.95", _ha_r, (S1 + S2) / 2)
        _vlbl(P1, "0.15", _ha_l, (P1 + P2) / 2)
        _vlbl(P2, "0.30", _ha_r, (P1 + P2) / 2)
        _rlbl((S1 + S2) / 2, "SNSPD",       "darkgreen")
        _rlbl((P1 + P2) / 2, "InGaAs SPAD", "darkred")

    else:
        _SINGLE = {
            "len_loss":       (0.15,  0.25,  "0.15",  "0.25"),
            "init_loss":      (0.05,  0.15,  "0.05",  "0.15"),
            "dark_count":     (1,     100,   "1",     "100"),
            "node_loss_db":   (0.5,   4.0,   "0.5",   "4.0"),
            "source_err_rate":(0.001, 0.02,  "0.001", "0.02"),
            "detector_eff_x": (0.65,  0.90,  "0.65",  "0.90"),
            "dephasing_rate": (2.6e-7,  3.8e-7,  "2.6e-7",  "3.8e-7"),
            "bs_eff":         (0.90,  0.99,  "0.90",  "0.99"),
        }
        if sweep_col not in _SINGLE:
            return
        r0, r1, l0, l1 = _SINGLE[sweep_col]
        ax1.axvspan(r0, r1, alpha=0.08, color='red', zorder=0)
        ax1.set_xlim(_xlim)
        _vline(r0); _vline(r1)
        mid = (r0 + r1) / 2
        _vlbl(r0, l0, _ha_l, mid)
        _vlbl(r1, l1, _ha_r, mid)
        _rlbl(mid, "Realistic hardware regime", "darkred")


def _parse() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Plot P2P key rate sweep from results.db",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="Sweep column choices: " + ", ".join(c for c, _, _ in SWEEP_COLS),
    )
    p.add_argument("--sweep",          default="fibre_len",
                   choices=[c for c, _, _ in SWEEP_COLS],
                   help="X-axis sweep column")
    p.add_argument("--protocols",      nargs="+", default=["BB84", "MDI"],
                   choices=["BB84", "MDI"], metavar="PROTO",
                   help="Protocols to plot (space-separated)")
    p.add_argument("--error",          default="shade", choices=ERROR_MODES)
    p.add_argument("--fibre-len",      type=float, default=COL_DEFAULTS["fibre_len"],      metavar="km")
    p.add_argument("--len-loss",       type=float, default=COL_DEFAULTS["len_loss"],       metavar="dB/km")
    p.add_argument("--init-loss",      type=float, default=COL_DEFAULTS["init_loss"])
    p.add_argument("--detector-eff-z", type=float, default=COL_DEFAULTS["detector_eff_z"], metavar="η")
    p.add_argument("--dark-count",     type=float, default=COL_DEFAULTS["dark_count"],     metavar="cps")
    p.add_argument("--node-loss",      type=float, default=COL_DEFAULTS["node_loss_db"],   metavar="dB")
    p.add_argument("--source-err",     type=float, default=COL_DEFAULTS["source_err_rate"])
    p.add_argument("--detector-eff-x", type=float, default=COL_DEFAULTS["detector_eff_x"], metavar="η")
    p.add_argument("--dephasing-rate", type=float, default=COL_DEFAULTS["dephasing_rate"])
    p.add_argument("--bs-eff",         type=float, default=COL_DEFAULTS["bs_eff"],         metavar="η")
    p.add_argument("--save",           metavar="FILE",
                   help="Save figure to file instead of displaying (e.g. out.png)")
    return p.parse_args()


def _fixed(args: argparse.Namespace) -> dict:
    return {
        "fibre_len":       args.fibre_len,
        "len_loss":        args.len_loss,
        "init_loss":       args.init_loss,
        "detector_eff_z":  args.detector_eff_z,
        "dark_count":      args.dark_count,
        "node_loss_db":    args.node_loss,
        "source_err_rate": args.source_err,
        "detector_eff_x":  args.detector_eff_x,
        "dephasing_rate":  args.dephasing_rate,
        "bs_eff":          args.bs_eff,
    }


def _plot_series(ax, d: dict, error_mode: str, proto: str):
    """Plot one protocol series; returns the plotted line for colour extraction."""
    x = d["x"]
    y = [v / 1000 for v in d["mean"]]
    s = d["std_log"]
    colour, fmt = _COLOURS[proto], _MARKERS[proto]

    if error_mode == "bars":
        lo = [max(y[i] - d["min"][i] / 1000, 0) for i in range(len(x))]
        hi = [max(d["max"][i] / 1000 - y[i], 0) for i in range(len(x))]
        ax.errorbar(x, y, yerr=[lo, hi], fmt=fmt, color=colour, label=proto, capsize=3)
        return None
    elif error_mode == "sigma":
        lo = [y[i] * (1 - math.exp(-s[i])) for i in range(len(x))]
        hi = [y[i] * (math.exp(s[i]) - 1)  for i in range(len(x))]
        ax.errorbar(x, y, yerr=[lo, hi], fmt=fmt, color=colour, label=proto, capsize=3)
        return None
    elif error_mode == "iqr":
        lo = [max(y[i] - d["q25"][i] / 1000, 0) for i in range(len(x))]
        hi = [max(d["q75"][i] / 1000 - y[i], 0) for i in range(len(x))]
        ax.errorbar(x, y, yerr=[lo, hi], fmt=fmt, color=colour, label=proto, capsize=3)
        return None
    elif error_mode == "sem":
        sem = [v / 1000 for v in d["sem"]]
        ax.errorbar(x, y, yerr=[sem, sem], fmt=fmt, color=colour, label=proto, capsize=3)
        return None
    else:  # shade
        line, = ax.plot(x, y, fmt, color=colour, label=proto)
        lo = [y[i] * math.exp(-s[i]) for i in range(len(x))]
        hi = [y[i] * math.exp(+s[i]) for i in range(len(x))]
        ax.fill_between(x, lo, hi, alpha=0.15, color=line.get_color())
        return line


def main() -> None:
    args   = _parse()
    fixed  = _fixed(args)
    protos = args.protocols

    t0     = time.time()
    n_rows = count_p2p(args.sweep, fixed, protos)
    data   = query_p2p(args.sweep, fixed, protos)
    dt     = time.time() - t0

    print(f"[p2p] {n_rows:,} rows  Q={dt:.2f}s  sweep={args.sweep}  error={args.error}  protocols={protos}")

    if not any(d["x"] for d in data.values()):
        print("[p2p] No data matches filter. Check fixed-param values against what's in the DB.")
        return

    fig, ax1 = plt.subplots()

    all_ns = []
    all_y  = []
    for proto, d in data.items():
        if not d["x"]:
            continue
        _plot_series(ax1, d, args.error, proto)
        all_ns.extend(d["n"])
        all_y.extend(v / 1000 for v in d["mean"])

    ax1.set_xlabel(_XLABEL.get(args.sweep, args.sweep))
    ax1.set_ylabel("Absolute secure key rate (kbps)")
    ax1.set_yscale("log")
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # Relative scale on right axis (invisible ghost lines to sync log scale)
    first_y = all_y[0] if all_y else 1.0
    ax2 = ax1.twinx()
    for proto, d in data.items():
        if d["x"]:
            ax2.plot(d["x"], [v / 1000 / first_y for v in d["mean"]], alpha=0)
    ax2.set_ylabel("Relative secure key rate")
    ax2.set_yscale("log")

    # Regime shading (must happen after plots set xlim, before tight_layout)
    all_x = sorted({xv for d in data.values() for xv in d["x"]})
    _add_regime_shading(ax1, args.sweep, all_x)

    lo_n, hi_n = min(all_ns), max(all_ns)
    count_str = f"n={lo_n}" if lo_n == hi_n else f"n={lo_n}–{hi_n}"
    plt.title(_build_title(args.sweep, fixed) + f"\n{count_str} sims/point", fontsize=9)
    plt.tight_layout()

    if args.save:
        plt.savefig(args.save, dpi=150, bbox_inches="tight")
        print(f"[p2p] saved to {args.save}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
