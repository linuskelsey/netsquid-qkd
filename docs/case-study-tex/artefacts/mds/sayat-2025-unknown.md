# Polarisation and Temperature Dependence of – Er<sup>3+</sup> :CaWO4 Towards a Solid-State Rare-Earth Ion-Doped Quantum Memory 

**ID ID ID** Mikhael T. Sayat<sup>1,2,3∗</sup> , Trevor R. Lee<sup>1,2</sup> , Suchit Negi<sup>1,2,4</sup> , **ID ID** Naoya Iwahara<sup>5</sup> **ID** , In Cheol Seo<sup>1,6</sup> , Yung Chuen Tan<sup>1,6</sup> , Ping **ID ID ID** Koy Lam<sup>1,2,3</sup> , Young-Wook Cho<sup>1,2,3#</sup> , Jian-Rui Soh<sup>1,2,3</sup> 

1. Quantum Innovation Centre (Q.InC), Agency for Science, Technology and Research (A*STAR), 2 Fusionopolis Way, Innovis #08-03, Singapore 138634, Singapore 

2. Institute of Materials Research and Engineering (IMRE), Agency for Science Technology and Research (A*STAR), 2 Fusionopolis Way, Innovis #08-03, Singapore 138634, Republic of Singapore 

3. Centre for Quantum Technologies, National University of Singapore, 3 Science Drive 2, Singapore 117543, Singapore 

4. Department of Physics, Faculty of Science, National University of Singapore, Science Drive 3, Singapore 117551, Singapore 

5. Graduate School of Engineering, Chiba University, 1-33 Yayoi-cho, Inage-ku, Chiba-shi, Chiba 263-8522, Japan 

6. National Metrology Centre (NMC), Agency for Science, Technology and Research (A*STAR), Singapore 637145 

E-mail: `*mikhael` ~~`s`~~ `ayat@imre.a-star.edu.sg, #cho` ~~`y`~~ `oungwook@imre.a-star.edu.sg,` † `soh jian` ~~`r`~~ `ui@imre.a-star.edu.sg` 

July 2025 

Abstract. In the endeavour of developing quantum memories, Er<sup>3+</sup> :CaWO4 has emerged as a promising rare-earth ion-doped (REID) crystal platform due to its long optical coherence times and compatibility with the 1550 nm telecommunications band. This work investigates the effects of polarisation and temperature on the absorption strength, central wavelength, and linewidth of the Z1 → Y1 and Z1 → Y2 optical transitions, with light incident along the crystal a and c axes. It is found that the Z1 → Y1 transition at 1532.6 nm with the incident laser along the c-axis at cryogenic temperatures (∼ 3 K) is particularly favourable. The transition exhibits a stable central wavelength, narrower linewidth, polarisation independence, larger absorption crosssection, and lies within the C-band –attributes that make it highly suitable for quantum memory applications. 

Keywords: quantum memory, rare-earth ion-doped crystal, absorption spectra, optical transition, telecommunication 

2 

## 1. Introduction 

The recent advancement of quantum technologies has made the grand goal of a global quantum network more feasible, featuring advances in computation, communication, sensing, and fundamental physics [1, 2]. This would usher in new quantum-enhanced technologies such as repeaters and relays [3–6], computers [7–9], sensors [10, 11], and cryptography [12–15]. 

An overarching technology in this advancement is the quantum memory, which can store and retrieve information encoded in quantum states [16]. The performance of quantum memories can be quantified with three figures of merit: bandwidth – allowable – repetition rate of the information storage, efficiency probability of successfully retrieving the stored quantum state, and storage time – period of time the quantum state is retained within the quantum memory [2, 17]. A variety of platforms, with different strengths and weaknesses in these metrics, have been developed. Examples include warm vapour cells [18,19], cold atoms [20], and single atoms/ions defects [21–23]. 

A promising platform is rare-earth-ion-doped crystals, which have long storage and coherence times [24, 25], narrow optical transitions at cryogenic temperatures [26] for controlling the quantum states, and wide bandwidths [25] to accommodate for a variety of wavelengths, and thus diverse applications. Significant advancements in quantum memories using rare-earth-ion-doped crystals include the demonstration of the coherent storage of light for 1 hour [27], and observed coherence times of 6 hours [28] and 18 hours [29], in Eu<sup>3+</sup> :Y2SiO5. In addition, the storage of qubits has been demonstrated for 1.021 ms [25] and 20 ms [30]. Entangled photons have also been heralded in quantum memories with a bandwidth of 1 GHz using Nd<sup>3+</sup> :YVO4 [31], and have also been interfaced with Ti:Tm:LiNbO3 waveguides with a bandwidth of 5 GHz [32]. Proposals have also been made with host crystals doped with Kramer’s ions (Er<sup>3+</sup> , Nd<sup>3+</sup> , Yb<sup>3+</sup> ) with bandwidths greater than 10 GHz [33]. 

A propitious rare-earth-ion-doped (REID) crystal is erbium-doped calcium tungstate Er<sup>3+</sup> :CaWO4, where coherence times of 1.3 ms [34] and 23 ms [35] have been achieved using microwave resonators at cryogenic temperatures. The host crystal, calcium tungstate (CaWO4), has a low spin bath since most nuclei in the crystal have no nuclear spin, which could lead to long coherence times [35]. This is in contrast with the Y2SiO5 host crystal, which has been the conventional host for rare-earth ions, where the only stable isotope of yttrium (Y) is nuclear active. In addition, the rare earth ion dopant, erbium (Er<sup>3+</sup> ), has optical transitions near 1550 nm (C-band) suitable for communication purposes and easier integration into existing telecommunication networks [36,37]. This makes Er<sup>3+</sup> :CaWO4 an attractive and promising REID crystal for developing quantum memories. However, studies have so far have predominantly been focused on the microwave regime leaving a knowledge gap in the optical regime; in particular, the operating regime of Er<sup>3+</sup> :CaWO4 for quantum memory applications. In this paper, the effects of linear polarisation and temperature on the optical transition strengths of Er<sup>3+</sup> :CaWO4 are investigated to address the suitability of storing quantum 

3 

information. The paper is structured as follows: Section 2 presents the electronic and crystal structure of Er<sup>3+</sup> :CaWO4, Section 3 presents the experiment and method for investigating the polarisation and temperature dependence, Section 4 presents the results, Section 5 provides a discussion and future work, and Section 6 concludes the study. 

## 2. Er<sup>3+</sup> :CaWO4 

## 2.1. Crystal Structure 

The host material calcium tungstate (CaWO4) belongs to the scheelite family with a tetragonal crystal structure (space group I41/a, No. 88) [38]. In this work, the setting #1 of the I41/a space group, in which the calcium (Ca), tungsten (W), and oxygen (O) atoms reside on the 4b, 4a and 16f Wyckoff sites respectively [Fig. 1(a)], was adopted. Given that the unit cell of CaWO4 is tetragonal, the crystal a and b axes are symmetry equivalent, related by a 4-fold (41) screw axes along the crystal c axes. As such, in the subsequent discussion, it is sufficient to consider the system only along the a and c axes, without loss of generality. 

The CaWO4 single crystals used were grown via the hybrid flow-zone-Czochralski method (SurfaceNet GmbH) with an Er<sup>3+</sup> dopant concentration of 50 ppm. These erbium dopants occupy the Ca sites, as depicted in Fig. 1(a). Single-crystal x-ray diffraction with an incident x-ray wavelength of ¼=1.5406 A<sup>˚</sup> (Cu Kα) using the 6-circle diffractometer (D8 VENTURE, Bruker) was performed to determine the cell parameters of the host crystal, CaWO4, at room temperature. It was found that the crystal a and c cell parameters were 5.2398(4) A<sup>˚</sup> and 11.3622(7) A,<sup>˚</sup> respectively, which is in good agreement with those obtained in Ref. [39]. 

To understand how the crystal cell parameters change as a function of temperature, high-resolution single-crystal x-ray diffraction was performed on the BL-3A beamline at the KEK photon factory. The measurements were performed in the vertical scattering geometry, with the incident photon energy fixed at 12 keV. A silicon drift detector was used to detect the scattered x-rays, while a closed-cycle He-4 cryostat provided temperature regulation. Figure 1(b), (c) plots the temperature dependence of the a and c cell parameters, based on the reciprocal space location of the structurally-allowed Q=(4,0,0) and Q=(0,0,8) reflections of CaWO4, respectively. It was found that the a and c cell parameters do not change appreciably, below ∼10 K. This means that the operating temperature of the CaWO4 host crystal should ideally be below 10 K to avoid thermal-expansion-induced misalignment of the laser with respect to the host crystal. 

## 2.2. Electronic Structure of CaWO4 

To understand the electronic structure of the host crystal at low temperatures, abinitio density functional theory (DFT) calculations of CaWO4 were performed using the Quantum Espresso package [40]. A plane wave basis set together with optimised 



<!-- Start of picture text -->
<a Pog J 11.36 /<br>og oD, 5.238 é<br>|| Toa = 5.236 of = 11.35 4<br>Dg PD rd 11.345 &<br>y Da 5.234 pr 5<br>\ ~ Ji 2 eeere coal 1 1 . 34 cae<br>@® 0 100 200 300 0 100 200 300<br>a T (K) T (K)<br><!-- End of picture text -->



<!-- Start of picture text -->
ee ewan - 21372<br>E SS" ) | [x ms<br>PS SESE — Total / | 2 111011<br>— |/ 100 E Ers 4fn<br>9 I a  — / I~ L=6S=3/2<br>& V0 1532.63nm| 1530.86 nm<br>g Lo (e)<br>= SS Ze _— N: N emesZs| 300 El Nf ———<br>a aXo a | <= LZ = A<br>6 S ooo o o << | i LF<br>== r= 227 ny | 100 §= —_—<br>BY r x M I'zZ R — A 70 — 10 20 30 Za CZ ’<br>PDOS (states/eV) I==15/2<br><!-- End of picture text -->

6 

field Hamiltonian within a given<sup>4</sup> IJ multiplet takes the form 



with ITOs T<sup>ˆ</sup> kq (see Ref. [46] and Supplemental materials). Only the terms consistent with S4 symmetry are retained, namely, B20, B40, B44, B60, and B64. Higher-order terms due to the inter-manifold couplings are neglected. 

Figure 2(c) plots the energy levels obtained from the calculations, which show the splitting in the J =<sup><u>15</u></sup> 2<sup>andJ=</sup><sup><u>13</u></sup> 2<sup>manifold.Inthefollowingsection,thetransitions</sup> considered were those between the ground state Z1 into the Y1 to Y7 manifold, paying special attention to the Z1 → Y1 and Z1 → Y2 transitions as they are closest to 1550 nm in wavelength. 

## 3. Experimental Method 

The experimental setup is shown in Fig. 3(a). A tunable C-band narrowband laser (Santec TSL-570) is coupled to free-space using a fibre-collimator for subsequent optical manipulation. The laser passes through a linear polariser consisting of a quarter-wave plate (QWP), a half-wave plate (HWP), and a polarising beam splitter (PBS). The QWP and HWP were optimised to minimise the power of the reflected beam from the PBS, ensuring the laser is horizontally polarised. The second HWP was used for linear polarisation control. A lens was used to focus the light on a 5×5×5mm CaWO4 single crystal with a Er<sup>3+</sup> dopant concentration of 50 ppm inside the cryostat (Montana Instruments, CryoAdvance-50). The laser is then coupled to a multimode fibre, measured by an InGaAs photodetector (PD) (Thorlabs Inc., PDA05CF2) connected to an oscilloscope (See Supplemental Materials for details on how the data was collected). 

The absorption, central wavelength, and linewidth of the Z1 → Y1 and Z1 → Y2 transitions were studied as a function of polarisation and temperature. As described earlier, these transitions were chosen as they are closest to the 1550 nm telecommunication wavelength. For power variation, the input power of the laser was varied while maintaining horizontally polarised light and a temperature of 3.2 K. For polarisation variation, the polarisation was varied using the second HWP [Fig. 3] while maintaining a laser input power of 100 µW and a temperature of 3.2 K. For temperature variation, the temperature within the cryostat was varied while maintaining horizontally polarised light and a laser input power of 100 µW. A laser input power of 100 µW was chosen for the polarisation and temperature dependence measurements because this order of magnitude for the laser input power produced a reasonable absorption with low noise (large SNR: signal-to-noise-ratio). 

These polarisation- and temperature-dependent measurements were performed in two configurations with respect to the host crystal axes [Fig. 3(b), (c)]. In the first configuration, the incident beam is oriented along the crystal c axis, namely k||c, where 



<!-- Start of picture text -->
(a) Cryostat<br>(<1 @ Crystal ®<br>Lens— RN<br>Laser Dawe PBS (4) Oscilloscope<br>= N=, NS—#—Pp— |<br>Collimator HWP Mirror Coupler PD<br><!-- End of picture text -->



<!-- Start of picture text -->
(b) :<br>; y<br>“Kle<br><!-- End of picture text -->



<!-- Start of picture text -->
(c) )<br>5 y<br>~k||b<br><!-- End of picture text -->



<!-- Start of picture text -->
OO<br><!-- End of picture text -->



<!-- Start of picture text -->
1.0 1.0<br>0.91 ¢ 0.9 © Z1 hn<br>0.8 5) © Zr Yo 0.8 © Z1 Y2<br>§ 0.7 % 8 0g 0-0 07<br>Ba 06 ©0.833090000 5000 0 8 gg<br>. oO o 0 o oo 0 — — = . Re<br>£0.5 5 0.5 oo o [e]<br>20.4 204 Ym REE<br>< 0.3 < 03 © ©00:0:0.0.0:0.00.0-0-9 .0<br>0.2 0.2<br>0.1 0.1<br>0.0 0.0<br>0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 09 1 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 09 1<br>Power (mW) Power (mW)<br><!-- End of picture text -->

9 

## 4.1. Polarisation 

The effects of varying the polarisation are shown in Fig. 5 for the k||c configuration and Fig. 6 for the k||a configuration. In addition to the absorption, the central wavelengths and linewidths of the Z1 → Y1 and Z1 → Y2 transitions are also investigated, 

As expected, the central wavelength for both configurations is centred around approximately 1532.6 nm for the Z1 → Y1 transition and 1530.8 nm for the Z1 → Y2 transition, neither transition exhibiting significant changes with polarisation. Since the electronic levels and the corresponding optical transitions are independent of the polarisation states, the central wavelength at these transitions should be invariant with respect to the incident beam linear polarisation. 

The absorption in the k||c configuration for the Z1 → Y1 transition is approximately 0.700 for all polarisations, and approximately 0.725 for the Z1 → Y2 transition for all polarisations, with both transitions following a circle with polarisation [Fig. 5(a)], implying polarisation independence. However, the absorption polarisation dependence in the k||a configuration follows a more interesting result [Fig. 6(a)]. The Z1 → Y1 transition follows an elliptical pattern with polarisation, with maxima when horizontally polarised light is used (where ϵ||c) and minima when vertically polarised light is used (where ϵ||a). Conversely, the absorption shows greater polarisation dependence in the Z1 → Y2 transition, which follows a more elongated ellipse with polarisation, with maxima when vertically polarised light (ϵ||a) is used and minima when horizontally polarised light is used (ϵ||c). 

The absorption results in this configuration agree qualitatively with previous PL and PLE measurements [38]. Indeed, the Z1 → Y1 transition involves a change in irreducible representation of the eigenstates [(Γ5 + Γ6) → (Γ7 + Γ8)] whereas the Z1 → Y2 transition does not [(Γ5 + Γ6) → (Γ5 + Γ6)]). For the k||a configuration, different selection rules are fulfilled as the incident beam linear polarisation, ϵ, is varied, which gives rise to angular dependence on polarisation and hence maxima and minima absorptions as shown in Fig. 6(a). On the other hand, for the k||c configuration, the same selection rules are always satisfied as the incident beam linear polarisation varies, which results in a more circular pattern indicating polarisation independence [Fig. 5(a)]. 

The linewidths in the k||c configuration are wider for the Z1 → Y2 transition than the Z1 → Y1 transition by approximately 0.7 pm, following a fairly circular pattern with polarisation [Fig. 5(c)]. The Z1 → Y1 transition linewidths are also narrower than the Z1 → Y2 transition linewidths in the k||a configuration [Fig. 6(c)]. This indicates that the Z1 → Y1 transition have longer lifetimes, which may translate to longer storage times for quantum states, due to its narrower linewidths in both crystal configurations. However, the Z1 → Y1 transition linewidths follow a fairly circular pattern with polarisation, while the Z1 → Y2 transition linewidths have maxima at 90° and 270° (vertically polarised light, ϵ||a) and minima at 0° and 180° (horizontally polarised light, ϵ||c). The polarisation dependence in the Z1 → Y2 transition could be linked to the change in selection rules that are satisfied [38]. 



<!-- Start of picture text -->
L.<br>% ° “% %,.<br>° 0 © 8g U: 0 © ° 4 5, 2%<br>Q es (o) ° ° % 0 © 90 2%:<br>Q 15 ®@ [¢) <] [) ° 9 © © o° g009%0%0 o°o © © %<br>Q ® [e} ° Le oe)<br>2) ® ° o Soo ;<br>@ i © o Central © ° o \ \ o<br>- Absorption © © Wavelength o oo Linewidth 3 M °<br>® © ° (nm) © 0 © (x10°nm) o<br>[es © o 0 © > v oq<br>° °o 7Z1 Ye ° . °° Z1 1h o ° 0 of 1 Y2 Jo%<br>or) 66 6 0®" ° ° °Z1 Ye 0 © ° © ©®000°6 600° 0°<br>oo ©<br>0 © o “Uy: Ji 2,%,.. 15 2,Go<br>° ° So. o © ° 5 EON ° ° Sap.<br>h # ° ° a %, ® id “0,<br>@ [<) ° % ° . »<br>% 00000 ° © © ° 0©00%0%0 y °<br>[oye] o %°0 o o ° . .<br>&° [5@ ° ° °° . oo o. ©©<br>°NE)o o0©© ° Central ° ° 5 » 4h®o °<br>5 o oo © Wavelength © oo inewidt J<br>0 Absorption o J ° (nm) © °° (x10 nm) o °<br>% on © ° ° 5 °© Zi +h oc ©<br>oo° £00000 o © ° °Z1 hh ° N ° ° o 7 Ya |, p ©<br>°©Z1 ° © [<) ° LY 0 © °<br>© 1h ° °o 71 Ya ° ooo<br>[9 lezZioo, 12© ° e g ° 4 ° JS . . J © 6 oo S °<br><!-- End of picture text -->



<!-- Start of picture text -->
1.0 6575 1530 ©?2 30<br>0.8 © Z1 V2 B 5 67 Ye 5208” 7 $Z1 Y2<br>=g 06 0.70.5 [ 88883 3 883g x 8 p=E28 Gn19%6°5) 3 0:206%ee0 zX15dg 20<br>BY ER s o 0 = 1<br>Q 04 . 3 15° 0.681 ks] p r »<br>203 E N S oAE a) owe5 E 10 ] °<br>0.2 = g pe 8 a wo 5s at<br>0.1*%. s ° °c © »15%OR0 000 0 , 0oo % 0,00g0 0 °° “0 Ea530"6% ~ 0 se888888 8°<br>5 10 15 2 3 30 2.6% 5 10 15 20 35 30 0 5 10 15 20 35 30<br>Temperature (K) hs Temperature (K) Temperature (K)<br>ho 1 seer 30<br>os he 6 coon 0S pg [2h A<br>0.8 © 71 Y2 7 PRE CZ Ye 0 60 © Z1 Yo<br>0.7. =E453 Sep E<br>= 6% 1530 [ @ 20<br>2g 06 Boys 306°® oO= d °<br>a 05 000 0, 54 1 . X15<br>3 oo io) 63° 4 20oo<br>@ 04 op . Epes ge BS d<br>2 03 ©o0og NUN Z 12.6% 0 § eS) B=g" ;<br>02- oo Ew 5 WEE iw<br>01 o °o . 8= gn °068959 0 0 0 2 ° q 530°[ag “ Jak] 88888888 Q © o<br>0.00 5 10 15 20 35 3 o 0 526 % 009° 5 ° 20 3m 3 530+6 00 5 10 15 20 35 30<br>Temperature (K) Temperature (K) Temperature (K)<br><!-- End of picture text -->

12 

## 4.3. Qualitative Analysis 

A qualitative comparison has been tabulated in Table 1 based on the results. It shows the dependency of the absorption, central wavelength, and linewidth based on the polarisation and temperature, as well as the particular crystal axis and transition. 

Table 1: Dependency of absorption, central wavelength, and linewidth on the polarisation and temperature 

|Dependency|Confguration|Transition|Polarisation|Temperature|
|---|---|---|---|---|
||k||c|Z1→Y1|Sightly smaller|Smaller, decreases<br>with temperature|
|Absorption||Z1→Y2|Slightly larger|Larger, decreases<br>with temperature|
||k||a|Z1→Y1|Overall smaller, maxima<br>with horizontally polarised<br>light, minima with vertically<br>polarised light<br>|Signifcantly larger,<br>decreases with<br>temperature|
|||Z1→Y2|Overall larger, maxima<br>with vertically polarised<br>light, minima with<br>horizontally polarised light|Signifcantly smaller,<br>decreases with<br>temperature|
|||Z→Y|No signifcant|Larger, increases|
|Central|k||c|11|changes<br>|with temperature<br>|
|Wavelength||Z1→Y2|No signifcant<br>changes|Smaller, increases<br>with temperature|
||k||a|Z1→Y1|No signifcant<br>changes|Smaller, increases<br>with temperature|
|||Z1→Y2|No signifcant<br>changes|Larger, increases<br>with temperature|
||k||c|Z1→Y1|Signifcantly smaller|Smaller, increases<br>with temperature|
|Linewidth||Z1→Y2|Signifcantly larger|Larger, increases<br>with temperature|
||k||a|Z1→Y1|Smaller, constant with<br>polarisation<br>Larger, maxima with|Smaller, increases<br>with temperature|
|||Z1→Y2|vertically polarised light,<br>minima with horizontally<br>polarised light|Larger, increases<br>with temperature|



## 5. Discussion 

The experimental characterization of the Z1 → Y1 and Z1 → Y2 optical transitions in Er<sup>3+</sup> : CaWO4 provides insight into their suitability for quantum memory applications. 

13 

Among the two transitions, the Z1 → Y1 transition exhibits narrower linewidth, higher absorption, and polarization insensitivity compared to the Z1 → Y2 transition. These features make the Z1 → Y1 transition more suitable for quantum memory protocols such as the atomic frequency comb (AFC) [49–51], where higher absorption is favorable for higher efficiency. Furthermore, the polarization-insensitive absorption characteristics makes the Z1 → Y1 transition suitable for quantum memories designed for storing photonic polarization qubits where arbitrary polarization states can be stored with high fidelity. 

The linewidth of the Z1 → Y2 transition is larger than the linewidth of the Z1 → Y1. The measurements also showed that both linewidth decreases with lower temperature and stops decreasing below approximately 5 K. This behavior is commonly attributed to the suppression of phonon-induced decoherence [52]. In general, the narrower linewidth, therefore, tends to translates to longer storage times. However, it is important to recognize that the linewidth measurements reflect inhomogeneous broadening, and does not directly inform about the homogenous linewidth, which ultimately determines the optical coherence time and hence the achievable storage time. 

Although the temperature dependence measurements showed the saturation behavior below approximately 5 K, it would be interesting to explore the phonon– induced decoherence effects near absolute zero at temperatures as low as 20 mK, it is known that phonons arising from lattice vibrations in the crystal causes decoherence [52]. The homogeneous linewidth is strongly temperature-dependent, with different phonon-induced decoherence mechanisms dominating at different temperature ranges. The precise characterization through coherent spectroscopy and mitigation of this phenomenon could be an avenue for future work. 

Although the absorption, central wavelength, and linewidth differ depending on the electronic transition, crystal axis orientation relative to the polarisation of incident light, the use of the Z1 → Y1 transition with the laser oriented along the crystal c-axis is recommended. It has a smaller linewidth than the Z1 → Y2 transition, along with a constant central wavelength (for temperatures below 5 K). Additionally, it has an overall greater absorption than the configuration with the laser oriented along the crystal a- axis and with ϵ||c. Significantly, it is much less polarisation dependent compared to the k||a configuration. In terms of engineering an Er<sup>3+</sup> :CaWO4-based quantum memory, a cryostat must be used to keep the temperature below 5 K. In addition, different sources of noise must be characterised and the quantum memory designed to mitigate them. 

## 6. Conclusion 

The polarisation and temperature dependence of the absorption spectra of Er<sup>3+</sup> :CaWO4 was studied in the endeavour of developing the solid-state rare-earth ion-doped crystal as a quantum memory. The results show that the central wavelength of the Z1 → Y1 and Z1 → Y2 transitions is independent of polarisation and temperature at cryogenic temperatures (below 5 K). In addition, the linewidth of the Z1 → Y1 transition is overall 

14 

smaller making it more favourable for long storage times than the Z1 → Y2 transition. Overall, the Z1 → Y1 transition saturates slower than the Z1 → Y2 making it more favourable for longer storage times. Significantly, the k||c configuration absorption is polarisation independent, making it the more favourable Er<sup>3+</sup> :CaWO4 configuration to store quantum states as the storage times will be fairly constant for any polarisation. 

Acknowledgments This research is supported by A*STAR under Project No. C230917009, Q.InC Strategic Research and Translational Thrust; the MTC Young Investigator Research Grant (Award # M24N8c0110); CQT++ Core Research Funding Grant (A*STAR); and Grant-in-Aid for Scientific Research (Grant No. 22K03507) from the Japan Society for the Promotion of Science. 

Conflict of Interest The authors declare no conflicts of interest. 

## References 

- [1] C. Simon, “Towards a global quantum network,” Nature Photonics, vol. 11, no. 11, pp. 678–680, 2017. 

- [2] J.-M. Mol, L. Esguerra, M. Meister, D. E. Bruschi, A. W. Schell, J. Wolters, and L. W¨orner, “Quantum memories for fundamental science in space,” Quantum science and technology, vol. 8, no. 2, p. 024006, 2023. 

- [3] H.-J. Briegel, W. D¨ur, J. I. Cirac, and P. Zoller, “Quantum repeaters: the role of imperfect local operations in quantum communication,” Physical Review Letters, vol. 81, no. 26, p. 5932, 1998. 

- [4] W. J. Munro, K. Azuma, K. Tamaki, and K. Nemoto, “Inside quantum repeaters,” IEEE Journal of Selected topics in quantum electronics, vol. 21, no. 3, pp. 78–90, 2015. 

- [5] C. Liorni, H. Kampermann, and D. Bruß, “Quantum repeaters in space,” New Journal of Physics, vol. 23, no. 5, p. 053021, 2021. 

- [6] K. Azuma, S. E. Economou, D. Elkouss, P. Hilaire, L. Jiang, H.-K. Lo, and I. Tzitrin, “Quantum repeaters: From quantum networks to the quantum internet,” Reviews of Modern Physics, vol. 95, no. 4, p. 045006, 2023. 

- [7] T. D. Ladd, F. Jelezko, R. Laflamme, Y. Nakamura, C. Monroe, and J. L. O’Brien, “Quantum computers,” nature, vol. 464, no. 7285, pp. 45–53, 2010. 

- [8] J. Preskill, “Quantum computing in the nisq era and beyond,” Quantum, vol. 2, p. 79, 2018. 

- [9] R. Rietsche, C. Dremel, S. Bosch, L. Steinacker, M. Meckel, and J.-M. Leimeister, “Quantum computing,” Electronic Markets, vol. 32, no. 4, pp. 2525–2536, 2022. 

- [10] S. Zaiser, T. Rendler, I. Jakobi, T. Wolf, S.-Y. Lee, S. Wagner, V. Bergholm, T. SchulteHerbr¨uggen, P. Neumann, and J. Wrachtrup, “Enhancing quantum sensing sensitivity by a quantum memory,” Nature communications, vol. 7, no. 1, p. 12279, 2016. 

- [11] Y. Yang, “Memory effects in quantum metrology,” Physical review letters, vol. 123, no. 11, p. 110501, 2019. 

- [12] E. Biham, B. Huttner, and T. Mor, “Quantum cryptographic network based on quantum memories,” Physical Review A, vol. 54, no. 4, p. 2651, 1996. 

- [13] M. G¨undo˘gan, J. S. Sidhu, V. Henderson, L. Mazzarella, J. Wolters, D. K. Oi, and M. Krutzik, “Proposal for space-borne quantum memories for global quantum networking,” npj Quantum Information, vol. 7, no. 1, p. 128, 2021. 

- [14] M. K. Bhaskar, R. Riedinger, B. Machielse, D. S. Levonian, C. T. Nguyen, E. N. Knall, H. Park, D. Englund, M. Lonˇcar, D. D. Sukachev et al., “Experimental demonstration of memoryenhanced quantum communication,” Nature, vol. 580, no. 7801, pp. 60–64, 2020. 

15 

- [15] Y. Wang, A. N. Craddock, R. Sekelsky, M. Flament, and M. Namazi, “Field-deployable quantum memory for quantum networking,” Physical Review Applied, vol. 18, no. 4, p. 044058, 2022. 

- [16] A. I. Lvovsky, B. C. Sanders, and W. Tittel, “Optical quantum memory,” Nature photonics, vol. 3, no. 12, pp. 706–714, 2009. 

- [17] J. Dajczgewand, “Optical memory in an erbium doped crystal: efficiency, bandwidth and noise studies for quantum memory applications,” Ph.D. dissertation, Universit´e Paris Saclay (COmUE), 2015. 

- [18] O. Pinel, M. Hosseini, B. M. Sparkes, J. L. Everett, D. Higginbottom, G. T. Campbell, P. K. Lam, and B. C. Buchler, “Gradient echo quantum memory in warm atomic vapor,” Journal of visualized experiments: JoVE, no. 81, p. 50552, 2013. 

- [19] M. Hosseini, G. Campbell, B. M. Sparkes, P. K. Lam, and B. C. Buchler, “Unconditional roomtemperature quantum memory,” Nature Physics, vol. 7, no. 10, pp. 794–798, 2011. 

- [20] Y.-W. Cho, G. Campbell, J. Everett, J. Bernu, D. Higginbottom, M. Cao, J. Geng, N. Robins, P. Lam, and B. Buchler, “Highly efficient optical quantum memory with long coherence time in cold atoms,” Optica, vol. 3, no. 1, pp. 100–107, 2016. 

- [21] M. P. Hedges, J. J. Longdell, Y. Li, and M. J. Sellars, “Efficient quantum memory for light,” Nature, vol. 465, no. 7301, pp. 1052–1056, 2010. 

- [22] K. Heshami, D. G. England, P. C. Humphreys, P. J. Bustard, V. M. Acosta, J. Nunn, and B. J. Sussman, “Quantum memories: emerging applications and recent advances,” Journal of modern optics, vol. 63, no. 20, pp. 2005–2028, 2016. 

- [23] B. Jing, S. Wei, L. Zhang, D. Zhou, Y. He, X. Zou, W. Pan, H.-Z. Song, and L. Yan, “Approaching scalable quantum memory with integrated atomic devices,” Applied Physics Reviews, vol. 11, no. 3, 2024. 

- [24] M. Nilsson, Coherent interactions in rare-earth-ion-doped crystals for applications in quantum information science. Lund University, 2005. 

- [25] Y.-P. Liu, Z.-W. Ou, T.-X. Zhu, M.-X. Su, C. Liu, Y.-J. Han, Z.-Q. Zhou, C.-F. Li, and G.C. Guo, “A millisecond integrated quantum memory for photonic qubits,” Science Advances, vol. 11, no. 13, p. eadu5264, 2025. 

- [26] P. Goldner, A. Ferrier, and O. Guillot-No¨el, “Chapter 267 - rare earth-doped crystals for quantum information processing,” ser. Handbook on the Physics and Chemistry of Rare Earths, J.-C. G. B¨unzli and V. K. Pecharsky, Eds. Elsevier, 2015, vol. 46, pp. 1–78. 

- [27] Y. Ma, Y.-Z. Ma, Z.-Q. Zhou, C.-F. Li, and G.-C. Guo, “One-hour coherent optical storage in an atomic frequency comb memory,” Nature communications, vol. 12, no. 1, p. 2381, 2021. 

- [28] M. Zhong, M. P. Hedges, R. L. Ahlefeldt, J. G. Bartholomew, S. E. Beavan, S. M. Wittig, J. J. Longdell, and M. J. Sellars, “Optically addressable nuclear spins in a solid with a six-hour coherence time,” Nature, vol. 517, no. 7533, pp. 177–180, 2015. 

- [29] F. Wang, M. Ren, W. Sun, M. Guo, M. J. Sellars, R. L. Ahlefeldt, J. G. Bartholomew, J. Yao, S. Liu, and M. Zhong, “Nuclear spins in a solid exceeding 10-hour coherence times for ultralong-term quantum storage,” PRX Quantum, vol. 6, no. 1, p. 010302, 2025. 

- [30] A. Ortu, A. Holz¨apfel, J. Etesse, and M. Afzelius, “Storage of photonic time-bin qubits for up to 20 ms in a rare-earth doped crystal,” npj Quantum Information, vol. 8, no. 1, p. 29, 2022. 

- [31] X. Liu, J. Hu, Z.-F. Li, X. Li, P.-Y. Li, P.-J. Liang, Z.-Q. Zhou, C.-F. Li, and G.-C. Guo, “Heralded entanglement distribution between two absorptive quantum memories,” Nature, vol. 594, no. 7861, pp. 41–45, 2021. 

- [32] E. Saglamyurek, N. Sinclair, J. Jin, J. A. Slater, D. Oblak, F. Bussieres, M. George, R. Ricken, W. Sohler, and W. Tittel, “Broadband waveguide quantum memory for entangled photons,” Nature, vol. 469, no. 7331, pp. 512–515, 2011. 

- [33] V. C. Vivoli, N. Sangouard, M. Afzelius, and N. Gisin, “High-bandwidth quantum memory protocol for storing single photons in rare-earth doped crystals,” New Journal of Physics, vol. 15, no. 9, p. 095012, 2013. 

- [34] M. Ranˇci´c, M. Le Dantec, S. Lin, S. Bertaina, T. Chaneli`ere, D. Serrano, P. Goldner, R. B. 

16 

Liu, E. Flurin, D. Est`eve et al., “Electron-spin spectral diffusion in an erbium doped crystal at millikelvin temperatures,” Physical Review B, vol. 106, no. 14, p. 144412, 2022. 

- [35] M. Le Dantec, M. Ranˇci´c, S. Lin, E. Billaud, V. Ranjan, D. Flanigan, S. Bertaina, T. Chaneli`ere, P. Goldner, A. Erb et al., “Twenty-three–millisecond electron spin coherence of erbium ions in a natural-abundance crystal,” Science advances, vol. 7, no. 51, p. eabj9786, 2021. 

- [36] S. Ourari, �L. Dusanowski, S. P. Horvath, M. T. Uysal, C. M. Phenicie, P. Stevenson, M. Raha, S. Chen, R. J. Cava, N. P. de Leon et al., “Indistinguishable telecom band photons from a single er ion in the solid state,” Nature, vol. 620, no. 7976, pp. 977–981, 2023. 

- [37] M. T. Uysal, �L. Dusanowski, H. Xu, S. P. Horvath, S. Ourari, R. J. Cava, N. P. De Leon, and J. D. Thompson, “Spin-photon entanglement of a single er 3+ ion in the telecom band,” Physical Review X, vol. 15, no. 1, p. 011071, 2025. 

- [38] F. Becker, C. L. Curtin, S. KC, T. Schneider, L. J. Sauerzopf, I. Elzeiny, and K. MAˇzller,<sup>˜</sup> “Spectroscopic investigations of multiple environments in er: Cawo4 through charge imbalance,” arXiv preprint arXiv:2412.03948, 2024. 

- [39] P. Villars and K. Cenzual, “Cawo4 (ca[wo4]) crystal structure: Springermaterials,” Springer-Verlag Berlin Heidelberg and MPDS and NIMS, 2011. 

- [40] G. Paolo and et al., “Quantum espresso: A modular and open-source software project for quantum simulations of materials,” J. Phys.: Condens. Matter, vol. 21, no. 39, pp. 1–19, 2009. 

- [41] S. Martin and G. Fran¸cois, “Optimization algorithm for the generation of oncv pseudopotentials,” Computer Physics Communications, vol. 196, pp. 36–44, 2015. 

- [42] J. P. Perdew, K. Burke, and M. Ernzerhof, “Generalized gradient approximation made simple,” Phys. Rev. Lett., vol. 77, pp. 3865–3868, Oct 1996. 

- [43] H. J. Monkhorst and J. D. Pack, “Special points for brillouin-zone integrations,” Phys. Rev. B, vol. 13, pp. 5188–5192, Jun 1976. 

- [44] R.Fletcher, Practical Methods of Optimization. 

   - John Wiley & Sons, Ltd, 2000, ch. 1-14. 

- [45] W. Setyawan and S. Curtarolo, “High-throughput electronic band structure calculations: Challenges and tools,” Computational Materials Science, vol. 49, no. 2, pp. 299–312, 2010. 

- [46] P. Santini, S. Carretta, G. Amoretti, R. Caciuffo, N. Magnani, and G. H. Lander, “Multipolar interactions in f -electron systems: The paradigm of actinide dioxides,” Rev. Mod. Phys., vol. 81, pp. 807–863, Jun 2009. 

- [47] N. Myoung and G. B. Jung, “Effects of annealing temperature and neodymium concentration on structural and photoluminescence properties of nd3+-doped y2o3-sio2 powders,” Journal of Rare Earths, vol. 39, no. 6, pp. 651–656, 2021. 

- [48] S. Das, R. Aluguri, S. Manna, R. Singha, A. Dhar, L. Pavesi, and S. Ray, “Optical and electrical properties of undoped and doped ge nanocrystals nanoscale res,” Lett, vol. 7, pp. 143–153, 2012. 

- [49] M. Afzelius, C. Simon, H. De Riedmatten, and N. Gisin, “Multimode quantum memory based on atomic frequency combs,” Physical Review A—Atomic, Molecular, and Optical Physics, vol. 79, no. 5, p. 052329, 2009. 

- [50] M. Bonarota, J. Ruggiero, J.-L. L. Gou¨et, and T. Chaneli`ere, “Efficiency optimization for atomic frequency comb storage,” Physical Review A—Atomic, Molecular, and Optical Physics, vol. 81, no. 3, p. 033803, 2010. 

- [51] M. Afzelius, I. Usmani, A. Amari, B. Lauritzen, A. Walther, C. Simon, N. Sangouard, J. Min´aˇr, H. De Riedmatten, N. Gisin et al., “Demonstration of atomic frequency comb memory for light with spin-wave storage,” Physical review letters, vol. 104, no. 4, p. 040503, 2010. 

- [52] R. P. Budoyo, K. Kakuyanagi, H. Toida, Y. Matsuzaki, W. J. Munro, H. Yamaguchi, and S. Saito, “Phonon-bottlenecked spin relaxation of er3+: Y2sio5 at sub-kelvin temperatures,” Applied Physics Express, vol. 11, no. 4, p. 043002, 2018. 

y 

xy 

Y ~~Y~~ T ~~—~~ 

y 

y ~~Yo~~ 



<!-- Start of picture text -->
a Lo<br>—— {|<br>7<br><!-- End of picture text -->

3 

The crystal field parameters (14) for different J’s have the following relation: 



Now, the above framework shall be applied to the Er impurity in CaWO4. It is assumed that the Er site has S4 point group symmetry, although, according to the experimental structure (your cif file), the Er site has slightly lower symmetry than the S4 symmetry. The crystal-field mixing between different J multiplet states was ignored. Within the above approximations, the crystal field Hamiltonian within the<sup>4</sup> IJ multiplet states is 



Up to 6th-rank terms are considered, ignoring the higher terms arising from, for example, J mixing. Because of the symmetry, the nonzero crystal field coefficients are B20, B40, B44, B60, and B64. 

Within the present formalism, the crystal field parameters for J = 15/2 and J = 13/2 of Er<sup>3+</sup> ion satisfy Eq. (15): 



In real materials, the ratios could vary due to the ignored effects, such as the energy dependence of the covalency [5, 6], while the variations would not be significant. The relations will be used to check the validity of the fitting. 

4 

## 2. Results from the Crystal Field Model 

The experimental energy levels of Er<sup>3+</sup> impurity in CaWO4 [7, 8] are fitted to the crystal field model. Table 1 shows the crystal-field parameters and crystal-field levels. The J = 15/2 (Z1-Z8) and J = 13/2 (Y1-Y7) crystal field levels are fit separately. The ratios of B<sup>13/2</sup> /B<sup>15/2</sup> are as follows. 



Except for the (6, 0) component with small crystal field parameters, the ratios are in line with those within the simple model, Eqs. (17)-(19). The 

Table 1: Crystal-field parameters (cm<sup>−1</sup> ). The lowest Z and Y levels are set to zero for the comparison with the experimental data. 

||Ref.|[7]|Ref. [8]|(data 1)||
|---|---|---|---|---|---|
||Z||Z|Y||
||calc.|exp.|calc.<br>exp.|calc.|exp.|
|B20|133.0||119.6|128.6||
|B40|−164.0||−146.1|−120.7||
|B44|186.0||187.6|123.2||
|B60|−4.8||−6.5|1.5||
|B64|281.8||284.3|96.2||
|||Crysta|l feld levels (me|V)||
||calc.|exp.|calc.<br>exp.|calc.|exp.|
|1|0|0|0<br>0|0|0|
|2|19.63|19.2|19.77<br>20.13|10.05|8.32|
|3|21.52|24.9|22.82<br>25.84|49.23|48.59|
|4|46.07|51.1|48.49<br>51.62|129.64|130.25|
|5|228.36|227.9|225.8<br>227.7|159.69|158.67|
|6|269.11|265.9|269.3<br>269.5|179.17|176.45|
|7|293.78|-|291.2<br>293.8|193.11|193.22|
|8|318.79|319.4|317.4<br>318.3|||



5 

## 3. Experimental Methods: Data Extraction and Analysis 

The oscilloscope used for data collection was set to Normal acquisition, with a sampling rate of 2 MSa/s. To acquire the data, the laser’s wavelength was varied at a speed vsweep of 1 nm/s, its lowest value, for maximum wavelength precision. At the beginning of a sweep, the laser sends an electrical trigger to the oscilloscope, which is set to Single trigger mode. This begins the plotting of the photodetector’s output voltage, which is directly proportional to the optical input power detected. By setting the time of the electrical trigger as t = 0, the sweep time was converted to wavelength by utilising the linear relationship between them, 



where λstart is the start wavelength for a particular wavelength range. 

For every characterisation sweep performed, nine more repeat sweeps were also performed. These ten sweeps were then linearly interpolated by oversampling the raw data with 10 × 10<sup>6</sup> points to an averaged plot with a single “common” wavelength axis. 

The instruments used were connected to a central computer via a router. Using Python SCPI commands, the laser powers, wavelengths, and the cryostat temperatures could be controlled on the computer. To ensure that the data captured by the oscilloscope was not getting clipped, while also achieving high resolution, some preliminary oscilloscope settings were determined and hard-coded into the oscilloscope under the necessary experimental conditions. 

The interpolated absorption dip signal was transformed by 



where µ is the mean voltage (excluding the absorption dip), and a Gaussian fit was used using MATLAB R2022a, which takes the form 



The corresponding errors in a, b, and c were calculated based on a 95% confidence interval. These errors have been propagated in calculations using a, b, and c. From this Gaussian fit, the absorption, central wavelength, and linewidth could be extracted. The absorption was calculated as 



representing the percentage of absorption. 

The central wavelength was taken as b from the fit. The linewidth was calculated 

as 

LW = √2c. (24) 

6 

## Appendix A. Comments on ITOs 

ITOs (see e.g. Ref. [4]) were used rather than traditional Steven’s operators. 

- ITOs are proportional to Steven’s operators. 

- Constructing the ITOs is much easier than Steven’s operators. For the ITOs, only Clebsch-Gordan coefficients need to be corrected, which is easily accomplished. On the other hand, the lists of Steven’s operators often contain errors. 

- With ITOs, symmetry properties (Wigner-Eckart theorem) can be used, which is not the case with Steven’s operators. 

- The ITOs fulfil the orthonormality: 



The trace is over the J multiplet defining the ITOs. 

## References 

- [1] A. Abragam and B. Bleaney, Electron Paramagnetic Resonance of Transition Ions. Oxford: Clarendon Press, 1970. 

- [2] L. Ungur and L. F. Chibotaru, “Ab Initio Crystal Field for Lanthanides,” Chem. Eur. J., vol. 23, no. 15, pp. 3708–3718, 2017. [Online]. Available: https://chemistry-europe.onlinelibrary.wiley.com/doi/abs/10.1002/chem.201605102 

- [3] B. R. Judd, Second Quantization and Atomic Spectroscopy. Baltimore: The Johns Hopkins Press, 1967. 

- [4] P. Santini, S. Carretta, G. Amoretti, R. Caciuffo, N. Magnani, and G. H. Lander, “Multipolar interactions in f -electron systems: The paradigm of actinide dioxides,” Rev. Mod. Phys., vol. 81, pp. 807–863, Jun 2009. [Online]. Available: https://link.aps.org/doi/10.1103/RevModPhys.81.807 

- [5] L. Ungur, B. Szabo, Z. A. ALOthman, A. A. S. Al-Kahtani, and L. F. Chibotaru, “Mechanisms of luminescence in lanthanide complexes: A crucial role of metal–ligand covalency,” Inorganic Chemistry, vol. 61, no. 16, pp. 5972–5976, 2022. [Online]. Available: https://doi.org/10.1021/acs.inorgchem.2c00071 

- [6] V. D. Dergachev, L. F. Chibotaru, and S. A. Varganov, “Ab initio description of vibronic emission bands in noncentrosymmetric lanthanide complexes,” The Journal of Physical Chemistry Letters, vol. 0, no. 0, pp. 2309–2313, 0. [Online]. Available: https://doi.org/10.1021/acs.jpclett.4c03531 

- [7] B. G. Enrique, “Optical spectrum and magnetic properties of er3+ in cawo4,” The Journal of Chemical Physics, vol. 55, no. 5, pp. 2538–2549, 09 1971. [Online]. Available: https://doi.org/10.1063/1.1676445 

- [8] F. Becker, C. L. Curtin, S. KC, T. Schneider, L. J. J. Sauerzopf, I. Elzeiny, and K. M¨uller, “Spectroscopic investigations of multiple environments in er:cawo4 through charge imbalance,” 2024. [Online]. Available: https://arxiv.org/abs/2412.03948 

