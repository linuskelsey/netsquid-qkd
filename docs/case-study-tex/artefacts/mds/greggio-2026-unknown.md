# **Optimal absorption and emission of itinerant fields into a spin ensemble memory** 

Linda Greggio,<sup>1,</sup><sup>_∗_</sup> Tristan Lorriaux,<sup>2</sup> Alexandru Petrescu,<sup>1</sup> Mazyar Mirrahimi,<sup>1</sup> and Audrey Bienfait<sup>2,</sup><sup>_§_</sup> 

> 1 _Laboratoire de Physique de l’Ecole Normale Sup´erieure, Mines Paris, Inria, CNRS, ENS-PSL, Sorbonne Universit´e, PSL Research University, Paris, France_ 

> 2 _Laboratoire de Physique de l’Ecole Normale Sup´erieure de Lyon, France_ 

(Dated: May 6, 2026) 

Quantum memories integrated in a modular quantum processing architecture can rationalize the resources required for quantum computation. This work focuses on spin-based quantum memories, where itinerant electromagnetic fields are stored in large ensembles of effective two-level systems, such as atomic or solid-state spin ensembles, embedded in a cavity. Using a mean-field framework, we model the ensemble as an effective spin communication channel and describe both absorption and emission processes using a cascaded quantum model. We derive optimal time-dependent modulations of the cavity linewidth that maximize storage and retrieval efficiency for fast incoming pulses. Our analysis yields an upper bound on efficiency, which can be met in the narrow bandwidth regime. It also shows the existence of a critical bandwidth above which the efficiency severely decreases. Numerical simulations are presented in the context of microwave-frequency quantum memories interfaced with superconducting quantum processors, highlighting the protocol’s relevance for modular quantum architectures. 

## **I. INTRODUCTION** 

Quantum memories - devices capable of faithfully capturing, storing and retrieving one or more quantum states - are fundamental components in a range of quantum technologies [1]. Their ability to preserve quantum information can enhance long-distance communication [2–4] through quantum repeaters [5], increase the sensitivity of quantum sensors [6, 7] and reduce the resource requirements for quantum computation [8, 9]. Various physical systems can serve as quantum memories, including atomic ensembles [10], solid-state defects [11, 12], molecular gases [13], single-mode oscillators [14, 15], atoms and ions [16, 17]. These systems rely on interactions such as microwave [14], mechanical [15], electronic [10], magnetic [18], or vibrational coupling [11] to store quantum information. This article focuses on one particular approach: storing itinerant electromagnetic fields using the inhomogeneous broadening of an ensemble of effective two-level systems (spins) addressed with a cavity, such as atoms or solid-state defects, and retrieving them using echo-based protocols [19]. Proposals [20– 22] for quantum memories based on inhomogeneouslybroadened spins in a cavity often emphasize operating in a “perfectly matched” regime, where to achieve efficient absorption, the losses induced by the ensemble on the cavity precisely balance the decay rate of the cavity due to its coupling to the input line. This efficiency sweetspot was derived considering “slow” incoming wavepackets, whose bandwidth was considerably smaller than the spin ensemble linewidth, the cavity linewidth, and the cavity to spin ensemble coupling. However, practical quantum memories should be able to exchange information with quantum processors [9] with a high swap 

> _∗_ linda.greggio@inria.fr 

> _§_ audrey.bienfait@ens-lyon.fr 

rate. For absorption-based quantum memory, this requires realizing quantum state transfers (QST) between the memory and the processor qubits with short-duration wavepackets. Between qubits, efficient QSTs require to dynamically control the coupling strength between the communication channel and the emitter node, as well as the receiver node [23–25]. Here, similarly to [26], we show that the same strategy can apply for quantum memories operating with fast incoming pulses. We cast the spinscavity system during the absorption and emission stages of the memory to a quantum cascaded system [27]. This framework allows us to determine the maximum achievable storage efficiency as a function of the memory’s physical parameters and the bandwidth of the incoming quantum signal. Furthermore, we derive the optimal time-dependent modulation of the cavity linewidth that maximizes storage and retrieval efficiency into the spin ensemble for an incoming pulse of arbitrary duration. 

The spin ensemble is characterized by an inhomogeneous linewidth Γ, determined by the frequency distribution of the spins. This linewidth sets both the spectral bandwidth of the memory and the upper bound on its operational speed [19]. Upon absorption, a quantum state becomes rapidly scattered across the internal degrees of freedom of the ensemble. Retrieval protocols are typically based on spin-echo strategies [11, 22, 28, 29], in which an initial magnetization created in the ensemble is refocused by applying pulse sequences that counteract dephasing from inhomogeneous broadening. Successful retrieval is limited by the ensemble’s coherence time _T_ 2. Depending on the spin and its dominant decoherence mechanisms, a variety of refocusing pulse sequences — ranging from simple Hahn echoes to more elaborate multi-pulse schemes — have been developed to extend coherence and thus storage time [30]. The ratio of the temporal duration of the stored signal to the total coherence time offers one metric for a key figure of merit: the quantum memory capacity, which quantifies how many 

2 

distinct temporal modes can be reliably stored. 

In contrast to these refocusing pulses, which impose their own constraints on the physical characteristics of the memory and its operation, optimizing the absorption and emission efficiency primarily depends on achieving sufficient coupling between the spin ensemble and the cavity. In such hybrid systems, the loss rate induced by the spins on the cavity is given by _κ_ s = 4 _g_ ens<sup>2</sup><sup>_/_Γ[31],</sup> where _g_ ens is the collective coupling strength between the cavity and the ensemble. Efficient absorption of slow or continuous signals — those with bandwidths smaller than the inhomogeneous broadening — can be achieved by matching _κ_ s to the cavity’s decay rate _κ_ , assuming this rate to be solely governed by the cavity coupling to the input channel, with no additional intrinsic losses. This has been shown in earlier mean-field analyses [21, 22]. In this article, we extend this line of work to explore the storage and retrieval efficiency of fast itinerant pulses with two primary objectives. First, we aim to increase the storage capacity of the memory. Second, we seek to better characterize the absorption and emission timescales of the memory to compare them to the timescale of typical processing quantum nodes, in the context of modular architectures incorporating quantum memories. Finally, we also include the intrinsic cavity loss in this analysis, which turns out to be an important limiting factor for the efficiency of the protocol. 

As shown in [26] for the absorption step, efficient storage of incoming pulses requires dynamic modulation of the cavity linewidth, mirroring strategies used in itinerant QST for optimal efficiency. We remain within the mean-field theoretical framework developed in earlier works [21, 22], and we leverage this description to model the ensemble as an effective spin communication channel. The channel interacts with a fictitious spin bosonic field with coupling rate Γ, which in turn couples to the cavity with strength _g_ ens . This model reduces the absorption process to a system of two coupled bosonic modes with one mode able to decay into a spin communication channel. In particular, it allows us to formulate and solve analytically an optimization problem to maximize absorption efficiency. Compared to other approaches [26], the emission step naturally emerges as a quantum cascade of the absorption step, with the emitted field into the spin channel driving a future instance of the same twomode system. This enables a similar optimization of the emission process. 

The article is organized as follows: in a first section, we briefly recall the physics of the itinerant absorptionrefocus-retrieve protocol, and introduce the physical system and its interaction structure. In a second part, we map the evolution of this system during the protocol into a quantum cascaded model. From this model, we derive the protocol efficiency in a steady-state operation regime. In Sec. V, we demonstrate that these steady-state efficiencies serve as upper bounds for the more realistic case of finite-length wavepackets, and derive the optimal modulation functions needed to maximize efficiency for 

a given input waveform. Finally, we perform numerical simulations to compute these optimal modulation profiles and analyze the corresponding decrease in efficiency as a function of the incoming signal bandwidth and the cavity’s intrinsic loss. We do so in the particular context of quantum memories implemented at microwave frequencies, and possibly coupled to superconducting quantum processors. 

## **II. PHYSICAL MODEL AND STORAGE PROTOCOL** 

An ensemble of _N_ spins is embedded in a cavity with intrinsic loss rate _κ_ 0, see Fig. 1 **(a)** . The cavity field is described by its annihilation _ε_ ˆ and creation _ε_ ˆ<sup>_†_</sup> operators, and is coupled to a measurement waveguide at a tunable coupling rate _κ_ ( _t_ ). Any spin _j_ of the ensemble, of Larmor frequency _ωj_ , interacts with the cavityˆ at a strengthˆ _gj_ with an interaction Hamiltonian _Hj/_ ℏ = _gj_ (ˆ _εσ_ +<sup>_j_+</sup><sup>_ε_ˆ</sup><sup>_†σ_ˆ</sup> _−_<sup>_j_),where</sup><sup>_σ_ˆ</sup> _−_<sup>_j_and</sup><sup>_σ_ˆ</sup> +<sup>_j_arethespin</sup> lowering and raising operators. The ensemble coupling rate to the cavity is given by _g_ ens<sup>2=</sup> � _p_ ( _g_ ) _g_<sup>2</sup> _dg_ . The derivations that follow do not require any assumption on the shape of the distribution _p_ ( _g_ ). We however assume that the spins are coupled to the electromagnetic field only through the cavity, an hypothesis that is very well verified for spin-cavity system at microwave frequencies. We consider the spin spectral distribution _n_ to be a Lorentzian centered at the mean spin Larmor frequency _ωs_ , i.e. _n_ (∆ _j_ = _ωj − ωs_ ) = 2Γ _π_ <u>Γ4</u><sup>2+∆</sup> <u>1</u><sup>2</sup> _j_<sup>_,_anduncorrelated</sup> with the spin coupling distribution _p_ ( _gj_ ) _._ All spins are assumed to be in their ground state at the beginning of the protocol. 

We consider a simple echo-based protocol proposed in earlier works [21] illustrated in Fig. 1 **(b)** . During the first stage of the protocol, an incoming signal of envelope _ε_ in( _t_ ), at mean Larmor frequency _ωs_ , is absorbed by the spin ensemble. Two refocusing pulses applied at _t_ = _τ_ a and 2 _τ_ a+ _τ_ e let us retrieve this absorbed quantum state at time _T_ E = 2 _τ_ a +2 _τ_ e. The echo occurring between the two refocusing pulses, at time 2 _τa_ , is suppressed by detuning the cavity between the refocusing pulses _τ_ a _< t <_ 2 _τ_ a + _τ_ e [32]. During absorption and emission, the equations of motion (EOMs) of the system in the frame rotating at _ωs_ , read [21] 





where _σ−_<sup>_j_(</sup><sup>_t_)and</sup><sup>_ε_(</sup><sup>_t_)aretheexpectationvaluesofthe</sup> operators _σ_ ˆ _−_<sup>_j_and</sup><sup>_ε_ˆ,while∆cs=</sup><sup>_ωc−ωs_isthedetun-</sup> ing between the cavity and the spin central frequency. 

3 





<!-- Start of picture text -->
R R<br>Absorption<br>Quantum<br>cascade<br>Emission<br><!-- End of picture text -->

FIG. 1. **(a)** Spin ensemble of central frequency _ω_ s and of inhomogeneous broadening Γ coupled with strength _g_ ens to a cavity driven by the input field _ε_ in( _t_ ) _._ The cavity is subject to intrinsic losses _κ_ 0 and interacts with the transmission line through a tunable coupling _κ_ ( _t_ ) _._ The intra-cavity field _ε_ ( _t_ ) and the field in the spin ensemble Σ( _t_ ) describe the dynamics of the stored field. **(b)** Memory protocol: once the incoming field is absorbed, the spins start to dephase. Two refocusing pulses are used to rephase the spins, and an echo is emitted at time _T_ E _._ To avoid the emission of the first noisy echo at 2 _τ_ a, the cavity is detuned between the two pulses. _ε_ out( _t_ ) represents the retrieved field. **(c)** Quantum cascaded formalism: the memory system is represented as two cascaded copies of a two-mode bosonic system. In the absorption copy the incoming field _ε_ in is stored in the spin ensemble, while in the emission copy the spin ensemble is driven by a feedback term Σe,in, representing a filtered version of the absorption output field Σa,out, with filter function specified in the box. 

During emission, there is no input field, i.e. the envelope _ε_ in( _t_ ) = 0. In the above EOMs, we include intrinsic losses for the cavity field without considering any population or phase decays of individual spins, as their coherence time is assumed to be much longer than the duration of the absorption or emission steps. We also do not consider any spin-spin interaction. Finally, in Eq. (2), we have already implemented a mean-field approximaˆ tion. Indeed, its last term should write as _−igj⟨σz_<sup>_jε_ˆ</sup><sup>_⟩_.It</sup> can be simplified through the Holstein-Primakoff approxˆ imation [21, 22, 33] to a factorized product _−igj⟨σz_<sup>_j⟩⟨ε_ˆ</sup><sup>_⟩_.</sup> Since we are considering the incoming field _ε_ in only carries a few photons compared to the large number of spins ( _N >_ 10<sup>4</sup> ) in the ensemble, we expect _⟨σ_ ˆ _z_<sup>_j⟩∼−_1during</sup> absorption. This mean population is also recovered after 

the two refocusing pulses, yielding the simplified form of Eq. (2) we are using. 

## **III. ABSORPTION AND EMISSION** 

## **A. Quantum cascaded model** 

We now cast the interaction of the cavity with the spin ensemble as an interaction with a bosonic mode Σ coupled to a communication channel. To introduce this bosonic mode, we replace the term<sup>�</sup><sup>_N_</sup> _j_ =1<sup>_gjσ_</sup> _−_<sup>_j_in Eq. (1)</sup> with its integrated version � _g_ �∆<sup>_gσ_</sup> _−_<sup>∆</sup><sup>_,gp_(</sup><sup>_g_)</sup><sup>_n_(∆)</sup><sup>_dgd_∆</sup><sup>_._By</sup> integrating the EOM of _σ−_<sup>_j_(Eq.(2))duringtheabsorp-</sup> tion step, we can proceed to the elimination of _σ−_<sup>∆</sup><sup>_,g_</sup> in the above mentioned term, so that it becomes solely dependent on _ε_ a, the cavity mean field during the absorption step (see Sec. A, Eq. (A3)) 



By recognizing the Fourier transform of the Lorentzian function _n_ (∆), we can equalize this term to _ig_ ens Σa( _t_ ), _t_ where Σa( _t_ ) = _g_ ens � _−∞_<sup>_dse−_</sup><sup><u>Γ</u></sup> 2<sup>(</sup><sup>_t−s_)</sup> _ε_ a( _s_ ), with Σa( _−∞_ ) = 0 _._ The variable Σa can also be defined by an EOM: 



We can now rewrite the intra-cavity EOM (Eq. (1)) using Σa, and we obtain a new expression for the dynamics of the cavity 



Eqs. (4) and (5) form a closed set of equations describing the full dynamics of the spin-cavity system during absorption _t < τ_ a. We can also recognize that they correspond to the evolution of the mean-values of two bosonic modes, _ε_ ˆa and Σ<sup>ˆ</sup> a, which interact with strength _g_ ens . Moreover, we can identify the decay rates for each mode: respectively _κ_ 0 and _κ_ a for the cavity field _ε_ a, and Γ for the mode Σa. This decay corresponds to the emission of a fictitious field Σa,out = _√_ ΓΣa into a newly defined spin channel, see Fig. 1 **(c)** . One can intuitively understand the nature of Σa as the field stored in a collective “bright” mode of the spin ensemble, which is maximally coupled to the cavity. However, due to the ensemble broadening, the energy stored in this bright mode rapidly dissipates into “dark” modes, representing the uncoupled degrees of freedom of the spin ensemble. This process corresponds in our model to emission into the spin channel. 

4 

Refocusing techniques, acting as time reversal, permit to recover the initial magnetization created on the spin ensemble. The resulting filtered field will then drive the two bosonic modes system during emission, in a quantum cascade arrangement. To highlight this quantum cascade, we introduce a new cavity variable _ε_ e and new spin variables _σ−_<sup>_j,_eto describe the system during the emis-</sup> sion step ( _t >_ 2 _τ_ a + _τ_ e), obeying respectively the EOMs Eq. (1) (without the driving term) and Eq. (2). Similarly to absorption, we can integrate the EOM of _σ−_<sup>_j,_eto obtain</sup> an expression for the term<sup>�</sup> _gjσ−_<sup>_j,_ethatsolelydepends</sup> on _ε_ a and _ε_ e (see Sec. A, Eq. (A10)), so that the cavity field evolution is given by 



where _κ_ e( _t_ ) is the cavity coupling rate during the emission part. Similarly to the absorption step, we can recognize that the cavity mode interacts at strength _g_ ens with the bosonic mode Σe. As detailed in Sec. A, we find that this bosonic mode is defined by the following EOM 



assuming Σe( _−∞_ ) = _ε_ e( _−∞_ ) = 0. Here, Σe,in corresponds to a drive field for this new spin bosonic mode. It corresponds to a filtered version of Σa,out given by Σe,in = _√_ ΓΣ<sup>˜</sup> a( _T_ E _− t_ ), where Σ<sup>˜</sup> a is defined by the following EOM (see Appendix A) 



with Σ<sup>˜</sup> a( _−∞_ ) = 0. By exploiting the symmetry in Eqs. (4) and (8), we can express the filter function _H_ between the emitted spin field during absorption Σa,out, and the incoming spin drive field during emission Σe,in as 



Using Eqs. (4) to (7), we identify a quantum cascaded system [27, 34] represented in Fig. 1 **(c)** : the two interacting bosonic modes _ε_ a and Σa, driven by a cavity drive _ε_ in and emitting a spin field Σa,out, govern the dynamics of the two interacting bosonic modes _ε_ e and Σe through the spin drive Σe,in. In Fig. 2, we compute the response of the system to an incoming pulse of various bandwidths. We show that a slow pulse is perfectly absorbed when ensuring the cavity is _matched_ to the spin ensemble (4 _g_ ens<sup>2</sup><sup>_/_(</sup><sup>_κ_aΓ)=1,whileforafasterpulse,the</sup> reflected field is non-zero, indicating an imperfect absorption. 

## **B. Efficiency definition** 

We define the efficiency of the absorption step as the ratio between the energy transferred from the drive field 



<!-- Start of picture text -->
(a)<br>1.0 α=0.12Γ<br>0.8 α=0.25Γ<br>α=0.45Γ<br>0.6<br>0.4<br>0.2<br>0.0<br>(b) 40 20 0 20 40<br>1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>40 20 0 20 40<br>Time t/Γ<br>out<br>, ε<br>in<br>ε<br>a<br> Σ,<br>a<br>ε<br><!-- End of picture text -->

FIG. 2. Response of the coupled spin-cavity system during the absorption step in case of a cosecant input pulse ~~�~~ _a/_ 2 _/_ cosh( _αt_ ) of increasing bandwidth _α_ derived through Eqs. (4) and (5) with a uniform cavity coupling rate _κa_ chosen to match the cavity-spin system to 1 (4 _g_ ens<sup>2</sup><sup>_/_(Γ</sup><sup>_κ_</sup> _a_<sup>)=1).</sup> We take _g_ ens _/_ Γ = 0 _._ 5 and _κ_ 0 _/_ Γ = 1 _/_ 30. **(a)** Input (solid) and reflected (dashes) cavity field. **(b)** Intracavity (solid) and spin (dashes) fields. 

_ε_ in to the field stored inside the spin ensemble, and the energy of that drive field 



Similarly, the efficiency of the emission step is given by the ratio of the energy transferred from the spin field, Σe,in, to the energy of the field emitted by the cavity _ε_ e,out = ~~�~~ _κ_ e( _t_ ) _ε_ e, namely 



where the integrals are understood to run over _t ∈_ ( _−∞, ∞_ ) (Sec. A). The overall efficiency of the protocol is given by _η_ = _η_ a _× η_ H _× η_ e, where _η_ H corresponds to the filter effect given by the refocusing pulses Eq. (9), i.e. _η_ H = <u>��</u> _dtdt|_ Σ _<u>|</u>_ Σa,oute,in(( _tt_ <u>))</u> _<u>||</u>_<sup>22.Here,weconsiderperfectrefocusing</sup> pulses, namely _η_ H = 1. 

Next, in Sec. IV, we derive the absorption and emission efficiencies _η_ a and _η_ e for a slow-pulse limit of the quantum cascaded system, as closed-form expressions in terms of the physical parameters _g_ ens , _κ_ 0 and Γ. We 

5 

will then show that these efficiencies represent an upper bound when considering faster pulses in Sec. V. 

## **IV. MEMORY EFFICIENCY IN THE CONTINUOUS-DRIVE LIMIT** 

In this section, we consider the quantum cascaded model driven by a continuous-wave drive, with a constant coupling rate _κ_ . We are interested in this steady-state behavior to derive the optimal value of _κ_ , as a function of the physical parameters _g_ ens , Γ and _κ_ 0, which maximizes the energy transmitted to the spins and then remitted by refocusing, or equivalently the efficiency _η_ defined above. The limit we derive here is a “slow-pulse” limit, which corresponds to pulses whose bandwidth is much narrower than the system bandwidth. While this limit might not be very useful in practice, as the pulse length should be much shorter than the coherence time of the quantum system generating it, it will provide a useful upper bound for _η_ in the case of realistic finite-length pulses, as treated in the next Sec. V. 

We define the following transmission coefficients associated with absorption and emission 



with _t_ a being the transmission coefficient from the driveline to the spins, while _t_ e is the transmission coefficient from the spins back to the driveline. Note that these transmission coefficients are related to the transmissivities of the spin-cavity channel _|t_ a _|_<sup>2</sup> _, |t_ e _|_<sup>2</sup> [35]. Using the EOMs for absorption and emission written in the frequency domain, these transmission coefficients are, in the Fourier domain, (see Sec. B) 



with frequency dependence given by _κ_ ˜s _/κ_ s = 1 _− δ_ ( _δ_ + ∆cs) _/g_ ens<sup>2and</sup><sup>_δ/δ_˜=1 + (</sup><sup>_κ_0+</sup><sup>_κ_</sup> a/e<sup>)</sup><sup>_/_Γ.Inabsenceof</sup> modulation, with constant coupling rate to the input line, the absorption and emission are described by a reciprocal linear system, so that the transmission coefficients _|t_ a _|_ and _|t_ e _|_ are symmetric under an interchange a _↔_ e. 

The efficiencies defined in Eqs. (10) and (11) can then be rewritten as a function of the transmission coefficients, by making use of Eq. (12) and of Parseval’s theorem to pass to the frequency domain 



From these expressions for the efficiencies, it is clear that an optimization of the memory protocol comes from a maximization of the transmissivities _|t_ a _|_<sup>2</sup> , and 

_|t_ e _|_<sup>2</sup> . To this end, we first maximize the transmissivities, as obtained from Eq. (13), at each frequency value _δ_ , with respect to ∆cs _,_ finding the optimal ∆<sup>_∗_</sup> cs<sup>[</sup><sup>_δ_]=</sup> _κ_ s _<u>/</u>_ Γ<sup>_−_1</sup> _δ._ Then, we evaluate the transmissivity � 1+4( _δ/_ Γ)<sup>2</sup> � at ∆<sup>_∗_</sup> cs<sup>,andmaximizeitwithrespectto</sup><sup>_κ_</sup> a/e<sup>,toob-</sup> tain equal values for emission and absorption _κ_<sup>_∗_=</sup> a/e<sup>[</sup><sup>_δ_]</sup> _κ_ 0 + 1+4( _<u>κδ/</u>_ <u>s</u> Γ)<sup>2</sup><sup>_,_leadingthentoequaloptimaltransmis-</sup> sivities _|t_ a/e[ _δ_ ] _|_<sup>2</sup> = _κ_ s+ _κ_ 0+4 _<u>κκ</u>_ <u>s</u> 0( _δ/_ Γ)<sup>2.</sup> Finally, these are clearly maximized for _δ_<sup>_∗_</sup> = 0. We thus find that the sweet spot for the quantum memory protocol occurs at zero frequency, i.e. for constant input _ε_ in( _t_ ) = _ε_ in, leading to zero detuning ∆<sup>_∗_</sup> cs<sup>=0,and</sup><sup>_κ∗_</sup> a/e<sup>=</sup><sup>_κ_0+</sup><sup>_κ_s,a</sup> coupling rate that maximizes both the transmission from the driveline to the spins and the transmission from the spins back to the driveline. 

The transmission coefficients at this sweet spot are then constant in time and read 



while the protocol efficiency is 



This expression highlights that the quality of the memory is given by the ratio _κ_ s _/κ_ 0, which describes how well the cavity is coupled to the spins compared to its coupling to the environment. Fig. 3 shows the transmissivity at zero detuning as a function of the coupling rate _κ_ a/e (panel **(a)** ) and of internal losses _κ_ 0 (panel **(b)** ) for increasing values of _g_ ens _/_ Γ. In panel **(a)** the crosses mark the sweet spot _κ_<sup>_∗_</sup> a/e<sup>=</sup><sup>_κ_0 +</sup><sup>_κ_sat</sup><sup>_κ_0</sup><sup>_/_Γ = 1</sup><sup>_/_30</sup><sup>_,_whilethetransmis-</sup> sivity depicted in panel **(b)** is evaluated at the sweet spot _κ_<sup>_∗_Moreover,panel</sup><sup>**(b)**showsthateveninthis</sup> a/e<sup>.</sup> case of optimal energy transfer, the cavity internal losses have a detrimental effect on the transmissivity, which can be overcome by increasing the coupling rate between the spins and the cavity, i.e. _κ_ s _._ The gain in transmissivity for larger _κ_ s is also clear in the other panel. 

Along with the transmitted energy comes the reflected energy, which is associated with the reflection coefficients _r_ a = _ε_ a,out _/ε_ in back to the driveline and _r_ e = Σe,out _/_ Σe,in back to the spins. Their expressions are presented in Sec. B (see Eq. (B5) and Eq. (B8)), and if we evaluate them at the transmission sweet spot ( _κ_<sup>_∗_</sup> a/e<sup>,</sup><sup>_δ∗_and ∆</sup> cs<sup>_∗_) we</sup> find _r_ a = 0, i.e. the incoming drive is perfectly absorbed and _r_ e = _κ_ 0 _<u>κ</u>_ +0 _κ_ s<sup>.Thismeansthateveninthecaseof</sup> optimal energy transfer, some energy remains within the spins during emission. At the optimal operation point for constant coupling rate, the cooperativity of the system is _C_<sup>_∗_</sup> = Γ( _κ_ 40 _<u>g</u>_ +ens<sup>2</sup> _κ_<sup>_<u>∗</u>_</sup> a/e<sup>)=</sup> (2 _κ_ 0 _<u>κ</u>_ +s _κ_ s)<sup>_≤_1,givingtheefficiencyoftheprotocolas</sup> 



6 



<!-- Start of picture text -->
(a) (b)<br>1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>10 -1 10 0 10 1 5 10 15<br>a/e /Γ 0 /Γ<br>2||t/ea<br><!-- End of picture text -->

FIG. 3. Transmissivity in the continuous-drive limit, when the cavity, the spins and the drive are all at resonance, as a function of cavity-driveline coupling ( **(a)** ), and of internal losses ( **(b)** ), for three different values of _g_ ens _/_ Γ (0 _._ 2 green, 1 blue, 2 red curve). In **(a)** the internal losses decay rate is fixed to _κ_ 0 _/_ Γ = 1 _/_ 30. The crosses correspond to the optimal coupling _κ_<sup>_∗_</sup> a/e<sup>=</sup><sup>_κ_0+</sup><sup>_κ_s,whichindeedmaximizesthetrans-</sup> missivity. In **(b)** the coupling is set to its optimal value _κ_<sup>_∗_</sup> a/e<sup>,</sup> showing that the detrimental effect of intrinsic losses can be mitigated by increasing the coupling between the spins and the cavity. 

Unit efficiency is thus achieved under unit cooperativity (the so-called impedance matching condition [21]), whenever the intrinsic losses of the cavity can be neglected. 

notations, the EOMs describing emission write 



while the EOMs for the absorption process are 



## **A. Optimizing absorption** 

Instead of fixing the shape of the incoming pulse _E_ in( _τ_ ), for simplicity, we equivalently fix the shape of _S_ a( _τ_ ), such that the energy emitted into the spin ensemble equals 1. In this way, the shapes of _E_ a and _E_ in can be found by the absorption EOMs (19) and can be expressed in terms of _S_ a( _τ_ ) and its derivatives _S_<sup>˙</sup> a( _τ_ ) and _S_<sup>¨</sup> a( _τ_ ), as well as _κ_ ¯a( _τ_ ). This last function is the only remaining degree of freedom that we would like to determine by solving an optimization problem which maximizes the absorption efficiency _η_ a = <u>��</u> _dτdτ|E|S_ ina(( _ττ_ <u>))</u> _<u>||</u>_<sup>22</sup><sup>_._</sup> 

Specifically, this optimization problem can be formulated as follows. For a given _S_ a such that � _dτ |S_ a( _τ_ ) _|_<sup>2</sup> = 1, solve 



## **V. OPTIMAL MEMORY EFFICIENCY FOR TEMPORAL PULSES** 

We now wish to derive the temporal modulation of the coupling strengths during absorption, _κ_ a( _t_ ), and emission, _κ_ e( _t_ ), which optimize the storage efficiency of the memory _η_ = _η_ a _× η_ e for an incoming pulse _ε_ in( _t_ ). Based on the continuous-drive limit we derived above, we assume that the optimal spin-cavity detuning remains similar, and we consider ∆cs = 0 in this section. Consequently, all the field variables are real. Before describing the optimization problem, we perform a time rescaling _τ_ = Γ _t_ : _δ_<sup>¯</sup> = _δ/_ Γ, _κ_ ¯0 = _κ_ 0 _/_ Γ, _κ_ ¯s = _κ_ s _/_ Γ, g = _g_ ens _/_ Γ, _κ_ ¯( _τ_ ) = _κ_ ( _τ/_ Γ) _/_ Γ, _T_<sup>¯</sup> E = Γ _T_ E. The resulting equations are dimensionless and describe the memory protocol dynamics in units of the spin decay rate Γ, which sets a natural time scale for storage into the memory system. We denote the cavity and spin fields _ε_ a/e( _τ/_ Γ) and Σa/e( _τ/_ Γ), as well as the input drive fields for absorption _ε_ in( _τ/_ Γ) and emission Σ<sup>˜</sup> _a_ ( _τ/_ Γ), all functions of the rescaled time _τ_ , by _E_ a/e( _τ_ ), _S_ a/e( _τ_ ), and _√_ Γ _E_ in( _τ_ ), _S_ in( _τ_ ). With these 

Noting that by Eq. (19) _E_ in = _A_ [ _S_ a _, S_<sup>˙</sup> a _, S_<sup>¨</sup> a] _/_<sup>_√_</sup> _<u>κ</u>_ <u>¯a</u> + _√κ_ <u>¯a</u> _<u>B</u>_ [ _S_ a _, S_<sup>˙</sup> a _, S_<sup>¨</sup> a] with 



we can re-express the optimization problem as 



whose optimal solution is clearly given by 



Now, given the optimal solution _κ_ ¯<sup>_∗_</sup> a<sup>,dependingonthe</sup> choice of _S_ a, we aim to derive an upper bound on the 

7 

absorption efficiency, that is, a lower bound for the functional in (20). Using the functions _A_ ( _t_ ) and _B_ ( _t_ ) decomposing _κ_ ¯<sup>_∗_</sup> a<sup>,wecanexpresstheoptimalvalueofthe</sup> functional as 



The integrand �� _<u>BA</u>_ ��� _A_ + _B_ �� _BA_ ���2 can be rewritten as 2 _|AB|_ + 2 _AB_ which is lower bounded by 4 _AB_ . Using the definitions of _A_ and _B_ in Eq. (21), we can show that (see Sec. C) 



Using Parseval’s theorem, this inequality is equivalent to 



which is lower bounded by _<u>κ</u>_ 2s _πκ_ <u>+</u> _<u>κ</u>_ s0 � _dδ_<sup>¯</sup> _|S_ a[ _δ_<sup>¯</sup> ] _|_<sup>2</sup> . We recall that we have assumed 21 _π_ � _dδ_<sup>¯</sup> _|S_ a[ _δ_<sup>¯</sup> ] _|_<sup>2</sup> = 1 _,_ which implies that the absorption efficiency _η_ a is directly upperbounded by 



As seen before, this upper bound corresponds to the maximal absorption efficiency Eq. (16) found in the case of constant _κ_ a for an adiabatic incoming pulse. 

## **B. Optimizing emission** 

Now that we have found the profile of _κ_ ¯a that realizes the maximal transfer of energy from the driveline to the spins, we aim to find the profile of _κ_ ¯e that permits the maximal transfer of energy from the spins back to the driveline, namely we want to maximize _η_ e = <u>�</u> _dτ_ <u>�</u> _dτ_ ¯ _κ_ e _|S_ <u>(</u> _τ_ in) _<u>|E</u>_ ( _τ_ e)( _|τ_<sup>2</sup> <u>)</u> _<u>|</u>_<sup>2</sup> _._ 

To this end, we first express the denominator � _dτ |S_ in( _τ_ ) _|_<sup>2</sup> using our knowledge of the absorption step. Through Eq. (9), we can show that _S_ in( _δ_<sup>¯</sup> ) = _H_ [Γ _δ_<sup>¯</sup> ] _S_ a( _δ_<sup>¯</sup> ). Given that we have assumed perfect refocusing pulses, i.e. _|H|_ = 1, we have � _dτ |S_ in( _τ_ ) _|_<sup>2</sup> = � _dτ |S_ a( _τ_ ) _|_<sup>2</sup> = 1. Similarly to the absorption problem, maximizing the emission efficiency thus reduces to maximizing _E_ out = � _dτ_ ¯ _κ_ e( _τ_ ) _E_ e( _τ_ )<sup>2</sup> . 

Rewriting the second Eq. (18) as g _E_ e = _S_<sup>˙</sup> e +<sup><u>1</u></sup> 2<sup>_S_e</sup><sup>_−_</sup> _S_ in _,_ and manipulating Eq. (18) as shown in Sec. C, it is possible to eliminate the dependence of _E_ out on _κ_ ¯e _,_ 

so that _E_ out is simply expressed as a function of _S_ e, its derivatives, and _S_ in 



Furthermore, note that, following Eq. (18), we have 



Therefore, the optimization problem can be written as a maximization of the output energy (28) as a function of _S_ e, under the constraint 



This constraint can be written in the following form 



with 



Therefore, the constraint can be seen as the union of two convex sets. It is possible to solve each of these convex optimization problems under constraints using an appropriate iterative algorithm, such as the Uzawa algorithm for finding the saddle point of the associated Lagrangian, and then compare the maximal values in each set to find the global maximum under constraints. 

Here, for simplicity, we have decided to relax the constraint, find the unconstrained optimal output energy, and finally check if this optimal solution actually satisfies the constraint. To this end, using Parseval’s theorem, we re-express the output energy in Eq. (28) as 



The corresponding optimal spin field (without constraint) is given by 



Using the second equation in (18), we can also deduce the optimal cavity field 



8 

while using the first Eq. (18) we can determine the corresponding optimal cavity bandwidth modulation 



where _F_<sup>_−_1</sup> stands for the inverse Fourier transform. 

In the absence of internal loss, _κ_ 0 = 0, we find _S_ e<sup>_∗_=</sup> _S_ in, _E_ e<sup>_∗_=</sup><sup>_−E_a(</sup><sup>_τ −T_¯</sup><sup>_E_), corresponding to an emission effi-</sup> ciency of 1. However, we have to check if the corresponding cavity bandwidth modulation satisfies the positivity constraint, i.e. that _κ_ ¯<sup>_∗_</sup> _e_<sup>givenasfollowsispositiveforall</sup> times (for _κ_ 0 = 0) 



At this point, we again consider the case of nonvanishing internal loss _κ_ ¯0 _>_ 0, and we derive an upper bound for the emission efficiency _η_ e. We plug in the general expression of _S_ e<sup>_∗_derivedinEq.(33)intheoutput</sup> energy (32), which yields 



This provides an upper bound for the emission efficiency as no positivity constraint on _κ_ ¯ _e_ is imposed. This bound is actually saturated when Eq. (35) remains positive for every time _τ_ . 

Now, let us go even further and note that from the above equation we obtain 



with the inequality a consequence of 21 _π_ � _dδ_<sup>¯</sup> _|S_ in _|_<sup>2</sup> = 1. We thus have _η_ e _≤ κ_ 0 _<u>κ</u>_ +s _κ_ s<sup>,whichtogetherwiththepre-</sup> viously derived bound (27) gives 



As for absorption, this upper bound on absorption and re-emission efficiency is reached in the limit of adiabatic input drives and with a constant modulation _κ_ a/e (see Eq. (16)). This limit is entirely governed by the amount of cavity intrinsic losses compared to the spin-induced losses. In the following section, we perform numerical simulations to evaluate the efficiency cost in using pulses whose bandwidth lies beyond this adiabatic limit. 

## **VI. NUMERICAL SIMULATIONS** 

From Sec. V, we can derive not only upper bounds on the efficiency but also determine the optimal modulation of the cavity coupling rates _κ_ ¯<sup>_∗_</sup> a<sup>and</sup><sup>_κ_¯</sup><sup>_∗_</sup> e<sup>(see Eqs. (23)</sup> and (35)), as well as the corresponding input drive _ε_ in( _t_ ), 

given a fixed shape for the occupancy of the spin field mode Σa. By considering a particular wavepacket shape _u_ ( _α_ Γ _t_ ), we can then derive the expected efficiency as a function of the wavepacket bandwidth _α_ Γ. Although this analysis does not allow us to identify an optimal pulse shape for a given bandwidth, it lets us quantify the reduction in efficiency in operating the quantum memory for this specific pulse shape given this bandwidth. From this study, we wish to extract the minimal wavepacket duration _τ_ in<sup>_∗_beyondwhichareductioninefficiencyoc-</sup> curs, and compare it with two key metrics for a quantum memory. First, comparing _τ_ in<sup>_∗_tothememorystorage</sup> time (given by the ensemble coherence time _T_ 2) provides an estimate of the capacity of the memory, i.e. the number of temporal modes it can potentially store. Second, in the context of a modular architecture, this wavepacket will realistically be emitted by a qubit. For a quantum memory to be pertinent in such an architecture, _τ_ in<sup>_∗_must</sup> be short compared to the qubit lifetime to not limit the itinerant transfer between the qubit and the memory. 

## **A. Physical parameters** 

We wish to realize this temporal analysis in the particular context of quantum memories operating at microwave frequencies that may eventually be coupled to superconducting quantum bits. The most promising spin candidates for these memories are, for example, donors in silicon [36] or rare-earth ions [37]. These spin systems are attractive candidates since they possess clock transition “sweetspots” where the decoherence created by spin-spin interactions is canceled [38]. For example, at these particular operating points, bismuth donors in silicon achieve _T_ 2<sup>Bi</sup> _≈_ 1 s [36], ytterbium ions in yttrium orthosilicate yield _T_ 2<sup>171 Yb:Y2SiO5</sup> = 4 ms [39] and the same ions in scheelite _T_ 2<sup>171 Yb:CaWO4</sup> = 0 _._ 15 s [40]. Very strikingly, the last system exhibits this coherence time in the absence of a biasing magnetic field. These spin coherence times compare favorably to present-day record coherence time for superconducting qubits ( _≈_ 1 ms), and even more favorably for qubits inserted in large-scale superconducting quantum processors or for qubits in quantum state transfer experiments where the achievable coherence time is rather about _∼_ 0 _._ 02 ms [41, 42]. 

Using an ensemble of these spins for implementing a microwave quantum memory will rely on patterning a superconducting microwave resonator implementing the cavity on top of the crystal containing the spins [29, 43] or placing this crystal on top of another substrate on which the resonator is patterned [30]. In the former case, the strain induced by the superconducting film on the crystal can broaden the spin inhomogeneous linewidth (which may already be sizable) to Γ _/_ (2 _π_ ) _∼_ 10 MHz, whereas in the latter geometry one may hope to be closer to its natural values, which can be as low as 5 kHz for<sup>171</sup> Yb : CaWO4 for instance [40]. The particular choice of geometry for the superconducting resonator, 

9 

combined with the particularities of the spin systems and the concentration of spins, sets the ensemble coupling constant [44]. For example, donors in silicon samples cannot be too heavily doped, so will reach a more limited coupling constant _g_ ens _/_ (2 _π_ ) _∼_ 100 kHz [43, 45] than for example some rare-earth ions where an ensemble coupling strength in the range of 4 MHz have been observed [31]. Overall, depending on the particular set of experimental conditions, the ratio _g_ ens _/_ Γ can take values between 0 _._ 02 and 200. However, let us note that the larger ensemble coupling constants are typically reached using high-spin concentrations, which limit the coherence time achievable at the clock-transition through second-order spinspin interactions [36], so that a more reasonable upper bound for _g_ ens _/_ Γ would be _∼_ 10. These parameters correspond to spin-induced losses on the cavity of the order of _κ_ s _/_ (2 _π_ ) = 1 kHz to 10 MHz. 

Let us now focus on the achievable cavity decay rates. For intrinsic losses, when the resonator is patterned on high-grade microwave substrates such as sapphire or silicon, decay rates as low as _κ_ 0 _/_ (2 _π_ ) = 10 kHz may be achieved [46]. When using a spin-doped crystal made of other materials, more realistic values _κ_ 0 _/_ (2 _π_ ) up to _∼_ 300 kHz should be considered. The ratio _κ_ 0 _/_ Γ can thus take values from 1 _×_ 10<sup>_−_4</sup> up to 30. The derivation of Sec. IV makes clear that the coupling rate of the cavity to the input line should at minima match _κ_ 0 + _κ_ s. We assume in the following that this is the case and that no limitation will come from limited coupling to the measurement line. Experimentally, this would imply modulating _κ_ from less than 10 kHz to more than 10 MHz. This has already been achieved for superconducting resonators using Josephson junctions [47, 48], and can also be done on a smaller range with kinetic inductance when the resonator should be operated in a magnetic field [49, 50]. Using these two techniques, modulating the resonator linewidth can be done with high precision for a broad range of desired shapes, with a response time of less than 10 ns. 

## **B. Wavepacket: hyperbolic secant case** 

To dictate the choice of the wavepacket Σa( _t_ ) that we will consider in the rest of the study, we remark that the optimal shape for _κ_ a is given by a ratio of the derivatives of Σa( _t_ ), and by a ratio of Fourier transforms for _κ_ e. Using a wavepacket that is not at least twice differentiable, with a well-behaved Fourier transform, is thus not advised. In practice, we consider an hyperbolic secant pulse Σa( _t_ ) = � _α/_ 2 _/_ cosh( _α_ Γ _t_ ) normalized to unity. In Sec. D, we also perform the study for a Lorentzianshaped wavepacket, which gives a higher requirement for the maximum coupling rate _κ_ max, and which performs worse in terms of efficiency compared to the hyperbolic secant pulse. The bandwidth of the input pulse is _α_ Γ, meaning that the spins are capable of absorbing all the frequency components of the input field within the en- 

semble linewidth Γ if _α ≤_ 1. 

To perform numerical simulations, we use this wavepacket to compute _κ_ ¯<sup>_∗_</sup> a<sup>using Eq. (23).We then com-</sup> pute the input field _E_ in and the cavity field _E_ a through the EOMs (19). 

For the emission process, we compute the dynamics in the frequency domain using Eqs. (33) and (34), and then apply the inverse Fourier transform to obtain the time-domain evolution. The associated modulation of the coupling through Eq. (35) leads to maximal emission efficiency, but does not take into account the positivity constraint on _κ_ ¯<sup>_∗_</sup> e<sup>(</sup><sup>_τ_).</sup> When this constraint is violated, as occurs for pulse speeds _α ≥ α_ em<sup>_∗_,theoutputfield</sup> _E_ e,out =<sup>_√_</sup> _<u>κ</u>_ <u>¯e</u> _<u>E</u>_ e becomes ill-defined. To address this issue in the fast-pulse regime ( _α ≥ α_ em<sup>_∗_), where Eq. (35) yields</sup> negative values for the modulated coupling, we instead adopt a suboptimal but physical modulation: we mirror the absorption profile, setting _κ_ e( _t_ ) = _κ_ a( _T_ E _− t_ ), which aligns with the time-reversed interpretation of emission in the quantum cascade formalism. We then compute the cavity field _E_ e, the spin field _S_ e through the EOMs (18). The feedback term _S_ in is evaluated in the frequency domain as _S_ in( _δ_<sup>¯</sup> ) = _H_ [Γ _δ_<sup>¯</sup> ] _S_ a( _δ_<sup>¯</sup> ), then Fourier transformed back to the time domain. Finally, we compare the associated emission efficiency with the upper bound given by Eq. (37). This upper bound is saturated for pulse speeds _α < α_ em<sup>_∗_.</sup> 

Numerical results for the cavity and spin field, as well as the modulated coupling rates, are presented in Fig. 4 for four values of the bandwidth _α_ = 0 _._ 12 _,_ 0 _._ 25 _,_ 0 _._ 46 and 0 _._ 69. For this set of parameters, we find _α_ em<sup>_∗_=0</sup><sup>_._5.In</sup> the small bandwidth limit ( _α_ = 0 _._ 12, green), the coupling rate approaches its “slow-pulse” optimal value _κ_ 0 + _κ_ s (black dotted line), and the numerically-determined efficiency ( _η_ = 93 _._ 5%) comes close to the adiabatic upper bound ( _η_ = 93 _._ 7%). Even at intermediate bandwidth ( _α_ = 0 _._ 25), there is little loss in efficiency ( _η_ = 93 _._ 2%). The input and outgoing cavity fields also closely resemble hyperbolic secant pulses. As we consider faster pulses, the optimal coupling modulations for absorption and emission lose in smoothness, and their minimum gets closer to 0. Similar to emission, we define the bandwidth _α_ abs<sup>_∗_atwhichacancellationpointappearsintheopti-</sup> mal absorption coupling _κ_<sup>_∗_</sup> a<sup>(</sup><sup>_t_).Weobservethatjustbe-</sup> low this limit ( _α_ = 0 _._ 46), the efficiency is still quite high ( _η_ = 92 _._ 0%). When switching to higher speed ( _α_ = 0 _._ 69, beyond even the definition region of _κ_ ¯<sup>_∗_</sup> e<sup>),theabsorption</sup> efficiency is largely impacted ( _η_ abs = 74 _._ 9%), evidencing a trade-off between the pulse bandwidth and its storage efficiency even though the optimal modulation function is still defined. We also see that the input pulse is considerably deformed and is rather akin to a simple exponential wavepacket. For emission, we observe that taking the suboptimal choice _κ_ e( _t_ ) = _κ_ a( _T_ E _− t_ ) also leads to a rather limited efficiency ( _η_ em = 61 _._ 0%), leading to a total efficiency of _η_ = 45 _._ 7%. 

10 



<!-- Start of picture text -->
(a) (b) (c) (d)<br>Σa(Γt) Σe(Γt) εin(Γt) εe, out(Γt) a (Γt) e (Γt) 20 a (Γt) e (Γt)<br>η = 93.5%<br>10<br>η = 93.2%<br>0.5<br>η = 92.0% 10<br>η = 45.7%<br>5<br>0.0<br>0<br>α=0.12 αα=0.46=0.46<br>α=0.25 αα=0.69=0.69<br>0.5 0<br>10<br>-20 0 20 -20 0 20 -20 0 20 -20 0 20 -20 0 20 -20 0 20 -20 0 20 -20 0 20<br>Γt Γ(t − TE) Γt Γ(t − TE) Γt Γ(t − TE) Γt Γ(t − TE)<br><!-- End of picture text -->

FIG. 4. Numerical simulations results for a hyperbolic secant pulse, with system parameters _g_ ens _/_ Γ = 1 _/_ 2 and _κ_ 0 _/_ Γ = 1 _/_ 30 _,_ corresponding to critical speeds _α_ abs<sup>_∗_=0</sup><sup>_._474and</sup><sup>_α_</sup> em<sup>_∗_= 0</sup><sup>_._5.Wecompareaslow-adiabaticcase(</sup><sup>_α_= 0</sup><sup>_._12),withfasterpulses</sup> just below ( _α_ = 0 _._ 46) and above _α_ = 0 _._ 69 these thresholds. **<u>(a)</u>** Field stored in the spins during absorption and emission (dimensionless). **(b)** Incoming and retrieved field (in units of _~~√~~_ Γ); evaluated using _κ_ e( _t_ )<sup>_∗_</sup> when defined, and _κ_ a( _TE − t_ ) when not (dashed-dot yellow curve). **(c)** - **(d)** Optimal modulation for cavity-driveline coupling during absorption (see Eq. (23)) and emission (see Eq. (35)) in units of Γ. As _α_ is increased, getting away from the “slow-pulse” limit (black-dotted line), efficiency decreases (printed in **(b)** ). At high speed ( _α >_ 1 _/_ 2), the denominator of Eq. (23) vanishes near _t_ = 0, creating a singularity in _κ_ a( _t_ ). A similar divergence occurs for _κ_ e( _t_ ) near _T_ E, accompanied by an unphysical modulation (crossing of the zero). 

## **C. Efficiency as a function of pulse bandwidth and intrinsic losses** 

Restricting our analysis to hyperbolic secant pulses, we first study the efficiency of the absorption process as a function of the wavepacket bandwidth _α_ Γ without (Fig. 5 **(a)** ) and with intrinsic losses (Fig. 5 **(b)** ). In both cases, we observe that the efficiency lies close to the slowpulse limit (Eq. (16)) up to some critical bandwidth value after which the efficiency drops considerably. We observe that the intrinsic losses, which irremediably lower the slow-pulse efficiency, seem to have a marginal effect on this bandwidth limitation. As we observed in Fig. 4, this drop in efficiency ties to the optimal modulation shape derived in Eq. (23), which expresses _κ_<sup>_∗_</sup> a<sup>(</sup><sup>_t_) as the absolute</sup> value of the ratio of _A_ over _B_ , where _A_ and _B_ are linear combinations of derivatives of the considered wavepacket. In our optimization problem, we only consider _A_ = 0 and _B_ = 0, which are non-zero at all times. At low speed, we find that _A/B_ is always positive, so that the absolute value does not play any role, and _A_ and _B_ are far from canceling at any point in time. In this case, Eq. (24) has a closed-form solution, which gives us an analytical expression of the absorption efficiency 



Noting that 

The maximum limit for speed comes from having the denominator well-defined and non-zero at all times, which 

corresponds here to _α <_ 1 _/_ 2. Even below this limit, the nominator may present a cancellation point that would activate the absolute value. We find that after this critical speed _α_ abs<sup>_∗_(represented by black crosses in Fig. 5</sup><sup>**(b)**),</sup> the optimal efficiency drops significantly due to this lack of a smooth control function, and Eq. (40) gives just an upper bound for _η_ abs. For hyperbolic secant pulses, we can derive that the cancellation point appears for 



marked with red crosses in Fig. 5 **(b)** , which stand in the vicinity of the numerically evaluated _α_ abs<sup>_∗_(black crosses).</sup> In the absence of intrinsic losses on the cavity, this result implies that when _κ_ s _>_ Γ, the optimal bandwidth to operate at full efficiency is at best Γ _/_ 2. Otherwise said, the memory protocol is only efficient for pulses whose bandwidth is below Γ _/_ 2, or equivalently, whose temporal extent is longer than 2 _/_ Γ. For smaller couplings, i.e. _κ_ s _<_ Γ, the admissible bandwidth is limited by _κ_ s _/_ 2, since _α_ abs<sup>_∗≈κ_s</sup><sup>_/_2Γ.</sup> 

In Fig. 5 **(c)** , we compute the minimal temporal extent 1 _/α_ abs<sup>_∗_Γasafunctionof</sup><sup>_g_ensfordifferentvaluesof</sup> the intrinsic loss rate _κ_ 0. Interestingly, the optimal operating bandwidth increases with intrinsic losses, but of course at the expense of protocol efficiency. Moreover, the lower bound for this extent is given by 2 _/_ Γ. This result has direct implications for the memory system. First, it limits its capacity to store multiple temporal modes. Indeed, at best, one would be able to store in the memory _∼ T_ 2Γ _/_ 2 temporal pulses, and in the case of a hybrid system with a small ensemble coupling constant, only _∼ T_ 2 _κ_ s _/_ 2 pulses. In the case of a second-long coherence time, this metric appears very optimistic since 

11 



<!-- Start of picture text -->
(a) (b)<br>0 /Γ = 0.00 0 /Γ = 0.03<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>0.00 0.25 0.50 0.75 1.00 0.00 0.25 0.50 0.75 1.00<br>α α<br>(c)<br>Γ/2π = 0.3 [MHz]<br>0 /2π = 0.02 [MHz]<br>0 /2π = 0.05 [MHz]<br>10 1<br>0 /2π = 0.08 [MHz]<br>0 /2π = 0.12 [MHz]<br>0 /2π = 0.15 [MHz]<br>10 0<br>0.05 0.10 0.15<br>gens/2π [MHz]<br>abs<br>η<br>][µs<br> ∗abs<br>α<br>Γ<br>/<br>1<br><!-- End of picture text -->

FIG. 5. Absorption efficiency analysis as a function of the pulse speed _α_ , increasing the ratio _g_ ens _/_ Γ from 0 _._ 05 (blue) to 0 _._ 5 (dark red), for zero cavity internal losses **(a)** and when _κ_ 0 _/_ Γ = 1 _/_ 30 **(b)** . When the input pulse is slow enough ( _α < α_ abs<sup>_∗_),theabsorptionefficiencyisgivenbyEq.(40).</sup> Above this critical value _α_ abs<sup>_∗_(blackcrosses),whichincreases</sup> with _g_ ens _/_ Γ, the efficiency drops. Its approximation by Eq. (42) is marked with red crosses. **(c)** Minimal pulse duration as a function of the spin-cavity coupling strength _g_ ens , for different values of the cavity internal losses _κ_ 0 _/_ 2 _π_ (printed in the legend, in [MHz]). An increment of _g_ ens allows for a faster input pulse, up to a point set by the spins’ bandwidth Γ _._ A similar effect is observed when increasing _κ_ 0 _,_ as you can see from the relative decrease between the different curves. We must recall that an increase of _κ_ 0 corresponds as well to a decrease in efficiency, meaning that you are allowed to go faster but with an efficiency cost. 

the capacity would then largely exceed the number of spins in the ensemble, which goes beyond the hypothesis of storing few excitations compared to the number of spins laid out in Sec. II. One should then consider another metric, which would account for the breakdown of the Holstein-Primakoff approximation. 

This minimal temporal extent also imposes constraints for inserting the memory in a modular architecture. Let us consider the simplest architecture of one qubit able to emit on demand its quantum state in the input waveguide of the quantum memory, with a wavepacket envelope appropriate for perfect absorption into the memory. To be a faithful representation of its past state, the itinerant quantum state should have a temporal extent signif- 

icantly smaller than the emitting qubit coherence times. However, if the corresponding bandwidth is too large, it may not be able to be absorbed with good efficiency into the memory, independently of its shape. Assuming a coherence time of 15 µs for a qubit connected in a quantum state transfer type architecture [41], it implies that the wavepacket should be emitted within the order of 1 _._ 5 µs. Assuming minimal intrinsic losses _κ_ 0 _/_ (2 _π_ ) = 20 kHz and a spin linewidth Γ _/_ (2 _π_ ) = 300 kHz, the ensemble coupling constant should then be larger than _g_ ens _/_ (2 _π_ ) = 120 kHz to be able to absorb efficiently this wavepacket. This constraint appears very reasonable in light of the parameters we considered for promising spin systems. 

The above analysis only concerns the optimal absorption efficiency. Concerning the optimal emission efficiency, (37) provides an upper bound. This upper bound is plotted in Fig. 6 **(a)** . This upper bound is attained for slow enough pulses such that the cavity bandwidth modulation _κ_<sup>_∗_</sup> e<sup>givenby(35)satisfiesthepositivitycon-</sup> straint. In Fig. 6 **(a)** , this corresponds to _α < α_ em<sup>_∗_de-</sup> noted by magenta crosses. As can be seen in the plot, these critical values are very close to the critical values for the absorption process. Above these critical values, the upper bound is not necessarily saturated, and to find the actual optimal emission efficiency, one needs to solve a convex optimization problem with constraints as stated before. 

We conclude by evaluating the impact of intrinsic losses on the total efficiency _η_ of the protocol. The numerical result is depicted in Fig. 6 **(b)** . The parameter _g_ ens _/_ Γ is set to 0 _._ 5 ( _α_ em<sup>_∗∼α_</sup> abs<sup>_∗∼_0</sup><sup>_._5forallvaluesof</sup> _κ_ 0), and we plot the efficiency as a function of _κ_ 0 _/_ Γ for _α_ = 0 _._ 12 _,_ 0 _._ 25 _,_ 0 _._ 46 and _α_ = 0 _._ 69 _> α_ abs<sup>_∗, α_</sup> em<sup>_∗_.In this last</sup> case of pulse speed above the critical point, the optimal modulation for _κ_ e, given by Eq. (35), violates the positivity constraint. Consequently, we adopt the suboptimal modulation _κ_ e( _t_ ) = _κ_<sup>_∗_</sup> a<sup>(</sup><sup>_TE−t_).Thischoiceismotivated</sup> by the fact that, for slow pulses, this time-reversed modulation is close to the optimal emission modulation (see Fig. 8). Fig. 6 **(b)** shows how much the efficiency associated with this suboptimal modulation (yellow, solid) deviates from its upper bound (yellow, dash-dotted), which is given by the product of the optimal absorption efficiency and the upper bound for emission efficiency (see Eq. (37)). 

## **VII. CONCLUSION** 

In this work, we have presented a quantum cascaded model for absorption and emission of an itinerant wavepacket into a spin ensemble embedded in a cavity. This model is derived in a mean-field framework and allows us to derive an upper bound for the memory catch and release efficiency depending on the hybrid system parameters. Spin coherence dynamics, for which we predict a limited impact, were excluded from the present derivation for conciseness, but could be straightforwardly 

12 



<!-- Start of picture text -->
(a) (b)<br>0 /Γ = 0.03 gens/Γ=0.50<br>1.0 1.0<br>α=0.12<br>0.8 0.8 α=0.25<br>α=0.46<br>0.6 0.6<br>α=0.69<br>0.4 0.4<br>0.2 0.2<br>0.0 0.0<br>0.0 0.5 1.0 0.0 0.5 1.0<br>α 0 /Γ<br>em η<br>η<br><!-- End of picture text -->

FIG. 6. **(a)** Emission efficiency analysis as a function of the pulse speed _α_ using the same convention as in Fig. 5 **(b)** . Dash-dotted line is the theoretical upper bound given by Eq. (37), that is saturated for _α < α_ em<sup>_∗_(magentacrosses),</sup> which closely matches _α_ abs<sup>_∗_(black crosses).</sup><sup>**(b)**Efficiency ver-</sup> sus cavity internal losses for the four pulse speeds in Fig. 4. For this coupling strength of _g_ ens = Γ _/_ 2, we have _α_ em<sup>_∗≈_0</sup><sup>_._5</sup> for all values of _κ_ 0. Thus, the first three pulses remain below the critical speed and reach the upper bounds shown by green, blue and red solid curves. The fastest pulse exceeds this critical speed, so that the upper bound (dash-dotted) can not be reached. Taking the suboptimal choice of _κ_ e( _t_ ) = _κ_ a( _T_ E _− t_ ) yields the solid yellow curve. 

included. We demonstrate that this efficiency bound is reached for adiabatic “slow” pulses and that there exists a critical bandwidth below which the memory performance remains close to this upper bound. Above this threshold, the efficiency decreases severely. We also derived the required modulation of the cavity coupling to the input waveguide to reach optimal absorption and emission of a given wavepacket. 

Another assumption of our model that could be easily revisited is the hypothesis of perfect refocusing pulses. While this allowed us to express simply the feedback occurring between absorption and emission, a more precise description of the action of the pulses, depending on each spin frequency or coupling constant, could be taken into account, which would allow us to derive a finiterefocusing efficiency. 

We conclude from this analysis that achieving in practice a high-fidelity quantum memory will require a bandwidth-tunable cavity with low intrinsic losses. Concerning the spin ensemble and its coupling to the cavity, the required parameters are within the reach of current experimental conditions. 

In future works, the results presented here could also be compared to numerical simulations discretizing the spin ensemble to study its dynamics [22] or to experimental realizations. Another theoretical development could be to use a mean-field framework extended to the second order to include the noise dynamics of the cavity and of the spin ensemble in the present analysis, and see whether this analysis would confirm the mean-field dynamics we have described here. Going further, outlining under which conditions the current mean-field dynamics 

would map to a full bosonic mode interaction dynamics, where the spin-cavity system could be described by a system density matrix, would be extremely helpful in the context of modeling a modular architecture. Indeed, this ability would allow for deriving transfer efficiency and fidelity in a very straightforward manner despite the high number of degrees of freedom in the overall system and its hybrid nature. 

## **Data availability** 

The datasets generated during the current study are available in a Github repository. 

## **Acknowledgments** 

L. Greggio, A. Petrescu and M. Mirrahimi acknowledge funding from French ANR grant OCTAVES (ANR21-CE47-0007). T. Lorriaux acknowledges the support of France 2030 project QuanTEdu-France ANR-22-CMAS0001, and A. Bienfait and T. Lorriaux acknowledge funding from the Plan France 2030 through the project ANR22-PETQ-0003. 

## **Author contributions** 

L.G., M.M. and A.B. performed the theoretical analysis, with contributions of A.P. and T.L.. L.G. performed the numerical simulations. L.G. and A.B. drafted the manuscript, and all authors reviewed it. 

## **Competing interests** 

The authors declare no competing interests 

## **Appendix A: Derivation of the EOMs** 

In this appendix, we derive the equations of motion for the intra-cavity field absorbed by the spins and then re-emitted at _T_ E = 2 _τ_ a + 2 _τ_ e. 

We recall that during absorption ( _t ≤ τ_ a), the dynamics of the intra-cavity field and of _σ−_<sup>_j_of spin</sup><sup>_j_is dictated</sup> by the following EOMs (see [21]) 





13 



<!-- Start of picture text -->
(a) (b) (c) (d)<br>Σa(Γt) Σe(Γt) εin(Γt) εe, out(Γt) a (Γt) e (Γt) 20 a (Γt) e (Γt)<br>1.0 α=0.12 α=0.46 η = 93.5%<br>α=0.25 α=0.69 η = 92.9% 10<br>0.5 η = 79.3% 10<br>η = 19.9%<br>5<br>0.0<br>0<br>0.5<br>0<br>10<br>-20 0 20 -20 0 20 -20 0 20 -20 0 20 -20 0 20 -20 0 20 -20 0 20 -20 0 20<br>Γt Γ(t − TE) Γt Γ(t − TE) Γt Γ(t − TE) Γt Γ(t − TE)<br><!-- End of picture text -->

FIG. 7. Same plots as in Fig. 4, but for a Lorentzian pulse. In **(c)** - **(d)** the printed efficiency for different values of the pulse speed is lower with respect to the relative one shown for a hyperbolic secant pulse (see Fig. 4 **(c)** - **(d)** ), especially for fast pulses. This demonstrates the better performance of a hyperbolic secant pulse compared to a Lorentzian pulse. 

We consider _ε_ a( _−∞_ ) = _σ−_<sup>_j,_a(</sup><sup>_−∞_)=0andweintegrate</sup> Eq. (A2) 

where the change of sign reflects the flipping caused by the first refocusing pulse. Using the convention _σ−_<sup>_j,_a/e</sup> ( _τ_ a<sup>+) =</sup><sup>_σ_</sup> _−_<sup>_j,_a(</sup><sup>_τ −_</sup> a<sup>)togetherwithEq.(A3),weobtain</sup> 





In the EOM for the intra-cavity field (A1), we replace the term<sup>�</sup><sup>_N_</sup> _j_ =1<sup>_gjσ_</sup> _−_<sup>_j_withitsintegratedversion,using</sup> the spin frequency and coupling distributions 





and we plug in the expression for _σ−_<sup>∆</sup><sup>_,g_</sup> given in Eq. (A3), to obtain 



We integrate Eq. (A9) using the convention _σ−_<sup>_j,_e(</sup><sup>_T_+</sup> E<sup>)=</sup> _σ−_<sup>_j,_a/e</sup> ( _T_ E<sup>_−_)andweobtain</sup> 

with _g_ ens<sup>2</sup> = � _p_ ( _g_ ) _g_<sup>2</sup> _dg_ , and where we recognize the Fourier transform of the frequency distribution _n_ (∆), i.e. _n_ ( _t − s_ ) = _e_<sup>_−_Γ</sup><sup>_|t−s|/_2</sup> . We can thus rewrite the above ex- _t_ pression as _−g_ ens<sup>2</sup> � _−∞_<sup>_dse−_Γ</sup><sup>_|t−s|/_2</sup><sup>_ε_a(</sup><sup>_s_)</sup><sup>_,_that we equalize</sup> _t_ to _−g_ ens Σa _,_ where Σa( _t_ ) = _g_ ens � _−∞_<sup>_dse−_</sup><sup><u>Γ</u></sup> 2<sup>(</sup><sup>_t−s_)</sup> _ε_ a( _s_ ) _,_ with Σa( _−∞_ ) = 0 _,_ representing the field stored in the cavity. 



Consequently, the spin-cavity EOMs during absorption rewrite as 



Now, we present the EOM for _σ−_<sup>_j_ofspin</sup><sup>_j_inbetween</sup> the two pulses ( _τ_ a _< t < T_ E = 2 _τ_ a + _τ_ e), when the cavity is detuned 





14 

The second term can be expressed as _−g_ ens Σ<sup>˜</sup> e, which introduces a new variable ˜Σe( _t_ ) = _t g_ ens � _T_ E<sup>_dse−_</sup><sup><u>Γ</u></sup> 2<sup>(</sup><sup>_t−s_)</sup> _ε_ e( _s_ ), with ˜Σe( _T_ E) = 0 _._ To deal with the first integral we define the variable _t_ ˜Σa( _t_ ) = _g_ ens � _−τ_ a<sup>_dse−_</sup><sup><u>Γ</u></sup> 2<sup>(</sup><sup>_t−s_)</sup> _ε_ a( _−s_ ) _,_ with Σ<sup>˜</sup> a( _−τ_ a) = 0; representing a filtered version of the field stored in the spins during absorption. Using these new variables, together with the previously defined Σa, we re-express Eq. (A11) as _−g_ ens Σe, where the field stored in the spin ensemble during emission is defined as 



We can now present the EOMs for the field in the cavity and the one stored in the spins during emission 



with Σ<sup>˜</sup> a( _T_ E _− t_ ) representing a feedback term from absorption, appearing when _t ≤ T_ E + _τ_ a. 

Concerning Σe( _t_ ), continuity and differentiability are not lost in _t_ = _T_ E+ _τ_ a. The initial conditions are _ε_ e( _T_ E) = _ε_ a( _τ_ a) _e_<sup>_−κ_</sup> 2<sup><u>0</u>(</sup><sup>_τ_a+</sup><sup>_τ_e)</sup> _,_ Σe( _T_ E) = Σa( _−τ_ e) + Σ<sup>˜</sup> a( _τ_ e) _._ 

In our work, we neglect the cut-off of the feedback term since it does not affect the storage time interval, and we consider Σe undergoing the following EOMs 



with Σe,in = _√_ ΓΣ<sup>˜</sup> a( _T_ E _− t_ ) being the feedback term from absorption. 

Finally, we consider _τ_ a large enough such that the entire field has left the cavity at the moment of the first refocusing pulse. This allows us to consider the intracavity field _ε_ a to be zero after _τ_ a, and the intra-cavity field _ε_ e to be zero before _T_ E _._ The same consideration holds for the field stored in the spins since we can consider that before the refocusing pulses the information has been totally washed out by inhomogeneous broadening, namely Σa and Σe are zero after _τ_ a and before _T_ E respectively. Under this assumption, we can consider _ε_ ( _±∞_ ) = Σ( _±∞_ ) = 0 _._ 

## **Appendix B: Transmission and reflection coefficients** 

In this appendix, we aim to derive the expression for the transmission and reflection coefficients in the frequency domain, in the case of constant coupling _κ_ and detuning ∆cs _._ 

We recall the definition of the transmission and reflection coefficients associated with absorption and emission 



with _t_ a being the transmission coefficient from the driveline to the spins, _t_ e being the one from the spins back to the driveline, _r_ a being the reflection coefficient back to the driveline and _r_ e being the one back to the spins. 

We rewrite the absorption EOMs (A5) in the frequency domain, considering a non-zero detuning ∆cs and a constant _κ_ a 



Rearranging the terms we get Σa[ _δ_ ] and _ε_ a[ _δ_ ] as functions of _ε_ in[ _δ_ ] 



with 



where _κ_ s = 4 _g_ ens<sup>2</sup><sup>_/_Γ,</sup><sup>_κ_˜s</sup><sup>_/κ_s= 1</sup><sup>_−δ_</sup><sup><u>(</u></sup><sup>_δ_</sup> _g_<sup><u>+</u></sup> ens<sup>2∆cs)</sup> and _δ/δ_<sup>˜</sup> = 1 + ( _κ_ 0 + _κ_ ) _/_ Γ. We consider the absorption transmission and reflection coefficients defined in Eq. (B1) in the frequency domain, we substitute Σa,out with _√_ ΓΣa and _ε_ a,out with ~~�~~ _κ_ a( _t_ ) _ε_ a _− ε_ in, and we plug in Eq. (B3) to obtain 



We pass to emission and we rewrite the relative EOMs (first eq. in (A12) and Eq. (A13)) in the frequency domain, considering the detuning ∆cs and a constant _κ_ e 



Rearranging the terms we get Σe[ _δ_ ] and _ε_ e[ _δ_ ] as functions of the driving field Σe,in[ _δ_ ] 



15 

We consider the emission transmission and reflection coefficients defined in Eq. (B1) in the frequency domain, substituting _ε_ e,out with<sup>_√_</sup> _<u>κ</u>_ e _<u>ε</u>_ e and Σe,out with _√_ ΓΣe _−_ Σe,in, and we plug in Eq. (B7) to obtain 



Note that the transmission coefficient during emission represents a mirrored version of the one during absorption, i.e. _t_ e[ _δ_ ] = _−t_ a[ _δ_ ] _,_ with relative coupling constant _κ_ e and _κ_ a _._ 

## **Appendix C: Input-output energies** 

In this appendix, we provide the derivation of the inequality (25) leading to the upper bound for the absorption process, and the identity (28) required for treating the optimization of the emission process. 

We recall that the input energy evaluated at the optimal _κ_ ¯<sup>_∗_</sup> a<sup>reads</sup> 



where _A_ (¯ _κ_ a) and _B_ (¯ _κ_ a) are defined in Eq. (21). The integrand �� _<u>BA</u>_ ��� _A_ + _B_ �� _BA_ ���2 can be rewritten as 2 _|AB|_ + 2 _AB_ , which is lower bounded by 4 _AB_ . Consequently, a lower bound for the input energy is given by 



where we have used the fact that _S_ a( _±∞_ ) = _S_<sup>˙</sup> a( _±∞_ ) = 0 _._ This proves the inequality (25). 

Now, for the emission process, we recall the EOMs 



We multiply the first equation by _E_ e, and the second equation by _S_ e, then integrate both of them over time to obtain 





<!-- Start of picture text -->
(a) α=0.12 (b) α=0.12<br>1.1<br>1.0<br>e (Γt) a (Γ(T E − t))<br>Γ Γ<br>268 T¯E 308 268 T¯E 308<br>Γt Γt<br><!-- End of picture text -->

FIG. 8. Same conventions as in of Fig. 4. Optimal shape for _κ_ e( _t_ ) (solid line, as defined in Eq. (35)) compared to the timereversed absorption profile _κ_ a( _T_ E _−t_ ) (dashed-dotted line), for a slow hyperbolic secant pulse ( **a** ) and a slow Lorentzian pulse ( **b** ), both not far from the the “slow-pulse” limit (black-dotted line). When _α < α_ em<sup>_∗_,</sup><sup>_κ_</sup> e<sup>(</sup><sup>_t_)closelyresemblesamirroredver-</sup> sion of the time-reversed _κ_ a, supporting the choice of using a mirrored coupling profile for emission in the fast-pulse regime ( _α ≥ α_ em<sup>_∗_).</sup> 

We recall that _E_ e( _±∞_ ) = _S_ e( _±∞_ ) = 0 _,_ we sum the two equations in (C3) and we get 



from which we derive the output energy as 



We rewrite the second equation in (C2) as _E_ e = g1 � _S_ ˙e +<sup><u>1</u></sup> 2<sup>_S_e</sup><sup>_−S_in</sup> �, we insert it in Eq. (C5) and we obtain 



To pass to the frequency domain through Parseval’s theorem, we get rid of the cross product _S_ e _S_ in by rewriting the term _−S_ e<sup>2+2</sup><sup>_S_e</sup><sup>_S_inas</sup><sup>_−_(</sup><sup>_S_e</sup><sup>_−S_in)2+</sup><sup>_S_</sup> in<sup>2</sup><sup>_._Consequently,</sup> we obtain the identity (28). 

## **Appendix D: Further numerical results** 

In this appendix, we present the simulation results for a Lorentzian pulse, showing its worse performance compared to the chosen hyperbolic secant pulse in terms of efficiency. Moreover, we show that, for _α < α_ em<sup>_∗_,the</sup> optimal modulation for the coupling during emission is approximately a mirrored version of the one derived for the absorption step, justifying why we are taking this approximation above the critical speed, when the positivity constraint for the optimization problem should be active. 

16 

The Lorentzian pulse, normalized to unity, writes Σa( _t_ ) = 1+( _<u>√</u>_ 2 _αα_ Γ _<u>/tπ</u>_ )<sup>2.</sup> The numerics are implemented the same way as for the hyperbolic secant pulse (see Subsec. VI B). The results are presented in Fig. 7, showing a lower efficiency compared to the one obtained by the corresponding hyperbolic secant pulse. 

pulses is presented in Fig. 8, together with the timereversed version of the optimal _κ_ a, given by Eq. (23). The first one represents a slightly translated version of the second one, which allows us to perform the approximation. 

## **Appendix E: Symbols and notations** 

The optimal _κ_ e, given by Eq. (35), for both types of 

- [1] K. Heshami, D. G. England, P. C. Humphreys, P. J. Bustard, V. M. Acosta, J. Nunn, and B. J. S. and, Journal of Modern Optics **63** , 2005 (2016), pMID: 27695198, https://doi.org/10.1080/09500340.2016.1148212. 

- [2] H. J. Kimble, Nature **453** , 1023 (2008). 

- [3] L. M. Duan, M. D. Lukin, J. I. Cirac, and P. Zoller, Nature **414** , 413 (2001). 

- [4] M. K. Bhaskar, R. Riedinger, B. Machielse, D. S. Levonian, C. T. Nguyen, E. N. Knall, H. Park, D. Englund, M. Lonˇcar, D. D. Sukachev, and M. D. Lukin, Nature **580** , 60 (2020). 

- [5] N. Sangouard, C. Simon, H. de Riedmatten, and N. Gisin, Rev. Mod. Phys. **83** , 33 (2011). 

- [6] S. Zaiser, T. Rendler, I. Jakobi, T. Wolf, S.-Y. Lee, S. Wagner, V. Bergholm, T. Schulte-Herbr¨uggen, P. Neumann, and J. Wrachtrup, Nature Communications **7** , 12279 (2016). 

- [7] W. Ding, W. Zhang, and X. Wang, Phys. Rev. A **102** , 032612 (2020). 

- [8] D. Thaker, T. Metodi, A. Cross, I. Chuang, and F. Chong, in _33rd International Symposium on Computer Architecture (ISCA’06)_ (2006) pp. 378–390. 

- [9] E. Gouzien and N. Sangouard, Phys. Rev. Lett. **127** , 140503 (2021). 

- [10] A. I. Lvovsky, B. C. Sanders, and W. Tittel, Nature Photonics **3** , 706 (2009). 

- [11] W. Tittel, M. Afzelius, T. Chaneli´ere, R. Cone, S. Kr¨oll, S. Moiseev, and M. Sellars, Laser & Photonics Reviews **4** , 244 (2010). 

- [12] C. Clausen, I. Usmani, F. Bussi`eres, N. Sangouard, M. Afzelius, H. de Riedmatten, and N. Gisin, Nature **469** , 508 (2011). 

- [13] P. Rabl, D. DeMille, J. M. Doyle, M. D. Lukin, R. J. Schoelkopf, and P. Zoller, Phys. Rev. Lett. **97** , 033003 (2006). 

- [14] M. Reagor, W. Pfaff, C. Axline, R. W. Heeres, N. Ofek, K. Sliwa, E. Holland, C. Wang, J. Blumoff, K. Chou, M. J. Hatridge, L. Frunzio, M. H. Devoret, L. Jiang, and R. J. Schoelkopf, Phys. Rev. B **94** , 014506 (2016). 

- [15] A. M. Bozkurt, S. Miles, S. L. D. ten Haaf, C.-X. Liu, F. Hassler, and M. Wimmer, “Interaction-induced strong zero modes in short quantum dot chains with timereversal symmetry,” (2025), arXiv:2405.14940 [condmat.mes-hall]. 

- [16] N. Sangouard, R. Dubessy, and C. Simon, Phys. Rev. A **79** , 042340 (2009). 

- [17] A. Reiserer and G. Rempe, Rev. Mod. Phys. **87** , 1379 (2015). 

- [18] C. E. Bradley, J. Randall, M. H. Abobeih, R. C. Berrevoets, M. J. Degen, M. A. Bakker, M. Markham, D. J. Twitchen, and T. H. Taminiau, Phys. Rev. X **9** , 031045 (2019). 

- [19] in _Advances In Atomic, Molecular, and Optical Physics_ , Vol. 67 (Academic Press, 2018) pp. 77–150. 

- [20] M. Afzelius and C. Simon, Phys. Rev. A **82** , 022310 (2010). 

- [21] M. Afzelius, N. Sangouard, G. Johansson, M. U. Staudt, and C. M. Wilson, New Journal of Physics **15** , 065008 (2013). 

- [22] B. Julsgaard, C. Grezes, P. Bertet, and K. Mølmer, Phys. Rev. Lett. **110** , 250503 (2013). 

- [23] K. Jahne, B. Yurke, and U. Gavish, Physical Review A **75** , 010301 (2007). 

- [24] A. N. Korotkov, Physical Review B **84** , 014510 (2011). 

- [25] E. Chatterjee, D. Soh, and M. Eichenfield, Journal of Physics A: Mathematical and Theoretical **55** , 105302 (2022). 

- [26] J. Z. Bern´ad, M. Schilling, Y. Wen, M. M. M¨uller, T. Calarco, P. Bertet, and F. Motzoi, Journal of Physics B: Atomic, Molecular and Optical Physics **58** , 035501 (2025). 

- [27] C. W. Gardiner, Phys. Rev. Lett. **70** , 2269 (1993). 

- [28] V. Damon, M. Bonarota, A. Louchet-Chauvet, T. Chaneli`ere, and J.-L. L. Gou¨et, **13** , 093031. 

- [29] J. O’Sullivan, O. W. Kennedy, K. Debnath, J. Alexander, C. W. Zollitsch, M. Sim˙enas,<sup>ˇ</sup> A. Hashim, C. N. Thomas, S. Withington, I. Siddiqi, K. Mølmer, and J. J. L. Morton, Phys. Rev. X **12** , 041014 (2022). 

- [30] C. Grezes, B. Julsgaard, Y. Kubo, W. L. Ma, M. Stern, A. Bienfait, K. Nakamura, J. Isoya, S. Onoda, T. Ohshima, V. Jacques, D. Vion, D. Esteve, R. B. Liu, K. Mølmer, and P. Bertet, Physical Review A **92** , 020301 (2015). 

- [31] M. U. Staudt, I.-C. Hoi, P. Krantz, M. Sandberg, M. Simoen, P. Bushev, N. Sangouard, M. Afzelius, V. S. Shumeiko, G. Johansson, P. Delsing, and C. M. Wilson, Journal of Physics B: Atomic, Molecular and Optical Physics **45** , 124019 (2012). 

- [32] V. Ranjan, Y. Wen, A. K. V. Keyser, S. E. Kubatkin, A. V. Danilov, T. Lindstr¨om, P. Bertet, and S. E. de Graaf, Physical Review Letters **129** , 180504 (2022). 

- [33] H. Primakoff and T. Holstein, Phys. Rev. **55** , 1218 (1939). 

- [34] H. J. Carmichael, Phys. Rev. Lett. **70** , 2273 (1993). 

- [35] C. Weedbrook, S. Pirandola, R. Garc´ıa-Patr´on, N. J. Cerf, T. C. Ralph, J. H. Shapiro, and S. Lloyd, Rev. Mod. Phys. **84** , 621 (2012). 

17 

## **General Notation and Constants** 

- _ωs_ Mean spin Larmor frequency _ωc_ Cavity frequency 

- _ωj_ Larmor frequency of spin _j_ 

- ∆ _j_ Detuning of spin _j_ from _ωs_ : ∆ _j_ = _ωj − ωs_ 

- ∆cs Detuning between cavity and spin central frequency: ∆cs = _ωc − ωs_ 

- Γ Inhomogeneous linewidth of the spin ensemble _T_ 2 Coherence time of the spin ensemble _TE_ Echo time: _TE_ = 2 _τa_ + 2 _τe_ 

- _τa_ Duration of the absorption step _τe_ Duration of the emission step 

## **Operators** 

- _ε_ ˆ Annihilation operator for the cavity field 

- _ε_ ˆ<sup>_†_</sup> Creation operator for the cavity field 

- _σ_ ˆ<sup>_j_</sup> 

- Lowering operator for spin _j_ 

_−_ 

- _σ_ ˆ+<sup>_j_</sup> Raising operator for spin _j_ 

- _σ_ ˆ<sup>_j_</sup> 

- _z_<sup>_j_</sup> Pauli- _z_ operator for spin _j_ 

## **Fields and Couplings** 

- _ε_ in( _t_ )[ _E_ in] Input field envelope 

- _ε_ out( _t_ )[ _E_ out] Output field envelope _ε_ ( _t_ )[ _E_ ] Intra-cavity field Σ( _t_ )[ _S_ ] Field in the spin ensemble 

- _gj_ Coupling strength between cavity and spin _j_ 

- _g_ ens [g] Collective coupling strength: _g_ ens<sup>2=</sup> � _p_ ( _g_ ) _g_<sup>2</sup> _dg_ 

- _κ_ 0[¯ _κ_ 0] Intrinsic loss rate of the cavity _κ_ ( _t_ )[¯ _κ_ ] Coupling rate of the cavity to the input line 

- _κ_ a( _t_ )[¯ _κ_ a] Cavity coupling rate during absorption _κ_ e( _t_ )[¯ _κ_ e] Cavity coupling rate during emission _κ_ s[¯ _κ_ s] Spin-induced loss rate on the cavity: _κ_ s = 4 _g_ ens<sup>2</sup><sup>_/_Γ</sup> Σa[ _S_ a] Spin field during absorption Σe[ _S_ e] Spin field during emission 

## **Efficiency and Transmission Coefficients** 

- _η_ Overall efficiency of the protocol _ηa × ηH × ηe_ 

- _ηa_ Absorption efficiency _ηe_ Emission efficiency 

- _ηH_ Efficiency of the refocusing pulses _ta_ Transmission coef. from driveline to spins _te_ Transmission coef. from spins back to driveline _ra_ Reflection coef. back to the driveline _re_ Reflection coef. back to the spins 

- **Optimization and Mathematical Functions** 

- _H_ [ _δ_ ] Filter function between Σa,out and Σe,in _F_ Fourier transform 

- _F_<sup>_−_1</sup> Inverse Fourier transform _κ_ ¯<sup>_∗_</sup> _a_ Optimal cavity coupling rate during absorption _κ_ ¯<sup>_∗_</sup> _e_ Optimal cavity coupling rate during emission 

## **Physical Parameters for Simulations** 

- _α_ Bandwidth of the input pulse: _α_ Γ 

- _α_ abs<sup>_∗_</sup> Critical bandwidth for absorption _α_ em<sup>_∗_</sup> Critical bandwidth for emission _κ_ max Maximum coupling rate _κ_ min Minimum coupling rate 

- [36] G. Wolfowicz, A. M. Tyryshkin, R. E. George, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, M. L. W. Thewalt, S. A. Lyon, and J. J. L. Morton, Nature Nanotechnology **8** , 561 (2013). 

- [37] W. Tittel, M. Afzelius, A. Kinos, L. Rippe, and A. Walther, “Quantum networks using rare-earth ions,” (2025), arXiv:2501.06110 [quant-ph]. 

- [38] E. Fraval, M. J. Sellars, and J. J. Longdell, Physical Review Letters **92** , 077601 (2004). 

- [39] J. Alexander, G. Dold, O. W. Kennedy, M. Sim˙enas,<sup>ˇ</sup> J. O’Sullivan, C. W. Zollitsch, S. Welinski, A. Ferrier, E. Lafitte-Houssat, T. Lindstr¨om, P. Goldner, and J. J. L. Morton, Physical Review B **106** , 245416 (2022). 

- [40] A. Tiranov, E. Green, S. Hermans, E. Liu, F. Chiossi, D. Serrano, P. Loiseau, A. M. Kumar, S. Bertaina, A. Faraon, and P. Goldner, “Sub-second spin and lifetime-limited optical coherences in<sup>171</sup> yb<sup>3+</sup> :cawo4,” (2025), arXiv:2504.01592 [quant-ph]. 

- [41] P. Kurpiers, P. Magnard, T. Walter, B. Royer, M. Pechal, J. Heinsoo, Y. Salath´e, A. Akin, S. Storz, J. C. Besse, S. Gasparinetti, A. Blais, and A. Wallraff, Nature **558** , 264 (2018). 

- [42] J. Niu, L. Zhang, Y. Liu, J. Qiu, W. Huang, J. Huang, H. Jia, J. Liu, Z. Tao, W. Wei, Y. Zhou, W. Zou, Y. Chen, X. Deng, X. Deng, C. Hu, L. Hu, J. Li, D. Tan, Y. Xu, F. Yan, T. Yan, S. Liu, Y. Zhong, A. N. Cleland, and D. Yu, Nature Electronics **6** , 235 (2023). 

- [43] V. Ranjan, J. O’Sullivan, E. Albertinale, B. Albanese, T. Chaneli`ere, T. Schenkel, D. Vion, D. Esteve, E. Flurin, J. J. L. Morton, and P. Bertet, Phys. Rev. Lett. **125** , 210505 (2020). 

- [44] C. Grezes, B. Julsgaard, Y. Kubo, M. Stern, T. Umeda, J. Isoya, H. Sumiya, H. Abe, S. Onoda, T. Ohshima, V. Jacques, J. Esteve, D. Vion, D. Esteve, K. Mølmer, and P. Bertet, Phys. Rev. X **4** , 021049 (2014). 

- [45] J. O’Sullivan, O. W. Kennedy, C. W. Zollitsch, M. Sim˙enas,<sup>ˇ</sup> C. N. Thomas, L. V. Abdurakhimov, S. Withington, and J. J. Morton, Physical Review Applied **14** , 064050 (2020). 

- [46] M. Kjaergaard, M. E. Schwartz, J. Braum¨uller, P. Krantz, J. I.-J. Wang, S. Gustavsson, and W. D. Oliver, Annual Review of Condensed Matter Physics **11** , 369 (2020). 

- [47] J. Kerckhoff, R. W. Andrews, H. S. Ku, W. F. Kindel, K. Cicak, R. W. Simmonds, and K. W. Lehnert, Physical Review X **3** , 021013 (2013). 

- [48] J. Grebel, H. Yan, M.-H. Chou, G. Andersson, C. R. Conner, Y. J. Joshi, J. M. Miller, R. G. Povey, H. Qiao, X. Wu, and A. N. Cleland, Physical Review Letters **132** , 047001 (2024). 

- [49] C. Bockstiegel, Y. Wang, M. R. Vissers, L. F. Wei, S. Chaudhuri, J. Hubmayr, and J. Gao, Applied Physics Letters **108** , 222604 (2016). 

- [50] Y. Wen, V. Ranjan, T. Lorriaux, D. Vion, B. Huard, A. Bienfait, E. Flurin, and P. Bertet, “Addressing spins at the clock transitions with a frequency- and bandwidth-tunable superconducting resonator,” (2025), arXiv:2510.19684 [quant-ph]. 

TABLE I. List of symbols and their definitions. Symbol _X_ in [ _X_ ( _τ_ )] indicates a rescaled quantity by the change of time variable _τ_ = Γ _t_ . 

