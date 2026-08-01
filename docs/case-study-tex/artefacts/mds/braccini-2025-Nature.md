**Nonclassicality of a Macroscopic Qubit-Ensemble via Parity Measurement Induced Disturbance** 

Lorenzo Braccini,<sup>1,</sup><sup>_∗_</sup> Debarshi Das,<sup>2, 1,</sup><sup>_†_</sup> Ben Zindorf,<sup>1</sup> Stephen D. Hogan,<sup>1</sup> John J. L. Morton,<sup>3, 4</sup> and Sougato Bose<sup>1</sup> 

> 1 _Department of Physics and Astronomy, University College London, Gower Street, London WC1E 6BT, England, United Kingdom_ 

> 2 _Department of Physics, Shiv Nadar Institution of Eminence, Gautam Buddha Nagar, Uttar Pradesh 201314, India_ 

> 3 _London Centre for Nanotechnology, University College London,_ 

_17-19 Gordon Street, London WCH1 0AH, England, United Kingdom_ 

> 4 _Department of Electronic & Electrical Engineering, University College London, London WC1E 7JE, England, United Kingdom_ 

We propose an experimental scheme to test the nonclassicality of a macroscopic ensemble of qubits, through the violation of the classical notion of macrorealism (MR) via the fundamental measurement-induced disturbance of quantum systems. An electromagnetic resonator is used to probe the parity of the qubit-ensemble. The action of sequential measurements allows the nonclassicality of whole ensemble to manifest itself, in the ideal case, irrespective of its size. This enables to probe the macroscopic limits of quantum mechanics as the qubit-ensemble is, effectively, a single large spin of many ℏ units. Even as ℏ _→_ 0 in comparison to the total angular momentum of the ensemble, a constant amount of violation of MR is found in the noiseless case. However, environmental decoherence and inhomogeneity of qubit-electromagnetic field couplings precipitate the quantum-to-classical transition. This implies that Bohr’s correspondence principle is not fundamental, but a consequence of practical limitations. We outline an implementation with a variety of qubits (superconducting qubits, spins in semiconductors, and Rydberg atoms) coupled to a coplanar waveguide resonator, and – via the corresponding noise analysis – find that violation of MR is detectable up to 100 qubits via current technology. 

### **I. INTRODUCTION** 

Probing the macroscopic limits of quantum mechanics, and thereof the boundary between quantum and classical physics, is one of the biggest open quests in modern science. Only persistent experimental efforts to observe genuine quantum mechanical phenomena in more and more macroscopic systems can address this issue. While spin is an important parameter to characterize the ‘macroscopicity’ of a system (i.e., an object with large spin can be considered as macroscopic), experiments to test the quantum nature of a large spin are still lacking. As opposed to other parameters, such as mass or spatial spread, spin is the only quantity directly comparable to the action in terms of ℏ, which has been historically used for explaining quantum-to-classical transition: ℏ _→_ 0 is traditionally believed to imply the classical limit of quantum mechanics. For example, a macroscopic magnet, which can be approximated as a collection of qubit spins, behaves, in general, as a large classical vector. Against this backdrop, we propose a realizable experiment to test the quantumness of a macroscopic ensemble of qubits, simulating a large spin. Specifically, our aim is to address the following: _When does a large ensemble of qubits, with a total spin of many units of_ ℏ _, stop behaving as a nonclassical entity?_ 

According to our protocol, in the ideal case, there is no such fundamental limit. However, experimental imperfections inevitably impose practical constraints on the ensemble size. Despite this, our proposed scheme can be implemented using different types of physical qubit-ensembles, and with current technology, it is capable of demonstrating nonclassicality with up to approximately 50 _−_ 100 qubits – equivalent to a spin of _∼_ 50ℏ _−_ 25ℏ. This opens a new avenue for testing 

genuine nonclassicality in large spin systems, extending into a macroscopic regime hitherto unexplored. Notably, this approach enables a simpler test of nonclassicality with spins of up to an order of magnitude greater than those of previous experiments, which had been limited to values below 10 [1–3]. 

As a tool for testing quantumness, we use the violation of the classical notion of macrorealism (MR) [4–6]. MR is the conjunction of the two assumptions: (1) _Realism per se:_ At any instant, even if unobserved, a system is definitely in one of its possible states with all its observable properties having definite values. (2) _Noninvasive measurability:_ It is possible to determine which of the states the system is in by ensuring the measurement induced disturbance is arbitrarily small, thus not affecting the state or the subsequent time evolution of the system [4]. Quantum systems violate these two assumptions due to the superposition principle and the measurement induced wavefunction collapse, respectively. From the above two assumptions, various necessary testable conditions of MR can be derived, for instance, the Leggett-Garg inequalities [4, 7] and the No Disturbance Condition (NDC)<sup>1</sup> [8–12], with the latter being used in this work. Experimental refutation of any of these conditions in a loophole-free way implies the inherent nonclassicality or quantumness of a measured system. 

Large qubit-ensembles have been established as reliable quantum resources for computing [13–17], sensing [18–20], memory [21–37], and communication [38–40]. Despite all these advances, its quantum property as a large collective spin remains unexplored, since usually these studies are limited to the low-excitation sector, where the system can be _approximated_ to a quantum harmonic oscillator (through the Holstein–Primakoff transformation [41]). On the other hand, experimental violation of MR has been reported earlier only for 

> _∗_ lorenzo.braccini.18@ucl.ac.uk 

> _†_ dasdebarshi90@gmail.com 

> 1 also known as the no signalling in time condition [8]. 

2 

single qubit or _microscopic_ spin systems [1, 2]. Although large spins have been considered in literature for probing quantumness [42–53], all these analyses are purely theoretical with no scope for near-term experimental realization. While quantum effects such as tunneling, squeezing, resonant transitions, coherence and precession have been experimentally observed in large-spin systems [3, 54–62], these demonstrations neither test the quantumness via violation of MR, nor can easily scale to macroscopic levels. 

Here, we close the gap between the current experiments involving qubit-ensembles – which have had mainly practical applications – and the above foundational questions of quantum mechanics of large spins – which, until now, have been lacking any realisable experimental schemes. This is achieved by exploiting the dispersive interaction between an ensemble of qubits and a common resonator, alongside homodyne measurements. This interaction has been central for entanglement gates between qubits in numerous architectures, known as strong coupling [63–72]. Moreover, measurement-based entanglement of two qubits, via this interaction with inclusion of homodyne measurement, has been demonstrated in superconducting and solid state experiments [73–77]. Under specific parameter choices, we show that the generalisation of these protocols to _N_ qubits can be used to perform parity measurements of the ensemble. Thus, an ensemble of _N_ qubits can violate MR through NDC by performing two such consecutive parity measurements. 

In Sec. II, the ideal protocol is proposed, for which a constant quantum violation of MR is detectable with arbitrary number of qubits. In Sec. III, we find that a quantum-toclassical transition for large spins is induced by practical constraints, namely, operational imperfection, decoherence, and inhomogeneities among qubits. In Sec. IV, the experimental challenge of avoiding classical disturbances in NDC detection is discussed. In Sec. V, the experimental requirements for testing MR with different qubit-ensembles – Rydberg atoms, quantum dot spins, and superconducting qubits – are presented, where bounds on the maximum number of qubits for which the violation of MR is detectable are derived given the current state-of-the-art in _noisy_ technologies, concluding that _N_ NDC _∼_ 50 _−_ 100 qubits. In our parallel work [78], the proposed protocol is mapped to gates and used on IBM Quantum Computers (QCs) to detect non-classicality up to 38 qubits<sup>2</sup> . 

common resonator or cavity, as such system can be physically implemented in numerous implementations (see Sec. V). 

### **A. The No Disturbance Condition (NDC)** 

We begin by introducing the form of the two-time NDC that involves sequential measurements of a dichotomic observable (with _±_ outcomes) at two different instants _t_ 1 and _t_ 2, where _t_ 1 _< t_ 2. The NDC implies that the probability of obtaining a particular outcome for the measurement at _t_ 2 should be independent of whether a previous measurement has been performed. Mathematically, the NDC can be expressed as 



where, for instance, _P_ 1 _,_ 2( _−,_ +) is the joint probability of getting the outcomes _−_ at instant _t_ 1 and + at instant _t_ 2, and _P_ 2(+) is the probability of outcome + at instant _t_ 2 without any measurement at _t_ 1. If classical disturbance is not present (see Sec. IV), any non-zero value of _V±_ denotes quantum violation of the NDC, as the system wavefunction undergoes the measurement induced non-unitary collapse. Here we note that from normalization of probabilities, it follows that _V_ + = _−V−_ , from which we will be interested in the magnitude of such quantity _|V±|_ . 

### **B. Collective Qubit-Light Interactions** 

Let us consider _N_ qubits, with Pauli operators _σα_<sup>(</sup><sup>_i_)(where</sup> _i ∈_ [1 _, N_ ] labels the qubit and _α_ = _x, y, z_ , from which _σ±_ = _σx ± iσy_ ), and a resonator or cavity of frequency _ω_ with annihilation and creation operators being _a_ and _a_<sup>_†_</sup> . All the Hamiltonians are given in units of ℏ, i.e., the coupling is in the angular frequency units. In the interaction picture, the rotating-wave approximation is considered, and the qubitcavity interaction is given by the Jaynes-Cummings interaction Hamiltonian for _N_ -qubits 



where _gi_ is the coupling between the _i_ -th qubit and the cavity [84]. 

### **II. IDEAL PROTOCOL** 

In this Section, we begin by introducing the form of the two-time NDC and collective qubits-light interactions, used in this work. Then, the proposed protocol is presented for the ideal case, which is with infinite operational precision and in the absence of noise and decoherence. The analysis is first kept general for an ensemble of _N_ qubits that interacts with a 

> 2 increasing by one order of magnitude the best known results of detection of violation of MR on QCs [79–83]. 

As first analysis, the qubits are assumed to be identical and uniformly interacting with the cavity: the former assumption implies that all the qubits have the same natural frequency _ω_ 0 and the latter ensures that the qubit-cavity coupling constant is the same for all qubits, i.e. _{gi_ = _g ∀i ∈_ [0 _, N_ ] _}_ . We will further assume that there is no qubit-qubit interaction (which physically can be ensured by spacing the qubits at large enough distances, as these interactions usually decay rapidly with the distance, for instance, the dipole-dipole magnetic interaction, see Sec. V). Under the above assumption, the qubitensemble can be treated as a single large spin with angular momentum _j_ = _N/_ 2, Hilbert space _H ≃_ C<sup>2</sup><sup>_j_+1</sup> , and spin operators _Jα_ := (1 _/_ 2)<sup>�</sup><sup>_N_</sup> _i_ =0<sup>_σ_</sup> _α_<sup>(</sup><sup>_i_),with</sup><sup>_α_=</sup><sup>_x, y, z,_+</sup><sup>_, −_[85].</sup> 

Even Cohrent Spin State 

Odd Cohrent Spin State 



<!-- Start of picture text -->
J J<br>i/2 il?<br>0? 0?<br>—3j/2 —3j/2<br>—Jj —Jj<br>J J<br>i 0? i 0’?<br>Po —jj2 Y Po —ij2 Y<br>x 92 x 92<br><!-- End of picture text -->

7 



<!-- Start of picture text -->
Ct<br><!-- End of picture text -->

> 

/ / 

> > 



<!-- Start of picture text -->
Ideal NDC Violation as Function of Rotation Angle<br>0.5 j=2<br>0.4 — j=11/2<br>— j—10?<br>== 0.3 — j=10°+1/2<br>-H<br>—~ 0.2<br>0.1<br>0 Ey ———<br>0 m/4 7/2 3/4<br><!-- End of picture text -->

(a) J=10 



<!-- Start of picture text -->
— 1[1—(cos2¢1)%]<br>— lsin2¢))%<br><!-- End of picture text -->



<!-- Start of picture text -->
0.25<br>0.20<br>ois<br>H<br>—olo g<br>:<br>0.05<br>0.00 F<br>T i ’<br>75 i.<br>™<br>oq<br>© is<br>=8 Im3m 2<br>0 8 fod<br>Vv.<br>. (b) J=4 . © J=40 g<br>7 7<br>020<br>fd8 sn8<br>0.15<br>$1 Sz<br>0.10<br>; ; 0.05<br>00<br>1il<br><!-- End of picture text -->

J 

~~_ — =~~ ( ) ~~=~~ 

~~-——~~ \/ 

~~-~~ 

# ~~BE —————~~ 



<!-- Start of picture text -->
(a) Spin Decoherence<br>025 : - 025 Too<br>: : 7=6 St teeentiiie, Ty =01<br>0.20 1 i — j=121 020 Tet « r;=001<br>i } — j=24 ees) « ry=0.001<br>—0.15 + + ¢ — 0154" “tens,<br>H 1 i i=4 . jl EE<br>~ I .<br>=o.10 3 0.10<br>0.05 : : i 0.05 EXTFTO<br>0.00 . i i 0.00<br>107 107 102 107! 10° 10! 0 10 20 . 30 40 50<br>Ts =%s/X J<br><!-- End of picture text -->



<!-- Start of picture text -->
(b) Cavity Decoherence<br>025 T= - - 0.25 —=e<br>020 | | lag] =1 Ble =<br>—+ ols I=I1| — laol=2ooJag|=10_ LAT| 02 ~_ ar VeeS “sq<br>~—~ 010 |1 0.10 Ne N oh<br>\ N 2= 1,=01<br>0.05 005 === 7e=0.01<br>M|=== r.=0.001<br>0.00 i 0.00 a<br>107+ 10-3 1072 107! 10° 10! 1 2 3 4 5<br>FaoX |v]<br><!-- End of picture text -->



<!-- Start of picture text -->
(a) j=12<br>0.25<br>—— n=2<br>a]2 m3 TN=<br>Bey n=4 !<br>00s 4 ~~~ 715=0.005 ! !<br>coo E== 1s = 0.01 ! ! NN eo<br>1073 10-2<br>To = a4/{9)<br>(b) 7, = 0.005 (c)r,=0.01<br>025 {5 i 0.25<br>0.20 ii T= i i] 0» ; i<br>hols { 0.15 |<br>>of 1 on=2 010 iI n=2 H i i<br>00s{ t n=3 gos Jie m=3 it<br>0.00 bP on=a 300 tf n=4<br>0 5 10 15 0 5 10 15<br>J J<br><!-- End of picture text -->

8 

- In both parts of the protocol, after the initial rotation, the spin is entangled with the cavity such that the joint state becomes _|ϕ⟩es |α_ 0 _⟩c_ + _|ϕ⟩os |−α_ 0 _⟩c_ . 

- Subsequently, the homodyne measurement is performed on the cavity, depending on which part of the protocol is being implemented – the homodyne measurement is performed in the double measurement part. In contrast, it is not performed in the single measurement part. On the one hand, if the measurement is performed, the spin-cavity collapses to one of the two unthe other hand, if the measurement was not performed, _|_ normalized _ϕ⟩os ⊗|−α_ post-measurement0 _⟩c_ with the probabilitiesstates _|ϕ_ of _⟩e_ Eq. _s ⊗|_ (10 _α_ 0). _⟩c_ Onor the state remains the same. 

- In both cases, an identical spin-cavity entanglement dynamics is performed again. If the measurement was performed, the second spin-cavity entanglement dynamics will evolve the aforementioned two collapsed states to _|ϕ⟩es ⊗|α_ 0 _⟩c_ and _|ϕ⟩os ⊗|α_ 0 _⟩c_ respectively. If the measurement was not performed, the non-collapsed state under the second entangling dynamics evolves to the initial product state, that is, _|ϕ⟩s ⊗|α_ 0 _⟩_ . 

- In both of these cases, the cavity is then discarded trivially.the homodyneHence, themeasurementspin is in thewas _|ϕ⟩_ performed, _es_ or _|ϕ⟩os_ whilestates inif the _|ϕ⟩s_ state if the homodyne measurement was not performed. 

- The second rotation of the spin and the final measurement (involving another spin-cavity entanglement dynamics along with the homodyne measurement on the cavity) are performed in both cases. 

In this modified protocol, the entangling dynamics is performed three times in both the double-measurement and single-measurement cases. The only difference between the two parts of the protocol is the intermediate homodyne measurement on the cavity. The violation of NDC is equivalent to that of the ideal protocol depicted in Sec. II, but ensuring that the classical disturbance is minimised. 

_Note Added:_ The above-modified protocol points out a fundamental feature of the quantum measurement process. Quantum measurement consists of two stages: (Step 1:) entangling dynamics between the target system (the system to be measured – the qubit-ensemble in the present case) and the probe (cavity in the present case), (Step 2:) reading out the outcome by performing the projective measurement on the probe (homodyne measurement on the cavity in the present case). The Step 1 causes disturbance on the target system, as any pure state of the target system becomes mixed after the entangling dynamics. On the other hand, the Step 2 makes this disturbance irreversible, as the pure entangled joint state of the target-probe collapses into a specific state depending on the outcome, thus becomes mixed due to this step over many 

runs of the experiment<sup>5</sup> . In the absence of this Step 2, the disturbance on the target can be eliminated by applying the inverse of the entangling unitary dynamics on the joint state of the target-probe (this happens in the above-mentioned modified protocol in the absence of the homodyne measurement). Hence, while the entangling dynamic is responsible for quantum measurement-induced disturbance, the reading-out step is crucial for making this disturbance irreversible. These two steps together cause an irreversible collapse on the target system – a genuine non-classical feature. 

Note that, without the reading out part, doing and then undoing the entangling dynamics between the probe and the system is done in the context Stern-Gerlach interferometry [12, 94, 95]. 

### **B. Method 2 to reduce the classical disturbance** 

The aforementioned method requires three entangling dynamics, which may be experimentally difficult to realise. An alternative method to minimise the CD is to always perform two entangling dynamics, but change the input state of the probe between the single and double measurement parts of the protocol. 

The double measurement part of the protocol is the same as presented in Sec. II. On the other hand, the single measurement part is the same as the double measurement part, except that the input state of the cavity during the first entangling dynamics is ( _|α_ 0 _⟩_ + _|−α_ 0 _⟩_ ) _/√_ 2. Hence, after the initial rotation of the spin state and introducing the cavity, the spin-cavity state becomes _|ϕ⟩s ⊗_ ( _|α_ 0 _⟩c_ + _|−α_ 0 _⟩c_ ) _/√_ 2, which evolves under the entangling dynamics to _|ϕ⟩s ⊗|α_ 0 _⟩c_ . Subsequently, the homodyne measurement on the cavity is performed trivially, leading to the post-measurement state of the spin _|ϕ⟩s_ . The second rotation and measurement are then performed as usual, leading to the same measurement probabilities, and the same NDC violation of Sec. II. 

In this method, the first entangling dynamics in the single measurement part does not entangle the spin and the cavity (we are using the term “entangling dynamics” just to refer to the interaction between the spin and the cavity mentioned in stage (iii) of Sect. II C). Consequently, this interaction along with the homodyne measurement on the cavity cannot be interpreted as a measurement of the spin at all. Hence, in effect, in the single measurement part, measurement on the spin is performed only once – i.e., the final measurement on the spin. Thus, the only difference between the single and double measurement parts of this method is applying an (optional) local unitary on the probe, significantly reducing the CD. It should be noted that such states are routinely prepared in optical systems [96, 97]. 

> 5 In a many-world interpretation, when reading out the outcome of a measurement, the target-probe entangles with the rest of the world, under a unitary that cannot be reversed. 



<!-- Start of picture text -->
Ly,<br>7 pLlL<br><!-- End of picture text -->

10 

|Experimental Parameters|Symbols|Units|Superconducting<br>Qubits|Rydberg Atoms|Spin Qubits with<br>Spin-Orbit|
|---|---|---|---|---|---|
|Electric Dipole|_d_|_a_0_e_|_∼_10<sup>4</sup>|_∼_3_·_10<sup>3</sup>|_∼_10<sup>2</sup>|
|Single Qubit-Photon Coupling|_g/_(2_π_)|MHz|110|7|1|
|Detuning Frequency|∆_/_(2_π_)|MHz|1000|70|10|
|Entanglement Coupling|_χ/_(2_π_)|MHz|45|3|0_._4|
|Distance Between Qubits|_rq_|_µ_m|35|23|7|
|Bound o|n Number|of Qubit|s and Decoherence|Rates||
|Bound on number from inhomogeneity|_N_ <sup>inh</sup><br>NDC|NA|≲41|≲53|≲110|
|Spin Dephasing Rate|_γs/_(2_π_)|kHz|≲4500|≲300|≲45|
|Cavity Decay Rate|_γc/_(2_π_)|kHz|≲1000|≲54|≲24|
|Single-qubit Rotation Uncertainty|_σϕ_|rad|≲0_._027|≲0_._024|≲0_._017|



TABLE I: Orders of magnitude of the parameters for realising the NDC parity protocol with (i) Superconducting Qubits, (ii) Rydberg Atoms, and (iii) Spin qubits. For all of the above, the fundamental frequency of the CWR is _ω/_ (2 _π_ ) _≈_ 3 _._ 5 GHz ( _e_ is the electron charge, and _a_ 0 the Bohr radius). 

where _E_ 0 is the vacuum electric field density, _V_ is the volume of the resonator, and _ϵ_ 0 and _ϵr_ are the vacuum and relative (effective) permittivities. From the values of _g_ given in Table I, it is possible to note that the bound on decay rate of the resonator does not represent an experimental challenge, as lower decay rates have been reported in a large number of resonator, for instance, _∼_ 1 kHz [104]. Here, it should be noted that a higher decay rate may be preferable in order to collect the necessary light to perform homodyne detection [77]. 

The number of qubits achievable ( _N_ NDC) is restricted by the volume in which the qubits can be placed. On the one hand, a large qubit-cavity coupling _g_ – which requires a small volume – is preferable such that the experiment is performed within the coherence time of the system and the strong coupling regime is met. On the other hand, a small volume increases the noise caused by direct qubit-qubit interactions – as they are placed closer to each other – and by coupling inhomogeneity – as the electric field strength of the resonator would change more rapidly among qubits, implying different couplings. The dipole-dipole interaction (with coupling _dg_ ) is negligible compared to the entanglement interaction (with coupling _χ ∼_ 0 _._ 4 _g_ , which is the slowest process of the experiment), when 



This gives the minimum distance between qubits ( _rq_ ) at which they can be placed such that the dipole-dipole interaction is negligible. Choosing _dg/χ ∼_ 0 _._ 05, the minimum distance is given by _rq ≈_ 1 _._ 6 _· n_<sup>1</sup> _d_<sup>_/_3</sup> _· µ_ m. 

However, different positions of the qubits in the resonator introduce inhomogeneity in the coupling because different qubits experience a different electric field strength due to its dependency on _x_ . Specifically, the qubits are placed in a line at ( _x, y_ ) = ( _krq,_ 0), where _k ∈_ [ _−N/_ 2 _, N/_ 2] and the _z_ - component of the electric field density is the first harmonic _Ez_ ( _x_ ) _∼ E_ 0 cos( _πx/Lx_ ). Then, the coupling of the _i_ -th qubit 

## is given by 



Such an inhomogeneity increases with the number of qubits as _k ∈_ [ _−N/_ 2 _, N/_ 2] and it is inversely proportional to the volume ( _V ∼ L_ ). In Appendix G, the arising inhomogeneity is studied and found to be negligible (i.e. _σg/g_ ≲ _O_ (1 _/_ (10 _N_ )), as shown in Sec. III), if the following bound is met 



One should note that this may not be a stringent bound compared to one given by physical implementation where fabrication imperfections (in the case of superconducting and spins qubits) and uncertainty in the trapping positions (Rydberg atoms) may increase inhomogeneity effects. However, the source of inhomogeneity studied may be decreased via the use of multiple cascaded cavities, similar to [73–77]. 

The chosen parameters are given in Table I, for which the bound given by the inhomogeneity ( _N_ NDC<sup>inh)isderived</sup> and subsequently used to compute the bounds on the spin dephasing rate and single-qubit rotation uncertainty, which have a _N_ dependency – i.e. _γs_ ≲ _g/_ (2 _._ 5 _N_ NDC<sup>inh)and</sup><sup>_σϕ_≲</sup> _O_ (1 _/_ (4�2 _N_ NDC<sup>inh+ 1)).Ononehand,itispossibletonote</sup> that for highly interacting qubits, as in the case of superconducting qubits and Rydberg atoms with high dipoles (and hence coupling), the dephasing bound is not stringent, as the experiment can be performed within decoherence times. However, high coupling increases the direct dipole-dipole interactions, which subsequently increases the minimum distance at which the qubit can be place, and hence the inohomodeinty bound limits the experiment to _N_ NDC<sup>Sup</sup><sup>_∼_41and</sup> _N_ NDC<sup>Ryd</sup><sup>_∼_53,for superconducting qubits and Rydberg atoms,</sup> respectively. One the other hand, in the case of semiconductor 

11 

spins, the lower dipole increases the bound given by the inhomogeneity _N_ NDC<sup>Spin</sup><sup>_∼_110,while,however,the lower coupling</sup> increases the demand on coherence time. 

### **VI. CONCLUSIONS** 

We present a protocol to implement parity measurements on an ensemble of qubits exploiting their dispersive interaction with a resonator and a subsequent homodyne measurement of a resonator’s quadrature. By comparing single and double parity measurement schemes, a constant quantum violation of MR is detectable via NDC with arbitrary many qubits: in the ideal case, the non-classicality of a qubit ensemble is always detectable, even for many ℏ units. The quantumness manifests itself via the unavoidable disturbance caused by collapse of the ensemble’s wavefunction under a parity measurement. The proposed protocol is operationally _independent_ of the size of the ensemble, hence representing the first experimentally realisable test for non-classicality up to any macroscopic scale in units of ℏ. 

We find that the limiting factors of the proposal are induced by decoherence and inhomogeneity in the qubit-resonator couplings, which induces the quantum-to-classical transition, recovering the classical behaviour of the macroscopic world as the number of qubits increases. This behaviour is not fundamental; rather it is only due to operational constraints, as it becomes more challenging to perform the experiment with a larger number of qubits. 

We detail a specific implementation of the protocol using CWR with a variety of qubits, namely, superconducting qubits, Rydberg atoms, and spin qubits with artificial spinorbit interaction. In this context, it should be noted that operationally similar experiments – i.e. dispersive interaction and homodyne measurement via CWR – have already been performed for probabilistic generation of the entangled state between two qubits (effectively performing a parity measurement), for superconducting and spin qubits [75–77]. Thus, 

- [1] V. Athalye, S. S. Roy, and T. S. Mahesh, _Investigation of the Leggett-Garg Inequality for Precessing Nuclear Spins_ , Phys. Rev. Lett. **107** , 130402 (2011). 

- [2] G. C. Knee, S. Simmons, _et al. Violation of a Leggett–Garg inequality with ideal non-invasive measurements_ , Nature Communications **3** , 606 (2012). 

- [3] A. Vaartjes, M. Nurizzo, _et al._ , _Certifying the quantumness of a nuclear spin qudit through its uniform precession_ , Newton **1** , 100017 (2025). 

- [4] A. J. Leggett and A. Garg, _Quantum mechanics versus macroscopic realism: Is the flux there when nobody looks?_ , Phys. Rev. Lett. **54** , 857 (1985). 

- [5] A. J. Leggett, _Testing the limits of quantum mechanics: motivation, state of play, prospects_ , J. Phys. Condens. Matter **14** , R415 (2002). 

our generalizations to _N_ -qubits is already accessible for experimental implementations to test the macroscopic limit of quantum mechanics. 

We conclude that, given the state-of-the-art quantum technologies, it is possible to detect the quantumness of ensembles of superconducting qubits, Rydberg atoms, and spins in semiconductors with spin-orbit interaction up to _N_ NDC<sup>Sup</sup><sup>_∼_41,</sup> _N_ NDC<sup>Ryd</sup><sup>_∼_53,and</sup><sup>_N_</sup> NDC<sup>Spin</sup><sup>_∼_110,respectively.Theproposed</sup> protocol is scalable in the number of qubits as the quantum technologies progress to more isolated systems, such that the transition to classicality can be experimentally investigated under different noises. Here we note our parallel work in the context of QC [78], where the clumsiness-loophole-free protocol has been used to detect quantumness of IBM QCs up to 38 qubits, showing the transition to classicality as the QC becomes macroscopic. 

To conclude, the presented protocol explores the limit of quantum mechanics for large and macroscopic qubit ensembles. Therefore, it can be concluded that Bohr’s correspondence principle is not a fundamental property of quantum mechanics, but rather an operational constraint: If decoherence and inhomogeneity can be conquered, then _in principle, quantum effects are present even when_ ℏ _→_ 0 _._ 

### **VII. ACKNOWLEDGMENTS** 

BZ and LB work was supported by the Engineering and Physical Sciences Research Council [Grant Numbers EP/R513143/1, EP/T517793/1, and EP/R513143/1,EP/W524335/1, respectively]. DD acknowledges the Royal Society, United Kingdom, for the support through the Newton International Fellowship (No. NIF _\_ R1 _\_ 212007). DD and SB acknowledge financial support from EPSRC (Engineering & Physical Sciences Research Council, United Kingdom) Grant Numbers EP/X009467/1 and EP/R029075/1 and STFC (Science and Technology Facilities Council, United Kingdom) Grant Numbers ST/W006227/1 and ST/Z510385/1. 

- [6] A. J. Leggett, _Realism and the physical world_ , Rep. Prog. Phys. **71** , 022001 (2008). 

- [7] C. Emary, N. Lambert, and F. Nori, _Leggett–Garg inequalities_ , Rep. Prog. Phys. **77** , 016001 (2014). 

- [8] J. Kofler and C. Brukner, _Condition for macroscopic realism beyond the Leggett-Garg inequalities_ , Phys. Rev. A **87** , 052115 (2013). 

- [9] G. Schild and C. Emary, _Maximum violations of the quantumwitness equality_ , Phys. Rev. A **92** , 032101 (2015). 

- [10] G. C. Knee, K. Kakuyanagi _et al._ , _A strict experimental test of macroscopic realism in a superconducting flux qubit_ , Nature Communications **7** , 13253 (2016). 

- [11] D. Das, D. Home, H. Ulbricht, and S. Bose, _Mass-Independent Scheme to Test the Quantumness of a Massive Object_ , Phys. Rev. Lett. **132** , 030202 (2024). 

12 

- [12] F. Hanif, D. Das _et al._ , _Testing Whether Gravity Acts as a Quantum Entity When Measured_ , Phys. Rev. Lett. **133** , 180201 (2024). 

- [13] J. H. Wesenberg, A. Ardavan _et al._ , _Quantum Computing with an Electron Spin Ensemble_ , Phys. Rev. Lett. **103** , 070502 (2009). 

- [14] Y. Kubo, F. R. Ong _et al._ , _Strong Coupling of a Spin Ensemble to a Superconducting Resonator_ , Phys. Rev. Lett. **105** , 140502 (2010). 

- [15] J. Chen, A. A. Zadorozhko, and D. Konstantinov, _Strong coupling of a two-dimensional electron ensemble to a single-mode cavity resonator_ , Phys. Rev. B **98** , 235418 (2018). 

- [16] Y. Ping, E. M. Gauger, and S. C. Benjamin, _Measurementbased quantum computing with a spin ensemble coupled to a stripline cavity_ , New J. Phys. **14** , 013030 (2012). 

- [17] N. Mohseni, M. Narozniak _et al._ , _Error suppression in adiabatic quantum computing with qubit ensembles_ , npj Quantum Inf **7** , 71 (2021). 

- [18] F. Troiani, A. Ghirri, M. G. A. Paris, C. Bonizzoni, and M. Affronte, _Towards quantum sensing with molecular spins_ , Journal of Magnetism and Magnetic Materials **491** , 165534 (2019). 

- [19] H. Wu, S. Yang _et al._ , _Enhanced quantum sensing with room-temperature solid-state masers,_ Science Advances **8** , 48 (2022). 

- [20] M. Schaffry, E. M. Gauger _et al._ , _Quantum metrology with molecular ensembles_ , Phys. Rev. A **82** , 042114 (2010). 

- [21] H. Wu, R. E. George _et al._ , _Storage of Multiple Coherent Microwave Excitations in an Electron Spin Ensemble_ , Phys. Rev. Lett. **105** , 140503 (2010). 

- [22] D. I. Schuster, A. P. Sears _et al._ , _High-Cooperativity Coupling of Electron-Spin Ensembles to Superconducting Cavities_ , Phys. Rev. Lett. **105** , 140501 (2010). 

- [23] Y. Kubo, C. Grezes _et al._ , _Hybrid Quantum Circuit with a Superconducting Qubit Coupled to a Spin Ensemble_ , Phys. Rev. Lett. **107** , 220501 (2011). 

- [24] X. Zhu, S. Saito _et al._ , _Coherent coupling of a superconducting flux qubit to an electron spin ensemble in diamond_ , Nature **478** , 221-224 (2011). 

- [25] R. Ams¨uss, Ch. Koller _et al._ , _Cavity QED with Magnetically Coupled Collective Spin States_ , Phys. Rev. Lett. **107** , 060502 (2011). 

- [26] J. H. Wesenberg, Z. Kurucz, and K. Molmer, _Dynamics of the collective modes of an inhomogeneous spin ensemble in a cavity_ , Phys. Rev. A **83** , 023826 (2011). 

- [27] S. Saito, X. Zhu, _et al._ , _Towards Realizing a Quantum Memory for a Superconducting Qubit: Storage and Retrieval of Quantum States_ , Phys. Rev. Lett. **111** , 107008 (2013). 

- [28] V. Ranjan, G. de Lange, _et al._ , _Probing Dynamics of an Electron-Spin Ensemble via a Superconducting Resonator_ , Phys. Rev. Lett. **110** , 067004 (2013). 

- [29] S. Probst, H. Rotzinger _et al._ , _Anisotropic Rare-Earth Spin Ensemble Strongly Coupled to a Superconducting Resonator_ , Phys. Rev. Lett. **110** , 157001 (2013). 

- [30] B. Julsgaard, and K. Molmer, _Fundamental limitations in spinensemble quantum memories for cavity fields_ , Phys. Rev. A **88** , 062324 (2013). 

- [31] C. Grezes, B. Julsgaard _et al._ , _Multimode Storage and Retrieval of Microwave Fields in a Spin Ensemble_ , Phys. Rev. X **4** , 021049 (2014). 

- [32] Y. Tabuchi, S. Ishino _et al._ , _Hybridizing Ferromagnetic Magnons and Microwave Photons in the Quantum Limit_ , Phys. Rev. Lett. **113** , 083603 (2014). 

- [33] C. Grezes, B. Julsgaard _et al._ , _Storage and retrieval of microwave fields at the single-photon level in a spin ensemble_ , Phys. Rev. A **92** , 020301(R) (2015). 

- [34] C. Grezes, Y. Kubo _et al._ , _Towards a spin-ensemble quantum memory for superconducting qubits_ , Comptes Rendus Physique **17** , 693 (2016). 

- [35] J. J. L. Morton, and P. Bertet, _Storing quantum information in spins and high-sensitivity ESR_ , Journal of Magnetic Resonance **287** , 128 (2018). 

- [36] J. O’Sullivan, O. W. Kennedy _et al._ , _Random-Access Quantum Memory Using Chirped Pulse Phase Encoding_ , Phys. Rev. X **12** , 041014 (2022). 

- [37] M. H. Appel, A. Ghorbal _et al._ , _Many-body quantum register for a spin qubit_ , Nat. Phys. **21** , 368-373 (2025). 

- [38] S. Simmons, R. Brown _et al._ , _Entanglement in a solid-state spin ensemble_ , Nature **470** , 69 (2011). 

- [39] M. Zhong, M. Hedges _et al._ , _Optically addressable nuclear spins in a solid with a six-hour coherence time_ , Nature **517** , 177 (2015). 

- [40] A. Bourassa, C. P. Anderson _et al._ , _Entanglement and control of single nuclear spins in isotopically engineered silicon carbide_ , Nat. Mater. **19** , 1319–1325 (2020). 

- [41] T. Holstein, and H. Primakoff, _Field Dependence of the Intrinsic Domain Magnetization of a Ferromagnet_ , Phys. Rev. **58** , 1098 (1940). 

- [42] N. Gisin, and A. Peres, _Maximal violation of Bell’s inequality for arbitrarily large spin_ , Phys. Lett. A **162** , 15 (1992). 

- [43] A. Peres, _Finite violation of a Bell inequality for arbitrarily large spin_ , Phys. Rev. A **46** , 4413 (1992). 

- [44] D. Home, and A. S. Majumdar, _Incompatibility between quantum mechanics and classical realism in the “strong” macroscopic limit_ , Phys. Rev. A **52** , 4959 (1995). 

- [45] A. Cabello, _Bell’s inequality for n spin-s particles_ , Phys. Rev. A **65** , 062105 (2002). 

- [46] J. Kofler, and C. Brukner, _Classical World Arising out of Quantum Physics under the Restriction of Coarse-Grained Measurements_ , Phys. Rev. Lett. **99** , 180403 (2007). 

- [47] J. Kofler, and C. Brukner, _Conditions for Quantum Violation of Macroscopic Realism_ , Phys. Rev. Lett. **101** , 090403 (2008). 

- [48] C. Budroni, T. Moroder, M. Kleinmann, and O. Guhne, _Bounding Temporal Quantum Correlations_ , Phys. Rev. Lett. **111** , 020403 (2013). 

- [49] H. Jeong, Y. Lim, and M. S. Kim, _Coarsening Measurement References and the Quantum-to-Classical Transition_ , Phys. Rev. Lett. **112** , 010402 (2014). 

- [50] C. Budroni, and C. Emary, _Temporal Quantum Correlations and Leggett-Garg Inequalities in Multilevel Systems_ , Phys. Rev. Lett. **113** , 050401 (2014). 

- [51] S. Mal, and A. S. Majumdar, _Optimal violation of the LeggettGarg inequality for arbitrary spin and emergence of classicality through unsharp measurements_ , Phys. Lett. A **380** , 2265 (2016). 

- [52] S. Mal, D. Das, and D. Home, _Quantum mechanical violation of macrorealism for large spin and its robustness against coarse-grained measurements_ , Phys. Rev. A **94** , 062117 (2016). 

- [53] S. Mukherjee, A. Rudra, D. Das, S. Mal, and D. Home, _Persistence of quantum violation of macrorealism for large spins even under coarsening of measurement times_ , Phys. Rev. A **100** , 042114 (2019). 

- [54] S. Hill, R. S. Edwards, N. Aliaga-Alcalde, and G. Christou, _Quantum coherence in an exchange-coupled dimer of singlemolecule magnets_ , Science **302** , 1015 (2003). 

13 

- [55] E. del Barco, N. Vernier _et al._ , _Quantum coherence in Fe8 molecular nanomagnets_ , EPL **47** , 722 (1999). 

- [56] E. del Barco, J. M. Hernandez _et al._ , _High-frequency resonant experiments in Fe_ 8 _molecular clusters_ , Phys. Rev. B **62** , 3018 (2000). 

- [57] D. D. Awschalom, D. P. DiVincenzo, and J. F. Smyth, _Macroscopic quantum effects in nanometer-scale magnets_ , Science **258** , 414 (1992). 

- [58] D. D. Awschalom, J. F. Smyth, G. Grinstein, D. P. DiVincenzo, and D. Loss, _Macroscopic quantum tunneling in magnetic proteins_ , Phys. Rev. Lett. **68** , 3092 (1992). 

- [59] S. Gider, D. Awschalom, T. Douglas, S. Mann and M. Charala, _Classical and quantum magnetic phenomena in natural and artificial ferritin proteins_ , Science **268** , 77 (1995). 

- [60] H. W. Lau, Z. Dutton, T. Wang, and C. Simon, _Proposal for the Creation and Optical Detection of Spin Cat States in BoseEinstein Condensates_ , Phys. Rev. Lett. **113** , 090401 (2014). 

- [61] P. Gupta, A. Vaartjes, X. Yu, A. Morello, and B. C. Sanders, _Robust Macroscopic Schr¨odinger’s Cat on a Nucleus_ , Phys. Rev. Research **6** , 013101 (2024). 

- [62] C. M. Ramsey, E. del Barco _et al._ , _Quantum interference of tunnel trajectories between states of different spin length in a dimeric molecular nanomagnet_ , Nature Phys. **4** , 277 (2008). 

- [63] Z.-L. Xiang, S. Ashhab, J. Q. You, and F. Nori, _Hybrid quantum circuits: Superconducting circuits interacting with other quantum systems_ , Rev. Mod. Phys. **85** , 623–653 (2013). 

- [64] A. Blais, J. Gambetta, _et al._ , _Quantum-information processing with circuit quantum electrodynamics_ , Phys. Rev. A **75** , 032329 (2007). 

- [65] A. Wallraff, D. I. Schuster _et al._ , _Strong coupling of a single photon to a superconducting qubit using circuit quantum electrodynamics_ , Nature **431** , 162–167 (2004). 

- [66] I. Chiorescu, P. Bertet _et al._ , _Coherent dynamics of a flux qubit coupled to a harmonic oscillator_ , Nature **431** , 159–162 (2004). 

- [67] N. Samkharadze, G. Zheng _et al._ , _Strong spin-photon coupling in silicon_ , Science **359** , 1123-1127 (2018). 

- [68] X. Mi, M. Benito _et al._ , _A coherent spin–photon interface in silicon_ , Nature **555** , 599-603 (2018). 

- [69] A. J. Landig, J. V. Koski _et al._ , _Coherent spin–photon coupling using a resonant exchange qubit_ , Nature **560** , 179–184 (2018). 

- [70] A. A. Morgan, and S. D. Hogan, _Coupling Rydberg Atoms to Microwave Fields in a Superconducting Coplanar Waveguide Resonator_ , Phys. Rev. Lett. **124** , 193604 (2020). 

- [71] J. Majer, J. Chow _et al._ , _Coupling superconducting qubits via a cavity bus_ , Nature **449** , 443–447 (2007). 

- [72] J. D. Pritchard, J. A. Isaacs _et al._ , _Hybrid atom-photon quantum gate in a superconducting microwave resonator_ , Phys. Rev. A **89** , 010301 (2014). 

- [73] R. Ruskov and A. N. Korotkov, _Entanglement of solid-state qubits by measurement_ , Phys. Rev. B **67** , 241305 (2003). 

- [74] K. Lalumi`ere, J. M. Gambetta, and A. Blais, _Tunable joint measurements in the dispersive regime of cavity QED_ , Phys. Rev. A **81** , 040301 (2010). 

- [75] N. Roch, M. Schwartz _et al._ , _Observation of measurementinduced entanglement and quantum trajectories of remote superconducting qubits_ , Phys. Rev. Lett. **112** , 170501 (2014). 

- [76] R. L. Delva, J. Mielke, G. Burkard, and J. R. Petta, _Measurement-based entanglement of semiconductor spin qubits_ , Phys. Rev. B **110** , 035304 (2024). 

- [77] R. L. Delva, J. Mielke, G. Burkard, and J. R. Petta, _Measurement-based entanglement of semiconductor spin qubits_ , Phys. Rev. B **110** , 035304 (2024). 

- [78] B. Zindorf, L. Braccini, D. Das, and S. Bose, _How Quantum is your Quantum Computer? Macrorealism-based Benchmarking via Mid-Circuit Parity Measurements_ , Parallel Work. 

- [79] E. Huffman, and A. Mizel, _Violation of noninvasive macrorealism by a superconducting qubit: Implementation of a Leggett-Garg test that addresses the clumsiness loophole_ , Phys. Rev. A **95** , 032131 (2017). 

- [80] H.-Y. Ku, N. Lambert, F.-J. Chan, C. Emary, Y.-N. Chen, and F. Nori, _Experimental test of non-macrorealistic cat states in the cloud_ , npj Quantum Inf **6** , 98 (2020). 

- [81] A. Santini, and V. Vitale, _Experimental violations of LeggettGarg inequalities on a quantum computer_ , Phys. Rev. A **105** , 032610 (2022). 

- [82] P. P. Nath, A. Sinha, and U. Sinha, _Certified Random Number Generation using Quantum Computers_ , arXiv:2502.02973 [quant-ph]. 

- [83] D. Melegari, M. Cardi, and P. Solinas, _Quantum simulations of macrorealism violation via the QNDM protocol_ , arXiv:2502.17040 [quant-ph]. 

- [84] A. D. Greentree, J. Koch, and J. Larson, _Fifty years of Jaynes–Cummings physics_ , J. Phys. B: At. Mol. Opt. Phys. **46** 220201. 

- [85] R. H. Dicke, _Coherence in Spontaneous Radiation Processes_ , Phys. Rev. **93** , 99 (1954). 

- [86] J. Schliemann, _Coherent Quantum Dynamics: What Fluctuations Can Tell_ , Phys. Rev. A **92** , 022108 (2015). 

- [87] Z. Wang, Y. Wang _et al._ , _Giant spin ensembles in waveguide magnonics_ , Nature Communications **13** , 7580 (2022). 

- [88] J. Ma, X. Wang, C. P. Sun, and F. Nori, _Quantum spin squeezing_ , Physics Reports **509** , 89-165 (2011). 

- [89] M. Tavis and T. Cummings,, _Exact Solution for an N - Molecule—Radiation-Field Hamiltonian_ , Phys. Rev. **170** , 379–384 (1968). 

- [90] A. Ferraro, S. Olivares, and M. G. A. Paris _Gaussian states in continuous variable quantum information_ arXiv, quantph/0503237, (2005). 

- [91] M. Schlosshauer, _Decoherence and the Quantum-To-Classical Transition_ , Springer International Publishing (2007). 

- [92] F. Bibak, C. Cepollaro _et al._ , _The classical limit of quantum mechanics through coarse-grained measurements_ arXiv, quant-ph/2503.15642, (2025). 

- [93] M. Wilde, and A. Mizel, _Addressing the Clumsiness Loophole in a Leggett-Garg Test of Macrorealism_ , Found. Phys. **42** , 256–26 (2012). 

- [94] S. Bose, A. Mazumdar _et al._ , _Spin entanglement witness for quantum gravity_ , Phys. Rev. Lett. **119** , 240401 (2017). 

- [95] Y. Margalit, O. Dobkowski _et al._ , _Realization of a complete stern-gerlach interferometer: Toward a test of quantum gravity_ , Science Advances **7** , eabg2879 (2021). 

- [96] A. Ourjoumtsev, R. Tualle-Brouri, J. Laurat, and P. Grangier, _Generating Optical Schr¨odinger Kittens for Quantum Information Processing._ , Science **312** , 83-86 (2006). 

- [97] A. Ourjoumtsev, H. Jeong, R. Tualle-Brouri, and P. Grangier, _Generation of optical ‘Schr¨odinger cats’ from photon number states_ , Nature **448** , 784–786 (2007). 

- [98] B. Danjou, and G Burkard, _Optimal dispersive readout of a spin qubit with a microwave resonator_ , Phys. Rev. B **100** , 245427 (2019). 

- [99] J. Kang, C. Kim, Y. Kim, and Younghun Kwon, _New design of three-qubit system with three transmons and a single fixed-frequency resonator coupler_ , Scientific Reports **15** , 12134 (2025). 

- [100] R.E.Collin, _Foundation of Microwave Engineering_ , IEEE Press Series on Electromagnetic Wave Theory. 

> 

/ ~~>~~ 

oe) ) > ~~—/~~ J ( oe) ) ) > ~~— >~~ ) > ~~— >~~ ) ~~=~~ > ~~3~~ ) ~~2~~ ) 

® () 

> 5 

~~YX~~ 

> 

15 

### **Appendix B: Deriving the expression of quantum violation of the NDC in ideal case** 

The analytical derivation of the violation is presented in details for a even integer spin _j_ . Subsequently, the odd integer and half-integer cases are described. The probabilities and the NDC violations are summarised in Table II. 

The spin is initially in the _ground_ state _|_ Ψ(0) _⟩s_ = _|j, −j⟩s_ . With the on-resonance Hamiltonian of Eq. (2), a rotation of angle _ϕ_ = 2 _gαtR_ is performed on the spin. Mathematically, the rotation (unitary) operator considered is _R_ ( _ϕ_ ) = _e_<sup>_−iϕJy_</sup> . After the rotation, the spin is described by the CS in Eq. (4). Next, the cavity and the spins are let to interact for a time interval _tI_ , with the cavity out of resonance, with the Hamiltonian in Eq. (3). The input cavity quantum state is taken in be a CS: _|α_ 0 _⟩c_ = _e_<sup>_−_</sup> 2<sup><u>1</u></sup><sup>_|α_0</sup><sup>_|_2 �</sup> _n_ _~~√~~ αn_<sup>_n_</sup> <u>0</u> !<sup>_|n⟩c_with</sup><sup>_α_0=</sup><sup><u>1+</u></sup> _~~√~~_ 2<sup>_<u>i</u>|α_0</sup><sup>_|_,where</sup><sup>_|α_0</sup><sup>_|≫_1.Aftertheinteraction,theentangledstatebetweenthe</sup> cavity and the spin system is 



up to a global phase (proportional to _J_<sup>2</sup> ), and where the second equality follows from the choice _χtI_ = _π_ , where we note that at this time the phase is trivially zero. 

The projective measurement _{_ Π+ _,_ Π _−}_ defined in Eq. (8) are performed on the cavity field, resulting in the following unnormalized post-measurement (UPM) states, 



where the position representation of the coherent state was used _⟨x|α⟩c_ = _π_<sup>_−_1</sup><sup>_/_4</sup> _e_<sup>_−_</sup><sup><u>1</u></sup> 2<sup>(</sup><sup>_x−_</sup> _~~√~~_ 2Re( _α_ ))2+ _i_ _~~√~~_ 2 _x_ Im( _α_ ). Here “U” denotes unnormalized states. 

The two Gaussian distributions have mean at _x_ = _±|α_ 0 _|_ and standard deviation being equal to 1. Since, as assumed earlier, _|α_ 0 _| ≫_ 1, the Gaussian distribution with mean at _x_ = + _|α_ 0 _|_ approximately vanishes in the region from _x ∈_ ( _−∞,_ 0) (and similarly in the region: _x ∈_ (0 _, ∞_ ) for the case of the Gaussian distribution with mean at _x_ = _−|α_ 0 _|_ ). Hence, we can approximate that 



With the similar approximation, and tracing out the cavity, the UPM spin states are _|_ Ψ<sup>+</sup> _⟩_<sup>U</sup> _s_<sup>_≈|ϕ⟩_</sup> _es_<sup>and</sup><sup>_|_Ψ</sup><sup>_−⟩_</sup> _s_<sup>U</sup><sup>_≈|ϕ⟩_</sup> _os_<sup>.</sup> 

For even integer _j_ , it is possible to note that 



where the following properties were used _d_<sup>(</sup> _m,_<sup>_j_)</sup> _−j_<sup>(</sup><sup>_−ϕ_) =</sup><sup>_d_(</sup> _−_<sup>_j_</sup> _j,m_<sup>)(</sup><sup>_ϕ_) = (</sup><sup>_−_1)</sup><sup>_m_+</sup><sup>_j d_(</sup> _m,_<sup>_j_)</sup> _−j_<sup>(</sup><sup>_ϕ_)</sup><sup>_._Similarly,</sup><sup>_|ϕ⟩_</sup> _s_<sup>_−|−ϕ⟩_</sup> _s_<sup>= 2</sup><sup>_|ϕ⟩_</sup> _os_<sup>.</sup> Hence, the UPM spin states can be written as 



Using the facts that _R_<sup>_†_</sup> ( _−ϕ_ ) = _R_ ( _ϕ_ ) and _R_ ( _ϕ_ 1) _R_ ( _ϕ_ 2) = _R_ ( _ϕ_ 1 + _ϕ_ 2) , the inner product _⟨−ϕ | ϕ⟩s_ = _d_<sup>(</sup> _−_<sup>_j_</sup> _j,_<sup>)</sup> _−j_<sup>(2</sup><sup>_ϕ_).The</sup> probabilities of the outcomes are then given by the norm of the UPM states: 



A similar analysis can be applied to the second rotation, which gives the rotated UPM states 



16 

||Integer_j_<br>Half-Integer_j_ =_n_+ <sup>1</sup><br>2|Integer_j_<br>Half-Integer_j_ =_n_+ <sup>1</sup><br>2|
|---|---|---|
||even_j_<br>odd_n_|odd_j_<br>even_n_|
|_P_2(_±_)|1<br>2 <sup>_±_ 1</sup><br>2 <sup>(cos 2</sup><sup>_ϕ_)2</sup><sup>_j_</sup>|1<br>2 <sup>_∓_1</sup><br>2 <sup>(cos 2</sup><sup>_ϕ_)2</sup><sup>_j_</sup>|
|_P_1_,_2(_±_+)|3<br>8 <sup>_±_</sup> <sup>1</sup><br>2 <sup>(cos</sup><sup>_ϕ_)2</sup><sup>_j_ + 1</sup><br>8 <sup>(cos 2</sup><sup>_ϕ_)2</sup><sup>_j_</sup>|1<br>8 <sup>_−_1</sup><br>8 <sup>(cos 2</sup><sup>_ϕ_)2</sup><sup>_j_</sup>|
|_P_1_,_2(_±−_)|1<br>8 <sup>_−_1</sup><br>8 <sup>(cos 2</sup><sup>_ϕ_)2</sup><sup>_j_</sup>|3<br>8 <sup>_∓_1</sup><br>2 <sup>(cos</sup><sup>_ϕ_)2</sup><sup>_j_ +</sup> <sup>1</sup><br>8 <sup>(cos 2</sup><sup>_ϕ_)2</sup><sup>_j_</sup>|
|_V±_|_∓_<sup>1</sup><br>4<br>�<br>1_−_(cos (2_ϕ_))<sup>2</sup><sup>_j_�</sup>|_±_ <sup>1</sup><br>4<br>�<br>1_−_(cos (2_ϕ_))<sup>2</sup><sup>_j_�</sup>|



TABLE II: Expressions for probability distributions and the violations of NDC for different _j_ . 

The coupling with the out of resonance cavity in the same CS _|α_ 0 _⟩c_ and with same interaction time _tI_ (recalling that _j_ is even) similarly split the cavity in _|±α_ 0 _⟩c_ . The joint state is then 



Performing the same projective measurement, tracing out the cavity Hilbert space and assuming _|α_ 0 _| ≫_ 1, we have the following UPM spin states, 



where ��Ψ _i,j_ ( _tR_ + _tI_ )�U _s_<sup>denotes the UPM states of the spins when the first and the second measurements give the outcomes</sup><sup>_i_</sup> and _j_ respectively. Hence, the joint probabilities can be computed as follows 



In order to find _P_ 2( _±_ ), we use the probabilities in Eq. (B4) with _ϕ →_ 2 _ϕ_ , as in this case, intermediate measurement is not implemented and only the two rotations are performed one after the other. The violations of the NDC for even integer _j_ are then computed according to Eq. (1) and recover the result claimed in Eq. (12). 

In order to extend this analysis to every _j_ , similar proofs were found for odd and half-integer spins. For odd _j_ , the only difference is that _|ϕ⟩s_ + _|−ϕ⟩s_ = 2 _|ϕ⟩os_ and _|ϕ⟩s −|−ϕ⟩s_ = 2 _|ϕ⟩es_ , leading to _|_ Ψ<sup>_±_</sup> _⟩_<sup>U</sup> _s_<sup>=</sup><sup><u>1</u></sup> 2<sup>(</sup><sup>_|ϕ⟩_</sup> _s_<sup>_∓|−ϕ⟩_</sup> _s_<sup>).The results can</sup> easily be derived following the same proof for even _j_ . 

For spin half-integer, it is possible to rewrite _j_ = _n_ +1 _/_ 2. This changes the entanglement between the cavity out of resonance and the spin in Eq. (B1), according to 



Here _|j, m_ + 1 _/_ 2 _⟩_ is the eigenstate of _Jz_ with eigenvalue _m_ + 1 _/_ 2 for a spin- _j_ system with _j_ being half-integer, where _m_ is an integer and _m ∈{−n −_ 1 _, −n, −n_ + 1 _, · · · , n}_ with _n_ = _j −_ 1 _/_ 2. In this case, even and odd CS are defined as 



Note, the _i_ difference in the cavity states. This motivated the choice of _α_ 0 =<sup><u>1+</u></sup> _~~√~~_ 2<sup>_<u>i</u>|α_0</sup><sup>_|_, ensuring that also for half-integer</sup><sup>_j_, the</sup> projective measurement gives the UPM states _|_ Ψ<sup>+</sup> _⟩_<sup>U</sup> _s_<sup>_≈|ϕ⟩_</sup> _es_<sup>and</sup><sup>_|_Ψ</sup><sup>_−⟩_</sup> _s_<sup>U</sup><sup>_≈|ϕ⟩_</sup> _os_<sup>.The probabilities follows from the norm.</sup> 

### **Appendix C: Deriving the expression of the violation of the NDC when the two arbitrary rotation angles** _ϕ_ 1 **and** _ϕ_ 2 

Let us consider _j_ to be integer. After the first rotation _R_ ( _ϕ_ 1) and first measurement (i.e., at time _t_<sup>(1)</sup> _R_<sup>+</sup><sup>_tI_),theUPMspin</sup> states are 



CC) x > CC) = 5 CC) Xx > | ) ~~|)x~~ 3 (= ) Co ~~E~~ r ~~(Fo~~ ) EEE ~~R~~ E EB E ~~E~~ ( ~~BR~~ N ~~ES~~ NEED NN ~~C~~ I ~~ES~~ I ~~(C~~ EN BN ~~(CR~~ E C ~~-=~~ 0] K ~~t =~~ [ ~~= 1-~~ 9) 

~~-~~ [ 

~~re~~ ~~<u>=1</u> —ET— CEECE~~ ~~<u>— — sr =r =)</u> —~~ ~~<u>=</u> — —nt~~ ~~<u>—</u>~~ 

~~-~~ | 

~~(CD(~~ T ~~)~~ 

| 

) 

( ) 

>. 

19 

where _ρm,n_ are the elements of the density matrix, and _|αm_ ( _t_ ) _⟩c_ = _|e_<sup>_−imχt_</sup> _αm⟩c_ . Hence, it is possible to break the problem into solving the full dynamics for each _ρm,n |αm_ ( _t_ ) _⟩⟨αn_ ( _t_ ) _|c_ element. The additional terms in Eq. (16) were studied in Ref. [105], where it was concluded that under cavity leaking, the coherent states basis evolves according to 



where _|α⟩c , |β⟩C_ are two cavity CSs. 

Now, to compute the full dynamics, we should consider that each _αm_ is a function of _γc_ in addition to _t_ . Let us consider infinitesimal time step _dt_ . On one hand, at every _dt_ , the unitary evolution and the dissipation will update the amplitude of the _m_ CS according to 



respectively. Combining the two, the following differential equation can be formulated and solved 



where the boundary condition _αm_ ( _γc,_ 0) = _α_ 0 was imposed _∀m_ . On the other hand, it is possible to note that the coefficients _ρm,n_ ( _γc, t_ ) will not be effected by the unitary evolution, and only by decoherence following Eq. (E2). At every _dt_ , 



Hence, evolving _ρm,n_ ( _γc,_ 0), 



where, using _⟨α|β⟩_ = exp<sup>_−_</sup> 2<sup><u>1</u>(</sup><sup>_|α|_2 +</sup><sup>_|β|_2</sup><sup>_−_2</sup><sup>_α∗β_), we get</sup> 



Using (E3) and evaluating the integral, Eq. (18) is recovered. Spin dephasing, of decoherence rate _γs_ , can be included in the model by replacing 



Hence, 

In order to keep the discussion general and do not commit to a physical system, we will compute the effect of the decoherence in the measurement probabilities in terms of the ratios _rc_ = _γc/χ_ and _rs_ = _γs/χ_ . 

At first, we assume that _j_ is integer. Substituting _t_ = _tI_ = _π/χ_ in Eq. (17), the density matrix is 



where 



Hence, taking the projection measurement and tracing out the cavity, the UPM spin state is given by: 

where 



>. 

>. 

> 

( ) 

>. ~~~/~~ ) (- -) ) ~~—/~~ K I GR )) 

| 

>. 

>. 

>. 

>. >. <u>s</u> 

( | 



<!-- Start of picture text -->
. i) J=10 . (ii) J =20 . (iii) J = 40 Ve<br>107! 107 107! 020<br>0.15<br>EE 0 Slo Slo<br>0.10<br>| 0.00<br>10+ 10 10<br>10° 102 104 10° 102 104 10° 10° 104<br>Vs Vs Vs<br><!-- End of picture text -->



<!-- Start of picture text -->
( )<br><!-- End of picture text -->

> 

® 

> 

| 

) 

> 

/ ~~—/~~ 

- ~~(~~ C ) 

)) 

| 

~~—)~~ 

) 

> 

> 

> ~~—/~~ [CC 

J ~~-~~ ( 

> ~~-~~ ( 

) ) 

23 

determined by the _z_ -components. In fact, let **E** = **E** _⊥_ + _Ez_ **z** ˆ where **E** _⊥_ = ( _Ex, Ey_ ) are the transverse components and and _Ez_ the propagating component. In this form, Maxwell’s equation in the vacuum implies that and 



where the first identity follows from _Bz_ = 0, _ψ_ is a scalar potential, and the last identity follows from the other Maxwell’s equation, which reads _∇_ **E** = _∇⊥_ **E** _⊥_ + _∂zEz_ = 0. This last Maxwell’s equation can be approached by separation of variables, _Ez_ = _ϕ_ ( _x, y_ ) _Z_ ( _z_ ), and the mode expansion leads to the eigenvalues solution 



where the latter, i.e. the dissipation relation, constrains the wavevector on the _z_ -axis given the frequency of the experiment ( _ω_ ) and the eigenvalues from the _xy_ boundary conditions. Often, as we shall see, this leads to complex values of _kz_ and hence a decay behaviour in the _z_ direction, known as evanescent TM modes. 

The final identity of Eq. (G2), for _ψ_ = _ϕ_ ( _x, y_ ) _f_ ( _z_ ), reads 



explicitly, showing the relationship between the transverse components and the _z_ -components, known as TM identity. 

Let us seek the particular solution under the boundary conditions imposed by the conducting box, i.e. at _x_ = _{−Lx/_ 2 _, Lx/_ 2 _}_ and _y_ = _{−Ly/_ 2 _, Ly/_ 2 _}_ , _Ez_ = 0 _∀z < Lz_ and _Ex, Ey_ = 0 for _z_ = _z_ 0. The former implies that the solutions for the transverse modes inside the box are 



where _E_ 0 is the vacuum electric field, _m_ and _n_ are the labels of the harmonics _ϕmn_ and ( _i_ ), represents the fact that these are quantities inside the box, and _|Az|_<sup>2</sup> + _|Bz|_<sup>2</sup> = 1 (as the normalization is given by _E_ 0). From _Ex, Ey_ = 0 for _x_ = _z_ 0, it is possible to show that _Bz_ = 0 = _⇒ Az_ = 1, as from Eq. (G3), the other components can be computed 



which are indeed zero at _z_ 0 = 0. From the continuity at _z_ = _Lz_ , we require **E**<sup>(</sup><sup>_i_)</sup> ( _x, y, Lz, t_ ) = **E**<sup>(</sup><sup>_o_)</sup> ( _x, y, Lz, t_ ) _∀ t, x, y_ . The outside _z_ component of the field can be taken to be 



such that _k⊥_<sup>(</sup><sup>_o_)=</sup><sup>_k_</sup> _⊥_<sup>(</sup><sup>_i_)=</sup><sup>_k⊥_, as</sup><sup>_ϕmn_(</sup><sup>_x, y_) do not change outside. Additionally, from the other components derived (from Eq. G3)</sup> evaluated at _Lz_ , it is possible to get the ratio 



defining _β_ = _kz_<sup>(</sup><sup>_i_)tan(</sup><sup>_k_</sup> _z_<sup>(</sup><sup>_i_)</sup><sup>_L_</sup> _z_<sup>), which implies an exponential decay outside the resonators, i.e.the field is</sup> 



The chosen parameters of the resonator are _Lx ∼_ 2 _·_ 10<sup>_−_2</sup> m, _Ly ∼_ 8 _·_ 10<sup>_−_6</sup> m, and _Lz ∼_ 2 _·_ 10<sup>_−_7</sup> , such that _V ∼_ 3 _._ 2 _·_ 10<sup>_−_14</sup> m<sup>3</sup> . Taking into account the resonant _ω_ , fundamental to to _Lx_ , i.e. _m_ = _n_ = 1, these values implies that inside the cavity, _kz_<sup>(</sup><sup>_i_)</sup> = � _<u>ωc</u>_<sup>22</sup><sup>_−_</sup> _L_<sup>_<u>π</u>_22</sup> _x_<sup>_−_</sup> _L_<sup>_<u>π</u>_22</sup> _y_<sup>_∼i_</sup> _L_<sup>_<u>π</u>_</sup> _y_<sup>_∼i_4</sup><sup>_·_105, which, for</sup><sup>_z<Lz_is negligible.However, outside the resonator,</sup><sup>_k_</sup> _z_<sup>(</sup><sup>_o_)</sup> _∼ i_ 3 _·_ 10<sup>_−_4</sup> . For a Rygdberg atom placed at _z ≈_ 50 _µ_ m, this implies a decay of a factor of _e_<sup>_−_1</sup><sup>_._5</sup> _∼_ 0 _._ 2. 

Then, the coupling as function of the qubit’s position inside the resonator is approximately given by (omitting the _z_ - dependency for the previous argument) 





<!-- Start of picture text -->
= C =) C 0 )<br>- x — x (— -c 9) ( —)<br>--—<br>22 x<br>I<br>-— === 0<br><!-- End of picture text -->

