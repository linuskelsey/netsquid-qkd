## **Many-body quantum register for a spin qubit** 

Martin Hayhurst Appel,<sup>1</sup> Alexander Ghorbal,<sup>1</sup> Noah Shofer,<sup>1</sup> Leon Zaporski,<sup>1</sup> Santanu Manna,<sup>2</sup> Saimon Filipe Covre da Silva,<sup>2</sup> Urs Haeusler,<sup>1</sup> Claire Le Gall,<sup>1</sup> Armando Rastelli,<sup>2</sup> Dorian A. Gangloff,<sup>1,</sup><sup>_∗_</sup> and Mete Atat¨ure<sup>1,</sup><sup>_†_</sup> 

> 1 _Cavendish Laboratory, University of Cambridge, J.J. Thomson Avenue, Cambridge, CB3 0HE, UK_ 

> 2 _Institute of Semiconductor and Solid State Physics, Johannes Kepler University, Altenberger Str. 69, Linz 4040, Austria_ (Dated: May 1, 2024) 

Quantum networks require quantum nodes with coherent optical interfaces and multiple stationary qubits. In terms of optical properties, semiconductor quantum dots are highly compelling, but their adoption as quantum nodes has been impaired by the lack of auxiliary qubits. Here, we demonstrate a functional quantum register in a semiconductor quantum dot leveraging the dense, always-present nuclear spin ensemble. We prepare 13,000 host nuclear spins into a single manybody dark state to operate as the register logic state _|_ 0 _⟩_ . The logic state _|_ 1 _⟩_ is defined as a single nuclear magnon excitation, enabling controlled quantum-state transfer between the electron spin qubit and the nuclear magnonic register. Using 130-ns SWAP gates, we implement a full writestore-retrieve-readout protocol with 68.6(4)% raw overall fidelity and a storage time of 130(16) µs in the absence of dynamical decoupling. Our work establishes how many-body physics can add stepchange functionality to quantum devices, in this case transforming quantum dots into multi-qubit quantum nodes with deterministic registers. 

Quantum nodes consisting of multiple qubits with efficient coupling to photons are required by a wide range of quantum information tasks including quantum repeaters [1–3] and deterministic 2d-cluster state generation [12, 13]. In one approach, an optically active spin qubit exchanges quantum information between a photonic mode and several long-lived register qubits [3, 4]. Multiple spin-photon interfaces have demonstrated functional registers including diamond color centres coupled to proximal 13C nuclear spins [14–16] or to the native nuclear spin of the color centre [17], SiC divacancy spins coupled to<sup>29</sup> Si nuclear spins [18], multi-species ion traps [19], and<sup>171</sup> Yb<sup>3+</sup> ions coupled with neighboring 51V5+ ions in a YVO4 crystal [20]. Group III-V semiconductor quantum dots (QDs) have state-of-the-art photon coherence [5, 6] and brightness [7] but have so far lacked auxiliary qubits for the electron spin qubit. In contrast to the aforementioned few-particle systems, an electron spin qubit confined in a QD is Fermi-contact coupled to an ensemble of _∼_ 10<sup>5</sup> nuclear spins [8] which when uncontrolled acts as a source of noise for the qubit [21–23]. Once sufficiently engineered, the ensemble can instead act as a bosonic system capable of encoding quantum information in collective excitations [9, 10, 24, 25] similar to photon memories [26], ferromagnetic magnons [27] and microwave resonators [28]. 

Significant progress on controlling dense nuclear spin ensemble using InGaAs QDs includes dynamical nuclear polarisation [29], stabilization of the nuclear Overhauser field [11, 30], and electron-mediated collective nuclear excitations [31]. Despite reaching low-fluctuation highpurity nuclear states, the coherence of the nuclear ensemble is however limited by the strain-induced nuclear broadening [23] present in self-assembled QDs. Recent work on lattice-matched GaAs QDs has overcome this limitation, leading to high-fidelity NMR control [32], nu- 

clear hyper-polarisation [33], enhanced electron spin dephasing times [34] and spin coherence exceeding 100 µs under dynamical decoupling [35]. The final requirement of a nuclear quantum register is the union of a controllable electron spin with an engineered nuclear ensemble. 

In this article, we demonstrate reversible quantum state transfer between an electron spin qubit and a collective excitation of 13000 nuclear spins in a GaAs QD. To achieve this, we introduce a way to engineer a collective nuclear state by polarizing the<sup>69</sup> Ga and<sup>71</sup> Ga isotopes in opposite directions. The result is that one isotope (<sup>71</sup> Ga) is prepared in our register ground state consisting of a coherent nuclear dark state with 60% polarisation. Our controlled electro-nuclear SWAP gates enable arbitrary state transfer from the electronic spin qubit to the single nuclear-magnon states. Ramsey interferometry of the register states operates as a quantum sensor to detect directly the electronic Knight field experienced by the nuclei. When decoupled from the Knight field, the register achieves a 130(16) µs storage time consistent with limits set by quadrupolar broadening, promising extension beyond 20 ms [32] with the addition of nuclear control pulses. 

### **ISOTOPE-RESOLVED ELECTRO-NUCLEAR INTERFACE** 

Our QD system can be approximated as a central electron spin **S**<sup>ˆ</sup> coupled to an ensemble of _N_ identical nuclear ˆspins<sup>ˆ</sup> **I** _i_ . We define the collective nuclear spin operator **I** =<sup>�</sup> _i_<sup>ˆ</sup><sup>**I**</sup><sup>_i_andworkinthecollectivebasis</sup><sup>_|j_,</sup><sup>_m⟩_:</sup><sup>_j≤j_0</sup> is the total angular momentum where _j_ 0 = _NI_ is the maximal spin length set by the nuclear spin magnitude _I_ , and _m_ = _−j_ , _. . ._ , _j_ is the spin projection along _z_ . For an external magnetic field along _z_ , the system evolves 

2 



<!-- Start of picture text -->
spin<br>...<br>...<br><!-- End of picture text -->



<!-- Start of picture text -->
i ...<br>...<br><!-- End of picture text -->



<!-- Start of picture text -->
...<br>...<br><!-- End of picture text -->



<!-- Start of picture text -->
e -<br>75As<br>69Ga<br>71Ga Magnetic field<br>~ 6 nm<br><!-- End of picture text -->





<!-- Start of picture text -->
T<br>Lock Init. Drive, Ω/2π = 2.2 MHz, δ Read<br><!-- End of picture text -->







Fig. 1. **Isotope-resolved electro-nuclear interface. a,** A central electron spin coupled to _N_ nuclear spins prepared in a dark state. The two lowest ensemble states create a register manifold where an electronic excitation (yellow) can be swapped to a collective nuclear excitation once the dressed-state splitting _χ_ is resonant with the nuclear Larmor frequency _ωn_ . **b,** Physical realization of a central spin system using a GaAs quantum dot hosting three nuclear species. **c,** Energy level diagram containing the ground states _|↑⟩_ , _|↓⟩_ . A pump laser (784.6 nm) resonant with the trion state _|⇓↑↓⟩_ allows readout of _|↓⟩_ and initialization into _|↑⟩_ . The Zeeman splitting _ωe_ is bridged by a _∼_ 600 GHz detuned bi-chromatic laser (yellow arrows) with two-photon detuning _δ_ and spin Rabi frequency Ω. **d,** Measured ESR spectrum, where the electron is initialized in _|↑⟩_ and driven with detuning _δ_ for drive time _T_ , following nuclear polarisation locking at _Iz ∼_ 0 (see sequence inset). **e,** Average signal within the white box in d. Three pairs of sidebands occur at the expected nuclear Larmor frequencies of the host material (colored lines). Other features stem from second-order processes (Supplementary Information). 

under the approximate Hamiltonian 



where _ωn_ is the nuclear Larmor frequency and _a∥_ ( _a⊥_ ) is the collinear(non-collinear) hyperfine coupling constant. We provide the energy required for a nuclear spin flip through the rotating frame electron drive _H_<sup>ˆ</sup> drive = _δS_<sup>ˆ</sup> _z_ + Ω _S_<sup>ˆ</sup> _x_ which creates dressed electronic states _{ |_<sup>˜</sup> _↑⟩_ , _|_<sup>˜</sup> _↓⟩}_ split by _χ_ = _√δ_<sup>2</sup> + Ω<sup>2</sup> (Fig. 1a). Setting _χ_ = _ωn_ satisfies the Hartmann–Hahn resonance condition [36] and leads to evolution dominated by 



where dressed-state spin flips inject collective nuclear excitations. We now imagine an ensemble prepared in a coherent dark state _|j_ , _−j⟩_ with _j < j_ 0. Further reduction of _m_ = _−j_ is forbidden under the system symmetries [9, 37], allowing the two lowest ensemble states _|_ 0 _⟩_ = _|j_ , _−j⟩_ and _|_ 1 _⟩_ = _|j_ , _−j_ + 1 _⟩_ to form a closed manifold permitting deterministic quantum state transfer (Fig. 1a). For a general input state _α |_<sup>˜</sup> _↓⟩_ + _β |_<sup>˜</sup> _↑⟩_ , correctly timed evolution under Eq. 2 yields ( _α |_<sup>˜</sup> _↓⟩_ + _β |_<sup>˜</sup> _↑⟩_ ) _|_ 0 _⟩→ |_<sup>˜</sup> _↓⟩_ ( _α |_ 0 _⟩_ + _β |_ 1 _⟩_ ), thereby storing the input state in a superposition of the register ground state and a single collective excitation (a nuclear magnon). 

The physical realization of our central spin system is a QD device containing a GaAs droplet embedded in AlGaAs [38–40], the lattice matching of which results in low strain and correspondingly low nuclear quadrupolar broadening of 10 to 100 kHz [32, 35]. Our spin qubit is a conduction band electron confined to a volume containing _∼_ 10<sup>5</sup> spin-3/2 nuclei (Fig. 1b) distributed across the species<sup>75</sup> As, 69Ga and 71Ga with abundances of 100%, 60.1% and 39.9%, respectively [41]. We operate the QD device at 4 K with a 4.5-T in-plane magnetic field tilted 45° from the crystallographic axes, yielding _ωe/_ 2 _π_ = 2.5 GHz electron Zeeman splitting. In GaAs QDs, this field orientation together with the anisotropy of the electron g-factor results in the non-collinear coupling _a⊥_ [42, 43]. Electron spin initialization and readout are realized through resonant optical excitation, while coherent spin control is provided by a Raman scheme [11, 44] where a two-photon detuning determines _δ_ , and Ωis controlled by power of the two-color Raman laser (Fig. 1c). 

The transformative nature of nuclear homogeneity in GaAs QDs is revealed directly through the electron spin resonance (ESR) spectrum. In the un-driven system at thermal equilibrium, the fluctuating nuclear polarisation �( _Iz_ )<sup>2�</sup> = _NI_ ( _I_ + 1) _/_ 3 couples to the electron via the second term in Eq. 1 resulting in a spin dephasing time _T_ 2,<sup>_∗_</sup> _e_<sup>_≈_2.5 ns[35]andaninhomogeneousESRlinewidth</sup> 

3 



<!-- Start of picture text -->
Probe (~0.2 to 0.8 µs)<br>5<br>Init. π/2x Ωy π/2-x Read.<br>T<br><!-- End of picture text -->



<!-- Start of picture text -->
Total  5<br>polarisation Init. Inject + 69 Ga  Init. Inject - 71 Ga<br>71Ga 75As 69Ga 71Ga 75As 69Ga<br>0 polarisation 0 polarisation<br><!-- End of picture text -->



<!-- Start of picture text -->
Measurement<br><!-- End of picture text -->



<!-- Start of picture text -->
d Simulation<br><!-- End of picture text -->



<!-- Start of picture text -->
e<br>Simulation:<br><!-- End of picture text -->



<!-- Start of picture text -->
Unpolarized<br>Polarized<br><!-- End of picture text -->

Fig. 2. **Engineering a many-body dark state. a,** Experimental pulse sequence and its effects on nuclear polarisation. The polarize and probe steps use a NOVEL drive (rightmost inset) to inject polarisation into the species with _ωn_ = _|_ Ω _y|_ . In the probe step (illustrated for Ω _y >_ 0), NOVEL driving couples _|↑_<sup>˜</sup> , _j_ , _m⟩↔|↓_<sup>˜</sup> , _j_ , _m_ + 1 _⟩_ , and the final _π/_ 2 pulse maps _|_<sup>˜</sup> _↓⟩→|↓⟩_ before readout. **b,** Probe spectrum of the polarized nuclear ensemble as a function of probe time _T_ and Rabi frequency Ω _y_ . **c,** Probe spectra from an unpolarized (orange curve) and polarized nuclear ensemble (blue curve) after a _T_ = 130 ns probe. The polarized trace corresponds to the dotted horizontal line in **b** . **d,** Monte Carlo simulation of the probe step for an initial polarized nuclear state with<sup>71</sup> Ga in a dark state. **e,** Measured and simulated probe signals (see legend) as a function of probe time for a polarized nuclear ensemble when driving the<sup>71</sup> Ga[ _±_ ] sidebands. Circles and lines correspond to the<sup>71</sup> Ga vertical dashed lines in **b,d** . 

of 210 MHz. We overcome this limitation by preceding ESR measurements with quantum-algorithmic feedback (Fig. 1d pulse sequence) that locks _Iz_ [30, 34], prolonging the electron _T_ 2,<sup>_∗_</sup> _e_<sup>to290nsandyieldingacoherence-</sup> limited linewidth of 1.8-MHz FWHM (Supplementary Information). To avoid coherent broadening, we drive the electron in the detuned regime _δ ≫_ Ωwhere the Hartmann–Hahn condition manifests as sidebands in the ESR spectrum at _δ_ = _±ωn_ ( _±_ sideband) for each of the three nuclear species [11]. Figure 1d presents the measured ESR spectrum as a function of drive time. It contains electron Rabi oscillations at a rate of Ω _/_ 2 _π_ = 2.2 MHz for _δ_ = 0 and three pairs of symmetric sidebands at the expected nuclear Larmor frequencies. In stark contrast to previous InGaAs QDs [11, 31, 37], the individual atomic species as well as their isotopes are distinctly resolved. The relative peak amplitudes (Fig. 1e) are consistent with the species abundances and a 1 _/ωn_ -rolloff associated with detuned driving. This sideband-resolved regime of a qubit-ensemble interaction makes it possible to pump the ensemble to its ground state as done in optomechanical [45] and trapped atomic [46] systems. 

### **NUCLEAR DARK-STATE ENGINEERING** 

The species resolvability allows us to maintain a locked species-summed polarization ( _Iz_ = 0) by only actuating 75As while simultaneously engineering an undisturbed, pure nuclear state of a gallium isotope. We employ a cyclic pulse sequence (Fig. 2a) where the gallium isotopes are subjected to fast, directional polarisation injection via the NOVEL driving scheme [44, 47]: A _π/_ 2 _σ_ ˆ _x_ rotation followed by a _σ_ ˆ _y_ drive with Rabi frequency Ω _y_ configures the electron for spin-locking. The Hartmann–Hahn condition is fulfilled for _χ_ = _|_ Ω _y|_ = _ωn_ , and the drive phase ( _±σ_ ˆ _y_ ) dictates the direction of nuclear polarisation. By alternating between periods of NOVEL drive and optical repumping of the electron spin, polarization is repeatedly transferred from the electron to the gallium isotopes. We choose to pump the<sup>69</sup> Ga and<sup>71</sup> Ga ensembles in opposite directions such that their hyperfine shifts of the ESR frequency roughly cancel. We expect this anti-polarised configuration to be highly stable, as the<sup>75</sup> As-based feedback only needs to correct minor fluctuations around _Iz_ = 0. 

The resulting nuclear state is probed using another NOVEL drive (Fig. 2a). This time, an additional _π/_ 2- 

4 

pulse maps the dressed states back to the readout basis via _|_<sup>˜</sup> _↓⟩→|↓⟩_ . Figure 2b shows the measured spectrum as a function of probe time _T_ , with Fig. 3c displaying a linecut of the spectrum at _T_ = 130 ns. It contains the same nuclear resonances as Fig. 1d but differs in several important aspects. First, probing with Ω _y_ = 0 equates to Ramsey interferometry and a slow relaxation due to _T_ 2,<sup>_∗_</sup> _e_<sup>.</sup> Second, the nuclear sidebands are coherently broadened by the NOVEL drive. Third, while the sidebands of the feedback species<sup>75</sup> As remain symmetric, the<sup>69</sup> Ga and 71Ga sidebands are strongly asymmetric and in opposite directions as expected from an anti-polarized state. We observe a near-perfect suppression of the<sup>71</sup> Ga[ _−_ ] sideband - the clearest indication to date of a nuclear dark state [37]. Figure 2d shows a Monte Carlo simulation (Supplementary Information) where the initial nuclear states are sampled from a thermal, near-dark, and fully dark state for<sup>75</sup> As,<sup>69</sup> Ga and<sup>71</sup> Ga, respectively, showing remarkable agreement with the measured NOVEL spectrum. 

The observation of a dark state indicates a high level of purity of the<sup>71</sup> Ga ensemble. The<sup>71</sup> Ga[+] sideband corresponds to driving the _|↑_<sup>˜</sup> , 0 _⟩↔|↓_<sup>˜</sup> , 1 _⟩_ transition (c.f. Fig. 1a) and yields clear Rabi oscillations (Fig. 2e), further signifying the nuclear state purity and the coherence of the electro-nuclear coupling. The peak electron spin inversion at 130 ns corresponds to the injection of a single magnon at a Rabi frequency Ωmag _/_ 2 _π_ = 3.8 MHz. For the nuclear dark state, the theoretical magnon injection rate is Ωmag = _a⊥_ � _j/_ 2 (Supplementary Information). Measuring _a_<sup>(71)</sup> _⊥ /_ 2 _π_ = 50 kHz from an unpolarized NOVEL spectrum allows us to extract the dark state spin length _j_ = 0.6 _× j_ 0, where _j_ 0 is the independently measured maximum spin length (Supplementary Information). Notably, _j/j_ 0 is 100-fold larger than the thermal expectation value 1 _/√N_ [48], implying that the polarisation step pumps the total angular momentum. The initialization of a nuclear dark state _j < j_ 0 also implies considerable entanglement within the nuclear many-body system [37] and signifies that magnons are injected much faster than the nuclear decorrelation time. 

The magnon Rabi oscillations in Fig. 2e are damped by two predominant mechanisms. First, the spectral overlap of neighboring nuclear sidebands (evident from Fig. 2b) results in dephasing of the<sup>71</sup> Ga[+] transition. Second, spin relaxation proportional to laser power [44, 49] (visible as an increasing background at high _|_ Ω _y|_ in Fig. 2b) further damps the<sup>71</sup> Ga[+] oscillation. These two error mechanisms additionally imply a _∼_ 2% electron _π_ - pulse error and unwanted electron inversion when driving the suppressed<sup>71</sup> Ga[ _−_ ] transition (red circles in Fig. 2e), with both effects being of consequence to state transfer. A simulation including these errors together with a 0.9% spin initialization error produces the solid blue curve in Fig. 2e. The remaining discrepancy between the mea- 



<!-- Start of picture text -->
a e -<br>71Ga Magnon precession<br>b during precession during precession<br><!-- End of picture text -->

Fig. 3. **Sensing the Knight field with a single magnon. a,** Quantum circuit for magnon Ramsey interferometry. The protocol is preceded by the lock and polarize steps in Fig. 2a. **b,** Magnon Ramsey contrast _c_ = ( _p_ + _− p−_ ) _/_ ( _p_ + + _p−_ ), where _p±_ is the probability of projecting the electron onto _|±x⟩_ during the final readout in **a** . The two datasets (blue circles and red diamonds) denote different states of the electron spin during magnon precession. For both datasets, a damped sinusoid is fit to the entire time series (left and right) to estimate the electron spin-dependent precession frequency and thus the Knight shift. 

sured and simulated<sup>71</sup> Ga[+] oscillations in Fig. 2e may be due to additional control pulse errors or inhomogeneity of the dark state spin length _j_ . Nonetheless, the achieved visibility of the magnon Rabi oscillations is already sufficient to demonstrate quantum state transfer. 

### **QUANTUM STATE TRANSFER AND INFORMATION STORAGE** 

We now use the 130-ns NOVEL drive resonant with 71 Ga as an electro-nuclear SWAP gate. We first investigate the coherence dynamics of the nuclear states _|_ 0 _⟩_ and _|_ 1 _⟩_ through a magnon Ramsey interferometry protocol comprised of two SWAP gates with an intermediate delay, illustrated in Fig. 3a. The first SWAP gate maps the electron superposition state _|_ + _x⟩_ = ( _|↓⟩_ + _|↑⟩_ ) _/√_ 2 to the nuclear state ( _|_ 0 _⟩_ + _|_ 1 _⟩_ ) _/√_ 2, i.e. a coherent superposition of the ensemble dark state and a single nuclear magnon. This state precesses in the magnetic field at the nuclear Larmor frequency for time _T_ R after which it is transferred back via the second SWAP gate to the electron, which is measured in the _x_ -basis. An electron reset operation immediately after the first SWAP guarantees that the quantum state is stored in the<sup>71</sup> Ga mode, and an optional _x_ -gate toggles the electron state during nuclear precession. A second reset repolarizes the electron immediately before the second SWAP. Figure 3b shows the measured Ramsey fringes and reveals a nuclear state precession frequency _ν_<sup>_↑_</sup> = 58.560(9) MHz or _ν_<sup>_↓_</sup> = 59.060(8) MHz when the electron is in _|↑⟩_ or _|↓⟩_ during precession, respectively. The mean frequency ( _ν_<sup>_↑_</sup> + _ν_<sup>_↓_</sup> ) _/_ 2 = 58.810(6) MHz is in 



<!-- Start of picture text -->
Titore/2 Titore/2<br>gy Sl md<br>Probability<br>0.00 0.25 0.50 0.75 1.00<br>Ideal Measurement Simulation<br>Zz F=0.686(4) F=0.730<br>9 +z<br>©<br>w y<br>Eel<br>£ x<br>+X<br>+X - X +y - y +z - z +X - X +y - y +z - z +X - X +y - y +z - z<br>Readout projection<br>po sal  go<br>=)<br>[2]<br>2 '<br>20.2 1 4 Noinversion : .<br>1%] o :<br>£ # Inversion :<br>0.0 : : wn S<br>10 71 10° 10! 102<br>Storage time Tgtore (US)<br><!-- End of picture text -->

6 

_|_ +1 _/_ 2 _⟩_ nuclear transition and perform dynamical decoupling, which has already resulted in 20-ms coherence in GaAs QDs [32]. Further nuclear environmental control measures including repeated electron inversion or fast charge control may protect against higher-order electronmediated dephasing [52]. Regarding the full process fidelity, the spectral overlap of different species under NOVEL drive is the main imperfection, currently leading to a 23% simulated infidelity. This error can be suppressed by reducing _a⊥_ through magnetic field alignment [42] or net nuclear polarisation [43]. Eliminating<sup>69</sup> Ga through isotopic purification will further reduce overlap. In the ideal case of a<sup>71</sup> Ga/<sup>75</sup> As QD with both species in _j_ = 0.6 _× j_ 0 dark states, the simulated overlap error only induces a1.7% infidelity for the current value of _a⊥_ . Alternatively, Hamiltonian engineering may be used to achieve species-selective transfer while remaining insensitive to electron _T_ 2,<sup>_∗_</sup> _e_<sup>[25].</sup> The laser-induced electron spin relaxation [44, 49] currently contributes an 8.5% infidelity which can likely be improved through device design and enhanced optical mode matching to reduce the optical power needed for qubit control. 

### **CONCLUSION AND OUTLOOK** 

In summary, we have demonstrated a functional quantum register based on a nuclear many-body system interfaced with an electron spin qubit. When operated as a memory, this many-body register transforms QDs into fully fledged quantum network nodes. The current storage time of _T_ 2,<sup>_∗_</sup> _n_<sup>= 130(16) µsisalreadysufficientfor fast</sup> protocols such as 2d-cluster state generation [12, 13] and Bell state analysers [53]. _T_ 2,<sup>_∗_</sup> _n_<sup>alreadygreatlyexceeds</sup> the _T_ 2,<sup>_∗_</sup> _e_<sup>of the electron spin qubit,and while it is equiva-</sup> lent to the dynamically decoupled electron spin coherence time [35], NMR control will extend the nuclear coherence time to the 20 ms regime [32]. Another opportunity is presented by the remaining nuclear species, which can operate in parallel to increase the quantum information storage capacity of our device. Beyond quantum node development, our demonstrated control of a central spin system in the coherent regime enables foundational studies of collective phenomena including super-radiant nuclear spin dynamics, time-crystalline behavior [54] and engineering of many-body singlets [55]. 

### **ACKNOWLEDGEMENTS** 

We would like to thank E. Chekhovich for fruitful discussions, as well as M. Tribble for device fabrication advice. We additionally acknowledge support from the US Office of Naval Research Global (N62909-19-12115;M.A.), the EU Horizon 2020 FET Open project QLUSTER (862035; M.A. and C.L.G), the EU Hori- 

zon 2020 research and innovation program under Marie Sklodowska-Curie grant QUDOT-TECH (861097; M.A.), the Royal Society (EA/181068; C.L.G), Qurope (899814; A.R.), ASCENT+ (871130; A.R.), the Austrian Science Fund (FWF; 10.55776/COE1; A.R.), the EU NextGenerationEU (10.55776/FG5; A.R.), and SERB India (CRG/2023/007444; S.M.). L.Z. acknowledges support from the EPSRC DTP (EP/R513180/1) and A.G. from a Harding scholarship and a Christ’s College scholarship. D.A.G acknowledges a Royal Society University Research Fellowship. C.L.G. acknowledges a Dorothy Hodgkin Royal Society Fellowship. 

- _∗_ Correspondence to: dag50@cam.ac.uk 

- Correspondence to: ma424@cam.ac.uk 

- [1] H.-J. Briegel, W. D¨ur, J. I. Cirac, and P. Zoller, Quantum Repeaters: The Role of Imperfect Local Operations in Quantum Communication, Phys. Rev. Lett. **81** , 5932 (1998). 

- [2] S. Wehner, D. Elkouss, and R. Hanson, Quantum internet: A vision for the road ahead, Science **362** , eaam9288 (2018). 

- [3] M. K. Bhaskar, R. Riedinger, B. Machielse, D. S. Levonian, C. T. Nguyen, E. N. Knall, H. Park, D. Englund, M. Lonˇcar, D. D. Sukachev, and M. D. Lukin, Experimental demonstration of memory-enhanced quantum communication, Nature **580** , 60 (2020). 

- [4] M. Pompili, S. L. N. Hermans, S. Baier, H. K. C. Beukers, P. C. Humphreys, R. N. Schouten, R. F. L. Vermeulen, M. J. Tiggelman, L. dos Santos Martins, B. Dirkse, S. Wehner, and R. Hanson, Realization of a multinode quantum network of remote solid-state qubits, Science **372** , 259 (2021). 

- [5] L. Zhai, G. N. Nguyen, C. Spinnler, J. Ritzmann, M. C. L¨obl, A. D. Wieck, A. Ludwig, A. Javadi, and R. J. Warburton, Quantum interference of identical photons from remote GaAs quantum dots, Nat. Nanotechnol. **17** , 829 (2022). 

- [6] R. Uppu, F. T. Pedersen, Y. Wang, C. T. Olesen, C. Papon, X. Zhou, L. Midolo, S. Scholz, A. D. Wieck, A. Ludwig, and P. Lodahl, Scalable integrated single-photon source, Sci. Adv. **6** , eabc8268 (2020). 

- [7] N. Tomm, A. Javadi, N. O. Antoniadis, D. Najer, M. C. L¨obl, A. R. Korsch, R. Schott, S. R. Valentin, A. D. Wieck, A. Ludwig, and R. J. Warburton, A bright and fast source of coherent single photons, Nat. Nanotechnol. **16** , 399 (2021). 

- [8] B. Urbaszek, X. Marie, T. Amand, O. Krebs, P. Voisin, P. Maletinsky, A. H¨ogele, and A. Imamoglu, Nuclear spin physics in quantum dots: An optical investigation, Rev. Mod. Phys. **85** , 79 (2013). 

- [9] J. M. Taylor, A. Imamoglu, and M. D. Lukin, Controlling a Mesoscopic Spin Environment by Quantum Bit Manipulation, Phys. Rev. Lett. **91** , 246802 (2003). 

- [10] J. M. Taylor, C. M. Marcus, and M. D. Lukin, Long-Lived Memory for Mesoscopic Quantum Bits, Phys. Rev. Lett. **90** , 206803 (2003). 

- [11] D. A. Gangloff, G. Ethier<sup>´</sup> Majcher, C. Lang, E. V. Denning, J. H. Bodey, D. M. Jackson, E. Clarke, M. Hugues, 

7 

   - C. Le Gall, and M. Atat¨ure, Quantum interface of an electron and a nuclear ensemble, Science **364** , 62 (2019). 

- [12] D. Buterakos, E. Barnes, and S. E. Economou, Deterministic Generation of All-Photonic Quantum Repeaters from Solid-State Emitters, Phys. Rev. X **7** , 041023 (2017). 

- [13] C. P. Michaels, J. A. Mart´ınez, R. Debroux, R. A. Parker, A. M. Stramma, L. I. Huber, C. M. Purser, M. Atat¨ure, and D. A. Gangloff, Multidimensional cluster states using a single spin-photon interface coupled strongly to an intrinsic nuclear register, Quantum **5** , 565 (2021). 

- [14] M. V. G. Dutt, L. Childress, L. Jiang, E. Togan, J. Maze, F. Jelezko, A. S. Zibrov, P. R. Hemmer, and M. D. Lukin, Quantum Register Based on Individual Electronic and Nuclear Spin Qubits in Diamond, Science **316** , 1312 (2007). 

- [15] T. H. Taminiau, J. J. T. Wagenaar, T. van der Sar, F. Jelezko, V. V. Dobrovitski, and R. Hanson, Detection and Control of Individual Nuclear Spins Using a Weakly Coupled Electron Spin, Phys. Rev. Lett. **109** , 137602 (2012). 

- [16] P. C. Maurer, G. Kucsko, C. Latta, L. Jiang, N. Y. Yao, S. D. Bennett, F. Pastawski, D. Hunger, N. Chisholm, M. Markham, D. J. Twitchen, J. I. Cirac, and M. D. Lukin, Room-Temperature Quantum Bit Memory Exceeding One Second, Science **336** , 1283 (2012). 

- [17] P.-J. Stas, Y. Q. Huan, B. Machielse, E. N. Knall, A. Suleymanzade, B. Pingault, M. Sutula, S. W. Ding, C. M. Knaut, D. R. Assumpcao, Y.-C. Wei, M. K. Bhaskar, R. Riedinger, D. D. Sukachev, H. Park, M. Lonˇcar, D. S. Levonian, and M. D. Lukin, Robust multi-qubit quantum network node with integrated error detection, Science **378** , 557 (2022). 

- [18] A. Bourassa, C. P. Anderson, K. C. Miao, M. Onizhuk, H. Ma, A. L. Crook, H. Abe, J. Ul-Hassan, T. Ohshima, N. T. Son, G. Galli, and D. D. Awschalom, Entanglement and control of single nuclear spins in isotopically engineered silicon carbide, Nat. Mater. **19** , 1319 (2020). 

- [19] P. Drmota, D. Main, D. Nadlinger, B. Nichol, M. Weber, E. Ainley, A. Agrawal, R. Srinivas, G. Araneda, C. Ballance, and D. Lucas, Robust Quantum Memory in a Trapped-Ion Quantum Network Node, Phys. Rev. Lett. **130** , 090803 (2023). 

- [20] A. Ruskuc, C.-J. Wu, J. Rochman, J. Choi, and A. Faraon, Nuclear spin-wave quantum register for a solid-state qubit, Nature **602** , 408 (2022). 

- [21] A. Bechtold, D. Rauch, F. Li, T. Simmet, P.-L. Ardelt, A. Regler, K. M¨uller, N. A. Sinitsyn, and J. J. Finley, Three-stage decoherence dynamics of an electron spin qubit in an optically active quantum dot, Nature Physics **11** , 1005 (2015). 

- [22] F. K. Malinowski, F. Martins, P. D. Nissen, E. Barnes, L. Cywinski, M. S. Rudner, S. Fallahi, G. C. Gardner, M. J. Manfra, C. M. Marcus, and F. Kuemmeth, Notch filtering the nuclear environment of a spin qubit, Nat. Nanotechnol. **12** , 16 (2016). 

- [23] R. Stockill, C. Le Gall, C. Matthiesen, L. Huthmacher, E. Clarke, M. Hugues, and M. Atat¨ure, Quantum dot spin coherence governed by a strained nuclear environment, Nat. Commun. **7** , 1 (2016). 

- [24] W. Ding, A. Shi, J. Q. You, and W. Zhang, High-fidelity quantum memory utilizing inhomogeneous nuclear polarization in a quantum dot, Phys. Rev. B **90** , 235421 (2014). 

- [25] E. V. Denning, D. A. Gangloff, M. Atat¨ure, J. Mørk, and C. Le Gall, Collective Quantum Memory Activated by a Driven Central Spin, Phys. Rev. Lett. **123** , 140502 (2019). 

- [26] A. E. Kozhekin, K. Mølmer, and E. Polzik, Quantum memory for light, Phys. Rev. A **62** , 033809 (2000). 

- [27] Y. Tabuchi, S. Ishino, A. Noguchi, T. Ishikawa, R. Yamazaki, K. Usami, and Y. Nakamura, Coherent coupling between a ferromagnetic magnon and a superconducting qubit, Science **349** , 405 (2015). 

- [28] A. Eickbusch, V. Sivak, A. Z. Ding, S. S. Elder, S. R. Jha, J. Venkatraman, B. Royer, S. M. Girvin, R. J. Schoelkopf, and M. H. Devoret, Fast universal control of an oscillator with weak dispersive coupling to a qubit, Nat. Phys. **18** , 1464 (2022). 

- [29] A. H¨ogele, M. Kroner, C. Latta, M. Claassen, I. Carusotto, C. Bulutay, and A. Imamoglu, Dynamic Nuclear Spin Polarization in the Resonant Laser Excitation of an InGaAs Quantum Dot, Phys. Rev. Lett. **108** , 197403 (2012). 

- [30] D. M. Jackson, U. Haeusler, L. Zaporski, J. H. Bodey, N. Shofer, E. Clarke, M. Hugues, M. Atat¨ure, C. Le Gall, and D. A. Gangloff, Optimal Purification of a Spin Ensemble by Quantum-Algorithmic Feedback, Phys. Rev. X **12** , 031014 (2022). 

- [31] D. M. Jackson, D. A. Gangloff, J. H. Bodey, L. Zaporski, C. Bachorz, E. Clarke, M. Hugues, C. Le Gall, and M. Atat¨ure, Quantum sensing of a coherent single spin excitation in a nuclear ensemble, Nat. Phys. **17** , 585 (2021). 

- [32] E. A. Chekhovich, S. F. C. da Silva, and A. Rastelli, Nuclear spin quantum register in an optically active semiconductor quantum dot, Nat. Nanotechnol. **15** , 999 (2020). 

- [33] P. Millington-Hotze, H. E. Dyte, S. Manna, S. F. Covre da Silva, A. Rastelli, and E. A. Chekhovich, Approaching a fully-polarized state of nuclear spins in a solid, Nat. Commun. **15** , 985 (2024). 

- [34] G. N. Nguyen, C. Spinnler, M. R. Hogg, L. Zhai, A. Javadi, C. A. Schrader, M. Erbe, M. Wyss, J. Ritzmann, H.-G. Babin, A. D. Wieck, A. Ludwig, and R. J. Warburton, Enhanced Electron-Spin Coherence in a GaAs Quantum Emitter, Phys. Rev. Lett. **131** , 210805 (2023). 

- [35] L. Zaporski, N. Shofer, J. H. Bodey, S. Manna, G. Gillard, M. H. Appel, C. Schimpf, S. F. Covre Da Silva, J. Jarman, G. Delamare, G. Park, U. Haeusler, E. A. Chekhovich, A. Rastelli, D. A. Gangloff, M. Atat¨ure, and C. Le Gall, Ideal refocusing of an optically active spin qubit under strong hyperfine interactions, Nat. Nanotechnol. **18** , 257 (2023). 

- [36] S. R. Hartmann and E. L. Hahn, Nuclear Double Resonance in the Rotating Frame, Phys. Rev. **128** , 2042 (1962). 

- [37] D. A. Gangloff, L. Zaporski, J. H. Bodey, C. Bachorz, D. M. Jackson, G. Ethier<sup>´</sup> Majcher, C. Lang, E. Clarke, M. Hugues, C. Le Gall, and M. Atat¨ure, Witnessing quantum correlations in a nuclear ensemble via an electron spin qubit, Nat. Phys. **17** , 1247 (2021). 

- [38] Y. H. Huo, A. Rastelli, and O. G. Schmidt, Ultra-small excitonic fine structure splitting in highly symmetric quantum dots on GaAs (001) substrate, Appl. Phys. Lett. **102** , 152105 (2013). 

8 

- [39] D. Huber, M. Reindl, Y. Huo, H. Huang, J. S. Wildmann, O. G. Schmidt, A. Rastelli, and R. Trotta, Highly indistinguishable and strongly entangled photons from symmetric GaAs quantum dots, Nat. Commun. **8** , 15506 (2017). 

075302 (2023). 

   - [55] L. Zaporski, S. R. de Wit, T. Isogawa, M. Hayhurst Appel, C. Le Gall, M. Atat¨ure, and D. A. Gangloff, ManyBody Singlet Prepared by a Central-Spin Qubit, PRX Quantum **4** , 040343 (2023). 

- [40] E. A. Chekhovich, A. Ulhaq, E. Zallo, F. Ding, O. G. Schmidt, and M. S. Skolnick, Measurement of the spin temperature of optically cooled nuclei and GaAs hyperfine constants in GaAs/AlGaAs quantum dots, Nat. Mater. **16** , 982 (2017). 

- [41] M. Berglund and M. E. Wieser, Isotopic compositions of the elements 2009 (IUPAC Technical Report), Pure Appl. Chem. **83** , 397 (2011). 

- [42] T. Botzem, R. P. G. McNeil, J.-M. Mol, D. Schuh, D. Bougeard, and H. Bluhm, Quadrupolar and anisotropy effects on dephasing in two-electron spin qubits in GaAs, Nat. Commun. **7** , 11170 (2016). 

- [43] N. Shofer, Tuning the coherent interaction of an electron qubit and a nuclear magnon, Recently submitted **TBD** (2024). 

- [44] J. H. Bodey, R. Stockill, E. V. Denning, D. A. Gangloff, G. Ethier Majcher, D. M. Jackson, E. Clarke, M. Hugues,<sup>´</sup> C. L. Gall, and M. Atat¨ure, Optical spin locking of a solid-state qubit, npj Quantum Inf. **5** , 95 (2019). 

- [45] A. Schliesser, O. Arcizet, R. Rivi`ere, G. Anetsberger, and T. J. Kippenberg, Resolved-sideband cooling and position measurement of a micromechanical oscillator close to the Heisenberg uncertainty limit, Nat. Phys **5** , 509 (2009). 

- [46] D. J. Wineland and W. M. Itano, Laser cooling of atoms, Phys. Rev. A **20** , 1521 (1979). 

- [47] A. Henstra, P. Dirksen, J. Schmidt, and W. Wenckebach, Nuclear spin orientation via electron spin locking (NOVEL), J. Magn. Reson. **77** , 389 (1987). 

- [48] J. Wesenberg and K. Mølmer, Mixed collective states of many spins, Phys. Rev. A **65** , 062304 (2002). 

- [49] M. H. Appel, A. Tiranov, S. Pabst, M. L. Chan, C. Starup, Y. Wang, L. Midolo, K. Tiurev, S. Scholz, A. D. Wieck, A. Ludwig, A. S. Sørensen, and P. Lodahl, Entangling a Hole Spin with a Time-Bin Photon: A Waveguide Approach for Quantum Dot Sources of Multiphoton Entanglement, Phys. Rev. Lett. **128** , 233602 (2022). 

- [50] C. W. Lai, P. Maletinsky, A. Badolato, and A. Imamoglu, Knight-Field-Enabled Nuclear Spin Polarization in Single Quantum Dots, Phys. Rev. Lett. **96** , 167403 (2006). 

- [51] G. Sallen, S. Kunz, T. Amand, L. Bouet, T. Kuroda, T. Mano, D. Paget, O. Krebs, X. Marie, K. Sakoda, and B. Urbaszek, Nuclear magnetization in gallium arsenide quantum dots at zero magnetic field, Nat Commun **5** , 3268 (2014). 

- [52] G. W¨ust, M. Munsch, F. Maier, A. V. Kuhlmann, A. Ludwig, A. D. Wieck, D. Loss, M. Poggio, and R. J. Warburton, Role of the electron spin in determining the coherence of the nuclear spins in a quantum dot, Nat. Nanotechnol. **11** , 885 (2016). 

- [53] D. Witthaut, M. D. Lukin, and A. S. Sørensen, Photon sorters and QND detectors using single photon emitters, Epl **97** , 50007 (2012). 

- [54] R. Frantzeskakis, J. Van Dyke, L. Zaporski, D. A. Gangloff, C. Le Gall, M. Atat¨ure, S. E. Economou, and E. Barnes, Time-crystalline behavior in central-spin models with Heisenberg interactions, Phys. Rev. B **108** , 

## **Supplementary information: Many-body quantum register for a spin qubit** 

Martin Hayhurst Appel,<sup>1</sup> Alexander Ghorbal,<sup>1</sup> Noah Shofer,<sup>1</sup> Leon Zaporski,<sup>1</sup> Santanu Manna,<sup>2</sup> Saimon Filipe Covre da Silva,<sup>2</sup> Urs Haeusler,<sup>1</sup> Claire Le Gall,<sup>1</sup> Armando Rastelli,<sup>2</sup> Dorian A. Gangloff,<sup>1,</sup><sup>_∗_</sup> and Mete Atat¨ure<sup>1,</sup><sup>_†_</sup> 

> 1 _Cavendish Laboratory, University of Cambridge, J.J. Thomson Avenue, Cambridge, CB3 0HE, UK_ 

> 2 _Institute of Semiconductor and Solid State Physics, Johannes Kepler University, Altenberger Str. 69, Linz 4040, Austria_ (Dated: May 1, 2024) 

### **CONTENTS** 

|1. Experimental setup|2|
|---|---|
|1.1. Sample details|2|
|1.2. Strain estimation|3|
|1.3. Optical setup|4|
|1.4. Spin readout and initialisation|5|
|1.5. Pulse sequences|6|
|2. Supplementary measurements|8|
|2.1. Ramsey interferometry with locked polarisation|8|
|2.2. Interpretation of higher-order magnon sidebands|9|
|2.3. Quantum register tomography|9|
|2.4. Magnon Ramsey|10|
|2.5. Quantum register storage time estimates|10|
|3. Estimation of the number of nuclei|13|
|4. System hamiltonian|14|
|4.1. Dressed state picture|14|
|5. Monte Carlo Simulation|16|
|5.1. Coherent evolution|16|
|5.2. Nuclear state sampling|16|
|5.3. Non unitary dynamics|17|
|5.4. Q-factor estimation|17|
|5.5. NOVEL probe simulation and anisotropy estimation|17|
|5.6. Simulating quantum register performance|20|
|6. Expected inhomogeneous dephasing time of the storage mode|20|
|7. Summary of system parameters|21|
|References|21|



> _∗_ Correspondence to: dag50@cam.ac.uk 

> _†_ Correspondence to: ma424@cam.ac.uk 

2 

### **1. EXPERIMENTAL SETUP** 

### **1.1. Sample details** 

Our quantum dot (QD) structure is grown via molecular beam epitaxy using Al-droplet etching and GaAs infilling to define the QDs. We refer to Ref. [1] for growth details. The QD device consists of a p-i-n diode with the GaAs QDs embedded in the intrinsic layer. The diode heterostructure is presented in Fig. 1a and is identical to the one utilized in Ref. [2] except for the thickness of the AlGaAs barrier immediately below the QD layer which was increased from 15 nm to 21 nm. To increase the light-matter coupling, the heterostructure contains a DBR mirror (6 pairs), and a super-hemispherical zirconia solid immersion lens is attached to the top of the heterostructure. By applying a weak forward bias across the diode, we can deterministically charge the QD. Fig. 1b shows a voltage-dependent photoluminescence measurement revealing discrete charge states including the negative charge state utilized in this work. 



<!-- Start of picture text -->
GaAs:C  p++<br>Al 0.15 Ga 0.85 As:C p++<br>Al0.15Ga0.85As:C p+<br><!-- End of picture text -->



<!-- Start of picture text -->
Al0.33Ga0.67As<br>Al0.33Ga0.67As<br>Al 0.15 Ga 0.85 As<br>Al0.15Ga0.85As:Si n+<br>Al0.15Ga0.85As<br>Al 0.95 Ga 0.05 As<br>Al 0.2 Ga 0.8 As<br>Al 0.95 Ga 0.05 As<br><!-- End of picture text -->



<!-- Start of picture text -->
GaAs substrate<br><!-- End of picture text -->



<!-- Start of picture text -->
X -<br><!-- End of picture text -->



FIG. 1. **a,** Schematic of the QD heterostructure. **b,** Photoluminescence spectrum of the studied QD. The QD is excited above bandgap with a 638 nm laser and the emission is resolved on a spectrometer. The emission line centered at 784.6 nm originates from the negative trion X<sup>_−_</sup> of a singly negatively charged QD. This charge state is stable under resonant excitation within the voltage range indicated by the dotted lines. 

3 

### **1.2. Strain estimation** 

We here briefly evidence that the non-collinear electro-nuclear coupling utilized in this work does not originate from strain. We follow Ref. [3] and use the splitting between the light hole (lh) and heavy hole (hh) emission lines of the free GaAs exciton as a proxy for strain. Fig. 2 shows photoluminescence measurements in which we observe a weak, linearly polarized hh emission and a doublet of partially polarized peaks corresponding to lh emission. We expect this emission to originate from the GaAs substrate in our device (bottom layer in Fig. 1a). Based on the low-energy lh peak, we extract a maximal lh-hh splitting of 4.9 meV. According to Ref. [3], this corresponds to a nuclear quadropolar shift _BQ/_ 2 _π_ of 89 kHz. Based on the single nuclear hyperfine coupling _a/_ 2 _π_ = 0.342 MHz and Larmor frequency _ωn/_ 2 _π_ = 58.41 MHz of the<sup>71</sup> Ga nuclear storage mode at 4.5 T (see table II), strain would lead to a non-collinear coupling [4] of _a⊥/_ 2 _π_ = _aBQ/_ (2 _πωn_ ) = 0.50 kHz which is less than 1% of the _a⊥/_ 2 _π_ = 51 kHz estimated in section 5.5. For this reason, we neglect strain effects in our modeling of the electro-nuclear interface. 



<!-- Start of picture text -->
6000<br>0 deg<br>lh lh hh 20 deg<br>5000 40 deg<br>60 deg<br>80 deg<br>4000 100 deg<br>120 deg<br>140 deg<br>3000 x 5 160 deg<br>180 deg<br>2000<br>1000<br>0<br>1.510 1.515 1.520<br>PL energy (eV)<br>Counts over 30 s<br><!-- End of picture text -->

FIG. 2. Photoluminescence measurement of the free GaAs exciton. The sample area containing the measured QD is excited with a 638 nm laser and the emission is resolved on a spectrometer. The legend indicates the orientation of the linear collection axis. For clarity, the spectra are also plotted with 5 _×_ magnification in the vicinity of the hh peak. 

4 

### **1.3. Optical setup** 

The QD device is held at 4 K inside a helium bath cryostat where a superconducting magnet produces a 4.5 T magnetic field in the z-direction (Fig. 3a). By mounting the QD sample sideways and additionally rotating it 45° around the optical axis, we obtain a magnetic field that is transverse to the QD growth axis and 45° in between the crystallographic [110] and [<sup>¯</sup> 110] axes. Figure 3a illustrates the optical setup. A resonant readout laser and a Raman laser are combined on a beam splitter and sent into the cryostat. The Raman laser is detuned 600 GHz from the trion states and is circularly polarized to avoid AC-stark shifts of the electron spin during driving [5] and to achieve spin Rabi frequencies up to 100 MHz. The readout laser is linearly polarized such that it only drives the _|↓⟩↔|⇓↑↓⟩_ transition and not the orthogonally polarized _|↑⟩↔|⇓↑↓⟩_ transition, see. Fig. 3b. Suppressing the latter transition significantly increases the spin initialization fidelity as this transition can otherwise off-resonantly repump the spin. We employ cross-polarisation to reject the resonant readout laser. Due to the linear excitation scheme, we only collect the H-polarized anti-Stokes Raman scattering. The polarisation-filtered emission is coupled into a fiber and spectrally filtered by a diffraction grating (30 GHz FWHM) to remove the Raman laser reflection. Finally, the QD emission is detected on an avalanche photodiode (APD) and time tagged with a Swabian Time Tagger 20. 

Our Raman scheme is based on the modulation of a CW-laser. The laser is modulated by a fibre-coupled amplitude electro-optical modulator (EOM) which is locked to its interferometric minimum and driven by microwave pulses generated from an arbitrary waveform generator (AWG). Driving the EOM at frequency _ωµw_ and phase _φ_ generates a pair of optical sidebands with splitting 2 _ωµw_ , phase difference 2 _φ_ , and resulting two-photon detuning _δ_ = _ωe −_ 2 _ωµw_ (Fig. 3b). This control scheme is further elaborated in Ref. [6]. Due to the modest _ωe_ , we directly synthesize the microwave pulses in the time domain. 

An acousto-optical modulator (AOM) placed after the EOM is used to stabilize the Raman power and to block EOM laser leakage during periods without Raman drive. An AOM is additionally used to create the resonant pumping pulses from the readout laser. The AOMs, AWG, and time tagger are all triggered by a Swabian Pulse Streamer. To ensure timing accuracy over long ( _>_ 100 µs) histograms, the Time Tagger and Pulse Streamer are locked to the AWG’s 10 MHz clock. 







<!-- Start of picture text -->
APD<br><!-- End of picture text -->







<!-- Start of picture text -->
Readout<br>laser<br>Legend:<br><!-- End of picture text -->







<!-- Start of picture text -->
Beamsplitter Linear polariser (LP)<br><!-- End of picture text -->



<!-- Start of picture text -->
Quater-wave plate (QWP) Diffraction grating<br><!-- End of picture text -->

FIG. 3. **a,** Optical setup. Two lasers are combined and sent onto the QD contained in a 4 K cryostat. Abbreviations are defined in the figure legend. The Raman control laser is made bichromatic by modulation with the AWG-driven EOM. The waveplates HWP1 and QWP1 result in a circularly polarised Raman laser field on the QD. The readout laser hits the fast axis of QWP1 and retains its linear polarisation. HWP2 is used to match the readout laser polarisation to the V-polarized transition (cf. panel b). The polarization optics QWP2 and LP3 are used to reject the resonant laser reflection. Lenses and optical fibers have been omitted from the diagram. **b,** Energy level diagram of a negatively charged QD including relevant energy splittings of the measured QD. H and V indicate the linear polarisations of the optical dipoles with V pointing along the external magnetic field. 

5 

### **1.4. Spin readout and initialisation** 

We use 100 ns long resonant pumping pulses to initialize the QD in _|↑⟩_ and to read out the _|↓⟩_ state. Figure 4a shows a histogram of detected QD fluorescence during a pumping pulse given an initial _|↓⟩_ state. The initial rise time is a result of the _≈_ 6 ns rise time of the AOM used for pulsing. The readout counts reported in the manuscript are acquired by subtracting the counts in the second readout window from the first readout window (colored areas in Fig. 4a). This effectively subtracts the constant background owing to laser scatter and residual QD fluorescence. 

We now estimate the fidelity of spin initialization. We first estimate the background originating from laser scatter and detector dark counts by switching the QD to a non-resonant charge state. By subtracting this background, we obtain a corrected spin pumping histogram (Fig. 4b). We fit a single exponential decay to this histogram to estimate ˆ the initialization fidelity _F_ init = _⟨↑|_ ˆ _ρ_ end _|↑⟩_ , where _ρ_ end is the state after pumping. _F_ init can be estimated from [7] 



where _I_ 0 and _I_ end are the fluorescence intensities at the start and the end of the pumping, respectively. As this model assumes a temporally square pumping pulse, we extend the exponential fit in Fig. 4b backward in time until its area matches the measured area. From this fit, we extract _I_ 0 = 4146(72), _I_ end = 38.7(1.9) and _F_ init _≥_ 99.07(5)%. This estimate constitutes a lower bound as we have assumed perfect initialization of _|↓⟩_ prior to pumping. 







<!-- Start of picture text -->
b<br>I0<br>Iend<br><!-- End of picture text -->

FIG. 4. **a,** Histogram of a resonant readout pulse given a bright electron spin state (blue curve). The difference between the integrated counts in the green and orange areas constitutes the readout counts. The pulse at 190 ns is an optical reflection of a Raman _π_ -pulse. By recording a histogram with a non-resonant bias voltage, we additionally estimate a background histogram (black curve). **b,** Corrected histogram obtained by subtracting the histograms in **a** . The histogram is fit with the model _I_ ( _t_ ) = Θ( _t − t_ 0) ( _I_ 0 _− I_ end) _e_<sup>_−_(</sup><sup>_t−t_0)Γ</sup> + _I_ end , where Θ( _t_ ) is the Heaviside function and _t_ 0 is chosen to ensure an equal area of � � the fit and the data. We further extract a spin pumping time 1 _/_ Γ = 8.88(15) ns. 

6 

**1.5. Pulse sequences** 

Figure 5 details the pulse sequences used in this work. 



<!-- Start of picture text -->
a)  Lock<br>T sense(i) 60 ns Nlock<br>Lock = (π/2)x (Ωgate)x Init.<br>time<br>b)  Polarize<br>100 ns 100 ns 5<br>Polarize = (π/2)x (Ω1)y Init. (π/2)x (Ω2)-y Init. time<br>c)  Reference Rabi  T Rabi(i) Nrabi<br>Ref. Rabi = Init. Ω/2π = 90 MHz Read<br>time<br>d)  ESR probe (Fig. 1d of main text)<br>Intensity reference T probe T max- T probe vary sign of δ<br>Lock Init. π Read Ωp, ±δ Read Ωp, ±δ Read time<br>e)  NOVEL probe (Fig. 2 of main text) T probe(i) Nprobe<br>Lock Polarize (π/2)x (Ωprobe)y (π/2)-x Read Ref. Rabi time<br>f)  Memory/Magnon Ramsey (Fig. 3&4 of main text)<br>130 ns (optinal) 130 ns Nbases<br>Lock Polarize Init. Up(i) (π/2)x (Ω 71Ga ) -y Init. π Init. (π/2)x (Ω 71Ga ) -y Ut(i) Read Ref. Rabi time<br>Tstore<br>SWAP SWAP<br><!-- End of picture text -->

FIG. 5. Experimental pulse sequences. All _π_ and _π/_ 2 pulses use a Ω _/_ 2 _π_ = 90 MHz Rabi frequency and 5.6 ns and 2.7 ns durations, respectively. Readout (Read) and initialization (Init.) pulses are both 100 ns long. Additional comments are given in the supplementary text. 

The algorithmic locking sequence in Fig. 5a is explained in Ref. [8]. Ωgate _≈ ωn_ 75 _As_ = 2 _π ×_ 32.5 MHz is used to ensure selective activation of arsenic. For the electron spin resonance (ESR) experiment, we use _N_ lock = 30 steps with a sensing time _T_ sense linearly chirped from 30 to 185 ns. We find this saturates the electron _T_ 2<sup>_∗_.Forallsubsequent</sup> measurements, we use a shorter lock step with _N_ lock = 12 and _T_ sense chirped from 60 ns to 162 ns. 

For the polarize step in Fig. 5b, we choose Ω1 _/_ 2 _π_ = 44 MHz and Ω2 _/_ 2 _π_ = 56 MHz to target<sup>69</sup> Ga and<sup>71</sup> Ga, respectively. The opposite drive phases + _y_ and _−y_ antipolarize the two species as explained in the main text. 

To achieve accurate spin Rabi frequencies, we include reference Rabi measurements where spin inversion is measured after Rabi drives with _T_ Rabi = 0, 2, 4..80 ns (Fig. 5c). This allows us to monitor the Rabi frequency on the fly and automatically adjust the Raman power setpoint in case of deviations. 

The ESR probing sequence (Fig. 5d) uses a single electron _π_ -pulse to estimate the readout counts for a fully inverted electron. Next, it contains two rounds of detuned driving with durations _T_ probe and _T_ max _− T_ probe. This ensures a constant duty cycle when _T_ probe is scanned from 0 to _T_ max. Additionally, the two driving steps are repeated with the opposite drive detuning to avoid the build-up of nuclear polarization. For the NOVEL probe (Fig. 5e), we first include the lock and polarize steps. The probe step consists of a NOVEL drive with spin locking Rabi frequency Ωprobe for duration _T_ probe. We repeat the lock-polarize-probe segment for all values of _T_ probe such that a single histogram contains measurements of all drive times for a single Ωprobe value. The pulse sequence is then updated with a new value of Ωprobe. The pulse sequence additionally contains a reference Rabi for long-term stabilization of all electron Rabi frequencies and for establishing the readout counts from _|↓⟩_ . When recording the thermal NOVEL spectrum (Fig. 14), we keep the polarize step but shift its waveform carrier frequency by 500 MHz (yielding a detuning _δ/_ 2 _π_ = 1 GHz), thus suppressing coherent dynamics while maintaining the optical power. 

For the magnon Ramsey and memory sequences (Fig. 5f), we include all different combinations of preparation 

7 

_Up_ and tomography pulses _Ut_ in the same histogram. Note that _T_ store is defined as the delay between the nuclearresonant spin locking pulses and cannot be reduced below 280 ns due to the intermediate pulses and inter-pulse delays. When varying _T_ store, we repeat the lock and polarize steps 3 times to compensate for the low duty cycle at long storage times. We include a reference Rabi measurement for the reasons discussed above. 

We now elaborate on the effect of the electron control pulses in Fig. 5f. Following previous studies of QDs, we assume a negative electron g-factor such that the bare electron spin state _|↑⟩_ is on the south pole of the Bloch Sphere (Fig. 6a). To realize the SWAP gate, we always apply a ( _π/_ 2) _x_ rotation before driving around the _−y_ axis. The rotation maps _|↑⟩_ and _|↓⟩_ to the dressed states _|_<sup>˜</sup> _↓⟩_ and _|_<sup>˜</sup> _↑⟩_ as defined by the (Ω) _−y_ drive. This mapping constricts the electro-nuclear state to the register manifold (Fig. 6b) during the second half of the protocol where the spin is initialized in _|↑⟩_ and subjected to a second SWAP. Strictly speaking, the second SWAP gate (Fig. 5f) is missing a local _U_ ˆ _t_ rotation.electronTablerotationI enumeratesrequired tothemaprotationthe dressedpulsesstatesusedbackto realizeto theallz-basis.6 inputWeandinsteadprojectiveincludemeasurementsthis rotation inin thethe quantum tomography (main text Fig. 4b). The fact that the optical readout always prepares _|↑⟩_ but can only read _|↓⟩_ is reflected in the choice of tomography rotations. 

|State|Preparation, <sup>ˆ</sup>_Up_|Tomography, <sup>ˆ</sup>_Ut_|
|---|---|---|
|+_x_|(_π/_2)_−y_|(_π/_2)_−y_|
|_−x_|(_π/_2)_y_|(_π/_2)_y_|
|+_y_|(_π/_2)_x_|I|
|_−y_|(_π/_2)_−x_|(_π_)_x_|
|+_z_|_πx_|(_π/_2)_−x_|
|_−z_|I|(_π/_2)_x_|



TABLE I. Local electron rotations used to prepare the initial state _|ψ_ 0 _⟩_ and to project the output state onto a target state. 



<!-- Start of picture text -->
a b<br>Register<br>manifold<br>(initial state)<br><!-- End of picture text -->

FIG. 6. Electron spin rotations used for state transfer. **a,** The electron spin on the Bloch Sphere. During the state transfer, the Ω _−y_ spin locking drive (red arrow) defines the high-energy dressed state _|↑⟩_<sup>˜</sup> and the low-energy dressed state _|↓⟩_<sup>˜</sup> to be along _|−y⟩_ and _|_ + _y⟩_ , respectively. **b,** Register manifold reproduced from main text Fig. 1a. 

8 

### **2. SUPPLEMENTARY MEASUREMENTS** 

### **2.1. Ramsey interferometry with locked polarisation** 

Figure 7 shows a Ramsey measurement of the electron spin coherence after applying the same nuclear polarisation locking step (Fig. 5a) used in the measurement of the ESR spectrum (Fig. 1d main text). We implement two Ramsey sequences with identical delays but opposite phases for the final _π/_ 2 pulses (Fig. 7 inset). The two sequences yield detection counts _n_ 1 and _n_ 2 from which the visibility _v_ = ( _n_ 1 _− n_ 2) _/_ ( _n_ 1 + _n_ 2) is estimated. The estimated dephasing time _T_ 2<sup>_∗_= 290(7) ns corresponds to a Overhauser-induced fluctuation of the qubit detuning</sup><sup>_δ_with</sup> _√_ 2 _/T_ 2<sup>_∗_=</sup> 2 _π ×_ 0.78(2) MHz standard deviation and 2 _π ×_ 1.83(4) MHz FWHM. 



<!-- Start of picture text -->
T Ramsey T Ramsey<br>Lock Init. (π/2)x (π/2)x Read (π/2)x (π/2)-x Read time<br><!-- End of picture text -->

FIG. 7. Electron Ramsey measurement preceded by polarisation locking (top inset). The function _v_ ( _t_ ) = _v_ 0 _× e_<sup>_−_(</sup><sup>_t/T_</sup> 2<sup>_∗_)</sup><sup>_α_</sup> (red curve) is fit to the measured Ramsey visibility (blue points). The extracted fit parameters are _{v_ 0, _T_ 2<sup>_∗_,</sup><sup>_α}_=</sup> _{_ 0.87(2), 290(7) ns, 1.62(10) _}_ . 

9 

### **2.2. Interpretation of higher-order magnon sidebands** 

We now explain the additional features of the measured ESR spectrum (main text Fig. 1d) which is replotted in Fig. 8 with additional lines indicating features of interest. Firstly, the three-body resonances (between the electron spin and two nuclei) predicted by Eq. (19) result in ESR peaks at the differences of nuclear Larmor frequencies. For negative drive detunings, we see clear peaks at the expected resonances (solid gray lines). Surprisingly, for positive detunings, the peaks are far less pronounced. This asymmetry may be an artifact of the specific pulse sequence as the three-body sidebands appear symmetric under NOVEL probing (Fig. 14). Due to the regular spacing of the nuclear Larmor frequencies, we cannot resolve the<sup>69</sup> Ga _−_<sup>75</sup> As transitions from the<sup>71</sup> Ga _−_<sup>69</sup> As transitions. 

Secondly, we observe a signature of the second-order arsenic transition (blue dashed line in Fig. 8) whereby two excitations are injected into the arsenic ensemble. The large ratio between the first and second-order Arsenic transitions is compatible with a non-collinear interaction dominated by electron g-factor anisotropy, as strain would result in a ratio close to unity (cf. ESR spectrum in Ref. [4]). 







FIG. 8. ESR spectrum resulting from an unpolarized nuclear ensemble with locked _Iz ∼_ 0 (reproduced main text Fig.1e-f). The additional three-body resonances (gray lines) and the second-order Arsenic transition (blue dashed line) have been marked. 

### **2.3. Quantum register tomography** 

In the quantum tomography in Fig. 4b of the main text, we convert the measured counts to probabilities by normalizing to pairs of orthogonal readouts: The reported probability _pa_ , _b_ of detecting output _|b⟩_ given input _|a⟩_ is estimated from _pa_ , _b_ = _na_ , _b/_ ( _na_ , _b_ + _na_ , _b′_ ) where _n_ is the number of detected counts and _⟨b_<sup>_′_</sup> _|b⟩_ = 0. To estimate the register storage fidelity, we first define the contrasts 



for _α ∈{x_ , _y_ , _z}_ . Following Ref.[9], we calculate the storage fidelity _F_ = (1 +<sup><u>1</u></sup> 3<sup>(</sup><sup>_Cx_+</sup><sup>_Cy_+</sup><sup>_Cz_))</sup><sup>_/_2andpropagatethe</sup> shot noise errors from _na_ , _b_ onto _F_ . 

10 

### **2.4. Magnon Ramsey** 

We perform the magnon Ramsey measurement from main text Fig. 3 using the pulse sequence in Fig. 5f. We utilize four combinations of _Up_ and _Ut_ to realize the initial states _|±x⟩_ and projective measurements of _|±x⟩_ . For each storage time _T_ store, we extract a _Cx_ contrast using Eq. (2). 

Fig. 9 shows a supplementary magnon Ramsey measurement where _T_ store is scanned from 280 ns to 1280 ns in steps of 8 ns. The Nyquist frequency 0.5 _/_ (8 ns) = 62.5 MHz is sufficient to resolve the<sup>71</sup> Ga Larmor frequency but leads to the visual illusion of a much slower oscillation. By fitting the data, we obtain the frequency estimates _ν_<sup>_↑_</sup> = 58.810(11) MHz and _ν_<sup>_↓_</sup> = 59.307(10) MHz for the electron stored in _|↑⟩_ and _|↓⟩_ , respectively. The mean frequency ( _ν_<sup>_↑_</sup> + _ν_<sup>_↓_</sup> ) _/_ 2 = 59.059(8) MHz differs from the 58.810(6) MHz estimate reported in the main text. We attribute the difference to a slow discharge of our superconducting magnet coils as the two measurements were taken several days apart. However, the hyperfine-induced frequency difference _ν_<sup>_↓_</sup> _− ν_<sup>_↑_</sup> = 0.497(15) MHz estimated from Fig. 9 is in statistical agreement with the 0.500(12) MHz value reported in the main text. The longer dephasing time observed in Fig. 9 for _|↓⟩_ can be attributed to a partial Knight shift rephasing owing to the included electron inversion. 



<!-- Start of picture text -->
|  during precession |  during precession<br>0.4 0.4<br>0.2 0.2<br>0.0 0.0<br>0.2 0.2<br>0.4 0.4<br>0.1 0.1<br>0.0 0.0<br>0.1 0.1<br>400 600 800 1000 1200 400 600 800 1000 1200<br>Storage time (ns) Storage time (ns)<br>Contrast<br>Fit residual<br><!-- End of picture text -->

FIG. 9. Supplementary measurement of magnon Ramsey. The left and right panels show measurements with the electron in _|↑⟩_ and _|↓⟩_ during precession, respectively. The Ramsey contrast (blue points) is fit with _Cx_ ( _t_ ) = _C_ 0 sin(2 _πνt_ + _φ_ ) _e_<sup>_−_(</sup><sup>_t/T_</sup> 2,mag<sup>_∗_)</sup><sup>_α_</sup> + _B_ (red lines). The bottom panels show the fit residuals. The left panel yields the fit parameters _{C_ 0, _ν_ , _φ_ , _T_ 2,mag<sup>_∗_,</sup><sup>_α_,</sup><sup>_B}_=</sup><sup>_{_0.339(10), 58.810(11) MHz,</sup><sup>_−_0.98(3), 1.4(2) µs, 2.6(9),</sup><sup>_−_2(4)</sup><sup>_·_10</sup><sup>_−_3</sup><sup>_}_.Therightpanelyields</sup> the fit parameters _{C_ 0, _ν_ , _φ_ , _T_ 2,mag<sup>_∗_,</sup><sup>_α_,</sup><sup>_B}_=</sup><sup>_{_0.353(8), 59.307(11) MHz,</sup><sup>_−_0.90(3), 1.9(1) µs, 3(6),</sup><sup>_−_5(4)</sup><sup>_·_10</sup><sup>_−_3</sup><sup>_}_.</sup> 

### **2.5. Quantum register storage time estimates** 

Fig. 10 shows the short segments of magnon Ramsey from which we extract the storage time-dependent Ramsey visibility in the presence of an electron spin inversion pulse. At each storage time, we store and retrieve the qubit state _|±x⟩_ , perform projective readout of _|±x⟩_ and estimate a _Cx_ contrast following Eq. (2). The contrast is fit with the model _Cx_ ( _t_ ) = _C_ 0 sin(2 _πνt_ + _φ_ ) + _B_ where _C_ 0 is the Ramsey visibility, _ν_ is the precession frequency, _φ_ is the fringe phase and _B_ is an empirical background. All four parameters are kept free across all datasets. As the storage time is increased, in addition to a decay _C_ 0, we observe a decay in the precession frequency _ν_ as evident from the final fits in Fig. 10. This frequency shift is plotted in Fig. 11. We do not currently understand the cause of this drift and have not identified any systematic errors in the synthesis of the control pulses determining the storage time. We note the stored qubit state persists in the nuclear ensemble despite the precession slowdown. 

11 



<!-- Start of picture text -->
0.4<br>0.2<br>0.0<br>0.2<br>0.4<br>= (58.9 ± 0.4) MHz = (60.1 ± 0.4) MHz = (58.3 ± 0.5) MHz = (57.7 ± 0.4) MHz = (58.4 ± 0.4) MHz<br>0.28 0.30 1.28 1.30 1.68 1.70 2.24 2.26 3.02 3.04<br>0.4<br>0.2<br>0.0<br>0.2<br>0.4<br>= (57.6 ± 0.5) MHz = (56.8 ± 0.4) MHz = (58.6 ± 0.4) MHz = (58.0 ± 0.5) MHz = (58.8 ± 0.4) MHz<br>4.10 4.12 4.14 5.64 5.66 7.76 7.78 7.80 10.76 10.78 14.92 14.94 14.96<br>0.4<br>0.2<br>0.0<br>0.2<br>0.4<br>= (57.8 ± 0.5) MHz = (56.7 ± 0.5) MHz = (55.8 ± 0.6) MHz = (55.0 ± 0.7) MHz = (53.8 ± 0.8) MHz<br>20.76 20.78 20.80 28.94 28.96 40.36 40.38 56.32 56.34 56.36 78.68 78.70<br>0.4<br>0.2<br>0.0<br>0.2<br>0.4<br>= (48.1 ± 1.0) MHz = (39.8 ± 1.3) MHz = (28.2 ± 2.1) MHz = (6.9 ± 44.4) MHz<br>109.92 109.94 109.96 153.64 153.66 214.78 214.80 300.28 300.30<br>Storage time (µs) Storage time (µs) Storage time (µs) Storage time (µs)<br>Contrast<br>Contrast<br>Contrast<br>Contrast<br><!-- End of picture text -->

FIG. 10. Measured segments (blue dots) of magnon Ramsey used to estimate the storage time of _|x⟩_ . Red curves indicate fits. The fitted magnon precession frequency _ν_ is given inside each subpanel. 



<!-- Start of picture text -->
L] y o. LJ]<br>[J<br>¢<br>t<br>u<br>0.4 +—<br>> _<br>3 ¢<br>2 0.2 ¢ No inversion : ®<br>x # Inversion :<br>h |<br>0.0 : rit A<br>4<br>0.4 YT<br>¥ Inversion : ie Ne<br>0.0 - :<br>10 71 10° 10? 102<br>Storage time tstore (US)<br><!-- End of picture text -->

13 

### **3. ESTIMATION OF THE NUMBER OF NUCLEI** 

The spatially varying wavefunction of the confined electron results in a gradient in the collinear and non-collinear hyperfine couplings. However, to simulate the system dynamics, we assume _N_ nuclei with a uniform hyperfine coupling to the electron. We estimate this effective _N_ from the differential Knight shift measured in the main text. This estimator is however biased by the fact that nuclei with strong hyperfine couplings contribute a bigger amplitude to the collective excitation while simultaneously experiencing a larger Knight shift. Assuming that the nuclear dark state represents a fully polarized nuclear ensemble, the energy difference between zero nuclear excitations _|_ 0 _⟩_ and a single excitation _|_ 1 _⟩_ is given by: 



where the sums run over individual nuclei and Φ<sup>+</sup> =<sup>�</sup> _i_<sup>_aiI_</sup> +<sup>(</sup><sup>_i_)</sup><sup>_/_</sup> � ~~�~~ _i_<sup>_a_</sup> _i_<sup>2isthenormalizedcollectiveraisingoperator</sup> [11]. The observed Knight shift thus depends on the second and third moments of the distribution of hyperfine couplings. The hyperfine coupling of a nucleus located at position **r** _i_ is given by _ai_ = _A|ψ_ ( **r** _i_ ) _|_<sup>2</sup> where _A_ is the hyperfine material constant and _|ψ_ ( **r** ) _|_<sup>2</sup> is the normalized electron envelope wavefunction [12]. We now assume a Gaussian envelope 



_∞_ where _r_ = _|_ **r** _|_ and _σ_ is the characteristic width. This satisfies the normalisation � _V_<sup>_dV |ψ_(</sup><sup>**r**)</sup><sup>_|_2=</sup> �0 _dr|ψ_ ( **r** ) _|_<sup>2</sup> _r_<sup>2</sup> 4 _π_ = 1. Converting the sums over nuclei to integrals, we obtain the moments 



Note that a Gaussian distribution with different widths along the _x_ , _y_ and _z_ axes will result in the same moments under the replacement _σ_<sup>3</sup> _→ σxσyσz_ , where _σα_ is the width along axis _α_ . The second moment is the first non-trivial moment and influences the thermal electron _T_ 2<sup>_∗_whichisoftenusedtoestimatethenumberofnuclei[2,4].We</sup> therefore use this moment to define an effective number of nuclei. A uniform collection of _N_ nuclei with _ai_ = _A/N_ results in 



Equating Eq. (10) and Eq. (8) then yields 



Substituting this result into Eqs. (5,8,9) leads to 



As expected, the measurable Knight shift is greater than the Knight shift from a uniformly coupled ensemble. The measured<sup>71</sup> Ga Knight shift is given by 



14 

where _c_ 71, _A_ 71 and _N_ 71 are the abundance, the hyperfine constant and the number of nuclei of<sup>71</sup> Ga, respectively. Using the measured _δν_ = 0.500(12) MHz and the material constants in table II, we estimate _N_ 71 = 1.35(3) _·_ 10<sup>4</sup> . The number of effective nuclei across all species is then _N_ tot = 2 _× N_ 71 _/c_ 71 = 6.84(16) _·_ 10<sup>4</sup> , where the factor 2 accounts for the presence of arsenic and gallium in the unit cell. Note that the quoted errors on _N_ tot only reflect the statistical fitting error on the _δν_ estimate. 

### **4. SYSTEM HAMILTONIAN** 

We consider the case discussed in Ref. [13] where an electron g-factor anisotropy tilts the electron quantization axis by angle _ϕ_ away from the external field **B** , giving rise to the Hamiltonian 



where _ωe_ is the electron Zeeman splitting, **S**<sup>ˆ</sup> is the electron spin operator, and<sup>ˆ</sup> **I**<sup>(</sup><sup>_i_)</sup> , _ωi_ , _ai_ denote the spin operator, Larmor frequency and hyperfine coupling of the i’th nucleus, respectively. In this coordinate system, the _y_ -axis is the QD growth direction. For a B-field 45° in-between the [110] and [<sup>¯</sup> 110] crystallographic axes, the electron quantisation axis tilt _ϕ_ is given by 



where the above g-factors are along the crystallographic axes in which the g-tensor is approximately diagonal [13]. We first diagonalize the electron Zeeman interaction with the unitary transform _U_<sup>ˆ</sup> = _e_<sup>_iϕSy_</sup> which leads to 



where the primed coordinates indicate a coordinate system co-aligned with the electron quantization axis. The nonsecular terms containing _IxSx′_ and _IySy′_ are suppressed to first order by the qubit splitting _ωe_ . By performing a Schrieffer-Wolff transformation [14] with small expansion parameter _a_<sup>2</sup> _/ωe_ , we thus obtain 



where we defined the collinear and non-collinear couplings _a_<sup>(</sup> _∥_<sup>_i_)</sup> = _ai_ cos( _ϕ_ ) and _a_<sup>(</sup> _⊥_<sup>_i_)=</sup><sup>_ai_sin(</sup><sup>_ϕ_),respectively,and</sup> ˆ<sup>we</sup> additionally used _I_<sup>ˆ</sup> _x_ = ( _I_<sup>ˆ</sup> + + _I_<sup>ˆ</sup> _−_ ) _/_ 2. The first three terms in Eq. (17) lead to Eq. (1) from the main text. _H_ 3b represents weaker three-body interactions where the electron spin couples to pairs of nuclei. In terms of nuclear raising and lowering operators, this term becomes 



The first term in Eq. (19) results in electron-mediated flip-flops between different nuclei and manifests in peaks in the ESR spectrum at the differences of nuclear Larmor frequencies (section 2.2). The second term represents a second-order process where two nuclear excitations are created at once. It is however very weak due to the quadratic _ϕ_ -dependence and is not considered further. The final term represents a similarly weak renormalization of the electron hyperfine shift. 

### **4.1. Dressed state picture** 

We now consider the rate of magnon activation in the presence of the first-order hyperfine coupling and electron drive as described by 



15 

where _δ_ is the drive detuning, Ωis the spin Rabi frequency and we have dropped the primed electron coordinates and additionally utilize the collective nuclear operators. As we can absorb the hyperfine shift _a∥Iz_ of the initial state into the drive detuning _δ_ , this term only contributes an electron-dependent Knight shift to the transition energy between the nuclear states _|Iz⟩_ and _|Iz ±_ 1 _⟩_ . We transform to the dressed electron states using the transformation 



giving rise to the dressed state Hamiltonian keeping _z_ as the quantization axis: 



where _χ_ = _√_ Ω<sup>2</sup> + _δ_<sup>2</sup> is the generalised Rabi frequency. The matrix element signifying an electro-nuclear swap is 



with a collective enhancement given by 



In the detuned driving limit, _δ ≫_ Ω, the rate reduces to Ω<sup>+</sup> mag<sup>=</sup><sup><u>Ω</u></sup> 2<sup>_<u>a</u>_</sup> _δ_<sup>_<u>⊥</u>|I_ˆ+</sup><sup>_|_whichcontainsa1</sup><sup>_/δ_drop-off.Inspecting</sup> the diagonal elements of Eq. (22), the resonance condition is _χ_ = _ωn_ + _a∥S_ 0 where _a∥S_ 0 is the differential Knight shift between the final and initial state given an initial electron spin _z_ -projection _S_ 0. As _χ ≈ δ_ , the magnon transition inherits the inhomogeneous electron linewidth set by _T_ 2<sup>_∗_.</sup> 

In the NOVEL scheme used for polarization and state transfer, _δ_ = 0 and _χ_ = Ω. This has the benefit that _χ_ is first-order insensitive to _δ_ fluctuations related to the finite _T_ 2<sup>_∗_.Inthiscase,thedressedelectronstatesareequal</sup> superpositions of the bare states and the Hamiltonian reduces to 



The first two terms dictate the resonance condition Ω= _ωn_ . The third term in Eq. (25) represents a weak coupling through the collinear term. As we can absorb _I_<sup>ˆ</sup> _z_ of the initial state into _δ_ , this term of magnitude _a∥_ becomes insignificant. Instead, the dynamics are dominated by the last term in Eq. (25) resulting in the magnon Rabi frequency 



For a dark state _m_ = _−j_ , this results in the rate Ω<sup>+</sup> mag<sup>=</sup><sup>_<u>a</u>_</sup> 2<sup>_<u>⊥</u>⟨j_,</sup><sup>_−j_+ 1</sup><sup>_|_ˆ</sup><sup>_I_+</sup><sup>_|j_,</sup><sup>_−j⟩_=</sup><sup>_a⊥_</sup> � _j/_ 2 following Eq. (24). 

16 

### **5. MONTE CARLO SIMULATION** 

We now describe the Monte Carlo simulation used to simulate the NOVEL spectra and the quantum state transfer. Simulating the large nuclear ensembles is enabled by working in truncated subspaces of the collective nuclear basis with initial nuclear spin states sampled at random. 

### **5.1. Coherent evolution** 

The simulation Hilbert space C<sup>2</sup> _⊗_ C<sup>3</sup> _⊗_ C<sup>3</sup> _⊗_ C<sup>5</sup> consists of the electron spin, the two Gallium ensembles, and the Arsenic ensemble. For the gallium ensembles, we include the collective states _{|j_ , _m_ + 1 _⟩_ , _|j_ , _m⟩_ , _|j_ , _m −_ 1 _⟩}_ , where _j_ is the spin length and _m_ is the spin z-projection. For arsenic, we include _{|j_ , _m_ + 2 _⟩_ , _|j_ , _m_ + 1 _⟩_ , _|j_ , _m⟩_ , _|j_ , _m −_ 1 _⟩_ , _|j_ , _m −_ 2 _⟩}_ in order to reproduce the weak second-order arsenic transition. We apply the Hamiltonian in Eq. (17) but only include the first three-body term in Eq. (19) to arrive at 



In the truncated Hilbert space, we implement the gallium raising and lowering operators in the matrix form 









where _ji_ and _mi_ relate to the initial state _|ji_ , _mi⟩_ for species _i_ . For arsenic, _I_<sup>ˆ</sup> _±_<sup>(</sup><sup>_i_)issimilarlyimplementedwitha5x5</sup> matrix. 

We additionally wish to reproduce the nuclear resonance at twice the arsenic Larmor frequency observed in the ESR spectrum (Fig. 8) and in NOVEL driving (main text Fig. 2b). The double-magnon transition rates expected from our device strain (section 1.2) and the three-body term (Eq. 19) are however too small to reproduce the observed rate. As this simulation is intended to reproduce the errors on state transfer from overlapping nuclear resonances, it is sufficient to incorporate an empirical Hamiltonian term 



where _η_ 2 _×_ As is estimated to be approximately 2 _π ×_ 11 Hz from polarized NOVEL spectra (Fig. 14). 

Finally, the time-dependent electron drive in the rotating frame is given by 



where the timescale represented by t is much longer than electron precession time. Note that Eq. (27) does not include the collinear hyperfine interaction _a∥S_<sup>ˆ</sup> _zI_<sup>ˆ</sup> _z_ which limits the electron _T_ 2<sup>_∗_.Weinsteadimplementthiseffectby</sup> randomly sampling _δ_ from a Gaussian distribution with _σ_ = _√_ 2 _/T_ 2<sup>_∗_standarddeviation.</sup> 

### **5.2. Nuclear state sampling** 

We now describe how to sample _|j_ , _m⟩_ for a thermal state. We note that an equal mixture of _N_ spin-1/2s is completely diagonal in the _|j_ , _m⟩_ basis with a joint probability mass function given by [15] 



17 

where _j_ 0 = _N/_ 2 is the maximal spin length and _p_ is the probability of a single spin being excited. The temperatures and magnetic fields considered in this work correspond to the infinite temperature limit with no thermal spin inversion and _p_ = 1 _/_ 2. This simplifies Eq. (34) which no longer depends on _m_ . The marginal distribution _pj_ is then given by 



as the angular momentum _j_ accommodates 2 _j_ + 1 equally likely polarisations. The strategy for sampling _|j_ , _m⟩_ is now clear: Sample _j_ from Eq. (35) and sample _m_ from the uniform _−j_ .. _j_ distribution. 

For the spin-3/2 nuclei considered in this work, explicitly calculating _pj_ , _m_ for _N ∼_ 10<sup>5</sup> is computationally challenging [15]. Instead, by working with a fully mixed state of many spins, we note that _Ix_ , _Iy_ , and _Iz_ are largely uncorrelated such that _I_<sup>2</sup> = _Ix_<sup>2+</sup><sup>_I_</sup> _y_<sup>2+</sup><sup>_I_</sup> _z_<sup>2</sup><sup>_≈_3</sup><sup>_I_</sup> _z_<sup>2.For</sup><sup>_N_thermalnucleiofspin</sup><sup>_I_,thevariance</sup> � _m_<sup>2�</sup> _−⟨m⟩_<sup>2</sup> = 3<sup><u>1</u></sup><sup>_NI_(</sup><sup>_I_+ 1)equals</sup> _N/_ 4 and 5 _N/_ 4 for _I_ = 1 _/_ 2 and _I_ = 3 _/_ 2, respectively. Thus, 5 _N_ spin-1/2s reproduce the same statistical distribution in _m_ (and by extension _j_ ) as _N_ spin-3/2s. This allows us to reuse the spin-1/2 sampling strategy by simply scaling the number of nuclei. 

### **5.3. Non unitary dynamics** 

We incorporate incoherent electron spin flips by solving the master equation 



ˆ where _ρ_ is the electro-nuclear density matrix. We include the collapse operators _C_<sup>ˆ</sup> 1 =<sup>_√_</sup> _<u>κ</u> |↑⟩⟨↓| ⊗_ Inuc and _C_<sup>ˆ</sup> 2 = _√κ |↓⟩⟨↑| ⊗_ Inuc, where Inuc is the identity operator on all nuclear ensembles. Following the observations in Ref. [6], we take the spin-flip rate _κ_ to be proportional to the drive Rabi frequency, _κ_ = _|_ Ω _|/_ (2 _Q_ ). For an undriven electron, this results in a relaxation time _T_ 1 = _Q_ (2 _π/_ Ω). We numerically integrate the master equation using the QuTip Python library. We note that spin flips can alternatively be incorporated with Monte Carlo wavefunctions which offer significant computational performance gains at the cost of numerical noise. 

### **5.4. Q-factor estimation** 

For an electron driven in a spin-locking configuration away from nuclear resonance, the master equation results in a prolonged _T_ 1 = 2 _× Q_ (2 _π/_ Ω) relaxation time. We use this fact to estimate _Q_ from the spin-locking data. Figure 13 shows _T_ 1-fits to the NOVEL signal. By averaging the extracted _T_ 1 estimates, we estimate _Q_ = 46. 

### **5.5. NOVEL probe simulation and anisotropy estimation** 

To simulate the NOVEL probe, we choose the initial state 



where _F_ init is the spin initialisation fidelity (estimated in 1.4) and _|ψ_ nuc _⟩_ is the randomly sampled nuclear state. We then numerically integrate the master equation for the _π/_ 2 pulse, spin locking pulse, and second _π/_ 2 pulse in the NOVEL probe (c.f. Fig. 5e). The final _|↓⟩_ electron population is given by _p↓_ = Trnuc _{⟨↓|_ ˆ _ρ_ 1 _|↓⟩}_ where _ρ_ ˆ1 is the final state and we have traced out the nuclei. This process is repeated for an ensemble of initial _|ψ_ nuc _⟩_ . 

To simulate an unpolarized ensemble, _|ψ_ nuc _⟩_ samples all three nuclear species from independent thermal distributions following the method in section 5.2. The assumption of a thermal<sup>75</sup> As ensemble is reasonable, as the<sup>75</sup> As polarisation is classically anticorrelated with the summed gallium ensembles (with near identical hyperfine constants) and thus inherits their thermal characteristics. As we will later discuss, this assumption yields simulations in good agreement with data. 

To simulate the ensemble with polarised gallium species, we again sample<sup>75</sup> As from a thermal distribution as we do not expect this distribution to change significantly. For<sup>71</sup> Ga, we assume a perfect dark state _|j_ , _−j⟩_ with _j_ set 

18 



<!-- Start of picture text -->
0.30<br>y /2 = -90 to -85 MHz<br>0.25 y /2 = 85 to 90 MHz  T1=981(20) ns<br>0.20<br>0.15 T1=1115(32) ns<br>0.10<br>0.05<br>0.00<br>0 100 200 300 400 500 600<br>Probe time (ns)<br> population<br>|<br><!-- End of picture text -->

FIG. 13. Estimation of electron _T_ 1 time. The dots denote the measured NOVEL signals for an unpolarized ensemble (Fig. 14) averaged across drive frequencies of -85 to -90 MHz (red dots) and 85 to 90 Mhz (blue dots). Fits (solid curves) use the model _p↑_ ( _t_ ) = (0.5 _− p_ 0) _·_ (1 _− e_<sup>(</sup><sup>_−t/T_1)</sup> ) + _p_ 0 where _p↑_ is the electron _|↑⟩_ population and _p_ 0 is the initial electron inversion. This model ensures electron spin depolarization at long drive times, i.e. _p↑_ ( _t →∞_ ) = 0.5. 

by the observed magnon Rabi frequency. Meanwhile, the state of<sup>69</sup> Ga is difficult to precisely estimate from measurements. Here, we simply seek to reproduce the main features of the observed<sup>69</sup> Ga resonance, namely its asymmetry, damping, and rise time. We find rough agreement with the experiment by assuming a<sup>69</sup> Ga state _|j_ , _j −_ ∆ _m⟩_ where ∆ _m ≥_ 0 is a dark state deviation which is sampled from an exponential distribution _p_ ∆ _m ∝ e_<sup>_−_∆</sup><sup>_m/λ_</sup> . We assume the same degree of polarisation as for<sup>71</sup> Ga, ie. _j/j_ 0 = 0.6. _λ_ describes the spread in _m_ and we estimate _λ_ = 2 based on the NOVEL signal rise time when driving<sup>69</sup> Ga. Indeed, for an ensemble of identical nuclei, a small ∆ _m_ is necessary to induce asymmetric sidebands following Eq. (24). 

Figure 14 shows the measured and simulated NOVEL spectra for an unpolarized and gallium-polarized nuclear ensemble. We use the unpolarized case to estimate the anisotropy tilt angle _ϕ_ which determines the non-collinear hyperfine coupling _a⊥_ = _a_ sin( _ϕ_ ) where _a_ is the single nucleus hyperfine constant. For each nuclear species _i_ , we set _ai_ = _Ai/_ ( _N_ tot _/_ 2) where _Ai_ is the material hyperfine material constant (table II) and _N_ tot is the effective number of total nuclei estimated in section 3. Under the assumption of a thermal ensemble, the activation times of all three species only depend on _ϕ_ . Figure 14 shows excellent agreement between measurement and simulation for _ϕ_ = 0.15 rad resulting in _a_ 71 _⊥ Ga_ = 50 kHz. In both experiment and simulation, the nuclear resonances deviate slightly from the nuclear Larmor frequencies as a result of the spectral overlap between magnon modes. We therefore compare simulation and experiment at the empirically observed resonances. Figure 15 shows NOVEL time traces for simulation and experiment further exemplifying their agreement. In experiment and simulation, the dynamics are strongly damped due to the large thermal inhomogeneity of the _|I_<sup>ˆ</sup> _±|_ matrix elements. 



# ~~<u><mark>[are</mark></u>~~ ~~<mark>ni</mark>~~ 

20 

### **5.6. Simulating quantum register performance** 

To simulate the quantum register, we use the same master equation to simulate all six periods of electron drive in Fig. 5f. The electron reset during storage is incorporated by Krauss operators: 





where _K_<sup>ˆ</sup> 3 and _K_<sup>ˆ</sup> 4 represent erroneous electron initialisation. We repeat the memory experiment for all combinations of input and output states. As our simulation assumes identical nuclei it does not incorporate any dephasing from quadrupolar or Knight field inhomogeneities. We therefore choose to compare fidelity of our simulation and experiment at the shortest storage time. 

We first test our simulation using ideal parameters: The couplings to<sup>75</sup> As and<sup>69</sup> Ga are turned off and there are no errors. Fig. 16a reveals the resulting tomography when using the<sup>71</sup> Ga storage mode. The resulting 0.35% infidelity stems from the rotating wave approximation not being fully satisfied during state transfer given that the transfer rate Ω<sup>+= 3.8 MHzisnotnegligiblecomparedtothestoragemodefrequency</sup><sup>_ωn/_2</sup><sup>_π_= 58.4 MHz.This</sup> mag<sup>_/_2</sup><sup>_π_</sup> error can be eliminated with pulse shaping or by slower state transfer. 

For simulating realistic parameters (Fig. 4b main text), we use the same parameters as for the polarized NOVEL simulation (Fig. 14) and apply a spin-locking drive with _T_ sl = 130 ns duration and Ω _y/_ 2 _π_ = 56 MHz Rabi frequency as this results in the maximal signal under NOVEL probing. The simulated tomography is shown in Fig. 16b. 

To estimate the infidelity owing to electron relaxation (Fig. 16c), we remove the coupling to<sup>75</sup> As and<sup>69</sup> Ga and include the electron relaxation parameterized by _Q_ = 46 as the only error mechanism. We further numerically optimize _T_ sl and Ω _y_ which vary from ideal conditions by _<_ 2%. 

To estimate the infidelity owing to nuclear resonance overlap (Fig. 16d), we use the nuclear state estimated from polarized NOVEL but set all other errors to zero. 

Finally, we simulate an ideal QD containing only<sup>75</sup> As and<sup>71</sup> Ga ensembles prepared in oppositely polarized _j_ = 0.6 _j_ 0 dark states and with no other errors. In this case, part of the electronic state can get stored in<sup>75</sup> As and be successfully retrieved if the<sup>75</sup> As and<sup>71</sup> Ga modes rephase during storage. This however results in a storage time-dependent fidelity making the fidelity measure ambigious. To circumvent this problem, we reinitialize the<sup>75</sup> As ensemble into its dark state after the first SWAP gate, thereby erasing any information stored. Using the same _ϕ_ = 0.15 as estimated from experiments, we obtain a simulated _F_ = 98.3% and a faster 83.6 ns SWAP gate owing to the increased collective enhancement of the now 100% abundant<sup>71</sup> Ga ensemble. 

### **6. EXPECTED INHOMOGENEOUS DEPHASING TIME OF THE STORAGE MODE** 

We estimate the nuclear quadrupolar-induced inhomogeneous dephasing time of the<sup>71</sup> Ga storage mode from NMR measurements of the _|±_ 3 _/_ 2 _⟩↔|±_ 1 _/_ 2 _⟩_ satellite transitions: Ref. [16] reports a _δν_ 69 _∼_ 7 kHz FWHM of the<sup>69</sup> Ga satellite transitions. This results in an inhomogeneous dephasing time 



where the factor �8 _log_ (2) is the FWHM of a Gaussian distribution. We apply a correction to account for the smaller quadrupolar moment of<sup>71</sup> Ga which translates to a proportionally smaller quadrupolar broadening under the assumption that the chemically similar gallium isotopes experience the same distribution of electric field gradients. From the reported ratio of quadropolar moments _Q_ 71 _/Q_ 69 = 0.63 [17], we estimate a<sup>71</sup> Ga dephasing time of ( _T_ 2<sup>_∗_)71=</sup> ( _T_ 2<sup>_∗_)69</sup><sup>_×_(</sup><sup>_Q_69</sup><sup>_/Q_71) = 120 µs.</sup> 

Probability 0.50 

0.00 

0.25 

0.75 

1.00 





<!-- Start of picture text -->
e) Crosstalk with<br>a) Perfect parameters b) Realistic parameters c) Spin relaxation d) Crosstalk isotopic purification<br>- z4 F=0.9965 -z { F=0.7299 - z -z { F=0.7709 - z{ F=0.9828<br>9zzzz z<br>©<br>7<br>32Yy yy [| yy yy [|| wyy<br>£ x - X - X - X - X<br>XXXX X<br>XX Y - y z - z X X Y - y z - z X X Y - y z - z X X Y - y z - z X X Y - y z - z<br>Readout projection<br><!-- End of picture text -->

22 

- [10] L. Zaporski, S. R. de Wit, T. Isogawa, M. Hayhurst Appel, C. Le Gall, M. Atat¨ure, and D. A. Gangloff, Many-Body Singlet Prepared by a Central-Spin Qubit, PRX Quantum **4** , 040343 (2023). 

- [11] J. Hu, W. Chen, Z. Vendeiro, H. Zhang, and V. Vuleti´c, Entangled collective-spin states of atomic ensembles under nonuniform atom-light interaction, Phys. Rev. A **92** , 063816 (2015). 

- [12] B. Urbaszek, X. Marie, T. Amand, O. Krebs, P. Voisin, P. Maletinsky, A. H¨ogele, and A. Imamoglu, Nuclear spin physics in quantum dots: An optical investigation, Rev. Mod. Phys. **85** , 79 (2013). 

- [13] T. Botzem, R. P. G. McNeil, J.-M. Mol, D. Schuh, D. Bougeard, and H. Bluhm, Quadrupolar and anisotropy effects on dephasing in two-electron spin qubits in GaAs, Nat. Commun. **7** , 11170 (2016). 

- [14] S. Bravyi, D. P. DiVincenzo, and D. Loss, Schrieffer–Wolff transformation for quantum many-body systems, Annals of Physics **326** , 2793 (2011). 

- [15] J. Wesenberg and K. Mølmer, Mixed collective states of many spins, Phys. Rev. A **65** , 062304 (2002). 

- [16] P. Millington-Hotze, H. E. Dyte, S. Manna, S. F. Covre da Silva, A. Rastelli, and E. A. Chekhovich, Approaching a fully-polarized state of nuclear spins in a solid, Nat. Commun. **15** , 985 (2024). 

- [17] N. J. Stone, Table of nuclear electric quadrupole moments, Atomic Data and Nuclear Data Tables **111-112** , 1 (2016). 

- [18] M. Berglund and M. E. Wieser, Isotopic compositions of the elements 2009 (IUPAC Technical Report), Pure Appl. Chem. **83** , 397 (2011). 

- [19] F. K. Malinowski, F. Martins, P. D. Nissen, E. Barnes, L. Cywinski, M. S. Rudner, S. Fallahi, G. C. Gardner, M. J. Manfra, C. M. Marcus, and F. Kuemmeth, Notch filtering the nuclear environment of a spin qubit, Nat. Nanotechnol. **12** , 16 (2016). 

