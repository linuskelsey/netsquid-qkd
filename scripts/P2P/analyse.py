"""
DB Query / Replot
=================
Regenerate plots from results.db without re-running simulations.

Usage:
    python scripts/P2P/analyse.py --script {length,loss,efficiency,dark_count,
                                            node_loss,source_err,dephasing,
                                            basis_bias,bs_eff,charlie_pos}
                                  [--db PATH]
                                  [--mode {key_rate,qber}]
                                  [--error {bars,shade,sigma,iqr,sem}]
                                  [--list]

Note: charlie_pos stores no QBER data — --mode qber will exit with a warning for that script.
"""

import argparse
import json
import math
import os
import sqlite3
import statistics
import sys
from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from lib.db import DEFAULT_DB_PATH
from lib.functions import DEFAULTS

# Maps DB column → DEFAULTS key for filtering non-sweep params
_COL_DEFAULT = {
    "fibre_loss": DEFAULTS["fibre_loss_db_per_km"],
    "det_eff":    DEFAULTS["detector_efficiency"],
    "dark_count": DEFAULTS["dark_count_rate"],
    "init_loss":  DEFAULTS["init_loss"],
    "node_loss":  DEFAULTS["node_loss_db"],
    "source_err": DEFAULTS["source_error_rate"],
    "dephasing":  DEFAULTS["dephasing_rate"],
    "bs_eff":     DEFAULTS["bs_eff"],
}

# (sweep_col, x_label, realistic_min, realistic_max, invert_x, region_label)
SWEEP_MAP = {
    "length":     ("fibre_len",  "Distance (km)",                           5,     50,    False, "Metropolitan regime"),
    "loss":       ("fibre_loss", "Fibre attenuation (dB/km)",               0.15,  0.25,  False, "Realistic hardware regime"),
    "efficiency": ("det_eff",    "Detector efficiency",                      0.65,  0.90,  True,  "Realistic hardware regime"),
    "dark_count": ("dark_count", "Dark count rate (cps)",                    1,     100,   False, "Realistic hardware regime"),
    "node_loss":  ("node_loss",  "Node loss (dB)",                           0.5,   4.0,   False, "Realistic hardware regime"),
    "source_err": ("source_err", "Source error rate",                        0.001, 0.02,  False, "Realistic hardware regime"),
    "dephasing":  ("dephasing",  r"Dephasing rate $\beta$ (per km)",         1e-4,  1e-3,  False, "Realistic hardware regime"),
    "basis_bias": ("det_eff",    r"X-basis detector efficiency $\eta_X$",    0.65,  0.90,  True,  "Realistic hardware regime"),
    "bs_eff":     ("bs_eff",     r"Beam splitter efficiency $\eta_{bs}$",    0.90,  0.99,  True,  "Realistic hardware regime"),
    "charlie_pos":("charlie_pos","Charlie position (fraction from Alice)",   0.4,   0.6,   False, "Near-symmetric regime"),
}

TITLE_MAP = {
    "length":     "Key rate vs distance",
    "loss":       "Key rate vs fibre attenuation",
    "efficiency": "Key rate vs detector efficiency",
    "dark_count": "Key rate vs dark count rate",
    "node_loss":  "Key rate vs node loss",
    "source_err": "Key rate vs source error rate",
    "dephasing":  "Key rate vs dephasing rate",
    "basis_bias": "Key rate vs detector basis bias",
    "bs_eff":     "Key rate vs beam splitter efficiency",
    "charlie_pos":"Key rate vs Charlie position",
}

QBER_TITLE_MAP = {k: v.replace("Key rate", "QBER") for k, v in TITLE_MAP.items()}

# (db_col, latex_label, unit_suffix)
_PARAM_DEFS = [
    ("fibre_len",  "$L$",               " km"),
    ("fibre_loss", r"$\alpha$",          " dB/km"),
    ("det_eff",    r"$\eta_d$",          ""),
    ("dark_count", "$d_c$",              " cps"),
    ("init_loss",  "$L_i$",             ""),
    ("node_loss",  "$L_n$",             " dB"),
    ("source_err", r"$\varepsilon_s$",  ""),
    ("dephasing",  r"$\beta$",           " /km"),
    ("bs_eff",     r"$\eta_{bs}$",       ""),
]

QBER_CUTOFF = 0.11


def _fixed_str(row_meta, sweep_col):
    cols   = [c for c, _, _ in _PARAM_DEFS]
    vals   = dict(zip(cols, row_meta))
    parts  = [(lbl, vals[c], u) for c, lbl, u in _PARAM_DEFS if c != sweep_col]
    line1  = "  |  ".join(f"{lbl}={v}{u}" for lbl, v, u in parts[:4])
    line2  = "  |  ".join(f"{lbl}={v}{u}" for lbl, v, u in parts[4:])
    return line1 + ("\n" + line2 if line2 else "")


def list_db(conn):
    rows = conn.execute(
        "SELECT script, COUNT(*) as n, MIN(timestamp), MAX(timestamp) "
        "FROM runs GROUP BY script ORDER BY MAX(timestamp) DESC"
    ).fetchall()
    if not rows:
        print("DB is empty.")
        return
    print(f"{'Script':<14}  {'Rows':>5}  {'First':<25}  {'Last'}")
    print("-" * 78)
    for script, n, first, last in rows:
        print(f"{script:<14}  {n:>5}  {first:<25}  {last}")


def _build_query(conn, script, sweep_col, value_col):
    filter_cols = {col: val for col, val in _COL_DEFAULT.items() if col != sweep_col}
    where       = "script=? AND " + " AND ".join(f"{c}=?" for c in filter_cols)
    where_vals  = [script] + list(filter_cols.values())
    meta_cols   = ("fibre_len", "fibre_loss", "det_eff", "dark_count",
                   "init_loss", "node_loss", "source_err", "dephasing", "bs_eff")
    rows = conn.execute(
        f"SELECT protocol, {sweep_col}, {value_col}, {', '.join(meta_cols)} "
        f"FROM runs WHERE {where} ORDER BY {sweep_col}",
        where_vals
    ).fetchall()
    return rows, meta_cols


def query_and_aggregate(conn, script, sweep_col):
    rows, meta_cols = _build_query(conn, script, sweep_col, "key_rates")
    if not rows:
        return None, None, None, None

    buckets  = defaultdict(list)
    meta_row = {}
    for row in rows:
        protocol, sweep_val, key_rates_json = row[0], row[1], row[2]
        key = (protocol, sweep_val)
        buckets[key].extend(json.loads(key_rates_json))
        meta_row[key] = row[3:]

    sweep_vals = sorted(set(v for _, v in buckets))
    protocols  = sorted(set(p for p, _ in buckets))

    results = {}
    for protocol in protocols:
        xs, avgs, mins, maxs, stds, q25s, q75s, sems = [], [], [], [], [], [], [], []
        for sv in sweep_vals:
            key = (protocol, sv)
            if key not in buckets:
                continue
            rates = buckets[key]
            nz    = [r for r in rates if r > 0]
            xs.append(sv)
            avgs.append((sum(rates) / len(rates)) / 1000)
            mins.append((min(nz) if nz else float('nan')) / 1000)
            maxs.append((max(rates) if rates else float('nan')) / 1000)
            stds.append(statistics.stdev([math.log(r) for r in nz]) if len(nz) > 1 else 0.0)
            q25s.append((float(np.percentile(nz, 25)) if nz else float('nan')) / 1000)
            q75s.append((float(np.percentile(nz, 75)) if nz else float('nan')) / 1000)
            sems.append((statistics.stdev(nz) / math.sqrt(len(nz)) if len(nz) > 1 else 0.0) / 1000)
        results[protocol] = (xs, avgs, mins, maxs, stds, q25s, q75s, sems)

    first_meta = meta_row[next(iter(meta_row))]
    fixed = _fixed_str(first_meta, sweep_col)
    return results, sweep_vals, protocols, fixed


def query_and_aggregate_qber(conn, script, sweep_col):
    rows, meta_cols = _build_query(conn, script, sweep_col, "qbers")
    if not rows:
        return None, None, None, None

    buckets  = defaultdict(list)
    meta_row = {}
    for row in rows:
        protocol, sweep_val, qbers_json = row[0], row[1], row[2]
        key = (protocol, sweep_val)
        loaded = json.loads(qbers_json)
        buckets[key].extend(loaded)
        meta_row[key] = row[3:]

    if sum(len(v) for v in buckets.values()) == 0:
        return None, None, None, None

    sweep_vals = sorted(set(v for _, v in buckets))
    protocols  = sorted(set(p for p, _ in buckets))

    results = {}
    for protocol in protocols:
        xs, avgs, stds, success_rates = [], [], [], []
        for sv in sweep_vals:
            key = (protocol, sv)
            if key not in buckets or not buckets[key]:
                continue
            qbers = buckets[key]
            xs.append(sv)
            avgs.append(sum(qbers) / len(qbers))
            stds.append(statistics.stdev(qbers) if len(qbers) > 1 else 0.0)
            success_rates.append(sum(1 for q in qbers if q < QBER_CUTOFF) / len(qbers))
        results[protocol] = (xs, avgs, stds, success_rates)

    first_meta = meta_row[next(iter(meta_row))]
    fixed = _fixed_str(first_meta, sweep_col)
    return results, sweep_vals, protocols, fixed


def _draw_region(ax1, rmin, rmax, label):
    ax1.axvspan(rmin, rmax, alpha=0.08, color='red', zorder=0)
    ax1.axvline(rmin, color='black', linestyle=':', linewidth=1.2)
    ax1.axvline(rmax, color='black', linestyle=':', linewidth=1.2)
    _ticks = ax1.get_xticks()
    _xlim  = ax1.get_xlim()
    _dx    = 0.012 * abs(_xlim[1] - _xlim[0])
    _inv   = _xlim[0] > _xlim[1]
    _ha_l  = 'left'  if _inv else 'right'
    _ha_r  = 'right' if _inv else 'left'
    for _xv, _lbl, _ha in [(rmin, str(rmin), _ha_l), (rmax, str(rmax), _ha_r)]:
        if not any(abs(_xv - _t) < max(abs(_xv), 1e-9) * 1e-3 + 1e-9 for _t in _ticks):
            _xp = _xv - _dx if _xv < (rmin + rmax) / 2 else _xv + _dx
            ax1.text(_xp, 0.01, _lbl, transform=ax1.get_xaxis_transform(),
                     ha=_ha, va='bottom', fontsize=7, color='dimgray')
    ax1.text((rmin + rmax) / 2, 0.97, label,
             transform=ax1.get_xaxis_transform(),
             ha='center', va='top', fontsize=7, color='darkred', alpha=0.7, style='italic')


def plot_results(results, x_label, title, fixed, error_style, invert_x, rmin, rmax, region_label):
    fmt = {'BB84': 'o-', 'MDI': 's-'}

    base = None
    for proto in ('BB84', 'MDI'):
        if proto in results and results[proto][1]:
            base = results[proto][1][0] * 1000
            break

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    for protocol, (xs, avgs, mins, maxs, stds, q25s, q75s, sems) in results.items():
        mk  = fmt.get(protocol, 'o-')
        rel = [r * 1000 / base for r in avgs] if base else [1.0] * len(avgs)

        if error_style == 'bars':
            yerr = [
                [max(r - m, 0) for r, m in zip(avgs, mins)],
                [max(m - r, 0) for r, m in zip(avgs, maxs)],
            ]
            ax1.errorbar(xs, avgs, yerr=yerr, fmt=mk, label=protocol, capsize=3)
        elif error_style == 'shade':
            lo = [r * math.exp(-s) for r, s in zip(avgs, stds)]
            hi = [r * math.exp(+s) for r, s in zip(avgs, stds)]
            line, = ax1.plot(xs, avgs, mk, label=protocol)
            ax1.fill_between(xs, lo, hi, alpha=0.15, color=line.get_color())
        elif error_style == 'sigma':
            lo = [r * (1 - math.exp(-s)) for r, s in zip(avgs, stds)]
            hi = [r * (math.exp(s) - 1)  for r, s in zip(avgs, stds)]
            ax1.errorbar(xs, avgs, yerr=[lo, hi], fmt=mk, label=protocol, capsize=3)
        elif error_style == 'iqr':
            yerr = [
                [max(r - q, 0) for r, q in zip(avgs, q25s)],
                [max(q - r, 0) for r, q in zip(avgs, q75s)],
            ]
            ax1.errorbar(xs, avgs, yerr=yerr, fmt=mk, label=protocol, capsize=3)
        else:  # sem
            ax1.errorbar(xs, avgs, yerr=[sems, sems], fmt=mk, label=protocol, capsize=3)

        ax2.plot(xs, rel, mk, alpha=0)

    ax1.set_xlabel(x_label)
    ax1.set_ylabel("Absolute secure key rate (kbps)")
    ax1.set_yscale("log")
    ax1.grid(True, alpha=0.3)
    ax2.set_ylabel("Relative secure key rate")
    ax2.set_yscale("log")

    if invert_x:
        ax1.invert_xaxis()

    ax1.legend()
    _draw_region(ax1, rmin, rmax, region_label)
    plt.title(f"{title}: BB84 and MDI-QKD\n{fixed}")
    plt.tight_layout()
    plt.show()


def plot_qber(results, x_label, title, fixed, invert_x, rmin, rmax, region_label):
    fmt = {'BB84': 'o-', 'MDI': 's-'}

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    for protocol, (xs, avgs, stds, success_rates) in results.items():
        mk = fmt.get(protocol, 'o-')
        line, = ax1.plot(xs, avgs, mk, label=protocol)
        ax1.fill_between(xs,
                         [max(a - s, 0) for a, s in zip(avgs, stds)],
                         [a + s for a, s in zip(avgs, stds)],
                         alpha=0.15, color=line.get_color())
        ax2.plot(xs, success_rates, mk, alpha=0.4, linestyle='--',
                 color=line.get_color(), label=f"{protocol} success rate")

    ax1.axhline(QBER_CUTOFF, color='red', linestyle='--', linewidth=1.2,
                label=f"QBER cutoff ({QBER_CUTOFF*100:.0f}%)")

    ax1.set_xlabel(x_label)
    ax1.set_ylabel("Mean QBER  (±1σ shaded)")
    ax1.set_ylim(bottom=0)
    ax1.grid(True, alpha=0.3)
    ax2.set_ylabel("Success rate (QBER < 11%)")
    ax2.set_ylim(0, 1.05)

    if invert_x:
        ax1.invert_xaxis()

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    _draw_region(ax1, rmin, rmax, region_label)
    plt.title(f"{title}: BB84 and MDI-QKD\n{fixed}")
    plt.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(
        description="Replot compare-script sweeps from results.db without re-running simulations."
    )
    parser.add_argument("--script", choices=list(SWEEP_MAP.keys()),
                        help="Sweep to load and plot")
    parser.add_argument("--db",    type=str, default=DEFAULT_DB_PATH,
                        help="Path to results SQLite DB")
    parser.add_argument("--mode",  choices=["key_rate", "qber"], default="key_rate",
                        help="Plot mode: key_rate (default) or qber")
    parser.add_argument("--error", choices=["bars", "shade", "sigma", "iqr", "sem"], default="bars",
                        help="Error display (key_rate mode only): bars=min/max, shade/sigma=±1σ, iqr=IQR, sem=±SEM")
    parser.add_argument("--list",  action="store_true",
                        help="Show available data in DB and exit")
    args = parser.parse_args()

    conn = sqlite3.connect(args.db)

    if args.list:
        list_db(conn)
        conn.close()
        return

    if args.script is None:
        parser.error("--script is required unless --list is used")

    sweep_col, x_label, rmin, rmax, invert_x, region_label = SWEEP_MAP[args.script]

    if args.mode == "qber":
        results, sweep_vals, protocols, fixed = query_and_aggregate_qber(conn, args.script, sweep_col)
        conn.close()
        if results is None:
            print(f"No QBER data for script='{args.script}' "
                  f"(charlie_pos stores no QBER; re-run other scripts to populate).")
            sys.exit(1)
        print(f"Loaded '{args.script}' QBER: {len(sweep_vals)} sweep points, protocols: {protocols}")
        plot_qber(results, x_label, QBER_TITLE_MAP[args.script], fixed,
                  invert_x, rmin, rmax, region_label)
    else:
        results, sweep_vals, protocols, fixed = query_and_aggregate(conn, args.script, sweep_col)
        conn.close()
        if results is None:
            print(f"No data for script='{args.script}' in {args.db}")
            sys.exit(1)
        print(f"Loaded '{args.script}': {len(sweep_vals)} sweep points, protocols: {protocols}")
        plot_results(results, x_label, TITLE_MAP[args.script], fixed,
                     args.error, invert_x, rmin, rmax, region_label)


if __name__ == "__main__":
    main()
