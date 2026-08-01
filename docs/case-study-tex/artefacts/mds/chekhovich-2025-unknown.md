# **Storing quantum coherence in a quantum dot nuclear spin ensemble for over 100 milliseconds** 

Harry E. Dyte 

_Department of Physics and Astronomy, University of Sheffield, Sheffield S3 7RH, United Kingdom_ 

Santanu Manna, Saimon F. Covre da Silva, and Armando Rastelli 

_Institute of Semiconductor and Solid State Physics,_ 

_Johannes Kepler University Linz, Altenberger Str. 69, 4040 Linz, Austria_ 

Evgeny A. Chekhovich<sup>_∗_</sup> 

_Department of Physics and Astronomy, University of Sussex, Brighton BN1 9QH, United Kingdom_ 

(Dated: February 18, 2025) 

States with long coherence are a crucial requirement for qubits and quantum memories. Nuclear spins in epitaxial quantum dots are a great candidate, offering excellent isolation from external environments and on-demand coupling to optical flying qubits. However, coherence times are limited to ≲ 1 ms by the dipole-dipole interactions between the nuclei and their quadrupolar coupling to inhomogeneous crystal strain. Here, we combine strain engineering of the nuclear spin ensemble and tailored dynamical decoupling sequences to achieve nuclear spin coherence times exceeding 100 ms. Recently, a reversible transfer of quantum information into nuclear spin ensembles has been demonstrated in quantum dots. Our results provide a path to develop this concept into a functioning solid-state quantum memory suitable for quantum repeaters in optical quantum communication networks. 

### **I. INTRODUCTION** 

Quantum memories are indispensable in large scale quantum networks, which are expected to enable long distance communication of quantum information [1–4]. Quantum memories have several key requirements [2], a primary figure of merit is the storage time, which is directly related to quantum repeater communication distance. Millisecond-range storage time allows for improvements over direct transmission through an optical fiber [5, 6]. Although entanglement generation rate is currently the main limitation [7], its continuous improvement highlights the need for even longer storage times, exceeding 100 ms, in order to achieve worldwide optical communication. 

> _∗_ E.Chekhovich@sussex.ac.uk 

2 

The storage of a quantum state in a memory is limited by the coherence time _T_ 2. Several material systems offer long _T_ 2, ranging from seconds to hours [8], including trapped atomic ensembles [9, 10], ions [11–16], electron spins [17, 18] and phosphorus nuclear spins [19–21] in silicon, as well as electron and nuclear spins of impurities in diamond [22, 23]. However, long _T_ 2 are often negated by poor optical properties required for a long-distance quantum network. There are promising hybrid approaches, such as combination of transmon qubits with solid-state quantum memories [24], but these often suffer from coupling inefficiencies and bandwidth mismatch [8] (see further discussion in Supplementary Note 4). 

Epitaxial quantum dots (QDs) in group III-V semiconductors have high qubit entanglement rates [25] and are excellent on-demand emitters of single [8, 26–28] and entangled photons [29, 30]. At the same time, QDs host material qubits: Electron spin qubits can be interfaced with optical photon qubits [31–33], but the coherence of the electron spin is limited to _≈_ 100 _µ_ s [34]. The nuclear spins are isolated from external environments, resulting in long lifetimes and coherence times [35–37]. Recently, two-way quantum state transfer between photon and nuclear spins has been demonstrated in a QD, using an electron spin qubit as a mediator [38, 39]. However, since all atoms in group III-V materials have non-zero nuclear spins, the natural nuclear spin coherence is limited to a rather modest _≈_ 1 ms range [40]. Extending nuclear spin coherence is thus a key task in achieving quantum memories suitable for quantum repeaters [41, 42]. 

Here, we achieve nuclear spin coherence of over _T_ 2 _≈_ 100 ms, made possible by applying two concepts: Firstly, elastic strain is used to engineer the spin-3/2 nuclei and spectrally isolate the subspace with _I_ z = _±_ 1 _/_ 2 spin projections. Small inhomogeneity of this subspace allows application of thousands of coherent control operations, thus enabling efficient dynamical decoupling. Secondly, a dedicated 40-pulse decoupling sequence is designed to extend nuclear spin ensemble coherence while overcoming the parasitic spin locking effects encountered in previous decoupling experiments [43, 44]. Analysis shows that residual decoherence is dominated by the finite-pulse effects and the effective three-body nuclear spin interactions, which are often overlooked. We predict that even longer _T_ 2, on the order of _≈_ 1 s, is well within reach through larger strains and further advances in dynamical decoupling. The macroscopically long coherence times achieved here do not rely on isotope enrichment, which is available only in group IV material spin qubits [20, 45]. Our demonstration of engineered long coherence unlocks the unrivaled optical properties of group III-V materials for applications in quantum memory devices. 

3 



<!-- Start of picture text -->
20<br>a b<br>18 I z = −3/2 nL+n   (1) Q AlGaAs 1010 54 Initialization  CHASE-10 pulse sequence cycle+x 2 𝜏 2𝜏 𝑇 Rf -x 2 Finalization<br>1614 +−1/21/2 nL+n   (2) Q Coherence storage subspace GaAsAlGaAs QD 6975GaAs 101010 321 pulse -x +y +y 𝑇 EvolTot +x = 12 𝜏+ 10 𝑇 +x -y Rf -y -x pulse t<br>12 +3/2 nL-n   (1) Q T Rf = 10 ms 10 0 c<br>108 75 B ZAs, 0 ≈ 5.16 T e , Dn-1/2 « +1/2 T Rf = 20 ms 101010 -1-2-3 CHASE-10 (+x)+x 2 -x 2 CHASE-10 (+y)+y 2 -y 2 CHASE-10 (-x)-x 2 +x 2 CHASE-10 (-y)-y 2 +y 2<br>10 -4<br>6 10 -5 d t<br>|n  (1) Q -n (2) Q | 10 -6 Dynamical Decoupling sequence<br>4 |n  (1) Q +n (2) Q | 10 -7 Optical Pumping Initialization Finalization Optical Probe<br>2 Dn+1/2 « +3/2 Dn-3/2 « -1/2 1010 -8-9<br>0 10 -10 NMR t<br>-300 -200 -100 0 100 200 300 V Pump V 0 e V Probe<br>Radio frequency offset (kHz)<br>eV)<br>m<br> (<br>hf<br>E<br>D<br>NMR signal,<br>Rf pulse spectral power density (arb. units)<br><!-- End of picture text -->

FIG. 1. **Optically detected nuclear magnetic resonance of a single quantum dot. a** Right inset shows schematic diagram of<sup>69</sup> Ga and<sup>75</sup> As nuclear spins in a GaAs/AlGaAs QD. NMR spectrum of the spin-3/2<sup>75</sup> As nuclei (black and blue solid lines, left scale) in an uncharged (0 _e_ ) QD. Frequency offset is shown with respect to the Larmor frequency _νL ≈_ 37 _._ 981 MHz arising from the Zeeman splitting at external field of _Bz ≈_ 5 _._ 16 T (left inset). Out of the three magnetic dipole transitions, the two satellite transitions (STs) undergo a first-order quadrupolar shift _±νQ_<sup>(1)</sup> (where _νQ_<sup>(1)</sup> _≈_ 255 _._ 1 kHz), while the central transition (CT) is affected only by the second-order quadrupolar shift _νQ_<sup>(2)</sup> _≈_ 3 _._ 3 kHz. The CT linewidth (∆ _ν−_ 1 _/_ 2 _↔_ +1 _/_ 2 _≈_ 0 _._ 8 kHz) is much narrower than the ST linewidth (∆ _ν_ +1 _/_ 2 _↔_ +3 _/_ 2 _≈_ ∆ _ν−_ 3 _/_ 2 _↔−_ 1 _/_ 2 _≈_ 13 _._ 8 kHz). Dashed lines (right scale) show spectral profiles of the Rf pulse bursts with duration _T_ Rf = 10 or 20 _µ_ s, tuned in resonance with the CT. **b** Schematic diagram of a CHASE-10 sequence cycle, letters and signs denote Rf pulse phases. The pulses are separated by the free-evolution intervals _τ_ . The total nuclear evolution time is _T_ EvolTot = 10 _T_ Rf + 12 _τ_ , while _T_ FreeEvol = 12 _τ_ is the pure free evolution time for one cycle. **c** The CHASE-40 supercycle constructed of four CHASE-10 steps, with pulse phase incremented by _π_ /2 in each step. **d** Timing of the ODNMR measurement cycle. Optical pumping creates longitudinal nuclear spin polarization. The initialization _π_ /2 Rf pulse converts this into transverse (coherent) nuclear polarization in the _xy_ plane. Dynamical decoupling is applied, followed by a finalization _π_ /2 pulse to rotate the remaining transverse polarization back along the z-axis. Finally, the nuclear polarization is read out using photoluminescence (PL) spectroscopy under an optical probe pulse. The sample bias is pulsed to maximize optical nuclear spin pumping and PL intensity during optical probing. 

### **II. RESULTS** 

**Strain-engineered nuclear spin ensemble.** We study the nuclear spin coherence of GaAs/AlGaAs QDs grown by molecular beam epitaxy. The right inset of Fig. 1a sketches the QD nuclear spin system of _N ≈_ 5 _×_ 10<sup>4</sup> nuclei. The three isotopes<sup>75</sup> As,<sup>69</sup> Ga, and<sup>71</sup> Ga all have nuclear spin _I_ = 3 _/_ 2. The sample is cooled to _≈_ 4 _._ 2 K. A superconducting magnet is used 

4 

to apply a static magnetic field _B_ z _≈_ 5 _._ 16 T along the sample growth crystal direction [001], lifting the degeneracy of the four nuclear spin states with spin projections _I_ z = _±_ 1 _/_ 2 _, ±_ 3 _/_ 2 (left inset in Fig. 1a). Optical pumping with circularly polarized light (Faraday geometry) is used to polarize the nuclear spins along the static magnetic field [46]. The nuclear spin lifetime is typically _T_ 1 _>_ 10 s [47], significantly longer than the coherence times measured in this work. Nuclear spin polarization is measured via photoluminescence (PL) spectroscopy [48], see examples in Fig. 2a. A copper coil generates oscillating magnetic field perpendicular to _Bz_ , enabling optically detected nuclear magnetic resonance (ODNMR) measurements. Radio frequency (Rf) bursts with raised cosine envelope are used to transfer coherence in and out of the storage nuclear spin subspace _I_ z = _±_ 1 _/_ 2 and to perform its dynamical decoupling. 

The sample is stressed uniaxially along the [110] crystal direction, perpendicular to the static magnetic field. The resulting anharmonicity [36, 49], is characterised by the first-order qudrupolar splitting _νQ_<sup>(1).ThemeasuredNMRspectrum,showninFig.1afor75Asnucleiinaneutral(0</sup><sup>_e_)</sup> GaAs/AlGaAs QD, reveals _νQ_<sup>(1)</sup><sup>_≈_255</sup><sup>_._1kHz.Thissplittingsignificantlyexceedsthelinewdithsof</sup> the NMR transitions: the full width at half maximum (FWHM) ∆ _ν_ +1 _/_ 2 _↔_ +3 _/_ 2 _≈_ ∆ _ν−_ 3 _/_ 2 _↔−_ 1 _/_ 2 _≈_ 13 _._ 8 kHz of the satellite transitions (STs) _−_ 3 _/_ 2 _↔−_ 1 _/_ 2 and +1 _/_ 2 _↔_ +3 _/_ 2 is dominated by the inhomogeneous qudrupolar broadening, while the FWHM ∆ _ν−_ 1 _/_ 2 _↔_ +1 _/_ 2 _≈_ 0 _._ 8 kHz of the central transition _−_ 1 _/_ 2 _↔_ +1 _/_ 2 is controlled by a combination of the second-order quadrupolar inhomogeneity and the dipole-dipole interactions [44, 50]. The small CT linewidth combined with its strain-induced spectral isolation from STs make it an ideal spin subspace for coherence storage. Notably, the lattice-matched GaAs/AlGaAs QDs offer a significant advantage over Stranski-Krastanov QDs where ∆ _ν−_ 1 _/_ 2 _↔_ +1 _/_ 2 _≈_ 10 _−_ 40 kHz [44]. 

**Hamiltonian engineering of a nuclear spin ensemble.** Dynamical control of spin interactions is a powerful technique in magnetic resonance [51, 52]. The method is based on applying a sequence of Rf pulses that perform fast coherent rotations of the spins, separated by the free evolution intervals. In the interaction picture (the “toggling” frame of reference) the Rf pulses can be viewed as transformations of the spin-interaction Hamiltonian. The _π_ -pulse rotations invert the sign of the frequency shifts, allowing refocusing of the dephasing [53], which in QDs is caused primarily by inhomogeneous quadrupolar broadening. On the other hand, a sequence of four phaseshifted _π_ /2-pulses transforms the nuclear spin-spin dipolar interactions in such a way that averages them to zero over the pulse sequence cycle [54]. The average Hamiltonian is the leading (0th order) term in the Magnus expansion of the entire Hamiltonian in the toggling frame. By introducing more complex sequences of pulses it is possible to eliminate the unwanted interactions to higher 

5 



<!-- Start of picture text -->
������<br>t i c l p<br>l a i z t i o<br>σ<br>σ �<br>f p l s e d t i o ,   ( µ<br>∆<br>,  ����������<br>� / 2  ↔  / 2<br> F I D (  = 1 0  µ<br> H n E o (  = 2 0  µ<br>0 d l i n g (  = 2 0  µ<br>l e  = 1 ( 0 p l s<br>l e  = 1 2 ( 0 p l s<br>l e  = 3 2 ( 0 p l s<br>l e  = 4 8 ( 0 p l s<br>. 6 . 6 . 6 . 0 . 0 . 1<br>L p t o n e y ( i n f r e e l u t i o n t i m ,   (<br>µ<br> (<br>∆<br>l ,<br>i g<br>i t s R s<br>. u<br>i t y (<br>µ<br>t e  (<br>L i n ∆<br>l ,<br>i g<br>R s<br><!-- End of picture text -->

FIG. 2. **Dynamical decoupling of QD nuclear spins. a** Two photoluminescence (PL) spectra of a neutral exciton in the same individual QD measured after optical pumping with _σ_<sup>+</sup> ( _σ_<sup>_−_</sup> ) polarized light, which results in negative (positive) nuclear spin polarization. PL spectral splitting ∆ _E_ PL is a sum of the constant Zeeman splitting and the nuclear hyperfine shift ∆ _E_ hf, which is derived from the variations of ∆ _E_ PL. **b** Rabi oscillations of the nuclear spins in a neutral (0 _e_ ) QD observed under an increasing duration _T_ Rf of an Rf pulse of constant amplitude. **c** Nuclear spin decoherence measured by optically detected nuclear magnetic resonance (ODNMR) under free induction decay (FID, open squares), Hahn echo (solid squares) and an increasing number of CHASE-40 dynamical decoupling cycles _n_ Cycles = 1 _−_ 48 (see legend). Rf pulses, with duration _T_ Rf = 20 _µ_ s are applied to the central spin transition _−_ 1 _/_ 2 _↔_ +1 _/_ 2 in a neutral (0 _e_ ) QD. Nuclear spin polarization is initialized with an x pulse ( _ϕ_ = 0). 

## orders, thus engineering the spin Hamiltonian to have the desired form [52]. 

Here, we engineer a “time suspension” [55] type of sequence, where the Hamiltonian terms are eliminated as much as possible to preserve an arbitrary coherent state of the nuclear spin ensemble for the longest possible time. As a starting point we use a CHASE-10 cyclic sequence of _π_ /2 and _π_ pulses [44] shown in Fig. 1b. This sequence eliminates the average (0th order) free-evolution Hamiltonian both for the resonance frequency shifts and the spin-spin interactions. By symmetrizing the sequence, a CHASE-20 supercycle is formed, which further eliminates all the 1st-order terms in the Hamiltonian. The CHASE-20 sequence has been applied to QDs previously, demonstrating its ability to suppress decoherence even under large inhomogeneous resonance broadenings 

6 

in Stranski-Krastanov InGaAs/GaAs QDs [44]. In low-strain GaAs/AlGaAs QDs, nuclear spin coherence times up to _T_ 2 _≈_ 20 ms have been achieved [36]. However, the _π_ pulses cause spin locking [43, 44] which selectively accelerate decoherence of the spin states polarized along a certain equatorial axis of the Bloch sphere in the rotating frame, while artificially enhancing (“locking”) the states polarized along the orthogonal equatorial axis. This behaviour is unwanted in quantum memory applications as it may lead to distortion of the state during storage. 

Here we use a different approach, where four CHASE-10 cycles are combined into a CHASE-40 supercycle shown in Fig. 1c. The phases of the Rf pulses in each CHASE-10 subcycle are stepped by _π_ /2. While each subcycle causes spin locking, the preferential direction of the “lock”, when viewed in the rotating frame, makes a full rotation around the direction of the static magnetic field ( _z_ ) over the CHASE-40 supercycle. This four-step “rotating spin lock” eliminates the net spin locking effect for an arbitrary coherent state, as demonstrated through rigorous calculation (See Supplementary Note 5). Furthermore, the leading order residual Hamiltonian of CHASE-40 is twice smaller than in CHASE-20, resulting in extended coherence. 

**Extended spin coherence under dynamical decoupling.** We start by examining experimentally the nuclear spin dynamics under continuous resonant Rf driving. The results shown in Fig. 2b reveal Rabi oscillations, which confirm the coherent nature of spin driving and allow the _π/_ 2 and _π_ Rf pulses to be calibrated for dynamical decoupling (See Supplementary Note 2C). We then apply dynamical decoupling to the isolated _I_ z = _±_ 1 _/_ 2 nuclear spin subspace with two varying parameters: the number of sequence cycles _n_ Cycles and the total free evolution time _T_ FreeEvol. Fig. 2c shows nuclear spin coherence decay measured using ODNMR. In the simplest case of free induction decay (FID), without any dynamical decoupling (open black squares), the dephasing time is _T_ 2<sup>_∗≈_0</sup><sup>_._46msandisacombinedeffectofquadrupolarinhomogeneityanddipole-dipole</sup> interactions. By using a single _π_ pulse as a decoupling sequence (solid squares), we find the Hahn echo [53] coherence time _T_ 2<sup>HE</sup> _≈_ 1 _._ 38 ms, which is dominated by the dipole-dipole interactions. 

The measured effect of dynamical decoupling with one cycle of CHASE-40 is shown by the circles in Fig. 2c. The decay of the transverse nuclear polarization is plotted as a function of the total free evolution time _T_ FreeEvol (i.e. excluding the duration of the Rf pulses), and reveals a significant extension of the coherence time _T_ 2<sup>1xCHASE</sup><sup>_−_40</sup> _≈_ 12 _._ 3 ms. With the increasing number of CHASE-40 cycles the coherence time is extended further, reaching _T_ 2<sup>48xCHASE</sup><sup>_−_40</sup> _≈_ 106 _._ 6 ms for _n_ Cycles = 48 (orange triangles), an improvement by 2 orders of magnitude compared to the bare Hahn echo coherence time. The achieved nuclear spin coherence is also 3 orders of magnitude longer than the coherence of a dynamically decoupled electron spin in these QDs [34]. These results 



<!-- Start of picture text -->
& a Norma zed < b Norma zed e<br>To 1xq00] Q expermen, ech amp ude =, .o| Q expermen, ech amp ude ——Measure T CT<br>o 1X As C -120412, 11 o IX As § -320-12, 11 -=-= Frs-prncp v(2M) CT<br>Ko Tae 2s 2 Ta 2s F=—M easure T ST<br>°£ | 090 © | 090 =< Frs-prncp Vv(@2M)ST<br>1x10 Terookvol 070 £ 1x10 070<br>ES041x102 Moyeo s " gil Be 050 ES©'1x1072 rr i i E : 050 _0= 107! (od PN AN<br>- e 030 - E- 030 = 7 *<br>on : on fie. ° .<br>2< 1x10? 010 [9]< 1x10? i i 010 g 2) \<br>OT 1x10 1x10 1x102 1x107"  1x10° -0.10 OT 1x10 1x10 1x10 1x10” -0.10 =5 \\)<br>Toa evou o me Tego (S) Toa evou 0 me Tgory (8) g 10 -2 “\\<br>5 © Norma zed & d Norma zed 3<br>-pS 1x10° Numer ca mode, ech amp ude pS 1x10%4 Numer ca mode, ech amp ude & N \<br>3 1 spns, 1" 3 N 1 spns, 1" 3 *<br>IN IN \<br>2 homogneous 090 nhomogeneous 090 o \<br>Elio & 070 2Ex 0 F i:l 070 2 107 ee" Ss S \K<br>s i i. h \<br>© Tr 050 s i 050 A '<br>1x107? ji ©1x1072 i \ \<br>- 030 - 1 030 R<br>7)< 1x10 =i 010 7)< 1x10 -i 010 S N<br>T T — ><br>OC 1x10 1x10 1x102 1x107"  1x10° -0.10 OC 1x10 1x10 1x10 1x10 -0.10 10 10<br>Toa evou o me Teor (S) Toa evou 0 me Teyo1e (8) CHASE-4 cyc me Tey, (s)<br><!-- End of picture text -->

8 

free evolution or the Rf control pulses. We seek this optimum by replotting the data of Fig. 2c in Fig. 3a, where the normalized nuclear spin coherence is shown as a function of the total evolution (free evolution plus Rf pulses) time _T_ EvolTot (horizontal axis) and the duration _T_ Cycle of one CHASE40 cycle (vertical axis). The individual decay plots of Fig. 2c measured at fixed _n_ Cycles now appear along the diagonal lines in Fig. 3a. We fit the decay of coherence with an exponential function of _T_ EvolTot: the resulting decay time, which we denote as spin memory time _T_ M, is distinct from coherence time _T_ 2 and is shown as a function of _T_ Cycle by the single solid line in Fig. 3e. The maximum _T_ M _≈_ 136 ms is achieved not under the fastest possible Rf pulsing, but at _T_ Cycle _≈_ 2 ms, which is 5 times longer than the minimum _T_ Cycle _≈_ 0 _._ 8 ms achieved at _T_ Rf = 20 _µ_ s. This confirms that the finite-pulse effects are the main limitation to extending coherence storage through fast dynamical decoupling. 

Decoherence during the Rf pulses can in principle be suppressed by reducing _T_ Rf . However, experiments conducted on the _I_ z = _±_ 1 _/_ 2 spin states with a reduced _T_ Rf = 10 _µ_ s yield faster decoherence than under _T_ Rf = 20 _µ_ s (see Supplementary Note 3A). This seemingly contradictory result is understood by considering the spectral profiles of the Rf pulses (dashed lines in Fig. 1a). While the unwanted spin decoherence is indeed suppressed under the shorter _T_ Rf = 10 _µ_ s pulses, their broader spectral profile results in a stronger overlap with the STs. Such overlap leads to a faster “leakage” of coherence from the storage _I_ z = _±_ 1 _/_ 2 subspace into the _I_ z = _±_ 3 _/_ 2 states. Thus, there is an optimal pulse duration that balances the finite-pulse and the leakage effects. For the studied structure with the strain-induced quadrupolar splitting of _ν_ Q<sup>(1)</sup><sup>_≈_250kHz,thisoptimumis</sup> close to _T_ Rf = 20 _µ_ s. Increasing elastic strain from _≈_ 0 _._ 0025 in the studied sample to the _≈_ 0 _._ 01 range [56] is a promising route for applying shorter Rf pulses and a further significant improvement of the storage time and fidelity in a QD nuclear spin quantum memory. 

**CHASE decoupling of an inhomogeneous spin ensemble.** In order to demonstrate the importance of isolating the homogeneous _I_ z = _±_ 1 _/_ 2 CT storage subspace, we examine the opposite case of a _I_ z = ( _−_ 3 _/_ 2 _, −_ 1 _/_ 2) subspace. The considerably larger inhomogeneous broadening is characterised by the spectral shape of the ST NMR transitions. This is a weighted sum of a visible peak (Fig. 1a) with a linewidth of ∆ _ν_ +1 _/_ 2 _↔_ +3 _/_ 2 _≈_ ∆ _ν−_ 3 _/_ 2 _↔−_ 1 _/_ 2 _≈_ 13 _._ 8 kHz (65% weight), and a much broader invisible peak, which was shown previously [34] to stretch to _≈±_ 100 kHz (35% weight) and is caused by the atomic-scale strain of the randomly positioned Al and Ga atoms. The measured ST decoherence under CHASE decoupling is shown in Fig. 3b, and the resulting spin memory time _T_ M is shown by the double solid line in Fig. 3e. Unlike with _I_ z = _±_ 1 _/_ 2, the best possible dynamical decoupling of the _I_ z = ( _−_ 3 _/_ 2 _, −_ 1 _/_ 2) subspace is achieved at the shortest 

9 

possible _T_ Cycle. Despite this fastest possible Rf pulsing, the maximum achieved memory time is _T_ M _≈_ 31 ms. Although this storage time is a factor of _≈_ 15 improvement over the simple Hahn echo, it is a factor of _≈_ 4 _._ 4 worse than _T_ M achieved for the spectrally narrow _I_ z = _±_ 1 _/_ 2 subspace. 

The inferior spin memory time for an inhomogeneously broadened spin ensemble demonstrates how CHASE-40, as any other dynamical decoupling protocol, reaches the limit of its performance when the interaction that is being decoupled is no longer a small perturbation. The inhomogeneous broadening of the _I_ z = _±_ 1 _/_ 2 CT subspace is a small perturbation, characterized by ∆ _ν−_ 1 _/_ 2 _↔_ +1 _/_ 2 _T_ Rf _≈_ 0 _._ 015 _≪_ 1. By contrast, the relative broadening of the _I_ z = ( _−_ 3 _/_ 2 _, −_ 1 _/_ 2) subspace is comparable to unity for the visible part of the ST NMR peak (∆ _ν−_ 3 _/_ 2 _↔−_ 1 _/_ 2 _T_ Rf _≈_ 0 _._ 28) and violates the perturbative approximation (∆ _ν−_ 3 _/_ 2 _↔−_ 1 _/_ 2 _T_ Rf _>_ 1) for the broad component of the ST. The large inhomogeneity of the ST exacerbates decoherence through spin evolution during the finite Rf pulses. Moreover, ∆ _ν−_ 3 _/_ 2 _↔−_ 1 _/_ 2 _T_ Rf ≳ 1 means that Rf control pulses become more “soft” (i.e. not infinitely broad spectrally), resulting in imperfect rotations of the nuclear spins [57, 58]. On the other hand, CHASE-40 shows no sign of spin-locking even for the _I_ z = ( _−_ 3 _/_ 2 _, −_ 1 _/_ 2) subspace, despite its larger inhomogeneous broadening (See Supplementary Note 3B). 



<!-- Start of picture text -->
a b<br>18<br>18<br>16 z<br>14 75As,  B z ≈ 5.16 T, 16 y<br>12 −1/2 « +1/2, 14 x<br>10 T Rf = 20 ms, 12<br>8 CHASE-40  n Cycles = 4 10 θ  =  π /2 θ  =  π /2 θ  =  π /2 θ  =  π /2 θ  = 0<br>6 Initialization Rf pulse phase:f = −p/4 8 ϕ  = - π /4 ϕ  = 0 ϕ  =  π /4 ϕ  =  π /2<br>4 f = 0 6<br>2 f = p/4 4<br>0 f = p/2 2<br>q = 0 (longitudinal polarization)<br>-2 0<br>0.1 1 10 100<br>Initial nuclear state polarization<br>Spin free evolution time,  T FreeEvol (ms)<br> (ms)<br>2<br>T<br>eV)<br>m<br> (<br>hf<br>E<br>D<br>QD NMR signal,<br>Nuclear spin coherence time,<br><!-- End of picture text -->

FIG. 4. **Uniform decoupling of an arbitrary coherent nuclear spin state. a** Nuclear spin decoherence measured under 4 cycles of CHASE-40 with different phases _ϕ_ of the initialization Rf pulse, which initializes transverse nuclear polarization along different azimuth angles in the _xy_ plane ( _θ_ = _π/_ 2). The measurement of the longitudinal nuclear spin relaxation under CHASE-40 (without the initialization pulse, _θ_ = 0) is shown by the open diamonds. **b** The nuclear spin decay times _T_ 2 and _T_ 1 obtained from fitting the data in **a** . Schematics show orientation of the nuclei on the Bloch sphere after the initialization pulse, where present. 

**Uniform decoupling of an arbitrary coherent nuclear spin state.** An ideal quantum memory must store any given state with equally high fidelity. However, dynamical decoupling can create parasitic spin locking regimes, where storage effectiveness depends on the initial state [43, 44]. 

10 

We examine the uniformness of the quantum state storage by measuring dynamical decoupling of the homogeneous _I_ z = _±_ 1 _/_ 2 subspace under four cycles of CHASE-40 with different initial states. The phase _ϕ_ of the initialization Rf pulse is varied to prepare transverse nuclear spin polarization along the different axes in the equatorial _xy_ plane of the rotating frame ( _ϕ_ = 0 corresponds to an “+x” Rf pulse and prepares polarization along the _−y_ axis, a “+y” pulse with _ϕ_ = _π/_ 2 prepares polarization along the _x_ axis). We further perform a measurement, where the initialization pulse is omitted, corresponding to initial nuclear spin polarization along the strong magnetic field ( _θ_ = 0). The measured decay curves are shown in Fig. 4a. The coherence times obtained from fitting are shown in Fig 4b, and are around _T_ 2 _≈_ 18 ms, nearly independent of the initial state. 

The uniform dynamical decoupling of different initial states confirms experimentally the design principle of the CHASE-40 supercycle. Cycling of the Rf pulse phases in the four constituent CHASE-10 subcycles can be understood intuitively as a “rotary spin lock”: the axis of spin locking is slowly precessing with respect to the rotating frame, with a net effect of removing any preferential spin locking axis over the entire CHASE-40 cycle. Rigorous calculations confirm this result, showing that the symmetry axis of the residual Hamiltonian of CHASE-40 is along the strong static magnetic field ( _z_ axis). It is also worth noting that the _T_ 2 decay time of the transverse polarization (measured with an initialization _π/_ 2 pulse) is nearly identical to that of the longitudinal _T_ 1 decay time (measured without any initialization pulse): a well-designed time-suspension sequence eliminates all the leading interaction terms, effectively removing the distinction between the longitudinal ( _T_ 1) and transverse ( _T_ 2) relaxation timescales. 

The rotary spin lock offers a simple and reliable approach for reusing the dynamical decoupling sequences where spin locking is otherwise present [44, 59, 60]. The robustness of CHASE-40 against spin locking is key to achieving long spin memory times _T_ M ≳ 100 ms through repeated cycling (up to 2400 pulses). 

## **Predicting dynamical decoupling performance through analytical and numerical** 

**modeling.** The effective spin Hamiltonian under dynamical decoupling can be calculated as a Magnus expansion series. However, finding the spin dynamics from a known Hamiltonian is still a difficult problem. On the other hand, the exact spin dynamics is related to the exact NMR spectral lineshape through Fourier transform. The NMR lineshape can be approximated as a Gaussian, and its linewidth can be approximated in terms of the second moment _M_ 2, which in turn can be found from the Hamiltonian through direct calculation. The approximate coherent memory time can then be found as _T_ M _≈_ ~~�~~ 2 _/M_ 2 [52]. The residual Hamiltonian of CHASE-40 has been computed analytically up to second order: it is too bulky to reproduce in full, a more detailed 

11 

discussion can be found in Supplementary Note 5. The Hamiltonian depends on two parameters: the magnitude of the dipole-dipole interaction and the quadrupolar inhomogeneity. These are derived from FID and Hahn Echo experimental data, allowing _T_ M<sup>CHASE</sup><sup>_−_40</sup> to be calculated up to second order in analytical form and without any fitting parameters. The results are shown by the dashed lines in Fig. 3e. For the homogeneous subspace _I_ z = _±_ 1 _/_ 2 (single dashed line), the analytical model accurately predicts the peak in the spin memory time _T_ M at _T_ Cycle _≈_ 2 ms. The actual peak value of _T_ M is underestimated but matches the experiment within a factor of _≈_ 2. By contrast, for the inhomogeneous subspace _I_ z = ( _−_ 3 _/_ 2 _, −_ 1 _/_ 2), the model underestimates _T_ M by an order of magnitude. This indicates the limited accuracy of the perturbative Magnus expansion, which breaks down when the inhomogeneous broadening (in frequency units) is no longer small when compared to the reciprocal cycle time 1 _/T_ Cycle. In principle, the analytical model could be improved by extending the Magnus expansion. However, the increasing complexity of the highorder terms makes this approach impractical. 

The advantage of the analytical model is that it allows insights into the underlying phenomena. In particular, we find that direct dipole-dipole interactions of the _i_ th and _j_ th spins of the ensemble, characterised by the coupling constant _νij_ , is eliminated by CHASE-40 up to second order inclusive. However, the dipolar interaction of the spins _i, j_ remains, but with a coupling constant _∝ νikνkj_ , where _k_ = _i, j_ is any other spin. Such a term can be interpreted as a three-particle coupling, where the interaction of any two spins _i_ and _j_ is mediated by any other spin _k_ . Although often ignored, here we find that the residual decoherence of the homogeneous subspace _I_ z = _±_ 1 _/_ 2 can be explained only by taking into account this effective three-body interaction. The three-body second-order interaction limits _T_ M under slow dynamical decoupling (long _T_ Cycle). In the oposite limit of fast decoupling (short _T_ Cycle) the memory time _T_ M is limited by the zero-order dipole-dipole term arising from finite _T_ Rf _>_ 0. A combination of these two effects results in a non-monotonic dependence _T_ M( _T_ Cycle) with a maximum in _T_ M, as shown by the single lines in Fig. 3e. By contrast, the decoherence in the inhomogeneous subspace _I_ z = ( _−_ 3 _/_ 2 _, −_ 1 _/_ 2) is dominated by the quadrupolar offset inhomogeneity under finite ( _T_ Rf _>_ 0) control pulses. 

We further conduct numerical modeling of the CHASE dynamical decoupling by solving the exact Schrodinger equation of a system of _N_ = 12 spins (see details in Supplementary Note 6). The results for the case of the inhomogeneous subspace _I_ z = ( _−_ 3 _/_ 2 _, −_ 1 _/_ 2), are shown in Fig. 3d. Since the decoherence rate is dominated by the quadrupolar offsets, which is a singleparticle effect, a good quantitative agreement with the experiment (Fig. 3b) is obtained by using realistic values of the inhomogeneous quadrupolar shifts in the numerical model. The results 

12 

for the _I_ z = _±_ 1 _/_ 2 subspace, where quadrupolar inhomogeneity is taken to be zero, are shown in Fig. 3c. The numerical model reproduces the main features of the experimental data on the _I_ z = _±_ 1 _/_ 2 subspace (Fig. 3a), in particular the nonmonotonic dependence of the spin memory time _T_ M on the decoupling sequence cycle time _T_ Cycle. However, the agreement is only within an order of magnitude: the numerically-simulated maximum _T_ M _≈_ 2 s occurs at _T_ Cycle _≈_ 8 ms, compared to the measured maximum _T_ M _≈_ 0 _._ 136 s at _T_ Cycle _≈_ 2 ms. This discrepancy may seem unexpected, given that the numerically-simulated coherence time under simple Hahn echo _T_ 2<sup>HE</sup> _≈_ 1 _._ 4 ms is very close to the measured _T_ 2<sup>HE</sup> _≈_ 1 _._ 38 ms. However, the decoherence under Hahn echo is governed by the direct (pairwise) dipole-dipole interaction of the nuclear spins, whereas decoherence under CHASE-40 is dominated by the effective three-spin interaction. We therefore ascribe the discrepancy in _T_ M to the limited number of spins in the numerical model: the number of three-spin combinations contributing to decoherence in an ensemble with _N_ = 12 is considerably smaller than in a real crystal lattice of a QD. The discrepancy is also likely to include the small but nonzero quadrupolar inhomogeneity of the _I_ z = _±_ 1 _/_ 2 subspace, which reduces CHASE-40 _T_ M in a real QD. 

### **III. DISCUSSION** 

We have demonstrated very long coherence storage times of over 100 ms in a nuclear spin ensemble of an optically-active GaAs semiconductor QD. These QDs are a promising candidate for quantum memory, which integrates the spin qubit with a single photon sources [8], thus avoiding the need for complex hybrid schemes [24]. Long-term preservation of nuclear spin coherence demonstrated here is a key step in bringing the concept of QD-based optical quantum memory [39] to practical implementation. The extended coherence is enabled by strain engineering of the nuclear spin ensemble and the tailored 40-pulse time-suspension decoupling sequences. 

We use a three-pronged approach to the design of dynamical decoupling sequences. Numerical modelling can predict the overall performance of a dynamical decoupling protocol, but its accuracy is limited by the small number of spins _N_ , constrained in turn by the exponential scaling of the required computing resources with increasing _N_ . As a result, numerical simulations are time-consuming: full datasets of Figs. 3c, d require many days of computations on a workstation PC, which is comparable to experimental time required for Figs. 3a, b. Analytical calculations provide good predictions in case of small inhomogeneity. However, for a sequences with 40 pulses, derivation of the residual Hamiltonian takes several hours of computer-assisted algebraic deriva- 

13 

tions and further tedious manual work to analyse the bulky analytical results. Thus, the two modeling approaches encounter their different limitations, leaving experiment as the ultimate verification of the excellent coherence protection achieved with CHASE-40. The sequence is robust against spin locking, errors in control pulses, and is applicable to spin ensembles with a substantial inhomogeneous broadening. 

Strain engineering is a key enabling technique, as it allows spectral isolation of the homogeneous _I_ z = _±_ 1 _/_ 2 nuclear spin subspace. A further increase of elastic strain by a factor of _≈_ 4 is within the yield strain of GaAs and is feasible using membrane microstructures [56, 61, 62]. This would allow quadrupolar splitting in excess of _νQ_<sup>(1)</sup> ≳ 1 MHz, enabling further improvement in quantum memory storage time and fidelity. More importantly, the MHz-range quadrupolar splitting would be sufficient to exceed the electron-nuclear hyperfine interaction, which is ≲ 200 kHz in the studied GaAs QDs [49]. While dynamical decoupling of nuclear spins in presence of the central electron spin qubit is possible in principle [37], achieving long nuclear spin coherence in presence of electron would require spectral isolation (through increased strain) of the hyperfine-broadened nuclear spin transitions. 

The maximum storage time _T_ M under CHASE-40 decoupling is limited by the finite duration of the control pulses, which causes a drop in _T_ M in the limit of frequent Rf pulsing (single lines in Fig. 3e, limit of small _T_ Cycle). By eliminating the effect of finite pulses [51, 63] it should be possible to achieve _T_ M _≈_ 1 s even at the current level of elastic strain, limited only by the second-order threeparticle spin-spin interactions. More broadly, dynamical decoupling can be used to study spin-spin entanglement, thermalization in disordered quantum systems, and many-body localization [64, 65]. 

### **ACKNOWLEDGMENTS** 

_Acknowledgements:_ H.E.D. was supported by an EPSRC doctoral training grant. E.A.C. was supported by a Royal Society University Research Fellowship, the Leverhulme Trust grant RPG2023-141, and the EPSRC award EP/V048333/1. A.R. acknowledges support of the Austrian Science Fund (FWF) via the Research Group FG5, I 4320, I 4380, I 3762, the Linz Institute of Technology (LIT), and the LIT Secure and Correct Systems Lab, supported by the State of Upper Austria, the European Union’s Horizon 2020 research and innovation program under Grant Agreements No. 899814 (Qurope), No. 871130 (Ascent+), the QuantERA II project QD-E-QKD and the FFG (grant No. 891366). A.R. and E.A.C. were supported by the QuantERA award MEEDGARD. _Author contributions:_ S.M., S.F.C.S. and A.R. developed, grew and processed the 

14 

quantum dot samples. H.E.D, conducted the experiments. H.E.D. and E.A.C. analysed the data. H.E.D. and E.A.C. drafted the manuscript with input from all authors. E.A.C. performed numerical modelling and coordinated the project. 

- [1] Ladd, T. D. _et al._ Quantum computers. _Nature_ **464** , 45–53 (2010). 

- [2] Lvovsky, A. I., Sanders, B. C. & Tittel, W. Optical quantum memory. _Nat. Photon._ **3** , 706–714 (2009). 

- [3] Pang, X.-L. _et al._ A hybrid quantum memory–enabled network at room temperature. _Sci. Adv._ **6** , eaax1425 (2020). 

- [4] Bussi`eres, F. _et al._ Quantum teleportation from a telecom-wavelength photon to a solid-state quantum memory. _CLEO: 2014_ FTu2A.4 (2014). 

- [5] Tittel, W. _et al._ Photon-echo quantum memory in solid state systems. _Laser Photonics Rev._ **4** , 244–267 (2010). 

- [6] Zhao, R. _et al._ Long-lived quantum memory. _Nat. Phys._ **5** , 100–104 (2009). 

- [7] Yu, Y. _et al._ Entanglement of two quantum memories via fibres over dozens of kilometres. _Nature_ **578** , 240–245 (2020). 

- [8] Neuwirth, J. _et al._ Quantum dot technology for quantum repeaters: from entangled photon generation toward the integration with quantum memories. _Mater. Quantum Technol._ **1** , 043001 (2021). 

- [9] Treutlein, P., Hommelhoff, P., Steinmetz, T., H¨ansch, T. W. & Reichel, J. Coherence in microchip traps. _Phys. Rev. Lett._ **92** , 203005 (2004). 

- [10] Deutsch, C. _et al._ Spin self-rephasing and very long coherence times in a trapped atomic ensemble. _Phys. Rev. Lett._ **105** , 020401 (2010). 

- [11] Langer, C. _et al._ Long-lived qubit memory using atomic ions. _Phys. Rev. Lett._ **95** , 060502 (2005). 

- [12] Bollinger, J., Heizen, D., Itano, W., Gilbert, S. & Wineland, D. A 303-MHz frequency standard based on trapped Be<sup>+</sup> ions. _IEEE Trans. Instrum. Meas._ **40** , 126–128 (1991). 

- [13] Wang, Y. _et al._ Single-qubit quantum memory exceeding ten-minute coherence time. _Nat. Photon._ **11** , 646–650 (2017). 

- [14] Wang, P. _et al._ Single ion qubit with estimated coherence time exceeding one hour. _Nat. Commun._ **12** , 233 (2021). 

- [15] Zhong, M. _et al._ Optically addressable nuclear spins in a solid with a six-hour coherence time. _Nature_ **517** , 177–180 (2015). 

- [16] Bruzewicz, C. D., Chiaverini, J., McConnell, R. & Sage, J. M. Trapped-ion quantum computing: Progress and challenges. _Appl. Phys. Rev._ **6** , 021314 (2019). 

- [17] Tyryshkin, A. M., Lyon, S. A., Astashkin, A. V. & Raitsimring, A. M. Electron spin relaxation times of phosphorus donors in silicon. _Phys. Rev. B_ **68** , 193207 (2003). 

- [18] Tyryshkin, A. M. _et al._ Electron spin coherence exceeding seconds in high-purity silicon. _Nat. Mater._ 

15 

**11** , 143–147 (2011). 

- [19] Morton, J. J. _et al._ Solid-state quantum memory using the<sup>31</sup> P nuclear spin. _Nature_ **455** , 1085–1088 (2008). 

- [20] Steger, M. _et al._ Quantum information storage for over 180 s using donor spins in a<sup>28</sup> Si ”semiconductor vacuum”. _Science_ **336** , 1280–1283 (2012). 

- [21] Freer, S. _et al._ A single-atom quantum memory in silicon. _Quantum Sci. Technol._ **2** , 015009 (2017). 

- [22] Atat¨ure, M., Englund, D., Vamivakas, N., Lee, S.-Y. & Wrachtrup, J. Material platforms for spin-based photonic quantum technologies. _Nat. Rev. Mater._ **3** , 38–51 (2018). 

- [23] Stas, P.-J. _et al._ Robust multi-qubit quantum network node with integrated error detection. _Science_ **378** , 557–560 (2022). 

- [24] Kubo, Y. _et al._ Hybrid quantum circuit with a superconducting qubit coupled to a spin ensemble. _Phys. Rev. Lett._ **107** , 220501 (2011). 

- [25] Stockill, R. _et al._ Phase-tuned entangled state generation between distant spin qubits. _Phys. Rev. Lett._ **119** , 010503 (2017). 

- [26] Huber, D. _et al._ Highly indistinguishable and strongly entangled photons from symmetric GaAs quantum dots. _Nat. Commun._ **8** , 15506 (2017). 

- [27] Schweickert, L. _et al._ On-demand generation of background-free single photons from a solid-state source. _Appl. Phys. Lett._ **112** , 093106 (2018). 

- [28] Arakawa, Y. & Holmes, M. J. Progress in quantum-dot single photon sources for quantum information technologies: A broad spectrum overview. _Appl. Phys. Rev._ **7** , 021309 (2020). 

- [29] Liu, J. _et al._ A solid-state source of strongly entangled photon pairs with high brightness and indistinguishability. _Nat. Nanotechnol._ **14** , 586–593 (2019). 

- [30] Rota, M. B. _et al._ A source of entangled photons based on a cavity-enhanced and strain-tuned GaAs quantum dot. _eLight_ **4** , 13 (2024). 

- [31] De Greve, K. _et al._ Quantum-dot spin–photon entanglement via frequency downconversion to telecom wavelength. _Nature_ **491** , 421–425 (2012). 

- [32] Coste, N. _et al._ High-rate entanglement between a semiconductor spin and indistinguishable photons. _Nat. Photon._ **17** , 582–587 (2023). 

- [33] Laccotripes, P. _et al._ Spin-photon entanglement with direct photon emission in the telecom C-band. _Nat. Commun._ **15** , 9740 (2024). 

- [34] Zaporski, L. _et al._ Ideal refocusing of an optically active spin qubit under strong hyperfine interactions. _Nat. Nanotechnol._ **18** , 257–263 (2023). 

- [35] Gillard, G. _et al._ Fundamental limits of electron and nuclear spin qubit lifetimes in an isolated selfassembled quantum dot. _npj Quantum Inf._ **7** , 43 (2021). 

- [36] Chekhovich, E. A., da Silva, S. F. C. & Rastelli, A. Nuclear spin quantum register in an optically active semiconductor quantum dot. _Nat. Nanotechnol._ **15** , 999–1004 (2020). 

- [37] Gillard, G., Clarke, E. & Chekhovich, E. A. Harnessing many-body spin environment for long coherence 

16 

storage and high-fidelity single-shot qubit readout. _Nat. Commun._ **13** , 4048 (2022). 

- [38] Gangloff, D. A. _et al._ Quantum interface of an electron and a nuclear ensemble. _Science_ **364** , 62–66 (2019). 

- [39] Appel, M. H. _et al._ A many-body quantum register for a spin qubit. _Nat. Phys._ (2025). 

- [40] Chekhovich, E., Hopkinson, M., Skolnick, M. & Tartakovskii, A. Suppression of nuclear spin bath fluctuations in self-assembled quantum dots induced by inhomogeneous strain. _Nat. Commun._ **6** , 6348 (2015). 

- [41] Childress, L., Taylor, J. M., Sørensen, A. S. & Lukin, M. D. Fault-tolerant quantum communication based on solid-state photon emitters. _Phys. Rev. Lett._ **96** , 070504 (2006). 

- [42] Sharman, K., Kimiaee Asadi, F., Wein, S. C. & Simon, C. Quantum repeaters based on individual electron spins and nuclear-spin-ensemble memories in quantum dots. _Quantum_ **5** , 570 (2021). 

- [43] Li, D. _et al._ Intrinsic origin of spin echoes in dipolar solids generated by strong _π_ pulses. _Phys. Rev. B_ **77** , 214306 (2008). 

- [44] Waeber, A. M. _et al._ Pulse control protocols for preserving coherence in dipolar-coupled nuclear spin baths. _Nat. Commun._ **10** , 3157 (2019). 

- [45] Balasubramanian, G. _et al._ Ultralong spin coherence time in isotopically engineered diamond. _Nat. Mater._ **8** , 383–387 (2009). 

- [46] Millington-Hotze, P. _et al._ Approaching a fully-polarized state of nuclear spins in a solid. _Nat. Commun._ **15** , 985 (2024). 

- [47] Millington-Hotze, P., Manna, S., Covre da Silva, S. F., Rastelli, A. & Chekhovich, E. A. Nuclear spin diffusion in the central spin system of a GaAs/AlGaAs quantum dot. _Nat. Commun._ **14** , 2677 (2023). 

- [48] Urbaszek, B. _et al._ Nuclear spin physics in quantum dots: An optical investigation. _Rev. Mod. Phys._ **85** , 79–133 (2013). 

- [49] Dyte, H. E. _et al._ Is wave function collapse necessary? explaining quantum nondemolition measurement of a spin qubit within linear evolution. _Phys. Rev. Lett._ **132** , 160804 (2024). 

- [50] Klauder, J. R. & Anderson, P. W. Spectral diffusion decay in spin resonance experiments. _Phys. Rev._ **125** , 912–932 (1962). 

- [51] Haeberlen, U. & Waugh, J. S. Coherent averaging effects in magnetic resonance. _Phys. Rev._ **175** , 453–467 (1968). 

- [52] Mehring, M. _Principles of High Resolution NMR in Solids_ (Springer Berlin Heidelberg, 1983). 

- [53] Hahn, E. L. Spin echoes. _Phys. Rev._ **80** , 580–594 (1950). 

- [54] Waugh, J. S., Huber, L. M. & Haeberlen, U. Approach to high-resolution NMR in solids. _Phys. Rev. Lett._ **20** , 180–182 (1968). 

- [55] Cory, D., Miller, J. & Garroway, A. Time-suspension multiple-pulse sequences: applications to solidstate imaging. _J. Magn. Reson. (1969)_ **90** , 205–213 (1990). 

- [56] Huo, Y. H. _et al._ A light-hole exciton in a quantum dot. _Nat. Phys._ **10** , 46–51 (2013). 

- [57] Khodjasteh, K. & Lidar, D. A. Fault-tolerant quantum dynamical decoupling. _Phys. Rev. Lett._ **95** , 

17 

180501 (2005). 

- [58] Souza, A. M., Alvarez,<sup>´</sup> G. A. & Suter, D. Robust dynamical decoupling. _Philos. Trans. R. Soc. A_ **370** , 4748–4769 (2012). 

- [59] Dementyev, A. E., Li, D., MacLean, K. & Barrett, S. E. Anomalies in the NMR of silicon: Unexpected spin echoes in a dilute dipolar solid. _Phys. Rev. B_ **68** , 153302 (2003). 

- [60] Li, D., Dementyev, A. E., Dong, Y., Ramos, R. G. & Barrett, S. E. Generating unexpected spin echoes in dipolar solids with _π_ pulses. _Phys. Rev. Lett._ **98** , 190401 (2007). 

- [61] Hjort, K., Soderkvist, J. & Schweitz, J. A. Gallium arsenide as a mechanical material. _J. Micromech. Microeng._ **4** , 1 (1994). 

- [62] Mart´ın-S´anchez, J. _et al._ Strain-tuning of the optical properties of semiconductor nanomaterials by integration onto piezoelectric actuators. _Semicond. Sci. and Technol._ **33** , 013001 (2017). 

- [63] Burum, D. P. & Rhim, W. K. Analysis of multiple pulse NMR in solids. III. _J. Chem. Phys._ **71** , 944–956 (1979). 

- [64] Wei, K. X., Ramanathan, C. & Cappellaro, P. Exploring localization in nuclear spin chains. _Phys. Rev. Lett._ **120** , 070501 (2018). 

- [65] Lukin, A. _et al._ Probing entanglement in a many-body–localized system. _Science_ **364** , 256–260 (2019). 

1 

### **SUPPLEMENTARY INFORMATION** 

### **Supplementary Note 1. SAMPLE STRUCTURE** 

The sample used for this work is the same as used in Refs. [34, 47, 49, 66]. The sample is grown on a semi-insulating GaAs (001) substrate. Supplementary Fig. 1 shows the layer sequence of the semiconductor structure. Growth starts with a layer of Al0 _._ 95Ga0 _._ 05As followed by a single pair of Al0 _._ 2Ga0 _._ 8As and Al0 _._ 95Ga0 _._ 05As layers, which act as a Bragg reflector in optical experiments. A 95 nm thick layer of Al0 _._ 15Ga0 _._ 85As is then grown followed by a 95 nm thick layer of Al0 _._ 15Ga0 _._ 85As doped with Si at a volume concentration of 1 _._ 0 _×_ 10<sup>18</sup> cm<sup>_−_3</sup> . The concentration of Al is kept at a low value of 0.15 in the Si doped layer, in order to avoid the formation of the deep DX centers [67–69]. The _n_ -type doped layer is followed by the electron tunnel barrier layers: first a 5 nm thick Al0 _._ 15Ga0 _._ 85As layer is grown at a reduced temperature of 560<sup>_◦_</sup> C to suppress Si segregation, followed by a 10 nm thick Al0 _._ 15Ga0 _._ 85As and then a 15 nm thick Al0 _._ 33Ga0 _._ 67As layer grown at 600<sup>_◦_</sup> C. Droplets of Aluminium are grown on the surface of the Al0 _._ 33Ga0 _._ 67As layer and are used to etch the nanoholes [70–72]. Atomic force microscopy shows typical nanoholes have a depth of _≈_ 6.5 nm and are _≈_ 70 nm in diameter [47]. A 2.1 nm thick layer of GaAs is grown to form QDs by infilling the nanoholes and additionally form the quantum well (QW) layer. Thus, the maximum height of the QDs in the growth _z_ direction is _≈_ 9 nm. The GaAs layer is followed by a 268 nm thick Al0 _._ 33Ga0 _._ 67As barrier layer. Finally, the _p_ -type contact layers doped with C are grown: a 65 nm thick layer of Al0 _._ 15Ga0 _._ 85As with a 5 _._ 0 _×_ 10<sup>18</sup> cm<sup>_−_3</sup> doping concentration, a 5 nm thick layer of Al0 _._ 15Ga0 _._ 85As with a 9 _._ 0 _×_ 10<sup>18</sup> cm<sup>_−_3</sup> concentration, and a final 10 nm thick layer of GaAs with a 5 _._ 0 _×_ 10<sup>18</sup> cm<sup>_−_3</sup> concentration. 

Next, the sample is processed into a _p-i-n_ diode structure. Mesa structures with a height of 250 nm are created by etching away the _p_ -doped layers and depositing onto the etched regions the following sequence of layers: Ni(10 nm), AuGe(150 nm), Ni(40 nm), Au(100 nm). The sample is then annealed to enable diffusion of the deposited metals down to the _n_ -doped layer to form the ohmic back contact. Depositing Ti(15 nm)/Au(100 nm) on to the _p_ -type surface of the mesa areas forms the top gate contact. QD photoluminescence (PL) is excited and collected through the top of the sample. Sample gate bias _V_ Gate is the bias of the _p_ -type top contact with respect to the grounded _n_ -type back contact. Tunneling of holes is suppressed due to the large thickness of the top Al0 _._ 33Ga0 _._ 67As layer, whereas tunnel coupling to the _n_ -type layer enables deterministic charging of the QDs with electrons by changing _V_ Gate. For this work however, we leave the QD 

2 



<!-- Start of picture text -->
10 nm GaAs:C p++<br>5 nm Al 0.15 Ga 0.85 As:C p++<br>65 nm Al0.15Ga0.85As:C p+<br>268 nm Al0.33Ga0.67As<br>2 nm GaAs QW and QDs<br>7 nm<br>8 nm Al0.33Ga0.67As<br>10 nm Al 0.15 Ga 0.85 As<br>5 nm Al 0.15 Ga 0.85 As<br>95 nm Al0.15Ga0.85As:Si<br>95 nm Al0.15Ga0.85As<br>Al 0.95 Ga 0.05 As<br>reBfrleacgtgor Al 0.20 Ga 0.80 As<br>Al 0.95 Ga 0.05 As<br>GaAs<br>v Gate<br>z<br>+<br>−<br><!-- End of picture text -->

Supplementary Figure 1. Schematic of the quantum dot sample structure. 

uncharged by applying reverse bias. 

To allow the quadrupolar components of the nuclear magnetic resonance (NMR) spectra to be resolved, the semiconductor sample used in this work is subjected to uniaxial mechanical stress. To this end, the semiconductor wafer is first cleaved into a small piece with a rectangular surface area of 0.7 mm _×_ 2.35 mm. The edges of the rectangular profile are aligned along the [110] and [1<sup>¯</sup> 10] crystallographic directions. The sample thickness along the [001] growth direction is 0.35 nm. Thus, the sample is a parallelepiped. The sample is then inserted into a home-made stress cell. This is done in such a way that the two 0.7 mm _×_ 0.35 mm surfaces of the sample are contacted to the flat titanium surfaces of the stress cell bracket. Finally, a titanium screw is directed along the 2.35 mm long edge of the sample in order to apply compressive stress [49]. 

3 



<!-- Start of picture text -->
Op�cal<br>Op�cal Pumping<br>Probe<br>Dynamical Decoupling sequence<br>Ini�aliza�on Finaliza�on<br>Popula�on Transfer NMR Popula�on Transfer t<br>VPump VProbe<br>0 e<br>0 e V0 e 0 e<br>2 2 2 2<br>↔+ 3 ↔- 1 ↔-1 ↔+ 3<br>+ 12 -3 2 -3 2 +12<br><!-- End of picture text -->

Supplementary Figure 2. Full timing diagram of pulsed dynamical decoupling experiments. 

### **Supplementary Note 2. EXPERIMENTAL TECHNIQUES** 

The sample is placed in a bath-cryostat and cooled using liquid He to _≈_ 4 _._ 2 K. An inbuilt superconducting coil is used to apply a static magnetic field _Bz_ up to 8 T along the _z_ -axis parallel to the sample growth direction [001] and the optical axis (Faraday geometry). Therefore, the applied mechanical stress is perpendicular to the field and optical axis. Optical measurements are conducted using a confocal microscopy configuration. An aspheric lens with a focal distance of 1.45 mm and NA = 0.58 is used as an objective for optical excitation of the QD and for collection of photoluminescence (PL). The excitation laser is focused into a spot with a diameter of _≈_ 1 _µ_ m. A two-stage Czerny-Turner spectrometer is used to analyze the collected PL. The light is collimated and directed to a plane diffraction grating at each stage. Upon dispersion, the light is focused by a mirror with a 1 m focal length. After the spectrometer, a pair of achromatic lens doublets transfer the spectral image onto a charge-coupled device (CCD) photo-detector with a magnification of 3.75. The changes in the spectral splitting, determined from the PL spectra of a neutral exciton _X_<sup>0</sup> , allow measurement of the hyperfine shifts _E_ hf , which is proportional to the nuclear spin polarization degree (Fig. 2a of the main text). Both the pump and probe laser pulses are formed using mechanical shutters. One more mechanical shutter is used to block the input of the spectrometer during the optical pumping. 

### **A. Optical pumping of nuclear spin polarization** 

Supplementary Fig. 2 shows the full timing diagram for the NMR measurements used in this work. In the first part of the measurement cycle dynamical nuclear spin polarization is created 

4 

by optically pumping the QD with a tunable single-mode circularly polarized diode laser. This is a well established technique and allows nuclear spin polarization greater than 50% to be reached – [48, 73 77]. The process is cyclic with three stages. First, optical excitation creates a spin polarized electron, a process enabled by the selection rules in III-V semiconductors allowing spin-polarized electron-hole pairs to be formed from the conversion of circularly polarized light. Secondly, the flipflop term of the electron-nuclear hyperfine Hamiltonian allows the electron to exchange its spin with a single nuclei. Finally, electron-hole recombination removes the flipped electron allowing another polarized electron to be created in the dot and the process repeats, building-up polarization of the ensemble of nuclei. The pump laser pulse is typically 5 s long, afterwards, a 10 ms delay is added to ensure that the mechanical shutter has fully closed. The pump power _≈_ 1 mW is three orders of magnitude greater than the ground-state PL saturation power, with typical photon energy _≈_ 5 _−_ 10 meV above the _X_<sup>0</sup> PL energy. To ensure the QD is unoccupied during the pump process, a large reverse bias is applied _V_ Gate = _−_ 2 _._ 4 V. 

### **B. Nuclear magnetic resonance (NMR)** 

A copper wire coil is used to generate the magnetic field _Bx ⊥ z_ needed to carry out NMR experiments. The coil is positioned _≈_ 0 _._ 5 mm from the QD sample. The coil is made of 10 turns of a 0.1 mm diameter enamelled copper wire wound on a _≈_ 0 _._ 4 mm diameter spool in 5 layers, with 2 turns in each layer. A class-AB radiofrequency (Rf) amplifier (Tomco BT01000-AlphaSA rated up to 1000 W) is used to drive the coil, fed by the output of an arbitrary waveform generator (Keysight M8190). 

The timing of NMR experiments proceeds as shown in Fig. 2. First, two Rf pulses are used to increase the NMR signal by transferring the nuclear spin population into the optimal configuration [40, 49]. Consider the case where the dot is pumped with _σ_<sup>+</sup> light leaving the _I_ z = _−_ 3 _/_ 2 nuclear spin states the most populated [66], while the _I_ z = +3 _/_ 2 states are nearly unpopulated. By maximising the population change we maximize the NMR signal. For measurements performed on the central transition the population difference between the _I_ z = _−_ 1 _/_ 2 and _I_ z = +1 _/_ 2 states needs to be maximized. To this end we apply two _π_ pulses to transfer the nuclear spin populations. First, a pulse is applied to the +1 _/_ 2 _↔_ +3 _/_ 2 transition, exchanging their populations leaving _I_ z = +1 _/_ 2 as the least populated state. Then, after a short delay, a second pulse is applied to the _−_ 3 _/_ 2 _↔−_ 1 _/_ 2 transition leaving _I_ z = _−_ 1 _/_ 2 as the most populated state. A similar process can be applied in the case one of the satellite transitions is being investigated. 

5 



<!-- Start of picture text -->
π/ 2 π π/ 2 π<br>l s e  l s e<br> 1  1<br> 2  2<br> 4  = 1 0  µ  4  = 2 0  µ<br>. 2 . 3 . 4 . 5 . 6 . 7 . 8 . 1 . 2 . 3 . 4 . 5<br>l s e a l i t u e s l e f a t o l s e a l i t u e s l e f a t o<br>µ µ<br>l ( l (<br>i g i g<br>R s R s<br>t N t N<br> d  d<br>t u t u<br><!-- End of picture text -->

Supplementary Figure 3. **a** Rabi oscillations of the nuclear spins under Rf pulse bursts of increasing amplitude with fixed pulse duration _T_ Rf = 10 _µ_ s. Increasing the pulse amplitude increases the degree of rotation of the spins. The first peak in the oscillation (solid squares, red, one pulse) corresponds to a _π_ rotation. We obtain the required amplitude of a _π_ /2 rotation from the first peak for the oscillation driven by two pulses (solid circles, blue). Additionally we conduct measurements with 4, 8 and 16 pulses to improve the accuracy of the acquired amplitudes. Only the 4 pulse measurement (solid triangles, green) is shown for clarity. **b** Same as **a** but for pulses with _T_ Rf = 20 _µ_ s. 

Next, the optically generated nuclear spin polarization needs to be converted from longitudinal polarization to transverse polarization. This is so the spins begin to decohere and the coherence time can be measured. We achieved this simply by using a single _π_ /2 Rf pulse. The phase of the pulse can be varied to allow control over the initial orientation of the nuclear spins in the _xy_ plane. Dynamical decoupling is then applied. The pulses for a given sequence are applied in a way that they are equally spaced by time _τ_ , this means that while _T_ FreeEvol is increased the time _τ_ between each pair of adjacent pulses increases uniformly. Due to hardware limitations, the minimal interpulse delay achievable is _τ ≈_ 0 _._ 3 _µ_ s. This places a lower limit on the free evolution time that could be measured for a given dynamical decoupling sequence, based on the sequences number of pulses. Finally, a _π_ /2 pulse is used to rotate the nuclei back along the _z_ axis for optical readout. Again, the phase of finalization pulse can be varied. If the phase of the finalization pulse is the same as the initialization pulse, the nuclei are rotated such that their populations are antiparrallel compared to before the initialization pulse. Comparatively, if the finalization pulse is _π_ out of phase with the initialization pulse, then the nuclear spins are aligned parallel to the orientation before initialization. All measurements use initialization and finalization pulses with _π_ phase difference, as this allows us to avoid the range of nuclear polarizations where electron-nuclear bistability [78] 

6 

accelerates the nuclear spin dynamics. 

Before optical readout we again transfer the spin populations, this allows us to multiply the NMR signal by exploiting the entire _I_ = 3 _/_ 2 Hilbert space. The process is the reverse of the process described above. First, a _π_ pulse is applied to the _−_ 3 _/_ 2 _↔−_ 1 _/_ 2 transition followed by another _π_ pulse on the +1 _/_ 2 _↔_ +3 _/_ 2 transition. The reason for this is that after application of the dynamical decoupling sequence, the remaining nuclear spin polarization is encoded in the _−_ 1 _/_ 2 _↔_ +1 _/_ 2 states. Assuming a _π_ phase difference between initial and final pulses, the _I_ z = _−_ 1 _/_ 2 state will be most populated, while the _I_ z = +1 _/_ 2 state will be least populated. The reverse population transfer means the _I_ z = _−_ 3 _/_ 2 and _I_ z = +3 _/_ 2 become the most and least populated states respectively, encoding the NMR signal into the _I_ z = _±_ 3 _/_ 2 subspace, approximately tripling the NMR signal measured optically. During NMR a bias of _V_ Gate = _−_ 1 _._ 5 V is applied to the sample to ensure that there are no resident electrons. 

### **C. Rf pulse calibration** 

Dynamical decoupling requires that precise rotations of the nuclei are performed. For some of the measurements in this work, as many as 2400 Rf pulses were applied to drive rotations of the nuclear spins, any inaccuracy in the rotations would therefore worsen the coherence of the nuclear spin polarization. To this end, we performed Rabi oscillation measurements to calibrate the _π_ and _π_ /2 Rf pulses. The Rf pulses are produced by modulating the Rf carrier with a raised cosine envelope function of total duration _T_ Rf between the two zero-amplitude points. For a desired _T_ Rf , the amplitude of the applied pulses was increased and the resulting NMR signal measured, Supplementary Fig. 3a shows the Rabi oscillations observed for _T_ Rf = 10 _µ_ s pulse duration. From this the power required for a _π_ pulse is obtained by locating the first peak in the oscillation. The power needed for a _π_ /2 Rf pulse is found by applying two separate pulses. Here, the first peak now gives the amplitude needed for a _π_ /2 pulse, as this corresponds to a total rotation of nuclei by _π_ meaning each of the two pulses will have rotated the nuclei by _π_ /2. Finally, to improve the accuracy of these calibrations we conducted measurements with an increasing number of pulses: 4, 8, and 16. The Rabi oscillations were collectively fitted to obtain the power scaling factors. Supplementary Fig. 3b shows the same calibrations but for _T_ Rf = 20 _µ_ s pulses. 

7 



<!-- Start of picture text -->
���������<br>�  p<br>. 0 . 1<br>i n g t i m ,   (<br>t s<br>i m<br> µ<br>R e<br>�<br>l ,<br>i g d i n N<br>R S<br>4 s u<br>. 0<br> = 0<br><!-- End of picture text -->

Supplementary Figure 4. Calibration measurement for the optical probe duration. Hyperfine shift measured under different duration optical probing after being polarized with _σ_<sup>+</sup> optical pumping. The time ( _T_ Probe) used for coherence measurements and nuclear spin decoupling is shown by the dashed line. Measurement was conducted with external magnetic field _B_ z = 2 _._ 39 T. 

### **D. Optical probing of nuclear spins** 

Measurement of the nuclear spin polarization is conducted using optical probing. The probe power and the bias during the probe ( _V_ Gate = +0 _._ 9 V) are chosen to maximize (saturate) the intensity of the ground neutral exciton (X<sup>0</sup> ) state PL. There is a 10 ms delay between the bias switching and the mechanical shutter activating, forming the probe pulse. This delay ensures that the charge state of the quantum dot is in its steady state when the optical probe pulse is applied. An example PL spectra is shown in Fig. 2a of the main text. The PL is generated by recombination of the electron-hole pairs. Under optical excitation the spin of the electron is random, meaning light is emitted from both bright exciton spin states. The PL is accumulated over millisecond timescales allowing both exciton states to be observed in the same PL spectrum. The applied magnetic field splits the two PL lines, these can be further shifted by the nuclear polarization via the hyperfine interaction. The shifts can be seen when the nuclei are polarized with different circularly polarized light. Injection of optically excited electrons into the dot leads to spin flip-flops between the electron spin and nuclei which will progressively depolarize the nuclei. A probe pulse duration measurement 

8 

is shown in Supplementary Fig. 4 for external magnetic field of _B_ z = 2 _._ 39 T. As the probe time is increased the nuclear polarization decreases, seen in the reduction of PL splitting. Similar results are observed in a wide range of magnetic fields _B_ z = 1 _−_ 8 T. Based on such calibration results we use a probe time of _T_ Probe = 0 _._ 04 s maximizing the collected signal from the optical excitation without a significant loss in nuclear spin polarization due to spin flip-flops. 

### **Supplementary Note 3. ADDITIONAL EXPERIMENTAL RESULTS** 

### **A. Optimal Rf pulse duration in dynamical decoupling** 

Ideally, nuclear spin rotations would be carried out instantaneously, minimising decoherence due to unwanted evolution of the nuclear spin ensemble during the rotation. As we are limited to using finite time Rf pulses, one may expect that shorter _T_ Rf times would yield better coherence storage performance. Yet, as discussed in the main text, we find that when using short _T_ Rf = 10 _µ_ s pulses we see a drop in performance for high pulse number sequences ( _≈_ 640 pulses) compared to when longer _T_ Rf = 20 _µ_ s pulses are used. Here were present experimental results that reveal these counterintuitive observations. Nuclear spin decoherence measurements, such as shown in Fig. 2c of the main text, have been conducted both with _T_ Rf = 10 _µ_ s and _T_ Rf = 20 _µ_ s on the _I_ z = _±_ 1 _/_ 2 nuclear spin subspace. In each such measurement, the total free evolution time _T_ FreeEvol is varied while keeping a constant number of pulses in the dynamical decoupling sequence. The resulting dependence of the spin echo NMR signal is fitted with a stretched exponential function of _T_ FreeEvol. From the fit we derive the NMR signal in the limit of short free evolution _T_ FreeEvol _→_ 0 and the characteristic nuclear spin coherence time _T_ 2. These results are shown in Figs. 5a and b, respectively. The values are shown as a function of the total number of pulses in Hahn echo (1 pulse), CHASE-5 (5 pulses), CHASE-10 (10 pulses), CHASE-20 (20 pulses), and a varying number of CHASE-40 cycles (all points with _≥_ 40 pulses). The results are shown for two different orientations of the initial nuclear spin polarization in the equatorial plane of the rotating frame (initialization pulse phase _ϕ_ = 0 and _ϕ_ = _π/_ 2). 

From Supplementary Fig. 5a we find that for short pulse sequences (≲ 100 pulses) the shortevolution NMR signal is somewhat better (larger) for short pulses ( _T_ Rf = 10 _µ_ s, squares), as these are better approximation to instantaneous spin Hamiltonian transformations than the _T_ Rf = 20 _µ_ s pulses (circles) pulses. However, for longer sequences (640 pulses) the short-evolution spin echo under short pulses ( _T_ Rf = 10 _µ_ s) becomes worse than under long pulses ( _T_ Rf = 20 _µ_ s). 

9 



<!-- Start of picture text -->
I n i t i a l i z t i o n p e a d  f<br>�  = 0 ,   = 1 0  µ<br>�  =  π/ 2 ,   = 1 0  µ ���������<br>�  = 0 ,   = 2 0  µ � / 2  ↔ / 2<br>�  =  π/ 2 ,   = 2 0  µ<br>r o f d i c l d l i n g p l s<br>µ<br>t f r<br>0 (<br>�<br>t s<br>l a<br>i g n<br>R s t i o<br>l u<br>i n c<br>,<br>r s<br>t i m<br>l e<br><!-- End of picture text -->

Supplementary Figure 5. **a** NMR signal (spin echo amplitude) at short free evolution time _T_ FreeEvol _→_ 0 plotted as a function of the number of Rf pulses in the dynamical decoupling sequence. The data is shown for Rf pulse durations of _T_ Rf = 10 _µ_ s (squares) and _T_ Rf = 20 _µ_ s (circles). Measurements are conducted with initial nuclear polarization along the _−y_ axis (solid symbols, initialization Rf pulse phase _ϕ_ = 0) and the _x_ axis ( _ϕ_ = _π/_ 2, open symbols) of the rotating frame. **b** Dependence of the nuclear spin coherence time _T_ 2 on the number of Rf pulses. 

Supplementary Fig. 5b shows that the coherence time _T_ 2, which is a measure of decoherence during free evolution, is nearly independent of the Rf pulse duration _T_ Rf . This allows us to conclude that the reduced short-evolution NMR signal (i.e. reduced fidelity of coherence storage) at _T_ Rf = 10 _µ_ s is a result of undesired spin evolution during the pulses, rather than pure decoherence during free evolution between the pulses. In particular, we attribute the reduced performance of the _T_ Rf = 10 _µ_ s pulses to parasitic leakage of the stored state to the two nuclear satellite transitions, owing to the broader spectral profile of the pulses, as shown by the dashed lines in Fig. 1a of the main text. 

10 



<!-- Start of picture text -->
���������<br>� / 2  ↔ � / 2<br> = 2 0  µ  1 c l e C<br> 2 c l e s C<br>1 c l c e C<br>�  = 0 ( l s<br>�  =  π/ 2 ( l s<br>2 c l e s o f C<br>�  = 0 ( l s<br>�  =  π/ 2 ( l s<br>. 1 π/ 2<br>i n e l u t i o n t i m ,   ( e o f i n i t i a l i z t i o n R f p l s ,  �<br>t f r µ<br>0 (<br>�<br>t s<br>l a<br> µ<br>l  i g n<br>i g R s t i ol u<br>R s<br>t N<br> d<br>t u<br>i n c<br>,<br>r s<br>t i m<br>l e<br><!-- End of picture text -->

Supplementary Figure 6. **a** Decoherence measured on the _I_ z = ( _−_ 3 _/_ 2 _, −_ 1 _/_ 2) nuclear spin subspace. Two cycles of CHASE-20 (squares) are compared to a single CHASE-40 cycle (circles) both when initializing the nuclear spin polarization along the _−y_ axis of the rotating frame (solid symbols, _ϕ_ = 0 Rf pulse phase) and along the _x_ axis (open symbols, _ϕ_ = _π/_ 2). **b** NMR signal (spin echo amplitude) at short free evolution time _T_ FreeEvol _→_ 0 plotted as a function of the phase _ϕ_ of the initialization Rf pulse for two cycles of CHASE-20 (squares) and one cycle of CHASE-40 (circles). The values are obtained from fitting the decay curves in ( **a** ). **c** Same as ( **b** ) but for nuclear spin decoherence time T2. 

### **B. Comparison of pulsed spin locking in CHASE-20 and CHASE-40 decoupling sequences** 

Pulsed spin locking is observed in various dynamical decoupling techniques. The simplest example is the Carr-Purcell sequence, where a train of _π_ Rf pulses of the same phase is applied. The spin locking can be understood intuitively as an effective transverse magnetic field in the rotating frame that arises from repeated rotations of the nuclear spins around a preferential equatorial axis of the rotating frame [43]. If the coherent nuclear polarization, created by the initial _π/_ 2 Rf pulse, is parallel to this effective transverse magnetic field, the nuclear state becomes “locked” and its decay is suppressed. In other words, the transverse ( _T_ 2) coherence decay is replaced by a decay that is akin to longitudinal ( _T_ 1) relaxation in the rotating frame. By contrast, the initial state polarized orthogonal to the effective locking field undergoes precession and accelerated decoherence. In the case of the CHASE-10 cycle, shown in Fig. 1b of the main text, the two _π_ rotations (labeled +x<sup>2</sup> and _−_ x<sup>2</sup> ) create a preferential direction in the rotating frame, whereas the four _π/_ 2 rotation pulses labeled as _±_ x are balanced by four _±_ y Rf pulses rotating the spins around the orthogonal axis in 

11 

the rotating frame. 

The CHASE-40 sequence is designed to be resilient against pulsed spin locking, by combining four CHASE-10 subsequences, where the phase of all Rf pulses is stepped in each block by _π/_ 2, as shown in Fig. 1c of the main text. Here we perform direct comparison of CHASE-40 with a sequences of pulses, where such phase stepping is omitted. To this end we use two cycles of CHASE-20 sequences, where each CHASE-20 block is a combination of CHASE-10 and its mirror copy, where all Rf pulses are applied in reverse [44]. Thus, both the CHASE-40 and 2 cycles of CHASE-20 differ only by the phases of the Rf pulses. In the case of CHASE-20, all the _π_ rotations (+x<sup>2</sup> and _−_ x<sup>2</sup> ) are around the same equatorial axis of the rotating frame. 

The experiments are performed on the _I_ z = ( _−_ 3 _/_ 2 _, −_ 1 _/_ 2) subspace of the<sup>75</sup> As nuclear spins. The resulting decays of nuclear spin echo with the increasing free evolution time _T_ FreeEvol are shown in Supplementary Fig. 6a. The decay curves are fitted with stretched exponentials to derive the NMR signal in the limit of short free evolution _T_ FreeEvol _→_ 0 (shown in Supplementary Fig. 6b) and the characteristic nuclear spin coherence time _T_ 2 (shown in Supplementary Fig. 6c). In the case of CHASE-40 (squares in Supplementary Fig. 6a) the decoherence (characterized by _T_ 2 _≈_ 5 _._ 3 ms) does not depend on the direction of the initial transverse nuclear spin polarization. This is also in agreement with the data of Fig. 4 of the main text obtained for the _I_ z = _−_ 1 _/_ 2 _,_ +1 _/_ 2 nuclear spin subspace. These results confirm that CHASE-40 effectively eliminates the pulsed spin locking. 

For the two cycles of CHASE-20 (circles in Supplementary Fig. 6a) we observe a pronounced difference in decoherence, depending on the initial nuclear spin state. For the spin state polarized along the _−y_ axis of the rotating frame (solid circles, _ϕ_ = 0) the decay is slowed down ( _T_ 2 _≈_ 7 _._ 5 ms), revealing the pulsed spin locking effect. (With the convention used here, the pulse labeled as “+x” in the sequence definition of Figs. 1b, c of the main text corresponds to _ϕ_ = 0. This pulse produces Rf magnetic field along the _x_ axis of the rotating frame and initializes nuclear polarization along the _−y_ axis of the rotating frame. For the “ _−_ x” pulse the Rf phase is _ϕ_ = _π_ . The “+y” pulse corresponds to _ϕ_ = _π/_ 2 and initializes the nuclear spin state along the _x_ axis. The _±_ x<sup>2</sup> Rf pulses have the same phase as _±_ x, and so on). 

For the case of CHASE-20 decoupling with an initial nuclear spin polarization along the _x_ axis ( _ϕ_ = 0), there is a pronounced reduction both in the nuclear spin echo amplitude at short free evolution _T_ FreeEvol _→_ 0 and in _T_ 2 _≈_ 4 _._ 1 ms, characterizing decoherence during free evolution. In the context of quantum memories, this can be interpreted as the worst case scenario, which is an inevitable side effect of the pulsed spin locking. This is why elimination of spin locking, such as achieved with CHASE-40, is important for operating nuclear spins as a quantum memory, which 

12 

is generally expected to preserve an arbitrary coherent state. 

### **C. Details on Measurement of Nuclear Spin Transitions** 

The NMR Spectra of the<sup>75</sup> As nuclei used in Fig. 1a of the main text were obtained using two seperate measurment techniques. For the _−_ 1 _/_ 2 _↔_ +1 _/_ 2 central transition (blue in Fig. 1a) the spectrum was obtained from a Fourier transform of the measured free induction decay. The free induction decay was measured using _T_ Rf = 10 _µs_ . The _−_ 3 _/_ 2 _↔−_ 1 _/_ 2 and +1 _/_ 2 _↔_ +3 _/_ 2 satellite transitions (black in Fig. 1a) were measured using the inverse NMR measurement technique [79]. 

### **Supplementary Note 4. DISCUSSION OF QUANTUM MEMORY APPLICABILITY FOR QUANTUM REPEATERS** 

Quantum repeaters are a necessary component for the realization of long distance communication of quantum information. The implementation of such devices will enable the secure communication of information, paving the way for the quantum internet [5, 6, 80]. The need for quantum repeaters stems from the limitations on information transfer distance in optical fibers. Photons are superb ’flying’ qubits that can be used for long distance communication of quantum states owing to their long coherence times. Yet modern optical fibers can only be used to transmit photons for distances of _≈_ 20 _−_ 100 km due to attenuation. One solution to this problem is to transmit the quantum information via satellites, removing the issue of losses due to fiber attenuation. Such systems have been demonstrated, enabling quantum teleportation over distances of up to 1400 km, yet issues such as sensitivity to atmospheric turbulence and the requirement for direct line of sight with the satellite remain [81]. Another alternative is to use quantum repeaters, which seek to get around this limitation by splitting the full communication distance into several shorter channels connected by quantum repeater nodes, by entangling all of the nodes, entanglement swapping can then be used to transmit information between the two end nodes over distances greater than those possible by direct photon transmission [5, 6, 80, 82]. This simplified approach requires that entanglement generation occurs on every repeater node simultaneously, which significantly limits the chance of success. By using a quantum memory qubit which possess a long coherence time _T_ 2, the entangled states can be stored for time _T_ 2 allowing multiple attempts at generating entanglement. Therefore, by using time multiplexing, the chance of successful entanglement swapping can be increased [80, 83]. 

13 

The storage time of the memory required to achieve the transfer of information over a useful distance varies significantly depending on the quantum repeater protocol. In particular, the required communication time can be reduced by introducing more complexity to the system, such as multiplexing [84, 85]. Therefore the memory time needed for a _≈_ 1000 km channel can vary from 1000 s down to 1 ms [5, 6, 42]. Fundamentally, the maximum distance achievable for a given memory time is tied to the speed of light, therefore memories of 1 ms are sufficient to beat direct photon transmission [5] while 5 ms is sufficient to reach distances of 1000 km, a commonly used benchmark in the literature [6]. Therefore, using this approach, we estimate that a quantum memory based on nuclear spins with _T_ M _≈_ 100 ms would be able to store a given state for long enough to send a message over a distance greater than half the Earth’s circumference, meaning it would be sufficient for world wide communication. However, photon transmission time is not the only limitation of a quantum repeater [42, 86]. Other limiting factors include: light-matter entanglement generation [31–33], state transfer to the nuclei [38, 39], entanglement swapping [25], and state measurement [87]. While all these building blocks have been demonstrated for QDs, they would all consume time, reducing the amount of time for generating entanglement. Out of the factors listed above, the generation of entanglement is the main limitation on communication distance. In the above discussion we assumed a unity fidelity of entanglement generation. In reality this is not the case and the photon transmission process needs to be repeated multiple times until the entanglement is established, which significantly limits the achievable distances for quantum repeaters [7]. For QDs, entanglement generation rates as high as 7.3 kHz have been demonstrated [25]. We can therefore estimate, using the equations and parameters reported in Ref. [7], that with the current memory storage time of _T_ M _≈_ 100 ms it should be possible to achieve quantum repeater communication distances of _≈_ 13 _._ 4 km. Assuiming a link efficiency of 0.34, as used in [7] leads to a more favorable estimate of _≈_ 39 _._ 4 km, making nuclear spin based memories competitive with the atomic ensemble systems used in Ref. [7], as well as matching communication distances achievable with direct fiber transmission of photons. 

Although current nuclear spin memory times do not yet match those achievable in certain solid state or atomic systems [13, 14, 22], the III-V semiconductor quantum dots benefit from superior optical properties such as efficient generation of single [8, 26–28] and entangled photons [29, 30], which are also required for quantum communication. QDs also benefit from the well established semiconductor fabrication techniques, offering a path for scalability. The storage times demonstrated here for nuclear spins, combined with the high optical entanglement generation rates mean that QDs should be able to compete with other existing approaches to quantum repeaters 

14 

[7, 25]. Finally, by using multiplexing or alternatively, by extending the coherence time to _T_ 2 = 1 s as discussed in the main text, it should be possible to extend the possible communication distance to 500 _−_ 1000 km, sufficient to outperform direct photon transmission and enable quantum repeater channels that, for example, connect major cities [42, 84]. 

### **Supplementary Note 5. AVERAGE HAMILTONIAN THEORY APPLIED TO DESIGN OF CHASE DYNAMICAL DECOUPLING SEQUENCES** 

### **A. Nuclear spin interactions** 

The Zeeman term accounts for the coupling of the QD nuclear spins **I** _k_ to the static magnetic field _B_ z directed along the _z_ axis. In the laboratory frame it can be written as 



where the summation goes over all individual nuclei 1 _≤ k ≤ N_ , ℏ = _h/_ (2 _π_ ) is the reduced Planck’s constant, _γk_ is the gyromagnetic ratio of the _k_ -th nuclear spin and<sup>ˆ</sup> **I** _k_ is a vector of spin operators with Cartesian components ( _I_<sup>ˆ</sup> x _,k, I_<sup>ˆ</sup> y _,k, I_<sup>ˆ</sup> z _,k_ ). The result of the Zeeman term alone is a spectrum of equidistant single-spin eigenenergies _−I_ zℏ _γkB_ z. These 2 _I_ + 1 states are also the eigenstates of the ˆ _I_ z spin projection operator with eigenvalues _I_ z satisfying _−I ≤ I_ z _≤_ + _I_ . 

The interaction of the nuclear electric quadrupolar moment with the electric field gradients is described by the term (Ch. 10 in Ref. [88]): 



where _qk_ and _ηk_ describe the magnitude and asymmetry of the electric field gradient tensor, whose principal axes are _x_<sup>_′_</sup> _y_<sup>_′_</sup> _z_<sup>_′_</sup> . The strain is inhomogeneous within the QD volume, so that _qk_ and _ηk_ vary between the individual nuclei. The axes _x_<sup>_′_</sup> _y_<sup>_′_</sup> _z_<sup>_′_</sup> are different for each nucleus and generally do not coincide with crystallographic axes or magnetic field direction. For the as-grown (unstrained) GaAs/AlGaAs QDs the typical quadrupolar shift is around _|qk|/h ≈_ 24 kHz for<sup>75</sup> As [47, 73]. The full width at half maximum of the _|qk|/h_ distribution is _≈_ 14 kHz. For a small fraction of arsenic nuclei, adjacent to aluminium atoms, the shifts are as large as _|qk|/h ≈_ 200 kHz [34]. In the strained sample structure, _qk_ are dominated by the extrinsic uniaxial stress, with the typical values _|qk|/h ≈_ 250 kHz for<sup>75</sup> As in the present work. All experiments are conducted under sufficiently strong magnetic fields, where _|_ ℏ _γkB_ z _| ≫|qk|_ and quadrupolar effects can be treated perturbatively. 

15 

In this perturbative regime, the main effect of the quadrupolar shifts is the anharmonicity of the nuclear spin eigenenergies and the resulting quadrupolar NMR multiplet of 2 _I_ magnetic-dipole transitions, split by _ν_ Q _≈ qk/h_ . The _I_ z = _±_ 1 _/_ 2 projection states of a half-integer nuclear spin are influenced by quadrupolar effects only in the second order. These second order shifts scale as _∝ ν_<sup>2where</sup><sup>_ν_N=</sup><sup>_γB_z</sup><sup>_/_(2</sup><sup>_π_)isthenuclearspinLarmorfrequency.</sup> Q<sup>_/ν_N,</sup> 

Since we apply dynamical decoupling only to the two-level subspaces of the spin 3/2 fourlevel Hilbert space, we can use the standard rotating frame representation. For the _I_ z = _±_ 1 _/_ 2 subspace the reference frequency of the frame is set to the Larmor frequency _ν_ N, while for the satellite subspaces the reference frequency is set to _ν_ N _± ν_ Q to match the NMR frequency of the corresponding satellite transition. The rotating frame transformation in the following effective Zeeman Hamiltonian term 



where ∆ _νk_ is the resonance offset of the _k_ th nucleus. In the case of the _I_ z = _±_ 1 _/_ 2 spin subspace, ∆ _νk_ represents the inhomogeneous second order quadrupolar shifts, which are within ≲ 1 kHz. For the _I_ z = ( _−_ 3 _/_ 2 _, −_ 1 _/_ 2) satellite transition subspace the set of ∆ _νk_ describes the distribution of the first order quadrupolar shifts which arise from inhomogeneous strain within the QD volume and range from tens to hundreds of kHz for the individual<sup>75</sup> As nuclei. 

Direct interaction between the nuclei is described by the dipole-dipole Hamiltonian: 



Here, _µ_ 0 = 4 _π ×_ 10<sup>_−_7</sup> N A<sup>_−_2</sup> is the magnetic constant and _rj,k_ denotes the length of the vector, which forms an angle _θ_ with the _z_ axis and connects the two spins _j_ and _k_ . The Hamiltonian of Supplementary Eq. S4 has been truncated to eliminate all spin non-conserving terms – this is justified for static magnetic field exceeding ≳ 1 mT. The spin-spin interaction constants can be written in frequency units _νjk_ = _bj,k/h_ . The typical magnitude of the interaction constants for the nearby nuclei in GaAs is max _|νjk| ≈_ 100 Hz. Consequently, the typical timescales of the decoherence driven by the many-body dipole-dipole interactions are on the order of _T_ 2 _≈_ 1 ms. The dipole-dipole interaction does not change its form under rotating frame transformation. 

16 

### **B. Average Hamiltonian theory** 

The basics of average Hamiltonian theory can be found in relevant textbooks [52]. Here we briefly outline the key points. The effect of the Rf pulses can be viewed as transformation of the many-body nuclear spin Hamiltonian. In the limit of short and strong Rf pulses, we can treat the Hamiltonian in a toggling reference frame as a piece-wise function of time, which remains constant in between the Rf pulses. After the first pulse, the Hamiltonian can be written as: 



where _H_ 0 = _H_ Z<sup>_′_</sup> _,_ N<sup>+</sup><sup>_H_DDistheinitialHamiltonianintherotatingframeand</sup><sup>_P_1istheunitary</sup> transformation operator. After the second and third Rf pulses, the Hamiltonian is: 





and so on for the subsequent pulses. The evolution of the spin ensemble can in principle be calculated using the Hamiltonians, such as in equations S5, S7, to derive the unitary propagators in each time segment. However, for long pulse sequences this quickly becomes impractical. Instead, we want to find the propagator over the entire pulse sequence cycle _T_ Cycle 



where _H_ eff is some effective Hamiltonian describing spin interactions in the toggling frame over the pulse sequence cycle. Such an effective Hamiltonian can indeed be found in the form of a Magnus expansion 



where the first terms of the expansion are 



17 

The _H_<sup>(0)</sup> term is the average Hamiltonian over the pulse sequence cycle. In all CHASE sequences it is eliminated _H_<sup>(0)</sup> = 0 in the limit of short Rf control pulses _T_ RF _→_ 0. For the term _H_<sup>(</sup><sup>_n_)</sup> , the integration volume scales as _∝ T_ Cycle<sup>_n_+1.Thus,aslongas</sup><sup>_H_(0)=0,onecanensuretheconvergence</sup> of the effective Hamiltonian to zero _H_ eff _→_ 0 in the limit of a short cycle _T_ Cycle _→_ 0 (i.e. in the limit of fast dynamical decoupling). This is the main goal of the time-suspension dynamical decoupling. As a general rule, one seeks to eliminate the lowest order terms in the expansion, in order to achieve faster convergence of the effective Hamiltonian. 

### **C. Average Hamiltonians of the CHASE cycles** 

We have calculated average Hamiltonian terms of the CHASE sequences up to the second order in Magnus expansion, inclusive. We take into account the finite (nonzero duration, _T_ Rf _>_ 0) Rf pulses, which represent the time segments within the sequence cycle where the toggling frame Hamiltonian depends explicitly on time. For simplicity, we only treat Rf pulses with rectangular envelope function. Although this is different from the raised cosine pulses used in experiment, the rectangular pulses are sufficient to derive the main effect of the finite control pulses on the average Hamiltonian terms. 

We start with the CHASE-10 sequence cycle. The leading term appears in the average Hamiltonian _H_<sup>(0)</sup> under finite pulses _T_ Rf _>_ 0. This Hamiltonian term has the form of a dipole-dipole interaction (Equation S4) but with an effective quantization axis along the _y_ direction (i.e. 3 _I_<sup>ˆ</sup> z _,jI_<sup>ˆ</sup> z _,k_ is replaced with 3 _I_<sup>ˆ</sup> y _,jI_<sup>ˆ</sup> y _,k_ ): 



This interaction causes preferential spin locking of the nuclear spin states polarized along the _y_ axis of the rotating frame. There are also non-zero first and second order terms in the Magnus expansion of the CHASE-10 effective Hamiltonian. The exact expressions can be derived, but are bulky. These higher order terms can be neglected, since they appear only for finite Rf pulses _T_ Rf _>_ 0 and are dominated by the zero order term _H_<sup>(0)</sup> in the practically useful limit of a short cycle time _T_ Cycle. 

The expression for the dominant zero order term of CHASE-20 is twice that of CHASE-10 (Eq. S13). However, since _T_ Cycle appears in denominator of Eq. S13 and is twice longer for CHASE20, the resulting zero order average Hamiltonian is the same as for CHASE-10. CHASE-20 is a symmetrised version of CHASE-10, i.e. it consists of a CHASE-10 subcycle and second CHASE-10 

18 

subcycle where all pulses are applied in reverse order. Symmetrisation leads to cancellation of the first order Magnus term, as well as all other terms with odd orders. 

We now consider CHASE-40, the new sequence implemented in this work. The zero order (average) Hamiltonian term appears only under finite pulses _T_ Rf _>_ 0 and has the following form 



Compared to Eq. S13, there is an additional factor of 2, but _T_ Cycle in the denominator is 4 times larger. Thus the _H_ CHASE<sup>(0)</sup> _−_ 40<sup>termistwicesmallerinmagnitudecomparedto</sup><sup>_H_</sup> CHASE<sup>(0)</sup> _−_ 10<sup>.More-</sup> over, the symmetry axis of _H_ CHASE<sup>(0)</sup> _−_ 40<sup>coincideswiththeexternalmagneticfield(</sup><sup>_z_axis).Thus,</sup> there is no preferential direction in the equatorial plane of the rotating frame, explaining the absence of spin locking. 

CHASE-40 is not symmetric, so the first order Magnus term is not canceled. However, for all physically relevant parameters the first order term is found to be dominated, either by the zero order term (at short _T_ Cycle) or by the second order term discussed below (for long _T_ Cycle). The small first order term is not a major issue since it can be easily eliminated with an 80-pulse symmetrised supercycle [52, 63]. 

The second order term of CHASE-40 is present even for ideal Rf pulses _T_ Rf _→_ 0. Thus we only consider this limit of delta-pulses and ignore all the corrections arising from finite pulses _T_ Rf _>_ 0. Even then, the expression for the second order term of CHASE-40 is rather bulky. There are different types of contributions. In particular there are the so called cross terms which appear only in presence of both the resonance offset of the individual spins (∆ _νk_ = 0) and the dipoledipole interactions between the spins ( _νjk_ = 0). These cross terms play an important role for the _I_ z = ( _−_ 3 _/_ 2 _, −_ 1 _/_ 2) spin subspace subject to a considerable first order quadrupolar broadening, leading to ∆ _νk_ on the order of tens of kHz. For the homogeneous _I_ z = _±_ 1 _/_ 2 subspace, affected only by the second order quadrupolar shifts, the resonance offsets ∆ _νk_ , and hence the cross term in _H_ CHASE<sup>(2)</sup> _−_ 40<sup>,canbemadearbitrarilysmall,forexamplebyincreasingthestaticmagneticfield,</sup> which increases the nuclear Larmor frequency _ν_ N. But even in the absence of any resonance offsets ∆ _νk_ = 0, there remains a second order Magnus term of the following form 



This term has a form of an effective dipolar coupling between spins _i_ and _j_ , summed over all unique pairs _i < j_ . Such interaction can arise from the direct dipole-dipole interaction of spins _i_ and _j_ in 

19 

presence of a resonance offset for at least one of the spins from the pair (the 8 _νij_ (∆ _νi_<sup>2+ ∆</sup><sup>_νi_∆</sup><sup>_νj_+</sup> ∆ _νj_<sup>2) term).However,the interaction remains even if all ∆</sup><sup>_νk_= 0,but requires dipolar coupling to</sup> some third spin _k_ . Such interaction can be interpreted as a three particle effect, where the effective interaction of spins _i_ and _j_ is mediated by all other spins _k_ = _i, j_ . There are some further second order terms that appear only under non-zero resonance offsets, but these are small and are omitted in Eq. S15. 

The _H_ CHASE<sup>(2)</sup> _−_ 40<sup>term of Eq. S15 dominates the residual toggling-frame Hamiltonian of CHASE-</sup> 40 in the limit of large _T_ Cycle. It is responsible for the quadratic growth of the decoherence rate _T_ M<sup>_−_1</sup> with increasing _T_ Cycle at large _T_ Cycle ≳ 2 ms, as observed in Fig. 3e of the main text for the measurement on the CT subspace _I_ z = _±_ 1 _/_ 2. The zero order term _H_ CHASE<sup>(0)</sup> _−_ 40<sup>(Eq.S14)is</sup> negligible at large _T_ Cycle due to the small ratio _T_ Rf _/T_ Cycle, but becomes dominant in the limit of fast dynamical decoupling (when most of the sequence cycle is taken up by the control pulses, corresponding to _T_ Rf _/T_ Cycle _≈_ 1 _/_ 40). The zero order term _H_<sup>(0)</sup> is responsible for the growth of the decoherence rate _T_ M<sup>_−_1</sup> with reducing _T_ Cycle at small _T_ Cycle ≳ 2 ms, as observed in Fig. 3e of the main text for the measurement on the CT subspace _I_ z = _±_ 1 _/_ 2. The slowest decoherence (the longest spin memory time _T_ M) is achieved when the contributions of the zero and second order terms are comparable. This observation allows us to estimate the maximum _T_ M that would be achieved if the effect of finite pulses was eliminated [51, 63]. Assuming the second order term would be unaffected, we can extrapolate the measured power-law dependence of _T_ M on _T_ Cycle at large _T_ Cycle ≳ 2 ms into the range of small _T_ Cycle. This yields an expected _T_ M _≈_ 1 s for the shortest possible _T_ Cycle = 0 _._ 8 ms of a CHASE-40 cycle at _T_ RF = 20 _µ_ s used in this work. This prediction shows that another order of mangitude improvement in the quantum memory storage time might be within reach with the existing material parameters (such as strain) and using only pulse sequence design techniques [51, 63]. 

Even once the effective Hamiltonian (Eq. S9) is known, finding the spin dynamics is still a difficult problem. Formally, the relaxation function of the transverse nuclear spin polarization can be written as an infinite power series over time, where the coefficients are the moments of the NMR spectral lineshape (Ch. 6 in [89]). In practice, only the second ( _M_ 2) and the fourth ( _M_ 4) moments can be calculated [90], making the power series rather inaccurate. It is more practical to approximate the lineshape with a function, such as Gaussian, and use the second moment _M_ 2 as a linewidth parameter. The approximate coherent memory time can then be found as 



20 

For nuclear spin polarization along the _x_ axis of the rotating frame, the second moment can be caclualted as 



The second moments can be calculated for an arbitrary orientation of the nuclear spin polarization by substituting the corresponding spin operators (e.g. _I_<sup>ˆ</sup> y _,k_ ) in Eq. S17. 

For practical calculations, Eq. S17 is applied to a system of 3 nuclear spins, assuming the same dipolar coupling _ν_ DD between each spin pair, and the resonance offsets of 0 _,_ +∆ _ν, −_ ∆ _ν_ . The effective Hamiltonians are calculated for free induction decay (FID, no dynamical decoupling), Hahn echo (single _π_ refocusing pulse), and CHASE-40, and are substituted into Eqns. S16, S17 to derive the spin memory times. The values for FID and Hahn echo are equated to the measured _T_ 2 values (the difference between _T_ 2 and _T_ M is negligible if there is at most one refocusing pulse). This allows the coupling parameters _ν_ DD and ∆ _ν_ to be extracted and then used to calculate the spin memory time _T_ M for the CHASE-40 sequence. The resulting _T_ M<sup>CHASE</sup><sup>_−_40</sup> is shown by the dashed lines as a function of _T_ Cycle in Fig. 3e of the main text and is discussed therein. 

### **Supplementary Note 6. NUMERICAL MODELING OF NUCLEAR SPIN DECOHERENCE AND DYNAMICAL DECOUPLING** 

We perform exact numerical modeling on an ensemble of _N_ spin-1/2 nuclei coupled through dipole-dipole interactions (Supplementary Eq. S4). The Zeeman effect of the strong static magnetic field is eliminated through rotating frame transformation. This leaves the Zeeman offset Hamiltonian (Supplementary Eq. S3), where ∆ _νk_ is the resonance frequency shift of the _k_ -th nucleus, which includes the inhomogeneous nuclear qaudrupolar effects and chemical shifts. 

During the Rf pulses, the time-dependent Hamiltonian is added: 



where the summation goes over all nuclei, _ν_ 1( _t_ ) is the slowly-varying Rf pulse envelope, and _ϕ_ describes the phase of the Rf carrier and the corresponding orientation of the transverse magnetic field in the equatorial plane of the rotating frame. The envelope function has a raised cosine profile _ν_ 1( _t_ ) _∝_ (1 _−_ cos(2 _π_ ( _t − t_ 0) _/T_ Rf )) _/_ 2, where _t_ 0 is the starting time of the Rf pulse burst. 

Most of the numerical modeling is carried out for a system of _N_ = 12<sup>75</sup> As nuclear spins. The 

21 

_{x, y, z}_ coordinates of the nuclei in units of nm are as follows: 



The unitary evolution of the system is simulated through numerical propagation of the Schr¨odinger equation from an initial wave function state _ψ_ Init. The computation is carried out using the software package Wolfram Mathematica 13.2 and the Python QuTiP 4.7.3 package [91]. We chose _ψ_ Init as eigenstates of the time-independent Hamiltonian, which is a sum of Supplementary Eq. S4 and Supplementary Eq. S3. We typically use 16 different initial states, spanning the whole range of the total spin _z_ projections from _−N/_ 2 to + _N/_ 2. The same initial states are used through when sweeping the parameters of the Rf pulse sequence. Once the spin evolution is calculated for a particular Rf pulse sequence, we use the final wavefunction _ψ_ Fin to calculate the final nuclear spin polarization _I_ z _,_ Fin = _⟨ψ_ Fin _|_<sup>�</sup><sup>_N_</sup> _k_ =1<sup>_I_ˆz</sup><sup>_,k|ψ_Fin</sup><sup>_⟩_.Eachfinalpolarizationvalueisnormalizedbythesign</sup> of the initial polarization _I_ z _,_ Init, and these normalized values are then averaged over all the initial states _ψ_ Init. Such averaging over multiple initial states helps to eliminate the oscillations that arise due to the small number of spins _N_ in the model. This averaging also mimics the experimental conditions, where the initial optically-induced nuclear polarization is subject to fluctuations due to fluctuations and drifts of various experimental parameters (e.g. optical pump power). 

When modeling the nuclear spin dynamics of the homogeneous _I_ z = _±_ 1 _/_ 2 subspace we set all resonance offsets to be zero ∆ _νk_ = 0. For the _I_ z = ( _−_ 3 _/_ 2 _, −_ 1 _/_ 2) satellite transition subspace we model the resonance offset of each nuclear spin _k_ as ∆ _νk_ = ∆ _ν_ 0( _k −_ 1) + N(0 _,_ 0 _._ 2∆ _ν_ 0 _/_ (2 _√_ 2 ln 2)), where N( _µ, σ_ ) stands for a normal distribution with the mean _µ_ and standard deviation _σ_ . This 

22 

model ensures that the resonance frequency of each nucleus is detuned from the nearest frequency of another nucleus by ∆ _ν_ 0, on average. Each resonance shift is randomly varied (by a _≈_ 20% fraction of ∆ _ν_ 0) to avoid periodic recurrences and oscillations. Once the set of randomized ∆ _νk_ is generated, it is fixed and used throughout the different modeling runs. We have used three sets with ∆ _ν_ 0 = 0 _._ 8 kHz, ∆ _ν_ 0 = 1 _._ 2 kHz, and ∆ _ν_ 0 = 1 _._ 6 kHz. The calculated final nuclear spin polarizations _I_ z _,_ Fin are averaged over these three sets, once again to combat the oscillations that arise from the small number of spins _N_ in the model. 

The numerical modeling closely follows the experiments: the total free evolution time _T_ FreeEvol and the number of cycles _n_ Cycles of the dynamical decoupling sequence are varied, to calculate the final nuclear spin polarization _I_ z _,_ Fin, averaged over initial states and resonance offsets as described above. The dependencies on _T_ FreeEvol yield decay curves that are similar to the experimental curves shown in Fig. 2c of the main text. Alternatively, the same data can be plotted as a function of the total evolution time _T_ EvolTot and the decoupling sequence period _T_ Cycle, such as shown in Figs. 3c, d of the main text. The numerically modeled values of the final nuclear polarization _I_ z _,_ Fin shown in Figs. 3c, d of the main text are normalized by the initial nuclear polarization _I_ z _,_ Init averaged over all the initial states. This way, the normalized values are limited to the [ _−_ 1 _,_ +1] range, with +1 corresponding to no decay of the nuclear spin polarization (i.e. complete preservation through dynamical decoupling). The values close to 0 can be interpreted as complete decoherence, whereas the negative values of the normalized nuclear spin echo amplitude are a sign of recurrences in the dynamics of a small nuclear spin ensemble. The corresponding experimental data, shown in Figs. 3a, b of the main text, is also normalized, but using the amplitude of the simple Hahn echo decoupling measured at short _T_ FreeEvol, which approximates the initial nuclear spin polarization with good accuracy. 

- [66] Millington-Hotze, P. _et al._ Approaching a fully-polarized state of nuclear spins in a solid. _Nat. Commun._ **15** , 985 (2024). 

- [67] Oshiyama, A. & Ohnishi, S. DX center: Crossover of deep and shallow states in Si-Al _x_ Ga1 _−x_ As. _Phys. Rev. B_ **33** , 4320–4323 (1986). 

- [68] Mooney, P. M. Deep donor levels (DX centers) in III-V semiconductors. _J. Appl. Phys._ **67** , R1–R26 (1990). 

- [69] Zhai, L. _et al._ Low-noise GaAs quantum dots for quantum photonics. _Nat. Commun._ **11** , 4745 (2020). 

- [70] Heyn, C. _et al._ Highly uniform and strain-free GaAs quantum dots fabricated by filling of self-assembled 

23 

nanoholes. _Appl. Phys. Lett._ **94** , 183113 (2009). 

- [71] Atkinson, P., Zallo, E. & Schmidt, O. G. Independent wavelength and density control of uniform GaAs/AlGaAs quantum dots grown by infilling self-assembled nanoholes. _J. Appl. Phys._ **112** , 4745 (2012). 

- [72] Huo, Y. H., Rastelli, A. & Schmidt, O. G. Ultra-small excitonic fine structure splitting in highly symmetric quantum dots on GaAs (001) substrate. _Appl. Phys. Lett._ **102** , 152105 (2013). 

- [73] Ulhaq, A. _et al._ Vanishing electron g factor and long-lived nuclear spin polarization in weakly strained nanohole-filled GaAs/AlGaAs quantum dots. _Phys. Rev. B_ **93** , 165306 (2016). 

- [74] Gammon, D. _et al._ Electron and nuclear spin interactions in the optical spectra of single GaAs quantum dots. _Phys. Rev. Lett._ **86** , 5176–5179 (2001). 

- [75] Eble, B. _et al._ Dynamic nuclear polarization of a single charge-tunable InAs/GaAs quantum dot. _Phys. Rev. B_ **74** , 081306 (2006). 

- [76] Skiba-Szymanska, J. _et al._ Overhauser effect in individual InP/Ga _x_ In1 _−x_ P dots. _Phys. Rev. B_ **77** , 165338 (2008). 

- [77] Ragunathan, G. _et al._ Direct measurement of hyperfine shifts and radio frequency manipulation of nuclear spins in individual CdTe/ZnTe quantum dots. _Phys. Rev. Lett._ **122** , 096801 (2019). 

- [78] Braun, P.-F. _et al._ Bistability of the nuclear polarization created through optical pumping in In1 _−x_ Ga _x_ As quantum dots. _Phys. Rev. B_ **74** , 245306 (2006). 

- [79] Chekhovich, E. A. _et al._ Structural analysis of strained quantum dots using nuclear magnetic resonance. _Nat. Nanotechnol._ **7** , 646–650 (2012). 

- [80] Azuma, K. _et al._ Quantum repeaters: From quantum networks to the quantum internet. _Rev. Mod. Phys._ **95** , 045006 (2023). 

- [81] Ren, J.-G. _et al._ Ground-to-satellite quantum teleportation. _Nature_ **549** , 70–73 (2017). 

- [82] Briegel, H.-J., D¨ur, W., Cirac, J. I. & Zoller, P. Quantum repeaters: The role of imperfect local operations in quantum communication. _Phys. Rev. Lett._ **81** , 5932–5935 (1998). 

- [83] Duan, L.-M., Lukin, M. D., Cirac, J. I. & Zoller, P. Long-distance quantum communication with atomic ensembles and linear optics. _Nature_ **414** , 413–418 (2001). 

- [84] Collins, O. A., Jenkins, S. D., Kuzmich, A. & Kennedy, T. A. B. Multiplexed memory-insensitive quantum repeaters. _Phys. Rev. Lett._ **98** , 060502 (2007). 

- [85] Jiang, L., Taylor, J. M. & Lukin, M. D. Fast and robust approach to long-distance quantum communication with atomic ensembles. _Phys. Rev. A_ **76** , 012301 (2007). 

- [86] Langenfeld, S., Thomas, P., Morin, O. & Rempe, G. Quantum repeater node demonstrating unconditionally secure key distribution. _Phys. Rev. Lett._ **126** , 230506 (2021). 

- [87] Atat¨ure, M. _et al._ Quantum-dot spin-state preparation with near-unity fidelity. _Science_ **312** , 551–553 (2006). 

- [88] Slichter, C. P. _Principles of Magnetic Resonance_ (Springer, 1990). 

- [89] Cowan, B. _Nuclear Magnetic Resonance and Relaxation_ (Cambridge University Press, 1997). 

24 

- [90] Van Vleck, J. H. The dipolar broadening of magnetic resonance lines in crystals. _Phys. Rev._ **74** , 1168–1183 (1948). 

- [91] Johansson, J., Nation, P. & Nori, F. Qutip 2: A Python framework for the dynamics of open quantum systems. _Comput. Phys. Commun._ **184** , 1234–1240 (2013). 

