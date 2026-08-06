"""
Query layer for scripts/analyse/tui.py.

Overview
--------
Provides all DB access for reconstructing P2P and network figures from
results.db without re-running simulations.

P2P queries (count_p2p, query_p2p)
    Pull raw key_rate rows from p2p_results filtered by one sweep axis
    and a set of fixed parameter values. All key_rates at the same sweep
    value are pooled together (across multiple run_ids / runtimes) before
    computing statistics — no average-of-averages. Only status='success'
    rows are included; QBER cutoffs and timeouts are excluded.

    bs_eff is silently dropped from the WHERE clause for BB84 queries
    because that column is NULL for all BB84 rows.

Network queries (query_network)
    Pull pre-aggregated rows from network_results (one row per seed ×
    protocol × x_value). Aggregation across seeds is done here in Python
    to produce error bars. The experiment tag (user_sweep / relay_sweep)
    is inferred automatically from x_col.

Statistics returned
    mean     — arithmetic mean of pooled values
    std_log  — (P2P only) std of log(key_rate); used for sigma/shade modes
    std      — (network only) linear std across seeds
    min/max  — sample extremes (used for 'bars' error mode)
    q25/q75  — 25th/75th percentiles (used for 'iqr' error mode)
    sem      — standard error of mean = std / sqrt(n)
    n        — sample count contributing to each point

Units
    key_rate values (P2P mean/min/max/q25/q75/sem) are in bps.
    Callers divide by 1000 for kbps display.
    avg_key_rate / min_key_rate / max_key_rate from network_results
    are also in bps.
    success_rate is a fraction [0, 1].

Constants exported
    SWEEP_COLS   — ordered list of (db_col, label, default) for the P2P tab
    COL_DEFAULTS — {db_col: default_value} mapping
    ERROR_MODES  — ordered list of supported error display modes
    NET_X_COLS   — valid x-axis column names for the Network tab
    NET_Y_COLS   — valid y-axis column names for the Network tab
    NET_Y_LABELS — human-readable axis labels for NET_Y_COLS
    NET_EXPERIMENT — maps x_col → experiment tag stored in network_results

Why _DEFAULTS is inlined
    lib/functions.py imports netsquid at module level. Importing it here
    would require a full netsquid install just to run the TUI. The values
    are duplicated and must stay in sync if lib/functions.py DEFAULTS change.
"""
import math
import os
import sqlite3
import statistics
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from lib.db import DEFAULT_DB_PATH

# Duplicated from lib/functions.py DEFAULTS — keep in sync if those change.
_DEFAULTS = {
    "fibre_loss_db_per_km": 0.2,
    "init_loss":            0.1,
    "detector_efficiency":  0.65,
    "dark_count_rate":      100,
    "node_loss_db":         2.0,
    "source_error_rate":    0.005,
    "det_eff_x":            0.715,
    "dephasing_rate":       3.2e-7,
    "bs_eff":               0.97,
}

# (db_col, display_label, default_value)
# Order matches P2P tab layout. fibre_len default is 25 km (not in _DEFAULTS).
SWEEP_COLS = [
    ("fibre_len",       "Distance (km)",      25.0),
    ("len_loss",        "Fibre loss (dB/km)", _DEFAULTS["fibre_loss_db_per_km"]),
    ("init_loss",       "Insertion loss",     _DEFAULTS["init_loss"]),
    ("detector_eff_z",  "Detector eff η_Z",   _DEFAULTS["detector_efficiency"]),
    ("dark_count",      "Dark count (cps)",   _DEFAULTS["dark_count_rate"]),
    ("node_loss_db",    "Node loss (dB)",     _DEFAULTS["node_loss_db"]),
    ("source_err_rate", "Source error rate",  _DEFAULTS["source_error_rate"]),
    ("detector_eff_x",  "Detector eff η_X",  _DEFAULTS["det_eff_x"]),
    ("dephasing_rate",  "Dephasing rate",     _DEFAULTS["dephasing_rate"]),
    ("bs_eff",          "BS efficiency",      _DEFAULTS["bs_eff"]),
]
COL_DEFAULTS = {col: default for col, _, default in SWEEP_COLS}

# Error display modes — same 5 as the compare scripts.
ERROR_MODES = ["bars", "shade", "sigma", "iqr", "sem"]

NET_X_COLS   = ["n_users", "k_relays"]
NET_Y_COLS   = [
    "avg_key_rate", "success_rate", "min_key_rate", "max_key_rate",
]
NET_Y_LABELS = {
    "avg_key_rate": "Avg key rate (kbps)",
    "success_rate": "Network success rate",
    "min_key_rate": "Min key rate (kbps)",
    "max_key_rate": "Max key rate (kbps)",
}
# Maps the x-axis column to the experiment tag stored in network_results.
NET_EXPERIMENT = {"n_users": "user_sweep", "k_relays": "relay_sweep"}


def _connect():
    return sqlite3.connect(DEFAULT_DB_PATH)


def _p2p_where(sweep_col, fixed_dict, protocol):
    """
    Build a WHERE clause and positional params list for a p2p_results query.

    Rules:
    - Always filters status='success' and the given protocol.
    - Skips the sweep column (it's the x-axis, not a filter).
    - Skips bs_eff for BB84 (NULL in all BB84 rows; including it would
      return zero rows).
    """
    clauses = ["status = 'success'", "protocol = ?"]
    params  = [protocol]
    # Sparse columns: only populated when they ARE the sweep axis; NULL in all
    # other rows. Including them as fixed filters returns zero rows.
    # detector_eff_x — NULL for both protocols unless basis_bias sweep.
    # charlie_pos    — NULL unless charlie_pos sweep.
    # bs_eff         — NULL for BB84 (but always set for MDI, so only skip BB84).
    _always_skip = {"detector_eff_x", "charlie_pos"}
    _bb84_skip   = {"bs_eff"}
    for col, val in fixed_dict.items():
        if col == sweep_col:
            continue
        if col in _always_skip:
            continue
        if col in _bb84_skip and protocol == "BB84":
            continue
        clauses.append(f"{col} = ?")
        params.append(val)
    return " AND ".join(clauses), params


def count_p2p(sweep_col, fixed_dict, protocols):
    """
    Return the total number of p2p_results rows matching the current filter.

    Used by the TUI status bar. Runs a fast COUNT(*) rather than fetching
    rows, so it stays responsive even against the full 2M+ row table.

    Args:
        sweep_col:  DB column name being swept (excluded from WHERE).
        fixed_dict: {col: value} for all non-swept parameters.
        protocols:  list of protocol strings, e.g. ["BB84", "MDI"].

    Returns:
        int — total matching rows across all requested protocols.
    """
    conn  = _connect()
    total = 0
    for proto in protocols:
        where, params = _p2p_where(sweep_col, fixed_dict, proto)
        total += conn.execute(
            f"SELECT COUNT(*) FROM p2p_results WHERE {where}", params
        ).fetchone()[0]
    conn.close()
    return total


def query_p2p(sweep_col, fixed_dict, protocols):
    """
    Query p2p_results and return per-protocol aggregated series.

    Pools all key_rate rows at the same sweep value before computing
    statistics (no average-of-averages). Zero and null key_rates are
    excluded (they represent failed runs already filtered by status='success'
    but occasionally stored as 0.0).

    Args:
        sweep_col:  DB column to use as x-axis.
        fixed_dict: {col: value} for all fixed parameters.
        protocols:  list of protocols to query.

    Returns:
        dict keyed by protocol string, each value a dict with keys:
            x        — sorted list of sweep values
            mean     — arithmetic mean of key_rate (bps)
            std_log  — std of log(key_rate); used by sigma/shade error modes
            min      — sample minimum (bps)
            max      — sample maximum (bps)
            q25      — 25th percentile (bps)
            q75      — 75th percentile (bps)
            sem      — standard error of mean (bps)
            n        — number of pooled samples per point
    """
    conn   = _connect()
    result = {}
    for proto in protocols:
        where, params = _p2p_where(sweep_col, fixed_dict, proto)
        rows = conn.execute(
            f"SELECT {sweep_col}, key_rate FROM p2p_results "
            f"WHERE {where} ORDER BY {sweep_col}", params
        ).fetchall()

        groups = {}
        for x_val, kr in rows:
            if kr is not None and kr > 0:
                groups.setdefault(x_val, []).append(kr)

        xs, means, stds, mins, maxs, q25s, q75s, sems, ns = [], [], [], [], [], [], [], [], []
        for x_val in sorted(groups):
            krs     = groups[x_val]
            n       = len(krs)
            mean    = sum(krs) / n
            log_krs = [math.log(r) for r in krs]
            xs.append(x_val)
            means.append(mean)
            stds.append(statistics.stdev(log_krs) if n > 1 else 0.0)
            mins.append(min(krs))
            maxs.append(max(krs))
            q25s.append(float(np.percentile(krs, 25)))
            q75s.append(float(np.percentile(krs, 75)))
            sems.append(statistics.stdev(krs) / math.sqrt(n) if n > 1 else 0.0)
            ns.append(n)

        result[proto] = dict(x=xs, mean=means, std_log=stds, min=mins,
                             max=maxs, q25=q25s, q75=q75s, sem=sems, n=ns)
    conn.close()
    return result


def query_network(x_col, y_col, fixed_dict, protocols):
    """
    Query network_results and return per-protocol series aggregated across seeds.

    Each row in network_results is already aggregated over pairs within one
    simulation run (one seed). This function aggregates those per-seed values
    across seeds to produce error bars.

    The experiment tag (user_sweep / relay_sweep) is inferred from x_col
    via NET_EXPERIMENT. A blank or None value in fixed_dict for any column
    means "aggregate over all values of that column" (used for seed: blank
    = pool all seeds).

    Args:
        x_col:      "n_users" or "k_relays".
        y_col:      one of NET_Y_COLS.
        fixed_dict: {col: value} for fixed params; blank string = ignore.
        protocols:  list of protocols to query.

    Returns:
        dict keyed by protocol string, each value a dict with keys:
            x     — sorted list of x-axis values
            mean  — mean of y_col across seeds
            std   — linear std across seeds (unlike P2P, not log-space)
            min, max, q25, q75, sem, n — as per query_p2p
    """
    # Columns that are always NULL for specific protocols in network_results.
    # When such a column is the x-axis, those protocols cannot produce a grouped
    # series. Instead we draw a flat horizontal line: aggregate all their matching
    # rows (ignoring the NULL x-axis column) and replicate across the x range.
    _proto_null_x = {"BB84": {"k_relays"}}

    experiment = NET_EXPERIMENT[x_col]
    conn       = _connect()
    result     = {}

    for proto in protocols:
        clauses = ["experiment = ?", "protocol = ?"]
        params  = [experiment, proto]
        # Columns that are NULL for this protocol — exclude from WHERE to avoid zero results.
        _null_cols = _proto_null_x.get(proto, set())
        for col, val in fixed_dict.items():
            if col == x_col or val is None or str(val).strip() == "":
                continue
            if col in _null_cols:
                continue
            clauses.append(f"{col} = ?")
            params.append(val)
        where = " AND ".join(clauses)

        # ── flat-line path ─────────────────────────────────────────────────
        # x_col is NULL for this protocol; aggregate all matching rows and
        # replicate the global aggregate as a flat line across the x range.
        if x_col in _null_cols:
            x_vals = [r[0] for r in conn.execute(
                f"SELECT DISTINCT {x_col} FROM network_results "
                f"WHERE experiment = ? AND {x_col} IS NOT NULL ORDER BY {x_col}",
                [experiment],
            ).fetchall()]
            flat_rows = conn.execute(
                f"SELECT {y_col}, runtimes, n_pairs FROM network_results WHERE {where}", params
            ).fetchall()
            ys  = [r[0] for r in flat_rows if r[0] is not None]
            n_mc = sum(r[1] * r[2] for r in flat_rows if r[0] is not None)

            _empty = dict(x=[], mean=[], std=[], std_log=[], min=[], max=[],
                          q25=[], q75=[], sem=[], n=[])
            if not x_vals or not ys:
                result[proto] = _empty
                continue

            n       = len(ys)
            mean    = sum(ys) / n
            std     = statistics.stdev(ys) if n > 1 else 0.0
            log_ys  = [math.log(y) for y in ys if y > 0]
            std_log = statistics.stdev(log_ys) if len(log_ys) > 1 else 0.0
            q25     = float(np.percentile(ys, 25))
            q75     = float(np.percentile(ys, 75))
            sem     = std / math.sqrt(n) if n > 1 else 0.0
            k       = len(x_vals)
            result[proto] = dict(
                x=x_vals,
                mean=[mean] * k, std=[std] * k, std_log=[std_log] * k,
                min=[min(ys)] * k, max=[max(ys)] * k,
                q25=[q25] * k, q75=[q75] * k, sem=[sem] * k, n=[n_mc] * k,
            )
            continue

        # ── normal grouped path ────────────────────────────────────────────
        rows = conn.execute(
            f"SELECT {x_col}, {y_col}, runtimes, n_pairs FROM network_results "
            f"WHERE {where} ORDER BY {x_col}", params
        ).fetchall()

        groups = {}
        mc_totals = {}
        for x_val, y_val, runtimes, n_pairs in rows:
            if x_val is not None and y_val is not None:
                groups.setdefault(x_val, []).append(y_val)
                mc_totals[x_val] = mc_totals.get(x_val, 0) + runtimes * n_pairs

        xs, means, stds, mins, maxs, q25s, q75s, sems, ns = [], [], [], [], [], [], [], [], []
        for x_val in sorted(groups):
            ys  = groups[x_val]
            n   = len(ys)
            xs.append(x_val)
            means.append(sum(ys) / n)
            stds.append(statistics.stdev(ys) if n > 1 else 0.0)
            mins.append(min(ys))
            maxs.append(max(ys))
            q25s.append(float(np.percentile(ys, 25)))
            q75s.append(float(np.percentile(ys, 75)))
            sems.append(statistics.stdev(ys) / math.sqrt(n) if n > 1 else 0.0)
            ns.append(mc_totals[x_val])

        std_logs = [
            statistics.stdev([math.log(y) for y in groups[xv] if y > 0])
            if len([y for y in groups[xv] if y > 0]) > 1 else 0.0
            for xv in xs
        ]
        result[proto] = dict(x=xs, mean=means, std=stds, std_log=std_logs, min=mins,
                             max=maxs, q25=q25s, q75=q75s, sem=sems, n=ns)

    conn.close()
    return result


def list_distinct(col, table="p2p_results"):
    """
    Return sorted unique non-null values for a column.

    Useful for populating dropdowns or validating user input.
    """
    conn = _connect()
    rows = conn.execute(
        f"SELECT DISTINCT {col} FROM {table} "
        f"WHERE {col} IS NOT NULL ORDER BY {col}"
    ).fetchall()
    conn.close()
    return [r[0] for r in rows]
