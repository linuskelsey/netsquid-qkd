import os
import sqlite3
import uuid
from datetime import datetime

DEFAULT_DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "results.db")


def init_db(path=DEFAULT_DB_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    conn = sqlite3.connect(path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS p2p_results (
            row_id          INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id          TEXT    NOT NULL,
            run_timestamp   TEXT    NOT NULL,
            protocol        TEXT    NOT NULL,
            fibre_len       REAL    NOT NULL,
            photon_count    INTEGER NOT NULL,
            source_freq     REAL    NOT NULL,
            q_speed         REAL    NOT NULL,
            q_delay         REAL    NOT NULL,
            len_loss        REAL    NOT NULL,
            init_loss       REAL    NOT NULL,
            detector_eff_z  REAL    NOT NULL,
            detector_eff_x  REAL,
            dark_count      REAL    NOT NULL,
            node_loss_db    REAL    NOT NULL,
            source_err_rate REAL    NOT NULL,
            dephasing_rate  REAL    NOT NULL,
            runtimes        INTEGER NOT NULL,
            config_preset   TEXT,
            bs_eff          REAL,
            charlie_pos     REAL,
            key_rate        REAL,
            qber            REAL,
            key_len         INTEGER,
            status          TEXT    NOT NULL
        )
    """)
    conn.commit()
    return conn


def new_run_id():
    return str(uuid.uuid4())


def insert_p2p_rows(conn, run_id, run_timestamp, params, key_lists_a, key_rate_list, qber_list):
    rows = []
    for keyA, kr, qb in zip(key_lists_a, key_rate_list, qber_list):
        if kr != "nan":
            status, key_rate, qber, key_len = "success", kr, qb, len(keyA)
        elif qb is not None:
            status, key_rate, qber, key_len = "qber_cutoff", None, qb, None
        else:
            status, key_rate, qber, key_len = "timeout", None, None, None

        rows.append((
            run_id, run_timestamp,
            params["protocol"],     params["fibre_len"],     params["photon_count"],
            params["source_freq"],  params["q_speed"],       params["q_delay"],
            params["len_loss"],     params["init_loss"],     params["detector_eff_z"],
            params.get("detector_eff_x"),                    params["dark_count"],
            params["node_loss_db"], params["source_err_rate"], params["dephasing_rate"],
            params["runtimes"],     params.get("config_preset"),
            params.get("bs_eff"),   params.get("charlie_pos"),
            key_rate, qber, key_len, status,
        ))

    conn.executemany("""
        INSERT INTO p2p_results (
            run_id, run_timestamp,
            protocol, fibre_len, photon_count, source_freq, q_speed, q_delay,
            len_loss, init_loss, detector_eff_z, detector_eff_x, dark_count,
            node_loss_db, source_err_rate, dephasing_rate, runtimes, config_preset,
            bs_eff, charlie_pos,
            key_rate, qber, key_len, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, rows)
    conn.commit()
