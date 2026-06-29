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
            net_run_id      TEXT,
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
    conn.execute("""
        CREATE TABLE IF NOT EXISTS network_results (
            row_id               INTEGER PRIMARY KEY AUTOINCREMENT,
            net_run_id           TEXT    NOT NULL,
            run_timestamp        TEXT    NOT NULL,
            experiment           TEXT,
            protocol             TEXT    NOT NULL,
            n_users              INTEGER NOT NULL,
            k_relays             INTEGER,
            area_km              REAL,
            seed                 INTEGER,
            runtimes             INTEGER NOT NULL,
            config_preset        TEXT,
            n_pairs              INTEGER NOT NULL,
            total_fibre_km       REAL,
            avg_pair_distance_km REAL,
            cross_relay_ratio    REAL,
            avg_key_rate         REAL,
            std_key_rate         REAL,
            success_rate         REAL,
            min_key_rate         REAL,
            max_key_rate         REAL
        )
    """)
    conn.commit()
    return conn


def new_run_id():
    return str(uuid.uuid4())


def insert_p2p_rows(conn, run_id, run_timestamp, params, key_lens, key_rate_list, qber_list, net_run_id=None):
    rows = []
    for kl, kr, qb in zip(key_lens, key_rate_list, qber_list):
        if kr != "nan":
            status, key_rate, qber, key_len = "success", kr, qb, kl
        elif qb is not None:
            status, key_rate, qber, key_len = "qber_cutoff", None, qb, None
        else:
            status, key_rate, qber, key_len = "timeout", None, None, None

        rows.append((
            run_id, run_timestamp, net_run_id,
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
            run_id, run_timestamp, net_run_id,
            protocol, fibre_len, photon_count, source_freq, q_speed, q_delay,
            len_loss, init_loss, detector_eff_z, detector_eff_x, dark_count,
            node_loss_db, source_err_rate, dephasing_rate, runtimes, config_preset,
            bs_eff, charlie_pos,
            key_rate, qber, key_len, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, rows)
    conn.commit()


def insert_network_row(conn, net_run_id, run_timestamp, experiment, protocol,
                       n_users, k_relays, area_km, seed, runtimes, config_preset,
                       n_pairs, total_fibre_km, avg_pair_distance_km, cross_relay_ratio,
                       avg_key_rate, std_key_rate, success_rate, min_key_rate, max_key_rate):
    conn.execute("""
        INSERT INTO network_results (
            net_run_id, run_timestamp, experiment, protocol,
            n_users, k_relays, area_km, seed, runtimes, config_preset,
            n_pairs, total_fibre_km, avg_pair_distance_km, cross_relay_ratio,
            avg_key_rate, std_key_rate, success_rate, min_key_rate, max_key_rate
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        net_run_id, run_timestamp, experiment, protocol,
        n_users, k_relays, area_km, seed, runtimes, config_preset,
        n_pairs, total_fibre_km, avg_pair_distance_km, cross_relay_ratio,
        avg_key_rate, std_key_rate, success_rate, min_key_rate, max_key_rate,
    ))
    conn.commit()
