# **Multimode storage of quantum microwave fields in electron spins over** 100 **ms** 

V. Ranjan,<sup>1</sup> J. O’Sullivan,<sup>2</sup> E. Albertinale,<sup>1</sup> B. Albanese,<sup>1</sup> T. Chaneli`ere,<sup>3</sup> 

T. Schenkel,<sup>4</sup> D. Vion,<sup>1</sup> D. Esteve,<sup>1</sup> E. Flurin,<sup>1</sup> J. J. L. Morton,<sup>2</sup> and P. Bertet<sup>1, ∗</sup> 

> 1 _Universit´e Paris-Saclay, CEA, CNRS, SPEC, 91191 Gif-sur-Yvette Cedex, France_ 

> 2 _London Centre for Nanotechnology, University College London, London WC1H 0AH, United Kingdom_ 

> 3 _Univ. Grenoble Alpes, CNRS, Grenoble INP, Institut N´eel, 38000 Grenoble, France_ 

> 4 _Accelerator Technology and Applied Physics Division, Lawrence Berkeley National Laboratory, Berkeley, California 94720, USA_ 

**A long-lived multi-mode qubit register is an enabling technology for modular quantum computing architectures. For interfacing with superconducting qubits, such a quantum memory should be able to store incoming quantum microwave fields at the single-photon level for long periods of time, and retrieve them on-demand. Here, we demonstrate the partial absorption of a train of weak microwave fields in an ensemble of bismuth donor spins in silicon, their storage for 100ms, and their retrieval, using a Hahn-echo-like protocol. The long storage time is obtained by biasing the bismuth donors at a clock transition. Phase coherence and quantum statistics are preserved in the storage.** 

Quantum memory as a matter-based information storage medium for itinerant qubits has been recognised a powerful ingredient in quantum technologies, underpinning applications such as quantum repeaters [1]. In analogy with memories in classical computing, quantum memories offer storage that is both long-term compared to data lifetimes in processing qubits as well as high density, for example when multimode memories are employed to store a large number of states. These attributes can be of general benefit to quantum computing architectures, supporting approaches with a high degree of modularity. Inspired by such possibilities, quantum memories in the optical domain have been developed in particular using rare-earth-ion-doped crystals, reaching high efficiency [2], and storage times in the millisecond range [3]. 

Quantum memories suitable for interfacing with superconducting quantum processors, must instead operate in the _microwave_ regime, which requires operation at millikelvin temperatures in a dilution refrigerator. A microwave multimode quantum memory with long storage times would represent a potent and versatile new component in quantum computing architectures based on superconducting qubits. For example, it could be used to realise sub-processors operating a Quantum Turing Machine architecture with high internal connectivity and built-in long-term memory [see Fig.1 **(A)** ] [4], helping to overcome some of the limitations of present day superconducting qubit processors [5–7]. 

For implementing such a quantum memory, superconducting microwave cavities [8, 9] and mechanical resonators [10, 11] have been considered, with storage times in the millisecond range. Ensembles of electron spins in solids offer a large number of degrees of freedom well decoupled from their environment with coherence times that can reach seconds [12–14], and are thus well suited to implement a manymode quantum memory with long storage time [4, 15]. For modularity, it is natural to physically separate the quantum processor and the quantum memory, and to interface the two devices via propagating microwave photons. Operating a spin-ensemble-based quantum memory thus amounts to absorbing incoming microwave photons and releasing them ondemand in the same quantum state [see Fig. 1( **A** )]. 

A convenient way to interface the spins and the incoming photons [see Fig. 1 **(B)** ] is via a superconducting microresonator of frequency ω0, capacitively coupled to the input line with an energy damping rate κ, and inductively coupled (with single spin coupling strength _g_ 0) to an ensemble of _N_ spins, characterized by its Larmor frequency ω _S_ with inhomogeneous linewidth of Full-Width-Half-Maximum Γ. The resonator serves to enhance microwave absorption and reemission by spins, but also provides a convenient reset mechanism for the memory, via the Purcell relaxation of each individual spin at a rate Γ _P_ = 4 _g_<sup>2</sup> 0<sup>/κ [16, 17].</sup> 

The physics of the memory can be demonstrated using weak resonant coherent pulses with a small average photon number. Such microwave pulses with amplitude envelope βin( _t_ ) are absorbed by the spins with an efficiency governed by the ensemble cooperativity _C_ = _N_ Γ _P_ /Γ. Since the reflected pulse amplitude is βref( _t_ ) = βin( _t_ )(1 − _C_ )/(1 + _C_ ), complete absorption is achieved for _C_ = 1, which appears as a necessary condition for a high-fidelity memory (see [18] and Supplementary Materials). After absorption in the spin ensemble, the microwave fields should be retrieved using sequences of control pulses. The simplest sequence consists in applying a π pulse to the spins after a delay τ, which generates an echo of the absorbed pulse at time 2τ. Because this echo is generated at a time when nearly all spins are in the excited state, it is unavoidably accompanied by _N_ Γ _P_ /Γ = _C_ spontaneously emitted noise photons, thus reducing the memory fidelity [19]. Therefore a more complex protocol must be used, involving two π pulses and dynamic 

> ∗ patrice.bertet@cea.fr 

2 

control of the cavity frequency, in order to form the echo in the spin ground state and thus avoid added noise [18]. 

Reaching unit cooperativity requires large spin concentrations; but spin-spin interactions then reduce the coherence time. This proved to be a serious limitation in previous experiments storing microwaves in spin ensembles, first in the classical regime [20], then in the quantum regime [21– 23], where the longest storage times demonstrated reached only of order 100 µs. This conflict can be mitigated by biasing the spins at specific magnetic fields where their effective magnetic moment vanishes (thus minimizing decoherence induced by spin-spin interactions), while keeping a finite transverse susceptibility so that _g_ 0 remains non-zero, opening the possibility to reach _C_ = 1 without compromising the coherence time. Such “clock transition” (CT) or “ZEroFirst-Order-Zeeman” (ZEFOZ) points occur in spin systems where the electron spin is strongly hybridized with a nuclear spin by the hyperfine interaction, as in bismuth donors in silicon [24, 25] and rare-earth-ion-doped crystals [26, 27]. 

Here, we use an ensemble of bismuth donors in silicon biased at a clock transition to demonstrate the longterm storage of microwave fields. The device schematic is shown in Fig. 1 **(C)** . Bismuth atoms were implanted around a ∼ 100 nm depth in a silicon substrate that was enriched with the nuclear-spin-free<sup>28</sup> Si isotope for longer coherence time. At low temperature, bismuth atoms trap a conduction electron, forming the donor systems. The spin Hamiltonian _H_ Bi/ℏ = (γe **S** + γn **I** ) · **B0** + _A_ **S** · **I** is the sum of the Zeeman interaction of the electron (nuclear) spin _S_ = 1/2 ( _I_ = 9/2) of the bismuth donor with the applied magnetic field _B_ 0 (γe/2π ≃ 28 MHz/mT and γn/2π ≃ 7 kHz/mT being the electronic and nuclear gyromagnetic ratios) and of their hyperfine interaction with a strength _A_ /2π = 1.475 GHz. The resulting energy levels | _F_ , _m_ ⟩ can be grouped in a low-energy ( _F_ = 4) manifold of 9 states and a high-energy ( _F_ = 5) manifold of 11 states [see Fig. 2 **(A)** ], separated by ∼ 7.38 GHz, _m_ being the eigenvalue of the total angular momentum _S z_ + _Iz_ along the field direction _z_ [24]. The operator _S x_ has nonzero matrix elements between all pairs of states that verify ∆ _m_ = ±1, and transitions between such states are therefore allowed under a transverse driving microwave field _B_ 1 along the _x_ direction. We note that transitions |4, _m_ ⟩↔|5, _m_ − 1⟩ and |4, _m_ − 1⟩↔|5, _m_ ⟩ are quasi-degenerate. In this work we are interested in the |4, 0⟩↔|5, −1⟩ and |4, −1⟩↔|5, 0⟩ transitions, which satisfy the CT condition at ∼ 7.338 GHz and _B_ 0 = 27 mT where _d_ ω/ _dB_ 0 = 0 while the transition matrix elements ⟨4, 0| _S x_ |5, −1⟩ = ⟨4, −1| _S x_ |5, 0⟩ = 0.25 remain non-zero. To describe the interaction with microwave fields close to resonance, we model the pair of transitions as independent spin-1/2 systems labelled generically as |0⟩ (|1⟩) for the ground (excited) state. 

The resonator is designed such that its resonance ω0 is close to the CT frequency of 7.338 GHz. A finer tuning of ω0 is obtained by changing the resonator coupling to the 



<!-- Start of picture text -->
A<br>… |ψ3〉 |ψ2〉 |ψ1〉<br>|ψ3〉   |ψ2〉   |ψ1〉…<br>Quantum  Quantum<br>processor control memory<br> pulse<br>B 3  2  1<br>IN<br>κc<br>3  2  1<br>OUT<br>data pulses C L g 0 B 0<br> spins<br>C z<br>x x10 16<br>B 0 y 28Si 8<br>e -<br>209Bi<br>0<br>0 200<br>y  (nm)<br>100 µm<br>5 µm<br>-3)<br> (cm<br>ρ<br><!-- End of picture text -->

FIG. 1. **Quantum memory. (A)** The proposed architecture consisting of a quantum processor coupled via a coaxial cable to a quantum memory from electron spins. **(B)** Circuit implementation of the quantum memory: an ensemble of _N_ electron spins are inductively coupled to a lumped resonator which is capacitively coupled to a microwave line. Weak coherent data pulses in our demonstration, travel along the lines, are stored by the spin ensemble, and then released on-demand by a control pulse. The coupling strength of an individual spin to the resonator is _g_ 0. **(C)** The hybrid resonatorspin system. The resonator is fabricated on top of the silicon substrate in a superconducting aluminum thin film to minimize internal losses. It consists of a capacitor shunted by a 5 µm-wide inductance wire, to which the spin of bismuth donors implanted around a depth ∼ 100 nm are inductively coupled. A magnetic field _B_ 0 is applied along the inductor ( _z_ direction). 

measurement line, which is controlled by the length of a microwave antenna inserted in the sample holder containing the silicon chip (see Supplementary Materials). Figure 2 **(B)** shows ω0 as a function of _B_ 0. Due to the kinetic inductance contribution to the resonator inductance, ω0/2π decreases with _B_ 0, reaching 7.336 GHz at 27 mT. The external energy coupling rate of the resonator is κ _c_ = 4 × 10<sup>5</sup> s<sup>−1</sup> , though its total damping rate, κ = κ _c_ + κ _i_ , including internal losses is power dependent (see Supplementary Materials). We find that at low input powers corresponding to one intracavity photon on average, κ _c_ /κ ∼ 0.3, whereas at high power κ _c_ /κ ∼ 0.5, revealing that part of the losses are caused by Two-Level-Systems (TLS). The experiments are performed at _T_ = 20 mK, in the quantum regime for microwave fields ℏω0 ≫ _k_ B _T_ . 

Spin spectroscopy is performed with a custom-built spectrometer described in more details in Ref. 28, using the 



<!-- Start of picture text -->
J<br>--av I a<br><!-- End of picture text -->

I 

4 



<!-- Start of picture text -->
A 1  spins  B<br>0<br>polarized<br> spins  9 data 9 simulation<br>saturated<br>spins polarized<br>8<br>11 spins saturated 11<br>0<br>0 40 80 120 0 100 200 300 0 100 200 300<br>time (µs) time (µs) time (µs)<br>C<br>20<br>input field ( n in = 240) retrieved field x ζ −1<br>...4 3 2 2 3 4...<br>0<br>1<br>-20<br>8<br>input field ( n in = 24) retrieved field x ζ −1<br>...4 3 2 2 3 4...<br>0<br>1 1<br>-8<br>0 3 6 9 109 112 115 118<br>time (ms)<br>intra-cav field (a.u.) reflected field (a.u.)<br> (a.u.)<br>Q<br>I,<br>Refocusing<br>Refocusing<br>reflected field quadratures,<br><!-- End of picture text -->

FIG. 3. **Storage and retrieval of weak pulses at clock transition** . **(A)** Measured intra-cavity field α averaged over 10<sup>3</sup> repetitions at a repetition rate of 200 ms (spins saturated, dashed curve) and of 16 s (spins polarized, solid curve). **(B)** Measured (left panel, 4 × 10<sup>3</sup> averages) and simulated (right panel) reflected field on resonance (<sup>√</sup> <u>κ</u> _c_ <u>α −</u> βin) and echo at a time ≪ _T_ 2<sup>E.The simulation assumes a spectral</sup> density of _N_ /(Γ/2π) = 10<sup>6</sup> spins/MHz and a fixed _g_ 0/2π = 40 Hz. For panels (A, B) there are 240 photons in the input pulse. **(C)** Top (bottom): a train of weak microwave fields, with input field βin measured off resonantly to allow comparison, containing 240 (24) photons at the input and their retrieval after the refocusing π pulse. The numbering highlights that retrieval maintains the phase relation with respect to the input field. The retrieved fields are multiplied by ζ<sup>−1</sup> ≈ 24, where ζ = 4 _C_ (κ _C_ /κ) is the theoretical efficiency of the retrieved field at a time ≪ _T_ 2<sup>_E_.</sup> 

these analytical predictions as well as with a complete simulation of the experiment. 

We then demonstrate long-lived and multi-mode firstin/last-out microwave storage by sending a train of 20 weak Gaussian pulses with varying phases, and retrieving them using a single refocusing pulse. The experiment was performed twice, comparing input pulse intensities of _n_ in = 240±24 and 24 ± 2 photons. As seen in Fig. 3 **(C)** , echoes are retrieved after 100 ms with a well-defined phase. The retrieved field amplitude is slightly reduced from the expected value of ζβin, mostly due to spin decoherence during the storage time, and also for a small part to resonator phase noise caused by vortices trapped in the resonator thin film (see Supplementary Materials). The recovered intensity corresponds to respectively 0.3 ± 0.1 and 0.03 ± 0.01 photons per echo, ∼ 10<sup>−3</sup> of the input pulse energy. 

Finally, we address the question of the quantum statistics of the echo field. For that, we record a histogram of integrated output signals acquired during the echo _E_ , and outside the echo _O_ at a time when all spins are in their ground state. Thanks to the photon number calibration, the average echo 

amplitude _E_<sup>¯</sup> − _O_<sup>¯</sup> = ζ<sup>~~√~~</sup> _<u>n</u>_ in = 0.5 ± 0.1 provides an absolute calibration of the horizontal scale in dimensionless (square root of photon number) units. This enables a comparison of the measured standard deviations σ _O_ ∼ σ _E_ = 1.5 ± 0.3 to the expected σ _O_ =<sup>√</sup> (¯ _n_ id + 1)/2 and σ _E_ =<sup>√</sup> (¯ _n_ id + _C_ + 1)/2 (see supplementary Materials), where _n_ ¯ id describes JTWPA non-ideality, microwave losses between the sample and the amplifier, and added noise by the higher-temperature amplification chain. We find _n_ ¯ id = 3.5 ± 1.7, a reasonable value compared to those measured in similar circuit QED setups. Then, no measurable difference is observed between σ _E_ and σ _O_ , in agreement with the theoretical estimate which predicts less than 0.5% difference. Overall, these measurements prove the consistency between our photon number calibration protocol and the statistics of the recovered signal, and they show that the echo is recovered with negligible added noise, close to the quantum limit. 

Turning this proof-of-principle into an operational quantum memory requires increasing the ensemble cooperativity by a factor ∼ 30, up to _C_ = 1. We argue that this can be achieved by straightforward design adjustments and without 

5 



<!-- Start of picture text -->
A 12<br>I<br>Q x 4<br>0<br>0 0.5 1 1.5 2<br>time (ms)<br>B<br>280<br>echo I Q<br>before π<br>0<br>-8 0 8 -8 0 8<br>(photons) 1/2 (photons) 1/2<br>Refocusing<br>Reflected field (a.u.)<br>counts<br><!-- End of picture text -->

FIG. 4. **Noise statistics of retrieved echo (A)** Average of 10<sup>3</sup> single shot traces of reflected signals (<sup>~~√~~</sup> <u>κ</u> _c_ <u>α−βin) acquired with a repe-</u> tition rate of 16 s. The input and retrieved field contain 240 photons and 0.25 photons respectively. In this run, the internal losses were slightly larger than in Fig. 3 **(B)** , leading to a lower value of ζ and a lower echo amplitude. **(B)** Histograms of signal quadratures before the refocusing π pulse and on the echo. Each histogram sample is acquired by integrating signals for 100 µs weighted by a normalized gaussian mode shape describing the echo. Solid curves are calculated gaussians of same area. 

- [1] Alexander I. Lvovsky, Barry C. Sanders, and Wolfgang Tittel. Optical quantum memory. <u>Nat Photon,</u> 3(12):706–714, December 2009. 

- [2] Morgan P. Hedges, Jevon J. Longdell, Yongmin Li, and Matthew J. Sellars. Efficient quantum memory for light. <u>Nature,</u> 465(7301):1052–1056, June 2010. Number: 7301 Publisher: Nature Publishing Group. 

- [3] M. Businger, A. Tiranov, K.T. Kaczmarek, S. Welinski, Z. Zhang, A. Ferrier, P. Goldner, and M. Afzelius. Optical Spin-Wave Storage in a Solid-State Hybridized Electron-Nuclear Spin Ensemble. <u>Physical Review Letters,</u> 124(5):053606, February 2020. 

- [4] Karl Tordrup, Antonio Negretti, and Klaus Mlmer. Holographic Quantum Computing. <u>Physical Review Letters,</u> 101(4):040501, July 2008. 

- [5] Chad Rigetti, Jay M. Gambetta, Stefano Poletto, B. L. T. Plourde, Jerry M. Chow, A. D. Corcoles, John A. Smolin, Seth T. Merkel, J. R. Rozen, George A. Keefe, Mary B. Rothwell, Mark B. Ketchen, and M. Steffen. Superconducting qubit in a waveguide cavity with a coherence time approaching 0.1 ms. <u>Physical Review B, 86(10), September 2012.</u> 

- [6] R. Barends, J. Kelly, A. Megrant, D. Sank, E. Jeffrey, Y. Chen, Y. Yin, B. Chiaro, J. Mutus, C. Neill, P. O Malley, P. Roushan, J. Wenner, T. C. White, A. N. Cleland, and John M. Martinis. Coherent Josephson Qubit Suitable for Scalable Quantum Integrated Circuits. <u>Physical Review Letters,</u> 111(8), August 2013. 

- [7] Frank Arute, Kunal Arya, Ryan Babbush, Dave Bacon, 

compromising the spin coherence time, by increasing both the resonator quality factor and the number of implanted spins. Importantly, we propose to increase the number of spins at fixed concentration, simply using a deeper implantation profile, up to 1 µm as already shown [31]. The demonstration of a fully operational microwave quantum memory will then be achieved using the two-pulse protocol proposed in [18], and applied to store quantum states originating from a transmon-based quantum processor. 

In conclusion, we have demonstrated the absorption of trains of weak microwave pulses consisting of only a few photons in a hybrid quantum device, their storage for 100 ms, and their phase-coherent re-emission without added noise. Our results illustrate the utility of clock transitions for efficient quantum memories with long storage times as well as memory reset via the Purcell effect. 

   - Joseph C. Bardin, Rami Barends, Rupak Biswas, Sergio Boixo, Fernando G. S. L. Brandao, David A. Buell, Brian Burkett, Yu Chen, Zijun Chen, Ben Chiaro, Roberto Collins, William Courtney, Andrew Dunsworth, Edward Farhi, Brooks Foxen, Austin Fowler, Craig Gidney, Marissa Giustina, Rob Graff, Keith Guerin, Steve Habegger, Matthew P. Harrigan, Michael J. Hartmann, Alan Ho, Markus Hoffmann, Trent Huang, Travis S. Humble, Sergei V. Isakov, Evan Jeffrey, Zhang Jiang, Dvir Kafri, Kostyantyn Kechedzhi, Julian Kelly, Paul V. Klimov, Sergey Knysh, Alexander Korotkov, Fedor Kostritsa, David Landhuis, Mike Lindmark, Erik Lucero, Dmitry Lyakh, Salvatore Mandr, Jarrod R. McClean, Matthew McEwen, Anthony Megrant, Xiao Mi, Kristel Michielsen, Masoud Mohseni, Josh Mutus, Ofer Naaman, Matthew Neeley, Charles Neill, Murphy Yuezhen Niu, Eric Ostby, Andre Petukhov, John C. Platt, Chris Quintana, Eleanor G. Rieffel, Pedram Roushan, Nicholas C. Rubin, Daniel Sank, Kevin J. Satzinger, Vadim Smelyanskiy, Kevin J. Sung, Matthew D. Trevithick, Amit Vainsencher, Benjamin Villalonga, Theodore White, Z. Jamie Yao, Ping Yeh, Adam Zalcman, Hartmut Neven, and John M. Martinis. Quantum supremacy using a programmable superconducting processor. <u>Nature,</u> 574(7779):505–510, October 2019. 

- [8] Matthew Reagor, Wolfgang Pfaff, Christopher Axline, Reinier W. Heeres, Nissim Ofek, Katrina Sliwa, Eric Holland, Chen Wang, Jacob Blumoff, Kevin Chou, Michael J. Hatridge, Luigi Frunzio, Michel H. Devoret, Liang Jiang, and Robert J. Schoelkopf. Quantum memory with millisecond coherence in 

6 

   - circuit QED. <u>Physical Review B,</u> 94(1):014506, July 2016. Publisher: American Physical Society. 

- [9] R. K. Naik, N. Leung, S. Chakram, Peter Groszkowski, Y. Lu, N. Earnest, D. C. McKay, Jens Koch, and D. I. Schuster. Random access quantum information processors using multimode circuit quantum electrodynamics. <u>Nature Communications,</u> 8(1):1–7, December 2017. Number: 1 Publisher: Nature Publishing Group. 

- [10] T. A. Palomaki, J. W. Harlow, J. D. Teufel, R. W. Simmonds, and K. W. Lehnert. Coherent state transfer between itinerant microwave fields and a mechanical oscillator. <u>Nature,</u> 495(7440):210–214, March 2013. Number: 7440 Publisher: Nature Publishing Group. 

- [11] Connor T. Hann, Chang-Ling Zou, Yaxing Zhang, Yiwen Chu, Robert J. Schoelkopf, S.M. Girvin, and Liang Jiang. Hardware-Efficient Quantum Random Access Memory with Hybrid Quantum Acoustic Systems. <u>Physical Review Letters,</u> 123(25):250501, December 2019. Publisher: American Physical Society. 

- [12] Alexei M. Tyryshkin, Shinichi Tojo, John J. L. Morton, Helge Riemann, Nikolai V. Abrosimov, Peter Becker, Hans-Joachim Pohl, Thomas Schenkel, Michael L. W. Thewalt, Kohei M. Itoh, and S. A. Lyon. Electron spin coherence exceeding seconds in high-purity silicon. <u>Nature Materials, 11(2):143–147,</u> 2012. 

- [13] M. Steger, K. Saeedi, M. L. W. Thewalt, J. J. L. Morton, H. Riemann, N. V. Abrosimov, P. Becker, and H.-J. Pohl. Quantum Information Storage for over 180 s Using Donor Spins in a 28Si Semiconductor Vacuum. <u>Science,</u> 336(6086):1280–1283, August 2012. 

- [14] Juha T. Muhonen, Juan P. Dehollain, Arne Laucht, Fay E. Hudson, Rachpon Kalra, Takeharu Sekiguchi, Kohei M. Itoh, David N. Jamieson, Jeffrey C. McCallum, Andrew S. Dzurak, and Andrea Morello. Storing quantum information for 30 seconds in a nanoelectronic device. <u>Nature Nanotechnology,</u> 9(12):986–991, October 2014. 

- [15] J. H. Wesenberg, A. Ardavan, G. A. D. Briggs, J. J. L. Morton, R. J. Schoelkopf, D. I. Schuster, and K. Mlmer. Quantum Computing with an Electron Spin Ensemble. <u>Physical Review Letters, 103(7):070502, 2009.</u> 

- [16] E. M Purcell. Spontaneous emission probabilities at radio frequencies. <u>Phys. Rev., 69:681, 1946.</u> 

- [17] A. Bienfait, J.J. Pla, Y. Kubo, X. Zhou, M. Stern, C.-C. Lo, C.D. Weis, T. Schenkel, D Vion, D. Esteve, J.J.L. Morton, and P. Bertet. Controlling Spin Relaxation with a Cavity. <u>Nature,</u> 531:74 – 77, 2016. 

- [18] M. Afzelius, N. Sangouard, G. Johansson, M. U. Staudt, and C. M. Wilson. Proposal for a coherent quantum memory for propagating microwave photons. <u>New Journal of Physics,</u> 15(6):065008, June 2013. 

- [19] Jrme Ruggiero, Jean-Louis Le Gout, Christoph Simon, and Thierry Chanelire. Why the two-pulse photon echo is not a good quantum memory protocol. <u>Physical Review A,</u> 79(5):053851, May 2009. Publisher: American Physical Society. 

- [20] Hua Wu, Richard E. George, Janus H. Wesenberg, Klaus Moelmer, David I. Schuster, Robert J. Schoelkopf, Kohei M. Itoh, Arzhang Ardavan, John J. L. Morton, and G. Andrew D. Briggs. Storage of Multiple Coherent Microwave Excita- 

tions in an Electron Spin Ensemble. <u>Physical Review Letters,</u> 105(14):140503, 2010. 

- [21] C. Grezes, B. Julsgaard, Y. Kubo, M. Stern, T. Umeda, J. Isoya, H. Sumiya, H. Abe, S. Onoda, T. Ohshima, V. Jacques, J. Esteve, D. Vion, D. Esteve, K. Molmer, and P. Bertet. Multimode Storage and Retrieval of Microwave Fields in a Spin Ensemble. <u>Physical Review X,</u> 4(2), June 2014. 

- [22] S. Probst, H. Rotzinger, A. V. Ustinov, and P. A. Bushev. Microwave multimode memory with an erbium spin ensemble. <u>Physical Review B, 92(1):014421, July 2015.</u> 

- [23] C. Grezes, B. Julsgaard, Y. Kubo, W. L. Ma, M. Stern, A. Bienfait, K. Nakamura, J. Isoya, S. Onoda, T. Ohshima, V. Jacques, D. Vion, D. Esteve, R. B. Liu, K. Mlmer, and P. Bertet. Storage and retrieval of microwave fields at the single-photon level in a spin ensemble. <u>Physical Review A,</u> 92(2):020301, August 2015. 

- [24] M. H. Mohammady, G. W. Morley, and T. S. Monteiro. Bismuth Qubits in Silicon: The Role of EPR Cancellation Resonances. <u>Physical Review Letters,</u> 105(6):067602, August 2010. 

- [25] Gary Wolfowicz, Alexei M. Tyryshkin, Richard E. George, Helge Riemann, Nikolai V. Abrosimov, Peter Becker, HansJoachim Pohl, Mike L. W. Thewalt, Stephen A. Lyon, and John J. L. Morton. Atomic clock transitions in silicon-based spin qubits. <u>Nat Nano, 8(11):881–881, November 2013.</u> 

- [26] Manjin Zhong, Morgan P. Hedges, Rose L. Ahlefeldt, John G. Bartholomew, Sarah E. Beavan, Sven M. Wittig, Jevon J. Longdell, and Matthew J. Sellars. Optically addressable nuclear spins in a solid with a six-hour coherence time. <u>Nature,</u> 517(7533):177–180, January 2015. 

- [27] Antonio Ortu, Alexey Tiranov, Sacha Welinski, Florian Frwis, Nicolas Gisin, Alban Ferrier, Philippe Goldner, and Mikael Afzelius. Simultaneous coherence enhancement of optical and microwave transitions in solid-state electronic spins. <u>Nature Materials, 17(8):671–675, August 2018.</u> 

- [28] A. Bienfait, J. J. Pla, Y. Kubo, M. Stern, X. Zhou, C. C. Lo, C. D. Weis, T. Schenkel, M. L. W. Thewalt, D. Vion, D. Esteve, B. Julsgaard, K. Mlmer, J. J. L. Morton, and P. Bertet. Reaching the quantum limit of sensitivity in electron spin resonance. <u>Nature Nanotechnology, 11(3):253–257, March 2016.</u> 

- [29] C. Macklin, K. OBrien, D. Hover, M. E. Schwartz, V. Bolkhovsky, X. Zhang, W. D. Oliver, and I. Siddiqi. A nearquantum-limited Josephson traveling-wave parametric amplifier. <u>Science, 350(6258):307–310, October 2015.</u> 

- [30] J.J. Pla, A. Bienfait, G. Pica, J. Mansir, F.A. Mohiyaddin, Z. Zeng, Y.M. Niquet, A. Morello, T. Schenkel, J.J.L. Morton, and P. Bertet. Strain-Induced Spin-Resonance Shifts in Silicon Devices. <u>Physical Review Applied, 9(4):044014, April 2018.</u> 

- [31] B. Albanese, S. Probst, V. Ranjan, C. W. Zollitsch, M. Pechal, A. Wallraff, J. J. L. Morton, D. Vion, D. Esteve, E. Flurin, and P. Bertet. Radiative cooling of a spin ensemble. <u>Nature Physics, pages 1–5, April 2020.</u> Publisher: Nature Publishing Group. 

- [32] C. D. Weis, C. C. Lo, V. Lang, A. M. Tyryshkin, R. E. George, K. M. Yu, J. Bokor, S. A. Lyon, J. J. L. Morton, and T. Schenkel. Electrical activation and electron spin resonance measurements of implanted bismuth in isotopically enriched silicon-28. <u>Applied Physics Letters, 100(17):172104, 2012.</u> 

7 

- [33] Richard E. George, Wayne Witzel, H. Riemann, N. V. Abrosimov, N. Ntzel, Mike L. W. Thewalt, and John J. L. Morton. Electron Spin Coherence and Electron Nuclear Double Resonance of Bi Donors in Natural Si. <u>Physical Review Letters,</u> 105(6):067601, August 2010. 

- [34] D. I. Schuster, A. P. Sears, E. Ginossar, L. DiCarlo, L. Frunzio, J. J. L. Morton, H. Wu, G. A. D. Briggs, B. B. Buckley, D. D. Awschalom, and R. J. Schoelkopf. High-Cooperativity Coupling of Electron-Spin Ensembles to Superconducting Cavities. <u>Physical Review Letters, 105(14):140501, 2010.</u> 

### **ACKNOWLEDGEMENTS** 

We thank P. Se´nat, D. Duet and J.-C. Tack for the technical support, and are grateful for fruitful discussions within the Quantronics group. We acknowledge IARPA and Lincoln Labs for providing a JTWPA used in the measurements. We acknowledge support from the Horizon 2020 research and innovation program through grant agreement No. 771493 (LOQO-MOTIONS), and of the European Union through the Marie 365 Sklodowska Curie Grant Agreement No. 765267 (QuSCO), and of the Agence Nationale de la Recherche (ANR) through projects QIPSE, MIRESPIN (ANR 19 CE47 0011), and the Chaire Industrielle NASNIQ, and of the UK’s Engineering and Physical Sciences Research Council through a Doctoral Training Award. T. S. was supported by the U.S. Department of Energy under Contract No. DE-AC02-05CH11231. 

### **AUTHOR CONTRIBUTIONS** 

V.R, J.J.M and P.B designed the experiment. T.S provided the implanted Si sample on which V.R fabricated the device. V.R and J.S performed measurements and numerical simulations with inputs from E.A and B.A. T.C provided theory support. V.R and P.B wrote the manuscript with useful contribution from all co-authors. 

## **SUPPLEMENTARY MATERIAL** 

### **I. DEVICE SETUP** 

The spin-resonator hybrid device is measured at the base temperature of a dilution refrigerator in a setup as shown in Fig. S1 **(A)** . The substrate is a natural silicon wafer with an epitaxially grown 700 nm surface layer of isotopically purified 99.95%<sup>28</sup> Si. This was implanted with Bi ions at energies of 40, 80, 120, 200, and 360 keV with a total fluence of 1.1 × 10<sup>12</sup> cm<sup>−3</sup> and annealed at 800<sup>◦</sup> C for 20 min in an N2 atmosphere (identical to the<sup>28</sup> Si sample used in Ref. 32). The resonator was patterned by electron-beam-lithography followed by evaporation of a 50 nm aluminum thin-film and liftoff. Prior to fabrication, the substrate was cleaned with a piranha solution, and oxygen plasma ashing was used shortly before thin-film deposition. The resonator inductance is a 700 µm long and 5 µm wide wire, which is shunted by a co-planar capacitor consisting of 12 inter-digitated fingers, 50 µm wide and 50 µm apart. 

The device is mounted inside a copper box with single antenna coupling to allow measurements in reflection. Reflected signals, before demodulation at room temperature, are first amplified by a TWPA at 20 mK and then by a HEMT at 4 K. The length of the antenna can be tuned to control the coupling and hence tune the resonance frequency, in this case by ∼ 10 MHz, which allows us to target the clock transition. Measured resonance curves are shown in the main panel of Fig. S1 **(B)** for two values of coupling rate κ _c_ . 

The magnetic field of 27 mT needed to bias the bismuth donor spins at their CT is large compared to the 10 mT critical field of bulk aluminum, and can therefore only be applied parallel to the sample. In our experiment, alignment is achieved mechanically before cool-down, since the field is applied by a single-axis coil, and residual misalignments are unavoidable. As a result, significant phase noise and frequency hysteresis (∼ 1 MHz) are observed in the resonator response. Moreover, the resonator frequency is seen to vary by ±1 MHz and κ change by ±20% from one cooldown to another. Resonator phase noise translates into an additional 

TABLE S1. Resonator parameters 

|Inductor width/length|5 µm/700 µm|
|---|---|
|ω0/2πat_B_0 =27 mT|7.336 GHz|
|Resonator impedance|40Ω|
|κ_c_|4×10<sup>5 </sup>s<sup>−1</sup>|
|κ_i_ (_n_cav =1,_B_0 =27 mT)|9×10<sup>5 </sup>s<sup>−1</sup>|
|κ (_n_cav =1,_B_0 =27 mT)|13×10<sup>5 </sup>s<sup>−1</sup>|





<!-- Start of picture text -->
1 v 3) | EE<br><!-- End of picture text -->

J J 



<!-- Start of picture text -->
| it :<br>L A AB ’ Notre es<br><!-- End of picture text -->



<!-- Start of picture text -->
~<br>N py o — 0 93g; ©) Gs? OF Dg, BO<br><!-- End of picture text -->

10 

### **V. TLS ABSORPTION** 

Two level systems (TLSs) already show up in the power dependence of internal quality factor, see the inset of Fig. S1. We extract their contribution quantitatively by measuring the absorbed field at magnetic fields where spins are resonant or non-resonant with the resonator frequency ω0. To get the absorbed field, we subtract the reflected field measured with a repetition time _t_ rep = 3 _T_ 1 from the one taken at _t_ rep ≪ _T_ 1, such that spins are either polarized or saturated, respectively. The measurements at different magnetic fields are plotted as solid lines in Fig. S3 **(B,D)** . For the first transition (CT) we observe that only 40 (20)% field absorption comes from spins, the rest being from the TLSs. The difference in absorption fraction between the first and the CT transition is consistent with the expected reduction in cooperativity. Indeed, at the CT, the matrix element is twice smaller than at the first transition, contributing to a reduction by a factor of 4 since _C_ is proportional to _g_<sup>2</sup> 0<sup>, whereas the number of spins</sup> is doubled because of the transition quasi degeneracy, leading to an overall cooperativity reduction by a factor of 2, as observed. All relevant plots in the main text and the Supplementary materials have been corrected for the contribution from TLSs. 



<!-- Start of picture text -->
A 1 B 52<br>α s<br>α p 48<br>44<br>0<br>40<br>0 30 60 1.3 1.4<br>time (µs) B 0 (mT)<br>C<br>10<br>input field ( n in = 40) retrieved field x ζ −1<br>1 2 3 4 ...  ... 4 3 2 1<br>0<br>I<br>-10 Q<br>0 2 4 6<br>time (ms)<br>310<br>(a.u.)<br>α  Q /<br>(a.u.)<br>ref<br>β<br><!-- End of picture text -->

FIG. S4. **Storage and retrieval of microwave photons near the first transition. (A)** Measured intra-cavity field for the cases of spins saturated (α<sup>_s_</sup> , red) and polarized (α<sup>_p_</sup> , green). **(B)** Change in total quality factor of the resonator due to absorption from spins measured at average photon number of _n_ cav ∼ 0.1. **(C)** Measured input fields and retrieved field quadratures _I_ and _Q_ . The retrieved field is multiplied by ζ<sup>−1</sup> , where ζ = 4 _C_ (κ _c_ /κ) = 0.14 is the memory field efficiency at time ≪ _T_ 2. Dashed curves in all panels are numerical simulations. 

input-output theory [34] 

### **VI. NUMBER OF SPINS** 

A rough estimate of the spin number _N_ can be made using the bismuth implantation profile, the device geometry and the spin linewidth. Taking the nominal concentration of 8 × 10<sup>16</sup> cm<sup>−3</sup> , there are 2.8×10<sup>7</sup> spins in a box of volume 5 µm× 0.1 µm × 700 µm (volume only below the wire forming the left peak of the split spectrum in Fig. S3 **A** ). These spins are distributed among states of the lower-energy _F_ = 4 manifold with a linewidth of Γ/2π ∼ 2.5 MHz, thus there are ∼ 1.2 × 10<sup>6</sup> spins/MHz per level of the _F_ = 4 manifold. 

For a quantitative extraction of _N_ , we measure the change in the intra-cavity field α<sup>sto</sup> when spins are saturated or polarized. In our case, a pulse sequence can be simply repeated on a time scale much shorter than _T_ 1 to saturate the spins. Experimentally measured intra-cavity fields are shown in Fig. S4(A) for the first transition from which we deduce _C_ ≈ 0.08. This value is consistent with the numerical simulations shown as dashed lines and yielding the number of spins coupled to the resonator as, _N_ /(Γ/2π) ≈ 5 × 10<sup>5</sup> spins/MHz for _g_ 0/2π ≈76 Hz. The same method has been employed in the main text (Fig. 3 **(A)** ) to extract 10<sup>6</sup> spins/MHz near the CT. 

An independent approach to quantify spin absorption is to measure change in the resonator quality factor as a function of the magnetic field as shown in the Fig. S4(A). The approach has the advantage that the TLSs do not react to magnetic fields. Changes in _Q_ = ω0/δω _B_ can be derived using 



where κ is the total decay rate of the resonator away from spin resonance, ∆ _s_ = ω0 − ω _s_ the detuning between spins and the resonator, Γ the spin ensemble linewidth and _g_ ens = _g_ 0 √ _N_ . The change in total quality factor _Q_ (= ω0/δω _B_ ) as a function of _B_ 0 near the first transition is plotted in Fig. S4 **(B)** . The dependence roughly follows the asymmetric shape seen in echo detected spectroscopy. From the Eq. S5, we estimate _N_ = 10<sup>6</sup> spins distributed in a Lorentzian spectrum of FWHM linewidth Γ/2π = 1 MHz. This estimate of _N_ /Γ is within a factor of 2 of the one extracted using the absorbed intra-cavity field. 

### **VII. FIELD ABSORPTION AND RETRIEVAL** 

In addition to the data shown in the main text, we also demonstrate the storage and retrieval of weak coherent fields at the first Bi:Si transition ( _B_ 0 = 1.4 mT, d _f_ /d _B_ 0 = 25 MHz/mT) as shown in Fig. S4 **(C)** . A train of microwave fields each containing less than 40 photons is incident on the spin ensemble and retrieved using a refocusing π pulse. We see again that the retrieved signal maintains the phase relation with respect to the input field. The storage time is however much smaller than at the CT, since the coherence time 

11 

is _T_ 2 = 7.5 ms. The retrieval field efficiency ζ = 4 _C_ (κ _c_ /κ) = 0.14 here is however larger than the value measured at CT due to lower internal losses (κ _i_ = 5×10<sup>5</sup> s<sup>−1</sup> , κ _c_ = 4×10<sup>5</sup> s<sup>−1</sup> ) and stronger spin-photon coupling strength _g_ 0/2π = 76 Hz. 

### **VIII. NOISE MEASUREMENTS** 

Here, we detail the noise measurements reported in Fig. 4. Considering _N_ spins excited during the refocusing π pulse, the number of photons _n_ SE emitted due to their spontaneous emission between time _t_ and _t_ + _dt_ is _Ndt_ / _T_ 1 for _t_ , _dt_ ≪ _T_ 1. In the Purcell limit, this yield the number of photons emitted by spontaneous emission during the echo, 



since the echo duration is ∼ 1/Γ. 

We can define the field annihilation and creation operators in the output mode in which the echo is emitted as _a_ = � _u_ ( _t_ − _t_ 0) _a_ out( _t_ ) _dt_ and _a_<sup>†</sup> = � _u_ ( _t_ − _t_ 0) _a_<sup>†</sup> out<sup>(</sup><sup>_t_)</sup><sup>_dt_, where</sup><sup>_t_0</sup> is the mean echo arrival time, and _u_ ( _t_ ) is the envelope function defining the mode, verifying � | _u_ ( _t_ )|<sup>2</sup> _dt_ = 1. We take _u_ ( _t_ ) as the Gaussian envelope of both the input pulse and the 

echo, i.e. _u_ ( _t_ ) = βin( _t_ )/ ~~�~~ <u>�</u> β<sup>2</sup> in<sup>(</sup><sup>_t_)</sup><sup>_dt_.With this definition, the</sup> quadrature _Xa_ = ( _a_ + _a_<sup>†</sup> )/2 verifies δ _Xa_<sup>2=1/4foracoher-</sup> ent state and for the vacuum, and δ _Xa_<sup>2=1/4(1 + 2</sup><sup>_C_)fora</sup> thermal state containing _C_ photons on average. The total output noise also includes the amplifier noise. Amplification is modelled as transforming input mode _a_ into output mode _b_ = √ _Ga_ + √ _G_ − 1 _a_<sup>†</sup> id<sup>,where</sup><sup>_G_isthepower</sup> gain, and _a_ id the idler operator. Defining the output mode quadrature as _Xb_ = ( _b_ + _b_<sup>†</sup> )/2, we get ⟨ _b_ ⟩ = √ _G_ ⟨ _a_ ⟩, and δ _Xb_<sup>2=</sup><sup>_G_δ</sup><sup>_X_</sup> _a_<sup>2+ (</sup><sup>_G_−1)δ</sup><sup>_X_</sup> id<sup>2.</sup> 

zero value ofWe then write _n_ ¯ id accounts for amplifier non-ideality, but also δ _X_ id<sup>2=</sup> 4<sup><u>1</u>(1 + 2¯</sup><sup>_n_id).In this equation, a non-</sup> for losses in-between the sample and the amplifier as well as added noise by the following amplifiers of the detection chain. In the limit of large gain, the total noise referred to the amplifier input thus writes δ _X_<sup>2</sup> = [ _G_ /4 + ( _G_ − 1)(1 + 2¯ _n_ id)/4]/ _G_ ≃ (¯ _n_ id + 1)/2 for vacuum or a coherent state, and δ _X_<sup>2</sup> = (¯ _n_ id + _C_ + 1)/2 for a thermal state of _C_ photons on average. 

As explained in the main text, we find _n_ ¯ id = 3.5 ± 1.7, a reasonable value compared to those measured in similar circuit QED setups. This consistency check gives us confidence both in the determination of field amplitudes and photon numbers in absolute units, and confirms that the echo emission occurs indeed with negligible added noise. 

