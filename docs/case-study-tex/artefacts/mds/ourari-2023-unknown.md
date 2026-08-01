# **Indistinguishable telecom band photons from a single erbium ion in the solid state** 

Salim Ourari,<sup>1,</sup><sup>_∗_</sup> Łukasz Dusanowski,<sup>1,</sup><sup>_∗_</sup> Sebastian P. Horvath,<sup>1,</sup><sup>_∗_</sup> Mehmet T. Uysal,<sup>1,</sup><sup>_∗_</sup> Christopher M. Phenicie,<sup>1</sup> Paul Stevenson,<sup>1,</sup><sup>_†_</sup> Mouktik Raha,<sup>1</sup> Songtao Chen,<sup>1,</sup><sup>_‡_</sup> Robert J. Cava,<sup>2</sup> Nathalie P. de Leon,<sup>1</sup> and Jeff D. Thompson<sup>1,</sup><sup>_§_</sup> 

> 1 _Department of Electrical and Computer Engineering, Princeton University, Princeton, NJ 08544, USA_ 

> 2 _Department of Chemistry, Princeton University, Princeton, NJ 08544, USA_ 

Atomic defects in the solid state are a key component of quantum repeater networks for longdistance quantum communication [1]. Recently, there has been significant interest in rare earth ions [2–4], in particular Er<sup>3+</sup> for its telecom-band optical transition [5–7], but their application has been hampered by optical spectral diffusion precluding indistinguishable single photon generation. In this work we implant Er<sup>3+</sup> into CaWO4, a material that combines a non-polar site symmetry, low decoherence from nuclear spins [8], and is free of background rare earth ions, to realize significantly reduced optical spectral diffusion. For shallow implanted ions coupled to nanophotonic cavities with large Purcell factor, we observe single-scan optical linewidths of 150 kHz and long-term spectral diffusion of 63 kHz, both close to the Purcell-enhanced radiative linewidth of 21 kHz. This enables the observation of Hong-Ou-Mandel interference [9] between successively emitted photons with high visibility, measured after a 36 km delay line. We also observe spin relaxation times _T_ 1 = 3.7 s and _T_ 2 > 200 _µ_ s, with the latter limited by paramagnetic impurities in the crystal instead of nuclear spins. This represents a significant step towards the construction of telecom-band quantum repeater networks with single Er<sup>3+</sup> ions. 

Long-distance quantum networks are an enabling technology for quantum communication, distributed quantum computing and entanglement-enhanced sensing and metrology [10]. The rate of direct entanglement transmission with photons decreases exponentially with distance, but this can be overcome using quantum repeaters with memories [11]. In particular, single atom-like defects in the solid state [1] have been used to demonstrate key milestones including spin-photon entanglement [12, 13] and single-photon transistors [14], remote entanglement of spins [15], entanglement purification [16] and memory-enhanced quantum communication [17]. A challenge to deploying these techniques in long-distance networks is that atomic systems typically operate at transition frequencies outside of the low-loss window of optical fibers, requiring wavelength conversion for long-distance propagation [18, 19]. 

The rare earth ion Er<sup>3+</sup> has a telecom-band optical transition at a wavelength of 1.5 _µ_ m that is widely exploited for solid-state optical amplifiers, and in dilute ensembles, as a quantum memory for light [20, 21]. Er<sup>3+</sup> ions can have long spin [8, 22] and optical [23] coherence in a variety of host crystals, a property shared with other rare earth ions [24–26]. In recent years, micro- and nano-scale optical resonators have enabled the observation of enhanced single photon emission from Er<sup>3+</sup> and other rare earth ions [3–5, 7, 27], which has subsequently enabled single-shot spin readout [4, 28] and coupling to nearby nuclear spins that could serve as ancilla qubits [29–31]. However, a central challenge to the development of quantum repeaters with single rare earth ions is spectral diffusion, which is particularly pronounced in nanophotonic devices used to achieve fast optical emission from single rare earth ions [4, 5, 7]. To date, indistinguishable single photon emission from a single rare earth ion has not been observed. 

Rare earth ions also provide a unique opportunity for materials engineering, as they can be incorporated into a wide range of host crystals while preserving their basic properties, including the optical transition wavelength and spin configuration [32–35]. An ideal host material would incorporate Er<sup>3+</sup> on a non-polar site to suppress linear electric field shifts of the optical transition, and have a low concentration of nuclear spins, other magnetic impurities and particularly trace rare earth ions to allow long spin coherence and low fluorescence background [36]. 

In this work, we demonstrate indistinguishable single photon emission from a single Er<sup>3+</sup> ion coupled to a nanophotonic optical cavity. This is enabled by shallow ion implantation of Er<sup>3+</sup> into CaWO4, a host material satisfying the above criteria and for which long electron spin coherence has recently been demonstrated in Er<sup>3+</sup> ensembles at millikelvin temperatures [8]. By coupling the ions to silicon nanophotonic circuits, we observe individual ions with single-scan optical linewidths of 150 kHz, and emission rate enhancement by a factor of _P_ = 850 via the Purcell effect. Using a 36 km delay line, we observe Hong-Ou-Mandel (HOM) interference between successively emitted photons with a visibility of _V_ = 80(4)%. We also demonstrate spin initialization and single-shot readout with a fidelity _F_ = 0 _._ 972, as well as the preservation of electron spin coherence for more than 200 _µ_ s, limited by paramagnetic impurities in the sample. This demonstration is a key step for the development of quantum repeaters based on single rare earth ions, and Er<sup>3+</sup> in particular. 

Our samples are produced by introducing erbium into commercially available high purity CaWO4 using ion implantation with an energy of 35 keV, targeting a depth of 10 nm. In a test sample implanted with a high Er<sup>3+</sup> fluence of 1 _×_ 10<sup>12</sup> ions/cm<sup>2</sup> , we observe an ensemble optical spectrum at _T_ = 4 K consistent with substitutional Er<sup>3+</sup> 

2 

on the Ca<sup>2+</sup> site with S4 symmetry (Fig. 1a) [37, 38]. After annealing at 300<sup>_◦_</sup> C in air, the inhomogeneous optical linewidth of the Z1-Y1 transition at 1532.63 nm is 730 MHz (Fig. 1b). This is comparable to previously reported linewidths in bulk-doped samples (approximately 0.5-1 GHz [35, 39]), suggesting that the implantation damage is effectively removed by annealing. 

To resolve individual ions, we implant a second sample at a lower fluence of 5 _×_ 10<sup>9</sup> ions/cm<sup>2</sup> . Single ions are probed using a silicon photonic crystal cavity that is fabricated on a separate silicon-on-insulator wafer, and then bonded to the top surface of the CaWO4 substrate (Fig. 1c-d) [5]. The device and sample are cooled to _T_ = 0 _._ 47 K in a<sup>3</sup> He cryostat, with optical and microwave access provided with a scanning probe head [40]. We probe single ions in the device using photoluminescence excitation (PLE) spectroscopy, by sweeping the frequency of a pulsed laser and observing the time-delayed fluorescence through the cavity with a superconducting nanowire single photon detector (SNSPD). The spectrum contains clearly resolved lines from individual Er<sup>3+</sup> ions (Fig. 1e). The number of lines is roughly consistent with the expected number of ions in the cavity area _A_ = 1 _._ 3 _µ_ m<sup>2</sup> , suggesting a high conversion efficiency. The following experiments are performed on the ion indicated by the arrow. 

Coupling the Er<sup>3+</sup> ion to the cavity allows for optical preparation and measurement of the electron spin. We apply a magnetic field of _|B|_ = 600 G to lift the degeneracy of the _S_ = 1 _/_ 2 ground and excited states, resulting in two spinconserving transitions ( _A_ , _B_ ) and two spin-flip transitions ( _C_ , _D_ ) as shown in Fig. 2a-b (the magnetic moments for the ground and excited state are described in the supplementary information [41]). Tuning the cavity to the _A_ transition enhances the decay rate of the excited state, shortening the lifetime from 6.3 ms to _τ_ = 7 _._ 4 _µ_ s, corresponding to a Purcell factor of _P_ = 850 (Fig. 2c). To enable spin readout, we engineer a cycling transition by selectively enhancing the _A_ transition relative to _D_ by a combination of detuning from the cavity and preferential orientation of the transition dipole moment with respect to the cavity polarization [28], resulting in Γ _A/_ Γ _D ≈_ 1030(10) [41]. Spin initialization is performed by optical pumping on the _A_ or _B_ transitions while simultaneously driving the excited state MW _e_ transition [42]. In Fig. 2d, we demonstrate spin initialization and readout with an average fidelity of _F_ = 0 _._ 972 (Fig. 2d). The combination of high collection efficiency and low background from other Er<sup>3+</sup> ions allows for high-contrast optical Rabi oscillations (Fig. 2e). After a _π_ pulse, a single photon is detected with a probability _P_ 1 = 0 _._ 035, on top of a background count rate of _Pb_ = _P_ 1 _/_ 117. Both _P_ 1 and the signal-to-background ratio are larger than what is obtained with frequency converted NV centers by more than an order of magnitude [19], enabled by the high quantum efficiency and collection efficiency of the Er-cavity system. 

The linewidth of the spin-conserving transitions is determined using PLE spectroscopy. To avoid optical pumping, the excitation laser has two tones separated by approximately 1 GHz to drive the _A_ and _B_ transitions simultaneously. The typical linewidth of a single scan (1 minute) is approximately 150 kHz, while the line center has an r.m.s. fluctuation of 63 kHz over 12 hours (Fig. 2f). This represents a 100-fold improvement over previously reported linewidths for individual Er<sup>3+</sup> ions in nanophotonic cavities [5, 7, 42], and is to our knowledge the narrowest optical transition observed for a solid-state defect in a nanophotonic device. We note that similar linewidths have been observed for single Er<sup>3+</sup> ions in 19 _µ_ m thick Y2SiO5 membranes [6]. The single-scan linewidth is 7 times larger than the Purcell-enhanced radiative linewidth of the _A_ transition, Γ _r_ = 1 _/τ_ = 2 _π ×_ 21 _._ 4 kHz, however, photon echo experiments suggest that this linewidth is dominated by slow dynamics [41], such that indistinguishable photon emission may be possible on short timescales or with active feedback. 

We perform HOM two-photon interference measurements [9] on time-delayed photons using an unbalanced MachZehnder interferometer (MZI) with a ∆ _L_ = 36 km delay line in one arm (Fig. 3a). By tuning the repetition rate of the excitation pulses to match the delay time of the long arm (∆ _t_ = 175 _µ_ s), successive photons may arrive at the final beamsplitter simultaneously, and HOM interference will suppress the probability of detecting one photon at each output if the photons are indistinguishable. Experimentally, we observe strongly suppressed coincidences (Fig. 3b), indicating a high degree of indistinguishability. In a control experiment, we artificially broaden the photon in the short arm using a fiber stretcher driven by a noise source, restoring the coincidence rate expected for distinguishable photons (Fig. 3c). We measure an HOM coincidence rate of _R_ = 2 min<sup>_−_1</sup> , defined as the rate of simultaneous photon detection in the distinguishable photon case, corresponding to a per-shot coincidence probability of _Pc_ = 8 _._ 5 _×_ 10<sup>_−_6</sup> . 

The indistinguishability is quantified by the visibility _V_ [43], given by _V_ = 1 _−_ 2 _A_ 0 _/A|i|≥_ 2, where _A_ 0 is the integrated counts under the central peak and _A|i|≥_ 2 is the average integrated counts in each side peak (Fig. 3b). The visibility is maximized for a coincidence window approaching zero, however the number of photons within this window (the acceptance fraction) will also be small (Fig. 3e). For coincidences with photon detection times _t_ 1 _, t_ 2 separated by _|t_ 2 _− t_ 1 _| <_ 2 _τ_ (corresponding to an acceptance fraction of 63%), the raw visibility is over 70%, rising to 90% when the accidental coincidences from dark counts and ambient background are subtracted. Integrating under the entire peak in Fig. 3d and subtracting accidental coincidences gives _V_ = 80(4)%. The residual distinguishability has a significant contribution (4%) due to the MZI output beamsplitter ratio deviating from 50:50. Therefore, we conclude that the effective linewidth over hundreds of microseconds is only slightly larger than the radiative linewidth [41]. Lastly, we study the properties of the Er<sup>3+</sup> spin, which has the potential to serve as a quantum memory for spin- 

3 

photon entanglement. In bulk Er<sup>3+</sup> :CaWO4 , the magnetic moment is anisotropic with _gc_ = 1 _._ 25 and _ga_ = 8 _._ 38 [38]. However, for the individual ions studied in this work, we observe significantly distorted magnetic moments, including a variation of _g_ in the _aa_ -plane. These deviations can be reproduced with the inclusion of a small axial crystal field term [41], which may arise from proximity to the surface or the presence of a nearby defect. 

The spin relaxation time is _T_ 1 = 3 _._ 7 s, in line with previous reports [8], and is limited by the direct process with a _T_ 1 _∝_ 1 _/B_<sup>5</sup> dependence [41]. Ramsey and Hahn echo experiments give _T_ 2<sup>_∗_=247nsand</sup><sup>_T_2=44</sup><sup>_µ_s,respectively</sup> (Fig. 4c-d). An XY<sup>64</sup> dynamical decoupling sequence allows coherence to be preserved for longer than 200 _µ_ s (Fig. 4e), while also showing collapses and revivals due to the<sup>183</sup> W nuclear spin bath. 

The Hahn echo _T_ 2 is improved by one order of magnitude from Er<sup>3+</sup> :Y2SiO5 under similar conditions [42], but the coherence is still significantly shorter than predictions based on CCE simulations accounting for the<sup>183</sup> W nuclear spin bath ( _I_ = 1 _/_ 2, 14.3% abundance). This implicates paramagnetic impurities in the host crystal or on the surface as the primary source of decoherence, with an inferred density of approximately 3 _×_ 10<sup>16</sup> cm<sup>_−_3</sup> [41]. Indeed, longer spin echo coherence times of _T_ 2 = 23 ms were observed for bulk Er<sup>3+</sup> ensembles in CaWO4 in Ref [8] by operating at dilution refrigerator temperatures to freeze out paramagnetic impurities. Although the coherence is not limited by the nuclear spin bath, dips in coherence due to a single strongly coupled<sup>183</sup> W spin are observed in Fig. 4d. 

The results demonstrated in this work will enable spin-photon entanglement and HOM interference between multiple Er<sup>3+</sup> emitters with postselection using a narrow coincidence window or active tracking of the transition frequencies. In future work, the radiative linewidth can be further increased using cavities with higher _Q_ [44] or smaller mode volume [45]. Furthermore, more careful annealing or surface preparation may reduce the spectral diffusion. The flexibility to incorporate Er<sup>3+</sup> via ion implantation, instead of during growth, will allow future exploration of CaWO4 samples produced and refined using diverse techniques. Reducing the impurity concentration may also improve the optical linewidth: scaling the ground state magnetic linewidth 1 _/T_ 2<sup>_∗_totheopticaltransition</sup> implies a significant magnetic noise contribution of 2 _π ×_ 46 kHz. 

In this work, we have demonstrated an engineered material, ion-implanted Er<sup>3+</sup> :CaWO4, that enables indistinguishable single photon generation from a single rare earth ion in the telecom band. We attribute the improved performance to the higher Er<sup>3+</sup> site symmetry (compared to previous observations of single Er<sup>3+</sup> ions [5, 7, 27]). Spectral multiplexing of many ions per node [42], using quantum eraser techniques to overcome static frequency differences [46], will enable higher repetition rates over long fiber segments, while simultaneously reducing the coherence time requirements [47]. Additional storage capacity and functionality may be obtained from ancilla nuclear spin registers, as recently demonstrated for several rare-earth ion systems [30, 31], and ion implantation may allow for the creation of spatially modulated density profiles with strong magnetic ion-ion interactions. 

_Acknowledgements:_ We acknowledge helpful conversations with Charles Thiel, Philippe Goldner, and Miloš Rančić. This work was primarily supported by the U.S. Department of Energy, Office of Science, National Quantum Information Science Research Centers, Co-design Center for Quantum Advantage (C2QA) under contract number DE-SC0012704. We also acknowledge support from the DOE Early Career award (for modeling of decoherence mechanisms and spin interactions), as well as AFOSR (FA9550-18-1-0334 and YIP FA9550-18-1-0081), the Eric and Wendy Schmidt Transformative Technology Fund, and DARPA DRINQS (D18AC00015) for establishing the materials spectroscopy pipeline and developing integrated nanophotonic devices. We acknowledge the use of Princeton’s Imaging and Analysis Center, which is partially supported by the PCCM, an NSF MRSEC (DMR1420541), as well as the Princeton Micro-Nano Fabrication Center. 

_Note:_ While finalizing this manuscript, we became aware of recent reporting the detection of single Er<sup>3+</sup> ions in CaWO4 using magnetic resonance techniques [48]. 

4 









<!-- Start of picture text -->
a c d<br>silicon cavity<br>Er (i) (i)<br>Ca<br>W<br>O<br>Y<br>Z Y e X Z ~10 nm<br>X 5 µm Y X X<br>a implanted Er 3+  CaWO4<br>a = 5.2 Å<br>b (ii) e<br>0.010<br>(ii)<br>0.005<br>Y 0.000<br>−6 −3 0 3 6 20 µm 2 µm X −500 −250 0 250 500<br>Laser frequency (GHz)<br>- 1532.62 nm Laser frequency (MHz)<br>FIG. 1. Er 3+ :CaWO 4 device architecture. a  CaWO44 crystal structure, with a substitutional Er 3+ impurity in an S44 Ca 2+<br>site. b  A dense implanted Er 3+ :CaWO44 ensemble has an inhomogeneous optical linewidth of 730 MHz on the Z1-Y11-Y1-Y11 transition.<br>addition to the central peak, we observe hyperfine structure from 167 Er with nuclear spin I = 7 / 2.. c Scanning electron<br>microscope image of a representative silicon nanophotonic device, consisting of a photonic crystal grating coupler [inset ( i )]<br>that tapers adiabatically into a bus waveguide connected to a photonic crystal nanobeam cavity [inset ( ii )]. d Erbium ions<br>implanted targeting a depth of 10 nm, and couple evanescently to the silicon photonic crystal on the surface. e PLE<br>spectrum of Er 3+ ions coupled to the cavity, with resolved single ion lines. The red arrow indicates the ion used for subsequent<br>experiments.<br>a c e f 12<br>6 GHz |↑ e ⟩ MWe |↓ e ⟩ 0.035<br>10<br>A D C B 0.018<br>1532 nm<br>8<br>7 GHz |↑ g ⟩ MW 0.000<br>g |↓ g ⟩ 100 101 102 103 104 0 300 600<br>Time (µs) Optical pulse width (ns) 6<br>b d 100 5.00<br>10−1 init.init . |↑ |↓ gg ⟩⟩ 4<br>10−2 4.75 2<br>C A B D −3<br>10<br>−10 −5 0 5 10 10−4 4.50 0<br>0 5 10 15 −500 −250 0 250 500 −500 −250 0 250 500<br>Frequency (GHz)<br>Number of photons Detuning (kHz) Detuning (kHz)<br>c = 11.4 Å<br>Fluorescence (a.u.) Counts per pulse<br>Counts per pulse<br>Fluorescence (a.u.)<br>Time (hours)<br>Reflection Probability<br>Time (hours)<br><!-- End of picture text -->



<!-- Start of picture text -->
silicon cavity<br>~10 nm<br><!-- End of picture text -->

FIG. 1. **Er**<sup>3+</sup> **:CaWO** 4 **device architecture. a** CaWO44 crystal structure, with a substitutional Er<sup>3+</sup> impurity in an S44 Ca<sup>2+</sup> site. **b** A dense implanted Er<sup>3+</sup> :CaWO44 ensemble has an inhomogeneous optical linewidth of 730 MHz on the Z1-Y11-Y1-Y11 transition. In addition to the central peak, we observe hyperfine structure from<sup>167</sup> Er with nuclear spin _I_ = 7 _/_ 2.. **c** Scanning electron microscope image of a representative silicon nanophotonic device, consisting of a photonic crystal grating coupler [inset ( _i_ )] that tapers adiabatically into a bus waveguide connected to a photonic crystal nanobeam cavity [inset ( _ii_ )]. **d** Erbium ions are implanted targeting a depth of 10 nm, and couple evanescently to the silicon photonic crystal on the surface. **e** PLE spectrum of Er<sup>3+</sup> ions coupled to the cavity, with resolved single ion lines. The red arrow indicates the ion used for subsequent experiments. 



<!-- Start of picture text -->
[inset ( ii )]. d Erbium ions<br>crystal on the surface. e PLE<br>f 12<br>10<br>8<br>6<br>4<br>2<br>0<br>500 −500 −250 0 250 500<br>Detuning (kHz)<br>Time (hours)<br><!-- End of picture text -->

FIG. 2. **Efficient photon collection from a cavity-coupled ion. a** Er<sup>3+</sup> level structure. In a magnetic field, Er<sup>3+</sup> has four distinct optical transitions. The field strength is _|B|_ = 600 G, oriented in the _aa_ -plane, 22<sup>_o_</sup> from the _X_ -axis. **b** Reflection spectrum of the cavity showing a full-width, half-maximum linewidth of _κ_ = 1 _._ 0 GHz ( _Q_ = 1 _._ 9 _×_ 10<sup>5</sup> ), which is tuned into resonance with the _A_ transition. **c** The lifetime of the _|↑_ e _⟩_ excited state is reduced to 7 _._ 4 _µ_ s (blue), which is 850 times shorter than the bulk lifetime of 6.3 ms (orange). **d** Histogram of photon counts obtained during spin readout after initializing in _|↑g⟩_ and _|↓g⟩_ . The average readout fidelity¯ is _F_ = 0 _._ 972, using a threshold of one photon. The solid line is a fit to a Poisson distribution with average photon number _n_ = 6 _._ 4. **e** Optical Rabi oscillation on transition _A_ . The peak single photon emission probability is _P_ 1 = 0 _._ 035. **f** Repeated PLE scans show an average single-scan linewidth of 150 kHz, and long-term diffusion of the line center of 63 kHz. 

5 



<!-- Start of picture text -->
a<br>∆t<br><!-- End of picture text -->



<!-- Start of picture text -->
a d<br>36 km<br>∆t fiber PC SNSPD 0.5<br>75:25 50:50<br>0.4<br>BS BS<br>fiber 0.3<br>VOA PC stretcher<br>0.2<br>SNSPD 0.1<br>FG<br>b<br>0.0<br>−30 −15 0 15 30<br>80 A-3 A-2 A-1 A1 A2 A3 Detection time difference  t 1 − t 2  ( μ s)<br>60 e<br>1.0<br>40<br>0.9<br>20 A0 0.8<br>0.7<br>0<br>0.6<br>c 80 −525 −350 −175 0 175 350 525<br>0.5<br>1.0<br>60<br>0.8<br>40 0.6<br>0.4<br>20<br>0.2<br>0 0.0<br>−525 −350 −175 0 175 350 525 0.0 0.5 1.0 1.5 2.0<br>Detection time difference  t 1 − t 2  ( μ s) Coincidence window /  (2 T 1)<br>orm. HOM coincidences<br>N<br>HOM coincidences<br>Visibility<br>HOM coincidences<br>Acceptance fraction<br><!-- End of picture text -->

FIG. 3. **Generation of indistinguishable photons. a** Schematic of the HOM interferometer, indicating beamsplitters (BS), a variable optical attenuator (VOA), polarization controllers (PC) and a fiber stretcher driven by a noise source (FG) to tune the distinguishability. **b** Histogram of coincidences detected in a 4 hour measurement period. The Hong-Ou-Mandel effect results in a suppressed probability of coincidences at zero delay, indicating indistinguishable single-photon emission. **c** Histogram of coincidences in a control experiment with a noise source applied to the fiber stretcher, destroying the indistinguishability and Hong–Ou–Mandel interference. **d** Zoom-in around the zero time delay HOM interference pattern. The red line shows a model including background counts (black dashed line) and pure dephasing of the optical transition. The blue dashed line shows a simple model for the control experiment assuming perfect distinguishability, while the solid blue line shows a model incorporating the finite bandwidth of the noise source [41]. **e** Interference visibility (top) and relative coincidence rate (bottom) as a function of the coincidence window, before (green) and after (red) subtracting the accidental coincidences from the detector and ambient background dark counts. 

6 



<!-- Start of picture text -->
a b<br>1.0 1.00<br>0.5 0.75<br>0.0 0.50<br>0 150 300 0 5 10<br>MWg pulse width (ns) Wait time (s)<br>c d<br>1.00 1.00<br>0.75 0.75<br>0.50 0.50<br>0.0 0.4 0.8 0 50 100<br>e Free evolution time (µs)  Free evolution time (µs)<br>1.0<br>0.8<br>0.6<br>0.4<br>0 200 400 600 800 1000 1200<br>Free evolution time (µs)<br>⟩|↑g ⟩|↑g<br>Population  Population<br>⟩|↑g ⟩|↓g<br>Population  Population<br>⟩|↑g<br>Population<br><!-- End of picture text -->

FIG. 4. **Spin dynamics. a** Rabi oscillations after initializing into _|↑g⟩_ (blue) or _|↓g⟩_ (orange). The spin transition frequency _f_ MW _g_ = 7.0 GHz. **b** Spin relaxation after initialization into _|↑g⟩_ . An exponential fit yields _T_ 1 = 3 _._ 7(3) s. **c** Ramsey measurement. Fitting to _e_<sup>_−_(</sup><sup>_t/T_</sup> 2<sup>_∗_)</sup><sup>_n_</sup> reveals a _T_ 2<sup>_∗_=247(9)nswith</sup><sup>_n_=2</sup><sup>_._2(3).</sup><sup>**d**AHahnechomeasurementshowsdips</sup> in coherence resulting from the<sup>183</sup> W nuclear spin bath. The grey lines show CCE simulations for randomly selected<sup>183</sup> W configurations, where each configuration includes a single strongly coupled<sup>183</sup> W spin required to reproduce the dips. The blue lines include an additional, phenomenological stretched decay with _T_ 2 = 44 _µ_ s. **e** Applying an XY<sup>64</sup> dynamical decoupling sequence extends the spin coherence to longer times. Here, the grey lines show CCE simulations for the same<sup>183</sup> W bath configurations in panel (d), while the blue lines have an additional phenomenological decay of 460 _µ_ s. 

7 

- _∗_ These authors contributed equally to this work. 

- Present address: Department of Physics, Northeastern University, Boston, Massachusetts 02115, USA 

- Present address: Department of Electrical and Computer Engineering, Rice University, Houston, Texas 77005, USA 

- _§_ jdthompson@princeton.edu 

- [1] Awschalom, D. D., Hanson, R., Wrachtrup, J. & Zhou, B. B. Quantum technologies with optically interfaced solid-state spins. _Nature Photonics_ **12** , 516–527 (2018). 

- [2] Simon, C. _et al._ Quantum memories. _The European Physical Journal D_ **58** , 1–22 (2010). 

- [3] Zhong, T. _et al._ Optically addressing single rare-earth ions in a nanophotonic cavity. _Physical Review Letters_ **121** , 183603 (2018). 

- [4] Kindem, J. M. _et al._ Control and single-shot readout of an ion embedded in a nanophotonic cavity. _Nature_ **580** , 201–204 (2020). 

- [5] Dibos, A. M., Raha, M., Phenicie, C. M. & Thompson, J. D. Atomic Source of Single Photons in the Telecom Band. _Physical Review Letters_ **120** , 243601 (2018). 

- [6] Ulanowski, A., Merkel, B. & Reiserer, A. Spectral multiplexing of telecom emitters with stable transition frequency. _Science Advances_ **8** , eabo4538 (2022). 

- [7] Yang, L., Wang, S., Shen, M., Xie, J. & Tang, H. X. Controlling single rare earth ion emission in an electro-optical nanocavity. Preprint at http://arxiv.org/abs/2211.12449 (2022). 

- [8] LeDantec, M. _et al._ Twenty-three–millisecond electron spin coherence of erbium ions in a natural-abundance crystal. _Science Advances_ **7** , eabj9786 (2021). 

- [9] Hong, C. K., Ou, Z. Y. & Mandel, L. Measurement of subpicosecond time intervals between two photons by interference. _Physical Review Letters_ **59** , 2044–2046 (1987). 

- [10] Awschalom, D. _et al._ Development of quantum interconnects (quics) for next-generation information technologies. _PRX Quantum_ **2** , 017002 (2021). 

- [11] Briegel, H.-J., Dür, W., Cirac, J. I. & Zoller, P. Quantum repeaters: The role of imperfect local operations in quantum communication. _Physical Review Letters_ **81** , 5932–5935 (1998). 

- [12] Togan, E. _et al._ Quantum entanglement between an optical photon and a solid-state spin qubit. _Nature_ **466** , 730–734 (2010). 

- [13] De Greve, K. _et al._ Quantum-dot spin-photon entanglement via frequency downconversion to telecom wavelength. _Nature_ **491** , 421 (2012). 

- [14] Sun, S., Kim, H., Luo, Z., Solomon, G. S. & Waks, E. A single-photon switch and transistor enabled by a solid-state quantum memory. _Science_ **361** , 57–60 (2018). 

- [15] Bernien, H. _et al._ Heralded entanglement between solid-state qubits separated by three metres. _Nature_ **497** , 86–90 (2013). 

- [16] Kalb, N. _et al._ Entanglement distillation between solid-state quantum network nodes. _Science_ **356** , 928–932 (2017). 

- [17] Bhaskar, M. K. _et al._ Experimental demonstration of memory-enhanced quantum communication. _Nature_ **580** , 60–64 (2020). 

- [18] Li, Q., Davanço, M. & Srinivasan, K. Efficient and low-noise single-photon-level frequency conversion interfaces using silicon nanophotonics. _Nature Photonics_ **10** , 406–414 (2016). 

- [19] Stolk, A. _et al._ Telecom-band quantum interference of frequency-converted photons from remote detuned NV centers. _PRX Quantum_ **3** , 020359 (2022). 

- [20] Saglamyurek, E. _et al._ Quantum storage of entangled telecom-wavelength photons in an erbium-doped optical fibre. _Nature Photonics_ **9** , 83–87 (2015). 

- [21] Craiciu, I. _et al._ Nanophotonic quantum storage at telecommunication wavelength. _Physical Review Applied_ **12** , 024062 (2019). 

- [22] Rančić, M., Hedges, M. P., Ahlefeldt, R. L. & Sellars, M. J. Coherence time of over a second in a telecom-compatible quantum memory storage material. _Nature Physics_ **14** , 50–54 (2018). 

- [23] Böttger, T., Thiel, C. W., Cone, R. L. & Sun, Y. Effects of magnetic field orientation on optical decoherence in Er<sup>3+</sup> :Y2SiO5. _Physical Review B_ **79** , 115104 (2009). 

- [24] Zhong, M. _et al._ Optically addressable nuclear spins in a solid with a six-hour coherence time. _Nature_ **517** , 177–180 (2015). 

- [25] Ortu, A. _et al._ Simultaneous coherence enhancement of optical and microwave transitions in solid-state electronic spins. _Nature Materials_ **17** , 671–675 (2018). 

- [26] Kindem, J. M. _et al._ Characterization of<sup>171</sup> Yb<sup>3+</sup> :YVO4 for photonic quantum technologies. _Physical Review B_ **98** , 024404 (2018). 

- [27] Ulanowski, A., Merkel, B. & Reiserer, A. Spectral multiplexing of telecom emitters with stable transition frequency. _Science Advances_ **8** , 4538 (2022). 

- [28] Raha, M. _et al._ Optical quantum nondemolition measurement of a single rare earth ion qubit. _Nature Communications_ **11** , 1605 (2020). 

- [29] Kornher, T. _et al._ Sensing individual nuclear spins with a single rare-earth electron spin. _Physical Review Letters_ **124** , 170402 (2020). 

- [30] Ruskuc, A., Wu, C.-J., Rochman, J., Choi, J. & Faraon, A. Nuclear spin-wave quantum register for a solid-state qubit. _Nature_ **602** , 408–413 (2022). 

- [31] Uysal, M. T. _et al._ Coherent control of a nuclear spin via interactions with a rare-earth ion in the solid-state. Preprint 

8 

at http://arxiv.org/abs/2209.05631 (2022). 

- [32] Thiel, C. W., Böttger, T. & Cone, R. L. Rare-earth-doped materials for applications in quantum information storage and signal processing. _Journal of Luminescence_ **131** , 353–361 (2011). 

- [33] Zhong, T. & Goldner, P. Emerging rare-earth doped material platforms for quantum nanophotonics. _Nanophotonics_ **8** , 2003–2015 (2019). 

- [34] Phenicie, C. M. _et al._ Narrow optical line widths in erbium implanted in TiO2. _Nano Letters_ **19** , 8928–8933 (2019). 

- [35] Stevenson, P. _et al._ Erbium-implanted materials for quantum communication applications. _Physical Review B_ **105** , 224106 (2022). 

- [36] Ferrenti, A. M., de Leon, N. P., Thompson, J. D. & Cava, R. J. Identifying candidate hosts for quantum defects via data mining. _npj Computational Materials_ **6** , 126 (2020). 

- [37] Nassau, K. & Loiacono, G. Calcium tungstate—III: Trivalent rare earth ion substitution. _Journal of Physics and Chemistry of Solids_ **24** , 1503–1510 (1963). 

- [38] Enrique, B. G. Optical spectrum and magnetic properties of Er<sup>3+</sup> in CaWO4. _The Journal of Chemical Physics_ **55** , 2538–2549 (1971). 

- [39] Sun, Y., Thiel, C., Cone, R., Equall, R. & Hutcheson, R. Recent progress in developing new rare earth materials for hole burning and coherent transient applications. _Journal of Luminescence_ **98** , 281–287 (2002). 

- [40] Chen, S. _et al._ Hybrid microwave-optical scanning probe for addressing solid-state spins in nanophotonic cavities. _Optics Express_ **29** , 4902 (2021). 

- [41] Supplementary Information. 

- [42] Chen, S., Raha, M., Phenicie, C. M., Ourari, S. & Thompson, J. D. Parallel single-shot measurement and coherent control of solid-state spins below the diffraction limit. _Science_ **370** , 592–595 (2020). 

- [43] Santori, C., Fattal, D., Vucković, J., Solomon, G. S. & Yamamoto, Y. Indistinguishable photons from a single-photon device. _Nature_ **419** , 594 (2002). 

- [44] Asano, T., Ochi, Y., Takahashi, Y., Kishimoto, K. & Noda, S. Photonic crystal nanocavity with a Q factor exceeding eleven million. _Optics Express_ **25** , 1769 (2017). 

- [45] Hu, S. & Weiss, S. M. Design of photonic crystal cavities for extreme light concentration. _ACS Photonics_ **3** , 1647–1653 (2016). 

- [46] Zhao, T.-M. _et al._ Entangling different-color photons via time-resolved measurement and active feed forward. _Physical Review Letters_ **112** , 103602 (2014). 

- [47] Collins, O. A., Jenkins, S. D., Kuzmich, A. & Kennedy, T. A. B. Multiplexed memory-insensitive quantum repeaters. _Physical Review Letters_ **98** , 060502 (2007). 

- [48] Wang, Z. _et al._ Single electron-spin-resonance detection by microwave photon counting (2023). URL `https://arxiv. org/abs/2301.02653` . 

# **Supplementary information for indistinguishable telecom band photons from a single erbium ion in the solid state** 

Salim Ourari,<sup>1,</sup><sup>_∗_</sup> Łukasz Dusanowski,<sup>1,</sup><sup>_∗_</sup> Sebastian P. Horvath,<sup>1,</sup><sup>_∗_</sup> Mehmet T. Uysal,<sup>1,</sup><sup>_∗_</sup> Christopher M. Phenicie,<sup>1</sup> Paul Stevenson,<sup>1</sup> Mouktik Raha,<sup>1</sup> Songtao Chen,<sup>1</sup> Robert J. Cava,<sup>2</sup> Nathalie P. de Leon,<sup>1</sup> and Jeff D. Thompson<sup>1,</sup><sup>_†_</sup> 1 _Department of Electrical and Computer Engineering, Princeton University, Princeton, NJ 08544, USA_ 2 _Department of Chemistry, Princeton University, Princeton, NJ 08544, USA_ 

## **CONTENTS** 

|I. Photon collection efciency|1|
|---|---|
|II. CaWO4 sample preparation|2|
|III. Site-selective excitation spectroscopy|2|
|IV. Spin state initialization and readout|3|
|V. Engineering an optical cycling transition|3|
|VI. Photon echo investigation of the optical coherence|4|
|VII. HOM ft functions|4|
|VIII. Distortion of the magnetic moment tensor|7|
|IX. Dependence of _T_1 on magnetic feld|8|
|X. Spin coherence modeling|8|
|XI. Estimating concentration of paramagnetic impurities|10|
|References|12|
|**I.**<br>**PHOTON COLLECTION EFFICIENCY**||



This section details the efficiency of components in our photonic circuit that impact the total photon collection efficiency. We group these losses into four terms: internal losses in the cavity, in the grating coupler and waveguide taper, transmission through passive optical components, and the quantum efficiency of the SNSPDs. 

The internal losses in the cavity are determined from the reflection spectrum. In particular, the contrast of the reflection on and off cavity resonance _C_ = ( _R_ off _− R_ on) _/R_ off has the form [1]: 



The photon extraction efficiency from the cavity _η_ cav = _κ_ wg _/κ_ tot is the ratio of cavity outcoupling rate _κ_ wg to the total loss _κ_ tot = _κ_ wg + _κ_ int, including internal cavity losses _κ_ int. For the device used in this work, we find _η_ cav = 0 _._ 26. The grating coupler and waveguide efficiency is estimated by measuring the round-trip optical losses away from the cavity resonance. We compute the efficiency as _η_ GC = � _P_ out _/P_ in, and find _η_ GC = 0 _._ 36 for the device used in this work. The transmission through passive optical components (beamsplitters, splices, etc.) is measured independently to be _η_ net = 0 _._ 61 (the HOM interferometer has additional losses, discussed below). The detection efficiency of the SNSPD is _η_ det = 0 _._ 85. This gives a combined predicted photon detection probability of _P_ 1 = _η_ cav _× η_ GC _× η_ net _× η_ det = 0 _._ 049. We lose an additional 7% of the single-ion emission from the finite time required to switch on the SNSPD bias current ( _≈_ 900 ns), which is turned off during the optical excitation pulse to avoid saturating the detector. The predicted photon detection probability is then _P_ 1 = 0 _._ 045, close to the measured value of 0.035. 

2 

In the HOM experiment, the two-photon coincidence probability is decreased by the losses of the MZI delay line. We measured the optical transmission in the 36 km fiber spool to be _T_ = 0 _._ 2, consistent with an attenuation length _La_ = 21 _._ 7 km. To maximize the coincidence probability and balance the power in the two arms of the interferometer, we use a 75 : 25 ratio beamsplitter at the input, such that 0.75 of the power is directed into the long MZI arm, while 0.25 is directed into the short one. In the shorter arm, we utilize a variable optical attenuator set to match the powers before the final MZI beamsplitter input ports. Accounting for both the losses in the fiber spool in the long interferometer arm (matched with a VOA on the short arm), as well as the beamsplitter ratio, the two-photon coincidence probability at _|t_ 1 _− t_ 2 _|_ = 0 is _P_ HOM = 0 _._ 5 _×_ (0 _._ 75 _P_ 1 _T_ )<sup>2</sup> = 0 _._ 01 _P_ 1<sup>2.Here,thefactorof0.5accountsfor</sup> the requirement that the early (late) photon must pass through the long (short) interferometer arm. For _P_ 1 = 0 _._ 035 we get _P_ HOM = 1 _._ 4 _×_ 10<sup>_−_5</sup> , close to the measured value of 8 _._ 5 _×_ 10<sup>_−_6</sup> . 

## **II. CAWO** 4 **SAMPLE PREPARATION** 

The CaWO4 substrates used in this study were procured from SurfaceNet GmbH with a single sided epi polish and (100) orientation ( _i.e._ , with a surface spanned by _a_ and _c_ axes). According to the vendor, the crystals were grown using 99.9999% purity precursors and sold as “high purity CaWO4.” Polished samples were implanted with erbium (II-VI Inc.) using an energy of 35 keV which corresponds to a target depth of 10 nm (calculated by Stopping-Range of Ions in Matter simulations [2]). Samples were prepared using two different Er<sup>3+</sup> concentrations, a high density sample used for ensemble spectroscopy utilizing a fluence of 1 _×_ 10<sup>12</sup> ions/cm<sup>2</sup> and a low density sample used for single ion spectroscopy implanted with a fluence of 5 _×_ 10<sup>9</sup> ions/cm<sup>2</sup> . Subsequent to implantation, samples were annealed in air at a temperature of _T_ = 300<sup>_◦_</sup> C for 1 hour, with a heating rate of _T_ = 300<sup>_◦_</sup> C/hour. Annealing healed implantation damage and improved site occupation of the S4 point-group symmetry substitutional site. 

Silicon photonic crystal cavities are prepared as described previously [3]. The cavities are oriented on the substrate such that the predominant electric field polarization is parallel to the CaWO4 _c_ -axis. 

## **III. SITE-SELECTIVE EXCITATION SPECTROSCOPY** 

In order to confirm that implanted Er<sup>3+</sup> ions substitute at a site with S4 symmetry we performed a site-selective excitation spectroscopy measurement using the high density sample cooled to 4 K. A tunable narrowband laser was employed in conjunction with an optical chopper to generate a train of excitation pulses. Using a second chopper, fluorescence was collected out of phase with the excitation laser, dispersed using a monochromator, and detected with an InGaAs detector array. By performing a fluorescence measurement while sweeping the excitation laser a map of site-specific excitation and emission frequencies was obtained (Fig. S1a). Table S1 summarizes the measured transition energies of four<sup>4</sup> I15 _/_ 2 and three<sup>4</sup> I13 _/_ 2 levels. The resulting energy level structure is shown in Fig. S1b, and found to be in close agreement with the transition energies previously reported for bulk doped samples [4], confirming the S4 site assignment. The spectrum does not show any detectable fluorescence at other wavelengths within our scan range, suggesting that this is the only Er<sup>3+</sup> incorporation site. 

TABLE S1. Transition energies of implanted Er<sup>3+</sup> :CaWO4 determined using site-selective excitation spectroscopy. All values are in cm<sup>_−_1</sup> . Transitions to Z _n_ and Y _n_ for _n_ greater than what is shown were not observed due to limitations in detection sensitivity. The observed transition energies are in close agreement with values obtained for bulk doped samples [4]. 

|n|4I15_/_2Z_n_|4I13_/_2Y_n_|
|---|---|---|
|1|0|6524.4|
|2|20.3|6532.9|
|3|25.9|6573.2|
|4|52.0|*|



We note that compared to the optical excited state lifetime of 6.3 ms the Y _n_ crystal field levels thermalize rapidly, such that an identical fluorescence spectrum is obtained independent of which<sup>4</sup> I13 _/_ 2 level is excited (green arrows in Fig. S1). Furthermore, while the fluorescence spectrum is dominated by decay from the<sup>4</sup> I13 _/_ 2Y1 level, a small fraction of fluorescence originates from the<sup>4</sup> I13 _/_ 2Y2 level. This leads to two sets of fluorescence patterns with identical energy splittings (but different intensities), overlaid with an offset given by the<sup>4</sup> I13 _/_ 2Y1-<sup>4</sup> I13 _/_ 2Y2 splitting (indicated using dashed arrows in Fig. S1). 

3 





FIG. S1. **Ensemble spectroscopy of Er**<sup>3+</sup> **:CaWO** 4. **a** Site-selective excitation spectrum of Er<sup>3+</sup> :CaWO4. Green arrows indicate when the excitation laser is resonant with different excited state crystal-field levels, where the corresponding excitation path is labeled using the matching number in (b). Solid orange arrows denote the fluorescence energies due to decay from the<sup>4</sup> I13 _/_ 2Y1 level, whereas the dashed arrows denote decay from the<sup>4</sup> I13 _/_ 2Y2 level. The prominent line with unity gradient corresponds to laser scatter and has been re-scaled in intensity for clarity. **b** The inferred energy level structure of Er<sup>3+</sup> :CaWO4. In total, the performed spectroscopy yielded energies of four<sup>4</sup> I15 _/_ 2 and three<sup>4</sup> I13 _/_ 2 levels. 

## **IV. SPIN STATE INITIALIZATION AND READOUT** 

To achieve fast and efficient spin state initialization we follow the approach used in Ref. [5]. This initialization scheme consists of using optical _π_ pulses resonant with either the _A_ or _B_ transition, each followed by a microwave pulse resonant with the excited state spin transition, MW _e_ . For example, to initialize into the _|↓g⟩_ state we alternate _π_ pulses resonant with the optical _A_ and MW _e_ transitions. The number of pulse pairs used for the HOM and spin dynamics experiments was 1 and 10, respectively. 

For spin state readout, we used a sequence of _n_ optical _π_ pulses resonant with the _A_ transition each followed by a fluorescence collection window. By varying the number of readout pulses we found that the spin state readout fidelity is maximized for _n_ = 195, and applying further pulses would reduce the readout fidelity due to optical pumping. After optimizing the number of readout pulses, a threshold was set for the total number of photons collected after _n_ pulses ( _N_ thresh) to discriminate between the _|↓g⟩_ and _|↑g⟩_ states. We found that a threshold of _N_ thresh = 1 gives the highest readout fidelity; that is, if we obtained on average one photon or more after the _n_ pulses then the spin state was assigned to _|↑g⟩_ , and if we obtained no photon then the spin state was assigned to _|↓g⟩_ . 

## **V. ENGINEERING AN OPTICAL CYCLING TRANSITION** 

As noted in Ref. [6] for Er<sup>3+</sup> :YSO, the cyclicity of the optical transition depends strongly on the magnetic field orientation since changing the field changes the atomic transition dipole moment with respect to the cavity polarization. For the case where the cavity linewidth is large compared to the Zeeman splitting, the cyclicity is maximized when the spin-flip transitions _C_ , _D_ are orthogonal to the cavity polarization. In this work, by combining a larger _C_ - _D_ splitting and a narrower optical cavity than in Ref. [6] we were able to tune the _A_ transition into resonance with the cavity while simultaneously keeping the spin-flip transitions _C_ and _D_ detuned from the cavity (see Fig. 2b). Consequently we optimize the magnetic field orientation to maximize cyclicity. From this we found the optimal field orientation to be in the _aa_ -plane, rotated 22<sup>_o_</sup> from the _X_ -axis. 

To probe the cyclicity, the ion was initialized into _|↑g⟩_ and subsequently read out using 400 pulses. Each readout pulse consisted of an optical _π_ pulse resonant with the _A_ transition followed by a fluorescence collection window. Due to the finite cyclicity, the fluorescence count rate decays with increasing readout pulse number. This yielded a cyclicity of _C_ = Γ _A/_ Γ _D_ = 1030(10) (Fig. S2a). 

To establish the single photon emission we calculate the intensity autocorrelation _g_<sup>(2)</sup> ( _τ_ ) as shown in Fig. S2b. At 

4 

zero offset pulse delay, we observe _g_<sup>(2)</sup> (0) = 0 _._ 018(3), showing strong suppression of multi-photon emission events and thus a high purity of single photon emission. 



<!-- Start of picture text -->
a b<br>0<br>10<br>0.03<br>0.02<br>−1<br>10<br>0.01<br>0.00 −2<br>10<br>0 100 200 300 400 −20 −10 0 10 20<br>Readout pulse number Pulse offset n<br>)<br>τ<br>(<br>(2)<br>g<br>Counts per pulse<br><!-- End of picture text -->

FIG. S2. **Measuring the cyclicity. a** Decay of the _A_ transition fluorescence count rate from optical pumping after initializing into _|↑g⟩_ (blue). The count rate decays as _e_<sup>_−n/C_</sup> revealing a cyclicity of _C_ = 1030(10). The orange trace corresponds to the same readout pulse sequence after initializing into _|↓g⟩_ . **b** Intensity autocorrelation _g_<sup>(2)</sup> ( _τ_ ) of the _A_ transition showing strong suppression of the zero-delay peak with _g_<sup>(2)</sup> (0) = 0 _._ 018(3). 

## **VI. PHOTON ECHO INVESTIGATION OF THE OPTICAL COHERENCE** 

We probe the coherence of the optical _A_ transition using the photon echo technique. After initialization of the spin state, we utilized an excitation sequence consisting of three optical pulses _π_ /2 - _π_ - _π_ /2 separated by a waiting time _τ_ (for a total free evolution time 2 _τ_ ), followed by a fluorescence collection window. The refocusing _π_ pulse in the middle of the sequence removes the slowly varying inhomogeneous dephasing. For each evolution time, we swept the phase of the last _π_ /2 pulse and fitted the fluorescence intensity change against the phase angle using a sine function. The fitted oscillation amplitude is proportional to the two-level coherence. This yielded a coherence time of _T_ 2 = 10 _._ 2 _µ_ s for a Hahn echo sequence (Fig. S3a blue points). To further filter out higher frequency noise, we increased the number of refocusing pulses using an _XY_<sup>_N_</sup> dynamical decoupling sequence (see Fig. S3b) and reached a radiatively limited coherence time of 18 _µ_ s for _N_ = 32 (see Fig. S3a orange points). We note that in this experiment the emission lifetime is _T_ 1 = 9 _._ 1 _µ_ s, different from 7 _._ 4 _µ_ s recorded using time-resolved PLE shown in the main text. The results of this experiment implicate slow spectral diffusion as the main source of decoherence in our system. In the case of the Hahn echo sequence, the recorded _T_ 2 time is approximately a factor of two from the lifetime limit _T_ 2 _/_ (2 _T_ 1) = 0 _._ 56. 

## **VII. HOM FIT FUNCTIONS** 

In this section, we derive the two-photon interference functions used to model the HOM histograms in the main text. In particular, we consider two dephasing mechanisms, which allow us to estimate the possible bounds on the emission linewidth based on the photon visibility determined from the HOM experiment. Finally, we extend the model to simulate the reference HOM measurement, where the photons are made distinguishable by periodically changing the phase of one of the two interfering photons. 

To model the HOM zero-delay time peak shape, we follow the derivation of Ref [7]. We assume that single photon spatio-temporal wave functions have an exponential form: 



where _H_ ( _t_ ) is the Heaviside function, _T_ 1 is the radiative lifetime, _ω_ ( _t_ ) is the photon frequency and _φ_ ( _t_ ) is the phase. In an ideal case, the frequency and phase of the photon are constant over time, so the photon coherence is lifetime limited. A time-dependent frequency and phase noise lead to decoherence. Typically it is assumed that such perturbations yield random walks in phase and frequency at two distinct timescales leading to two different physical descriptions. The first regime is pure dephasing, caused by fast frequency jumps accumulating phase on a timescale 

5 



<!-- Start of picture text -->
a<br>0<br>10<br>−1<br>10<br>0 10 20 30 40 50<br>Free evolution time ( μ s)<br>b<br>20<br>15<br>10<br>5<br>0 5 10 15 20 25 30<br> Number of  π  pulses<br>Coherence<br>)<br>μs<br>(<br> Coherence time<br><!-- End of picture text -->

FIG. S3. **Optical coherence of Er**<sup>3+</sup> **:CaWO** 4. **a** An optical Hahn echo measurement (green) reveals an optical coherence of _T_ 2 = 10 _._ 2 _µ_ s. Applying _XY_<sup>32</sup> dynamical decoupling sequence (orange) extends the optical coherence to the radiative limit (blue dashed line) _T_ 2 = 18 _µ_ s, at a field where the optical _T_ 1 = 9 _._ 1(3) _µ_ s. **b** Optical coherence scaling with the number of refocusing pulses of _XY_ dynamical decoupling sequences (red) compared to the lifetime limit (blue). 

shorter than _T_ 1. The second regime is described by spectral diffusion, primarily attributed to slow frequency drift on a timescale considerably longer than _T_ 1. It is worth noting that this time-scale distinction is somewhat artificial, as it is known that different noise sources have continuous power spectral densities [8]. Still, we perform this analysis to study limiting cases. It can be shown that for single photons passing through an unbalanced MZI with a delay equal to the photon generation rate, the HOM histogram peak areas _An_ will be given by: _A|i|≥_ 2 = _A_ , _A_ 1 = _A_ (1 _− R_<sup>2</sup> ), _A−_ 1 = _A_ (1 _− T_<sup>2</sup> ) and _A_ 0 = _A_ ( _R_<sup>2</sup> + _T_<sup>2</sup> _−_ 2 _RTV_ int) [9]. Here, _A_ is the Poissionian peak coincidence level, _R_ / _T_ is the reflection/transmission coefficient of the output MZI beamsplitter, and _Vint_ is the emitter visibility. In such cases, the HOM two-photon interference coincidence probability function can be described by 



where _P_ dc is the coincidence level related to SNSPD dark counts and ambient light counts, and _t_ rep is the pulse repetition period. Further, _F_ ( _τ_ ) is an integral defined as [7] 



where ∆ _φ_ ( _τ, t_ 0) is a the phase difference and ∆ _ω_ ( _τ, t_ 0) is the frequency difference between two interfering photons. If frequency and phase fluctuations are assumed to follow Gaussian distribution functions, _F_ ( _τ_ ) is given by [7] 



where _T_ dep is the dephasing time 1 _/T_ dep = 1 _/T_ 2 _−_ 1 _/_ (2 _T_ 1), and _σ_ is the inhomogeneous linewidth broadening related to slow spectral diffusion. 

First, we consider the case where fast spectral dominates (Lorentzian broadening), for which 



This allows for the evaluation of the HOM histogram central peak area 



6 

and the off-center peak area _A|i|≥_ 2 



giving a visibility of 



Note that this definition of visibility contains information about both the MZI interferometer imperfections (BS _R_ : _T_ ) and the intrinsic indistinguishability of the emitted photons _V_ int = _T_ 2 _/_ (2 _T_ 1). In our experiment _R_ : _T_ = 0 _._ 43 : 0 _._ 57 is determined from the imbalance between _A−_ 1 and _A_ 1 peak areas in the HOM histogram (see Fig. 3b in the main text), contributing to a decrease in visibility of around 4%. By evaluating the integrated counts _A_ 0 and _A|n|≥_ 2 in the HOM experiment, we obtain a visibility of 80% after the dark and ambient light counts are subtracted. This allows us to estimate _V_ int = 0 _._ 84, and further _T_ 2 = 0 _._ 84 _×_ 2 _T_ 1 = 15 _._ 3 _µ_ s. Using Eqs. (3) and (6) with _T_ 2 = 15 _._ 3 _µ_ s we model the HOM histogram in the main text (Fig. 3b,d). Furthermore, using this model, we can estimate the bound on the emission linewidth at the timescale of 100 _−_ 200 _µ_ s following 



which yields Lorentzian broadening of _νL_ = 20 _._ 6 kHz. Note that in the case of Fourier limited photons, one obtains _νLF_ = 1 _/_ (2 _πT_ 1) = 17 _._ 3 kHz. 

In the case where slow dynamics dominate decoherence (Gaussian broadening), the function _F_ ( _τ_ ) is simplified to _F_ gau( _τ_ ) = exp � _−σ_<sup>2</sup> _τ_<sup>2�</sup> , such that 



This leads to a visibility given by 



where the intrinsic emitter visibility is given by 



Using _V_ int = 0 _._ 84 we get _σ_ equal to 0.039 MHz, which corresponds to a Gaussian broadening of _νG_ = 2 _√_ 2 _ln_ 2 _√_ 2 _σ_ = 21 kHz. Note that the estimated _νG_ is on the order of the Fourier limit of 17.3 kHz, such that the resultant emission line-shape will be described by a Voigt profile with a total width of 



equal to a linewidth of 31.4 kHz. This bounds the emission linewidth to be in the range 20 _._ 6 _−_ 31 _._ 4 kHz for a timescale of 175.2 _µ_ s. 

Next, we consider the case of the reference HOM measurement in Fig. 3c. Typically, the distinguishability in HOM experiments is tuned by rotating the polarization of one of the photons. However, our SNSPDs have a strongly polarization-dependent detection efficiency, which complicates the interpretation of such a measurement. Therefore, we instead make the photons distinguishable by artificial spectral broadening, achieved by rapidly modulating the path length of one of the interferometer arms with a large amplitude. Specifically, the phase of the photons traveling through the shorter MZI arm is modulated using a triangle wave with frequency _<u>ω</u>_ 2 _<u>mπ</u>_<sup>=43kHzandamplitude</sup> _Am_ = 0 _._ 75 _π_ . Consequently, the phase difference can be described directly by 



7 

In this case we can assume that the HOM zero-delay peak area will be dominated by the external phase modulation so that we can omit the ∆ _ω_ term, and _F_ ( _τ_ ) will only depend on ∆ _φ_ ( _t_ 0 _, τ_ ) 



The periodic modulation of the phase difference with _τ_ will translate into a quantum-beat-like signal with a distinct dip at zero detection time difference. To fit the HOM data in Fig. 3c,d of the main text, we evaluate _F_ mod( _τ_ ) numerically. The best fit to the experimental data is obtained for a modulation amplitude of 0.73(5) _π_ where the modulation frequency was fixed to the value used in the experiment, 43 kHz. 

## **VIII. DISTORTION OF THE MAGNETIC MOMENT TENSOR** 

The magnetic moments of individual single ions changed appreciably from ion-to-ion as well as from the previously recorded ground state _g_ -tensor [4]. To investigate this, the magnetic response of two single ions (different from the single ion investigated in the main text) was fully characterized by probing the optical transition frequencies of the four transitions _A_ , _B_ , _C_ , and _D_ for a range of field orientations using a magnetic field magnitude of 50 G, with the results shown in Tab. S2. 

TABLE S2. Single-ion _g_ -tensors measured for two separate ions. Due to a small distortion of the S4 point-group site, the single-ion magnetic moments do not satisfy _gx_ = _gy_ = _g⊥_ . We note that in this and subsequent sections we use the convention where the _z_ axis points along the crystallographic _c_ axis, which is different to the coordinate system used in the main text. 

||Ground state||E|xcited stat|e|
|---|---|---|---|---|---|
||_gx_<br>_gy_|_gz_|_gx_|_gy_|_gz_|
|Ion 1|8.5<br>7.6|1.7|7.3|6.9|1.8|
|Ion 2|8.6<br>7.9|2.5|7.6|6.9|2.3|



In order to gain a deeper understanding of the _g_ -tensor anisotropy, an effective crystal-field Hamiltonian was used to model the intra-4 _f_ transitions of Er<sup>3+</sup> :CaWO4. The complete Hamiltonian has the form 



where _H_ FI corresponds to the free-ion components of the Hamiltonian, _H_ CF accounts for the interaction of the valance electrons with the host material, and _H_ Z is the Zeeman Hamiltonian. The free-ion Hamiltonian used is [10] 



Noting only the most significant contributions, _E_ AVG accounts for the spherically symmetric one-electron component, _F_<sup>_k_</sup> are the Slater parameters, _f_<sup>_k_</sup> are the electrostatic repulsion with angular dependence, _ζ_ 4 _f_ is the spin-orbit coupling term, and _A_ SO is the spin-orbit coupling operator. The remaining contributions are higher-order and the reader is referred to Ref. [11] for details. To model the contribution of the S4 point-group symmetry crystal-field the following Hamiltonian was used 



with the coefficients _Bq_<sup>_k_the crystal-field parameters and</sup><sup>_C_</sup> _q_<sup>(</sup><sup>_k_)</sup> spherical-tensor operators in Wybourne’s normalization. We note that the above _Bq_<sup>_k_areallrealwiththeexceptionof</sup><sup>_B_</sup> 4<sup>6,whichiscomplex.TheaboveHamiltonianwas</sup> fitted to data obtained using site-selective fluorescence spectroscopy of the<sup>4</sup> I13 _/_ 2 _→_<sup>4</sup> I15 _/_ 2 transitions as well as the barycenter of higher-energy transitions up to<sup>4</sup> S3 _/_ 2 obtained from literature [4]. Furthermore, the fit was optimized to reproduce the ensemble<sup>4</sup> I15 _/_ 2Z1 and<sup>4</sup> I13 _/_ 2Y1 _g_ -tensors. 

Using the crystal-field parameters obtained via the method outlined above as a starting point, a fit was then performed to the _g_ -tensor of both Ion 1 and Ion 2 to determine the crystal-field environment local to each ion. We hypothesize that the perturbation of the S4 point-group symmetry was caused by a single dominant defect, potentially due to the substrate surface or some form of remote charge compensation. Consequently, an axial term _B_<sup>¯</sup> 0<sup>2oriented</sup> at an arbitrary angle with respect to the crystal-field quantization axis was introduced, and both the magnitude as 

8 

well as the orientation were varied to reproduce the observed ground and excited state _g_ -tensors. This assumed that the crystal-field potential due to the defect is superposable with the nominal crystal-field potential [12]. 

For Ion 1, the observed _g_ -tensor was reproduced by an axial term _B_<sup>¯</sup> 0<sup>2=9</sup><sup>_._3cm</sup><sup>_−_1,rotatedbyanEulerrotation</sup> from the quantization axis with _α_ = 90 _._ 4<sup>_◦_</sup> , _β_ = 265<sup>_◦_</sup> and _γ_ = 0<sup>_◦_</sup> , following the Euler angle convention of Messiah [13]. Similarly, Ion 2 required an axial term _B_<sup>¯</sup> 0<sup>2= 10</sup><sup>_._7 cm</sup><sup>_−_1, rotated by an Euler rotation from the quantization axis with</sup> _α_ = 270 _._ 2<sup>_◦_</sup> , _β_ = 98 _._ 0<sup>_◦_</sup> and _γ_ = 0<sup>_◦_</sup> . We note that the unperturbed rank 2 crystal-field parameter has a magnitude of _B_ 0<sup>2= 578cm</sup><sup>_−_1,suchthattheobservedchangeintherank2crystal-fieldpotentialconsistedofaround</sup><sup>_∼_2%for</sup> both of the ions. This amounts to a frequency shift of 3 _._ 5 GHz for Ion 1 and 3 _._ 9 GHz for Ion 2 for the<sup>4</sup> I15 _/_ 2Z1 to<sup>4</sup> I13 _/_ 2Y1 transition when compared to the crystal-field model not including any perturbation, which is somewhat larger than, but comparable to, the observed inhomogeneous linewidth for single ions coupled to the nanophotonic device. Therefore, the observed _g_ -value anisotropy is consistent with a small amount of strain near the ion, potentially due to proximity to the surface or a charge compensation mechanism. 

In order to perform the initial crystal-field Hamiltonian fit we independently measured the<sup>4</sup> I15 _/_ 2Z1 and<sup>4</sup> I13 _/_ 2Y1 ensemble magnetic moments using optical spectroscopy by utilizing the high density implanted sample. From this we obtain _g⊥_ = 8 _._ 6 and _g∥_ = 1 _._ 4 for the ground state, and _g⊥_ = 7 _._ 6 and _g∥_ = 1 _._ 3 for the excited state. The fitted ground state _g_ -values deviate from the literature values measured by electron-spin resonance [4]; however, the deviation is within the uncertainty of our vector magnet calibration due to magnetic field gradients within the sample space. We note that the above conclusion about the mechanism for the anisotropy of single ion _g_ -values does not depend on the precise magnetic moments assumed for bulk Er<sup>3+</sup> :CaWO4. Additionally, in the above fit we have constrained that _gx_ = _gy_ , and our data was also consistent with a fit for which _gx_ = _gy_ at the 5% level. This suggests that some of the observed distortion of the magnetic moment tensor may also be present in an ensemble average. 

## **IX. DEPENDENCE OF** _T_ 1 **ON MAGNETIC FIELD** 

To understand the observed spin lifetime, we performed a lifetime measurement at a second magnetic field strength, _|B|_ = 950 G, obtaining _T_ 1 = 0 _._ 393 s. At low temperatures, Raman and Orbach processes are slow and the spin relaxation rate is dominated by the direct process. This has the following functional form with respect to an applied magnetic field [14]: 



Fitting the above equation to the observed spin lifetime data (Fig. S4) yielded a direct process constant _Ad_ = 6 _._ 4(2) _×_ 10<sup>_−_6</sup> s<sup>_−_1</sup> GHz<sup>_−_5</sup> , with the expected _T_ 1 _∝_ 1 _/B_<sup>5</sup> scaling. The spin _T_ 1 has previously been measured for CaWO4 at low temperatures, and the zero-temperature extrapolated lifetime was found to be 4 _._ 8 s at a frequency of 7 _._ 881 GHz [15]. This corresponds to _Ad_ = 7 _._ 2 _×_ 10<sup>_−_6</sup> s<sup>_−_1</sup> GHz<sup>_−_5</sup> , approximately consistent with our value. 

## **X. SPIN COHERENCE MODELING** 

In order to explain the observed spin coherence, we consider the magnetic environment of the Er<sup>3+</sup> ion in the CaWO4 host crystal, consisting of the<sup>183</sup> W nuclear spin bath and paramagnetic impurities. While the concentration and dynamics of paramagnetic impurities is not well known, the dynamics of the nuclear spin bath under decoupling sequences can be understood using standard CCE (Cluster Correlation Expansion) techniques [16]. First, we describe the Er<sup>3+</sup> spin coupling to the nuclear spin bath and explain features observed in the Hahn experiment at short times. Then, we apply our understanding of the nuclear spin bath to find the expected decoherence rates for the Hahn and Ramsey experiments and observe that it cannot explain the observed rates in either. This leads us to conjecture the existence of an appreciable concentration of paramagnetic impurities, which we discuss in the next section. 

To form the nuclear spin bath, we generate random configurations of nuclear spins by allowing each W atom to be an<sup>183</sup> W isotope ( _I_ = 1 _/_ 2) with probability 14.3%. Under the secular approximation for the electron spin, this bath can be described by the following Hamiltonian in the rotating frame of the Er<sup>3+</sup> spin: 



where _Iz/x_<sup>_i_arethenuclearspinoperatorsoftheithspin,</sup><sup>_A_(</sup> _||_<sup>_i_)</sup> and _A_<sup>(</sup> _⊥_<sup>_i_)aretheparallelandperpendicularhyperfine</sup> interaction terms, _ωL,W_ is the Larmor frequency of the W nuclear spin (107.7 kHz at _|B|_ = 600 G) and _Hnn_<sup>(</sup><sup>_i,j_)</sup> is the dipolar interaction Hamiltonian between W nuclear spins. 

9 



<!-- Start of picture text -->
2<br>10<br>1<br>10<br>0<br>10<br>−1<br>10<br>2 3<br>10 10<br>|B| (G)<br> (s)<br>1<br>Spin T<br><!-- End of picture text -->

FIG. S4. **Spin lifetime as a function of magnetic field strength** . Solid line is a fit to Eq.(20) as is predicted for the spin-lattice relaxation time. 

This implies that there can be considerable variation in ESEEM (Electron Spin Echo Envelope Modulation) features observed for an Er<sup>3+</sup> ion, depending on whether a nearby W nuclear spin is present. We observe such features as dips in coherence in the Hahn experiment (Fig. 4d). In contrast to decay envelopes, these sharp features occur at particular pulse spacings and indicate coherent coupling to a _W_ nuclear spin occupying one of the nearest sites. Since we are working under the assumption that there is only one nearby W nuclear spin, we do not allow another nuclear spin within the first ten nearest W sites when generating the random nuclear spin baths. We find hyperfine parameters of the strongly coupled W nuclear spin by minimizing over the following cost function: 



Here, _τj_ are the time units that were sampled in the Hahn experiment, _S_ sim _,k_ ( _τj_ ) is the simulated signal for the k<sup>th</sup> bath and _S_ exp( _τj_ ) is the experimentally measured contrast for the experiment. _S_ sim _,k_ ( _τj_ ) is calculated by taking a product of three factors: a stretched exponential decay, with decay constants _T_ 2 = 44 _µ_ s and _n_ = 1 _._ 4 used in Fig. 4d, the CCE simulation for the nuclear spin bath, _S_ bath,k( _τj_ ), and simulation for a single W nuclear spin coupled to Er<sup>3+</sup> , _S_ ( _τj, A||, A⊥_ ). The form of _S_ sim _,k_ ( _τj_ ) is justified as a first order CCE expansion, which does not take interactions between constituents of the bath into account. The envelope _e_<sup>_−_(2</sup><sup>_τj/T_2)</sup><sup>_n_</sup> is assumed to come from a source independent of the nuclear spin bath. 

The minimization yields the hyperfine parameters, ( _A||, A⊥_ ) = (25.2, 31.7) kHz. These values are within range of expected interaction strengths for nearby W nuclear spin. In particular, for the W nuclear spin coordinates given as ˆ ˆ **rW** = _±_ **a** _/_ 2 + **c** _/_ 2, where **a** = _ax_ and **c** = _cz_ are CaWO4 lattice vectors, we calculate ( _A||, A⊥_ ) = (15.5, 30.5) kHz at our field orientation. The discrepancy could be due to uncertainty in the field alignment or the Er<sup>3+</sup> spin g-tensor, which can lead to rotations as discussed in Sec. VIII. 

Finally, ignoring the contribution from the phenomenological decay, we simulate longer time delays to extract the W bath limited coherence times for the Hahn and Ramsey experiments. We perform a second order CCE simulation for the simulation of the Hahn experiment, which takes into account the dipolar coupling between nuclear spins. Noting that ESEEM features will persist as observed in Fig. 4d, we find that the interaction between nuclear spin pairs leads to an envelope which decays in 22.6 ms (Fig. S5a). We also perform a Ramsey simulation and show that the expected _T_ 2<sup>_∗_decoherenceduetotheW-bathisabout4</sup><sup>_µ_s(Fig.S5b).Bothofthesecoherencevaluesare</sup> significantly longer than the observed values for _T_ 2 and _T_ 2<sup>_∗_.Weattributethedifferencetoparamagneticimpurities</sup> and explore the expected concentration in the next section. 

10 



<!-- Start of picture text -->
a<br>1<br>0.5<br>0<br>0 10 20 30 40 50 60 70 80<br>Free evolution time 2 τ  (µs)<br>b<br>1<br>0.5<br>0<br>0 5 10 15 20 25 30<br>Free evolution time  τ  (µs)<br>|  g<br>Population<br>|  g<br>Population<br><!-- End of picture text -->

FIG. S5. **W bath limited coherence** . **a** The second order contribution to the CCE simulation for the Hahn experiment for 10 random W-bath configurations, where we assume that the nearest W nuclear spin is located at **rW** . Fitting each of the curves to a stretched exponential yields _T_ 2 = 22 _._ 7(4) ms with _n_ = 2 _._ 7(1). We note that this is only the envelope and faster ESEEM features, obtained from the first order CCE simulation, persist as seen in Fig. 4d. This simulation considers W nuclear spins within an 11 nm radius of the Er<sup>3+</sup> spin. **b** CCE simulation of Ramsey experiment for the same W bath configurations. Fitting each of the curves to a Gaussian decay yields _T_ 2<sup>_∗_=4</sup><sup>_._0(4)</sup><sup>_µ_s.Bothsimulationsareperformedatour</sup> experimental field configuration. 

## **XI. ESTIMATING CONCENTRATION OF PARAMAGNETIC IMPURITIES** 

In order to estimate the concentration of paramagnetic impurities, we use the Ramsey experiment as a probe of the static magnetic noise experienced by the Er<sup>3+</sup> ion. As stated in the previous sections, the W bath limited _T_ 2<sup>_∗_</sup> (Fig. S5b) is significantly longer than the measured _T_ 2<sup>_∗_of247ns.Thisindicatesthatthemeasured</sup><sup>_T ∗_</sup> 2<sup>islimited</sup> by paramagnetic impurities. Therefore, we can use the measured _T_ 2<sup>_∗_toroughlyestimatetheconcentrationofthese</sup> impurities. 

Without loss of generality, we can assume that the interaction between the Er<sup>3+</sup> spin and the paramagnetic impurity will be of the Ising form under the secular approximation, forbidding exchanges that do not conserve magnetization. Under these assumptions, we can write down the Hamiltonian concerning the Er<sup>3+</sup> spin and the paramagnetic bath in the frame rotating at Er<sup>3+</sup> and the impurity frequency for a single impurity species 



Here, _JI_<sup>(</sup><sup>_i_)</sup> is the Ising interaction strength between the Er<sup>3+</sup> spin and the impurity, while _JI_<sup>(</sup><sup>_i,j_)</sup> and _JS_<sup>(</sup><sup>_i,j_)</sup> are the Ising and Symmetric interaction strengths between the two impurities and ∆ _i_ is the disorder in the precession frequency of each impurity. While the bath interaction and disorder terms become important for decoupling sequences, these processes do not contribute on the timescale of the Ramsey experiment, which is dominated by the static noise represented by the first term. Based on this understanding, we can compute the net frequency, in the rotating frame, of the Er<sup>3+</sup> spin given the state of the bath. For the purposes of this calculation, we take this bath to consist of _S_ = 1 _/_ 2 electrons with _g_ = 2 and represent its state by the bitstring _k_ of length _N_ . We can then write down the Hamiltonian projected by the state _k_ of the bath 



Here, _ωk_ is the precession frequency of the Er<sup>3+</sup> spin given the state _k_ of the bath. We can then calculate the Ramsey 

11 

coherence as _T_ 2<sup>_∗_=</sup><sup>_π/_∆</sup><sup>_ω_,where∆</sup><sup>_ω_2isthevarianceovertheset</sup><sup>_{ωk}_:</sup> 



where we have used the fact that the distribution is centered at zero and the summations can be reordered. We observe that the frequency standard deviation can be interpreted as the norm of the vector of Ising interaction strengths. 

In order to estimate the concentration based on this expression, we generate 2000 instances of randomly distributed electron spin baths across a range of concentrations, calculate the resultant _T_ 2<sup>_∗_ofeachconfigurationanduseBayes</sup> rule to infer a probability density, _P_ ( _ρ|T_ 2<sup>_∗_),fortheconcentration,</sup><sup>_ρ_,givenourobservationof</sup><sup>_T ∗_</sup> 2 



Here, _P_ ( _T_ 2<sup>_∗|ρ′_)istheprobabilitytoobtainagiven</sup><sup>_T ∗_</sup> 2<sup>forthebathconcentration</sup><sup>_ρ_.Inpractice,wecalculatethis</sup> expression by counting the number of instances for each concentration that yields a value of _T_ 2<sup>_∗_within3standard</sup> deviations of the observed value. We perform this estimate for both a 3D geometry of electron spins located in the bulk and a 2D geometry of spins located on the sample surface, estimated to be 10 nm away. We obtain concentrations of 1 _._ 6 _−_ 5 _._ 7 _×_ 10<sup>16</sup> cm<sup>_−_3</sup> and 0 _._ 5 _−_ 1 _._ 3 nm<sup>_−_2</sup> for the bulk and surface concentration estimates respectively with 70% confidence (Fig. S6). As both of these are plausible concentrations, we note that both may be playing a non-negligible role. We are not able to make a calculation of how this concentration of paramagnetic impurities affects the Hahn coherence because it depends on the dynamics of this paramagnetic impurity bath, which is not well known. Doing this calculation would require further information such as the species and spin-lifetime of impurities, as well as the disorder of the bath. 



<!-- Start of picture text -->
a<br>0.2<br>0.1<br>0.0<br>0 5 10 15 20<br>ρ  (10 16  cm -3 )<br>b<br>3.0<br>2.0<br>1.0<br>0.0<br>0.0 0.5 1.0 1.5<br>ρΑ  (nm -2 )<br>3) cm<br>-16<br>Prob. density (10<br>2)Prob. density (nm<br><!-- End of picture text -->

FIG. S6. **Probability density of paramagnetic impurity concentration** . **a** Assuming a 3D uniform distribution of impurities, we estimate that the bath concentration is in the range 1.6 _×_ 10<sup>16</sup> – 5.7 _×_ 10<sup>16</sup> cm<sup>_−_3</sup> with 70% confidence, with the likeliest concentration at 3.7 _×_ 10<sup>16</sup> cm<sup>_−_3</sup> . **b** Assuming a 2D distribution on the surface of our crystal, assumed to be located 10 nm away from the Er<sup>3+</sup> spin, we estimate an area concentration in the range of 0.5 – 1.3 nm<sup>_−_2</sup> with 70% confidence, with the likeliest concentration at 0.77 nm<sup>_−_2</sup> . Dashed lines indicate the confidence ranges for the impurity concentrations. 

12 

- _∗_ These authors contributed equally to this work. 

- jdthompson@princeton.edu 

- [1] Dibos, A. M., Raha, M., Phenicie, C. M. & Thompson, J. D. Atomic Source of Single Photons in the Telecom Band. _Physical Review Letters_ **120** , 243601 (2018). 

- [2] Ziegler, J. F., Ziegler, M. D. & Biersack, J. P. SRIM – The stopping and range of ions in matter (2010). _Nuclear Instruments and Methods in Physics Research Section B: Beam Interactions with Materials and Atoms_ **268** , 1818–1823 (2010). 

- [3] Chen, S. _et al._ Hybrid microwave-optical scanning probe for addressing solid-state spins in nanophotonic cavities. _Optics Express_ **29** , 4902 (2021). 

- [4] Enrique, B. G. Optical spectrum and magnetic properties of Er<sup>3+</sup> in CaWO4. _The Journal of Chemical Physics_ **55** , 2538–2549 (1971). 

- [5] Chen, S., Raha, M., Phenicie, C. M., Ourari, S. & Thompson, J. D. Parallel single-shot measurement and coherent control of solid-state spins below the diffraction limit. _Science_ **370** , 592–595 (2020). 

- [6] Raha, M. _et al._ Optical quantum nondemolition measurement of a single rare earth ion qubit. _Nature Communications_ **11** , 1605 (2020). 

- [7] Kambs, B. & Becher, C. Limitations on the indistinguishability of photons from remote solid state sources. _New Journal of Physics_ **20** , 115003 (2018). 

- [8] Kuhlmann, A. V. _et al._ Transform-limited single photons from a single quantum dot. _Nature Communications_ **6** , 8204 (2015). 

- [9] Loredo, J. C. _et al._ Scalable performance in solid-state single-photon sources. _Optica_ **3** , 433 (2016). 

- [10] Carnall, W. T., Goodman, G. L., Rajnak, K. & Rana, R. S. A systematic analysis of the spectra of the lanthanides doped into single crystal LaF3. _The Journal of Chemical Physics_ **90** , 3443–3457 (1989). 

- [11] Wybourne, B. G. _Spectroscopic properties of rare earths_ (Interscience Publishers, 1965). 

- [12] Newman, D. Theory of lanthanide crystal _Advances in Physics_ **20** , 197–256 (1971). 

- [13] Messiah, A. _Quantum mechanics_ (Dover Publications, 1961). 

- [14] Abragam, A. & Bleaney, B. _Electron Paramagnetic Resonance of Transition Ions_ (OUP Oxford, 1970). 

- [15] LeDantec, M. _et al._ Twenty-three–millisecond electron spin coherence of erbium ions in a natural-abundance crystal. _Science Advances_ **7** , eabj9786 (2021). 

- [16] Yang, W. & Liu, R.-B. Quantum many-body theory of qubit decoherence in a finite-size spin bath. ii. ensemble dynamics. _Physical Review B_ **79** , 115320 (2009). 

