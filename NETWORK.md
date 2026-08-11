# Network Modelling Plan

## Goal

Compare BB84 and MDI-QKD on key rate, cost, and scalability across multi-user network topologies. Identify conditions under which each protocol is preferable.

## Network Model

**Application layer:** All users form a fully connected graph — every user can request a key with any other. User positions are randomised in geographic space. The same positions are used for both protocols in any given simulation instance.

**Transport layer:** MDI-QKD uses K Charlie nodes (BSM only, untrusted). BB84 uses no relay nodes — instead each user pair is connected by a direct P2P fibre link (fully connected mesh, N(N-1)/2 links total). Relay nodes introduce unnecessary trust assumptions for BB84 and are not deployed in practice when direct links are available.

**Cross-cluster routing (MDI):** When two users are homed to different Charlie nodes (C1, C2), C2 acts as a passive optical router — redirecting the photon toward C1 without measuring it (fibre switch / optical circulator). Quantum state is preserved. Extra cost: C2→C1 fibre loss plus switch insertion loss, configurable via `switch_loss_db` (default 0.0 dB — abstracted away rather than modelled/swept; see dissertation Simulation Model Limitations, "Metropolitan network scope"). Bob's effective link length includes the relay-relay hop; dephasing accumulates over the full path. Timing compensation is absorbed into the simulation's channel delay model.

## Experiments

**Experiment 1 — Relay count sweep (fixed N users, vary K relays)**
Relay infrastructure is redesigned from scratch at each K (greenfield): cluster assignment is k-means-seeded, then relay position is refined by the generalised (multi-facility) Weiszfeld iteration, which minimises total fibre length — spoke plus backbone, the network's actual linear-cost objective — rather than the sum-of-squared distances a plain k-means centroid minimises (see dissertation §Relay Placement, Appendix Relay Placement Optimisation). Measures how key rate evolves as relay infrastructure is added. The K at which performance plateaus/peaks becomes the fixed relay count for Experiment 2.

**Experiment 2 — User count sweep (fixed K relays, vary N users)**
Provider-growth model: users are drawn incrementally from a single RNG stream (so $N \to N+1$ means genuinely *adding* a user, not redrawing an unrelated sample); relay position is placed once, for the $N_\text{min}$-user network, by the strategy under test (centroid/boundary/Weiszfeld) and then held fixed as $N$ grows — modelling a provider that sizes relay infrastructure once and serves subsequent organic growth without continuously re-optimising it. Measures how each protocol degrades as user load grows under infrastructure sized for an earlier, smaller network. Primary scalability comparison.

Both experiments aggregate statistics across many random user placements of the same network size N to yield results representative of an average randomised N-user metropolitan network.

## Scheduling

All N(N-1)/2 user pairs are simulated for each network instance. This is equivalent to uniform-random pair selection (Poisson process, uniform pair weights) for the primary metric of average key rate per pair. Results are aggregated over multiple random user placements (seeds) per network size to yield statistics representative of an average metropolitan network.

A Poisson event scheduler (pair selection with user availability pool) is deferred — it is relevant for network throughput and contention modelling but does not affect average key rate comparison.

## Metrics

| Metric | Role |
|--------|------|
| Average key rate per keygen event | Primary — summative, highlights general trend |
| Network success rate (fraction of events with QBER < 11%) | Primary — captures reliability at network level |
| Minimum key rate across events | Secondary |
| Total network throughput | Secondary |

Extension: compare success rate for same-relay pairs vs cross-relay pairs to quantify the cost of passive routing.

## Cost Model

Cost is not tracked in simulation code — no £/cost-unit columns, no `network/cost.py`, no cost sweep scripts. It is modelled purely analytically in the dissertation instead: total CapEx is expressed symbolically as component counts (source/detector/fibre-length terms, determined by topology) times free per-unit-price parameters $c_s$, $c_d$, $c_f$, since manufacturer prices for QD sources and SNSPD detectors are not publicly available. The structural result — BB84 fibre cost scales $\mathcal{O}(N^2)$ (one link per user pair) vs MDI's $\mathcal{O}(N)$ (per-user spoke + $K(K-1)/2$ backbone) — is independent of absolute prices and yields an analytically-derived crossover user count $N^*$ as a function of the ratio $c_d/c_f$, relay count $K$, and network geometry.

`total_fibre_km` (and, from the relay-count sweep, per-seed spoke/backbone lengths) is tracked per simulation and stored in `network_results` — this is the empirical geometric input the symbolic cost formulae are evaluated against; it is not itself a cost figure.

Relay count comparison (cost vs performance) is a secondary analysis. Primary focus is user scaling. Note: the relay-count sweep on the current model shows the fibre-cost-optimal $K$ and the key-rate-optimal $K$ are *not* the same operating point (dissertation §Network Performance) — worth keeping in mind before treating "relay count that minimises cost" and "relay count that maximises rate" as interchangeable in any downstream cost-efficiency analysis here.

## Infrastructure Comparison

| | BB84 | MDI-QKD | Trusted-node BB84 |
|---|---|---|---|
| Fibre links | N(N-1)/2 direct P2P links | N user-relay + K(K-1)/2 relay-relay links | N user-relay + K(K-1)/2 relay-relay links |
| Relay hardware | none | K Charlie nodes (untrusted) | K trusted relay nodes |
| Security assumptions | none beyond endpoints | relay untrusted — MDI advantage | relay **trusted** — holds plaintext key material |
| Infrastructure scaling | O(N²) | O(N) | O(N) |
| Key rate bottleneck | direct link | BSM success rate + routing | min link in chain; backbone shared across cross-relay pairs |

BB84's O(N²) fibre scaling makes it prohibitively expensive at large N even if per-pair key rate is higher. MDI's O(N) fibre scaling is the primary economic argument for network deployment. Trusted-node BB84 shares the same O(N) infrastructure as MDI but requires relays to be security-trusted, sacrificing the key advantage of MDI — the comparison isolates the cost of the trust-removal guarantee.

## Working Hypotheses

- MDI infrastructure scales better: BB84 requires N(N-1)/2 fibre links; MDI requires ~N links to K relays. At large N, MDI fibre cost grows far more slowly.
- MDI key rate per pair degrades more slowly with N: detector count is fixed at Charlie nodes regardless of user count; BB84 per-pair rate is unaffected by N (direct links) but total fibre cost is not.
- A crossover user count exists beyond which MDI total infrastructure cost is lower than BB84, despite potentially lower per-pair key rate.

## Extensions (nice to have)

- WDM multi-user MDI: multiple user pairs on separate wavelengths, simultaneous BSM at shared Charlie. Extra cost: MUX/DEMUX insertion loss (~1–3 dB per device). Requires T1/T2 quantum memory decoherence model — photons from different wavelength channels must be stored at Charlie until all channels are ready for BSM; coherence time during that wait is the fundamental scalability limit.
- Key rate vs memory coherence time (T2 sweep) for WDM relay nodes.
- Entanglement swapping at relay nodes: MDI-QKD without trusted relay requirement at backbone. Needs quantum memory and additional BSM node between Charlies. More complex than passive optical routing but preserves MDI security end-to-end.
- Long-distance repeater chain: N-hop linear topology for range extension beyond metropolitan scale. Separate from metro network model. Most prior repeater research covers this regime.
- Key rate vs number of repeater hops (sweep) for long-distance chain.
- BB84 vs MDI-QKD repeater chain performance head-to-head.
- Fully connected BB84 (direct pairwise links, no relay) as additional baseline.
- Relay count as secondary analysis axis: key rate per unit cost vs K at fixed N.
- Relay placement sensitivity: random vs optimal placement comparison.
- Cross-relay vs same-relay pair success rate comparison.
- Untrusted BB84 relay model (removes the security-model equivalence assumption).
