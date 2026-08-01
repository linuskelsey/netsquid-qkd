# Spin-photon entanglement of a single Er<sup>3+</sup> ion in the telecom band 

Mehmet T. Uysal<sup>1</sup> ,<sup>∗</sup> Łukasz Dusanowski<sup>1</sup><sup>_∗_</sup> , Haitong Xu<sup>1</sup><sup>_∗_</sup> , Sebastian P. Horvath<sup>1</sup> , Salim Ourari<sup>1</sup> , Robert J. Cava<sup>2</sup> , Nathalie P. de Leon<sup>1</sup> , Jeff D. Thompson<sup>1†</sup> 

> 1Department of Electrical and Computer Engineering, Princeton University, Princeton, NJ, 08544, USA 

> 2Department of Chemistry, Princeton University, Princeton, NJ 08544, USA 

**Long-distance quantum communication using quantum repeaters is an enabling technology for secure communication, distributed quantum computing and quantum-enhanced sensing and metrology [1, 2]. As a building block of quantum repeaters, spin-photon entanglement has been demonstrated with both atomic [3, 4, 5, 6, 7] and solid-state qubits [8, 9, 10, 11, 12, 13, 14]. However, previously demonstrated qubits with long spin coherence do not directly emit photons into the low-loss telecom band that is needed for long-distance communication. Here, we demonstrate spin-photon entanglement using a single Er**<sup>3+</sup> **ion in a solid-state crystal, integrated into a silicon nanophotonic circuit. Direct emission into the telecom band enables an entanglement rate of 1.48 Hz over 15.6 km of optical fiber, with a fidelity of 73(3)%. This opens the door to large-scale quantum networks based on scalable nanophotonic devices and many spectrally multiplexed Er**<sup>3+</sup> **ions [15].** 

Individually addressable solid-state defects integrated with nanophotonic devices are particularly attractive for combining a single photon source and quantum memory in a scalable platform [16, 17, 18, 19, 20, 21, 14]. However, a challenge is that the typical energy scale for atomic transitions (400 – 900 nm) is outside the low-loss telecom band in standard optical fibers (1.5 _µ_ m), resulting in significant losses for long distance transmission. Two approaches have been demonstrated to circumvent this challenge: single-photon frequency conversion [9, 22, 23, 24, 25, 26, 27] and generating entangled photon pairs using spontaneous parametric downconversion (SPDC), where one photon is in the telecom band and the other matches the wavelength of an atomic memory [13, 28]. However, these approaches suffer from limited efficiency and added noise, and in the case of SPDC, involve non-deterministic sources. Recently, direct telecom spinphoton entanglement of a single emitter has been demonstrated in an InAs/InP quantum dot [29], but direct entanglement with a long-lived spin suitable for long-distance transmission has not been reported. 

The rare earth ion (REI) Er<sup>3+</sup> provides a direct spin-photon interface in the telecom band, but exploiting individual REIs as single photon sources and quantum memories is challenging because of their low photon emission rate and correspondingly increased sensitivity to decoherence. Recent work has demonstrated incorporating REIs into nanophotonic cavities to enhance the emission rate up to 1000fold [30, 31, 32, 33, 34, 35, 36, 37], enabling single-shot readout [38, 39, 40] and manipulating nearby nuclear spin ancillae [41, 42, 43], and remote entanglement of two Yb<sup>3+</sup> :YVO4 defects [14]. Careful selection and engineering of host materials has also led to improved coherence properties. In particular, Er<sup>3+</sup> :CaWO4 has demonstrated coherence times of 23 ms in small ensembles [44], and low enough spectral diffusion to enable indistinguishable single photon generation in a Si nanophotonic cavity [45]. However, despite these improvements, maintaining the joint spin and optical coherence during photon emission remains a challenge. 

Here, we demonstrate spin-photon entanglement directly in the telecom band, with a single Er<sup>3+</sup> ion in CaWO4 integrated into a silicon nanophotonic device. The key advance enabling this demonstration is a spin-photon entanglement protocol capable of refocusing spin decoherence while waiting for a photon to 

> ∗These authors contributed equally to this work. 

> †jdthompson@princeton.edu 

i 

be emitted; this protocol has the additional benefit of mitigating an unanticipated optically-induced spin dephasing mechanism. Through the large Purcell factor of the cavity ( _P_ = 342), the absence of losses from frequency conversion, and the low propagation losses at the emission wavelength of _λ_ = 1532 _._ 6 nm, we reach a spin-photon entanglement rate of 1.48 Hz over 15.6 kilometers of optical fiber. This rate improves on previously demonstrated telecom band spin-photon entanglement using frequency converted solid-state sources [9, 22, 27] and is comparable to frequency-converted spin-photon entanglement from trapped ions and single atoms in optical tweezers [23, 24, 26]. The fidelity is _F_ = 0 _._ 73(3), beyond the classical bound of 0.5 [10]. This opens the door to implementing long-distance quantum networks with Er<sup>3+</sup> devices. 

Our experimental approach is depicted schematically in Fig. **1** a. The nanophotonic device architecture has previously been described in Refs. [45, 46]. Briefly, a hybrid structure is formed by a Si nanophotonic device bonded on the CaWO4 substrate (Fig. **1** b). The sample is cooled to _T_ = 500 mK in a<sup>3</sup> He cryostat. Light is extracted from the cavity into a bus waveguide and ultimately an optical fiber though a grating coupler, and microwaves to drive spin transitions are applied using a nearby antenna [46]. Er<sup>3+</sup> ions are implanted _∼_ 10 nm below the surface of the CaWO4 crystal, within the evanescent field of the Si cavity, resulting in a strong enhancement of the emission rate (Fig. **1** c). Through careful control of the implantation and annealing conditions, we have observed single ions with spectral diffusion linewidths below 200 kHz and spectral diffusion less than the radiative linewidth on the timescale of photon emission [45]. The ion used in this work has a slightly broader spectral diffusion linewidth of 470 kHz (Extended Data Fig. **1** ), and a radiative lifetime of _τr_ = 18 _._ 4 _µ_ s for the B transition that is resonant with the optical cavity (Fig. **1** d), given by the Purcell factor of _P_ = 342. 

In the standard time-bin spin-photon entanglement protocol [47], optical excitation pulses are embedded in a Hahn echo sequence with a free precession period that is long enough to allow the excited state to fully decay between pulses in order to preserve spin-photon correlations. There are two challenges to implementing this directly in our Er<sup>3+</sup> :CaWO4 devices. First, maintaining coherence for significantly longer than _τr_ requires faster dynamical decoupling than a Hahn echo: while the XY-16 coherence time is 200 _µ_ s, the Hahn echo coherence time is only 30 _µ_ s (Fig. **2** a), likely limited by fluctuating magnetic field noise from paramagnetic impurities [45]. Second, the optical pulses themselves cause spin decoherence through a previously unreported mechanism, which is not refocused in the standard sequence. 

We first investigate spin decoherence caused by optical pulses. We discovered that the insertion of an optical pulse during free precession can reduce the Hahn echo coherence time significantly, to less than 4 _µ_ s (Fig. **2** b). The effect does not depend on the optical pulses being resonant with the optical transition of Er<sup>3+</sup> . The coherence is restored if the optical pulse is applied at the beginning or end of the echo sequence, which suggests a mechanism of spin spectral diffusion induced by the optical pulse (Fig. **2** c). Because of its _S_ 4 site symmetry (Fig. **2** d), the spin precession frequency of Er<sup>3+</sup> :CaWO4 is linearly sensitive to both magnetic and electric fields, where the latter arises from a distortion in the electronic wavefunction that changes the magnetic moment [48, 44]. We disentangle their effects by measuring the induced spectral diffusion, _σω_ , for different magnetic field orientations in the _ab−_ plane, and observe a dependence of _σω ∝|_ sin (2 _ϕ −_ 2 _ϕ_ 0) _|_ with _ϕ_ 0 = 35<sup>_◦_</sup> (1) (Fig. **2** e), matching the previously measured electric field induced magnetic moment shift for Er<sup>3+</sup> :CaWO4 [48]. Therefore, we attribute the optically-induced dephasing to charge noise, and based on the measured scaling with power and pulse duration, conclude that it results from a single-photon absorption process [Extended Data Fig. **2** ]. We note that previous measurements of spin coherence in Er<sup>3+</sup> :CaWO4 were performed without optical illumination, and are therefore not sensitive to this effect [45, 49, 44]. 

To mitigate both the optically-induced spin dephasing and magnetic field noise, we introduce a modified spin-photon entanglement protocol with fast dynamical decoupling. In the modified protocol, we apply an XY-16 decoupling sequence with a _π_ pulse spacing that is much shorter than the excited state lifetime. To preserve spin-photon correlations, we apply the _π_ pulses to both the ground and excited state spin manifolds simultaneously (Fig. **3** a,b). We apply two optical pulses separated by an odd number of _π_ pulses to create the spin-photon entangled state ( _|↓_ g _⟩|E⟩_ + _|↑_ g _⟩|L⟩_ ) _/√_ 2, where _|E⟩_ and _|L⟩_ denote photons in the early and late time-bins, respectively. Since the optical pulses are applied at refocusing points of the 

ii 

XY-16 sequence, the optically induced spin dephasing is also refocused. 

In Fig. **3** c, we compare the photon emission timing and spin coherence under optical illumination for both protocols. In a standard Hahn echo time-bin entanglement protocol, the spin coherence decays on the timescale of 20 _µ_ s, which is comparable to _τr_ . In the modified protocol, the spin coherence is protected beyond 150 _µ_ s, provided the precise pulse spacing is chosen to avoid resonant interactions with the<sup>183</sup> W nuclear spin bath. 

We generate and measure spin-photon entanglement using the sequence in Fig. **4** a. To measure the photonic state, we send the emitted photons to an unbalanced Mach-Zehnder interferometer (MZI). The time-bin encoded photon, with bins separated by _T_ = 75 _._ 5 _µ_ s, is split between a long arm of 15.6 km and a short arm (attenuated for equivalent loss) and re-combined on a 50:50 beam-splitter (BS) before going to two superconducting nanowire single photon detectors (SNSPD)(Fig. **1** a). The detection of a single photon in the early ([0 _, T_ ]) or late ([2 _T,_ 3 _T_ ]) time bins corresponds to a measurement of the photon in the _Zp_ basis ( _|E⟩_ , _|L⟩_ ), while the detection of a photon in the central time bin, [ _T,_ 2 _T_ ], corresponds to a measurement in the superposition basis Φ _p_ , _|±ϕ⟩_ = _|E⟩± e_<sup>_−iϕ_</sup> _|L⟩_ ) _/√_ 2, where _ϕ_ is the relative phase accumulated in the interferometer (Fig. **4** b). Instead of stabilizing _ϕ_ , we track it continuously throughout the experiment using a reference laser sent through the same interferometer, resulting in a uniformly distributed set of measurement bases [Methods S5]. After each entanglement attempt, the spin state is measured only if a photon is detected within the heralding window, using real-time control with a complex programmable logic device (CPLD) [Methods S6]. We compute the entanglement fidelity from the visibility of the entanglement in the X, Y and Z bases (Fig. **4** c,d,e), _F_ = (1 + _EX_ + _EY_ + _EZ_ ) _/_ 4 [22], where _⟨Xs_ Φ _p⟩_ = _EX_ cos( _ϕ_ ), _⟨Ys_ Φ _p⟩_ = _EY_ sin( _ϕ_ ) and _EZ_ = _⟨ZsZp⟩_ . Here, Φ _p_ = _|_ + _ϕ⟩⟨_ + _ϕ| −|−ϕ⟩⟨−ϕ|_ . The experimentally observed visibilities are _{EX , EY , EZ}_ = _{_ 0 _._ 60(3) _,_ 0 _._ 55(3) _,_ 0 _._ 77(5) _}_ [Methods S8], corresponding to a total fidelity of _F_ = 0 _._ 73(3). The rate of successful entanglement generation is _R_ = 1 _._ 48 Hz. We note that we only accept photons emitted within the first 2.5 _µ_ s of the collection window, comprising 9.1% of all emitted photons, to minimize sensitivity to errors from fast dephasing of the optical transition [50] [Methods S9]. 

The measured fidelity is in reasonable agreement with estimated visibilities of _EX/Y_ = 0 _._ 63 and _EZ_ = 0 _._ 80 based on independently measured sources of error [Methods S10]. In particular, we identify significant contributions from spin decoherence and MW pulse errors ( _ϵX/Y_ = 25%, _ϵZ_ = 14%), optical decoherence (7%), background counts (5%), initialization errors (3%), and overlap of emission from the early and late time bins (2%). 

In this work, we have demonstrated spin-photon entanglement of a single Er<sup>3+</sup> ion directly in the telecom band over 15.6 km of optical fiber, enabled by our fast dynamical decoupling protocol that protects spin coherence during photon emission and mitigates optically induced dephasing. The demonstrated entanglement rate is comparable to that obtained with frequency-conversion from single trapped atoms or ions [23, 24, 26] and is higher than that obtained with frequency-converted solid-state sources [9, 22, 27]. The high rate for this distance is achieved by avoiding frequency conversion, and is not limited by the relatively long optical lifetime of the Er<sup>3+</sup> ion: after cavity enhancement, the lifetime is shorter than the photon propagation time through a long fiber link such as the one used here. We estimate that the entanglement rate can be increased to 150 Hz with improvements in optical and spin coherence to make use of all emitted photons ( _×_ 11), improvements to the cavity impedance matching and fiber coupling efficiency ( _×_ 6) [51], and faster spin reset ( _×_ 1 _._ 5) [Methods S11]. The entanglement fidelity is mainly limited by coherence and dark counts, and should improve with the same enhancements. 

These results pave the way to future long-distance quantum repeaters based on Er<sup>3+</sup> ions interfaced with scalable nanophotonic devices. While the long-term spectral diffusion is still significantly larger than the radiative linewidth, it was recently demonstrated that quasi-static depehasing can be refocused in the context of spin-spin entanglement protocols [14, 52]. A particularly exciting direction is to use multiplexed control of many emitters in the same cavity [15] to store multiple Bell pairs, which can enable higher-rate operation with reduced memory time requirements in a repeater protocol [53], as well as entanglement distillation [54, 55]. 

**Acknowledgements** We acknowledge helpful conversations with Shimon Kolkowitz, Rose Ahlefeldt 

iii 

and Adam Turflinger. This work was primarily supported by the U.S. Department of Energy, Office of Science, National Quantum Information Science Research Centers, Co-design Center for Quantum Advantage (C2QA) under contract number DE-SC0012704. We also acknowledge support from the DOE Early Career award (DE-SC0020120, for modeling of decoherence mechanisms and spin interactions), as well as AFOSR (FA9550-18-1-0334 and YIP FA9550-18-1-0081), the Eric and Wendy Schmidt Transformative Technology Fund, the Princeton Catalysis Initiative, and DARPA DRINQS (D18AC00015) for establishing the materials spectroscopy pipeline and developing integrated nanophotonic devices. We acknowledge the use of Princeton’s Imaging and Analysis Center, which is partially supported by the PCCM, an NSF MRSEC (DMR-1420541), as well as the Princeton Micro-Nano Fabrication Center. 

iv 

## **References** 

- [1] Awschalom, D. _et al._ Development of quantum interconnects (quics) for next-generation information technologies. _PRX Quantum_ **2** , 017002 (2021). 

- [2] Gisin, N., Ribordy, G., Tittel, W. & Zbinden, H. Quantum cryptography. _Reviews of modern physics_ **74** , 145 (2002). 

- [3] Blinov, B. B., Moehring, D. L., Duan, L.-M. & Monroe, C. Observation of entanglement between a single trapped atom and a single photon. _Nature_ **428** , 153–157 (2004). 

- [4] Matsukevich, D. & Kuzmich, A. Quantum state transfer between matter and light. _Science_ **306** , 663–666 (2004). 

- [5] Chou, C.-W. _et al._ Measurement-induced entanglement for excitation stored in remote atomic ensembles. _Nature_ **438** , 828–832 (2005). 

- [6] Volz, J. _et al._ Observation of entanglement of a single photon with a trapped atom. _Physical review letters_ **96** , 030404 (2006). 

- [7] Wilk, T., Webster, S. C., Kuhn, A. & Rempe, G. Single-atom single-photon quantum interface. _Science_ **317** , 488–490 (2007). 

- [8] Gao, W., Fallahi, P., Togan, E., Miguel-Sánchez, J. & Imamoglu, A. Observation of entanglement between a quantum dot spin and a single photon. _Nature_ **491** , 426–430 (2012). 

- [9] De Greve, K. _et al._ Quantum-dot spin–photon entanglement via frequency downconversion to telecom wavelength. _Nature_ **491** , 421–425 (2012). 

- [10] Togan, E. _et al._ Quantum entanglement between an optical photon and a solid-state spin qubit. _Nature_ **466** , 730–734 (2010). 

- [11] Bernien, H. _et al._ Heralded entanglement between solid-state qubits separated by three metres. _Nature_ **497** , 86–90 (2013). 

- [12] Bhaskar, M. K. _et al._ Experimental demonstration of memory-enhanced quantum communication. _Nature_ **580** , 60–64 (2020). 

- [13] Lago-Rivera, D., Grandi, S., Rakonjac, J. V., Seri, A. & de Riedmatten, H. Telecom-heralded entanglement between multimode solid-state quantum memories. _Nature_ **594** , 37–40 (2021). 

- [14] Ruskuc, A. _et al._ Scalable multipartite entanglement of remote rare-earth ion qubits. _arXiv preprint arXiv:2402.16224_ (2024). 

- [15] Chen, S., Raha, M., Phenicie, C. M., Ourari, S. & Thompson, J. D. Parallel single-shot measurement and coherent control of solid-state spins below the diffraction limit. _Science_ **370** , 592–595 (2020). 

- [16] Sipahigil, A. _et al._ An integrated diamond nanophotonics platform for quantum-optical networks. _Science_ **354** , 847–850 (2016). 

- [17] Jung, T. _et al._ Spin measurements of NV centers coupled to a photonic crystal cavity. _Apl Photonics_ **4** (2019). 

- [18] Mouradian, S., Wan, N. H., Schröder, T. & Englund, D. Rectangular photonic crystal nanobeam cavities in bulk diamond. _Applied Physics Letters_ **111** (2017). 

v 

- [19] Kuruma, K. _et al._ Coupling of a single tin-vacancy center to a photonic crystal cavity in diamond. _Applied Physics Letters_ **118** (2021). 

- [20] Rugar, A. E. _et al._ Quantum photonic interface for tin-vacancy centers in diamond. _Physical Review X_ **11** , 031021 (2021). 

- [21] Chakravarthi, S. _et al._ Hybrid integration of gap photonic crystal cavities with silicon-vacancy centers in diamond by stamp-transfer. _Nano Letters_ **23** , 3708–3715 (2023). 

- [22] Tchebotareva, A. _et al._ Entanglement between a diamond spin qubit and a photonic time-bin qubit at telecom wavelength. _Physical review letters_ **123** , 063601 (2019). 

- [23] Krutyanskiy, V. _et al._ Light-matter entanglement over 50 km of optical fibre. _npj Quantum Information_ **5** , 72 (2019). 

- [24] Krutyanskiy, V. _et al._ Telecom-wavelength quantum repeater node based on a trapped-ion processor. _Physical Review Letters_ **130** , 213601 (2023). 

- [25] van Leent, T. _et al._ Long-distance distribution of atom-photon entanglement at telecom wavelength. _Physical Review Letters_ **124** , 010510 (2020). 

- [26] van Leent, T. _et al._ Entangling single atoms over 33 km telecom fibre. _Nature_ **607** , 69–73 (2022). 

- [27] Knaut, C. _et al._ Entanglement of nanophotonic quantum memory nodes in a telecom network. _Nature_ **629** , 573–578 (2024). 

- [28] Lago-Rivera, D., Rakonjac, J. V., Grandi, S. & Riedmatten, H. d. Long distance multiplexed quantum teleportation from a telecom photon to a solid-state qubit. _Nature Communications_ **14** , 1889 (2023). 

- [29] Laccotripes, P. _et al._ Spin-photon entanglement with direct photon emission in the telecom C-band. _arXiv preprint arXiv:2310.16930_ (2023). 

- [30] Dibos, A. M., Raha, M., Phenicie, C. M. & Thompson, J. D. Atomic source of single photons in the telecom band. _Physical Review Letters_ **120** , 243601 (2018). 

- [31] Zhong, T. _et al._ Optically addressing single rare-earth ions in a nanophotonic cavity. _Physical Review Letters_ **121** , 183603 (2018). 

- [32] Yu, Y. _et al._ Frequency tunable, cavity-enhanced single erbium quantum emitter in the telecom band. _arXiv preprint arXiv:2304.14685_ (2023). 

- [33] Huang, J.-Y. _et al._ Stark tuning of telecom single-photon emitters based on a single Er<sup>3+</sup> . _Chinese Physics Letters_ (2023). 

- [34] Ji, C. _et al._ Nanocavity-mediated purcell enhancement of Er in TiO2 thin films grown via atomic layer deposition. _ACS nano_ **18** , 9929–9941 (2024). 

- [35] Ulanowski, A., Merkel, B. & Reiserer, A. Spectral multiplexing of telecom emitters with stable transition frequency. _Science Advances_ **8** , eabo4538 (2022). 

- [36] Yang, L., Wang, S., Shen, M., Xie, J. & Tang, H. X. Controlling single rare earth ion emission in an electro-optical nanocavity. _Nature Communications_ **14** , 1718 (2023). 

- [37] Horvath, S. P. _et al._ Strong purcell enhancement of an optical magnetic dipole transition. _arXiv preprint arXiv:2307.03022_ (2023). 

- [38] Raha, M. _et al._ Optical quantum nondemolition measurement of a single rare earth ion qubit. _Nature Communications_ **11** , 1605 (2020). 

vi 

- [39] Kindem, J. M. _et al._ Control and single-shot readout of an ion embedded in a nanophotonic cavity. _Nature_ **580** , 201–204 (2020). 

- [40] Gritsch, A., Ulanowski, A., Pforr, J. & Reiserer, A. Optical single-shot readout of spin qubits in silicon. _arXiv preprint arXiv:2405.05351_ (2024). 

- [41] Kornher, T. _et al._ Sensing individual nuclear spins with a single rare-earth electron spin. _Physical Review Letters_ **124** , 170402 (2020). 

- [42] Ruskuc, A., Wu, C.-J., Rochman, J., Choi, J. & Faraon, A. Nuclear spin-wave quantum register for a solid-state qubit. _Nature_ **602** , 408–413 (2022). 

- [43] Uysal, M. T. _et al._ Coherent control of a nuclear spin via interactions with a rare-earth ion in the solid state. _PRX Quantum_ **4** , 010323 (2023). 

- [44] LeDantec, M. _et al._ Twenty-three–millisecond electron spin coherence of erbium ions in a naturalabundance crystal. _Science Advances_ **7** , eabj9786 (2021). 

- [45] Ourari, S. _et al._ Indistinguishable telecom band photons from a single Er ion in the solid state. _Nature_ **620** , 977–981 (2023). 

- [46] Chen, S. _et al._ Hybrid microwave-optical scanning probe for addressing solid-state spins in nanophotonic cavities. _Optics Express_ **29** , 4902 (2021). 

- [47] Barrett, S. D. & Kok, P. Efficient high-fidelity quantum computation using matter qubits and linear optics. _Physical Review A_ **71** , 060310 (2005). 

- [48] Mims, W. Electric field shift in paramagnetic resonance for four ions in a calcium tungstate lattice. _Physical Review_ **140** , A531 (1965). 

- [49] Wang, Z. _et al._ Single-electron spin resonance detection by microwave photon counting. _Nature_ **619** , 276–281 (2023). 

- [50] Metz, J. & Barrett, S. Effect of frequency-mismatched photons in quantum-information processing. _Physical Review A_ **77** , 042323 (2008). 

- [51] Tiecke, T. _et al._ Efficient fiber-optical interface for nanophotonic devices. _Optica_ **2** , 70–75 (2015). 

- [52] Uysal, M. T. & Thompson, J. D. Rephasing spectral diffusion in time-bin spin-spin entanglement protocols. _arXiv preprint arXiv:2406.06497_ (2024). 

- [53] Collins, O., Jenkins, S., Kuzmich, A. & Kennedy, T. Multiplexed memory-insensitive quantum repeaters. _Physical review letters_ **98** , 060502 (2007). 

- [54] Bennett, C. H. _et al._ Purification of noisy entanglement and faithful teleportation via noisy channels. _Physical review letters_ **76** , 722 (1996). 

- [55] Kalb, N. _et al._ Entanglement distillation between solid-state quantum network nodes. _Science_ **356** , 928–932 (2017). 

- [56] Biercuk, M., Doherty, A. & Uys, H. Dynamical decoupling sequence construction as a filter-design problem. _Journal of Physics B: Atomic, Molecular and Optical Physics_ **44** , 154002 (2011). 

- [57] de Sousa, R. _Electron Spin as a Spectrometer of Nuclear-Spin Noise and Other Fluctuations_ , chap. 2, 186–194 (Springer Berlin, Heidelberg, 2009). 

- [58] Bylander, J., Robert-Philip, I. & Abram, I. Interference and correlation of two independent photons. _The European Physical Journal D-Atomic, Molecular, Optical and Plasma Physics_ **22** , 295–301 (2003). 

vii 

- [59] Zheng, X., Dolde, J. & Kolkowitz, S. Reducing the instability of an optical lattice clock using multiple atomic ensembles. _Physical Review X_ **14** , 011006 (2024). 

viii 





<!-- Start of picture text -->
4<br>J4 4 ~, ~ Sse<br>J Sse<br>J Sse<br>hI Ss<br><!-- End of picture text -->



<!-- Start of picture text -->
ee<br>A1|<br>[]<br>1<br>1 [| ]<br>y J o<br>es & eo.1)hloc¢ c [),1  I|]1 |<br>NS |<br>AN []<br>[I]<br><!-- End of picture text -->



<!-- Start of picture text -->
SND ® |<br>—a a a a ——— [][)<br>Pe [)1<br>0 eA<br>EE\yl[)|<br>vi<br>\X}<br>Ee —— — Y]<br><!-- End of picture text -->



<!-- Start of picture text -->
ET<br>NN<br><!-- End of picture text -->



<!-- Start of picture text -->
a 1.0<br>0.5<br>XY-16<br>0.0 Hahn<br>0 50 100 150 200<br>Free evolution time ( μ s)<br>opt.<br>b MWg τ c τopt<br>1.0 1.0<br>0 nW<br>1.6 nW<br>0.5 65 nW 0.5<br>0.0<br>0.0<br>0 20 40 60 80 0 10 20<br>2τ  (us) τ opt ( μ s)<br>d e<br>Er<br>100<br>Ca<br>50<br>c<br>Ec a b 0 −60 −30 0 30 60<br>Angle relative to the a-axis (deg)<br>Contrast<br>Contrast<br> (kHz)<br>/2π<br>ω<br>σ<br><!-- End of picture text -->

**Fig. 2** : **Optically induced spin dephasing. a** In the absence of optical illumination, the Hahn echo spin coherence is 30 _µ_ s, which can be extended to over 200 _µ_ s with an XY-16 sequence. **b** Applying an optical pulse in the middle of a Hahn echo sequence degrades the coherence. The effect is shown for 200 ns pulses at two optical powers: 1.6 nW, corresponding to the power used for optical _π_ pulses in the following experiments, 65 nW, to more clearly show the effect. **c** In a fixed sequence length (2 _τ_ = 20 _µ_ s), the Hahn echo contrast is maximized by placing the optical pulse at the beginning or the end of the sequence, indicating that the optically induced dephasing can be refocused. The dashed line is a fit to a Gaussian decay envelope, _e_<sup>_−_(</sup><sup>_τ_opt</sup><sup>_/Td_)2</sup> with _Td_ = 2.1 _µ_ s. **d** The four nearest neighbor calcium ions in the Er<sup>3+</sup> :CaWO4 unit cell (highlighted by black lines) show _S_ 4 symmetry, invariant under a 90<sup>_◦_</sup> improper rotation. An electric field along the _c_ -axis (red arrows) lowers the symmetry, which lifts the in-plane g- tensor degeneracy and results in a linear shift of the spin splitting [48]. W and O atoms are not displayed. **e** The induced frequency fluctuation _σω_ = _√_ 2 _/Td_ varies with the magnetic field orientation in the _aa_ -plane as _σω_ ( _ϕ_ ) _∝|_ sin(2 _ϕB −_ 2 _ϕ_ 0) _|_ with _ϕ_ 0 = _−_ 35(1)<sup>_◦_</sup> , confirming that it arises from a fluctuating electric field. The dashed line corresponds to the field orientation used in the spin-photon experiment, which is needed to obtain a cycling transition for this ion [38]. 

x 



<!-- Start of picture text -->
a T b Even Odd<br>MW<br>Optical<br>Δω<br>MWg B A<br>MWe<br>X X Y X Y Y X Y X X Y X Y Y X Y X θ 2 τ<br>c 1.0<br>0.5<br>0.0<br>Fluoresence collection window ( μ s)<br>d 1.0<br>0.5<br>0.0<br>0 20 40 60 80 100 120 140<br>Free evolution time ( μ s)<br>Norm. counts<br>Contrast<br><!-- End of picture text -->

**Fig. 3** : **Entanglement protocol with dynamical decoupling. a** The pulse sequence for spin-photon entanglement. Two optical _πB_ pulses interleaved with an XY-16 sequence on the MW _g_ and MW _e_ transitions, where the optical pulses are separated by 15 _π_ pulses on the spin. The decoupling sequence ends shortly after the heralding window (grey highlight) and the last excited state _π_ pulse also omitted since there is no need to continue decoupling beyond this point. A generalized form of the sequence is provided in Extended Data Fig. **4** . The last _π/_ 2 pulse on the MW _g_ transition chooses the spin measurement basis. The optical pulses are applied at refocusing points of the decoupling sequence, so that any random frequency shift of the spin, ∆ _ω_ , induced by the pulse is cancelled. **b** The emitter state before spontaneous emission transitions between the _|ψE⟩_ = ( _|↑_ g _⟩_ + _|↓_ e _⟩_ ) _/√_ 2 (red highlight) and _|ψO⟩_ = ( _|↓_ g _⟩_ + _|↑_ e _⟩_ ) _/√_ 2 (blue highlight) states for even and odd windows. **c** Fluorescence during the standard protocol (orange) and the modified protocol (blue) is shown. For the modified protocol, the fluorescence switches between emission rates Γ _B_ and Γ _A_ with each _π_ pulse, corresponding to the states in panel b. The higher count rate in the very beginning of the sequence is due to a temporarily higher bias current when the SNSPD is biased on. **d** Ground manifold spin coherence relevant for entanglement attempts is measured for XY-16 (blue) and Hahn echo (orange), perturbed by an off-resonant optical pulse with equivalent power to excitation pulses (1.6 nW). The XY-16 total evolution time used in the entanglement generation is 80.5 _µ_ s, also indicated by the grey dashed line. 

xi 









## **Methods** 

## **1 Experimental details** 

In this work, we use a CaWO4 sample (SurfaceNet GmbH) polished at (100) orientation (surface in a-c plane) with erbium introduced by ion implantation (II-VI Inc.) using an energy of 35 keV and a fluence of 5 _×_ 10<sup>9</sup> ions per cm<sup>2</sup> . Following the implantation, the sample was annealed in air at a temperature of 300<sup>_◦_</sup> C for one hour. The nanophotonic devices stamped on the surface of the CaWO4 sample were fabricated from silicon-on-insulator wafers following the procedure described in ref. [46]. The cavity used in this work has a quality factor of _Q_ = 1 _._ 6 _×_ 10<sup>5</sup> , allowing to Purcell enhance the Er<sup>3+</sup> emission rate, such that emission lifetime for the investigated ion is reduced from 6.3 ms to 18.4 _µ_ s for the optical _B_ transition, used for generating spin-photon entanglement. Due to its larger detuning from cavity resonance, the optical _A_ transition has a longer lifetime of 85.2 _µ_ s. The device is tuned on resonance with the Er<sup>3+</sup> optical transitions via nitrogen condensation. A photonic crystal grating coupler and an angle-polished single-mode fiber are used to couple light to the cavity. The device and sample are cooled to _T_ = 0 _._ 47 K in a<sup>3</sup> He cryostat (BlueFors LD250HE). 

For optical addressing of Er<sup>3+</sup> transitions, we use a continuous-wave tuneable laser (Toptica CTL1500) offset locked to a second laser (Toptica CTL1500), which is frequency stabilized to ultra-low expansion reference cavity (Stable Laser Systems) by Pound–Drever–Hall lock technique. Optical pulses are generated using an intensity-modulating electro-optic modulator and two acousto-optic modulators to provide high extinction. Time-delayed fluorescence is detected using an SNSPD (Photon Spot). To avoid saturating the detector, the SNSPD bias current is turned off during optical excitation. 

The spin transitions are driven with microwave pulses delivered by a wirebond antenna attached to the end of the optical fiber. Microwaves are generated using two IQ-modulated synthesizers (Agilent PSG E8267D) with signals being amplified to 3W before entering the cryostat. 

Unless otherwise indicated, all experiments are performed at magnetic field strength of _|B|_ = 943 _._ 5 G at orientation ( _θ, ϕ_ ) = (85<sup>_◦_</sup> , -22<sup>_◦_</sup> ), where _θ_ is the angle from the CaWO4 _c_ -axis and _ϕ_ is the angle from the _a_ -axis, which yields an optimal cyclicity for the optical _B_ transition of _C_ = 600(10). At this magnetic field setting, we work with a ground state spin-splitting of _ωg_ = 10 _._ 7 GHz and excited state spin-splitting of _ωe_ = 9 _._ 5 GHz and drive the spin transitions with Rabi frequencies Ω _R,g_ = 13 MHz and Ω _R,e_ = 7 MHz respectively, for the ion in this work. Finally, for the experiments probing optically induced spin dephasing, the optical pulse is detuned by 1 GHz from the ion. 

## **2 Optically induced spin dephasing** 

As discussed in the main text, we observe that optical pulses induce dephasing of the spin in the form of random but static frequency fluctuations (Fig. **2** ). Here, we supplement the discussion and report additional experiments to understand the origin of the dephasing mechanism. 

First, we discuss the time-dependence of the dephasing effect. For optical pulses that are short with respect to the total evolution time, the effective evolution time _τe_ under a random frequency shift, ∆ _ω_ is given as _τe_ = min( _τ_ opt _,_ 2 _τ − τ_ opt), where _τ_ opt is the position of the optical pulse and 2 _τ_ is the total evolution time of the Hahn sequence. The longest effective evolution time is achieved when the optical pulse is placed at the center of the Hahn sequence with _τe_ = _τ_ . For normally distributed ∆ _ω_ , the decay of the contrast over _τe_ can be obtained as: 



where we have integrated over a Gaussian frequency distribution, _f_ ( _ω, σω_ ) with standard deviation _σω_ . Using Eq. 1, we infer _σω_ , by fitting a Gaussian decay envelope with dephasing time _Td_ = _√_ 2 _/σω_ . 

xiii 

Next, we further investigate the dephasing dependence on optical pulse parameters. In Extended Data Fig. **2** a,b, we extract the dephasing magnitude _σω_ as a function of the optical power, _P_ and pulse-width, _W_ . Before the observed saturation, fitting each to an exponential scaling of _σω ∝ P_<sup>_βP_</sup> and _σω ∝ W_<sup>_βW_</sup> yields exponents _βP_ = 0 _._ 52(1) and _βP_ = 0 _._ 43(6), consistent with a square root scaling with the number of photons, _NP ∝ PW_ , so that both experiments can be explained by a random walk model resulting in a frequency spread _σP_ = _kN √NP_ , where _kN_ is an effective prefactor. To also account for the saturation observed, we fit to a simple model that limits the maximum frequency spread by the saturation value _σ_ sat as _σω_<sup>2=</sup><sup>_σ_</sup> sat<sup>2</sup><sup>_S_2</sup><sup>_/_(</sup><sup>_S_2+ 1),where</sup><sup>_S_=</sup><sup>_σP/σ_sat.Suchasaturationbehaviorcouldresultfromexhausting</sup> the configuration space of a finite sized bath. Comparing the extracted saturation, _σ_ sat = 2 _π×_ 370 kHz, to the long-term spin spectral diffusion _σω_<sup>_∗_=</sup> _√_ 2 _/T_ 2<sup>_∗_=2</sup><sup>_π×_980kHz,wefindthattheopticallyinducedspin</sup> spectral diffusion may account for about 1/3 of the spin spectral diffusion over long time scales. 

Finally, we investigate the origin of this dephasing mechanism, which could originate from magnetic or electric field noise. For Er<sup>3+</sup> :CaWO4, electric fields are known to cause shifts of the Er<sup>3+</sup> g-tensor depending on the external magnetic field orientation [48]. In particular, the magnitude of the corresponding frequency shift, ∆ _ωE_ , for a magnetic field in the aa-plane of the CaWO4 crystal is given as: 



where _ωg_ is the frequency splitting of the ground spin state, _g⊥_ is the g-factor in the aa-plane of CaWO4 and _Ez_ is the electric field along the CaWO4 _c_ -axis. _ϕ_ is the angle from the _a_ -axis, _ϕ_ 0 = 31<sup>_◦_</sup> and _α_ = 11 _·_ 10<sup>_−_6</sup> (V/cm)<sup>_−_1</sup> , as discussed in Ref. [44] in the context of spin linewidths. In contrast to the varying sensitivity to electric field noise depending on the field orientation (Eq. 2), the magnetic moment in the aa-plane is uniform, suggesting that the sensitivity to magnetic field noise should not vary. In Fig. **2** e, we measure the optical dephasing effect at various magnetic field orientations on the aa-plane, which confirms the electric field origin of this effect. As expected by Eq. 2, the frequency spread varies as _σω_ = _A|_ sin(2 _ϕ −_ 2 _ϕ_<sup>_′_</sup> 0<sup>)</sup><sup>_|_,where</sup><sup>_ϕ′_</sup> 0<sup>=35(1)</sup><sup>_◦_and</sup><sup>_A_=2</sup><sup>_π×_103(4)kHz.Thesmalldifferencebetween</sup><sup>_ϕ_0</sup> and measured _ϕ_<sup>_′_</sup> 0<sup>couldbeduetoerrorsinthecrystal-cutorthemagneticfieldorientation.Weperform</sup> the field sweep at _|B|_ = 600 G, where the spin splitting is about 7 GHz. Based on Eq. 2, this suggests an electric field fluctuation of _σEz ∼_ 0 _._ 2 kV/cm induced by the optical pulse in this experiment, equivalent in magnitude to a field from a single point charge at a distance of _∼_ 100 nm. We note that the electric field fluctuations can be larger on a longer time-scale as inferred from the inhomogenous spin linewidth of a bulk ensemble in Ref. [44]. We note that the electric field origin of optically induced dephasing is also confirmed by a separate measurement of a _g_ = 2 ( _S_ = 1 _/_ 2) paramagnetic impurity coupled to the ion in this work. For the _g_ = 2 spin, we find that optical pulses have no effect on the spin coherence. Given the sensitivity of this impurity to magnetic noise, this agrees with our conclusion that the perturbation caused by the optical pulse is electric in origin rather than magnetic. 

In the spin-photon entanglement experiments, we decouple this effect using the dynamical decouplingbased entanglement sequences. In Extended Data Fig. **2** c, we repeat the XY-16 experiment with an offresonant optical pulse at a range of optical powers, which confirms that the sequence is robust to optically induced dephasing when the optical pulse is placed at a refocusing point of the sequence. While the dephasing mechanism can also be suppressed by an appropriate choice of the magnetic field orientation, to optimize cyclicity we are constrained to use a field orientation slightly off the aa-plane and at an angle that is sensitive to electric field fluctuations. In future, the alignment between the photonic cavity and the crystal can also be adjusted to obtain a field orientation with good cyclicity that is also less susceptible to the optically induced dephasing effect. 

## **3 Spin coherence of the spin-photon state** 

Here, we discuss spin coherence during the spin-photon entanglement protocol with dynamical decoupling in the context of a generalized form of the protocol (Extended Data Fig. **4** ). Dynamical decoupling is 

xiv 

a well studied technique to decouple fast noise [56]. Intuitively, our protocol simply performs dynamical decoupling in both the ground and excited spin manifolds to decouple noise in each, regardless of when the state decays from the excited state. However, the decay, at time _t_ , can still occur in the middle of a decoupling unit, ( _τ − π − τ_ ), before the phase is entirely refocused in the excited manifold. Even in this case, we show that phase is still fully corrected for quasi-static noise. For fast noise, we find that there is a residual term, which can also be eliminated in the limit of smaller pulse spacings. 

We consider decoupling under a dynamic noise bath, which can represent interactions with a bath of paramagnetic impurities, or charge noise as discussed in Methods S2, in a mean-field approach [57]. In the rotating frame for the ground and excited spin manifolds, the 4-level Hamiltonian in the presence of dynamic noise can be given as: 



where _Sz_<sup>_g_=</sup> 21<sup>diag(0</sup><sup>_,_0</sup><sup>_,_1</sup><sup>_, −_1)and</sup><sup>_S_</sup> _z_<sup>_e_=</sup> <u>12</u><sup>diag(1</sup><sup>_, −_1</sup><sup>_,_0</sup><sup>_,_0)arethegroundandexcitedspinoperators</sup> respectively. For noise that is magnetic in origin, the ground and excited state noise terms are related by the magnetic moments of the spin states such that _βe_ ( _t_ ) = _rβg_ ( _t_ ), where _r_ = _ωe/ωg_ . For noise originating from electric field fluctuations, the noise terms should still be correlated but the scaling, _r_ , would depend on the distortion of the excited state g-tensor of Er<sup>3+</sup> :CaWO4, which has not been measured to our knowledge. 

We calculate the phase accumulated in our sequence under this noise model as represented in Extended Data Fig. **4** . A decoupling sequence with _N_ pulses can be expressed as _N_ repetitions of the decoupling unit as ( _τ − π − τ_ )<sup>_N_</sup> . If spontaneous emission occurs on the boundary of a decoupling unit ( _i.e. t_ = 2 _τk_ , _k ∈Z_ ), the total phase can be simply expressed as a sum over decoupling units before and after the emission, equivalent to standard decoupling sequences. In general, as indicated by the highlighted areas in Extended Data Fig. **4** , when spontaneous emission does not occur at a boundary, a residual phase term will emerge: 



betweenwhere _β_ ¯ _g_ ( _ti, tfk_ ) = _e_ the=� _tt_ two _if_ round<sup>_βg_(</sup> optical<sup>_t_)</sup> (<sup>_dt/_</sup> _t/_ 2<sup>(</sup> _τ_<sup>_tf_</sup> )pulses.<sup>_−_</sup> is<sup>_ti_</sup> the<sup>).First,</sup> _β_ ¯nearest _g_ ( _ti, t_<sup>we</sup> _f_ )<sup>note</sup> decouplingdenotes<sup>that</sup> time-average<sup>ifthe</sup> unit<sup>noise</sup> to the<sup>is</sup> over<sup>quasi-static,</sup> emissionthe time-interval,time<sup>constant</sup> _t_ and<sup>over</sup> [ _tiT, tf_<sup>the</sup> is] definesthe<sup>duration</sup> timeas of the entanglement attempt, the phase resulting from the decay time after the first excitation is cancelled by an equivalent term after the second excitation, after a time _T_ . The cancellation of these terms after a longer time implies that noise at these two points is less likely to be correlated and may not be canceled efficiently. Second, the residual phase term is suppressed by correlations _r_ between the ground and excited state, disappearing for _r_ = 1. We expect that the optically induced dephasing mechanism discussed in Methods S2 will induce an uncorrected frequency shift for this residual term, whose magnitude depends on the emission time _t_ . In our experiment, we do not observe a strong dependence of the Bell state fidelity with respect to the emission time (Extended Data Fig. **5** ), indicating that this residual term is small. Finally, the duration of the residual phase accumulation, (2 _τke − t_ ), can at most be _τ_ so that _ϕ_<sup>˜</sup> _r_ will disappear in the limit of choosing shorter _τ_ for the decoupling sequence. 

## **4 Optical decoherence during the entanglement sequence** 

In this section, we calculate the optical phase of the spin-photon state after the photon travels through the interferometer. Then, we briefly discuss the loss of coherence due to fast optical spectral diffusion and how we estimate the optical coherence in our experiment. 

First, we discuss the regime where all optical frequency fluctuations are static over a single attempt and show that slow spectral diffusion does not lead to phase errors. As discussed in the main-text, a MW _g π/_ 2 pulse followed by an optical _πB_ pulse prepares the superposition ( _|↓_ e _⟩_ + _|↑_ g _⟩_ <u>)</u> _<u>/√</u>_ 2. Spontaneous emission of this state in an even time-window yields ( _e_<sup>_i_(</sup><sup>_kx−ωBτ_1)</sup> _|↓_ g _⟩|E⟩_ + _|↑_ g _⟩|_ 0 _⟩_ ) _/√_ 2, where _τ_ 1 is the detection time after the optical _πB_ pulse, _x_ is the optical path-length of the long arm, _ωB_ is the frequency of the probed transition and _k_ = _ωB/c_ is the wavevector. After an odd number of _π_ pulses and a second optical 

xv 

excitation at time _T_ , we obtain the state ( _e_<sup>_i_(</sup><sup>_kx−ωBτ_)</sup> _|↑_ g _⟩|E⟩_ + _e_<sup>_−iωLT_</sup> _|↓_ e _⟩|_ 0 _⟩_ ) _/√_ 2, where the phase of the laser at frequency _ωL_ is imprinted on the excited term. Finally, the spontaneous emission of the second excitation and completion of the decoupling sequence prepares the spin-photon entangled state: 



where _τ_ 2 is the detection time after the second optical _πB_ pulse. The detection of a single photon at time _τ_ det, projects both _τ_ 1 and _τ_ 2 so that _τ_ det = _τ_ 1 = _τ_ 2 + _T_ . Each variable can also be broken down into a time of emission and propagation time, _τ_ 1 = _t_ 1 + _T_<sup>_′_</sup> and _τ_ 2 = _t_ 2, where _T_<sup>_′_</sup> = _x/c_ is the true propagation delay of the interferometer and _t_ 1(2) is the time of emission after the first (second) optical excitation. After simplification, we find that the relative phase of the Bell state in the quasi-static regime is given as _ϕ_ Bell = _ϕ_ + ∆ _ω_ ∆ _T_ , where ∆ _ω_ = _ωB − ωL_ is the detuning of the emitter from the laser frequency, ∆ _T_ = _T_<sup>_′_</sup> _− T_ is the difference between the true propagation delay of the interferometer and the experimental delay and _ϕ_ = _ωLT_<sup>_′_</sup> is the interferometer phase at the laser frequency. For our parameter regime, the shot-to-shot spectral diffusion ∆ _ω_ is on the order of 100 kHz and the propagation delay mismatch is on the order of 10 ns so that the phase error is very small (∆ _ω_ ∆ _T ≪_ 1). 

However, optical frequency fluctuations within a single entanglement attempt can decohere the Bell state. To estimate the effect of fast frequency fluctuations on the optical coherence of the spinphoton entanglement experiment, we use the Hong-Ou-Mandel (HOM) visibility, which probes the indistinguishability of photons separated by the interferometer delay _T_ (Extended Data Fig. **6** ). For this estimate, we assume that frequency fluctuations are either much slower or much faster than the time-scale of our experiment. As argued above, any noise that is static over an entanglement attempt does not lead to optical dephasing. For the fast noise, we assume a Markovian noise model, where the frequency fluctuations are drawn from a Gaussian distribution with an infinitesimally short correlation time [58]. Following the discussion in Ref. [45], we fit the HOM interference to obtain a pure dephasing time _Tϕ_ under this model, leading to a reduced coherence _F_ ( _t_ ) = exp( _−_ 2 _t/Tϕ_ ) for a given emission time _t_ , or equivalently a detection time-difference for the HOM experiment. The average optical coherence for photons collected in a given time-window, [ _t_ 1 _, t_ 2] can then be calculated as: 



where 1 _/T_ 2 = 1 _/_ 2 _T_ 1 + 1 _/Tϕ_ and _T_ 1 = _τr_ . The HOM fit yields a dephasing time _Tϕ_ = 31 _._ 5 _µ_ s, which leads to an _fop_ (0 _,_ 2 _._ 5 _µ_ s) = 0 _._ 93 for the time-window used in the Fig. **4** . In Extended Data Fig. **9** , we extend the entanglement sequence to additionally use a later collection window, which is estimated to have a lower optical coherence of _fop_ (7 _._ 5 _µ_ s _,_ 12 _._ 5 _µ_ s) = 0 _._ 53. We also note that, as discussed for spin coherence in the main-text, electric field fluctuations induced by the optical pulse also cause a frequency shift of the optical transitions. We do not analyze the effect of this on the optical coherence here. 

## **5 Phase monitoring** 

Here, we discuss the experimental setup and analysis to measure the phase of the interferometer. The phase of the MZI is tracked using a pair of avalanche photodiodes (APDs) placed in one of the output ports of the MZI (see Extended Data Fig. **7** a), registering the interference of two reference laser pulses sent through the interferometer after each entanglement attempt. The APD signals are recorded using an oscilloscope (PicoScope 5000). The two phase tracking pulses are generated at the same time as the two _πB_ pulses in the spin-photon entanglement experiment (Fig. **3** ). To generate these pulses, a laser beam is divided into two optical paths (not shown), where a small fraction of laser light enters the cryostat for the optical excitation of the ions and a larger fraction is used for phase tracking to provide sufficient SNR. The phase tracking pulses are passed through an optical switch, turned on for the early and late entanglement attempt pulses 

xvi 

only, before entering an input port of the MZI. Due to the scattering of the phase tracking laser pulses in the 15.6 km fiber spool of MZI, an additional time-dependent signal is observed in the time trace of the background counts as shown in Extended Data Fig. **10** a. To avoid the overlap of the entangled photons with this scattering signal, phase monitoring pulses are delayed by 7.3 _µ_ s with an additional 1.5 km fiber spool before entering the MZI. For the experiment in Extended Data Fig. **9** , a 3 km fiber spool is used instead to delay the scattering further and avoid the overlap with the later photon collection window. 

Next, we discuss the required analysis to obtain the phase. The two phase tracking pulses sent through the interferometer accumulate a relative phase, _ϕ_ . When recombined, this relative phase results in amplitudes of 1 _±_ cos _ϕ_ in the two output ports of the interferometer. By measuring one of these output amplitudes using an APD, the phase _ϕ_ can be measured up to an integer multiple of _π_ . To resolve the full phase up to 2 _π_ , we use a technique developed in Ref. [59] based on simultaneous measurements of interference that are out-of-phase. Here, the birefringence property of the 15.6 km long optical fiber is utilized, which is induced by bending strain in the fiber spool. Laser pulses polarized along the fast axis or slow axis can gain different phases, i.e. **E** _fast → e_<sup>_iϕ_</sup> **E** _fast_ and **E** _slow → e_<sup>_i_(</sup><sup>_ϕ_+</sup><sup>_δϕ_)</sup> **E** _slow_ , corresponding to two different amplitudes after the interferometer, 1 + cos _ϕ_ and 1 + cos( _ϕ_ + _δϕ_ ). Because the phase difference _δϕ_ is random and usually non-zero, cos _ϕ_ and cos( _ϕ_ + _δϕ_ ) do not reach maximum or minimum at the same time, leading to reduced interferometer visibility if the input polarization is not aligned with one of the principal axes. To align the birefringent axes with the polarization of single photons, equivalently the cavity polarization, we optimize the interference contrast of the cavity reflected light on SNSPDs after the MZI. After traveling through the MZI, the phase tracking pulses are split using a PBS to separately read the phase of the fast and slow axes polarizations. Thus, each phase monitoring yields two measurements, cos _ϕ_ for the polarization of the single photons, and cos( _ϕ_ + _δϕ_ ) for the polarization perpendicular to the single photons, revealing an ellipse when plotted against each other over many trials (Extended Data Fig. **7** b). The eccentricity of the ellipse can be fitted to extract _δϕ_ and determine the phase, _ϕ_ , of each point on the ellipse up to an integer multiple of 2 _π_ . The phase difference _δϕ_ changes by less than a degree over twenty minutes, while the phase _ϕ_ of the interferometer only remains stable for several milliseconds, as shown in Extended Data Fig. **7** c,d. 

The knowledge of cos _ϕ_ and cos( _ϕ_ + _δϕ_ ) can resolve the phase up to 2 _π_ , but cannot distinguish _±ϕ_ without knowing the sign of _δϕ_ , i.e., which axis is fast or slow. In this work, we do not distinguish the sign, but instead keep track of _δϕ_ such that it does not cross 0 or 2 _π_ . 

## **6 Conditional operation** 

To increase the spin-photon entanglement generation rate, we perform a spin readout conditional on the detection of a single photon in the heralding window. For that purpose, we utilize a complex programmable logic device (CPLD), which switches the experiment state between two modes: (E) initialization followed by the entanglement attempt, and (R) spin readout (see Fig. **4** a in the main text). The default CPLD state is E, so that entanglement attempts are performed most of the time. In the case of relatively rare events of single photon detection (probability of 6 _._ 7 _×_ 10<sup>_−_4</sup> per attempt), the CPLD changes the experiment state to R. After sending 432 optical readout pulses (lasting around 49 ms), it switches back to E mode. The CPLD switches the experiment between the two modes by controlling the flow of the gating and triggering signals to the switches and waveform generators responsible for optical and MW pulse generation. The basic block sequence in our experiment is defined by 6 periods each lasting 75.5 _µ_ s. In E mode, it consists of 2 initializing pulse pairs [Methods S7], an empty period followed by an entanglement attempt consisting of 2 optical pulses, and ends with another empty period. Entanglement pulses are sandwiched between empty periods to prevent overlap of entanglement photons with photons emitted after the last initialization and the first readout pulses (due to the delay picked up in the MZI). In R mode, the block sequence is repeated 108 times and consists of four readout pulses and two empty periods. The presence of empty periods in R mode is inherited from the E sequence, but it does not serve any purpose. Conditional spin readout allowed us to increase the spin-photon entanglement generation rate by two orders of magnitude 

xvii 

by skipping the slow readout when no photon is detected within the heralding window. 

## **7 Initialization and readout** 

For spin initialization, we used a sequence consisting of optical _πA_ pulses, each followed by a chirped microwave pulse resonant with an excited state spin transition. The chirped pulses were used to achieve a high inversion of the excited state spin population, in the presence of interaction with two paramagnetic impurities with interaction strength near 3.3 MHz, close to the Rabi frequency of Ω _R,e_ = 7 MHz for the excited state. This allowed us to initialize using only two initialization cycles in the spinphoton entanglement experiment with an estimated fidelity of 98.5% based on fluoresence measured after initialization. 

For spin readout, we used a sequence of 240 and 432 optical _πB_ pulses each followed by a fluorescence collection window of 70 _µ_ s, for spin dynamics experiments without the MZI and spin-photon entanglement experiments, respectively. To differentiate the two spin states, a threshold of one photon is used. The number of readout pulses for each type of experiment is optimized to maximize the readout fidelity. For spin dynamics experiments, after initializing the spin into the _|↑⟩_ ( _|↓⟩_ ) state, an average of 3.1 (0.1) photons is observed, allowing for _|↑⟩_ ( _|↓⟩_ ) readout with fidelity _F↑_ = 0 _._ 93 ( _F↓_ = 0 _._ 85). For the spin-photon entanglement experiment, the spin-readout fluorescence signal is passed through the MZI with a 15.6 km fiber delay, introducing 72% of additional photon loss. In this case, an average of 1.4 (0.2) photons is observed after initializing spin into the _|↑⟩_ ( _|↓⟩_ ) state, allowing for _|↑⟩_ ( _|↓⟩_ ) readout with fidelity _F↑_ = 0 _._ 81 ( _F↓_ = 0 _._ 69). Corresponding histograms of photon counts are shown in Extended Data Fig. **8** . We note that both the spin dynamics and spin-photon entanglement data shown in the main manuscript are normalized to readout fidelity. The readout fidelity here is lower than in previous work [45], primarily because of the lower Purcell factor, resulting in lower cyclicity and higher dark counts accumulated over a longer photon collection window. For entanglement experiments an additional factor is photon loss in the MZI, which can be mitigated in the future by bypassing the MZI with an optical switch during spin readout. 

## **8 Spin-photon entanglement fidelity estimation** 

Here, we describe the procedure to estimate the spin-photon entanglement fidelity in each basis. For ZZ basis measurements, which correlate the spin state in the _Zs_ basis and the photon state in the _Zp_ basis, the correlation between spin and photon measurements can be directly calculated, as shown in Fig. **4** e. For XX (YY) basis measurements, which correlate the spin state in the _Xs_ ( _Ys_ ) basis and the photon state in the Φ _p_ basis, we use Bayesian inference to estimate the finite fidelity spin-photon state most likely to yield the measurement results. Suppose the state is in the form of _ρ_ ( _α_ ) = _α |_ Ψ _⟩⟨_ Ψ _|_ +(1 _−α_ ) _I_ , where _|_ Ψ _⟩_ is the desired spin-photon Bell state and _I_ is the fully mixed state. Projecting _ρ_ ( _α_ ) onto the measured spin and photon state gives the conditional probability to obtain the measurement given _α_ : _P_ ( _|↑, ±ϕ⟩|α_ ) = (1 _± α_ cos _ϕ_ ) _/_ 2 for XX basis and _P_ ( _|↑, ±ϕ⟩|α_ ) = (1 _± α_ sin _ϕ_ ) _/_ 2 for YY basis. The likelihood of parameter _α_ given the dataset is _P_ (result _|α_ ) = Π _iP_ ( _|Si, Pi⟩|α_ ), taking a product over all heralded entanglement attempts indexed by _i_ . Finally, the likelihood function _f_ ( _α_ ) = _P_ (result _|α_ ) is fitted using a Gaussian to extract the value of _α_ that is most likely to reproduce the result and its uncertainty. The contrast of the oscillation for the XX or YY basis is given by the fitted parameter _EX/Y_ = _α_<sup>_∗_</sup> . While data is not binned for the estimation, we bin it into 11 phase points to plot it in Fig. **4** c,d. 

We correct the spin-photon correlations for the readout fidelity after fitting. The fidelities of reading two spin states are _F↑_ = 0 _._ 81 and _F↓_ = 0 _._ 69 respectively [Methods S7]. Therefore, the probability of measuring state _|↑⟩_ is _P_ ( _m_ = _|↑⟩_ ) = _F↑P_ ( _|↑⟩_ ) + (1 _− F↓_ ) _P_ ( _|↓⟩_ ). Alternatively, given the measured probability, the readout corrected population is _P_ ( _|↑⟩_ ) = ( _P_ ( _m_ = _|↑⟩_ ) _−_ 1+ _F↓_ ) _/_ ( _F↑_ + _F↓ −_ 1). Thus, the measured contrasts in the spin-photon entanglement experiment are scaled by ( _F↑_ + _F↓ −_ 1)<sup>_−_1</sup> to obtain the readout corrected fidelity. 

xviii 

## **9 Extended spin-photon sequence** 

As mentioned in the main-text, we limit our photon collection window to the first 2.5 _µ_ s for the XY-16 based entanglement sequence to minimize sensitivity to fast dephasing of the optical transition. Here, we discuss an additional spin-photon entanglement experiment based on the XY-20 dynamical decoupling sequence, which allows us to use a second collection window by prolonging the sequence duration to include this emission window (Extended Data Fig. **9** a,b). Then, we briefly discuss requirements to include all emitted photons in the sequence. 

In Extended Data Fig. **9** c,d, we observe parity oscillations of the Bell state for both the first and second heralding windows. Photons collected from the two windows yield visibilities of _{EX_ 1 _, EY_ 1 _, EZ_ 1 _}_ = _{_ 0 _._ 48(3) _,_ 0 _._ 47(3) _,_ 0 _._ 80(1) _}_ and _{EX_ 2 _, EY_ 2 _, EZ_ 2 _}_ = _{_ 0 _._ 14(3) _,_ 0 _._ 09(3) _,_ 0 _._ 72(1) _}_ , leading to fidelities _F_ 1 = 0 _._ 69(1) and _F_ 2 = 0 _._ 49(1) respectively. The slightly lower visibility of parity oscillations in the first window for this experiment in comparison to the XY-16 based experiment is due to lower spin coherence ( _fs_ = 0 _._ 67) after the longer spin evolution time under the XY-20 sequence. The lower visibility of the second window is primarily due to the lower optical coherence for cases where spontaneous emission occurs in the second heralding window of [7.5 _µ_ s – 12.5 _µ_ s] ( _fop_ = 0 _._ 53), which can be roughly estimated based on the dephasing time extracted from the HOM experiment [Methods S4]. Another factor for the lower fidelity is the higher impact of background counts due to the lower emission rate in the second window ( _fbg_ ( _X/Y_ ) = 0 _._ 91, _fbg_ ( _Z_ ) = 0 _._ 92). A final factor may be larger pulses errors experienced in the excited state arising from the lower Rabi frequency (Ω _R,e_ = 7 MHz), comparable to interaction strength of 3.3 MHz with two paramagnetic impurities. While the second window has lower fidelity, integrating over all photons in both windows, we obtain a rate of _R_ = 2 _._ 8 Hz and visibilities of _{EX , EY , EZ}_ = _{_ 0 _._ 31(2) _,_ 0 _._ 30(2) _,_ 0 _._ 76(1) _}_ , leading to an entanglement fidelity of _F_ = 0 _._ 59(1), still above the classical threshold. 

To make use of all emitted photons, we need larger optical and spin coherence and additionally track the interferometer phase at the frequency _ωA_ , corresponding to photons emitted in the odd windows. 

## **10 Error model for spin-photon entanglement** 

The error sources of the spin-photon entanglement generation in this work (Fig. **4** ) mainly consist of finite optical and spin coherence, pulse errors, background photon counts, initialization fidelity, and finite optical lifetime. The error values, _ϵ_ , stated in the main-text are expressed as fidelity contributions, _f_ = 1 _− ϵ_ , in the following discussion. 

The optical coherence can be obtained from the Hong–Ou–Mandel (HOM) visibility through the same interferometer used in the experiment, as shown in Extended Data Fig. **6** . The end of the heralding window of 2.5 _µ_ s after the optical excitation used in the entanglement experiment gives a HOM visibility of _fop_ = 0 _._ 93. The spin coherence during the spin-photon entanglement experiment is assumed to be similar to the spin coherence under XY-16 dynamical decoupling sequence because the ion spends at most 2.5 _µ_ s in the excited state compared to the total free evolution time of 80.5 _µ_ s. The heralding measurement also ensures that both spin states spend the same amount of time in the excited state such that the extra phases acquired due to excitation are canceled by the dynamical decoupling as discussed in Methods S3. Furthermore, the standard XY-16 sequence contains errors due to imperfect pulses. Based on Extended Data Fig. **3** , the spin coherence is _fs_ = 0 _._ 75 after 80.5 _µ_ s of total evolution time used in the entanglement experiment. Both the optical and spin coherence induced errors contribute only to XX and YY basis in the spin-photon entanglement. For the ZZ basis, optical coherence is assumed to be irrelevant. To estimate the effect of pulse errors, we apply the XY-16 decoupling sequence, without _π/_ 2 pulses, directly on the _|↑_ g _⟩_ and _|↓_ g _⟩_ states, which yields a reduced contrast of _fp_ = 0 _._ 86. 

Dark counts of the SNSPDs and the laser scattering contribute to the background photon counts we observe in the experiment. The background is measured by repeating the spin-photon entanglement experiment sequence with the laser detuned from the ion by 100 MHz, as shown in Extended Data Fig. **10** . In the ZZ basis, the background photon counts are similar to the dark count rate of 6 Hz, and the two 

xix 

heralding windows yield a false heralding probability of 4%, or _fbg_ ( _Z_ ) = 0 _._ 96. In the XX/YY basis, the background counts are higher than the dark counts at around 15 Hz due to scattered photons from the phase tracking pulses. The single XX/YY heralding window yields a false heralding probability of 5%, or _fbg_ ( _X/Y_ ) = 0 _._ 95. 

Initialization errors also reduce the contrast of the Bell state parity oscillations. A false initialization probability of 1.5% reduces the contrast of parity oscillations by 3%, so that the contribution is _fi_ = 0 _._ 97. However, initialization errors do not affect the ZZ basis measurement since the heralding of the _|E⟩_ or _|L⟩_ photon state correctly projects the spin-state regardless of initialization errors. 

The finite optical lifetime can lead to a residue excited state population excited by the first optical pulse, which does not decay before the second optical excitation. During the spin-photon entanglement sequence, the probabilities of photon emission during the second heralding window excited by the first or second optical pulses are _P_ 1 = _e_<sup>_−T_(1</sup><sup>_/_2</sup><sup>_τA_+1</sup><sup>_/_2</sup><sup>_τB_)</sup> (1 _− e_<sup>_−δ/τA_</sup> ) = 0 _._ 2% and _P_ 2 = 1 _− e_<sup>_−δ/τB_</sup> = 9 _._ 8% respectively. Here _δ_ = 1 _._ 9 _µ_ s is the heralding window width, _T_ = 75 _._ 5 _µ_ s is the separation between two optical pulses, and _τA_ = 85 _._ 2 _µ_ s and _τB_ = 18 _._ 4 _µ_ s are the optical lifetime of two optical transitions of the ion. This corresponds to the contrast of _fl_ = _P_ 2 _/_ ( _P_ 1 + _P_ 2) = 0 _._ 98 for both ZZ and XX/YY basis measurements. 

By accounting for the above source of errors, the expected contrasts are _EX/Y_ = _fopfsflfbg_ ( _X/Y_ ) _fi_ = 0 _._ 63 and _EZ_ = _fpflfbg_ ( _Z_ ) = 0 _._ 81, compared to the experiment result _EX_ = 0 _._ 60, _EY_ = 0 _._ 55, and _EZ_ = 0 _._ 77. The expected final fidelity is 0.78, compared to the experiment result of 0.73. 

## **11 Entanglement rate** 

In this section, we discuss the current entanglement rate and consider its extensions. We start by discussing factors yielding the current rate and estimate the spin-photon entanglement rate that can be achieved with improvements to these factors. 

For the spin-photon entanglement generation experiment, we use two initialization pulse pairs followed by two optical excitation pulses (Fig. **4** a), repeated at a rate of 2.2 kHz. The entanglement generation is successful with probability _P_ ent = 6 _._ 7 _×_ 10<sup>_−_4</sup> , leading to the entanglement rate of 1.48 Hz in our experiment, which is not limited by the readout performed conditionally [Methods S6]. The probability _P_ ent is limited by the total photon collection efficiency and the finite width of the photon collection window in our protocol. The experimentally recorded probability of detecting a single photon on an SNSPD after optical excitation is around 0 _._ 02, which is limited by several factors, including the photon extraction efficiency from the cavity _ηcav_ = 0 _._ 24, the grating coupler efficiency _ηgc_ = 0 _._ 33, the transmission through the passive optical components _ηnet_ = 0 _._ 61 and the SNSPD detection efficiency _ηdet_ = 0 _._ 85. The combined predicted detection probability is _P_ = _ηcav × ηgc × ηnet × ηdet_ = 0 _._ 04. For spin-photon entanglement experiments, efficiency is further decreased by the losses of the MZI _ηMZI_ = 0 _._ 28 (dominated by 15.6 km fiber delay) and the narrow photon collection window of 1.9 _µ_ s, corresponding to _ηpc_ = 0 _._ 091. This gives an overall predicted entanglement generation probability of _P_ ent = _P × ηMZI × ηpc_ = 1 _._ 0 _×_ 10<sup>_−_3</sup> , close to the measured value of 6 _._ 7 _×_ 10<sup>_−_4</sup> . 

The rate can be further improved with straightforward improvements to these parameters. First, the entanglement attempt rate can be increased to 3.3 kHz (x1.5), for a total attempt duration of (1 + 2 + 1) _×_ 75 _._ 5 _µ_ s, by using a single initialization pulse, two pulses for the entanglement attempt and an additional waiting period to collect all photons after the MZI. Using a cavity that is critically coupled would lead to an _ηcav_ of 0 _._ 5 (x2), gaining in coupling efficiency without significantly reducing the _Q_ of the cavity. Switching to an adiabatically tapered fiber for coupling to the photonic device, instead of a grating coupler, could lead to a coupling efficiency of 0.97 (x3) [51]. Finally, using all emitted photons would lead to _ηpc_ of 1 (x11). As discussed in Methods S9, the use of all emitted photons is currently limited by fast optical dephasing and spin coherence errors. Improving optical and spin coherence would facilitate the collection of all emitted photons. Leaving other factors fixed, these improvements would lead to an entanglement rate of 150 Hz after 15.6 km. 

xx 



<!-- Start of picture text -->
—<br><!-- End of picture text -->



<!-- Start of picture text -->
rd+€°<br>«7<br><!-- End of picture text -->



<!-- Start of picture text -->
-<br>2<br><!-- End of picture text -->



<!-- Start of picture text -->
I i<br><!-- End of picture text -->



<!-- Start of picture text -->
$ 3<br>[: } t iss<br><!-- End of picture text -->



<!-- Start of picture text -->
:<br><!-- End of picture text -->



<!-- Start of picture text -->
T<br>t t<br>Optical<br>MWg ... ...<br>MWe ... ...<br> Spin ... ...<br>phase<br>2τ<br><!-- End of picture text -->

**Extended Data Fig. 4** : **Spin-photon decoupling sequence.** Spin phase accumulation during the spinphoton entanglement with dynamical decoupling for with inter-pulse spacing 2 _τ_ and seperation between optical pulses of _T_ = 2 _τkp_ , where _kp_ is an odd integer. The red dashed lines indicates the emission time of the photon after time _t_ with respect to each optical pulse. For slow noise, the phase is fully canceled, indicated by the total area summing to 0. The highlighted squares indicate the small amount of phase that is cancelled after a longer time _T_ . 



<!-- Start of picture text -->
a b<br>1.0 2.0<br>0.9 1.5<br>0.8 1.0<br>0.7 0.5<br>0.6 0.0<br>0.2 0.6 1.0 1.4 1.8 2.2 0.2 0.6 1.0 1.4 1.8 2.2<br>Collection window width ( μ s) Collection window width ( μ s)<br>Fidelity<br>Rate (Hz)<br><!-- End of picture text -->

**Extended Data Fig. 5** : **Entanglement fidelity vs rate. a** The spin-photon entangled state fidelity and **b** rate as a function of the photon collection window width. The collection window starts 0.4 _µ_ s after the falling edge of the optical _π_ pulse. Error bars correspond to one s.d. 



<!-- Start of picture text -->
a b<br>250 1.0<br>200<br>150 0.8<br>100<br>0.6<br>50<br>0<br>−0.2 −0.1 0.0 0.1 0.2 0 10 20 30 40<br>Detection time difference  τ1 −τ2  (ms) Detection window width ( μ s)<br>HOM visibility<br>HOM coincidences<br><!-- End of picture text -->

**Extended Data Fig. 6** : **Generation of indistinguishable photons. a** Two-photon interference histogram for photons emitted by the same ion spaced by 75.5 _µ_ s. The grey dashed line corresponds to an independently recorded background level. The solid black line is a fit. **b** HOM visibility extracted from the fit corrected for background counts and imperfections of the MZI. For the detection window width of 2.5 _µ_ s (corresponding to the photon detection window in the entanglement experiment), we observe a HOM visibility of 0.93. 

xxiii 



<!-- Start of picture text -->
Optical excitation<br>85:15 pulses<br>BS<br>50:50<br>BS<br>Phase tracking  Optical<br>pulses  switch<br><!-- End of picture text -->



<!-- Start of picture text -->
Optical excitation 15.6 km<br>pulses fiber<br>PC<br>SNSPD1<br>50:50 50:50<br>BS BS SNSPD2<br>90:10<br>VOA PC BS<br>HWP APD1<br>Phase detection<br>PBS APD2 setup<br>c d<br><!-- End of picture text -->



**Extended Data Fig. 7** : **Phase tracking. a** Optical setup used to measure time-bin photons after 15.6 km of fiber in an unbalanced MZI and track the interferometer phase. Optical pulses for excitation and phase tracking are sent to nanophotonic cavity and interferometer respectively. Single photons from the Er<sup>3+</sup> ion are detected at two SNSPDs after the MZI. A variable optical attenuator (VOA) attenuates the short arm to match the attenuation rate of the 15.6 km fiber spool and polarization controllers (PC) are used to match the polarization of single-photons from each arm. Bright phase tracking pulses are measured in two orthogonal polarizations on avalanche photodiodes (APD), using a half-wave-plate (HWP) followed by a polarization beam splitter (PBS). **b** Ellipse constructed from the phase detection setup. 5000 data points measured in 2 seconds are shown to form the shape of an ellipse, with the fitted parametric equation APD1 = cos _ϕ_ and APD2 = cos( _ϕ_ + _δϕ_ ) with 0 _< ϕ ≤_ 2 _π_ and the fitting parameter _δϕ_ . The location of each data point on the ellipse corresponds to the interferometer phase at the time of each measurement. **c,d** Extracted interferometer phase, _ϕ_ , (c) varies in the timescale of milliseconds and phase difference, _δϕ_ , between the two polarization components (d) varies by less than a degree over 20 minutes. 

xxiv 







<!-- Start of picture text -->
ARI<br><!-- End of picture text -->





<!-- Start of picture text -->
a b<br>104 20 ZZ early XX/YY ZZ late<br>103 15<br>102 10<br>1 5<br>10<br>0 0<br>10<br>−200 −100 0 100 200 5 10 15 80 85 90 155 160 165<br>Time ( μ s) Time ( μ s) Time ( μ s) Time ( μ s)<br>Count rate (Hz) Count rate (Hz)<br><!-- End of picture text -->

**Extended Data Fig. 10** : **Dark counts and laser scattering. a** Time-trace of background counts for spin-photon entanglement experiment with laser detuned by 100 MHz from the ion transition. The blue trace corresponds to the XX/YY basis experiment, where phase-tracking laser pulses are sent through the MZI, while the orange trace corresponds to the ZZ basis experiment without phase-tracking pulses. The phase-tracking laser pulses are delayed by 7.3 _µ_ s with respect to ion excitation pulses and lead to double scattering events in 15.6 km long fiber, visible as a significant increase of count rate reaching 10<sup>3</sup> _−_ 10<sup>4</sup> Hz. The dashed line corresponds to the total SNSPDs dark count level. **b** Zoom-in around the photon collection window showing average background counts on the level of 6 and 15 Hz for the XX/YY and ZZ basis experiments, respectively. 

xxvi 

