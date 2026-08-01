# Scaling Strategies: Classical Network Simulation → NetSquid

Five levers classical network simulation used to break its own scale ceiling, mapped to NetSquid. Four are inherited; one (state compression) is quantum-native. You tested two (surrogates, adaptive sampling).

The key axis for each: **what cost does it actually attack?** Two strategies can both "trade fidelity for tractability" while attacking completely different bottlenecks — conflating them will not survive questions from the CQT audience.

---

## 1. Parallel DES (PDES)
**Attacks:** wall-clock time via parallelism.

### Classical
Partition the simulation across logical processes (LPs) on separate cores/nodes.

- **Conservative (Chandy–Misra–Bryant):** LP advances only when lookahead on message latency proves no earlier event can arrive. Safe, but stalls badly when lookahead is small relative to event density.
- **Optimistic (Time Warp / Jefferson):** Speculative execution; roll back with anti-messages on causality violation, coordinated by global virtual time. Enables massive scale — ROSS-based simulators run flit-level HPC network models across hundreds of thousands of cores.
- **Hybrid:** Switch between families at runtime based on observed rollback rate.

### Quantum analogue
Embarrassingly-parallel Monte Carlo over independent noise realisations. This ports cleanly — different seeds/pairs never share state.

**The quantum caveat (important for questions):** Classical LPs are loosely coupled — a packet is self-contained state. Entanglement is not. A Bell pair straddling a partition boundary means the reduced state on either side is only well-defined jointly. Conservative lookahead has nothing clean to bound; Time Warp rollback would need to undo a *shared* density matrix. Event-loop parallelism does not port. Only the MC-over-realisations layer does.

**Pro:** Horizontal scaling; zero fidelity cost for MC.  
**Con:** Entanglement coupling makes event-loop partitioning ill-defined — only embarrassingly-parallel MC ports.

---

## 2. Fluid / Flow-Level Abstraction
**Attacks:** event count — the number of events the scheduler must process.

### Classical
Replace per-packet events with continuous flow-rate ODEs or flow-level rate variables. Ten thousand packet events collapse into a handful of rate-change events. Per-event cost is essentially unchanged; the win is entirely in event count. Estimation error is typically small.

### Quantum analogue
Replace per-attempt simulation of probabilistic heralded entanglement generation with analytic or sampled waiting-time descriptions. Instead of stepping through 10⁴ failed heralding attempts, draw once from the waiting-time distribution.

Key references:
- **Shchukin, Schmidt & van Loock (PRA 100, 032322, 2019):** Exact Markov-chain for average waiting time and transmission rate in repeater chains.
- **Brand, Coopmans & Wehner:** Efficient algorithms for generation time and fidelity of first end-to-end pair; polynomial runtime vs exponential for earlier methods.
- **Generating-function work on swap-ASAP chains:** Exact analytic fidelity moments up to 25 segments — optimise cutoffs without Monte Carlo at all. That last phrase is the cleanest statement of the analogy.

**Caveat:** Naive Markov-chain transition matrix grows exponentially with node count — the abstraction has its own wall, which is why the efficient-algorithm and generating-function literature exists.

**Pro:** Event count collapses; large speedup.  
**Con:** Analytic models limited to specific topologies/protocols; exponential matrix at scale.

---

## 3. State-Space Compression *(no classical twin)*
**Attacks:** per-event cost — the cost of each individual event. Event count in the scheduler is completely unchanged.

### Why no classical twin
Classical packet state does not grow exponentially with interaction history, so there was never pressure to develop compressed per-event state representations. This bottleneck is native to the quantum problem.

### Quantum techniques
- **Hilbert truncation:** Truncate high-occupation Fock states. Exact for low-photon-number regimes.
- **Stabiliser / Clifford restriction (Gottesman-Knill):** Exponential Hilbert space → polynomial classical simulation. Exact for Clifford circuits; completely breaks for non-Clifford gates.
- **Matrix-product state (MPS):** Cap entanglement rank. Exact for low-entanglement states; approximation degrades as entanglement grows.

Each is exact within a restricted class and degrades outside it.

**Rhetorical use:** This is the one row of the table where the quantum problem is genuinely native rather than inherited — a strength for the talk rather than a gap.

**Pro:** Cheaper per event; zero approximation within class; no event-count overhead.  
**Con:** Restricted class only; high-entanglement or non-Clifford protocols fall outside.

---

## 4. Learned Surrogates *(tested)*
**Attacks:** both event count and per-event cost — replaces simulation wholesale.

### Classical: MimicNet (Zhang et al., SIGCOMM 2021)
Simulate one observable cluster at full packet-level fidelity in OMNeT++; train LSTMs to approximate all others. Up to 675× speedup for 128-cluster data centre; FCT, throughput, RTT within 5% of ground truth. Assumes FatTree topology and proportionally-scaling traffic patterns. Successors: m4, DeepQueueNet, RouteNet-Fermi (GNNs, direct queuing/congestion estimation).

### Quantum analogue
Train on the simulable regime (≤30 nodes on a modern machine in a reasonable timeframe), using topology and noise parameters as inputs and secret key rate / fidelity as targets. GP or GNN extrapolates beyond the wall. The premise transfers exactly: simulate what is tractable, learn what is not.

**Your results:** ~10⁶× speedup demonstrated; uncertainty quantification free (GP posterior gives confidence intervals at no extra cost).

**Pro:** Most scalable direction; ~10⁶× speedup; UQ free with GP.  
**Con:** Requires training data from simulable regime; empirical validity outside training distribution must be validated; topology/protocol class constraint analogous to MimicNet's FatTree assumption.

---

## 5. Engine-Level Optimisation
**Attacks:** constant-factor scheduler overhead. Zero fidelity cost.

### Classical
Better future-event-list data structures: calendar queues, ladder queues — reduce scheduling overhead per event. Memoisation and fast-forwarding: recognise when a chunk of simulation state has already been computed and skip recomputation. Explicitly orthogonal to and combinable with all other levers.

### Quantum analogue
Exploit repeated topological structure in `pydynaa`. Identical repeater segments and symmetric branches are recomputed redundantly — caching these is a currently underused lever. Unlike all other levers, this introduces zero approximation error. Natural first thing to try before accepting any fidelity cost.

**Pro:** Zero fidelity cost; combinable with all other levers; rhetorical setup for why other levers cost something.  
**Con:** Limited gains; only effective where topology has repeated structure.

---

## 6. Adaptive Sampling *(tested, quantum-native)*
**Attacks:** wasted Monte Carlo budget in clearly-passing or clearly-failing regimes.

No classical network simulation equivalent. Arises from the specific structure of QKD: QBER has a cutoff beyond which key rate → 0. Budget spent in the stable regime or far beyond the cutoff is wasted.

Concentrate MC budget near the QBER cutoff; exit early when σ/μ < threshold in the stable regime (batches of 100; stop when σ/μ < 10%).

**Your results:**
- BB84: 30% wall-clock saving vs fixed-1000 baseline.
- MDI-QKD: No gain — η_d² variance means even stable-regime estimates are noisy; multiprocessing spawn overhead eats any saving from fewer runs.

**Pro:** 30% wall-clock saving for BB84; zero fidelity cost.  
**Con:** Blocked by spawn overhead for MDI; protocol-dependent — not a universal fix.

---

## Summary Table

| Strategy | Attacks | Classical origin | Fidelity cost | Tested |
|---|---|---|---|---|
| PDES | Wall-clock | Direct (MC layer only; event-loop doesn't port) | None | No |
| Fluid/flow | Event count | Direct | Small, controllable | No |
| State compression | Per-event cost | **None — quantum-native** | Exact within class | No |
| Surrogates | Both | Direct (MimicNet, RouteNet-Fermi) | Empirical | Yes |
| Engine optimisation | Constant overhead | Direct | None | No |
| Adaptive sampling | Wasted MC budget | **None — quantum-native** | None | Yes |

---

## Anticipated questions

**"Doesn't PDES apply directly — you just run multiple seeds in parallel?"**  
Yes, and you already do. The question is whether the *event loop itself* can be parallelised across a single trial. That requires partitioning shared state, which entanglement prevents.

**"Couldn't you use Time Warp if you restrict to separable states?"**  
Possibly, for specific subprotocols. Open research question — good slide-closer.

**"What about GPU acceleration?"**  
Attacks per-event cost, similar axis to state compression. NetSquid's Cython layer doesn't trivially GPU-port. Related to why you have a GPU directions slide.
