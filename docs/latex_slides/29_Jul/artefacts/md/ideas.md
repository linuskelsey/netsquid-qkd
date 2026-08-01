# Ideas

---

## GPU acceleration via linear algebra reformulation

**Idea:** NetSquid's event loop is inherently sequential and has no GPU backend. However, if the simulation could be reformulated as a linear algebra problem, GPU acceleration becomes viable — large batched matrix operations are exactly where GPUs excel.

**Sketch:** QKD key rate is ultimately a function of transmission probabilities and error rates, which derive from products of transfer matrices (loss, noise, detection). A full parameter sweep over N points is N independent evaluations of the same functional form — this is embarrassingly parallel and maps naturally to batched matrix-vector products on GPU.

**What this would require:**
- Express the per-pair simulation as a closed-form matrix expression (or tensor contraction) rather than an event-driven process
- Sacrifice generality for structure — works for the fixed protocol/noise-model case, not arbitrary NetSquid protocols
- Essentially: derive the analytical form NetSquid is approximating via MC, implement it as a vectorised GPU kernel

**Why it's non-trivial:**
- NetSquid's power is handling *arbitrary* protocols where no closed form exists
- For BB84/MDI the analytical form is known (PLOB-adjacent expressions), so the reformulation may be tractable for this specific case
- Heralding, coincidence detection, and multi-round protocols introduce conditional branching that resists pure linear algebra treatment

**Relation to surrogate modelling:** a linear algebra reformulation would be exact (not an approximation), unlike a GP surrogate. But it requires deriving the math; surrogates work without it.

**To explore:** whether the layered noise model (layers 0–9) can be expressed as a product of transfer matrices, one per layer, applied to an initial state vector.

---

## Graph matrix / transfer matrix formulation of network key rates

**Idea:** express the network as a weighted graph where matrix elements encode device parameters, then compute key rates for all pairs as matrix operations — GPU-parallelisable by construction.

**Structure:**

- Weight matrix $A$ where $A_{ij}$ = transmission efficiency of link $(i,j)$, encoding $\alpha$, $L_{ij}$, $\eta_d$, insertion loss, connector loss, etc.
- **BB84 full mesh:** $K_{ij} = f(A_{ij})$ — key rate is a direct function of each edge weight. All pairs computed simultaneously as elementwise matrix ops.
- **MDI star-mesh:** $K_{ij} = f(A_{i,r} \cdot A_{j,r})$ where $r$ is the relay node for the pair. Product of two edge weights — still a matrix operation over all pairs at once.
- **Parameter sweep:** update entries of $A$ (change $\alpha$, $\eta_d$, etc.), recompute $K$. No re-simulation — just matrix arithmetic.

**Why GPU works here:** batched elementwise operations on $N \times N$ matrices are exactly what GPU tensor cores are designed for. At $N=100$: 10,000 pair evaluations in a single kernel launch.

**Key condition:** the protocol must have a closed analytical rate expression. BB84 and MDI both do (same functional forms used to compute PLOB comparisons). The 10-layer noise model adds multiplicative correction factors to each $A_{ij}$ entry — doesn't change matrix structure.

**Where it breaks down:** quantum memory, entanglement swapping chains, purification rounds — conditional branching and sequential heralding that can't be flattened into matrix products without approximation. Full DES still needed for these.

**Relation to other approaches:**
- vs. NetSquid MC: this is exact (not stochastic), but assumes the analytical form is derivable — loses protocol generality
- vs. GP surrogate: exact not approximate, but requires deriving the math; surrogates work without it
- vs. PDES: avoids the synchronisation problem entirely by removing the event loop — trades generality for speed
