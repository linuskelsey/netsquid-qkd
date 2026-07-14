# Data

Simulation results are stored in a SQLite database (`data/results.db`, not tracked by git).
Raw simulation data is available upon request.

---

## Tables

### `p2p_results`

One row per Monte Carlo simulation run (single protocol exchange between one Alice–Bob pair).
Populated by all P2P compare scripts, raw scripts, layers script, and network simulations.
For trusted-node BB84 network runs, rows represent individual user-relay links (not end-to-end pairs); `net_run_id` links them to the corresponding `network_results` row.

| Column | Type | Description |
|---|---|---|
| `row_id` | INTEGER PK | Auto-increment row identifier |
| `run_id` | TEXT | UUID grouping all rows from one `run_BB84_sims`/`run_mdi_sims` call |
| `run_timestamp` | TEXT | ISO8601 timestamp of run start |
| `net_run_id` | TEXT | UUID linking to `network_results`; NULL for standalone P2P runs |
| `protocol` | TEXT | `BB84` or `MDI` |
| `fibre_len` | REAL | Alice–Bob fibre length (km) |
| `photon_count` | INTEGER | Photons sent per run |
| `source_freq` | REAL | Source repetition rate (Hz) |
| `q_speed` | REAL | Speed of light fraction in fibre |
| `q_delay` | REAL | Initial quantum channel delay (ns) |
| `len_loss` | REAL | Fibre attenuation (dB/km) |
| `init_loss` | REAL | Coupling/insertion loss at source, linear fraction |
| `detector_eff_z` | REAL | Z-basis detector efficiency |
| `detector_eff_x` | REAL | X-basis detector efficiency; NULL means same as Z |
| `dark_count` | REAL | Dark count rate (cps) |
| `node_loss_db` | REAL | Receiver-side node/connector loss (dB) |
| `source_err_rate` | REAL | Source bit error rate |
| `dephasing_rate` | REAL | Fibre dephasing rate (per km) |
| `runtimes` | INTEGER | Number of Monte Carlo runs in this batch |
| `config_preset` | TEXT | Config JSON path used; NULL if using DEFAULTS |
| `bs_eff` | REAL | Beam splitter efficiency at relay (MDI only; NULL for BB84) |
| `charlie_pos` | REAL | Charlie position as fraction from Alice (MDI only; NULL for BB84) |
| `key_rate` | REAL | Secure key rate (bps); NULL if run failed |
| `qber` | REAL | Quantum bit error rate; NULL if run timed out |
| `key_len` | INTEGER | Sifted key length (bits); NULL if run failed |
| `status` | TEXT | `success`, `qber_cutoff` (QBER > 11%), or `timeout` |

---

### `network_results`

One row per network simulation call — one protocol × one seed × one sweep point (K or N value).
Populated by `relay_sweep.py` and `user_sweep.py`.
Physical parameters for each pair are recoverable via JOIN on `net_run_id` to `p2p_results`.

| Column | Type | Description |
|---|---|---|
| `row_id` | INTEGER PK | Auto-increment row identifier |
| `net_run_id` | TEXT | UUID linking to `p2p_results.net_run_id` |
| `run_timestamp` | TEXT | ISO8601 timestamp of run start |
| `experiment` | TEXT | `relay_sweep` or `user_sweep` |
| `protocol` | TEXT | `BB84`, `MDI`, or `trusted_BB84` |
| `n_users` | INTEGER | Number of users in the network |
| `k_relays` | INTEGER | Number of relay nodes; NULL for direct BB84 only |
| `area_km` | REAL | Side length of square deployment area (km) |
| `seed` | INTEGER | Random seed used for user/relay placement |
| `runtimes` | INTEGER | Monte Carlo runs per pair |
| `config_preset` | TEXT | Config JSON path used; NULL if using DEFAULTS |
| `n_pairs` | INTEGER | Number of user pairs simulated |
| `total_fibre_km` | REAL | Total fibre deployed in the network (km) |
| `avg_pair_distance_km` | REAL | Mean Alice–Bob distance across all pairs (km) |
| `cross_relay_ratio` | REAL | Fraction of pairs routed across relay nodes; populated for MDI and trusted BB84; NULL for direct BB84 |
| `avg_key_rate` | REAL | Mean key rate across all valid pair runs (bps) |
| `std_key_rate` | REAL | Standard deviation of key rate across valid runs (bps) |
| `success_rate` | REAL | Fraction of runs with QBER below cutoff |
| `min_key_rate` | REAL | Minimum key rate across valid runs (bps) |
| `max_key_rate` | REAL | Maximum key rate across valid runs (bps) |

---

## Joining tables

To recover per-run pair data for a network experiment:

```sql
-- MDI pair data
SELECT p.*, n.experiment, n.n_users, n.k_relays, n.seed
FROM p2p_results p
JOIN network_results n ON p.net_run_id = n.net_run_id
WHERE n.experiment = 'relay_sweep'
  AND n.protocol   = 'MDI'
  AND n.k_relays   = 4;

-- trusted BB84 user-relay link data
SELECT p.fibre_len, p.key_rate, n.k_relays, n.seed
FROM p2p_results p
JOIN network_results n ON p.net_run_id = n.net_run_id
WHERE n.protocol = 'trusted_BB84';
```

To query standalone P2P sweep results:

```sql
SELECT * FROM p2p_results
WHERE net_run_id IS NULL
  AND protocol   = 'BB84'
  AND fibre_len  = 50.0;
```
