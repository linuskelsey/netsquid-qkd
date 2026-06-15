# Implementing Network Analysis

### What is guiding me?
Ultimately, what I want is to characterise and compare how both BB84 and MDI performance metrics (key rate) vary across topologies. I want to identify the application layer topologies that are preferential toward one protocol or another as regards key rate, cost and scalability.

### What do I need to get there?
Working backwards, I need simulated key rates for a swept number of users in a variety of user topologies. Therefore I must have NetSquid simulators built for both BB84 and MDI, in each user topology, that take in a parameter of user count, generate a network model and simulate key generation across the network, extracting rates from all pairs.

However, it is not just the application layer that determines the key rate. It is clear that having different relay networks for MDI would have a stark impact on network key rate. So this is something I also need to investigate. Furthermore, more relays = more cost, and so this is a crucial business decision for customers wishing to deploy MDI-QKD networks.

---

## Open Questions

**Q1 — Security model**
MDI-QKD's defining property is that the relay (Charlie) is untrusted — measurement-device-independent. BB84 through a relay node requires that relay to be trusted (it sees key material). Is preserving this security distinction part of what you want to compare, or are you treating both protocols as equivalent in terms of trust assumptions for the purpose of this analysis?

**A1** - I think it is easiest for us to assume trusted nodes for BB84 for the time being. Anything beyond that is absolutely a nice to have.

**Q2 — BB84 network baseline**
Given the same physical fiber infrastructure (same nodes, same links), what does BB84 look like? Options:
- Direct pairwise links between every user (no relay, N(N-1)/2 fibers)?
- BB84 through trusted intermediate nodes (same relay positions as MDI Charlies, but trusted)?
Which is the fair comparison?

**A2** - I think let's do it with trusted relay nodes for the time being, with placement mirroring that of MDI. This makes it most explicitly a fair comparison. It is a nice to have to investigate what a fair comparison might look like were we to model pairwise links between communicating nodes, or even to add in pairwise links (fully connected) as a comparison. Perhaps - we can use fully connected BB84 as a sort of baseline for all our comparisons. Worth considering.

**Q3 — Topology definition**
What does "variety of topologies" mean concretely? Options:
- Fixed graph structures: star, tree, ring, mesh — enumerate a small set and compare?
- Geographic: users placed in space, relays positioned by some rule (e.g. optimal, grid, random)?
Which approach, and which specific topologies?

**A3** - I am starting to lean toward not caring about the user graph structure. I think from a user perspective it should really always be a fully connected graph to ensure maximal communication capabilities. What I am interested in is the effect of relay placement in the transport/physical layer. Therefore users can be placed randomly in space but equivalently for both protocols. Then we vary the number of relays (optimising placement based on least-squares or similar simple regression, minimising total distance to nearest relay) and investigate effects on key rate for both as we add more. But that is considering a fixed user count. If instead we had a fixed transport layer, and a fixed number of relays, we could then start to consider scalability and the effects of increasing our user counts to see when relays are overwhelmed in each protocol and which protocol reacts more kindly to increasing user count.

**Q4 — Relay placement strategy**
For MDI, if you vary relay count, how are relays placed? Options:
- Fixed positions (e.g. evenly spaced, grid)?
- Optimal placement (minimise average user-to-relay distance)?
- Random (averaged over many placements)?

**A4** - Discussed in A3, I believe in full. Optimal for fixed user count portions and fixed for variable user count portions.

**Q5 — Network key rate metric**
How do you reduce per-pair key rates to a single network-level metric? Options:
- Average key rate per user pair?
- Minimum key rate (worst-case pair)?
- Total throughput (sum over all pairs)?
Which is your primary metric, and why?

**A5** I am imagining average key rate across all attempts at generating a key. We will also need to measure the success rate of key generation (i.e. rate at which QBER < 11%). Minimum and Total are also useful metrics. I want to track all but primary I think should be average key rate per key. Mostly because it is a good summative statistic and highlights general trend well.

**Q6 — User pairing / multiplexing**
In a multi-user MDI network, which pairs communicate through which Charlie, and how? Options:
- All-to-all (every user pair communicates)?
- Time-multiplexed (pairs take turns at Charlie)?
- WDM (each pair on a separate wavelength, simultaneous)?

**A6** - Okay. This is a little complex. Let's say we have two communicating parties, say A1 and B2, connected to different relay nodes. They send their photons to their connected nodes, say C1 and C2. Then C2 will need to forward its received photons to C1 (or vice versa), who performs the BSM and returns the measurement data back along to B2 via C2. As such, the relay node graph is almost contracted onto the relay node in the P2P model. I want all users to be able to communicate, and for key requests to be random along some simulation period (ensuring no user is involved in 2 key generation events simultaneously). WDM should be possible, but I think for now it is nice to have.

**Q7 — Cost model**
What counts as "cost"? Options:
- Number of relay (Charlie) nodes?
- Total fiber length deployed?
- Both (weighted sum)?
What is the cost-efficiency metric — key rate per relay node? Key rate per km of fiber?

**A7** - My plan is to assign arbitrary cost markers to each piece of hardware (on the assumption that the protocols are using equivalent hardware aside from protocol-specific tech). Then for a given network simulation, the network generated will have an attached cost in terms of the arbitrary costs, and we will be able to perform some sort of estimations to lower and upper bound each one using industry standard costs.

**Q8 — Scientific claims**
What specific hypotheses is this analysis testing? E.g.:
- "MDI-QKD achieves higher per-pair key rate than BB84 beyond N users in topology X"
- "Clustered relay topology outperforms star topology for MDI beyond N users"
Writing the claims first will sharpen the experimental design.

**A8** The claims I am as yet unsure on. This is more of a discovery piece but what my intuition tells me is that in identical network architectures, MDI will be cheaper to add nodes (a new BB84 node requires detector and source and MDI requires only source). Further, since detector efficiency seems to present a dominant reduction in key rate and increase in QBER, I believe that key rates for MDI will decrease less than for BB84 as more users are added (number of detectors stays constant for MDI). I don't know where the cross-over will be but there should be a user count past which MDI dominates BB84 wrt key rate. I expect other hypotheses to be illuminated in the course of investigations.

---

## Design Challenges & Resolutions

**C1 — Cross-cluster photon routing**
Cross-cluster user pairs (A1 on C1, B2 on C2) cannot have C2 measure and re-emit B2's photon — no-cloning. *Resolution:* C2 acts as a passive optical router (fiber switch / optical circulator), redirecting B2's photon to C1 without measuring it. Quantum state is preserved. Cost: extra fiber loss on the C2→C1 link plus switch insertion loss (~0.5–2 dB). Timing: B2 must emit earlier than A1 to compensate for extra travel time so both photons arrive at C1 simultaneously. BSM then proceeds normally at C1.

**C2 — Relay saturation / capacity**
Not in scope. Dropped.

**C3 — Concurrent user scheduling**
Key generation events are driven by a Poisson process. On each firing, two users are selected uniformly at random from the available pool. They are removed from the pool for the duration of their keygen event and re-added on completion. This ensures no user participates in two simultaneous key events. Scheduler is classical and sits outside the quantum simulation layer.

**C4 — Random placement reproducibility**
Same random user positions and same transport layer graph are used for both BB84 and MDI in each simulation instance. Aggregated over many simulation runs of the same network size N, this yields statistics for an "average randomised N-user metropolitan network." Results are comparable across protocols because the underlying network is identical.

**C5 — Detector count asymmetry in cost model**
Primary investigation is user count scaling with fixed relay infrastructure — relay count comparison is a nice-to-have. Cost model complexity (detector asymmetry between BB84 trusted-node and MDI Charlie) is deferred. When cost analysis is done, detector counts per node type must be made explicit.

**C6 — Two-experiment anchor**
Relay-count experiment (vary K, fixed N) runs first. The K at which key rate plateaus is used as the fixed relay count for the user-scaling experiment (vary N, fixed K). Ensures the two experiments are calibrated against each other.

**C7 — Per-pair QBER tracking**
Primary metric is cumulative network success rate (fraction of keygen events with QBER < 11%), reported at the network level. Per-pair tracking is deferred. Extension: compare success rate statistics for same-relay pairs vs cross-relay pairs to characterise the cost of passive routing.
