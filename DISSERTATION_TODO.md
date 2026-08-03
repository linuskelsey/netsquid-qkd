# Dissertation TODO
> Generated 2026-08-03 from audit of `dissertation.tex`, `ROADMAP.md`, `TODO.md`, and `cost rethink/cost_analysis.tex`.
> Organised by category. Items marked **[BLOCKING]** must be done before submission.

---

## 1. Code Bugs (fix before final data runs)

- [x] **`mdi_network.py`**: return dict has `"n_spd": 2 * topo.K` — stale, cost model uses 4K. Update to `4 * topo.K`. (cost_analysis.tex Inconsistency IV)
- [x] **`cost_sweep.py`**: when `--detector-tech SPAD`, `dark_count_rate` stays at 100 cps (SNSPD-tier). Couple dark count to detector class: SPAD → ~10,000 cps, SNSPD → ~100 cps. (cost_analysis.tex Inconsistency II)
- [x] **`lib/functions.py` / JSON configs**: protocol-specific node loss implemented. BB84=2.0 dB, MDI=1.0 dB per arm, TBB84=3.0 dB. Fallback pattern: runners use `cfg.get("node_loss_db_mdi/tbb84", cfg["node_loss_db"])`. (cost_analysis.tex Inconsistency I)

---

## 2. New Code / Features (needed for thesis results)

- [ ] **[HIGH PRIORITY] Real-topology input tool**: implement a mechanism to load a fixed QKD network graph (node positions + edges) and feed it directly into the existing simulators instead of random generation. Use cases: real-world named networks (BT, Tokyo, Berrevoets et al.) and case study topologies fixed to real geography. Design questions to resolve before implementing:
  - Input format: JSON or adjacency list specifying node positions (lat/lon or km-grid coords), node types (user/relay), and optionally fixed link distances.
  - Entry point: likely a new flag on `relay_sweep.py` / `user_sweep.py` (e.g. `--topology PATH`) that replaces `topology.py`'s random generator with a loaded graph.
  - Relay placement: skip k-means when topology is fixed; relay positions come from the input file.
  - Visualisation: `visualise_network.py` should render the loaded topology correctly alongside simulation output.
  - Cost model: `total_fibre_km` must be computed from the fixed link distances rather than Euclidean node positions.

- [ ] **Cost columns in DB**: implement `ALTER TABLE network_results ADD COLUMN ...` for `detector_efficiency`, `hardware_cost_gbp`, `fibre_cost_gbp`, `total_cost_gbp`, `spd_cost_gbp`, etc. (see proposed SQL in `cost rethink/cost_analysis.tex` §8). Insert cost breakdown at simulation write time in `cost_sweep.py`.
- [ ] **DB cost reconstruction**: `--cost` flag on `scripts/analyse/network.py` — query `total_fibre_km` from historical `network_results` rows, apply `component_counts` + `total_cost` from `network/cost.py`, produce cost/efficiency curves without re-running simulations. (ROADMAP Planned)
- [ ] **Cost–rate optimisation sweep**: sweep relay count K at fixed N and area; extract (total_cost_gbp, avg_key_rate) per configuration per protocol; identify cost-optimal and rate-optimal configurations; plot cost vs rate for each protocol. Needed for the Deployment Recommendations section in the dissertation. (ROADMAP Planned, dissertation §4)
- [ ] **`--tortuosity FLOAT` flag** on `cost_sweep.py` (default 1.0) to scale all fibre distances before cost computation without affecting simulation physics. Useful for sensitivity analysis; note typical urban values 1.2–1.5×.

---

## 3. Simulations to Run (data collection)

- [ ] **[HIGH PRIORITY] Regenerate all figures** — node_loss_db (now protocol-specific) and dark_count_rate (now coupled to detector class) both affect simulated key rate. All existing P2P and network figures are stale and must be rerun before thesis submission.
- [ ] **Cost sweep — SPAD and SNSPD** at representative N range (e.g. N=2..16, K=2): cost vs N and cost-efficiency vs N for all three protocols → figure for thesis §4.
- [ ] **Cost–rate optimisation sweep** (K grid at fixed N, multi-seed): (cost, avg_key_rate) pairs for BB84/MDI/TBB84 → cost vs rate figures per protocol.
- [ ] **Realistic hardware region shading**: finalise hardware parameter values from Lo 2012 (`\cite{Lo_2012}`), Tang 2016 (`\cite{Tang_2016}`), Berrevoets 2022 (`\cite{Berrevoets_2022}`); add to all P2P compare figures as shaded region. (TODO.md §1)
- [ ] **Literature validation on `layers.py`**: identify 2–3 published key rate vs distance curves per protocol; overlay as scatter markers on layers figure. (TODO.md §2)
- [ ] **MC run count audit**: for rates of order 10⁻ˣ target 10^(x+1) samples per point; audit all scripts and increase where under-sampled. (ROADMAP Analysis)
- [ ] **MDI network-scale key rate gap experiment**: targeted simulation to isolate which factors explain the ~10× gap (vs ~3× at P2P). Candidate causes: relay routing adds distance, BSM η² dependency, switch insertion loss, cross-cluster routing. Run with each effect disabled in turn. (ROADMAP Open Questions + Project Report)

---

## 4. Cost Model — Verification

All default costs in `network/cost.py` are unverified placeholders. Verify each against literature or supplier datasheets before citing in thesis.

- [ ] **QD photon source £150,000**: check against Quandela Prometheus (already in bib as `\cite{QuandelaSPS}`) or equivalent; confirm includes cryostat amortisation.
- [ ] **InGaAs SPAD η=0.20, £15,000**: verify efficiency and price; check dark count rate (expected ~1,000–50,000 cps) for Inconsistency II fix.
- [ ] **SNSPD η=0.85, £100,000**: verify efficiency and price; check dark count rate (expected ~1–100 cps).
- [ ] **50:50 fibre coupler (HOM BS) £1,000**: verify.
- [ ] **PBS £500**: verify.
- [ ] **EOM £2,000**: verify; also check insertion loss (0.5–3 dB, needed for Inconsistency I fix).
- [ ] **Optical switch £5,000**: verify; check insertion loss (0.5–2 dB, needed for Inconsistency I fix).
- [ ] **Dark fibre installed £10,000/km**: this varies significantly by region and duct availability; find a UK-relevant citation or acknowledge the range.
- [ ] **Verify per-protocol node_loss_db values against literature**: BB84 (EOM+PBS), MDI per arm (BS excess+PBS), TBB84 (switch+EOM+PBS). Current values (2.0 / 1.0 / 3.0 dB) are indicative midpoints. Update `lib/functions.py` DEFAULTS and `configs/layer5_node_loss.json` once confirmed.
- [ ] Once values verified: update `PARAMS.md` and `DEFAULT_COSTS` in `network/cost.py`, and cite sources in dissertation cost methodology section.

---

## 5. Dissertation Writing

### §3 Methodology — Cost Analysis (currently: two-line stub)
- [ ] Write full algebraic cost model section: component counts per protocol, SPD linear model (η → cost), total cost formula, cost-rate optimisation framing (fixed budget / fixed rate dual problems). Reference `network/cost.py` and `cost rethink/cost_analysis.tex`.
- [ ] State all cost model assumptions explicitly: Euclidean topology (no tortuosity), CapEx only (no OpEx), classical comms free, QD source fixed, TBB84 backbone source count simplified (1 per relay vs K−1 strict).
- [ ] Mention and cite the ONDM 2025 paper (`\cite{DBLP:conf/ondm/KaraviasHBLP25}`) as the most directly related prior cost work; note it covers PM and entanglement-based QKD but not MDI.

### §3 Methodology — NetSquid / Simulation Architecture (currently: stub)
- [ ] Describe NetSquid DES engine and why it was chosen; cite `\cite{Coopmans_2021}`.
- [ ] Describe ten-layer hardware model: each layer, what impairment it adds, cite physical motivation.
- [ ] Describe multiprocessing architecture (pool per protocol, seeds split across cores).
- [ ] Describe SQLite persistence (`lib/db.py`), how results are stored and queried.

### §3 Methodology — Bipartite Single-Link Analysis (currently: stub)
- [ ] Describe BB84 and MDI-QKD protocol implementations in NetSquid.
- [ ] Explain Monte Carlo statistics: runtimes per point, key rate extraction, QBER cutoff application.
- [ ] **Justify QBER cutoff at 11%**: cite Shor–Preskill proof (already `\cite{Shor_2000}`); state explicitly.
- [ ] Describe key rate formula: key length / simulation time.

### §3 Methodology — Network / Multi-User Analysis (currently: stub)
- [ ] Describe topology generator: random user placement on A×A km grid, k-means relay placement.
- [ ] **Justify k-means relay placement**: argue from grid-search results already in `relay_placement.py` outputs; centroid ≈ optimal for single relay, k-means generalises this.
- [ ] **Justify multi-seeding**: state seed count, explain why averaging over random topologies gives more representative results than a single fixed topology.
- [ ] Describe BB84 mesh, MDI, TBB84 network simulators: what each computes, how pairs are aggregated.
- [ ] Describe cross-relay routing model and key dilution for TBB84.

### §4 Results (currently: "bunch of graphs...")
- [ ] **P2P performance**: present layers figure + selected parameter sweeps; refer to parameter impact table.
- [ ] **Network key rate vs relay count** and **vs user count**: present relay_sweep and user_sweep figures.
- [ ] **Network key rate gap**: explain MDI ~10× vs BB84 (supported by experiment or cited causes).
- [ ] **Cost results**: cost vs N, cost-efficiency vs N for SPAD and SNSPD configurations.
- [ ] **Cost vs rate optimisation plot**: for each protocol; read off deployment recommendations at given budget or rate requirement.
- [ ] **Parameter impact summary table**: one row per physical parameter (fibre loss, detector efficiency, dark count rate, node loss, init loss, source error, dephasing, basis bias, BS efficiency, Charlie position); columns = BB84 and MDI key rate reduction (% or ×) across the realistic operating range. Replaces or supplements 10 individual compare figures. (ROADMAP Project Report)
- [ ] **Deployment Recommendations subsection** (§4 already has a skeleton): populate with actual cost-rate optimisation results; frame using security level argument (when MDI is worth the rate penalty).

### §5 Discussion (currently: "Discuss results?")
- [ ] Critical analysis: MDI rate penalty vs security gain — where is the cross-over point?
- [ ] Cost model limitations: CapEx only, Euclidean distances, QD cost unverified, no OpEx for cryo systems.
- [ ] Note simulation–cost decoupling (cost_analysis.tex Inconsistency I): adding components raises cost but doesn't degrade simulated rate; discuss implications for interpretation.
- [ ] Note TBB84 trust assumption vs MDI: relay node compromise vs detector side-channel attacks.
- [ ] Energetic footprint: cite `\cite{Yehia_2025}`; note cryogenic OpEx for SNSPD and QD is unmodelled.

### §6 Conclusion (currently: skeleton notes)
- [ ] Past work summary: what simulation infrastructure was built (10-layer model, network simulators, cost model, DB).
- [ ] Present findings: key rate gap quantified; cost model shows MDI has lower component cost but higher per-bit cost; cost-rate optimisation reveals deployment-optimal configurations.
- [ ] Future work: finite-key corrections, WCP/decoy-state source model, ILP relay placement, WDM multi-user MDI, traffic-aware relay count optimisation (queueing model), TF-QKD extension.

### §2 Background — minor fixes
- [ ] Line 104 comment `% make a brief appendix entry showing this? incorp hong-ou-mandel?` — decide: add brief HOM explanation in background or appendix; cite `\cite{Hong_1987}` (already in bib).
- [ ] Check Table 2 (bit-flip rules): confirm correctness against Lo 2012 and cite.
- [ ] Abstract: "up to 10 times" — confirm this is supported by actual results before submission.

---

## 6. Referencing

### Missing citations needed in dissertation
- [ ] Citation for QD photon source cost (£150k): `\cite{QuandelaSPS}` already in bib — use it or find alternative with price data.
- [ ] Citation for InGaAs SPAD specs (η, dark count rate, cost per unit): likely ID Quantique or Excelitas datasheets; add to bib.
- [ ] Citation for SNSPD specs (η, dark count rate, cost per unit): likely Single Quantum, Photon Spot, or NIST publications; add to bib.
- [ ] Citation for dark fibre installation cost per km (UK context): Ofcom or BT Openreach infrastructure reports.
- [ ] Citation for EOM insertion loss range (0.5–3 dB): standard photonics reference.
- [ ] Citation for 11% QBER threshold: already `\cite{Shor_2000}` — ensure it is cited in the methodology where the cutoff is stated.

### Citations to verify compile correctly
All of the following are in `bibliography.bib` but confirm they appear in the compiled `.bbl` with no warning:
- [ ] `\cite{Dynes_2019}` — Cambridge quantum network
- [ ] `\cite{Yan2025}` — MDI-QKD with frequency comb
- [ ] `\cite{Yehia_2022}` — Quantum City simulation
- [ ] `\cite{Yehia_2025}` — energetic analysis
- [ ] `\cite{DBLP:conf/ondm/KaraviasHBLP25}` — comparative cost analysis ONDM 2025
- [ ] `\cite{Berrevoets_2022}` — deployed MDI-QKD
- [ ] `\cite{Martins2024}` — MadQCI heterogeneous network
- [ ] `\cite{eu_open_qkd}` — OpenQKD project

### Bibliography hygiene
- [ ] `\cite{PNS_desc}` currently points to EITCA (non-peer-reviewed); consider replacing with `\cite{Brassard_2000}` or `\cite{Chen2022}` for a more citable source.
- [ ] Check all `author = {... and others}` entries — some journals require full author lists; verify if UCL submission requires it.

---

## 7. Assumptions & Justifications Required

Every item below is an assumption baked into the simulation or cost model that must be **explicitly stated and justified** in the dissertation (methodology or limitations). The justification approach is noted alongside each.

### Simulation / Protocol Assumptions

- [ ] **QBER cutoff at 11%**: state the threshold and cite Shor–Preskill `\cite{Shor_2000}`. Note that 11% is the security proof threshold for the BB84 protocol under individual attacks; the same threshold is applied to MDI as a conservative bound.
- [ ] **Asymptotic key rate (no finite-key corrections)**: justify as standard for comparative simulation at this scale; cite or note that finite-key corrections become significant at short block lengths. State that this overestimates key rate at low photon counts. (ROADMAP lists finite-key as a future extension.)
- [ ] **Ideal single-photon sources (not WCP/decoy)**: all simulations use ideal SPS. Justify that this gives a clean upper-bound comparison between protocols. Note that WCP sources with decoy states are the practical standard; the decoy-state technique `\cite{Lo_decoys}` tightens the single-photon bound for WCP, but is not modelled here.
- [ ] **`source_error_rate = 0.005` (0.5% multi-photon / emission error)**: not derived from a specific QD device. State the assumed value and note it is plausible for a high-quality QD (cite `\cite{Bozzio_2022}` or `\cite{Yang_2024}`). Acknowledge it is not propagated from a source-technology model.
- [ ] **`node_loss_db = 2.0 dB`**: described as "FC/PC connectors + optical components at receiver". Justify the value or acknowledge it is a lumped approximation. Note it does not break out individual EOM/PBS/switch losses. (cost_analysis.tex Inconsistency I)
- [ ] **`init_loss = 0.15` (15% TX coupling loss)**: source-to-fibre coupling at Alice. Justify or cite a typical value for fibre-pigtailed QD sources.
- [ ] **`dephasing_rate = 0.0001`**: per-km fibre dephasing. State this is a conservative value; cite or justify.
- [ ] **`bs_eff = 0.97` (BSM beam splitter efficiency)**: 3% excess loss at the HOM BS. Plausible for a high-quality fibre coupler; cite or justify.
- [ ] **Linear-optical BSM discriminates only ψ⁺ and ψ⁻**: inherent to any linear-optical implementation `\cite{Lo_2012}`. State that this halves the effective BSM success rate (50% of valid coincidences are kept). This is already in the background section but should be referenced again in methodology.
- [ ] **`dark_count_rate = 100 cps` default**: SNSPD-tier; does not match InGaAs SPAD when `--detector-tech SPAD` is used. Note the inconsistency; plan to fix (see §1 Code Bugs). In the dissertation, state that all results use the default 100 cps unless otherwise specified.
- [ ] **Euclidean (flat-grid) topology**: all node positions on a flat A×A km grid with straight-line distances. Justify as appropriate for a comparative study at metropolitan scale where topology geometry is varied across seeds rather than fixed to a real city. Note no tortuosity factor; real fibre follows duct paths with typical tortuosity 1.2–1.5×.

### Network Modelling Assumptions

- [ ] **k-means relay placement**: relays placed at k-means centroids of user clusters. Justify: show or cite that centroid placement ≈ optimal for K=1 (from `relay_placement.py` results); argue k-means generalises this to K>1. Note that ILP-optimal placement is not computed (leave as future work).
- [ ] **Multi-seeding (seed count justification)**: state number of seeds used; justify that averaging over N random user placements gives representative results that are not artefacts of a single topology. Discuss choice of seed count (diminishing returns argument or variance plot).
- [ ] **TBB84 backbone: 1 source per relay (not K−1)**: relay backbone uses one QD source per relay node for relay-to-relay BB84. Strict bidirectional full-mesh backbone would require K−1 sources per relay (K(K−1) total). State simplification and bound the error: for K≤8 the undercount is ≤7× on backbone source cost. (cost_analysis.tex §9.6)
- [ ] **TBB84 backbone: unidirectional links (K(K−1)/2 sessions)**: simulated as half-duplex shared key per relay pair. Full duplex (separate key per direction) would double backbone rate and source count. State and justify or flag as a limitation. (cost_analysis.tex Inconsistency VII)
- [ ] **TBB84 classical XOR forwarding is secure**: the relayed message K_AR1 ⊕ K_R1R2 is a one-time pad; in-flight interception reveals nothing. State clearly that the trust assumption is on the relay *node* (physical security), not the classical link. (already discussed in cost_analysis.tex §4.3)
- [ ] **Monte Carlo run count choice**: state how many runtimes per point are used and why. For low key rates, more samples reduce variance; audit whether the chosen count is adequate. (ROADMAP Analysis)

### Cost Model Assumptions

- [ ] **CapEx only, no OpEx**: cryogenic systems (SNSPD at ~2 K, QD at ~4 K) have cooling costs that can rival hardware CapEx over a 10-year lifetime. State this is not modelled; cite `\cite{Yehia_2025}` as the only energetic analysis in the QKD context.
- [ ] **Classical communications free**: synchronisation, basis reconciliation, error correction, privacy amplification, and key forwarding are not costed. Standard assumption in early-stage techno-economic QKD analysis; state explicitly. (cost_analysis.tex §9.1)
- [ ] **BB84 mesh: one dark fibre per user pair**: N(N−1)/2 individual dark fibre runs. Correct for passive dark-fibre mesh; unrealistic at large N where WDM or switched architecture would be used. State this makes BB84 costs appear very large at high N, which is physically meaningful (mesh BB84 doesn't scale) but should not be interpreted as a realistic deployment estimate at N>8. (cost_analysis.tex §9.3)
- [ ] **SPD cost linear in η**: two-point linear model anchored at SPAD (η=0.20, £15k) and SNSPD (η=0.85, £100k). State that this is a modelling simplification; in reality cost is not strictly linear and dark count rate (a second major parameter) is not captured. Justify as sufficient for comparative analysis given the technology class is swept in discrete steps. (cost_analysis.tex §3)
- [ ] **QD source at £150,000**: reflects QD SPS + cryostat cost amortised per channel. State this is an estimate requiring verification; use `--source-cost` to override when revised figures are available.
- [ ] **TX coupling loss (`init_loss = 0.15`) has no cost entry**: coupling hardware (collimator, circulator) is ~£100–500, negligible vs £150k source. State explicitly that it is omitted as negligible. (cost_analysis.tex Inconsistency VI)
- [ ] **Optical switch at MDI relay: cost charged per relay, loss only for cross-cluster pairs**: the switch must be installed at every relay unconditionally; its insertion loss only applies when routing cross-cluster photons. State this asymmetry; note that networks with high K have a larger switch cost fraction relative to switch-induced rate penalty. (cost_analysis.tex Inconsistency V)
- [ ] **Cost and simulation models are not tightly coupled**: adding components to the cost model raises cost but does not change simulated key rate (node_loss_db is fixed). State this explicitly in the cost methodology section; note that the correct approach is to update both cost model and `node_loss_db` when refining component budgets. (cost_analysis.tex §9.4)

---

## 8. Miscellaneous

- [ ] **Word/page count**: check dissertation is within UCL MSc Quantum Technologies project report page limit.
- [ ] **Figure captions**: all figures need captions that are self-contained (readable without surrounding text).
- [ ] **Figure references**: every figure must be referenced in the text with `Figure~\ref{fig:...}`; check none are orphaned.
- [ ] **Spell check**: run `aspell` or equivalent on dissertation.tex; enforce British English throughout (`\cite{}` keys and code names exempt).
- [ ] **Compile clean**: ensure `dissertation.tex` compiles with zero warnings on two-pass `pdflatex` + `bibtex` run before submission.
- [ ] **Case study** (`docs/case-study-tex/case-study.tex`): confirm whether this is submitted alongside the main dissertation or is separate; if submitted, apply same checks.
