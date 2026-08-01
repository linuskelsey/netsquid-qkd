Journal of Magnetic Resonance 287 (2018) 128–139 



Contents lists available at ScienceDirect 

# Journal of Magnetic Resonance 

journal homepage: www.elsevier.com/locate/jmr 



## Storing quantum information in spins and high-sensitivity ESR 

### John J.L. Morton<sup>a,b,⇑</sup> , Patrice Bertet<sup>c</sup> 



> a London Centre for Nanotechnology, UCL, London WC1H 0AH, United Kingdom 

> b Dept. of Electronic and Electrical Engineering, UCL, London WC1E 7JE, United Kingdom 

> c Quantronics Group, SPEC, CEA, CNRS, Université Paris-Saclay, CEA Saclay, 91191 Gif-sur-Yvette Cedex, France 

|a r t i c l e<br>i n f o|a b s t r a c t|
|---|---|
|Article history:<br>Received 12 September 2017<br>Revised 21 November 2017<br>Accepted 22 November 2017<br>Keywords:<br>Spin decoherence<br>Quantum information<br>Quantum memory<br>Superconducting resonators<br>High sensitivity ESR|Quantum information, encoded within the states of quantum systems, represents a novel and rich form of<br>information which has inspired new types of computers and communications systems. Many diverse<br>electron spin systems have been studied with a view to storing quantum information, including molec-<br>ular radicals, point defects and impurities in inorganic systems, and quantum dots in semiconductor<br>devices. In these systems, spin coherence times can exceed seconds, single spins can be addressed<br>through electrical and optical methods, and new spin systems with advantageous properties continue<br>to be identifed. Spin ensembles strongly coupled to microwave resonators can, in principle, be used to<br>store the coherent states of single microwave photons, enabling so-called microwave quantum memo-<br>ries. We discuss key requirements in realising such memories, including considerations for supercon-<br>ducting resonators whose frequency can be tuned onto resonance with the spins. Finally, progress<br>towards microwave quantum memories and other developments in the feld of superconducting quan-<br>tum devices are being used to push the limits of sensitivity of inductively-detected electron spin reso-<br>nance. The state-of-the-art currently stands at around 65 spins per<br>fff<br>Hz<br>p<br>, with prospects to scale down<br>to even fewer spins.<br>�2017 Published by Elsevier Inc.|



#### 1. Introduction 

The storage of information using ferromagnetically-coupled spins in magnetic materials is commonplace through devices such as magnetic storage disks and MRAM, where as few as Oð10<sup>5</sup> Þ spins are used represent the logical ‘0’ or ‘1’ states of each bit [1]. In contrast, the use of isolated, uncoupled spins for information storage did not progress far beyond early studies in the 1950s [2,3] – these proposed a ‘spin echo serial storage memory’ where weak NMR pulses were applied to a sample rich in nuclear spins to ‘write’ data, which could then be recalled in arbitrary order using magnetic field pulses. Through such schemes, multiple bits could be stored as distinct collective excitations of an ensemble of uncoupled spins. The storage capacity of such memories was determined by factors such as the thermal noise of the detecting apparatus, the effect of self-diffusion of the molecules, and relaxation times – and although the ‘spin echo memory’ may have promised some early advantages in latency against contemporary methods, we now know that these storage capacities were not able to become 

> ⇑ Corresponding author at: London Centre for Nanotechnology, UCL, London WC1H 0AH, United Kingdom. 

> E-mail address: jjl.morton@ucl.ac.uk (J.J.L. Morton). 

competitive with (ferro) magnetic information storage and its successors. 

Through the concept of quantum information [4,5] in the 1980s came the recognition that storing information in coherent quantum states offered the possibility of major, disruptive impacts in areas such as computing [4] and security [6]. For example, a computer able to process quantum information, with a memory of only 50 quantum bits (‘qubits’), would be able solve problems beyond the capabilities of today’s most powerful supercomputers [7]. In addition, quantum information, either stored or transmitted, can not be read by a third-party without detection, offering new methods for certification [8] and cryptography [6]. Thus, storing information in isolated spins offers the possibility to exploit the coherence of spins in fundamentally new ways and there is strong motivation to revisit the ideas of writing information into collective states of coherent spins. 

Inspired by such goals of using spins to represent qubits, extensive work has been performed over the past fifteen years on the measurement and extension of electron and nuclear spin coherence times (T 2) using a range of materials. Electron spin coherence times of seconds (at 6 K) [9] or milliseconds (at room temperature) [10] have been measured, while nuclear spin coherence times in the solid-state can be as long as 40 min (room temperature) [11] to six hours (2 K) [12]. Theoretical schemes have also been 

https://doi.org/10.1016/j.jmr.2017.11.015 1090-7807/� 2017 Published by Elsevier Inc. 



<!-- Start of picture text -->
Electron spin<br>Molecules Defects in solids Quantum dots Spin-based<br>aS l 3<br># vaQO Iv0 AN | quantum processor<br>» 4 tum computer<br>& 1% : 4 Universal general purpose<br>Va x, Van WS07, quan p<br>Long coherence times (ms to seconds) + quantum- i<br>JSelpsdevel op |_| microwave EEE<br>Optical Microwave | | High sensitivity ESR<br>quantum memory quantum memory<br>Enables quantum repeaters to Storage ofquantum bits using Inductively detected ESR of<br>extend range ofquantum comms. excitations in spin ensembles hundreds ofspins (or less?)<br><!-- End of picture text -->



<!-- Start of picture text -->
+ quantum- i<br>microwave EEE<br><!-- End of picture text -->

J.J.L. Morton, P. Bertet / Journal of Magnetic Resonance 287 (2018) 128–139 

130 

molecule N@C60 [28,29], in which a nitrogen atom is trapped within a C60 fullerene cage, offers an S ¼ 3=2 electron spin with a coherence time of 80 ls in CS2 at room temperature, rising to 240 ls at 170 K [30], just above the freezing point of the solvent. CS2 crystallizes upon freezing, leading to the segregation of the N@C60 into regions of high concentration. The<sup>15</sup> N nuclear spin of the N@C60 can be used to coherently store one of the electron spin coherences within the S ¼ 3=2 manifold, offering a T 2n > 100 ms at 10 K in a C60 matrix [31]. 

ESR clock transitions have been identified and studied in molecular magnets as a way to suppress decoherence from nuclear spins or spin-spin coupling in samples with large concentrations [22,32], though coherence times in such cases remain rather low (between 8 and 14 ls). More promising, in terms of T 2, has been the synthesis of a molecular magnet with ligands that are nuclear-spin-free and offer good solubility in CS2 [33]. In this way, segregation of the molecule upon solvent freezing is avoided, enabling the study of dilute molecules in a nuclear-spin-free matrix down to low temperatures, and the vanadium(IV) complex showed an electron spin coherence time of 700 ls at 10 K. Despite such impressive progress, the unique advantages of molecular systems remain to be fully demonstrated – as we shall see, their coherence times fall well short of what can be achieved using certain inorganic materials, and the exciting potential of synthetic chemistry to achieve complex structures of coupled spins [34] must be tempered with challenges such as maintaining chemical purity and molecular orientation across a spin ensemble, the punishing restrictions of using nuclear-spin-free ligands, and the absence of a straightforward route to single spin measurement. 

#### 2.2. Electron spins in inorganic solids 

#### 2.2.1. Donor spins in silicon 

Thanks to the key role which it plays in the information technology industry and the resulting work on perfecting high-purity crystal growth, silicon has become one of the purest substances mankind has produced. Impurity concentrations below 10<sup>13</sup> cm<sup>�3</sup> (or 0.2 ppb) are routine in silicon, and isotopic enrichment of the majority<sup>28</sup> Si isotope (I ¼ 0) has been performed with a remaining concentration of the 29Si isotope ðI ¼ 1=2Þ down to 

50 ppm [35]. When silicon is doped with Group V elements, or ‘donors’, such as P, As, Sb or Bi, and cooled below about 50 K, electrons become bound to the donor atom, with an isotropic hyperfine coupling to the donor nucleus. The electron spins of such donors have coherences times which are limited to several hundreds of microseconds in natural abundance silicon (5%<sup>29</sup> Si) [19,36], but can reach tens of milliseconds in<sup>28</sup> Si with ½P�¼ 10<sup>14</sup> cm<sup>�3</sup> , limited only by instantaneous diffusion caused by the finite concentration of donor electron spins [20]. 

The Bi donor, where the S ¼ 1=2 electron spin is coupled to the (I ¼ 9=2)<sup>209</sup> Bi nuclear spin, was used to perform the first demonstration of clock transitions in ESR [9], achieving electron spin coherence times of up to 2.7 s at 6 K in enriched<sup>28</sup> Si, measured using a Hahn echo. At such clock transitions, T 2 increases to 100 ms in natural abundance silicon, while dynamical decoupling techniques such as CPMG [37] can be used to extend this to approach a second [38] (see Fig. 2). From the perspective of quantum memories based on spin ensembles, the most significant advantage of using ESR clock transitions in Bi is the ability to increase the spin concentration by up to two orders of magnitude (and thus increase the strength of the spin-resonator coupling by a factor of Oð10Þ, as discussed in Section 3), whilst maintaining the same spin coherence lifetime. 

Additional features which make donor spins in silicon attractive for quantum information storage include the ability to place them with near-atomic precision using scanning tunnelling microscopy (STM)-based hydrogen lithography [39], while the electron and nuclear spin states of single donor spins can be read out with high fidelity by incorporating the donor into a silicon nanoelectronic device [40,41]. The coherent state of the donor electron spin can be stored in the nuclear spin [25], giving access to coherence times of up to 180 s at a nuclear spin clock transition of the neutral 31P donor [42]. 

#### 2.2.2. Optical spin defects in diamond and SiC 

Since it was first studied in the context of quantum information processing [43], the nitrogen-vacancy (NV) centre in diamond has stimulated a dramatic growth in research across a range of applications, now spanning magnetic-field, electric-field and temperature sensing and imaging down to the cellular and molecular level. One 



Fig. 2. (A) Spin energy level spectrum and ESR transition frequencies of Bi donors in Si, as a function of magnetic field, highlighting four ESR clock transitions. Electron spin coherence time measurements made using (B) natural silicon ([Bi] ¼ 3 � 10<sup>15</sup> cm<sup>�3</sup> ) under various degrees of CPMG dynamical decoupling and (C) isotoptically engineered 28Si ([Bi] ¼ 4 � 1014 cm�3). Adapted with permission from Ref. [38], � American Physical Society, and Ref. [9], � (2013) Macmillan Publishers Ltd: Nature Nanotechnology. 

J.J.L. Morton, P. Bertet / Journal of Magnetic Resonance 287 (2018) 128–139 

131 

key feature the NV centre offers is the ability to measure the spin state of a single defect through changes in the optical photoluminescence [43], even at room temperature. Furthermore, the large Debye temperature of diamond, coupled with the mainly nuclear-spin-free carbon environment leads to electron spin coherence times of several hundred microseconds at room temperature, extendable to a few milliseconds using CPMG [10], or by using<sup>12</sup> C- enriched diamond [18]. While this significant room-temperature coherence opens up a range of sensing applications, the use of NV-centres in diamond for quantum information is likely to require cryogenic temperatures: to be used as a single-spin or ensemble microwave quantum memory, the temperature must be low enough to suppress blackbody radiation at the microwave frequency, x (such that T � �hx=kB, where kB is Boltzmann’s constant). Furthermore, high-fidelity single-shot readout and spinphoton entanglement exploit spin-selective optical transitions which can only be resolved at low temperatures [44]. The nitrogen nuclear spin of the NV centre can be used to store the state of electron spin, as can<sup>13</sup> C in the environment around the defect which can be manipulated by periodically flipping (e.g. by CPMG) the NV centre electron spin at the NMR frequency [45]. 

Other centres in diamond, with potential advantages over the NV, are the subject of very active investigation. The negatively charged silicon-vacancy SiV<sup>�1</sup> (S ¼ 1=2; T 2 � 100 ns at 3.6 K) [46,47] and germanium-vacancy GeV<sup>�1</sup> (T<sup>�</sup> 2<sup>�20 nsat2.2 K)</sup> [48,49] centres have strong coherent optical transitions, but rather short coherence times at liquid helium temperatures due to their orbital degeneracy. However, recent studies of SiV<sup>�1</sup> in diamond have shown considerable increases in coherence properties when cooled down to 10 mK, with T<sup>�</sup> 2<sup>�10 ls and T2up to a several hun-</sup> dred microseconds [50,51]. The neutral SiV<sup>0</sup> centre (S ¼ 1), in contrast, has T 2 � 1 ms at 20 K, while still retaining most (90%) of its optical emission in the zero phonon line, a combination which makes it very promising [52]. Finally, silicon carbide (SiC) is another host offering a largely nuclear-spin-free environment, and defect centres such as the neutral (kk)-divacancy in 4H-SiC (S ¼ 1; T 2 � 1 ms at 20 K) [53] are being investigated. 

#### 2.2.3. RE ions in optical crystals 

The defect centres in diamond described above have optical transition wavelengths in the range of 600 nm (GeV<sup>0</sup> ) to 950 nm (SiV<sup>0</sup> ), and, with the exception of the recently explored SiV<sup>0</sup> , those with the best optical properties have shown relatively poor spin coherence times. Another class of spin defect of importance to quantum information storage is that of rare-earth (RE) dopants in crystal hosts such as YSO (yttrium orthosilicate) and YLiF4. Such defects offer optical transition wavelengths up to 1550 nm (a technologically significant value due to its use in optical fibre communication). RE dopant spins can be divided into two classes: those of Kramers ions (e.g. Er, Nd, Yb) which have ESR transitions and can couple to microwave fields, and those of non-Kramers (e.g. Eu, Pr) ions where the nuclear spin can be used alongside the optical transition to create an optical quantum memory [54]. The nonKramers ions offer the longest spin coherence times (T 2n can be up to six hours using a nuclear spin clock transition [12]) due to the absence of decoherence via an electron spin. However, use of Kramers ions is necessary to operate at optical wavelengths of 1550 nm (i.e. using Er), or as a route to develop quantum coherent microwave-to-optical conversion based on microwave and optical quantum memories operating in tandem [55,56].<sup>1</sup> Recently, nuclear 

> 1 Coherent conversion of single microwave photons to optical photons would enable important applications such as the deterministic entanglement of optical photons, or building room temperature optical links between quantum processors operating in separate cryostats. Methods to achieve such conversion following a number of different designs are currently being pursued. 



Fig. 3. Spin coherence and relaxation time measurements of Nd and Yb ions in YSO, illustrating features such as the ability to exploit the longer coherence time of the nuclear spin (T 2n), and the ability to extend the electron spin coherence time using dynamical decoupling (such as XY16) to suppress effects of spectral diffusion from non-resonant electron spins. Measurements on Yb were performed using<sup>171</sup> Yb in site I at a magnetic field of 1020.8 mT, addressing the mI ¼ �1=2 ESR transition [60]. Measurements on Nd were performed using<sup>145</sup> Nd at a magnetic field of 561.5 mT addressing the mI ¼ þ7=2 ESR transition. Adapted with permission from Ref. [58], � American Physical Society. 

spin coherence times over one second have been measured in Erdoped YSO, by applying high fields (7 T) and low temperatures (1.4 K) to suppress electron spin dynamics [57], in contrast to ENDOR measurements on Nd at lower field which showed T 2n up to only 9 ms [58]. Electron spin coherence times of RE spins have been measured for Nd, Er, and Yb to be up to 100 ls (see Fig. 3) [58–60], and should be compared with the electron g-factor (which can vary from 0.7 to 14) when assessing suitability for strong coupling to microwave resonators (see Section 3). 

#### 2.3. Electron spins of quantum dots 

In addition to the ‘natural’ spins of molecules, atoms and defects described above, electron spins of ‘artificial’ quantum dot (QD) systems are attractive for hosting quantum information, particularly from the point of view of engineering scalable spin-spin interactions to build up quantum information processors. Such QDs have been studied in ensembles by conventional ESR, showing T 2 = 380 ls for QDs formed within Si/SiGe heterostructures [61]. There is also growing work at the single spin level based on electrical spin readout, with coherence times measured up to 1 ms (by Hahn echo) for QD spins formed within isotopically purified<sup>28</sup> Si MOS nanodevices [62]. A promising future direction is developing electrical driving of spin resonance (EDSR) in such structures, as microwave electric fields are more readily confined at the nano-scale than the microwave magnetic fields used for conventional ESR. One method to achieve this is to use a double QD and magnetic field gradient, to create an effective spin-orbit coupling to allow EDSR – such control has been demonstrated in Si/SiGe QDs with a cobalt micromagnet used to provide a field gradient, and coherence times up to 40 ls have been measured [63]. Finally, coupled systems of an impurity spin and QD spin have been studied and offer a hybrid implementation of a singlet-triplet spin qubit [64]. 

#### 3. Quantum memories 

While the most promising schemes for spin-based quantum information processing require qubits represented by single spins [40,62,63], many attractive realisations for quantum information storage make use of ensembles: As with the spin echo serial storage memory proposals of the 1950s, the qubit is represented as a collective excitation of the ensemble. Key ideas around quantum information storage using ensembles were extensively developed 

J.J.L. Morton, P. Bertet / Journal of Magnetic Resonance 287 (2018) 128–139 

132 

and explored in the context of optical quantum memories in which the states of single optical photons are stored in, and subsequently retrieved from, an ensemble of optical emitters, often making use of their internal hyperfine states [13]. Such optical memories are a pre-requisite for so-called quantum repeaters [15,16,65] which are used to distribute entangled states of light over long distances and underpin a quantum-secure communication network [17]. Here, we focus on microwave quantum memories [66,14,67], based on electron spin ensembles (for example comprising one of the spin systems described in Section 2), which are able to store and recall the states of single microwave photons. Such memories benefit from the long coherence lifetimes found in spin ensembles, and are intended to interface with quantum processors operating in the microwave domain (e.g. those based on superconducting qubits [68] or other types of spin qubits). Crucially, through the use of inhomogeneous broadening (either natural, or created through magnetic field gradients), many separate modes of spin excitation fi ffiffi can be addressed, enabling an ensemble of N spins to store OðpNÞ qubits [69,26,14,70]. 

The essence of the microwave quantum memory protocol is summarised in Fig. 4, and comprises a spin ensemble which is strongly coupled to a microwave resonator. To enter this regime, the coupling between the spin ensemble and the microwave cavity, gens, must exceed both the spin linewidth (c<sup>�</sup> 2<sup>) and the coupled cav-</sup> ity linewidth (j ¼ xc=Q ), where Q and xc are the cavity the Q- factor and frequency, respectively. The ensemble coupling gens derives from the coupling strength of a single spin to the cavity fi ffiffi g0, enhanced by a factor pN for N identical spins (in practice, the spin-coupling strength can vary across the ensemble and gens is obtained from a numerical integration). The single spin-cavity coupling g0 can be determined by first calculating the magnitude of 

the zero-point fluctuations of the current in the resonator (i.e. the current corresponding to a resonator energy of <u>12</u><sup>�hxc), then cal-</sup> culating the magnetic field produced by such a current, and the coupling strength of the relevant spin transition to this field. To reach the ‘strong coupling’ regime ðgens � j; c<sup>�</sup> 2<sup>Þ, a large cav-</sup> ity Q-factor is therefore desirable and this is typically achieved using structures made from superconducting materials such as Al, Nb, NbN, NbTiN and TiN. However, superconductivity is only sustained up to a certain value of DC magnetic field, Bc (which varies according to the material), and Q-factor degradation of a superconducting resonator is observed at fields well below Bc, imposing restrictions on the field which can be applied to the spins to obtain a suitable ESR transition frequency. In addition, the spin concentration must be optimised to ensure a spin ensemble with a narrow linewidth (and long coherence time), while obtaining a significant fi ffiffi pN-enhancement of the spin-cavity coupling. For this reason, the use of spins tuned to clock transitions as the storage medium for the microwave quantum memory is particularly attractive as it enables the spin concentration to be increased while reducing the impact on spin-decoherence caused by spin-spin interactions. 

#### 3.1. Resonator designs 

For 3D cavities at X-band, typical values of single spin-cavity coupling, g0, are 2p � 50 mHz with a cavity mode volume of Oð0:1Þ cm<sup>3</sup> [71]. Given a spin concentration of 10<sup>15</sup> cm<sup>�3</sup> , and assuming full spin polarisation, this would lead to a total gens=2p � 0:5 MHz, requiring Q > 20; 000 to achieve strong coupling. Similar values of gens are achievable with planar superconducting resonators based on a k=4 or k=2 transmission line 



Fig. 4. (A) Summary of key terms in cavity quantum electrodynamics with spin ensembles. g is the spin-cavity coupling strength (which scales with pfðNÞ for N spins) and j is the cavity damping rate (which can be expressed as xc=Q , where Q is the cavity Q-factor and xc the cavity frequency). The terms c<sup>�</sup> 2<sup>;c</sup> 2<sup>and c</sup> 1<sup>refer to the various decay rates</sup> for the spin ensemble: respectively, the inhomogeneous ensemble dephasing rate (¼ 1=T<sup>�</sup> 2<sup>),theHahn-echoensembledecoherencerate(¼ 1=T2)andthespin-lattice</sup> relaxation rate (¼ 1=T 1). (B) Protocol for multi-mode microwave quantum memory using a spin ensemble. Single microwave photon states can be stored as collective excitations in the spin ensemble (k ¼ 0 mode), by allowing the spins and cavity to resonantly couple for some time (p=g). By applying a magnetic field gradient, or relying on intrinsic inhomogenous broadening, this collective excitation is transferred to some other mode,fi ffiffi k0, allowing a second quantum state to be written to the k ¼ 0 mode of the same ensemble. This process can be repeated allowing OðpNÞ states to be written. (C) An illustration of the multi-mode memory concept, performed using weak microwave pulses (containing large numbers of microwave photons) and P-donors in silicon. Panel (C) reprinted with permission from Ref. [26], � (2010) American Physical Society. 

< 

< 



<!-- Start of picture text -->
A C E CPW feedline<br>J - ] :interdigitated|} resonator<br>capacitor 5 :<br>; : : ~—|capacitor 3<br>4 £<br>4 E Patterned ground plane<br>ground plane D<br>Sm [EE— Vier [ime a]<br>I he ’ pais grins]<br>=<br>5 |phil lu |<br>CPW . igitated 7<br>feedline capacitor <li lil F EN -—<br>| E- SRS | | 850] le<br>’ Nas 11mm #50 Zde ie: capacitor i<br>Microwave port NNER Bee re HH ee<br><!-- End of picture text -->

© 

© 

© 

X 

© 



<!-- Start of picture text -->
A Exx B 1<br>Al a<br>(x10) 0.9] 3D resonator q ®<br>0.1 2 5 08] 2D resonator py | *<br>= 0.7 ®s 0<br>£2 1 gS os06 sF liait i[ ae<br>3 03 0 g 04 / i EP S<br>= S03 a lo<br>s £ 02 id L oL<br>= 05 5 & 0.1 pr oe % y * »<br>06 9 5 PY 2 f49 oe® 50 51 52 1 53 54 Lo) 55<br>[110] (um) B, (G)<br>C<br>300 m,<br>— 49/2<br>N 200 —- +7/2<br>= 100 — +5/2<br>£ | |= +32<br>v = —u — +172<br>& = +<br>1 00 fp— - 1 p<br>2- 2 00 = - - n<br>2 — = - o k<br>iL —300 ==——u oo )<br>—4 00 — — -9 /2<br>- 25 -2 - 15 -1 - 05 0<br>Hydrostatic strain x 10°<br><!-- End of picture text -->

J.J.L. Morton, P. Bertet / Journal of Magnetic Resonance 287 (2018) 128–139 

135 



Fig. 7. (A) The electron spin relaxation time, T 1 of Group V donor spins in silicon exceed one second at temperatures below 5–10 K, and rise to approach or exceed hours at temperatures below 2 K. Many other electron spin systems also exhibit long T 1 at sub-K temperatures. For this reason, it is important to identify methods to rapidly relax such spins to thermal equilibrium if they are to be coupled to superconducting cavities operating at typtical temperatures of tens of milliKelvin. (B) By placing the spin in a cavity, the rate of spin relaxation by spontaneous emission of a microwave photon can be substantially enhanced to a rate equal to 4g<sup>2</sup> 0<sup>=j.Ifthisexceedstheintrinsic(e.g.spin-</sup> lattice) relaxation rate c1, then the cavity-induced spin relaxation becomes the dominant mechanism, and returns the spin polarisation to thermal equilibrium. (C) This is demonstrated for the case of Bi donors in Si, coupled to a high-Q superconducting resonator (see Fig. 5D). Two inversion-recovery experiments are shown, obtained from the same sample measured using resonators with different mode volumes, with a corresponding difference in cavity-induced spin relaxation time observed (the loaded Q-factors were 3 � 10<sup>5</sup> and 4 � 10<sup>4</sup> for the larger and smaller resonators, respectively). (D) By detuning the spins from the cavity frequency, the degree of cavity-induced spin relaxation can be engineered, yielding a variation of three orders of magnitude in T 1, with just 2 MHz of detuning. Panel (A) adapted from Ref. [94] and panels (C, D) adapted from Refs. [74,81]. 

Table 1 

Various regimes of interest for one or more spins coupled to a cavity. 

|gens >fj;c<sup>�</sup><br>2<sup>g</sup>|Strong coupling (ensemble)|
|---|---|
|4g<sup>2</sup><br>ens<br>j<br>>c<sup>�</sup><br>2|High cooperativity (ensemble)|
|4g<sup>2</sup><br>0<br>j <sup>> c</sup>2|High cooperativity (single spin)|
|4g<sup>2</sup><br>0<br>j <sup>> c1</sup>|Purcell regime|



enhanced spin relaxation or indeed perform high-sensitivity ESR as discussed further in Section 4. An obvious way to control the spincavity detuning is to apply a magnetic field, using the Zeeman interaction to bring the spins onto resonance with the cavity. This can be used, for example, to compensate for the difference between the actual frequency of the fabricated resonator and that it was designed for. The applied magnetic field also shifts the resonator frequency, but if the field is kept in the plane of the superconducting film, this effect is negligible compared to the typical electron gyromagnetic ratio of 28 GHz/T. 

To achieve microwave photon storage in a spin-based quantum memory, it is necessary to obtain spin-cavity coupling for a precisely determined period of time, requiring the ability to quickly tune the spins and cavity into and out of resonance [68]. In such cases, a globally applied magnetic field would need to be applied through a secondary set of coils with lower inductance to allow 

faster switching. Faster, more sensitive tuning of the resonator frequency can be achieved using one or more SQUIDs, incorporated into the resonator structure (see Fig. 8A and B), whose inductance is sensitive to the perpendicular magnetic flux density. Resonator frequency shifts of order 100 MHz can be achieved using perpendicular fields applied globally (e.g. of 10 lT) [82], or created by on-chip bias loops (e.g. with 1 lA of current) [83]. 

A final method to achieve fast control of resonator frequency makes use of photonic bandgap NbTiN resonators based on Bragg mirrors, where DC currents can be directly passed through the resonator to shift its frequency. This has been demonstrated using resonators with Q � 3000, where a DC current of 3 mA resulted in a frequency shift of about 100 MHz, due to the impact of the bias current on the kinetic inductance [76]. 

#### 4. High-sensitivity pulsed ESR with superconducting devices 

Much of the development around microwave quantum memories, described above, can also be directed towards the improvement of spin number sensitivity in ESR. Various derivations for the sensitivity of pulsed ESR have been performed [84,85], though a simple and useful expression for the minimum number of spins detectable in a single echo can be obtained by considering simple arguments from microwave quantum optics, assuming the cavity 

J.J.L. Morton, P. Bertet / Journal of Magnetic Resonance 287 (2018) 128–139 

136 



Fig. 8. Controlling the spin-cavity detuning is important for several reasons, including gating the spin-cavity coupling in quantum memory applications, engineering spinrelaxation, and performing high-sensitivity ESR. Various methods to achieve this exist, depending on the type of materials used for the superconducting resonator. (A) Top panel is an optical micrograph displaying a series of SQUID loops, made using Al/Al2O3/Al Josephson junctions, which act as a magnetic-field-tunable inductor that can be incorporated within a lumped element or CPW resonator. The SQUID loops can be tuned by a globally applied bias field, or by a local bias loop on-chip, as shown in the schematic (middle panel). In this case, 150 MHz tuning of the resonator frequency can be achieved with a bias current of about 1 lA (bottom panel). (B) In other materials, such as Nb, SQUIDs can be formed using narrow constrictions of superconductor, in this case (20 nm). When incorporated into a CPW resonator such a SQUID enables tuning of the resonator frequency by 100 MHz with 10 lT of applied out-of-plane field. (C) The use of SQUIDs can be avoided, instead relying on the change in kinetic inductance in the superconducting film caused by an applied out-of-plane magnetic field. This is demonstrated in (C) for the case of a NbN lumped element resonator, whose frequency is tuned by about 10 MHz using an 5 mT out-of-plane field, while maintaining Q > 10<sup>5</sup> . Panel (A) is adapted with permission from Ref. [82], � American Physical Society; (B) from Ref. [83], and (D) from Ref. [76] with the permission of AIP Publishing. 

damping rate is dominated by external coupling and internal cavity losses are negligible (see Ref. [86] for a more detailed derivation). 

We consider an ensemble of N spins each with identical coupling to the cavity (g0), at the end of a pulsed ESR experiment where a spin echo is formed. At this point, the spins are in-phase and hence there is an enhanced collective coupling of the ensemble fi ffiffi to the cavity of gens ¼ pNg0. Each spin now experiences an enhanced cavity-induced relaxation rate of 4g<sup>2</sup> ens<sup>=j,leadingto</sup> microwave photon emission from the cavity over some duration approximately equal to the spin ensemble dephasing time (1/c<sup>�</sup> 2<sup>).</sup> Thus, the total number of microwave photons emitted by the spins during a spin echo is: 



where C0 is the single spin cooperativity. The amplitude of the microwave signal can be obtained from the square root of the photon number, and we can account for finite spin polarisation, p, by taking the effective number of fully-polarised spins to be pN. Therefore the signal-to-noise ratio (SNR) from a single echo can be written as: 



where n is the number of noise photons added to the signal. The minimum detectable number of spins (i.e. that for which the SNR is equal to one) is then: 



which is minimised by reducing the number of noise photons and by increasing the spin polarisation, cavity Q-factor, spin dephasing time, and single spin-cavity coupling. 

The contribution to n from thermal noise goes as <u>12</u><sup>coth</sup> 2�hkxB0T<sup>~~,~~</sup> which tends to 1/2 at low temperatures. Recent developments motivated by measuring superconducting qubits have led to significant improvements in so-called Josephson Parametric Amplifiers (JPAs), which are loss-less, quantum-limited amplifiers, operating at microwave frequencies (e.g. 1–12 GHz) [87,88]. They can be incorporated into an ESR detection arm, mounted at milliKelvin temperatures (see Fig. 9) and produce no further noise photons beyond thermal noise (when operated in the mode where only one signal quadrature is amplified). Therefore, for ESR at milliKelvin temperatures where spins are highly polarised, thermal noise is determined by vacuum fluctuations, and loss-less amplifiers can be fi fi fi f used, Nmin can be approximately written as 1=p2C0. 

The superconducting resonators described in Section 3.1 have shown Q-factors above 10<sup>5</sup> and demonstrated spin-cavity coupling g0=2p ¼ 450 Hz [81]. When used to perform ESR of Bi donors in Si with T<sup>�</sup> 2<sup>�5 ls, a sensitivity of Nmin¼ 260 spins was demonstrated,</sup> in good agreement with the expected value. Furthermore, the use of the Purcell effect to determine spin relaxation means that a repetition rate of at least 16 Hz can be used regardless of the intrinsic relaxation times of the spin system, such that a sensitivity of 65 fi fi f spins/pHz may be inferred (see Fig. 9B). The primary factor in improving the sensitivity further is likely to come from shrinking the resonator volume further, increasing g0. In addition to improving the SNR per echo, this also enables faster repetition rates due to fi fi f the Purcell effect, such that the ESR sensitivity per pHz follows g<sup>�</sup> 0<sup>2</sup> [89]. 

137 



<!-- Start of picture text -->
J.J.L. Morton, P. Bertet / Journal of Magnetic Resonance 287 (2018) 128–139<br><!-- End of picture text -->



Fig. 9. (A) Schematic showing experimental set-up for high-sensitivity ESR at milliKelvin temperatures. Microwave pulses are sent down an attenuated line to the base temperature of a dilution fridge, and the reflected pulses and emitted spin echo are passed to a quantum-limited Josephson Parametric Amplifier (JPA), which operates in reflection. The amplified signal is then further amplified at 4 K using a high electron mobility (HEMT) amplifier, and again at 300 K using a low noise amplifier (LNA), before being analysed through an IQ-mixer. (B) Example two-pulse Hahn echo experiment measured on such a set-up, using a microresonator where � 230 spins are on-resonance, contributing to the echo signal. The signal-to-noise is 0.9 per single-shot echo. Figure adapted from Refs. [86,81]. 

Despite these impressive opportunities in pulsed ESR sensitivity, there are several practical issues arising from the use of such resonators and milliKelvin environments which are far from those typically used in conventional ESR. First, the very large Q-factors of 10<sup>5</sup> or more may not be well-suited for samples with short coherence times (requiring short pulses). In such cases, the resonators could be over-coupled, or other resonators used, bearing in mind a 1000-fold reduction in the Q-factor would reduce the per-echo sensitivity by a factor of about 30, but the per-root-Hz sensitivity by 1000. The possibility of Q-switched resonators, or shaped microwave pulses to obtain short drive pulses in high-Q cavities [90], could have useful applications in such situations. 

Second, when performing magnetic field sweeps, as is typical in ESR, it is important to consider the shift in the resonator frequency (and, potentially Q-factor) which may remain even if the field is well aligned with the plane of the resonator (see Section 3.3). Such effects could be accounted for, to some extent, in the postprocessing of the data. Alternatively, it may be possible to compensate for field-induced shifts of the resonator frequency through some other tuning mechanism, for example, using a separately biasable SQUID, or by passing a DC current through a photonic bandgap resonator. 

Third, it is worth considering the microwave powers used in such experiments. In order to ensure the thermal noise at the sample is not dominated by black-body radiation from room temperature, the input line feeding the microwave pulses must be heavily attenuated at various stages in the cryostat. However, this should not raise particular concern because the small resonator volume enables extremely low powers to be used. For example, in Ref. [81] a p-pulse of duration 1 ls was achieved using 0.5 pW input power into the resonator, while p-pulse durations of 10 ns (more typical in ESR) would require 5 nW. 

A final practical consideration is the loading of the sample into the resonator volume: to take full advantage of the small values of Nmin demonstrated, it is necessary to ensure there is an efficient sample preparation procedure with minimum ‘wasted’ spins outside the resonator volume. In principle, this could be achieved using a microfluidic device to enable a small volume of injected material to reside over the resonator structure. 

Engineered quantum dots in semiconductor devices offer strong possibilities for large-scale integration for quantum information processing, a variety of optically-active defects and ions in solidstate materials offer opportunities to interface with light for measurement and microwave-optical conversion, while some impurities in suitable host environments offer electron spin coherence times exceeding seconds. Through the toolbox of cavity quantum electrodynamics, such long-lived spins can be coupled to high-Q superconducting resonators to build multi-mode memories for microwave photons. Preliminary results have already shown the exchange of a single qubit state between a spin ensemble and superconducting qubit [68], as well as multi-mode storage using weak microwave pulses [26,70], suggesting that a high-fidelity spin-based quantum memory could be demonstrated in near future. Finally, we have seen how parallel developments based on a similar experimental and theoretical toolbox have yielded improvements in pulsed ESR sensitivity, with the current statefi fi f of-the-art at 65 spins/pHz. Given the advantages arising from the high spin polarisation, low thermal noise, high-Q superconducting resonators and quantum-limited amplifiers, there are good reasons to expect milliKelvin temperatures will become increasingly common in ESR laboratories. 

#### References 

- [1] J.J. Nowak, R.P. Robertazzi, J.Z. Sun, G. Hu, J.H. Park, J. Lee, A.J. Annunziata, G.P. Lauer, R. Kothandaraman, E.J. OSullivan, P.L. Trouilloud, Y. Kim, D.C. Worledge, Dependence of voltage and size on write error rates in spin-transfer torque magnetic random-access memory, IEEE Magn. Lett. 7 (2016) 1–4, https://doi. org/10.1109/LMAG.2016.2539256. 

- [2] A.G. Anderson, R.L. Garwin, E.L. Hahn, J.W. Horton, G.L. Tucker, R.M. Walker, Spin echo serial storage memory, J. Appl. Phys. 26 (11) (1955) 1324–1338, https://doi.org/10.1063/1.1721903. 

- [3] S. Fernbach, W.G. Proctor, Spin echo memory device, J. Appl. Phys. 26 (2) (1955) 170–181, https://doi.org/10.1063/1.1721955. 

- [4] D. Deutsch, Quantum theory, the Church-Turing principle and the universal quantum computer, Proc. Roy. Soc. A: Math. Phys. Eng. Sci. 400 (1818), https:// doi.org/10.1098/rspa.1985.0070(1985)97–117, URL <http://rspa. royalsocietypublishing.org/cgi/doi/10.1098/rspa.1985.0070>. 

- [5] I.L. Chuang, M.A. Nielsen, Quantum Computation and Quantum Information, Cambridge University Press, 2000, URL <http://books.google.com/books? id=65FqEKQOfP8C&printsec=frontcovernnpapers://59f2198e-b16b-49bb89ac-26689742810e/Paper/p2100>. 

- [6] C.H. Bennett, G. Brassard, Quantum cryptography: public key distribution and coin tossing, IBM Tech. Discl. Bull. 28 (1) (1985) 3153–3163. 

#### 5. Summary 

A rich set of electron spin systems are available for use in the storage of quantum information, each with different advantages. 

- [7] E. Farhi, A.W. Harrow, Quantum Supremacy Through the Quantum Approximate Optimization Algorithm. <1602.07674>. 

- [8] S. Wiesner, Conjugate coding, SIGACT News 15 (1) (1983) 78–88. 

- [9] G. Wolfowicz, A.M. Tyryshkin, R.E. George, H. Riemann, N.V. Abrosimov, P. Becker, H.-j. Pohl, M.L.W. Thewalt, S.A. Lyon, J.J.L. Morton, Atomic clock 

J.J.L. Morton, P. Bertet / Journal of Magnetic Resonance 287 (2018) 128–139 

138 

transitions in silicon-based spin qubits, Nat. Nanotechnol. 8 (8) (2013) 561– 564, https://doi.org/10.1038/nnano.2013.117, URL <http://www.ncbi.nlm. nih.gov/pubmed/23793304>. http://arxiv.org/abs/1301.6567. 

- [10] N. Bar-Gill, L.M. Pham, A. Jarmola, D. Budker, R.L. Walsworth, Solid-state electronic spin coherence time approaching one second, Nat. Commun. 4 (2013) 1743, https://doi.org/10.1038/ncomms2771, URL <http://www.ncbi. nlm.nih.gov/pubmed/23612284>. 

- [11] K. Saeedi, S. Simmons, J.Z. Salvail, P. Dluhy, H. Riemann, N.V. Abrosimov, P. Becker, H.-J. Pohl, J.J.L. Morton, M.L.W. Thewalt, Room-temperature quantum bit storage exceeding 39 minutes using ionized donors in silicon-28, Science 342 (6160) (2013) 830–833, https://doi.org/10.1126/science.1239584, URL <http://www.ncbi.nlm.nih.gov/pubmed/24233718>. <http:// www.sciencemag.org/cgi/doi/10.1126/science.1239584>. 

- [12] M. Zhong, M.P. Hedges, R.L. Ahlefeldt, J.G. Bartholomew, E. Sarah, S.M. Wittig, J. J. Longdell, M.J. Sellars, Optically addressable nuclear spins in a solid with a six hour coherence time, Nature 517 (7533) (2015) 1–18, https://doi.org/ 10.1038/nature14025. 

- [13] A. Grodecka-Grad, E. Zeuthen, A.S. Sørensen, High-capacity spatial multimode quantum memories based on atomic ensembles, Phys. Rev. Lett. 109 (2012) 133601, https://doi.org/10.1103/PhysRevLett.109.133601, URL <https://link. aps.org/doi/10.1103/PhysRevLett.109.133601>. 

- [14] B. Julsgaard, C. Grezes, P. Bertet, K. Mølmer, Quantum memory for microwave photons in an inhomogeneously broadened spin ensemble, Phys. Rev. Lett. 110 (2013) 250503, https://doi.org/10.1103/PhysRevLett.110.250503, URL <https://link.aps.org/doi/10.1103/PhysRevLett.110.250503>. 

- [15] H.-J. Briegel, W. Dür, J.I. Cirac, P. Zoller, Quantum repeaters: the role of imperfect local operations in quantum communication, Phys. Rev. Lett. 81 (1998) 5932–5935, https://doi.org/10.1103/PhysRevLett.81.5932, URL <https://link.aps.org/doi/10.1103/PhysRevLett.81.5932>. 

- [16] N. Sangouard, C. Simon, H. de Riedmatten, N. Gisin, Quantum repeaters based on atomic ensembles and linear optics, Rev. Mod. Phys. 83 (2011) 33–80, https://doi.org/10.1103/RevModPhys.83.33, URL <https://link.aps.org/doi/10. 1103/RevModPhys.83.33>. 

- [17] H. Kimble, The quantum internet, Nature 453 (7198) (2008) 1023–1030, https://doi.org/10.1038/nature07127, 10.1038/nature07127. 

- [18] G. Balasubramanian, P. Neumann, D. Twitchen, M. Markham, R. Kolesov, N. Mizuochi, J. Isoya, J. Achard, J. Beck, J. Tissler, V. Jacques, P.R. Hemmer, F. Jelezko, J. Wrachtrup, Ultralong spin coherence time in isotopically engineered diamond, Nat. Mater. 8 (2009) 383–387. 

- [19] A.M. Tyryshkin, J.J.L. Morton, S.C. Benjamin, A. Ardavan, G.A.D. Briggs, J.W. Ager, S.A. Lyon, Coherence of spin qubits in silicon, J. Phys.: Condens. Matter 18 (21) (2006) S783, URL <http://stacks.iop.org/0953-8984/18/i=21/a=S06>. 

- [20] A.M. Tyryshkin, S. Tojo, J.J.L. Morton, H. Riemann, N.V. Abrosimov, P. Becker, H.-J. Pohl, T. Schenkel, M.L.W. Thewalt, K.M. Itoh, S.a. Lyon, Electron spin coherence exceeding seconds in high-purity silicon, Nat. Mater. 11 (2) (2011) 143–147, https://doi.org/10.1038/nmat3182, URL <http://www.ncbi.nlm. nih.gov/pubmed/22138791>. <http://arxiv.org/abs/1105.3772>. <http:// 

   - www.nature.com/doifinder/10.1038/nmat3182>. 

- [21] J. Bollinger, J. Prestage, W. Itano, D. Wineland, Laser-cooled-atomic frequency standard, Phys. Rev. Lett. 54 (10) (1985) 1000–1003, https://doi.org/10.1103/ PhysRevLett.54.1000. 

- [22] J.M. Zadrozny, A.T. Gallagher, T.D. Harris, D.E. Freedman, A porous array of clock qubits, J. Am. Chem. Soc. 139 (20) (2017) 7089–7094, https://doi.org/ 10.1021/jacs.7b03123, pMID: 28453274. 

- [23] F. Dolde, H. Fedder, M.M.W. Doherty, T. Nöbauer, F. Rempp, G. Balasubramanian, T. Wolf, F. Reinhard, L.C.L. Hollenberg, F. Jelezko, J. Wrachtrup, Electric-field sensing using single diamond spins, Nat. Phys. 7 (6) (2011) 459–463, https://doi.org/10.1038/nphys1969, URL <http://arxiv. org/abs/1103.3432>. <http://www.nature.com/doifinder/10.1038/ 

   - nphys1969>. 

- [24] P. Jamonneau, M. Lesik, J.P. Tetienne, I. Alvizu, L. Mayer, A. Dréau, S. Kosen, J.-F. Roch, S. Pezzagna, J. Meijer, T. Teraji, Y. Kubo, P. Bertet, J.R. Maze, V. Jacques, Competition between electric field and magnetic field noise in the decoherence of a single spin in diamond, Phys. Rev. B 93 (2016) 024305, https://doi.org/10.1103/PhysRevB.93.024305, URL <https://link.aps.org/doi/ 10.1103/PhysRevB.93.024305>. 

- [25] J.J.L. Morton, A.M. Tyryshkin, R.M. Brown, S. Shankar, B.W. Lovett, A. Ardavan, T. Schenkel, E.E. Haller, J.W. Ager, S.A. Lyon, Solid state quantum memory using the 31P nuclear spin, Nature 455 (7216) (2008) 1085–1088, https://doi.org/ 10.1038/nature07295, URL <http://www.nature.com/doifinder/10. 1038/nature07295>. <http://arxiv.org/abs/0803.2021>. 

- [26] H. Wu, R. George, A. Ardavan, J.H. Wesenberg, K. Moelmer, D.I. Schuster, R.J. Schoelkopf, K. Itoh, J.J.L. Morton, G.A.D. Briggs, Storage of multiple coherent microwave excitations in an electron spin ensemble, Phys. Rev. Lett. 105 (14) (2010) 140503, https://doi.org/10.1103/PhysRevLett.105.140503, URL <http://link.aps.org/doi/10.1103/PhysRevLett.105.140503>. 

- [27] R. Ward, A. Bowman, E. Sozudogru, H. El-Mkami, T. Owen-Hughes, D.G. Norman, Epr distance measurements in deuterated proteins, J. Magn. Reson. 207 (1) (2010) 164–167. 

- [28] W. Harneit, Fullerene-based electron-spin quantum computer, Phys. Rev. A 65 (2002) 032322, https://doi.org/10.1103/PhysRevA.65.032322, URL <https:// link.aps.org/doi/10.1103/PhysRevA.65.032322>. 

- [29] M. Mehring, W. Scherer, A. Weidinger, Pseudoentanglement of spin states in the multilevel<sup>15</sup> N@c60 system, Phys. Rev. Lett. 93 (2004) 206603, https://doi. org/10.1103/PhysRevLett.93.206603, URL <https://link.aps.org/doi/10.1103/ PhysRevLett.93.206603>. 

- [30] J.J.L. Morton, A.M. Tyryshkin, A. Ardavan, K. Porfyrakis, S.A. Lyon, G.AndrewD. Briggs, Electron spin relaxation of N@C60 in CS2, J. Chem. Phys. 124 (1) (2006) 014508, https://doi.org/10.1063/1.2147262, URL <http://scitation.aip. org/content/aip/journal/jcp/124/1/10.1063/1.2147262>. 

- [31] R.M. Brown, A.M. Tyryshkin, K. Porfyrakis, E.M. Gauger, B.W. Lovett, A. Ardavan, S.A. Lyon, G.A.D. Briggs, J.J.L. Morton, Coherent state transfer between an electron and nuclear spin in<sup>15</sup> N@c60, Phys. Rev. Lett. 106 (2011) 110504, https://doi.org/10.1103/PhysRevLett.106.110504, URL <https://link.aps. org/doi/10.1103/PhysRevLett.106.110504>. 

- [32] M. Shiddiq, D. Komijani, T. Duan, A. Gaita-Ari/ no, E. Coronado, S. Hill, Enhancing coherence in molecular spin qubits via atomic clock transitions, Nature 531 (2016) 348. 

- [33] J.M. Zadrozny, J. Niklas, O.G. Poluektov, D.E. Freedman, Millisecond coherence time in a tunable molecular electronic spin qubit, ACS Centr. Sci. 1 (9) (2015) 488–492, https://doi.org/10.1021/acscentsci.5b00338, pMID: 27163013. 

- [34] J.M. Zadrozny, A.T. Gallagher, T.D. Harris, D.E. Freedman, A porous array of clock qubits, J. Am. Chem. Soc. 139 (2017) 7089–7094, https://doi.org/ 10.1021/jacs.7b03123. 

- [35] B. Andreas, Y. Azuma, G. Bartl, P. Becker, H. Bettin, M. Borys, I. Busch, M. Gray, P. Fuchs, K. Fujii, H. Fujimoto, E. Kessler, M. Krumrey, U. Kuetgens, N. Kuramoto, G. Mana, P. Manson, E. Massa, S. Mizushima, A. Nicolaus, A. Picard, A. Pramann, O. Rienitz, D. Schiel, S. Valkiers, A. Waseda, Determination of the avogadro constant by counting the atoms in a<sup>28</sup> Si crystal, Phys. Rev. Lett. 106 (3) (2011) 030801, https://doi.org/10.1103/PhysRevLett.106.030801, URL <http://link.aps.org/doi/10.1103/PhysRevLett.106.030801>. 

- [36] R.E. George, W. Witzel, H. Riemann, N.V. Abrosimov, N. Nötzel, M.L.W. Thewalt, J.J.L. Morton, Electron spin coherence and electron nuclear double resonance of bi donors in natural si, Phys. Rev. Lett. 105 (2010) 067601, https://doi.org/10.1103/PhysRevLett.105.067601, URL <https://link.aps. org/doi/10.1103/PhysRevLett.105.067601>. 

- [37] S. Meiboom, D. Gill, Modified spin-echo method for measuring nuclear relaxation times, Rev. Sci. Instrum. 29 (8) (1958) 688, https://doi.org/ 10.1063/1.1716296, URL <http://link.aip.org/link/RSINAK/v29/i8/p688/s1& Agg=doi>. <http://scitation.aip.org/content/aip/journal/rsi/29/8/10.1063/1. 1716296>. 

- [38] W.-L. Ma, G. Wolfowicz, S.-s. Li, J.J.L. Morton, R.-b. Liu, Classical nature of nuclear spin noise near clock transitions of Bi donors in silicon, Phys. Rev. B 92 (16) (2015) 161403, https://doi.org/10.1103/PhysRevB.92.161403, URL <1505. 01604v1> <http://link.aps.org/doi/10.1103/PhysRevB.92.161403>. 

- [39] T.F. Watson, B. Weber, Y.-L. Hsueh, L.C.L. Hollenberg, R. Rahman, M.Y. Simmons, Atomically engineered electron spin lifetimes of 30 s in silicon, Sci. Adv. 3(3). http://advances.sciencemag.org/content/3/3/e1602811. https://doi.org/10.1126/sciadv.1602811. 

- [40] J.J. Pla, K.Y. Tan, J.P. Dehollain, W.H. Lim, J.J.L. Morton, D.N. Jamieson, A.S. Dzurak, A. Morello, A single-atom electron spin qubit in silicon, Nature 489 (7417) (2012) 541–545, https://doi.org/10.1038/nature11449, URL <http:// www.nature.com/nature/journal/v489/n7417/full/nature11449.html>. 

- [41] J.J. Pla, K.Y. Tan, J.P. Dehollain, W.H. Lim, J.J.L. Morton, F.A. Zwanenburg, D.N. Jamieson, A.S. Dzurak, A. Morello, High-fidelity readout and control of a nuclear spin qubit in silicon, Nature 496 (2013) 334. 

- [42] M. Steger, K. Saeedi, M.L.W. Thewalt, J.J.L. Morton, H. Riemann, N.V. Abrosimov, P. Becker, H.-J. Pohl, Quantum information storage for over 180 s using donor spins in a 28Si semiconductor vacuum, Science 336 (6086) (2012) 1280–1283, https://doi.org/10.1126/science.1217635, URL <http://www. ncbi.nlm.nih.gov/pubmed/22679091>. <https://www.sciencemag. org/content/336/6086/1280.short>. <http://www.sciencemag.org/cgi/doi/ 10.1126/science.1217635>. 

- [43] F. Jelezko, T. Gaebel, I. Popa, a. Gruber, J. Wrachtrup, Observation of coherent oscillations in a single electron spin, Phys. Rev. Lett. 92 (7) (2004) 1–4, https:// doi.org/10.1103/PhysRevLett.92.076401, URL <http://link.aps.org/doi/10. 1103/PhysRevLett.92.076401>. 

- [44] L. Robledo, L. Childress, H. Bernien, B. Hensen, P.A. Alkemade, R. Hanson, Highfidelity projective read-out of a solid-state spin quantum register, Nature 477 (2011) 547. 

- [45] T.H. Taminiau, J. Cramer, T. van der Sar, V.V. Dobrovitski, R. Hanson, Universal control and error correction in multi-qubit spin registers in diamond, Nat. Nanotechnol. 9 (3) (2014) 171–176, https://doi.org/10.1038/nnano.2014.2, URL <http://www.ncbi.nlm.nih.gov/pubmed/24487650>. 

- [46] B. Pingault, D.-D. Jarausch, C. Hepp, L. Klintberg, J.N. Becker, M. Markham, C. Becher, M. Atatüre, Coherent control of the silicon-vacancy spin in diamond, Nat. Commun. 8 (2017) 15579. 

- [47] L.J. Rogers, K.D. Jahnke, M.H. Metsch, A. Sipahigil, J.M. Binder, T. Teraji, H. Sumiya, J. Isoya, M.D. Lukin, P. Hemmer, F. Jelezko, All-optical initialization, readout, and coherent preparation of single silicon-vacancy spins in diamond, Phys. Rev. Lett. 113 (2014) 263602, https://doi.org/10.1103/ PhysRevLett.113.263602, URL <https://link.aps.org/doi/10.1103/ PhysRevLett.113.263602>. 

- [48] P. Siyushev, M.H. Metsch, A. Ijaz, J.M. Binder, M.K. Bhaskar, D.D. Sukachev, A. Sipahigil, R.E. Evans, C.T. Nguyen, M.D. Lukin, P.R. Hemmer, Y.N. Palyanov, I.N. Kupriyanov, Y.M. Borzdov, L.J. Rogers, F. Jelezko, Optical and microwave control of germanium-vacancy center spins in diamond. <1612.02947>. 

- [49] M.K. Bhaskar, D.D. Sukachev, A. Sipahigil, R.E. Evans, M.J. Burek, C.T. Nguyen, L. J. Rogers, P. Siyushev, M.H. Metsch, H. Park, F. Jelezko, M. Lonar, M.D. Lukin, Quantum nonlinear optics with a germanium-vacancy color center in a nanoscale diamond waveguide, Phys. Rev. Lett. 118 (2017) 223603, https://doi. 

J.J.L. Morton, P. Bertet / Journal of Magnetic Resonance 287 (2018) 128–139 

139 

org/10.1103/PhysRevLett.118.223603, URL <https://link.aps.org/doi/10.1103/ PhysRevLett.118.223603>. 

- [50] J.N. Becker, B. Pingault, D. Groß, M. Gündog�an, N. Kukharchyk, M. Markham, A. Edmonds, M. Atatüre, P. Bushev, C. Becher, All-optical Control of the Siliconvacancy Spin in Diamond at Millikelvin Temperatures. <1708.08263>. 

- [51] D.D. Sukachev, A. Sipahigil, C.T. Nguyen, M.K. Bhaskar, R.E. Evans, F. Jelezko, M. D. Lukin, The Silicon-vacancy Spin Qubit in Diamond: Quantum Memory Exceeding Ten Milliseconds and Single-shot State Readout. <1708.08852>. 

- [52] B.C. Rose, D. Huang, Z.-H. Zhang, A.M. Tyryshkin, S. Sangtawesin, S. Srinivasan, L. Loudin, M.L. Markham, A.M. Edmonds, D.J. Twitchen, S.A. Lyon, N.P. de Leon, Observation of An Environmentally Insensitive Solid State Spin Defect in Diamond. <1706.01555>. 

- [53] H. Seo, A. Falk, P. Klimov, K. Miao, G. Galli, D.D. Awschalom, Quantum decoherence dynamics of divacancy spins in silicon carbide, Nat. Commun. 7 (2016) 12935, URL <https://www.nature.com/ncomms/2016/160929/ ncomms12935/full/ncomms12935.html>. 

- [54] M. Hedges, J. Longdell, Y. Li, M. Sellars, Efficient quantum memory for light, Nature 465 (7301) (2010) 1052–1056, https://doi.org/10.1038/nature09081. 

- [55] C. O’Brien, N. Lauk, S. Blum, G. Morigi, M. Fleischhauer, Interfacing superconducting qubits and telecom photons via a rare-earth-doped crystal, Phys. Rev. Lett. 113 (2014) 063603, https://doi.org/10.1103/ PhysRevLett.113.063603, URL <https://link.aps.org/doi/10.1103/ PhysRevLett.113.063603>. 

- [56] Y.-H. Chen, X. Fernandez-Gonzalvo, J.J. Longdell, Coupling erbium spins to a three-dimensional superconducting cavity at zero magnetic field, Phys. Rev. B 94 (2016) 075117, https://doi.org/10.1103/PhysRevB.94.075117, URL <https://link.aps.org/doi/10.1103/PhysRevB.94.075117>. 

- [57] M. Rancˇic´, M. Hedges, R.L. Ahlefeldt, M.J. Sellars, Coherence time of over a second in a telecom-compatible quantum memory storage material, Nat. Phys. <1611.04315>. 

- [58] G. Wolfowicz, H. Maier-Flaig, R. Marino, A. Ferrier, H. Vezin, J.J.L. Morton, P. Goldner, Coherent storage of microwave excitations in rare-earth nuclear spins, Phys. Rev. Lett. 114 (17) (2015) 170503, https://doi.org/10.1103/ PhysRevLett.114.170503, URL <http://link.aps.org/doi/10.1103/PhysRevLett. 114.170503>. 

- [59] S. Bertaina, S. Gambarelli, A. Tkachuk, I. Kurkin, B. Malkin, A. Stepanov, B. Barbara, Rare-earth solid-state qubits, Nat. Nano 2 (2007) 39–42. 

- [60] H.-J. Lim, S. Welinski, M. Afzelius, P. Goldner, J.J.L. Morton, Coherent spin ensembles of ytterbium ions in yttrium orthosilicate, arXiv:1712.00435, 2017. 

- [61] R.M. Jock, Ph.D. thesis, Princeton University, 2015. 

- [62] M. Veldhorst, J.C.C. Hwang, C.H. Yang, a.W. Leenstra, B. de Ronde, J.P. Dehollain, J.T. Muhonen, F.E. Hudson, K.M. Itoh, A. Morello, a.S. Dzurak, An addressable quantum dot qubit with fault-tolerant control-fidelity, Nat. Nanotechnol. 9 (12) (2014) 981–985, https://doi.org/10.1038/nnano.2014.216, URL <1407. 1950v1> <http://www.nature.com/doifinder/10.1038/nnano.2014.216>. 

[63] E. Kawakami, P. Scarlino, D. Ward, F.R. Braakman, D.E. Savage, M.G. Lagally, M. Friesen, S.N. Coppersmith, M.A. Eriksson, L.M.K. Vandersypen, Electrical control of a long-lived spin qubit in a Si/SiGe quantum dot, Nat. Nanotechnol. 9 (2014) 666–670. 

- [64] M. Urdampilleta, A. Chatterjee, C.C. Lo, T. Kobayashi, J. Mansir, S. Barraud, A.C. Betz, S. Rogge, M.F. Gonzalez-Zalba, J.J.L. Morton, Charge dynamics and spin blockade in a hybrid double quantum dot in silicon, Phys. Rev. X 5 (2015) 031024, https://doi.org/10.1103/PhysRevX.5.031024, URL <https://link.aps. org/doi/10.1103/PhysRevX.5.031024>. 

- [65] S. Muralidharan, L. Li, J. Kim, N. Lütkenhaus, M. Lukin, L. Jiang, Optimal architectures for long distance quantum communication, Sci. Rep. 6 (2016) 20463. 

- [66] P. Rabl, D. DeMille, J.M. Doyle, M.D. Lukin, R.J. Schoelkopf, P. Zoller, Hybrid quantum processors: molecular ensembles as quantum memory for solid state circuits, Phys. Rev. Lett. 97 (2006) 033003, https://doi.org/10.1103/ PhysRevLett.97.033003, URL <https://link.aps.org/doi/10.1103/PhysRevLett. 97.033003>. 

- [67] C. Grezes, Y. Kubo, B. Julsgaard, T. Umeda, J. Isoya, H. Sumiya, H. Abe, S. Onoda, T. Ohshima, K. Nakamura, I. Diniz, A. Auffeves, V. Jacques, J.-F. Roch, D. Vion, D. Esteve, K. Moelmer, P. Bertet, Towards a spin-ensemble quantum memory for superconducting qubits, C.R. Phys. 17 (7) (2016) 693–704, https://doi.org/ 10.1016/j.crhy.2016.07.006, URL quantum microwaves/ Micro-ondes quantiques <http://www.sciencedirect.com/science/article/pii/ 

   - S1631070516300573>. 

- [68] Y. Kubo, C. Grezes, A. Dewes, T. Umeda, J. Isoya, H. Sumiya, N. Morishita, H. Abe, S. Onoda, T. Ohshima, V. Jacques, A. Dréau, J.-F. Roch, I. Diniz, A. Auffeves, D. Vion, D. Esteve, P. Bertet, Hybrid quantum circuit with a superconducting qubit coupled to a spin ensemble, Phys. Rev. Lett. 107 (2011) 220501, https:// doi.org/10.1103/PhysRevLett.107.220501, URL <https://link.aps.org/doi/10. 1103/PhysRevLett.107.220501>. 

- [69] J.H. Wesenberg, A. Ardavan, G.A.D. Briggs, J.J.L. Morton, R.J. Schoelkopf, D.I. Schuster, K. Mølmer, Quantum computing with an electron spin ensemble, Phys. Rev. Lett. 103 (2009) 070502, https://doi.org/10.1103/ PhysRevLett.103.070502, URL <https://link.aps.org/doi/10.1103/ PhysRevLett.103.070502>. 

- [70] C. Grezes, B. Julsgaard, Y. Kubo, M. Stern, T. Umeda, J. Isoya, H. Sumiya, H. Abe, S. Onoda, T. Ohshima, V. Jacques, J. Esteve, D. Vion, D. Esteve, K. Mølmer, P. Bertet, Multimode storage and retrieval of microwave fields in a spin ensemble, Phys. Rev. X 4 (2014) 021049, https://doi.org/10.1103/ PhysRevX.4.021049, URL <https://link.aps.org/doi/10.1103/PhysRevX.4. 021049>. 

- [71] E. Abe, H. Wu, A. Ardavan, J. Morton, Electron spin ensemble strongly coupled to a three-dimensional microwave cavity, Appl. Phys. Lett. <http://aip. scitation.org/doi/abs/10.1063/1.3601930>. 

- [72] D.I. Schuster, A.P. Sears, E. Ginossar, L. DiCarlo, L. Frunzio, J.J.L. Morton, H. Wu, G.A.D. Briggs, B.B. Buckley, D.D. Awschalom, R.J. Schoelkopf, Highcooperativity coupling of electron-spin ensembles to superconducting cavities, Phys. Rev. Lett. 105 (2010) 140501, https://doi.org/10.1103/ PhysRevLett.105.140501, URL <https://link.aps.org/doi/10.1103/ PhysRevLett.105.140501>. 

- [73] A. Sigillito, A. Tyryshkin, T. Schenkel, A. Houck, S. Lyon, All-electric control of donor nuclear spin qubits in silicon, Nat. Nano Adv. online publication SP-EP . https://doi.org/10.1038/nnano.2017.154. 

- [74] A. Bienfait, J.J. Pla, Y. Kubo, X. Zhou, M. Stern, C.C. Lo, C.D. Weis, T. Schenkel, D. Vion, D. Esteve, J.J.L. Morton, P. Bertet, Controlling spin relaxation with a cavity, Nature 531 (2016) 74. 

- [75] N. Samkharadze, A. Bruno, P. Scarlino, G. Zheng, D.P. DiVincenzo, L. DiCarlo, L. M.K. Vandersypen, High-kinetic-inductance superconducting nanowire resonators for circuit qed in a magnetic field, Phys. Rev. Appl. 5 (2016) 044004, https://doi.org/10.1103/PhysRevApplied.5.044004, URL <https://link. aps.org/doi/10.1103/PhysRevApplied.5.044004>. 

- [76] A.T. Asfaw, A.J. Sigillito, A.M. Tyryshkin, T. Schenkel, S.A. Lyon, Multi-frequency spin manipulation using rapidly tunable superconducting coplanar waveguide microresonators, Appl. Phys. Lett. 111 (3) (2017) 032601, https://doi.org/ 10.1063/1.4993930. 

- [77] C. Eichler, A.J. Sigillito, S.A. Lyon, J.R. Petta, Electron spin resonance at the level of 10<sup>4</sup> spins using low impedance superconducting resonators, Phys. Rev. Lett. 118 (2017) 037701, https://doi.org/10.1103/PhysRevLett.118.037701, URL <https://link.aps.org/doi/10.1103/PhysRevLett.118.037701>. 

- [78] E.M. Purcell, Spontaneous emission probabilities at radio frequencies, Phys. Rev. 69 (1946) 681, https://doi.org/10.1103/PhysRev.69.674.2. 

- [79] P. Goy, J.M. Raimond, M. Gross, S. Haroche, Observation of cavity-enhanced single-atom spontaneous emission, Phys. Rev. Lett. 50 (1983) 1903–1906, https://doi.org/10.1103/PhysRevLett.50.1903, URL <https://link.aps.org/doi/ 10.1103/PhysRevLett.50.1903>. 

- [80] A. Bienfait, Ph.D. thesis, Universit Paris-Sud, 2017. 

- [81] S. Probst, A. Bienfait, P. Campagne-Ibarcq, J.J. Pla, B. Albanese, J.F.D.S. Barbosa, T. Schenkel, D. Vion, D. Esteve, K. Moelmer, J.J.L. Morton, R. Heeres, P. Bertet, Inductive-detection electron-spin resonance spectroscopy with 65 spins/ hz sensitivity, Appl. Phys. Lett. 111 (20) (2017) 202604, https://doi.org/10.1063/ 1.5002540. 

- [82] Y. Kubo, F.R. Ong, P. Bertet, D. Vion, V. Jacques, D. Zheng, A. Dréau, J.-F. Roch, A. Auffeves, F. Jelezko, J. Wrachtrup, M.F. Barthe, P. Bergonzo, D. Esteve, Strong coupling of a spin ensemble to a superconducting resonator, Phys. Rev. Lett. 105 (2010) 140502, https://doi.org/10.1103/PhysRevLett.105.140502, URL <https://link.aps.org/doi/10.1103/PhysRevLett.105.140502>. 

- [83] O.W. Kennedy, J. Burnett, J.C. Fenton, P.A. Warburton, J.J.L. Morton, E. DupontFerrier, Tuneable superconducting resonators based upon a Ne FIB fabricated constriction nanoSQUID (in preparation). 

- [84] T.F. Prisner, M. Rohrer, K. Möbius, Pulsed 95 ghz high-field epr heterodyne spectrometer with high spectral and time resolution, Appl. Magn. Reson. 7 (2) (1994) 167–183, https://doi.org/10.1007/BF03162610. 

- [85] G.A. Rinard, R.W. Quine, S.S. Eaton, G.R. Eaton, Frequency dependence of epr signal intensity, 250 mhz to 9.1 ghz, J. Magn. Reson. 156 (1) (2002) 113–121, https://doi.org/10.1006/jmre.2002.2530, URL <http:// www.sciencedirect.com/science/article/pii/S1090780702925309>. 

- [86] A. Bienfait, J.J. Pla, Y. Kubo, M. Stern, X. Zhou, C.C. Lo, C.D. Weis, T. Schenkel, M. L.W. Thewalt, D. Vion, D. Esteve, B. Julsgaard, K. Moelmer, J.J.L. Morton, P. Bertet, Reaching the quantum limit of sensitivity in electron spin resonance, Nat. Nanotechnol. 11 (2016) 253. 

- [87] O. Yaakobi, L. Friedland, C. Macklin, I. Siddiqi, Parametric amplification in josephson junction embedded transmission lines, Phys. Rev. B 87 (2013) 144301, https://doi.org/10.1103/PhysRevB.87.144301, URL <https://link.aps. org/doi/10.1103/PhysRevB.87.144301>. 

- [88] X. Zhou, V. Schmitt, P. Bertet, D. Vion, W. Wustmann, V. Shumeiko, D. Esteve, High-gain weakly nonlinear flux-modulated josephson parametric amplifier using a squid array, Phys. Rev. B 89 (2014) 214517, https://doi.org/10.1103/ PhysRevB.89.214517, URL <https://link.aps.org/doi/10.1103/PhysRevB.89. 214517>. 

- [89] P. Haikka, Y. Kubo, A. Bienfait, P. Bertet, K. Mølmer, Proposal for detecting a single electron spin in a microwave resonator, Phys. Rev. A 95 (2017) 022306, https://doi.org/10.1103/PhysRevA.95.022306, URL <https://link.aps.org/doi/ 10.1103/PhysRevA.95.022306>. 

- [90] J.M. Franck, R.P. Barnes, T.J. Keller, T. Kaufmann, S. Han, Active cancellation a means to zero dead-time pulse epr, J. Magn. Reson. 261 (Supplement C) (2015) 199–204, https://doi.org/10.1016/j.jmr.2015.07.005, URL <http:// www.sciencedirect.com/science/article/pii/S1090780715001573>. 

- [91] S.E. de Graaf, A.V. Danilov, A. Adamyan, T. Bauch, S.E. Kubatkin, Magnetic field resilient superconducting fractal resonators for coupling to free spins, J. Appl. Phys. 112 (12) (2012) 123905, https://doi.org/10.1063/1.4769208. 

- [92] J. Pla, A. Bienfait, G. Pica, J. Mansir, F. Mohiyaddin, A. Morello, T. Schenkel, B. Lovett, J. Morton, P. Bertet, Strain-induced Spin Resonance Splittings in Silicon Devices. <1608.07346>. 

- [93] J. Mansir, P. Conti, Z. Zeng, J. Pla, P. Bertet, Y. Niquet, J. Morton, Linear hyperfine tuning of donor spins in silicon using hydrostatic strain. <1706.01555>. 

- [94] G. Wolfowicz, Ph.D. Thesis, UCL (2016). 

