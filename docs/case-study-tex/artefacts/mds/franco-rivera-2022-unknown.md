# **Strong coupling of a Gd**<sup>3+</sup> **multilevel spin system to an on-chip superconducting resonator** 

Giovanni Franco-Rivera,<sup>1,</sup><sup>_∗_</sup> Josiah Cochran,<sup>1</sup> Seiji Miyashita,<sup>2</sup> Sylvain Bertaina,<sup>3</sup> and Irinel Chiorescu<sup>1, †</sup> 

> 1 _Department of Physics and The National High Magnetic Field Laboratory, Florida State University, Tallahassee, Florida 32310, USA_ 

> 2 _Department of Physics, Graduate School of Science, The University of Tokyo, 7-3-1 Bunkyo-Ku, Tokyo, 113-0033 Japan_ 

> 3 _CNRS, Aix-Marseille Université, IM2NP (UMR 7344),_ 

_Institut Matériaux Microélectronique et Nanosciences de Provence, Marseille, France_ 

(Dated: November 4, 2022) 

We report the realization of a strong coupling between a Gd<sup>3+</sup> spin ensemble hosted in a scheelite (CaWO4) single crystal and the resonant mode of a coplanar stripline superconducting cavity leading to a large separation of spin-photon states of 146 MHz. The interaction is well described by the Dicke model and the crystal-field Hamiltonian of the multilevel spin system. We observe a change of the crystal-field parameters due to the presence of photons in the cavity that generates a significant perturbation of the crystal ground state. Using finite-element calculations, we numerically estimate the cavity sensing volume as well as the average spinphoton coupling strength of _g_ 0 _≈_ 620 Hz. Lastly, the dynamics of the spin-cavity states are explored via pulsed measurements by recording the cavity ring-down signal as a function of pulse length and amplitude. The results indicate a potential method to initialize this multilevel system in its ground state via an active cooling process. 

## **I. INTRODUCTION** 

Interaction between quantum systems via electromagnetic excitations are currently the basis of operation of many quantum hybrid systems using photonic entanglement [1]. The confinement of electromagnetic fields in mesoscopic mode volumes, as in the case of on-chip superconducting cavities, allows the study of light and matter interactions in the strongcoupling regime when its coupling strength _gc_ exceeds the qubit dephasing rate _γ_ and cavity dissipation rate _κc_ [2]. Experimentally, electric dipole coupling between electromagnetic excitations in a cavity and a single quantum emitter has been achieved in atomic systems [3] and superconducting qubits [4] where the electric dipole interaction with the cavity mode is large. In contrast, achieving strong magnetic coupling between an electromagnetic field and a single quantum spin remains elusive due to its small magnetic dipole. However, the interaction can be collectively enhanced by employing an ensemble of _N_ -identical spins such that the ensemble coupling strength is enhanced by a factor of _√N_ . In this way strong coupling has been demonstrated with various spin systems like N-V centers and point defects in diamond [5–7], molecular magnets [8–10] and transition metals and rare-earth (RE) ions in crystals [6, 11–15]. Moreover, recent studies using Er<sup>3+</sup> :Y2SiO5 spin diluted crystals [16], N-V centers in diamond [17] and Bi defects in Si [18] demonstrated storing and retrieving the state of microwave photons at high-power and near the quantum limit regime. 

Among the 4f ions, Gd<sup>3+</sup> is half-filled and posses the largest spin quantum number ( _S_ = 7 _/_ 2) with no orbital angular momentum ( _L_ = 0). When doped into the CaWO4, this spin provides a large magnetic moment and crystal field which in moderate fields ( _∼_ 0 _._ 1 kG) allows spin transitions at large frequencies of _≈_ 18 GHz. The characteristics of the crystal 

> _∗_ gf15@fsu.edu 

> † ichiorescu@fsu.edu 

field allow the use of clock transitions where spin coherence is insensitive to field fluctuations [19]. It is important to note that the higher the transition (or cavity) frequency, the higher the spin-photon coupling which is another benefit of the Gd<sup>+3</sup> crystal field. Nevertheless, the resulting spin dynamics is using a frequency regime still practical for integration in circuit Quantum Electro-Dynamics (QED) architectures. 

By performing field dependent cavity spectroscopy measurements we explore the coupling between a Gd<sup>3+</sup> spin ensemble to a superconducting on-chip resonator. We demonstrate the strong-coupling regime characterized by a large avoided crossing of 146 MHz, so large that it leads to a significant perturbation of crystal’s ground state by the presence of a photon. The experimentally observed spin-cavity dressed states are well described by the Dicke model [20] for a multilevel system with high anisotropy. Moreover, we perform pulsed electron spin resonance (ESR) measurements which show a population inversion and suggest a way to perform active cooling of the spin system into its ground state. 

## **II. OBSERVATION OF THE STRONG COUPLING REGIME DESCRIBED BY THE DICKE MODEL** 

The spectroscopy of resonator-photon spin interaction is studied using a home-built heterodyne detector [19]. The sample holder is introduced inside a superconducting vector magnet with field **_H_** 0 and thermally anchored to the mixing chamber of a dilution refrigerator at _T ≃_ 0 _._ 38 K. The resonator is etched out of a 20 nm Nb film and contains a transition from a coplanar waveguide (CPW) to a coplanar stripline (CPS) [21] matched for a 50 Ω impedance. The CPS is capacitively coupled to a _λ /_ 4 resonant structure ending with a short-circuit shaped into an Ω-loop (internal radius of 15 _µ_ m). Fig. 1a shows a single crystal (size _≃_ 2 _._ 5 _×_ 1 _×_ 0 _._ 6 mm<sup>3</sup> ) of CaWO4 with a 0.05% spin concentration of Gd<sup>3+</sup> (Fig. 1b) well pressed on a bead of grease atop of the loop, where the field distribution of the resonant mode is mostly concentrated (see Fig. 1c-d). The crystal has a _I_ 4 _/a_ tetragonal symme- 



<!-- Start of picture text -->
B ey<br>fe 0, ° °<br><!-- End of picture text -->

~~— —~~ C ) 

( ) 

3 

TABLE I. Eigenstates of the cavity-spin Hamiltonian at the observed resonance field _Hr_ = 72 G. Amplitude coefficients less than 0.01 have been disregarded for clarity. 

|_|_3_⟩_=|_Sz_=7_/_2|_Sz_=5_/_2|_Sz_=3_/_2|_Sz_=1_/_2|_Sz_=_−_1_/_2|_Sz_=_−_3_/_2|_Sz −_5_/_2|_Sz_=_−_7_/_2|
|---|---|---|---|---|---|---|---|---|
|_n_=0|0.010|-0.629|-0.092|0|0|-0.153|-0.318|0|
|_n_=1|0.669|0.01|0|0|0.036|0|0|0.145|
|_|_4_⟩_=|_Sz_=7_/_2|_Sz_=5_/_2|_Sz_=3_/_2|_Sz_=1_/_2|_Sz_=_−_1_/_2|_Sz_=_−_3_/_2|_Sz −_5_/_2|_Sz_=_−_7_/_2|
|_n_=0|0|0.145|0.140|0|0|0.05|0.578|0|
|_n_=1|0.561|0|0|-0.03|0.03|0|0|-0.553|
|_|_5_⟩_=|_Sz_=7_/_2|_Sz_=5_/_2|_Sz_=3_/_2|_Sz_=1_/_2|_Sz_=_−_1_/_2|_Sz_=_−_3_/_2|_Sz_=_−_5_/_2|_Sz_=_−_7_/_2|
|_n_=0|0|0.605|0.015|0|0|0.141|-0.010|0|
|_n_=1|0.460|0|0|0.033|0.024|0|0|0.631|





<!-- Start of picture text -->
P11 (dBm) Aij/ A i m j ax<br>-20 -10 0 0.00 0.25 0.50 0.75 1.00<br>18.0<br>(a) (b)<br>17.9<br>17.8<br>17.7<br>-20 -10 0 10 20 -20 - 10 0 10 20<br>H0 (mT) H0 (mT)<br>0<br>-2<br>-4<br>-6 (c)<br>17.65 17.70 17.75 17.80 17.85 17.90 17.95 18.00<br>Frequency (GHz)<br>Frequency (GHz)<br> (dBm)<br>11<br>P<br><!-- End of picture text -->

FIG. 2. (a) Reflected power as a function of field and frequency showing a large splitting of _≈_ 146 MHz due to spin-photon strong coupling. The dashed line indicates the location of maximum separation between dips. (b) Normalized _A_ 2 _,_ 4 and _A_ 2 _,_ 5 (see Eq. 4) as the lower and upper branches, respectively. Simulated resonance frequencies are shown by yellow stars on panel (a), in good agreement with the experiment. (c) Reflected power _P_ 11 (black circles) at the resonance field represented by the dashed line in panel (a). The solid orange line corresponds to a fit to the data using Eq. 2. 

An iterative least-square comparison between the experimental spectra (Fig. 2a) and calculated transition frequencies (Fig. 2b) leads to crystal field parameters _B_<sup>_q_</sup> _k_<sup>,cav-</sup> ity resonance frequency _ωc/_ (2 _π_ ), relative orientation _θ_ of the static field relative to the _c_ -axis and spin-cavity coupling strength _gc_ : _B_<sup>0</sup> 2<sup>=-945.66,</sup><sup>_B_0</sup> 4<sup>=-1.2435,</sup><sup>_B_4</sup> 4<sup>=-25.3,</sup> _B_<sup>0and</sup><sup>_B_4(all in MHz units),</sup> 6<sup>= 5.712</sup><sup>_×_10</sup><sup>_−_4</sup> 6<sup>= 70.0</sup><sup>_×_10</sup><sup>_−_4</sup> _ωc/_ (2 _π_ ) = 17930.7 MHz, _θ_ = 81.66<sup>_◦_</sup> and _gc_ = 57.35 MHz. All crystal field parameters agree with our previous weak coupling study [19] within 1% difference except for _B_<sup>4</sup> 4<sup>which</sup> here is found to be 3 _._ 5 _×_ larger. 

The six lowest eigenenergies _|k⟩k_ =1 _..._ 6 are shown in Fig. 3a for _gc_ = 0 (dashed gray) and _gc_ = 57.35 MHz (blue). For _gc_ = 0 the states are labeled _|g, nc⟩_ and _|e j, nc⟩_ with _nc_ = 0 _,_ 1 for the ground and _j_<sup>th</sup> excited spin state, respectively ( _j_ = 1 _,_ 2 _,_ 3). States _|{g, e_ 1 _} ,_ 0 _⟩_ and _|{e_ 2 _, e_ 3 _} ,_ 0 _⟩_ correspond to the 7/2 and 5/2 Kramers doublets, respectively (see Fig. 3b left) split by the transverse field _H_ 0. States _|{g, e_ 1 _} ,_ 1 _⟩_ correspond to the _|Sz|_ =<sup>_∼_</sup> 7 _/_ 2 doublet raised by _h_ ¯ _ωc_ (see Fig. 3b right). A spin-cavity coupling strength _gc/_ (2 _π_ ) = 57.35 MHz leaves _|_ 1 _⟩_ = _|g,_ 0 _⟩_ and _|_ 2 _⟩_ = _|e_ 1 _,_ 0 _⟩_ untouched but gives a hybridization between the _|e_ 1 _,_ 1 _⟩_ and _|e_ 2 _,_ 0 _⟩_ leading to the experimentally observed gap of 146 MHz between states _|_ 4 _⟩_ and _|_ 5 _⟩_ (states _|{_ 3 _,_ 4 _,_ 5 _}⟩_ are listed in Table I). Thus, the exact diagonalization leads to a cooperativity factor _C_ = _κgc_<sup>2</sup> _<u>cγs</u>_<sup>_≈_35 rather</sup> than _≈_ 58 obtained from the two-level picture of the _S_ 11 fit . We note that larger factors have been inferred in other RE ions [15] but no gap was observed. 

The observed large difference in the crystal-field _B_<sup>4</sup> 4<sup>param-</sup> eter between the weak and strong coupling cases, as mentioned above, can be explained using the Dicke Hamiltonian of Eq. 3. We calculate the change in _E_ 1 =<sup>_∼_</sup> _Eg,_ 0 at zero field as a function of _B_<sup>4</sup> 4<sup>(seeFigure3cleftaxis)andcompareditto</sup> the change inflicted by the presence of a single photon in the cavity _E_ 3 _− E_ 1 as a function of _gc_ for fixed _B_<sup>4</sup> 4<sup>=</sup><sup>_−_25</sup><sup>_._3 MHz</sup> ( _E_ 3 = _Eg,_ 1 only for _gc_ = 0). For a proper comparison, the photon frequency needs to be subtracted as well as shown in Fig. 3c (right axis). The two vertical axes of Fig. 3c have the same range: as _B_<sup>4</sup> 4<sup>or</sup><sup>_gc_increases, so does the perturbation of</sup> the electronic ground state leading to a _∼_ 130 MHz shift for the measured values of _B_<sup>4</sup> 4<sup>and</sup><sup>_gc_.The similarity between the</sup> two trends indicates that the photon field is so strongly coupled to spin that the electrostatic interaction, intrinsic to the crystal only, it’s severely perturbed. 

## **III. SINGLE SPIN COUPLING STRENGTH ESTIMATION** 

The average single spin coupling to the resonator is done by integrating the coupling to the vacuum field _δ_ **_H_** 1 over ¯ the mode volume for an input power _Pn_ =0 = _hωcκc/_ 2 = - 124.1 dBm. For _|ψi, f ⟩_ = _|e_ 1 _,_ 2 _,_ 0 _⟩_ the single-spin cou- 



<!-- Start of picture text -->
— nm<br>ga—_ mmmmmmIITE lez, 0) h g lei, 1) mmm<br>De ommmmTTIIEES 3 ee __<br>SEE] Sa “Ter, 0 2 lel) |<br>a lg, 0)<br>a  — g. [27 (MHz)<br>Tee TTT 0 10 20 30 40 50 60<br>eel | | 0<br>=~ -20160 ~__ —a—g, = 57.35 MHz<br>.<br>-20180 —=— |Bj| = -25.3 MHz 20 —~<br>a Ny- Hy = 0 kG N<br>__-20200z IN 2040 ==8<br>— = -20220 60 3<br>P op =e ABET — 0.974 =<br>LL 20240 80 5<br>-20260 -100,p<br>-20280 -120<br>5 10 15 20 25<br>IBS] (MHz)<br><!-- End of picture text -->

5 



<!-- Start of picture text -->
8.0<br>(a)<br>-40 -20 0<br>7.0<br>P11 - Pin (dBm)<br>6.0<br>5.0<br>4.0<br>3.0<br>2.0<br>1.0<br>0.02 0.04 0.06 0.08 0.10 0.12 0.14<br>Pin  ( W) 1/2<br> (mW)<br>in<br>P<br> -<br>11<br>P<br>s)<br>Pulse length,  (  (dBm)<br>in<br>P<br> -<br>11<br>P<br><!-- End of picture text -->



<!-- Start of picture text -->
 = 2.0 s<br>(b)<br>0.02 0.04 0.06 0.08 0.10<br>Pin ( W) 1/2<br>Pin = -59.0 dBm Pin = -51.0 dBm<br>Pin = -57.0 dBm Pin = -49.0 dBm<br>Pin = -55.0 dBm Pin = -47.2 dBm<br>Pin = -53.0 dBm<br>3<br>2<br>5 10 15 20 25<br>(c) 1/ Pin  ( W) 1/2<br>0 2 4 6 8<br>pulse length,  ( s)<br>s)<br> (<br>inv<br><!-- End of picture text -->

FIG. 4. (a) Pulsed ESR measurements of the reflected cavity ringdown signal as a function of pulse length and squared-root of the applied drive power. (b) Horizontal cut of the FFT amplitude for a 2 _µ_ s pulse and its low-pass FFT average done to remove unwanted noise: a clear pattern corresponding to the Rabi oscillations of the state admixture is seen. (c) Pulse length cuts of the relative FFT amplitude obtained from panel (a) at large applied powers _Pin_ . Inset shows inversion pulse length _τ_ inv vs the inverse of the cavity input drive power 1 _/_<sup>_~~√~~_</sup> _Pin_ . 

cavity-spin states. The main minimum is well developed at high powers, as shown by vertical cuts in Fig. 3(c). The inset shows the position of the dip _τinv_ as a function of 1 _/_<sup>_~~√~~_</sup> _Pin_ and gives the required pulse length to transfer the population of _|_ 2 _⟩_ to _|_ 4 _⟩_ . In the simplest case of a driven two-level qubit, it is expected that the nutation angle increases linearly with _√Pin_ giving an oscillatory decay of the Rabi signal. In a similar fashion, the inversion time of the Rabi flop will decrease with increasing field amplitude. In the case of our experiments, the Gd spins are multi-level systems in the presence of a large and highly anisotropic crystal field (analyzing spin dynamics would require solving the time-dependence of the full Hamiltonian in the laboratory frame). An outcome of the observed population inversion suggests the possibility of an active cooling procedure [29, 30]: (i) a _τinv_ pulse depletes _|_ 2 _⟩_ and populates _|_ 4 _⟩_ , (ii) a fast relaxation from _|_ 4 _⟩_ to _|_ 1 _⟩_ provides the cooling to the ground state. Such relaxation can be induced by a _ω_ 41 pulse resonant with the _|_ 4 _⟩→|_ 1 _⟩_ transition or simply by waiting a certain amount of time. Although _ω_ 41 is slightly detuned from _ωc_ , the pulse can have enough power to stimulate the _|_ 4 _⟩→|_ 1 _⟩_ transition, by adding another microwave source. Using Eq. 4 we find _A_ 24 _, A_ 41 _≫ A_ 12 =<sup>_∼_</sup> 0 and thus the relaxation to _|_ 1 _⟩_ can take place prior to a repopulation of _|_ 2 _⟩_ . By repeating the pulse sequence, one can in principle provide a spin initialization in its ground state. 

The on-chip pulsed ESR measurements shown here represent a first step for the characterization of the spin dynamics of this multilevel system. Having a well known description of the pulse lengths and drive power will lead to _π_ -pulse dynamical decoupling sequences such as spin echo[31] and Carr-PurcellMeiboom-Gill (CPMG)[32, 33] that provide a direct measure of the spin dephasing time. 

## **V. CONCLUSION** 

In conclusion, we demonstrate the strong coupling regime between the Gd<sup>3+</sup> multilevel spin system to an on-chip superconducting resonator. Using exact diagonalization of the spincavity Dicke Hamiltonian we estimate the coupling strength of the spin ensemble as _gc/_ (2 _π_ ) = 57.35MHz. Together with the estimated cavity and spin dephasing rates, this leads to a cooperativity factor _C ≈_ 35 and averaged single spin coupling strength of 620 Hz. The dynamics of the cavity-spin states are explored using pulsed ESR measurements and a population inversion is observed. Most remarkably, we measure a strong perturbation of the anisotropic crystal-field parameter _B_<sup>4</sup> 4<sup>due</sup> to the large coupling between the spins and the resonator. 

## **ACKNOWLEDGEMENTS** 

This work was performed at NHMFL at the Florida State University and supported by the National Science Foundation through Grant No. NSF/DMR-1644779 and the State of Florida. We acknowledge discussions with Dr. Petru Andrei (FSU) and we thank Dr. A.M. Tkachuk for providing the sample. S.B. acknowledges support from CNRS research infrastructure INFRANALYTICS (FR2054) and the International Emerging Action QULT. S.M. acknowledges support from Grants-in-Aid for Scientific Research C (No. 18K03444) and the Elements Strategy Initiative Center for Magnetic Materials (ESICMM) funded by MEXT of Japan (Grant No. 12016013). 

6 

- [1] G. Kurizki, P. Bertet, Y. Kubo, K. Mølmer, D. Petrosyan, P. Rabl, and J. Schmiedmayer, Quantum technologies with hybrid systems, Proceedings of the National Academy of Sciences **112** , 3866 (2015), publisher: Proceedings of the National Academy of Sciences. 

- [2] S. Haroche and J.-M. Raimond, _Exploring the Quantum_ (Oxford University Press, 2006). 

- [3] R. J. Thompson, G. Rempe, and H. J. Kimble, Observation of normal-mode splitting for an atom in an optical cavity, Physical Review Letters **68** , 1132 (1992), publisher: American Physical Society. 

- [4] A. Wallraff, D. I. Schuster, A. Blais, L. Frunzio, R.-S. Huang, J. Majer, S. Kumar, S. M. Girvin, and R. J. Schoelkopf, Strong coupling of a single photon to a superconducting qubit using circuit quantum electrodynamics, Nature **431** , 162 (2004). 

- [5] Y. Kubo, F. R. Ong, P. Bertet, D. Vion, V. Jacques, D. Zheng, A. Dréau, J. F. Roch, A. Auffeves, F. Jelezko, J. Wrachtrup, M. F. Barthe, P. Bergonzo, and D. Esteve, Strong coupling of a spin ensemble to a superconducting resonator, Physical Review Letters **105** , 1 (2010), iSBN: 0031-9007\n1079-7114. 

- [6] D. I. Schuster, A. P. Sears, E. Ginossar, L. Dicarlo, L. Frunzio, J. J. L. Morton, H. Wu, G. A. D. Briggs, B. B. Buckley, D. D. Awschalom, and R. J. Schoelkopf, High-cooperativity coupling of electron-spin ensembles to superconducting cavities, Physical Review Letters **105** , 1 (2010), arXiv:1006.0242. 

- [7] R. Amsüss, C. Koller, T. Nöbauer, S. Putz, S. Rotter, K. Sandner, S. Schneider, M. Schramböck, G. Steinhauser, H. Ritsch, J. Schmiedmayer, and J. Majer, Cavity qed with magnetically coupled collective spin states, Physical Review Letters **107** , 060502 (2011). 

- [8] I. Chiorescu, N. Groll, S. Bertaina, T. Mori, and S. Miyashita, Magnetic strong coupling in a spin-photon system and transition to classical regime, Physical Review B - Condensed Matter and Materials Physics **82** , 1 (2010), iSBN: 1098-0121. 

- [9] A. Eddins, C. Beedle, D. Hendrickson, and J. R. Friedman, Collective coupling of a macroscopic number of single-molecule magnets with a microwave cavity mode, Physical Review Letters **112** , 120501 (2014), publisher: American Physical Society. 

- [10] C. Bonizzoni, A. Ghirri, and M. Affronte, Coherent coupling of molecular spins with microwave photons in planar superconducting resonators, Advances in Physics: X **3** , 1435305 (2018), https://doi.org/10.1080/23746149.2018.1435305. 

- [11] P. Bushev, A. K. Feofanov, H. Rotzinger, I. Protopopov, J. H. Cole, C. M. Wilson, G. Fischer, A. Lukashenko, and A. V. Ustinov, Ultralow-power spectroscopy of a rare-earth spin ensemble using a superconducting resonator, Physical Review B - Condensed Matter and Materials Physics **84** , 3 (2011). 

- [12] S. Probst, H. Rotzinger, S. Wünsch, P. Jung, M. Jerger, M. Siegel, A. V. Ustinov, and P. A. Bushev, Anisotropic rareearth spin ensemble strongly coupled to a superconducting resonator, Physical Review Letters **110** , 1 (2013). 

- [13] A. K. V. Keyser, J. J. Burnett, S. E. Kubatkin, A. V. Danilov, M. Oxborrow, S. E. d. Graaf, and T. Lindström, Pulsed electron spin resonance of an organic microcrystal by dispersive readout, Journal of Magnetic Resonance **321** , 106853 (2020). 

- [14] G. Dold, C. W. Zollitsch, J. O’Sullivan, S. Welinski, A. Ferrier, P. Goldner, S. de Graaf, T. Lindström, and J. J. Morton, High-cooperativity coupling of a rare-earth spin ensemble to a superconducting resonator using yttrium orthosilicate as a substrate, Phys. Rev. Applied **11** , 054082 (2019). 

- [15] S. Wang, L. Yang, R. L. Cone, C. W. Thiel, and H. X. Tang, High-cooperativity coupling of rare-earth spins to a planar superconducting resonator, Phys. Rev. Applied **18** , 014071 (2022). 

- [16] S. Probst, H. Rotzinger, A. V. Ustinov, and P. A. Bushev, Microwave multimode memory with an erbium spin ensemble, Physical Review B **92** , 014421 (2015). 

- [17] C. Grezes, B. Julsgaard, Y. Kubo, W. L. Ma, M. Stern, A. Bienfait, K. Nakamura, J. Isoya, S. Onoda, T. Ohshima, V. Jacques, D. Vion, D. Esteve, R. B. Liu, K. Mølmer, and P. Bertet, Storage and retrieval of microwave fields at the single-photon level in a spin ensemble, Physical Review A **92** , 020301 (2015). 

- [18] V. Ranjan, J. O’Sullivan, E. Albertinale, B. Albanese, T. Chanelière, T. Schenkel, D. Vion, D. Esteve, E. Flurin, J. J. L. Morton, and P. Bertet, Multimode storage of quantum microwave fields in electron spins over 100 ms, Physical Review Letters **125** , 210505 (2020). 

- [19] G. Franco-Rivera, J. Cochran, L. Chen, S. Bertaina, and I. Chiorescu, _On-chip detection of electro-nuclear transitions in_ 155 _,_ 157 _Gd multi-level spin system_ , Tech. Rep. arXiv:2203.11304 (arXiv, 2022). 

- [20] R. H. Dicke, Coherence in spontaneous radiation processes, Physical Review **93** , 99 (1954), publisher: American Physical Society. 

- [21] D. E. Anagnostou, M. Morton, J. Papapolymerou, and C. G. Christodoulou, A 0 - 55 ghz coplanar waveguide to coplanar strip transition, IEEE Transactions on Microwave Theory and Techniques **56** , 1 (2008). 

- [22] C. F. Hempstead and K. D. Bowers, Paramagnetic resonance of impurities in CaWO4. I. Two S-state ions, Physical Review **118** , 131 (1960). 

- [23] A. Zalkin and D. H. Templeton, X-ray diffraction refinement of the calcium tungstate structure, The Journal of Chemical Physics **40** , 501 (1964). 

- [24] C. Rudowicz and C. Y. Chung, The generalization of the extended Stevens operators to higher ranks and spins, and a systematic review of the tables of the tensor operators and their matrix elements, Journal of Physics Condensed Matter **16** , 5825 (2004). 

- [25] E. I. Baibekov, M. R. Gafurov, D. G. Zverev, I. N. Kurkin, A. A. Rodionov, B. Z. Malkin, and B. Barbara, Coherent spin dynamics in a gadolinium-doped CaW O4 crystal, Physical Review B **95** , 1 (2017). 

- [26] E. Abe, H. Wu, A. Ardavan, and J. J. Morton, Electron spin ensemble strongly coupled to a three-dimensional microwave cavity, Applied Physics Letters **98** , 10.1063/1.3601930 (2011). 

- [27] J. R. Johansson, P. D. Nation, and F. Nori, QuTiP: An opensource Python framework for the dynamics of open quantum systems, Computer Physics Communications **183** , 1760 (2012). 

- [28] A. Schweiger, _Principles of pulse electron paramagnetic resonance_ (Oxford University Press, Oxford, UK ; New York, 2001). 

- [29] S. O. Valenzuela, W. D. Oliver, D. M. Berns, K. K. Berggren, L. S. Levitov, and T. P. Orlando, Microwave-Induced Cooling of a Superconducting Qubit, Science **314** , 1589 (2006), publisher: American Association for the Advancement of Science. 

- [30] D. Leibfried, R. Blatt, C. Monroe, and D. Wineland, Quantum dynamics of single trapped ions, Rev. Mod. Phys. **75** , 281 (2003). 

- [31] E. L. Hahn, Spin echoes, Phys. Rev. **80** , 580 (1950). 

7 

- [32] H. Y. Carr and E. M. Purcell, Effects of diffusion on free precession in nuclear magnetic resonance experiments, Phys. Rev. **94** , 630 (1954). 

- [33] S. Meiboom and D. Gill, Modified spin-echo method for measuring nuclear relaxation times, Review of Scientific Instruments **29** , 688 (1958), https://doi.org/10.1063/1.1716296. 

