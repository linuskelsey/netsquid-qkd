"""
SQLite persistence for simulation results.

One row per (protocol, sweep point). Result arrays stored as JSON.

Expected params dict keys:
    fibre_len   — Alice-Bob separation (km)
    fibre_loss  — fibre attenuation (dB/km)
    det_eff     — detector efficiency
    dark_count  — dark count rate (cps)
    init_loss   — TX insertion loss, linear fraction
    node_loss   — RX node loss (dB)
    source_err  — source error rate
    dephasing   — fibre dephasing rate (/km)
    bs_eff      — beam splitter efficiency (MDI only)
"""

import os
import sqlite3
import json
from datetime import datetime

DEFAULT_DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results", "results_P2P.db")

_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS runs (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    protocol    TEXT    NOT NULL,
    script      TEXT,
    fibre_len   REAL,
    fibre_loss  REAL,
    det_eff     REAL,
    dark_count  REAL,
    init_loss   REAL,
    node_loss   REAL,
    source_err  REAL,
    dephasing   REAL,
    bs_eff      REAL,
    key_rates   TEXT,
    qbers       TEXT,
    key_lengths TEXT,
    n_completed INTEGER,
    runtimes    INTEGER,
    photons     INTEGER,
    timestamp   TEXT,
    charlie_pos REAL
)
"""


def init_db(path=DEFAULT_DB_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute(_CREATE_TABLE)
    existing = {row[1] for row in conn.execute("PRAGMA table_info(runs)")}
    if "charlie_pos" not in existing:
        conn.execute("ALTER TABLE runs ADD COLUMN charlie_pos REAL")
    conn.commit()
    return conn


def save_sweep_point(conn, protocol, params, key_rates, qbers, key_lengths,
                     script="", runtimes=None, photons=None):
    conn.execute(
        """INSERT INTO runs
               (protocol, script,
                fibre_len, fibre_loss, det_eff, dark_count,
                init_loss, node_loss, source_err, dephasing, bs_eff,
                key_rates, qbers, key_lengths,
                n_completed, runtimes, photons, timestamp, charlie_pos)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (
            protocol,
            script,
            params.get("fibre_len"),
            params.get("fibre_loss"),
            params.get("det_eff"),
            params.get("dark_count"),
            params.get("init_loss"),
            params.get("node_loss"),
            params.get("source_err"),
            params.get("dephasing"),
            params.get("bs_eff"),
            json.dumps(key_rates),
            json.dumps(qbers),
            json.dumps(key_lengths),
            len(key_rates),
            runtimes,
            photons,
            datetime.utcnow().isoformat(),
            params.get("charlie_pos"),
        ),
    )
    conn.commit()
