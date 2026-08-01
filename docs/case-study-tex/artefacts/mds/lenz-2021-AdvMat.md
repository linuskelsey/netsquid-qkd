**ReseaRch aRticle** 

**www.advmat.de** 

# **Room-Temperature Quantum Memories Based on Molecular Electron Spin Ensembles** 

_Samuel Lenz, Dennis König, David Hunger, and Joris van Slageren*_ 

suitable.<sup>[5]</sup> Superconducting quantum bits are addressed by means of microwave radiation and quantum memories in this context thus need to be able to store microwave photon states. To this end, resonant structures for electromagnetic radiation can be used to strongly couple quantum bits and quantum memories to quantized cavity modes of the electromagnetic field. The strong coupling generates a hybrid quantum system that allows mapping the qubit state onto the cavity field state.<sup>[6]</sup> This strategy has given rise to the field of cavity quantum electrodynamics and has already been used to couple two superconducting qubits together via a cavity bus.<sup>[7]</sup> A second application of quantum memories is in quantum repeaters for quantum communication. Because telecom wavelengths are in the near-infrared, for this application, optical quantum memories are required that store optical photon states.<sup>[8]</sup> 

**Whilst quantum computing has recently taken great leaps ahead, the development of quantum memories has decidedly lagged behind. Quantum memories are essential devices in the quantum technology palette and are needed for intermediate storage of quantum bit states and as quantum repeaters in long-distance quantum communication. Current quantum memories operate at cryogenic, mostly sub-Kelvin temperatures and require extensive and costly peripheral hardware. It is demonstrated that ensembles of weakly coupled molecular spins show long coherence times and can be used to store microwave pulses of arbitrary phase. These studies exploit strong coupling of the spin ensemble to special 3D microwave resonators. Most importantly, these systems operate at room temperature.** 

## **1. Introduction** 

Quantum technologies rely on the ability to perform coherent manipulations of systems that possess two or more levels. Such systems are called quantum bits, or qubits for short. Many platforms for the implementation of quantum bits have been proposed.<sup>[1]</sup> For practical quantum operations, it appears that qubits based on superconducting circuits are ahead of the pack because of their speed of operation and (limited) scalability.<sup>[2]</sup> However, superconducting circuits must be cooled down to millikelvin temperatures because their coherence times are short (typically several microseconds).<sup>[3]</sup> Because in a functional quantum device, operations will be carried out on many qubits that must be synchronized, there is a need for units to store quantum information for longer times. Such units are called quantum memories.<sup>[4]</sup> Furthermore, a means must be devised to transfer quantum information between quantum memory and quantum bit. For transfer of quantum information between quantum processors and memories, photons are most 

Considering the choice of material platform for designing microwave quantum memories, electron spins in solids can be easily addressed by microwave pulses and have been shown to possess excellent coherence times up to seconds, for some systems even up to room temperature.<sup>[9–10]</sup> Unfortunately, the coupling of a single electron spin to a photon is very weak. Although resonant structures can be tailored to improve single-spin coupling,<sup>[11–13]</sup> the weakness of the coupling renders addressing individual spins by means of coupling to cavity modes very challenging. This can be overcome by using an electron spin ensemble rather than single spins, because the coupling strength of a spin ensemble to an electromagnetic resonator mode is proportional to the square root of the number of electron spins in the ensemble.<sup>[14]</sup> 

This then leads to the general idea of the implementation of a microwave quantum memory using spin ensembles and microwave resonators ( **Figure 1** ). The state to be stored is encoded in a weak microwave pulse and sent to the hybrid quantum system constituted of an electron spin ensemble that is strongly coupled to a microwave resonator, where it is stored. When the quantum state is needed again, a strong microwave pulse is sent to the resonator, which leads to deterministic retrieval of the quantum state that is emitted as a microwave photon to be used as desired. 

S. Lenz, D. König, D. Hunger, Prof. J. van Slageren Institute of Physical Chemistry and Center for Integrated Quantum Science and Technology 

University of Stuttgart Pfaffenwaldring 55, D-70569 Stuttgart, Germany E-mail: slageren@ipc.uni-stuttgart.de 

The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/adma.202101673. 

© 2021 The Authors. Advanced Materials published by Wiley-VCH GmbH. This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited. 

Strong coupling between cavity and electron spin ensembles has been observed in a variety of spin systems, including organic radicals,<sup>[15–20]</sup> phosphorous dopants in silicon,<sup>[21,22]</sup> P1 and nitrogen vacancy (NV) defects in diamond,<sup>[23–32]</sup> N@ C60,<sup>[33]</sup> rare earth dopants in oxides,<sup>[34,35]</sup> transition metal 

### **DOI: 10.1002/adma.202101673** 

**2101673 (1 of 11)** 

_Adv. Mater._ **2021** , _33_ , 2101673 

© 2021 The Authors. Advanced Materials published by Wiley-VCH GmbH 

ADVANCED 

ADVANCED 

SCIENCENEWS~~~ MATERIALS 



<!-- Start of picture text -->
Storage Retrieval<br>Roy Quantum sl. Quantum<br>Information 2 = Information<br>ClaraFaLD Tg 7tAAZ — E : I<br>pA AA I ey [<br>Spin ol AAAZ x x<br>Ensemble Resonator- Storage<br>Spin Ensemble Time<br><!-- End of picture text -->

NE - 

<u>Na</u> 

**www.advancedsciencenews.com** 

**www.advmat.de** 

spin–photon coupling strength (vacuum Rabi oscillations). This oscillation is damped by rates given by the loss of energy from the cavity (cavity dissipation) and decoherence of the spin. Both are usually many orders of magnitude larger than _g_ s. 

This changes if an ensemble of spins is considered. For each spin in the ensemble that is excited, an equal amount of energy is added to the system, suggesting a harmonic-oscillatorlike energy spectrum, which allows the description of the spin system by bosonic operators (the so-called Holstein–Primakoff transformation).<sup>[50]</sup> If we consider that the excitation energy is shared by all the spins, the excitation becomes spin-wave-like in nature, with the magnon as the corresponding quasi-particle. The spin system is then considered a giant spin, for which the total spin is _S_ T = _N_ /2 (assuming _T_ << _ħω_ s). If the number of photons and magnons is small compared to the number of spins, the hybrid spin-cavity system can be described as two interacting harmonic oscillators: 







The crucially important result of this description is that the effective collective coupling spin–photon strength is given by Ωeff = _N g_ s, that is, the coupling is increased by a factor _N_ . This means that by using large enough numbers of spins the cavity-spin coupling can be made larger than the spin and cavity dissipation frequencies. Here, it has been assumed that all spins have the same excitation frequency, which, in real life, is not the case. We will consider the effects of such inhomogeneous broadening below, when we discuss the probing of hybrid spin-cavity systems. 

The steady-state response of the hybrid system can be studied by sending weak microwave radiation to the cavity and recording the radiation returning, as a function of microwave frequency _ω_ p and external magnetic field _B_ 0, for example by employing a network analyzer. To take into account the inhomogeneous broadening of the ensemble, we divide the spin ensemble into sub-ensembles (spin packets) that are each assumed to have the same excitation frequency. The scattering parameter _S_ 11, that is, the ratio between input and output fields, is then given by: 



Here _κ_ e is the external dissipation rate, that is, the losses due to the coupling of the resonator to an external microwave circuit (e.g., source, detector,…), _κ_ i is the internal dissipation rate (the losses inside the cavity, essentially due to the finite resistance of the cavity wall) and _γ_ the spin dissipation rate (spin–spin and spin–lattice relaxation). N is the number of spin packets and 

_Nj_ is the number of spins in each spin packet. The expression contains the _Ŝ_ z expectation value to take into account the effects of finite temperature and interactions within the sample.<sup>[20]</sup> In this case the collective spin–photon coupling strength is given by ˆ Ωeff = −2 _N j S_ z _g_ s. In the _S_ 11( _B_ 0, _ω_ p) diagram, this leads to an anticrossing of the absorption lines describing cavity and spin excitations in the field–frequency diagram. The observation of such an anticrossing, where the splitting is larger than the line widths of cavity and spin resonance lines, is considered a signature of strong coupling between cavity and spin ensemble. In terms of rates, this means that the coupling rate Ωeff must be much higher than the cavity loss rate _κ_ and the spin decoherence rate _γ_ . The cooperativity parameter _C_ , defined as _C_ = Ω2eff /(κγ ), with _C_ >> 1, summarizes this requirement. The time-dependent response can be calculated by numerically solving a closed set of differential equations describing the rates of change of the photon number and spin excitations.<sup>[51]</sup> To this end, a driving term describing the effect of microwave irradiation must be added to the Tavis–Cummings Hamiltonian (which is the Jaynes–Cummings Hamiltonian, Equation (1), for many spins). Using a coordinate frame that rotates with the precession frequency of the spins at the center of their distribution, this Hamiltonian reads: 



Here Δcs = _ω_ c – _ω_ s,c is the detuning between the cavity resonance and the spin resonance at the center of the inhomogeneous distribution, and Δs,i = _ω_ s,i – _ω_ s,c is the difference between spin resonance frequencies of spin _i_ and that at the center of the distribution. The probing field is denoted _B_ ’ because in the rotating coordinate frame, it corresponds to the down-converted (in signal processing terms) field, i.e., _B_ ’ = _B_ exp(– _iω_ s,c _t_ ). The resulting differential equations that can be solved numerically are given in refs. [51,52] and not repeated here. 

## **3. Results and Discussion** 

### **3.1. Investigation of the Steady-State Properties by Continuous Wave Measurements** 

First we investigated the steady-state response of the hybrid quantum system consisting of a 9.4 mg (≈6 × 10<sup>18</sup> spins) pressed powder sample of the stable free radical _α_ , _γ_ -bisdiphenylene- _β_ -phenylallyl benzene solvate (, abbreviated BDPA hereafter) mounted on the bottom, flat mirror of a semi-confocal copper Fabry–Pérot resonator (FPR).<sup>[47]</sup> To this end, we recorded the radiation reflected from the cavity ( _S_ 11 scattering parameter) as a function of external magnetic field _B_ 0 and microwave frequency by means of a vector network analyzer at a temperature of _T_ =  7 K ( **Figure 2** A). The first resonance mode (i.e., that with smallest inter-mirror separation) of the cavity was tuned to 35.000 GHz prior to the measurement. The measurement 

**2101673 (3 of 11)** 

© 2021 The Authors. Advanced Materials published by Wiley-VCH GmbH 

_Adv. Mater._ **2021** , _33_ , 2101673 

ADVANCED 

ADVANCED 

SCIENCENEWS= MATERIALS 



<!-- Start of picture text -->
A 354 8 i<br>0) 35.2 - — a<br>Fey 35.0 5<br>= - —<br>$ us I —— *<br>oO — _—<br>o §-25<br>LL 346<br>a<br>1240 1244 1248 1252 1240 1244 1248 1252<br>Magnetic field (mT) Magnetic field (mT)<br>Cc D 120<br>000|<br>|<br>7) -4 2 ’<br>8 Bs<br>2 | 3 | a<br>= H 4<br>«w -12 i BPTI<br>- * i . : Fy<br>-16 i . al<br>-8<br>-20 6 0<br>345 350 355 345 350 355 345 350 355 0 50 100 150 200 250 300<br>Frequency (GHz) Temp. (K)<br><!-- End of picture text -->

0) 

oO) 

SADVANGED,a ADVANCEDMATERIALS 



<!-- Start of picture text -->
<<br>A i n BVM<br>0.1 0.2 0.3 0.4 05 01 0.2 0.3 0.4 0.5<br>Time (ps) Time (us)<br><!-- End of picture text -->

ADVANCED ADVANCED SCIENCENEWS= MATERIALS 



<!-- Start of picture text -->
A B _ 9<br>—_—~EzN *’:<br>sFo) = 60 R s 3<br>j= |c Li " ooe .<br>= oO . . 3<br>a = 30 - . .<br><£ 32 .digd BF5:<br>—< {2<br>1.9 2.0 2.1 22 23 34.8 34.9 35.0 35.1 35.2<br>Time (us) Microwave Frequency (GHz)<br>c CORES<br>= © 104 Y<br>pe2 £~ 0 PU * A Y<br>< Ih ag oe [A 8 A<br>£2 [)<br>= = 04<br>E a 02. ¥ Lower Polariton Mode<br>= A Upper Polariton Mode<br>2 90<br>1.6 1.8 2.0 22 24 0 50 100 150 200 250 300<br>Time (us) Temperature (K)<br><!-- End of picture text -->

**www.advancedsciencenews.com** 

**www.advmat.de** 

( _ω_ p _ω_ c = _ω_ s). A Fourier transform of the echo signal reveals that the oscillation has a frequency of 78 MHz, which again corresponds to the effective collective coupling strength. This is corroborated by the fact that the oscillation frequency shows a linear dependence on the microwave frequency (Figure 4B, Figure S6, Supporting Information). At some frequencies, two distinct oscillations are observed, consistent with the excitation of both polariton modes. The echo intensity as a function of the interpulse delay (Figure S7, Supporting Information) decays mono-exponentially with a time constant (phase memory time) of _T_ M =  1.4(1) µs, which corresponds to a decay rate of _γ_ M/2 _π_ = 0.114(8) MHz. Such a decay rate is much smaller than any decay rate (spin, cavity) observed so far. In fact, it is much longer than the phase memory time of BDPA determined to be of the order of 100 ns between 77 K and room temperature.<sup>[62,63]</sup> Spin echoes have been observed (at millikelvin temperatures) under conditions where the single-spin–cavity coupling is large, but in most cases the cooperativity parameter _C_ was small, meaning that the response of individual spins was measured.<sup>[52,64,65]</sup> Therefore, that scenario is not applicable to the present case. We believe our findings to be consistent with the following scenario: i) The initial pulse creates coherence on both polariton modes. Although the polariton frequency is beyond the bandwidth of the pulse, we have seen that the instantaneous bandwidth of the pulse edges is sufficient to excite the polariton modes. The fact that coherence is generated by the pulse edges is corroborated by an experiment where an initial pulse of a much longer duration of 280 ns is employed. Here two echoes are observed after the second pulse, spaced by exactly 280 ns (Figure 4C), proving that both rising and falling edges of the first pulse generate coherences. ii) the generated coherence is transferred via interaction with the cavity to dark modes. These dark modes are weakly coupled to the cavity and thus do not decay efficiently via Purcell-like photon emission. Importantly, however, these dark modes are outside of the spectral density of the spin ensemble. The (exchange-narrowed) width of the spectral density distribution ( _γ_ inh =  11.9 MHz, see above) is much smaller than the frequency difference (given by Ωeff _=_ 80 MHz, see above) between the ensemble center frequency and the polariton frequency. In fact, the echo signal could not be reproduced by using the model outlined in the theory section. This brings us back to the ≈10% impurity observed in the magnetic, as well as in the steady-state microwave measurements. This second spin ensemble is not exchange narrowed and should thus have a much broader spectral distribution, and have substantial spectral density at the frequency of the polariton modes. iii) After being transferred to the impurity spin ensemble, the coherence dephases rapidly due to the inhomogeneity in the spectral distribution. iv) However, this type of dephasing can be refocused by a second microwave pulse, which is the basis of the spin echo measurement. Indeed, the magnetization is refocussed after a delay time equal to the interpulse separation. v) At the point where the magnetization is refocussed, interaction with the cavity radiation field is again possible, which excites the polariton modes and leads to a modulated echo signal. This scenario is somewhat similar to that proposed by Putz et al.<sup>[29,60]</sup> with two main differences: First, in their spin ensemble, the inhomogeneous distribution width exceeds the effective collective spin–cavity 

coupling. Second, in their experiments they inserted up to 10<sup>4</sup> photons per spin into the cavity, whereas in our experiments we have about 10<sup>4</sup> spins per photon. As a result, no significant hole burning is taking place in our experiments. Simulations of the system response, including a second spin ensemble that is associated with the impurity spins lead to a very satisfactory reproduction of the experimental data (Figure 4A,C), which corroborates the validity of our scenario. Finally, we have studied the temperature dependence of the phase memory time. For convenience, that is, avoiding the echo modulation, we directly excited the upper or lower polariton modes, and recorded the interpulse time dependence of the echo decay as a function of temperature (Figure S8, Supporting Information). Monoexponential fits of these data (Figure 4D) reveal that the phase memory time of the strongly coupled ensemble only changes slowly with temperature and still amounts to 600 ns, even at room temperature. 

Because coherence on the polariton modes is only generated by the pulse edges, that is, a small fraction of the actual pulse, these measurements can also be seen as the storage of weak microwave excitations into an inhomogeneously broadened system. In fact, the concept of storing information in an inhomogeneously broadened spin system dates back to 1955.<sup>[66,67]</sup> In this scheme, a number of electromagnetic pulses generate coherences in the ensemble. These pulses must be weak so that subsequent pulses do not change the stored information. This information quickly dephases due to the inhomogeneous distribution of Larmor frequencies, but can be recalled by a strong pulse in a second step. With the advent of cavity QED, the idea has resurfaced in recent years, where the aim is to eventually store single photons.<sup>[32,33,46,51]</sup> In the following, we explore the possibility to store microwave pulses in inhomogeneously broadened spin ensembles in more detail. To this end, we employed a hybrid system of a 5.5 mg BDPA pellet mounted in a copper FPR tuned to _ω_ c/2 _π_ =  35.000 GHz ( _T_ =  7 K, Ωeff/2 _π_ = 62 MHz), with an applied field strength such that that _ω_ s = _ω_ c. First, three weak (5 mW) 30 ns microwave pulses, spaced by 290 ns were applied. Their frequency was set to coincide with the upper polariton mode (35.062 GHz). The phase of the second pulse was inverted compared to that of the other two. These pulses are too weak to create measurable spin echos by themselves. After a waiting time of _τ_ =  1.4 µs, a strong (5 W) pulse of 22.5 ns duration was employed. As a result, at a time of 2 _τ_ =  2.8 µs, a series of echoes was observed ( **Figure 5** A, Figure S9, Supporting Information), that correspond to the stored pulses in reverse order. In contrast to the previously discussed results, these echoes are not modulated, because the polariton mode (i.e., the eigenstate) is excited directly. Importantly, the phases of these retrieved echoes are the same as of the pulses that were stored. These results demonstrate that information in the form of microwave pulses can be successfully stored in the ensemble-resonator system. We note furthermore, that the phase information is faithfully reproduced by the simulation. It can be seen that the echo amplitude decreases monotonously, which is due to decoherence, the characteristic time of which is the same as found above ( _γ_ M/2 _π_ =  0.114 MHz). Unfortunately, we could not explore the maximum number of pulses that can be stored any further, because with four pulses, the duty cycle of our 

**2101673 (7 of 11)** 

© 2021 The Authors. Advanced Materials published by Wiley-VCH GmbH 

_Adv. Mater._ **2021** , _33_ , 2101673 

ADVANCED ADVANCED SCIENCENEWS_ MATERIALS 



<!-- Start of picture text -->
AB<br>3<br><£. a=ry2|i<br><J i<br>3.0 36 4.0 4.5 5.0 26 28 30 32 34 36 38 40<br>Time (us) Time (us)<br><!-- End of picture text -->

**www.advancedsciencenews.com** 

**www.advmat.de** 

have considered two examples, namely one based on the solid state material Pr<sup>3+</sup> :Y2SiO5 and one based on cesium atomic gas. Retrieval efficiencies are orders of magnitude higher in these systems. On the other hand, their storage times and storage bandwidths are not too dissimilar to the BDPA/FPR system we present here, especially when considering that in the latter pulse lengths can easily be shortened by an order of magnitude. Furthermore, we note that we have carried out measurements on different BDPA samples and with different FPRs and have always obtained comparable results, underlining the robustness of the platform. One of the next steps would be now to assess the retrieval fidelity that is the overlap between the stored and retrieved photon (superposition) state. 

## **4. Conclusion** 

We have shown that very high cooperativities can be obtained when using molecular spin ensembles and 3D microwave resonators. This is because the microwave mode volume is larger than in 2D-resonators allowing for using larger numbers of spins. We directly observed vacuum Rabi oscillations in timedomain investigations. Here the high degree of microwave magnetic field homogeneity of 3D resonators compared to 2D resonators was of benefit, and no distribution of Rabi frequencies needed to be taken into account. Furthermore, we found unexpectedly long coherence times when using conventional Hahn echo pulse sequences. Finally, we demonstrated the feasibility of storing microwave pulses, including phase information into the spin-ensembles, which is a prerequisite for using such hybrid systems as quantum memories. Time-domain experiments have been reported previously, but only at (sub)Kelvin temperatures. Here we have shown the possibility of performing such measurements up to room temperature, greatly increasing the potential of magnetically dense organic radicals in hybrid cavity–spin-ensemble quantum systems for application as robust quantum memories. 

## **5. Experimental Section** 

The benzene complex of _α_ , _γ_ -bisdiphenylene- _β_ -phenylallyl (≡ BDPA·Bz) was acquired commercially. Magnetic measurements were carried out on a Quantum Design MPMS3 SQUID magnetometer. The data were corrected for diamagnetic contributions using Pascal’s constants. All strong coupling experiments were carried out employing a home-built Fabry–Pérot resonator (FPR) made of copper,<sup>[47]</sup> inserted into an Oxford Instruments CF935 continuous flow helium cryostat. Samples were pressed into 5 mm pellets. Magnetic fields were applied with a Varian V-3800 electromagnet, equipped with an Elektro-Automatik EA-PS 9200-140 power supply. For all CW measurements an Anritsu MS46322B vector network analyzer was used, which was connected to the resonator via a WR28-2.92mm waveguide-coax transition. The VNA was calibrated up to the coax connection for a measurement range of 34.5–35.5 GHz using a SOLT calibration kit. The probe power was set to −20 dBm. At this probe power ≈10<sup>9</sup> photons are inserted into the cavity, that is, far fewer than the number of spins, and probing does not influence the spin state population. Pulsed measurements were performed using a home-built pulsed _Q_ -band (35 GHz) spectrometer, which is based on a homodyne bridge, in which the reflected microwave signal is mixed in a balance mixer with the reference arm signal and amplified by a video amplifier.<sup>[73]</sup> Microwave simulations were carried using CST Microwave 

Studio. The continuous wavelet transforms were calculated using Matlab’s Wavelet toolbox. 

## **Supporting Information** 

Supporting Information is available from the Wiley Online Library or from the author. 

## **Acknowledgements** 

The authors thank the Zeiss Foundation and the Vector Foundation for funding. 

Open access funding enabled and organized by Projekt DEAL. 

## **Conflict of Interest** 

The authors declare no conflict of interest. 

## **Data Availability Statement** 

The data that support the findings of this study are available from the corresponding author upon reasonable request. 

## **Keywords** 

microwave pulse storage, molecular quantum bits, organic radicals, quantum memories, quantum technologies 

Received: March 1, 2021 Revised: May 6, 2021 Published online: June 9, 2021 

- [1] R. J. Schoelkopf, S. M. Girvin, _Nature_ **2008** , _451_ , 664. 

- [2] H.-L. Huang, D. Wu, D. Fan, X. Zhu, _Sci. China Technol. Sci._ **2020** , _63_ , 180501. 

- [3] A. A. Houck, J. Koch, M. H. Devoret, S. M. Girvin, R. J. Schoelkopf, _Quantum Inf. Process._ **2009** , _8_ , 105. 

- [4] C. Simon, M. Afzelius, J. Appel, A. Boyer de la Giroday, S. J. Dewhurst, N. Gisin, C. Y. Hu, F. Jelezko, S. Kröll, J. H. Müller, J. Nunn, E. S. Polzik, J. G. Rarity, H. De Riedmatten, W. Rosenfeld, A. J. Shields, N. Sköld, R. M. Stevenson, R. Thew, I. A. Walmsley, M. C. Weber, H. Weinfurter, J. Wrachtrup, R. J. Young, _Eur. Phys. J. D_ **2010** , _58_ , 1. 

- [5] J. Yin, Y.-H. Li, S.-K. Liao, M. Yang, Y. Cao, L. Zhang, J.-G. Ren, W.-Q. Cai, W.-Y. Liu, S.-L. Li, R. Shu, Y.-M. Huang, L. Deng, L. Li, Q. Zhang, N.-L. Liu, Y.-A. Chen, C.-Y. Lu, X.-B. Wang, F. Xu, J.-Y. Wang, C.-Z. Peng, A. K. Ekert, J.-W. Pan, _Nature_ **2020** , _582_ , 501. 

- [6] Z.-L. Xiang, S. Ashhab, J. Q. You, F. Nori, _Rev. Mod. Phys._ **2013** , _85_ , 623. 

- [7] J. Majer, J. M. Chow, J. M. Gambetta, J. Koch, B. R. Johnson, J. A. Schreier, L. Frunzio, D. I. Schuster, A. A. Houck, A. Wallraff, A. Blais, M. H. Devoret, S. M. Girvin, R. J. Schoelkopf, _Nature_ **2007** , _449_ , 443. 

- [8] A. I. Lvovsky, B. C. Sanders, W. Tittel, _Nat. Photonics_ **2009** , _3_ , 706. 

- [9] A. M. Tyryshkin, S. Tojo, J. J. L. Morton, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, T. Schenkel, M. L. W. Thewalt, K. M. Itoh, S. A. Lyon, _Nat. Mater._ **2012** , _11_ , 143. 

**2101673 (9 of 11)** 

© 2021 The Authors. Advanced Materials published by Wiley-VCH GmbH 

_Adv. Mater._ **2021** , _33_ , 2101673 

**www.advancedsciencenews.com** 

**www.advmat.de** 

- [10] G. Balasubramanian, P. Neumann, D. Twitchen, M. Markham, R. Kolesov, N. Mizuochi, J. Isoya, J. Achard, J. Beck, J. Tissler, V. Jacques, P. R. Hemmer, F. Jelezko, J. Wrachtrup, _Nat. Mater._ **2009** , _8_ , 383. 

- [11] C. Eichler, A. J. Sigillito, S. A. Lyon, J. R. Petta, _Phys. Rev. Lett._ **2017** , _118_ , 037701. 

- [12] M. D. Jenkins, U. Naether, M. Ciria, J. Sesé, J. Atkinson, C. SánchezAzqueta, E. d. Barco, J. Majer, D. Zueco, F. Luis, _Appl. Phys. Lett._ **2014** , _105_ , 162601. 

- [13] I. Gimeno, W. Kersten, M. C. Pallarés, P. Hermosilla, M. J. MartínezPérez, M. D. Jenkins, A. Angerer, C. Sánchez-Azqueta, D. Zueco, J. Majer, A. Lostao, F. Luis, _ACS Nano_ **2020** , _14_ , 8707. 

- [14] M. Tavis, F. W. Cummings, _Phys. Rev._ **1968** , _170_ , 379. 

- [15] E. Abe, H. Wu, A. Ardavan, J. J. L. Morton, _Appl. Phys. Lett._ **2011** , _98_ , 251108. 

- [16] M. Mergenthaler, J. Liu, J. J. Le Roy, N. Ares, A. L. Thompson, L. Bogani, F. Luis, S. J. Blundell, T. Lancaster, A. Ardavan, G. A. D. Briggs, P. J. Leek, E. A. Laird, _Phys. Rev. Lett._ **2017** , _119_ , 147701. 

- [17] A. Ghirri, C. Bonizzoni, F. Troiani, N. Buccheri, L. Beverina, A. Cassinese, M. Affronte, _Phys. Rev. A_ **2016** , _93_ , 063855. 

- [18] G. Boero, G. Gualco, R. Lisowski, J. Anders, D. Suter, J. Brugger, _J. Magn. Reson._ **2013** , _231_ , 133. 

- [19] I. Chiorescu, N. Groll, S. Bertaina, T. Mori, S. Miyashita, _Phys. Rev. B_ **2010** , _82_ , 024413. 

- [20] S. Lenz, D. Hunger, J. van Slageren, _Chem. Commun._ **2020** , _56_ , 12837. 

- [21] C. W. Zollitsch, K. Mueller, D. P. Franke, S. T. B. Goennenwein, M. S. Brandt, R. Gross, H. Huebl, _Appl. Phys. Lett._ **2015** , _107_ , 142105. 

- [22] B. C. Rose, A. M. Tyryshkin, H. Riemann, N. V. Abrosimov, P. Becker, H. J. Pohl, M. L. W. Thewalt, K. M. Itoh, S. A. Lyon, _Phys. Rev. X_ **2017** , _7_ , 031002. 

- [23] Y. Kubo, F. R. Ong, P. Bertet, D. Vion, V. Jacques, D. Zheng, A. Dreau, J. F. Roch, A. Auffeves, F. Jelezko, J. Wrachtrup, M. F. Barthe, P. Bergonzo, D. Esteve, _Phys. Rev. Lett._ **2010** , _105_ , 140502. 

- [24] J.-M. Le Floch, N. Delhote, M. Aubourg, V. Madrangeas, D. Cros, S. Castelletto, M. E. Tobar, _J. Appl. Phys._ **2016** , _119_ , 153901. 

- [25] A. Angerer, T. Astner, D. Wirtitsch, H. Sumiya, S. Onoda, J. Isoya, S. Putz, J. Majer, _Appl. Phys. Lett._ **2016** , _109_ , 033508. 

- [26] D. O. Krimer, M. Liertzer, S. Rotter, H. E. Türeci, _Phys. Rev. A_ **2014** , _89_ , 033820. 

- [27] R. Amsüss, C. Koller, T. Nöbauer, S. Putz, S. Rotter, K. Sandner, S. Schneider, M. Schramböck, G. Steinhauser, H. Ritsch, J. Schmiedmayer, J. Majer, _Phys. Rev. Lett._ **2011** , _107_ , 060502. 

- [28] D. I. Schuster, A. P. Sears, E. Ginossar, L. DiCarlo, L. Frunzio, J. J. L. Morton, H. Wu, G. A. D. Briggs, B. B. Buckley, D. D. Awschalom, R. J. Schoelkopf, _Phys. Rev. Lett._ **2010** , _105_ , 140501. 

- [29] S. Putz, A. Angerer, D. O. Krimer, R. Glattauer, W. J. Munro, S. Rotter, J. Schmiedmayer, J. Majer, _Nat. Photon_ **2016** , _11_ , 36. 

- [30] Y. Kubo, I. Diniz, A. Dewes, V. Jacques, A. Dréau, J. F. Roch, A. Auffeves, D. Vion, D. Esteve, P. Bertet, _Phys. Rev. A_ **2012** , _85_ , 012333. 

- [31] V. Ranjan, G. de Lange, R. Schutjens, T. Debelhoir, J. P. Groen, D. Szombati, D. J. Thoen, T. M. Klapwijk, R. Hanson, L. DiCarlo, _Phys. Rev. Lett._ **2013** , _110_ , 067004. 

- [32] C. Grezes, B. Julsgaard, Y. Kubo, M. Stern, T. Umeda, J. Isoya, H. Sumiya, H. Abe, S. Onoda, T. Ohshima, V. Jacques, J. Esteve, D. Vion, D. Esteve, K. Mølmer, P. Bertet, _Phys. Rev. X_ **2014** , _4_ , 021049. 

- [33] H. Wu, R. E. George, J. H. Wesenberg, K. Mølmer, D. I. Schuster, R. J. Schoelkopf, K. M. Itoh, A. Ardavan, J. J. L. Morton, G. A. D. Briggs, _Phys. Rev. Lett._ **2010** , _105_ , 140503. 

- [34] S. Probst, H. Rotzinger, S. Wünsch, P. Jung, M. Jerger, M. Siegel, A. V. Ustinov, P. A. Bushev, _Phys. Rev. Lett._ **2013** , _110_ , 157001. 

- [35] A. Tkalčec, S. Probst, D. Rieger, H. Rotzinger, S. Wünsch, N. Kukharchyk, A. D. Wieck, M. Siegel, A. V. Ustinov, P. Bushev, _Phys. Rev. B_ **2014** , _90_ , 075112. 

- [36] C. Bonizzoni, A. Ghirri, K. Bader, J. van Slageren, M. Perfetti, L. Sorace, Y. Lan, O. Fuhr, M. Ruben, M. Affronte, _Dalton Trans._ **2016** , _45_ , 16596. 

- [37] C. Bonizzoni, A. Ghirri, M. Atzori, L. Sorace, R. Sessoli, M. Affronte, _Sci. Rep._ **2017** , _7_ , 13096. 

- [38] A. W. Eddins, C. C. Beedle, D. N. Hendrickson, J. R. Friedman, _Phys. Rev. Lett._ **2014** , _112_ , 120501. 

- [39] M. Goryachev, W. G. Farr, D. L. Creedon, Y. Fan, M. Kostylev, M. E. Tobar, _Phys. Rev. Applied_ **2014** , _2_ , 054002. 

- [40] N. Kostylev, M. Goryachev, M. E. Tobar, _Appl. Phys. Lett._ **2016** , _108_ , 062402. 

- [41] H. Maier-Flaig, M. Harder, R. Gross, H. Huebl, S. T. B. Goennenwein, _Phys. Rev. B_ **2016** , _94_ , 054433. 

- [42] S. Putz, D. O. Krimer, R. Amsüss, A. Valookaran, T. Nöbauer, J. Schmiedmayer, S. Rotter, J. Majer, _Nat. Phys._ **2014** , _10_ , 720. 

- [43] T. Astner, J. Gugler, A. Angerer, S. Wald, S. Putz, N. J. Mauser, M. Trupke, H. Sumiya, S. Onoda, J. Isoya, J. Schmiedmayer, P. Mohn, J. Majer, _Nat. Mater._ **2018** , _17_ , 313. 

- [44] K. Debnath, G. Dold, J. J. L. Morton, K. Mølmer, _Phys. Rev. Lett._ **2020** , _125_ , 137702. 

- [45] S. Weichselbaumer, M. Zens, C. W. Zollitsch, M. S. Brandt, S. Rotter, R. Gross, H. Huebl, _Phys. Rev. Lett._ **2020** , _125_ , 137701. 

- [46] C. Bonizzoni, A. Ghirri, F. Santanni, M. Atzori, L. Sorace, R. Sessoli, M. Affronte, _npj Quantum Inf._ **2020** , _6_ , 68. 

- [47] S. Lenz, B. Kern, M. Schneider, J. van Slageren, _Chem. Commun._ **2019** , _55_ , 7163. 

- [48] E. T. Jaynes, F. W. Cummings, _Proc. IEEE_ **1963** , _51_ , 89. 

- [49] G. S. Agarwal, _J. Opt. Soc. Am. B_ **1985** , _2_ , 480. 

- [50] T. Holstein, H. Primakoff, _Phys. Rev._ **1940** , _58_ , 1098. 

- [51] B. Julsgaard, C. Grezes, P. Bertet, K. Mølmer, _Phys. Rev. Lett._ **2013** , _110_ , 250503. 

- [52] V. Ranjan, S. Probst, B. Albanese, A. Doll, O. Jacquot, E. Flurin, R. Heeres, D. Vion, D. Esteve, J. J. L. Morton, P. Bertet, _J. Magn. Reson._ **2020** , _310_ , 106662. 

- [53] A. Nagao, O. Takehiro, Y. Jun, _Bull. Chem. Soc. Jpn._ **1994** , _67_ , 31. 

- [54] R. B. Griffiths, _Phys. Rev._ **1961** , _124_ , 1023. 

- [55] W. Duffy, J. F. Dubach, P. A. Pianetta, J. F. Deck, D. L. Strandburg, A. R. Miedema, _J. Chem. Phys._ **1972** , _56_ , 2555. 

- [56] J. C. Bonner, M. E. Fisher, _Phys. Rev. A_ **1964** , _135_ , A640. 

- [57] W. O. Hamilton, G. E. Pake, _J. Chem. Phys._ **1963** , _39_ , 2694. 

- [58] Z. Kurucz, J. H. Wesenberg, K. Mølmer, _Phys. Rev. A_ **2011** , _83_ , 053852. 

- [59] I. Diniz, S. Portolan, R. Ferreira, J. M. Gérard, P. Bertet, A. Auffèves, _Phys. Rev. A_ **2011** , _84_ , 063810. 

- [60] S. Putz, _Ph.D. Thesis_ , TU Wien, Vienna, Austria **2017** . 

- [61] A. Schweiger, G. Jeschke, _Principles of Pulse Electron Paramagnetic Resonance_ , Oxford University Press, Oxford, UK **2001** . 

- [62] D. G. Mitchell, R. W. Quine, M. Tseitlin, R. T. Weber, V. Meyer, 

   - A. Avery, S. S. Eaton, G. R. Eaton, _J. Phys. Chem. B_ **2011** , _115_ , 7986. 

- [63] J. P. Goldsborough, M. Mandel, G. E. Pake, _Phys. Rev. Lett._ **1960** , _4_ , 13. 

- [64] A. Bienfait, J. J. Pla, Y. Kubo, X. Zhou, M. Stern, C. C. Lo, C. D. Weis, T. Schenkel, D. Vion, D. Esteve, J. J. L. Morton, P. Bertet, _Nature_ **2016** , _531_ , 74. 

- [65] S. Probst, A. Bienfait, P. Campagne-Ibarcq, J. J. Pla, B. Albanese, J. F. D. S. Barbosa, T. Schenkel, D. Vion, D. Esteve, K. Mølmer, J. J. L. Morton, R. Heeres, P. Bertet, _Appl. Phys. Lett._ **2017** , _111_ , 202604. 

- [66] A. G. Anderson, R. L. Garwin, E. L. Hahn, J. W. Horton, G. L. Tucker, R. M. Walker, _J. Appl. Phys._ **1955** , _26_ , 1324. 

**2101673 (10 of 11)** 

_Adv. Mater._ **2021** , _33_ , 2101673 

© 2021 The Authors. Advanced Materials published by Wiley-VCH GmbH 

**www.advancedsciencenews.com** 

**www.advmat.de** 

- [67] S. Fernbach, W. G. Proctor, _J. Appl. Phys._ **1955** , _26_ , 170. 

- [68] C. Grezes, Y. Kubo, B. Julsgaard, T. Umeda, J. Isoya, H. Sumiya, H. Abe, S. Onoda, T. Ohshima, K. Nakamura, I. Diniz, A. Auffeves, V. Jacques, J.-F. Roch, D. Vion, D. Esteve, K. Moelmer, P. Bertet, _C. R. Phys._ **2016** , _17_ , 693. 

- [69] C. Grezes, B. Julsgaard, Y. Kubo, W. L. Ma, M. Stern, A. Bienfait, K. Nakamura, J. Isoya, S. Onoda, T. Ohshima, V. Jacques, D. Vion, D. Esteve, R. B. Liu, K. Mølmer, P. Bertet, _Phys. Rev. A_ **2015** , _92_ , 020301. 

- [70] C. Zhang, H. Yuan, N. Zhang, L. X. Xu, B. Li, G. D. Cheng, Y. Wang, Q. Gui, J. C. Fang, _J. Phys. D Appl. Phys._ **2017** , _50_ , 505104. 

- [71] M. P. Hedges, J. J. Longdell, Y. Li, M. J. Sellars, _Nature_ **2010** , _465_ , 1052. 

- [72] J.-P. Dou, A.-L. Yang, M.-Y. Du, D. Lao, J. Gao, L.-F. Qiao, H. Li, X.-L. Pang, Z. Feng, H. Tang, X.-M. Jin, _Commun. Phys._ **2018** , _1_ , 55. 

- [73] I. Tkach, A. Baldansuren, E. Kalabukhova, S. Lukin, A. Sitnikov, A. Tsvir, M. Ischenko, Y. Rosentzweig, E. Roduner, _Appl. Magn. Reson._ **2008** , _35_ , 95. 

**2101673 (11 of 11)** 

© 2021 The Authors. Advanced Materials published by Wiley-VCH GmbH 

_Adv. Mater._ **2021** , _33_ , 2101673 

