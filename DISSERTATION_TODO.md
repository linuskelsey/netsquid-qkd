# Dissertation TODO
> Generated 2026-08-03 from audit of `dissertation.tex`, `ROADMAP.md`, `TODO.md`, and `cost rethink/cost_analysis.tex`.
> Updated 2026-08-03: cost model stripped from simulation code entirely. Cost analysis is now purely analytical in the dissertation (component count formulae with free parameters α, β). No cost sweep scripts; no £ columns in DB. Simulation code outputs (N, K, avg_key_rate, total_fibre_km) only.
> Updated 2026-08-07: re-audited against current `dissertation.tex` (§4 Results still empty except Deployment Recommendations; §5/§6 substantially drafted) and hardware-param sourcing completed 2026-08-06 (all 10 layer params now cited). Ticked items confirmed done below; stale values/premises noted inline.
> Organised by category. Items marked **[BLOCKING]** must be done before submission.

---

## 1. Code Bugs (fix before final data runs)

- [x] **`mdi_network.py`**: return dict `"n_spd"` corrected to `4 * topo.K`. *(moot post cost-strip but fixed for completeness)*
- [x] **`lib/functions.py` / JSON configs**: node loss unified to single `node_loss_db = 2.0 dB` for both BB84 and MDI. `node_loss_db_mdi` removed. `SWITCH_LOSS_DB = 0.0`. Noted as limitation in §5.
- [x] **Strip all cost code** — removed `cost_sweep.py`, `network/cost.py`, `update_network_cost` calls from all sweep scripts, cost columns from DB schema and `lib/db.py`, cost imports from `user_sweep.py` / `relay_sweep.py`. DB consolidated: old cost-schema results.db (30k rows) deleted; results_to_Aug.db (11M rows, no cost cols) renamed to results.db.

---

## 2. New Code / Features (needed for thesis results)

- [x] **Real-topology input tool**: `network/real_topology.py` — equirectangular lat/lon → km projection; JSON format with `"nodes"` (type: user/relay) and `"protocols"` fields; `load_real_topology()` returns `(Topology, meta)`. `--real NAME` flag on `user_sweep.py` and `cost_sweep.py` loads `data/real_topologies/NAME.json`, fixes relay positions, enforces 30 km catchment radius for clustered placement, skips k-means. Users generated incrementally (pool of n_max sliced per data point). TBB84 gated by `"protocols"` in JSON — only available in `--real` path. BT topology at `data/real_topologies/bt.json` (Slough, West End, City of London; 3 relays; BB84+MDI+TBB84). `relay_sweep.py` excluded (K sweep meaningless with fixed real topology).

- [x] **`--tortuosity FLOAT` flag** on all network sweep scripts (default 1.0 = off). Per-cable factor drawn from truncated normal(mean, σ=0.1), min 1.0. Affects simulated key rate via longer fibre distances; `total_fibre_km` in DB reflects tortuous lengths.
- ~~**Cost columns in DB**~~ — stripped; cost is analytical in dissertation, not stored in DB.
- ~~**Cost–rate optimisation sweep**~~ — replaced by analytical model in dissertation §4 (component count formulae with free parameters; crossover N discussed qualitatively).

---

## 3. Simulations to Run (data collection)

- [ ] **[HIGH PRIORITY] Regenerate all figures** — hardware defaults updated (fibre_loss 0.2→0.18, detector_efficiency 0.65→0.90, dark_count_rate 100→50, source_error_rate 0.005→0.015) and node_loss_db unified across protocols. All existing P2P and network figures are stale and must be rerun before thesis submission. *(Plotting infra as of 2026-08-07: every P2P/network script now takes `--output-dir` and writes a `{plot.png, plot.tex, assumptions.md}` bundle — Times New Roman/LaTeX styling, titles cut to ≤6 words, sweep params dumped to assumptions.md instead of cluttering the plot. Ready to run for real now; `scripts/P2P/compare/run_all.py --output-dir ...` sweeps all 11 P2P comparisons in one go.)*
- [ ] **Re-run `sensitivity.py` and `compare/efficiency.py`** (2026-08-09 changes): `sensitivity.py` now has two separate detector-efficiency bars (SPAD η_d=0.20, IDQ ID230 midpoint; SNSPD η_d=0.90) instead of one; `compare/efficiency.py`'s SPAD shaded band corrected from the old InGaAs-SPAD figure (0.15–0.30) to the IDQ ID230-cited range (0.10–0.25) already used elsewhere in the diss, band label updated to "IDQ ID230 SPAD". Both scripts are cheap to run (sensitivity.py is not a large sweep) — rerun and swap in the new figures before citing Figure~\ref{fig:sensitivity} or Figure~\ref{fig:p2p_efficiency} numbers in §4/§5.
- ~~**Cost sweep**~~ — removed; cost treated analytically in dissertation.
- ~~**Cost–rate optimisation sweep**~~ — removed; crossover point derived analytically from component count formulae.
- [ ] **Realistic hardware region shading**: finalise hardware parameter values from Lo 2012 (`\cite{Lo_2012}`), Tang 2016 (`\cite{Tang_2016}`), Berrevoets 2022 (`\cite{Berrevoets_2022}`); add to all P2P compare figures as shaded region. (TODO.md §1)
- [ ] **Literature validation on `layers.py`**: identify 2–3 published key rate vs distance curves per protocol; overlay as scatter markers on layers figure. (TODO.md §2)
- [ ] **MC run count audit**: for rates of order 10⁻ˣ target 10^(x+1) samples per point; audit all scripts and increase where under-sampled. (ROADMAP Analysis)
- [ ] **MDI network-scale key rate gap experiment**: targeted simulation to isolate which factors explain the ~10× gap (vs ~3× at P2P). Candidate causes: relay routing adds distance, BSM η² dependency, switch insertion loss, cross-cluster routing. Run with each effect disabled in turn. (ROADMAP Open Questions + Project Report) *(Partial head start: a prior session already found and DB-confirmed the geometric mechanism — `avg_pair_distance_km` for MDI rises with N (18.1→19.0 km, N=11→19) while BB84 stays flat at ~12.7 km, explained by triangle-inequality relay detour on cross-cluster pairs. See project memory "MDI Geometric Finding". This covers the "relay routing adds distance" / "cross-cluster routing" causes but not BSM η² or switch loss — still worth a dedicated ablation run for those two.)*

---

## 4. Model Parameters — Verification

All parameters below are unverified placeholders or indicative midpoints. Verify each against literature or supplier datasheets before citing in thesis. Entries marked **[graph range]** are swept in existing compare/P2P figures and the realistic range stated here should be confirmed and used as the shaded region boundary.

### 4a. Hardware Physics Parameters (`lib/functions.py` DEFAULTS)

| Parameter | Current default | Realistic range | Graph-swept? | Verify against | Datasheet / link |
|---|---|---|---|---|---|
| `fibre_loss_db_per_km` | **0.18 dB/km** ✓ | 0.15–0.25 dB/km | **Yes** | Corning SMF-28 datasheet (max at 1550 nm, confirmed) | https://www.corning.com/media/worldwide/coc/documents/Fiber/product-information-sheets/PI-1424-AEN.pdf|
| `init_loss` | **0.10** ✓ *(was 0.15)* | 0.05–0.30 | Possibly | OZ Optics DTS0092 PM fused coupler, 0.4dB max excess loss (polarisation-orthogonal combining avoids reciprocal 3dB split loss). Cited in code + Simulation Model Limitations prose. | https://www.ozoptics.com/ALLNEW_PDF/DTS0092.pdf |
| `detector_efficiency` η_Z | **0.90** ✓ | SPAD: 10–25% (IDQ ID230); SNSPD: 80–95% (IDQ ID281) | **Yes** | IDQ ID230 (SPAD, default 20%); IDQ ID281 (SNSPD, default 90%). Multi-channel: 1 unit = 4 ch per relay. Quote requested. | IDQ ID230: https://www.idquantique.com/quantum-detection-systems/products/id230/ IDQ ID281: https://www.idquantique.com/quantum-detection-systems/products/id281-snspd-system/|
| `dark_count_rate` | **50 cps** ✓ | SNSPD: 25–100 cps (ID281); SPAD: 70–90 cps at η=10%, 150–250 cps at η=20% (ID230) | **Yes** | IDQ datasheets. SPAD d_c coupled to η — realistic SPAD point = η=0.20 + d_c=200 together. | (same as η_Z links) |
| `node_loss_db` (both protocols) | **2.0 dB** ✓ | 1.0–4.0 dB | No | Duplinskiy et al. 2017, Opt. Express 25(23):28886 — measured Bob-receiver insertion loss (LiNbO3 phase mod + PBS). Lumped-approximation limitation written in §Simulation Model Limitations (EOM+PBS for BB84 vs HOM+PBS+switch for MDI not broken out separately; future work). | Duplinskiy et al. 2017 |
| `source_error_rate` | **0.015 (1.5%)** ✓ | 0.001–0.05 | **Yes** | Quandela Prometheus: g²(0) < 3% → ε_s < 0.015. Bozzio 2022 upper bound 2%. | Prometheus datasheet: https://www.quandela.com/products-and-services/prometheus/|
| `det_eff_x` η_X | **0.715** ✓ *(was 0.85)* | same as η_Z | Partially (basis_bias sweep) | Grasselli et al. 2025, PRApplied 23:044011 — 1dB extra insertion loss for test-basis stage. | Grasselli et al. 2025 |
| `dephasing_rate` | **3.2e-7 /km** ✓ *(was 0.0001 /ns)* | derived, not swept as a range | Possibly | Corning SMF-28 PMD spec ($D_\text{PMD}=0.04$ps/√km) + IDQ ID281 timing window. | Corning SMF-28 PMD spec |
| `bs_eff` | **0.97** ✓ | 0.87–0.99 | **Yes** (MDI compare) | Thorlabs TN1550R5F2, 0.15dB excess loss. | Thorlabs TN1550R5F2 |

All 10 hardware-model params now sourced/cited as of 2026-08-06 (was 5/10). Derivations live in the "Layer N" prose paragraphs of `dissertation.tex`, not table footnotes.

- [ ] **Confirm sweep ranges** used in compare figures match the realistic ranges above. Where they differ, update the compare script x-ranges and re-shade. *(Still needs a manual pass — params are now sourced but nobody has cross-checked each compare script's `REALISTIC_MIN/MAX` shading against the literature ranges above.)*
- [x] **`node_loss_db`** (2.0 dB unified): now sourced (Duplinskiy et al. 2017) and the lumped-approximation limitation is written out in §Simulation Model Limitations — no longer an "unverified" gap, just an explicitly-acknowledged simplification.

### 4b. Cost Model (analytical — no code)

Cost is expressed in the dissertation as component count formulae with free parameters $c_s$ (source), $c_d$ (detector), $c_f$ (fibre/km). No absolute £ values required in code. For the dissertation discuss qualitatively using literature ranges:

| Component | Indicative range | Notes |
|---|---|---|
| QD source | very high (£100k–£300k) | Cryogenic; unverified; discuss as barrier |
| SNSPD | high (£50k–£150k) | Cryogenic; drives MDI relay cost |
| SPAD | moderate (£5k–£30k) | Room-temp; lower η |
| Fibre (dark, installed) | £5k–£15k/km | Region-dependent |
| Passive optics (BS, PBS, EOM) | low (£0.5k–£5k each) | Negligible vs sources/detectors |

- [ ] In dissertation §3 cost methodology: state component count formulae for BB84, MDI, TBB84 (already in `cost_analysis.tex`); express costs symbolically; discuss qualitative scaling (O(N²) fibre for BB84 vs O(N) for MDI/TBB84).
- [ ] In dissertation §4: derive crossover N analytically (where MDI total cost < BB84); show it depends on ratio $c_s / c_f$ and discuss which regime (source-dominated vs fibre-dominated) favours each protocol.

---

## 5. Dissertation Writing

### §3 Methodology — Cost Analysis
- [x] Write component count formulae for BB84, MDI. Expressed symbolically with free parameters $c_s, c_d, c_f$ (Eqs cost\_bb84 / cost\_mdi in dissertation.tex). TBB84 cost formulae deferred — TBB84 is only in --real path, out of scope for main methodology.
- [x] State assumptions: CapEx only, classical comms free (sunk cost of existing infra), absolute prices unverified — results are scaling analysis only.
- [x] Mention and cite ONDM 2025 (`\cite{DBLP:conf/ondm/KaraviasHBLP25}`) as prior cost work; noted it uses ILP optimisation for PM-QKD with concrete prices; this work extends to MDI symbolically.
- [x] Tortuosity model written (truncated normal, μ=1.2, σ=0.1); noted as affecting simulated key rate via longer fibre loss only (not cost directly since cost is symbolic).
- [ ] §4 Results: write cost analysis prose — present component count scaling table (already Tab:components); derive or cite the crossover N* argument; discuss which c_d/c_f regime favours each protocol.

### §3 Methodology — NetSquid / Simulation Architecture
- [x] Describe NetSquid DES engine and why it was chosen; cite `\cite{Coopmans_2021}`. *(DES vs analytical justification: extensibility to repeater chains; density matrix / Kraus operator framing.)*
- [x] Describe ten-layer hardware model: each layer, what impairment it adds, cite physical motivation. *(§Hardware Model subsubsection; layer table + layer-5 node loss caveat written.)*
- [x] Describe multiprocessing architecture (pool per protocol, seeds split across cores). *(spawn context rationale, 80% pool, batch-100 P2P vs single pool.map network, written.)*
- [x] Describe SQLite persistence (`lib/db.py`), how results are stored and queried. *(p2p_results + network_results tables described; post-hoc filtering rationale stated.)*

### §3 Methodology — Bipartite Single-Link Analysis
- [x] Describe BB84 and MDI-QKD protocol implementations in NetSquid. *(Full BB84 encoding/loss/detection/sifting + MDI 3-node/BSM/basis-corrections written.)*
- [x] Explain Monte Carlo statistics: runtimes per point, key rate extraction, QBER cutoff application. *(Key rate = ℓ/T equation; QBER formula; 11% cutoff stated.)*
- [x] **Justify QBER cutoff at 11%**: cite Shor–Preskill proof (already `\cite{Shor_2000}`); state explicitly. *(Written; Shor_2000 cited.)*
- [x] Describe key rate formula: key length / simulation time. *(eq:key_rate written; nanosecond timestamp arithmetic stated.)*

### §3 Methodology — Multi-User Network Analysis
- [x] Describe topology generator: random user placement on A×A km grid, k-means relay placement. *(place_users uniform grid; optimise_relays k-means n_init=10 written.)*
- [x] **Justify k-means relay placement**: centroid minimises sum squared distances → minimises expected path loss; k-means generalises to K>1. *(Karavias citation removed; mathematical argument written.)*
- [x] **Justify multi-seeding**: averaging over random topologies removes single-topology bias; inter-seed std small relative to protocol gap justifies seed count. *(Written.)*
- [x] Describe BB84 mesh and MDI network simulators: what each computes, how pairs are aggregated. *(Per-link tortuosity, N(N-1)/2 pairs for BB84; N + K(K-1)/2 physical cables for MDI written.)*
- [x] Describe cross-relay routing model for MDI (cross-cluster path via relay backbone). *(Same-cluster vs cross-cluster arm lengths; eq:charlie_pos geometrically derived; SWITCH_LOSS_DB=0 limitation noted.)*

### §4 Results (currently: "bunch of graphs...")
- [ ] **P2P performance**: present layers figure + selected parameter sweeps; refer to parameter impact table.
- [ ] **Network key rate vs relay count** and **vs user count**: present relay_sweep and user_sweep figures.
- [ ] **Network key rate gap**: explain MDI ~10× vs BB84 (supported by experiment or cited causes).
- [ ] **Cost analysis**: present component count scaling argument (Tab:components already in tex); narrate $\mathcal{O}(N^2)$ vs $\mathcal{O}(N)$ fibre result; discuss crossover N* dependence on $c_d/c_f$ ratio; note SNSPD multi-channel packaging caveat and OpEx omission.
- [ ] **Parameter impact summary table**: one row per physical parameter (fibre loss, detector efficiency, dark count rate, node loss, init loss, source error, dephasing, basis bias, BS efficiency, Charlie position); columns = BB84 and MDI key rate reduction (% or ×) across the realistic operating range. Replaces or supplements 10 individual compare figures. (ROADMAP Project Report)
- [x] **Deployment Recommendations subsection**: full prose written — frames $R_\min \to K^*$ via the relay sweep, ties to $C_\text{MDI}$ vs $C_\text{BB84}$ symbolically, states the crossover depends on $c_d/c_f$. Still references $K^*$/$N^*$ symbolically since the actual sweep numbers aren't plugged in yet — revisit once §4 P2P/Network/Cost subsections have real figures and numbers.

### §5 Discussion (currently: "Discuss results?")
- [x] Critical analysis: MDI rate penalty vs security gain — §The Security–Rate Trade-off written (BSM coincidence → $\eta_\text{arm}^2$ scaling explanation, network-level widening via relay detour). Numeric cross-over point still symbolic/qualitative — needs real numbers once §4 results exist.
- [x] Cost model limitations: written in dissertation.tex (§Cost Model Limitations) — component price data unavailable → symbolic model; OpEx not modelled; BB84 O(N²) fibre is upper bound.
- [x] Note that cost and simulation are decoupled by design: simulation gives key rate, cost model is analytical; explicitly stated as design choice not a limitation.
- [x] Note TBB84 trust assumption vs MDI: relay node compromise vs detector side-channel attacks. Written 2026-08-07 as new paragraph in §The Security–Rate Trade-off (`sec:security_rate`) — MDI relay discloses only joint correlation (no trust needed) vs TBB84 relay handling plaintext-equivalent key material (compromise = full key exposure at that hop). Also explains why TBB84 is excluded from the core metro-scale relay/user sweeps and only exercised in the real-topology path — fixed a stale claim in §Simulation Model Limitations ("Metropolitan network scope") that said neither trusted-relay nor repeater architectures were modelled, when TBB84 actually is (just not in the main comparison).
- [x] Energetic footprint: cite `\cite{Yehia_2025}`; cryogenic OpEx noted as unmodelled — written in §Cost Model Limitations ("Operational expenditure" paragraph).

### §6 Conclusion (currently: skeleton notes)
- [x] Summary of Contributions: written in dissertation.tex (§Summary of Contributions) — 10-layer model, network simulators, symbolic cost model, DB persistence.
- [ ] Present findings: key rate gap quantified (placeholder bullets in tex — need actual numbers); cost crossover N* depends on $c_d/c_f$ (written).
- [ ] Future work: finite-key corrections, WCP/decoy-state source model, ILP relay placement, WDM multi-user MDI, traffic-aware relay count optimisation (queueing model), TF-QKD extension. *(already drafted in dissertation.tex §Future Work)*

### §2 Background — minor fixes
- [x] HOM explanation written in-line (§MDI subsection, cites `\cite{Hong_1987}`) — comment resolved, no separate appendix needed.
- [x] Check Table~\ref{tab:mdi_flips} (bit-flip rules): user confirmed 2026-08-07 — copied from lit review, matches Lo et al. 2012.
- [ ] Abstract: "up to 10 times" — still unconfirmed; §4 Results and §6 Findings are both empty/placeholder, so there's no data yet to support or contradict this number.

---

## 6. Referencing

### Missing citations needed in dissertation
- ~~Citation for QD photon source cost (£150k)~~ — moot; absolute costs removed from dissertation.
- [x] Citation for SPAD η / dark count specs: IDQ ID230 datasheet — `\cite{idq_id230}` added to bib and used in §3.2.1 detector note.
- [x] Citation for SNSPD η / dark count specs: IDQ ID281 datasheet — `\cite{idq_id281}` added to bib and used in hardware model table + §3.2.1 detector note.
- ~~Citation for dark fibre installation cost per km~~ — moot; $c_f$ is a free symbolic parameter.
- [ ] Citation for EOM insertion loss range (0.5–3 dB): standard photonics reference — needed for §7 node\_loss justification.
- [x] Citation for 11% QBER threshold: `\cite{Shor_2000}` cited in §Bipartite Single-Link Analysis.

### Citations to verify compile correctly
All of the following are in `bibliography.bib` but confirm they appear in the compiled `.bbl` with no warning:
- [x] `\cite{Dynes_2019}` — Cambridge quantum network
- [x] `\cite{Yan2025}` — MDI-QKD with frequency comb
- [x] `\cite{Yehia_2022}` — Quantum City simulation
- [x] `\cite{Yehia_2025}` — energetic analysis
- [x] `\cite{DBLP:conf/ondm/KaraviasHBLP25}` — comparative cost analysis ONDM 2025
- [x] `\cite{Berrevoets_2022}` — deployed MDI-QKD
- [x] `\cite{Martins2024}` — MadQCI heterogeneous network
- [x] `\cite{eu_open_qkd}` — OpenQKD project

### Bibliography hygiene
- [ ] `\cite{PNS_desc}` currently points to EITCA (non-peer-reviewed); consider replacing with `\cite{Brassard_2000}` or `\cite{Chen2022}` for a more citable source.
- [ ] Check all `author = {... and others}` entries — some journals require full author lists; verify if UCL submission requires it.

---

## 7. Assumptions & Justifications Required

Every item below is an assumption baked into the simulation or cost model that must be **explicitly stated and justified** in the dissertation (methodology or limitations). The justification approach is noted alongside each.

### Simulation / Protocol Assumptions

- [x] **QBER cutoff at 11%**: stated in §Bipartite Single-Link Analysis; Shor_2000 cited; MDI application noted as conservative bound.
- [x] **Asymptotic key rate (no finite-key corrections)**: written in §Simulation Model Limitations ("Asymptotic key rates" paragraph) — states finite-key penalty is expected worst for MDI at long distances.
- [x] **Ideal single-photon sources (not WCP/decoy)**: written in §Simulation Model Limitations ("Ideal single-photon sources" paragraph) — upper-bound-on-rate / lower-bound-on-cost framing, `\cite{Lo_decoys}` cited.
- [x] **`source_error_rate = 0.015` (was documented as 0.005 — stale)**: sourced to Quandela Prometheus g²(0)<3% specification, coded inline in `lib/functions.py`.
- [x] **`node_loss_db = 2.0 dB`**: sourced (Duplinskiy et al. 2017) and lumped-approximation limitation written in §Simulation Model Limitations ("Receiver node loss" paragraph, explicitly notes EOM/PBS vs HOM/PBS/switch are not broken out).
- [x] **`init_loss = 0.10` (was documented as 0.15 — stale)**: correction to earlier audit — full derivation prose already exists in the Layer~4 paragraph of §Hardware Model (not §Discussion, which is where I'd checked): OZ Optics DTS0092 max excess loss 0.4dB → $L_i = 1-10^{-0.4/10}\approx0.09$, rounded up to 0.10. Nothing further needed.
- [x] **`dephasing_rate = 3.2e-7 /km` (was documented as 0.0001 — stale, and wrong units: was /ns not /km)**: sourced to Corning SMF-28 PMD spec + IDQ ID281 timing window.
- [x] **`bs_eff = 0.97` (BSM beam splitter efficiency)**: sourced to Thorlabs TN1550R5F2 (0.15dB excess loss).
- [x] **Linear-optical BSM discriminates only ψ⁺ and ψ⁻**: stated in §Bipartite Single-Link Analysis with BSM outcome table and 50% constraint; Lo_2012 cited.
- [x] **`dark_count_rate` SPAD-mode inconsistency**: moot — `--detector-tech` flag no longer exists in the codebase (removed in the cost-strip cleanup); default is now 50 cps (IDQ ID281 SNSPD), sourced.
- [x] **Euclidean (flat-grid) topology**: moot as originally worded — per-cable tortuosity ($\tau \sim \mathcal{N}(1.2, 0.1^2)$ truncated) was added after this TODO item was written and is fully described in §Multi-User Network Analysis, including the "duct routes longer than straight-line" justification this item asked for.

### Network Modelling Assumptions

- [x] **k-means relay placement**: written in §Multi-User Network Analysis — centroid minimises sum squared distances; k-means generalises to K>1; ILP-optimal deferred to future work.
- [ ] **Multi-seeding (seed count justification)**: seed count stated in text but diminishing-returns argument or inter-seed variance plot not yet included — add when results figures are available. *(Possibly relevant: the MDI-rate-vs-N geometric finding from DB analysis — see project memory — used 20 seeds/75 runtimes and found a clean, low-noise trend; could double as evidence for seed-count adequacy.)*
- [ ] **TBB84 backbone: 1 source per relay (not K−1)**: relay backbone uses one QD source per relay node for relay-to-relay BB84. Strict bidirectional full-mesh backbone would require K−1 sources per relay (K(K−1) total). State simplification and bound the error: for K≤8 the undercount is ≤7× on backbone source cost. (cost_analysis.tex §9.6)
- [ ] **TBB84 backbone: unidirectional links (K(K−1)/2 sessions)**: simulated as half-duplex shared key per relay pair. Full duplex (separate key per direction) would double backbone rate and source count. State and justify or flag as a limitation. (cost_analysis.tex Inconsistency VII)
- [ ] **TBB84 classical XOR forwarding is secure**: the relayed message K_AR1 ⊕ K_R1R2 is a one-time pad; in-flight interception reveals nothing. State clearly that the trust assumption is on the relay *node* (physical security), not the classical link. (already discussed in cost_analysis.tex §4.3)
- [ ] **Monte Carlo run count choice**: state how many runtimes per point are used and why. For low key rates, more samples reduce variance; audit whether the chosen count is adequate. (ROADMAP Analysis)

### Cost Model Assumptions

- [x] **CapEx only, no OpEx**: stated in dissertation.tex §Cost Model and §Cost Model Limitations; cites `\cite{Yehia_2025}`.
- [x] **Classical communications free**: stated as sunk cost of existing infrastructure in §Cost Model intro.
- [x] **BB84 mesh: one dark fibre per user pair**: stated as upper bound applicable to passive dark-fibre mesh deployments; WDM/switched caveat noted in §Cost Model Limitations.
- ~~**SPD cost linear in η**~~ — moot; linear cost model removed. Cost is now symbolic ($c_d$ per detector, no η dependence).
- ~~**QD source at £150,000**~~ — moot; absolute prices removed. Cost is $c_s$ (free parameter).
- ~~**TX coupling loss has no cost entry**~~ — moot; cost model is symbolic, no component-level price entries.
- ~~**Optical switch: cost vs insertion loss asymmetry**~~ — moot; switch cost absorbed into symbolic relay hardware term (omitted for clarity in Eqs).
- [x] **Cost and simulation models are not tightly coupled**: stated explicitly as design choice (simulation gives key rate; cost model is analytical). Mentioned in §Simulation Model Limitations (receiver node loss discussion).

---

## 8. Miscellaneous

- [ ] **Word/page count**: check dissertation is within UCL MSc Quantum Technologies project report page limit.
- [ ] **Figure captions**: all figures need captions that are self-contained (readable without surrounding text).
- [ ] **Figure references**: every figure must be referenced in the text with `Figure~\ref{fig:...}`; check none are orphaned.
- [ ] **Spell check**: run `aspell` or equivalent on dissertation.tex; enforce British English throughout (`\cite{}` keys and code names exempt).
- [ ] **Compile clean**: ensure `dissertation.tex` compiles with zero warnings on two-pass `pdflatex` + `bibtex` run before submission.
- [ ] **Case study** (`docs/case-study-tex/case-study.tex`): confirm whether this is submitted alongside the main dissertation or is separate; if submitted, apply same checks.
