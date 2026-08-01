# **Addressing spins at their clock transition with a frequency- and bandwidth-tunable superconducting resonator** 

Yutian Wen,<sup>1, 2,</sup><sup>_∗_</sup> V. Ranjan,<sup>3</sup> T. Lorriaux,<sup>2</sup> D. Vion,<sup>1</sup> B. Huard,<sup>2</sup> A. Bienfait,<sup>2</sup> E. Flurin,<sup>1</sup> and P. Bertet<sup>1,</sup><sup>_†_</sup> 

> 1 _Quantronics group, Universit´e Paris-Saclay, CEA, CNRS, SPEC, 91191 Gif-sur-Yvette Cedex, France_ 

2 _´Ecole Normale Sup´erieure de Lyon, CNRS, Laboratoire de Physique, F-69342 Lyon, France_ 

> 3 _Tata Institute of Fundamental Research Hyderabad, 500046 Hyderabad, India_ 

(Dated: October 23, 2025) 

Solid-state spin ensembles addressed via superconducting circuits are promising candidates for quantum memory applications, offering multimodal storage capability and second-long coherence times at their clock transition. Implementing practical memory schemes requires dynamic control over both the resonator frequency and bandwidth. In this letter, we report measurements of a superconducting resonator whose frequency can be tuned by passing a DC current through the high-kinetic-inductance thin film, and whose bandwidth can be tuned by parametric coupling to a low-Q buffer resonator. Using this resonator, we address an ensemble of bismuth donors at their clock transition, measuring a Hahn-echo coherence time of 450 ms. We demonstrate RF driving of the bismuth donor hyperfine transitions, as well as dynamic bandwidth control of the resonator. 

Despite continuous improvements, the limited coherence time remains a key challenge for superconducting quantum processors, constraining both noisy intermediate-scale quantum (NISQ) algorithms [1] and quantum error correction schemes [2]. A promising solution [3] relies on dedicated quantum memory units capable of parallel storage of multiple qubit states over extended periods. Amongst various platforms explored to this end [4–9], solid-state spin ensembles stand out for their multimodal storage capability [9–13] and secondlong coherence times [14]. An example of architecture consists in encoding the qubit states in single- or fewphoton microwave pulses to be stored in and retrieved from the spin ensemble memory through refocussing sequences [15–18]. One difficulty of this approach is to achieve efficient absorption of the wave packet in the spin ensemble. Even with the use of high-quality-factor resonators to enhance the spin-photon interaction strength, efficient photon absorption requires relatively large spin density, which leads to broad ensemble spin linewidth and reduced spin coherence time due to dipolar interactions [19]. 

One possible way to solve this issue is to bias spins at specific magnetic fields where their mean magnetic dipoles vanish, allowing for long coherence times even at large spin concentrations. These so-called clock transitions (CTs), or zero first-order-insensitive (ZEFOZ) points, occur in coupled electron-nuclear spin systems with large hyperfine interactions. Enhanced coherence times at CTs have been observed in donors in silicon [14], molecular spins [20], and rare-earth-ion-doped crystals [21, 22]. Because CTs occur only at specific magnetic fields, they require resonators tuned precisely to the corresponding transition frequency. While this can be achieved via trial and error with fixed-frequency resonators [9], a more general and scalable approach uses resonators whose frequency can be tuned in-situ and dy- 

namically to the CT frequency. Additionally, several quantum memory protocols [18, 23] also require dynamical control of the resonator bandwidth, to avoid maser emission when the spin ensemble is inverted by the control pulses. 

Aluminium-based Josephson devices offer many tools to design resonators with tunable characteristics [24], but they are usually incompatible with the application of magnetic fields above _∼_ 10 mT that are necessary to bias the spins. Another mechanism, compatible with large magnetic fields, arises from the quadratic dependence of the kinetic inductance of a superconducting wire, _Lk_ ( _I_ ) = _Lk_ 0 + _αI_<sup>2</sup> on the current _I_ passing through it. Field-resilient kinetic inductance (KI)based frequency-tunable resonators have been demonstrated [25–27] and used for interfacing spins at _∼_ 200 _−_ 500 mT fields [28]. Here, we design and fabricate a frequency- and bandwidth-tunable resonator based on KI. We demonstrate its suitability as a spin-ensemble quantum memory interface by addressing bismuth donor spins in silicon (Bi:Si) at their CT where we measure extended coherence times, and we perform a spectroscopy of Bi:Si sub-gigahertz transitions by electron nuclear double resonance (ENDOR). 

The circuit schematics is shown in Fig. 1. The core part of the device is a pair of superconducting microwave resonators (“resonator A” and “resonator B” in Fig. 1c and the subcircuits of matching colours in Fig. 1a) that are inductively coupled via a small mutual inductance, called the kinetic inductance coupler (KIC). Resonator A is a high quality-factor resonator which inductively couples to the spin ensemble. It consists of a 800 nm-wide inductive wire with large KI (referred to as microwire A) and a capacitor in parallel. Resonator B is a low- _Q_ auxiliary that acts as a tunable microwave buffer for resonator A. Its inductor is 4 _µ_ m wide. The KIC comprises a pair of 5 _µ_ m-long, 250 nm-wide nanowires (Fig. 1d). 

2 



<!-- Start of picture text -->
I<br>� A c2<br>f A<br>Bragg<br>Mirror A<br><!-- End of picture text -->



<!-- Start of picture text -->
Bragg<br>Mirror B<br><!-- End of picture text -->



<!-- Start of picture text -->
1mm<br><!-- End of picture text -->



<!-- Start of picture text -->
Resonator B Resonator A<br><!-- End of picture text -->



<!-- Start of picture text -->
Coupler<br>20�m<br><!-- End of picture text -->



FIG. 1. Device layout. (a) Schematic circuit diagram. The lumped element models of resonator A (blue) and resonator B (red) are highlighted in (c). The kinetic inductance coupler (KIC) is shown as an inductive shunt to the ground. (b) Overview micrograph of the circuit substrate before flip chip bonding. The green box outlines the footprint of the Bi-doped silicon die which is subsequently glued on top. The external polarising field _B_ z is applied parallel to the microwire of resonator A, i.e., horizontal in this image. (c) Zoom-in of the resonator region (brown box in (b)). Resonators A and B are marked with dashed boxes. The arrows point to the KIC. (d) Optical and scanning electron micrographs of the KIC nanowire. The bright areas of various shades are NbTiN films with different vortex-trapping hole densities. The darkest regions are the exposed silicon substrate. 

An inductor is tunable when it owes a large fraction of its value to kinetic inductance, as ensured by lateral confinement for microwire A and the KIC. Microwire B is much wider, and has next to no tunability, as we confirm shortly thereafter. The resonator frequency _f_ A can be tuned by passing a DC current _I_ A through microwire A. Its bandwidth tuning is achieved via three-wave mixing with resonator B through the KIC [26, 29]. Both tuning processes require low-frequency or DC bias of the nonlinear inductors. To this end we flank the dual resonator on either side with notch filters, centred at _f_ A and _f_ B respectively. These so-called “Bragg mirrors” [30], consisting in successions of quarter-wave-length coplanar 

waveguides (CPW) of alternating impedances, can maintain high quality factors while permitting DC current and radio-frequency (RF) pump tones to pass through. The separate control of DC currents _I_ A and _I_ B injected into the devices ports implies independent biases of microwire A ( _I_ A) and the KIC ( _I_ A + _I_ B), so that the bandwidth and frequency tunabilities are in principle decoupled. Note that the Bragg mirror A contains twelve _{_ high- _Z_ , low- _Z}_ repetitions, whereas the Bragg mirror B contains only four. As a result, microwave transmission through port A is less than 10<sup>3</sup> s<sup>_−_1</sup> and thus negligible, so for both resonators the only relevant microwave coupling are the ones through Bragg mirror B, the rate of which we denote as _κ_<sup>A</sup> c<sup>and</sup><sup>_κ_B</sup> c<sup>hereinafter.Accord-</sup> ingly, the internal loss rates are denoted by _κ_<sup>A(B)</sup> i , and the respective total linewidths _κ_<sup>A(B)</sup> = _κ_<sup>A(B)</sup> i + _κ_<sup>A(B)</sup> c . The whole circuit is patterned on a 50 nm-thick NbTiN film, on which we measured kinetic inductance per square _L_<sup>sq2</sup><sup>_._2pH</sup><sup>_/_□.Thecircuitiscooledto10mKina</sup> kin<sup>=</sup> dilution refrigerator, with appropriate attenuation and filtering to suppress thermal noise. 

We first characterize the circuit by microwave reflectometry through port B. In absence of bias current, we find _f_ A = 7 _._ 422 GHz, _κ_<sup>A</sup> c<sup>= 9</sup><sup>_._4</sup><sup>_×_104/s,</sup><sup>_κ_A</sup> i<sup>= 7</sup><sup>_._5</sup><sup>_×_105/s;</sup> _f_ B = 6 _._ 605 GHz, _κ_<sup>B</sup> c<sup>= 2</sup><sup>_._6</sup><sup>_×_107/s,</sup><sup>_κ_B</sup> i<sup>= 5</sup><sup>_._7</sup><sup>_×_106/s.The</sup> resonator frequency shift ∆ _f_ is then measured as functions of _I_ A and _I_ B (Fig. 2ab). We observe that resonator A can be tuned over an _∼_ 80 MHz range, whereas resonator B shifts by less than 10 MHz, as designed. All tuning curves fit well to simple Ginzburg-Landau theory [25], from which we can extract the critical current of microwire A, 9 _._ 53 mA, and that of the KIC, 5 _._ 73 mA. We note the critical currents are proportional to the total cross-section areas, as expected [31]. 

In addition to frequency tuning, the KIC creates a three-wave mixing (3WM) term ( _a_ + _a†_ )( _b_ + _b†_ )2 in the circuit Hamiltonian [32], where _a_ ( _b_ ) is the annihilation _† †_ operator of mode A (B), and _a_ ( _b_ ) the creation operator. When a strong drive tone is applied through port B at frequency _f_ 3WM = _f_ A _− f_ B, this terms simplifies to a _† †_ frequency-conversion Hamiltonian _g_ 3WM( _ab_ + _a b_ ) [33], with _<u>g</u>_ 3WM being proportional to the pump amplitude _√P_ 3WM and DC current _I_ A + _I_ B flowing through the KIC. Since resonator B has a significantly larger decay rate than resonator A, whenever the 3WM is enabled, it translates into an additional loss rate _κ_<sup>A</sup> i = 4 _g_ 3WM<sup>2</sup><sup>_/κ_B</sup> for resonator A (see Figs. 2c and d) [34]. The linear dependence of _κ_<sup>A</sup> i on _P_ 3WM and ( _I_ A + _I_ B)<sup>2</sup> is confirmed in Fig. 2e. The bandwidth can also be tuned dynamically. It is for instance possible to suddenly accelerate the resonator field decay, as demonstrated in Fig. 2f. 

We finally measure the resonator A frequency and internal loss rate as a function of a magnetic field _Bz_ applied approximately parallel to the sample surface and to the microwire (Fig. 2f). The frequency decreases due 

3 





<!-- Start of picture text -->
�<br>/2<br>A<br>�<br><!-- End of picture text -->





<!-- Start of picture text -->
-4<br>0<br><!-- End of picture text -->

FIG. 2. Resonator tunabilities. (a-b) Resonance frequency shift of the two modes in response to sweeping DC bias current _I_ A (a) or _I_ B (b), under different _I_ B or _I_ A offsets. Solid curves: fits to Ginzburg-Landau theory [25]. (c-d) Amplitude of the microwave reflection _S_ 11 off port B near the resonance frequency of mode B (c) and A (d), as the RF pump frequency _f_ 3WM is swept across the frequency difference _f_ A _−f_ B. (e) Dependence of the measured mode A linewidth _κ_<sup>A</sup> i<sup>(open circles)</sup> on the RF pump amplitude, under various DC bias through _I_ B while _I_ A is held neutral. (f) Ringdown suppression via dynamic control of resonator bandwidth. The green curves of varying shades represent the ringdown amplitude after a resonant microwave pulse, as the 3WM pump pulses are delayed by 0 _µ_ s, 1 _µ_ s, ..., 4 _µ_ s. The pulse sequences are shown in insets with the varying parameters marked in red with arrows. (g) Resonance frequency _f_ A (left axis) and internal loss rate _κ_<sup>A</sup> i<sup>(rightaxis)ofmodeAasfunctionsofthemagneticfield</sup> _B_ z applied in-plane, parallel to microwire A. 

to the kinetic inductance dependence on magnetic field. 



<!-- Start of picture text -->
(a) 4<br>3<br>-4<br>-5<br>0 20 40 60<br>Bz  (mT)<br>(b)<br>7.42<br>7.40<br>7.38 20<br>7.36 10<br>7.34 0<br>0 20 40 60<br>(c) Bz  (mT)<br>1.1<br>Bz  = 2 mT 0.4<br>0.9<br>0<br>0 �/�e0.7<br>0.7<br>7.35 7.37 7.39 7.41<br>f A (GHz)<br>FIG. 3. Tracking bismuth spin transitions with a tunable<br>resonator. (a) Calculated bismuth donor energy spectrum as<br>a function of the polarising field Bz [37, 38]. The arrows<br>mark the clock transitions characterised in Fig. 4, and the<br>relevant spin states are coloured green. (b) The resonator ab-<br>sorption spectrometry, measured by the internal loss rate κ A i<br>of mode A as its resonance frequency f is swept across the<br>tuning range, and B z between 0 and 65 mT. The contrast is<br>enhanced and the field-independent background is removed<br>for visibility. The red dashed curves indicate the calculated<br>transition frequencies. (c) The absorption spectrum (open<br>circles) at 2 . 1 mT. The bismuth transition peaks are indi-<br>cated by the gray dash lines. Inset: the extracted bismuth<br>transition peak width Γ versus the gyromagnetic ratio γ in<br>unit of the Bohr magneton  γ e. The dashed line represents the<br>homogenous linewidth corresponding to an Overhauser field<br>δB 0 = 4 µ T due to the residual 500 ppm of 29 Si [30, 39].<br>|4, -4<br>|F = 4, m = 4<br>|5, 5<br>|5, -5<br>energy (GHz)<br> (kHz)<br>�<br>/2<br>A<br>��<br>(GHz)<br>f A<br>6 rad/s) (10 (MHz)��<br>A�i<br><!-- End of picture text -->

The loss rate shows an increase around 260 mT, and otherwise remains constant except for a slight increase close to 500 mT. A closer look into the 260 mT feature reveals a narrow peak that we tentatively ascribe to dangling bond spins at the Si/SiO2 interface with _g_ = 2 _._ 0 (socalled Pb0 centers [35]), and a broader peak centred at _g_ = 1 _._ 922, similar to the one called USO in [36] and that has been ascribed to a Ti-related paramagnetic defect. 

4 

We now demonstrate that the frequencyand bandwidth-tunable resonator can be used to address spins in solids. A<sup>28</sup> Si-enriched silicon chip is bonded on top of microwire A, the surface layer facing the resonator pre-implanted with<sup>209</sup> Bi<sup>+</sup> ions. Bismuth is a donor for silicon, which resumes a neutral state at low temperatures. Its spin Hamiltonian is _H_ = ( _γe_ **S** + _γn_ **I** ) _Bz_ + _A_ **I** _·_ **S** , with **S** ( **I** ) being the electron (nuclear) spin operator, _γe/_ 2 _π_ = _−_ 28 GHz/T ( _γn/_ 2 _π_ = 8 MHz/T) the electron (nuclear) spin gyromagnetic ratio, and _A/_ 2 _π_ = 1 _._ 47507 GHz the hyperfine coupling constant [40]. At _Bz_ = 0, the energy states are eigenstates of the total angular momentum operator, **F** = **I** + **S** , with eigenvalue _F_ = 4 for the ground-state manifold of 9 levels, and _F_ = 5 for the excited state manifold of 11 levels. Application of a small magnetic field lifts the degeneracy between levels with different _m_ values of the _F_ projection on _z_ (see Fig. 3a). An oscillating magnetic field perpendicular to _Bz_ can induce transitions between these levels whenever ∆ _m_ = _±_ 1. This can occur at microwave frequency for transitions between levels with _F_ = 4 and _F_ = 5 (electron spin resonance (ESR)–like transitions), or at radio-frequency between levels within the same _F_ manifold (nuclear magnetic resonance (NMR)–like transitions). Owing to this peculiar energy-level diagram, several CTs can be found in the Bi:Si spectrum [14, 37]. Here we will concentrate primarily on the one at 25 _._ 6 mT and 7 _._ 3382 GHz [40]. 

We perform the spin spectroscopy, first by measuring the resonator loss rate as a function of frequency _f_ A (by application of _I_ A) and polarising field _Bz_ . We subtract the field-independent background and plot the change in internal loss rate ∆ _κ_ A in Fig. 3(b). _Bz_ -dependent resonant losses are observed, and their position matches the ESR-like transitions of Bi:Si. The _Bz_ = 2 _._ 1 mT data are plotted in Fig. 3c; the Bi:Si resonances have linewidth of _∼_ 300 kHz, indicative of significantly lower strain than in devices where the metallic resonator was deposited directly on top of the crystal [41–43], but they are not yet at the homogenous linewidth limit. We remove part of the spectrum around _Bz_ = 9 mT where aluminium bonding wires were transiting from superconducting to normal states. 

The Bi:Si spectrum at the CT is measured by sweeping the resonator frequency _f_ A and recording the amplitude of a Hahn echo. It consists of two resolved peaks of width _∼_ 90 kHz, corresponding respectively to the transitions _|_ 4 _, −_ 1 _⟩↔|_ 5 _,_ 0 _⟩_ and _|_ 4 _,_ 0 _⟩↔|_ 5 _, −_ 1 _⟩_ (see Fig. 3a). The energy relaxation time is measured to be _T_ 1 = 53 s by an inversion recovery sequence (see Fig. 4a). This is two orders of magnitude shorter than typical non-radiative relaxation times in Bi:Si at 10 mK, indicating that the donor spins are well in the Purcell regime [44, 45]. We then measure the echo amplitude as a function of the Hahn echo delay _τ_ (see Fig. 4b). The data are well-fitted by an exponential decay, with a time constant _T_ 2 = 450 ms, sim- 



<!-- Start of picture text -->
(a) (b)<br>1<br>1<br>� �<br>���<br>T<br>0 0<br>7.337 7.339 0 400 800 1200<br>f A (GHz) T (s)<br>(c) (d)<br>1 1 data<br>�<br>simulation<br>���<br>�� mw<br>f A<br>� f A<br>0<br>0<br>0 1 2 0 0.2 0.4 0.6<br>2� (s) �� f A (MHz)<br>(e)<br>|4, 4 |5, 3 |4, 3 |5, 3 |4, 2 |5, 1 |4, 1 |5, 0 |4, 0 |5, -1 |4, -1<br>|4, 3 |5, 2 |4, 2 |5, 1 |4, 1 |5, 0 |4, 0 |5, -1 |4, -1 |5, -2 |4, -2<br>1<br>20<br>mw<br>0 2.6 2.8 f NMR<br>0 � (kHz/�T)<br>36.5 37 37.5 38 38.5<br>f NMR (MHz)<br>echo (arb. u.) echo (arb. u.)<br>echo (arb. u.)<br>echo (arb. u.)<br> (kHz)<br>�<br>echo (arb. u.)<br><!-- End of picture text -->

FIG. 4. Clock transitions and electron nuclear double resonance (ENDOR). The open circles represents the raw data, and the solid curves Lorentzian (a, e) or exponential (b-d) fits. The pulse sequences are shown in insets with the varying parameters marked in red with arrows. (a) Hahn echo spectroscopy at 25 _._ 6 mT. _T_ 1 (b) and _T_ 2 (c) measurement at 7.3382 GHz (dashed grey line in (a)). (d) Echo silencing via resonator shifting. The normalised echo magnitude decays with increasing resonance frequency detuning ∆ _f_ A of mode A during the period of echo. (e) Normalised microwave echo magnitude (open circles) as a function of the disruptive radio frequency pulse frequency _f_ NMR. The grey lines indicate the nuclear magnetic resonance (NMR)–like transitions. The ones involving _|_ 4 _,_ 1 _⟩ , |_ 4 _,_ 0 _⟩ , |_ 5 _,_ 0 _⟩_ , or _|_ 5 _,_ 1 _⟩_ are highlighted with solid lines. Left inset: the extracted peak width Γ of the NMR-like transitions versus their gyromagnetic ratio _γ_ . The dashed line represents the homogenous linewidth corresponding to a magnetic noise _δB_ 0 = 4 _µ_ T. 

ilar to those already observed at Bi:Si CTs using fixedfrequency resonators [9, 14]. This demonstrates that we can address the Bi:Si donor spins at their CT, using a frequency-tunable resonator. Echo emission can be controlled by dynamically tuning the resonator away from resonance at the time of the echo formation, as already demonstrated in Ref. [46, 47]. Such echo silencing is useful in several quantum memory protocols [15, 23, 48]. 

The ability to send sub-gigahertz pulses is harnessed 

5 

to drive NMR-like transitions between Bi:Si levels. To that goal, the amplitude of a Hahn echo is measured as a function of the frequency _f_ NMR of a radio frequency pulse sent in-between the two echo control pulses. With the magnetic field set to _B_ z = 13 _._ 49 mT and the resonator to 7422.5 MHz, we primarily probe the _|_ 4 _,_ 0 _⟩↔|_ 5 _,_ 1 _⟩_ transition, though the _|_ 4 _,_ 1 _⟩↔|_ 5 _,_ 0 _⟩_ transition also contributes slightly due to spectral overlap. The echo signal diminishes when _f_ NMR matches an NMR–like transition involving one of these states. This is evident in Fig. 4(e), where the dips on the normalised echo magnitude correspond to the relevant NMR-like transition spectrum, from low to high frequency: _|_ 5 _,_ 2 _⟩↔|_ 5 _,_ 1 _⟩ , |_ 4 _,_ 2 _⟩↔|_ 4 _,_ 1 _⟩ , |_ 5 _,_ 1 _⟩↔ |_ 5 _,_ 0 _⟩ , |_ 4 _,_ 1 _⟩↔|_ 4 _,_ 0 _⟩ , |_ 5 _,_ 0 _⟩↔|_ 5 _, −_ 1 _⟩ , |_ 4 _,_ 0 _⟩↔|_ 4 _, −_ 1 _⟩_ . In particular, the _|_ 4 _,_ 2 _⟩↔|_ 4 _,_ 1 _⟩ , |_ 5 _,_ 0 _⟩↔|_ 5 _, −_ 1 _⟩_ dips are visibly shallower than the other four, as expected from the lower contribution of levels _|_ 4 _,_ 1 _⟩_ and _|_ 5 _,_ 0 _⟩_ to the echo signal. Other NMR-like transitions have no impact 

on the echo amplitude. 

In conclusion, we have demonstrated a field-resilient resonator with tunable frequency and bandwidth, suitable for addressing paramagnetic impurities. Such device should find applications in microwave quantum memories, as well as nanoscale magnetic resonance spectroscopy [49–51]. 

The authors acknowledge the technical support of P. S´enat, D. Duet, P.-F. Orfila, and S. Delprat, and fruitful discussions within the Quantronics group. The authors acknowledge the support of the AIDAS joint laboratory, of R´egion Ile-de-France through the DIM SIRTEQ, of the Agence Nationale de la Recherche under the Chaire Industrielle NASNIQ, and under the PEPR Plan Project ROBUSTSUPERQ, and IARPA and Lincoln Labs for providing the Josephson travelling-wave parametric amplifier. 

## **Supplemental materials to “Addressing spins at the clock transitions with a frequency- and bandwidth-tunable superconducting resonator”** 

## **Sample** 

The bottom chip containing the superconducting device is made out of 50-nm-thick NbTiN deposited on Silicon. Our fabrication starts from a 2” Si wafer (high-resistivity grade supplied from Siltronics), that is deoxidised in 5% HF for two minutes before NbTiN sputtering. The device fabrication process comprises three lithography steps, using either a 30 keV Raith electron-beam lithography system or a Heidelberg Instruments Maskless Aligner. Afterwards the pattern is either converted to 30 nm of aluminium hard mask via lift-off, or we use directly the developed photoresist as a soft mask for reactive ion etching to remove the appropriate parts of the NbTiN film or the silicon substrate. 

The cover chip is a silicon chip topped by a 800 nm-thick epilayer of<sup>28</sup> Si. Bismuth atoms have been implanted in this layer with the following implantation energies and fluences: 

|**Ion Energy (keV) **|**Area **|**Dose (Ions/cm**<sup>2</sup>**)**|
|---|---|---|
|2300||1_._585_×_10<sup>12</sup>|
|2000||1_._2184_×_10<sup>12</sup>|
|1400||8_._9772_×_10<sup>11</sup>|
|900||6_._6804_×_10<sup>11</sup>|
|500||3_._1748_×_10<sup>11</sup>|
|360||1_._0517_×_10<sup>11</sup>|
|120||7_._0692_×_10<sup>10</sup>|
|**Total Dose**||4_._8626_×_10<sup>12</sup>|



We can then estimate the implantation profile using Stopping and Range of Ions in Matter (SRIM) simulation, as shown in Fig. S1. 

The two chips have been assembled in a flip-chip bonding machine, glued together by PMMA 950A6 only at the contact pillars of the base chip (elliptical structures at the ends of the green box in Fig. 1b). Two 200 _µ_ m-deep reservoirs are etched out around the pillars (dark pentagon regions) to contain excess PMMA, preventing it from wetting the entire device region through capillary action. 

## **Measurement setup** 

The cryogenic and room temperature setups are shown in Fig. S2. 



<!-- Start of picture text -->
12 WnLJ — 120keV<br>10 NA Ww1 —— 3650 0keV<br>Eg wv \ —— 900keV<br>2 / y —— 1400keV<br>5 6 ~ A \\ —— 2000keV<br>7<br>[92] 4 1] \ 2300keV<br>[+ H A == Total<br>24 M \<br>\<br>0>—<br>0200 400 600 800 1000<br>Depth (nm)<br><!-- End of picture text -->

7 



<!-- Start of picture text -->
7.4 GHz<br>37 MHz<br>~<br>Femto<br>ZVA<br>183-S+<br>800 MHz<br>ZVE-8G+<br>~<br>BLP<br>RC<br>1.9+<br>BLP Fast switch ZX60<br>V RC 1.9+ ~ 06183LN+<br>> 300K<br>HEMT<br>< 20mK<br>JTWPA<br>A B<br>Device<br>-20dB<br>CRYODPLX-0218NM  CRYODPLX-0218NM<br>ZFBT-6GW<br>ZFBT-6GW<br>VLF 400<br>SLP 1000<br>20 dB<br>60 dB 20 dB 20 dB 60 dB 40 dB<br>~<br>V<br><!-- End of picture text -->

FIG. S2. Experimental setup at room temperature and at low-temperature. The microwave tone driving the spins is controlled through IQ-mixing as well as with fast switches. Its transmission, or any signal emitted from the spins, is amplified by a series of four amplifiers: a Josephson parametric amlifier provided by the Lincoln lab, a HEMT amplifier, and two mini-circuits amplifiers. The DC currents controlling the KIC and microwire inductances are generated by Yokogawa voltage sources. Both channels are fitted with home-made RC filters (225 Ω, 220 pF). On the buffer side, the dc current is combined with the 3 wave-mixing tone using a bias-tee at room-temperature, and is further recombined with the microwave signal at the mixingchamber stage. On the other side, the current is recombined at low temperature with the rf drive for nuclear spin manipulation. An Anapico APSUASYN30-4 generates the 4 microwaves tones necessary to the experiments (rf, three-wave mixing, JTWPA pump, and microwave drive tone). A Quantum Machine OPX generates the low-frequency control signals (yellow squares) and perform the acquisition of the low-frequency signals (red squares). The experiment is realized in a Bluefors LD system equipped with a 3D vector magnet. Some unused components are omitted for simplicity. 



<!-- Start of picture text -->
Qp, Py, Lp Lg Qa D,<br>Cy L, T Ca<br><!-- End of picture text -->

9 

and others _gi,j_ are geometrical terms that can be expressed as a function of _L_<sup>0</sup> c<sup>,</sup><sup>_L_0</sup> a<sup>,</sup><sup>_L_b,</sup><sup>_ca_</sup> 1<sup>,</sup><sup>_cn_</sup> 1<sup>,butdonotinvolve</sup> _L_<sup>0</sup> <u>a</u><sup>_L_b</sup> _c_<sup>_a_</sup> 2<sup>and</sup><sup>_cb_</sup> 2<sup>.Wedefined</sup><sup>_L_ab=</sup> _L_<sup>0</sup> a+ _L_ b<sup>.Wenowintroducetheannihilationoperators</sup><sup>_a_ˆ=(Φa +</sup><sup>_iZ_a</sup><sup>_Q_a)</sup><sup>_/_</sup> �(2ℏ _Z_ a) and ˆ ˜ ˜ _b_ = (Φb + _iZ_ b _Q_ b) _/_ ~~�~~ (2ℏ _Z_ b), where _Z_ a = � _L_ a _/C_ a and _Z_ b = ~~�~~ _L_ b _/C_ b are the impedances of the coupled resonators. The Hamiltonian S15 can be re-expressed as a function of these operators. 

## _Three-wave mixing for dissipation engineering_ 

We now wish to derive the effective three-wave Hamiltonian, and show that it can be used to control the dissipation rate of resonator _A_ . We thus consider the action of a pump tone of amplitude _ξ_ with frequency _ω_ p _∼ ω_ a _− ω_ b applied on the buffer port, as well as a drive tone applied at _ω_ d _∼ ω_ a. We accomplish this by considering the interacting Hamiltonian _H_ int = _UHU_<sup>_†_</sup> _− i_ ℏ _U_<sup>_<u>dU</u>_</sup> _dt_<sup>_†_</sup> calculated using the following evolution operator 



where˜ we remove the classical displacement due to the application of pump on the buffer flux.˜ The displacement _ξ_ = _ξe_<sup>_−iω_</sup> p<sup>_t_</sup> can be related to the rf drive current flowing through the inductor by _ξ_ = _L_ b _I_ rf _/_<sup>_√_</sup> 2ℏ _Z_ b. In our experiment, owing to the Bragg mirror, this current can be safely related to the input pump power on the buffer port _P_ in as ~~�~~ _P_ in _/Z_ 0, since the pump tone is applied far below the Bragg mirror bandpass frequency range. Keeping only terms of _H_ int which are non zero after a time-average over one drive period, we effectively perform the rotating-wave approximation and we find: 



where we have _δ_ a = _ω_ a _− ωd_ , _δ_ b = _ω_ b + _ωp − ωd_ and: 



with _k ≈ L_<sup>0</sup> _k,n_<sup>_/√_</sup> _L_ a _L_ b and where we have neglected the contribution of _L_ a to the third-order non-linearity. We now derive the quantum Langevin equations from Eq. S21, including the dissipation on modes _a_ and _b_ , as well as a drive of strength _α_ in applied to mode _a_ : 



In the steady-state, whenever _δ_ b = 0, we find: 



where we can identify that through the three-wave mixing interaction, the buffer mode creates an additional decay channel for mode _a_ of rate 4 _g_ 3WM<sup>2</sup><sup>_/κ_b.</sup> 

> _∗_ Present address: Department of Physics and Astronomy, University of Notre Dame, IN, USA.; ywen2@nd.edu 

> _†_ patrice.bertet@cea.fr 

> [1] J. Preskill, Quantum **2** , 79 (2018). 

> [2] A. G. Fowler, M. Mariantoni, J. M. Martinis, and A. N. Cleland, Physical Review A **86** , 032324 (2012). 

> [3] E.<sup>´</sup> Gouzien and N. Sangouard, Physical Review Letters **127** , 140503 (2021). 

> [4] I. Craiciu, M. Lei, J. Rochman, J. G. Bartholomew, and A. Faraon, Optica **8** , 114 (2021). 

> [5] M. Businger, A. Tiranov, K. T. Kaczmarek, S. Welinski, Z. Zhang, A. Ferrier, P. Goldner, and M. Afzelius, Physical Review Letters **124** , 053606 (2020). 

> [6] C. T. Hann, C.-L. Zou, Y. Zhang, Y. Chu, R. J. Schoelkopf, S. M. Girvin, and L. Jiang, Physical Review Letters **123** , 250501 (2019). 

10 

- [7] T. Zhong, J. M. Kindem, J. G. Bartholomew, J. Rochman, I. Craiciu, E. Miyazono, M. Bettinelli, E. Cavalli, V. Verma, S. W. Nam, F. Marsili, M. D. Shaw, A. D. Beyer, and A. Faraon, Science **357** , 1392 (2017). 

- [8] S. Freer, S. Simmons, A. Laucht, J. T. Muhonen, J. P. Dehollain, R. Kalra, F. A. Mohiyaddin, F. E. Hudson, K. M. Itoh, J. C. McCallum, D. N. Jamieson, A. S. Dzurak, and A. Morello, Quantum Science and Technology **2** , 015009 (2017). 

- [9] V. Ranjan, J. O’Sullivan, E. Albertinale, B. Albanese, T. Chaneli`ere, T. Schenkel, D. Vion, D. Esteve, E. Flurin, J. J. L. Morton, and P. Bertet, Physical Review Letters **125** , 210505 (2020). 

- [10] D. I. Schuster, A. P. Sears, E. Ginossar, L. DiCarlo, L. Frunzio, J. J. L. Morton, H. Wu, G. A. D. Briggs, B. B. Buckley, D. D. Awschalom, and R. J. Schoelkopf, Physical Review Letters **105** , 140501 (2010). 

- [11] C. Grezes, Y. Kubo, B. Julsgaard, T. Umeda, J. Isoya, H. Sumiya, H. Abe, S. Onoda, T. Ohshima, K. Nakamura, I. Diniz, A. Auffeves, V. Jacques, J.-F. Roch, D. Vion, D. Esteve, K. Moelmer, and P. Bertet, Comptes Rendus Physique Quantum microwaves / Micro-ondes quantiques, **17** , 693 (2016). 

- [12] S. Probst, A. Bienfait, P. Campagne-Ibarcq, J. J. Pla, B. Albanese, J. F. Da Silva Barbosa, T. Schenkel, D. Vion, D. Esteve, K. Mølmer, J. J. L. Morton, R. Heeres, and P. Bertet, Applied Physics Letters **111** , 202604 (2017). 

- [13] J. O’Sullivan, O. W. Kennedy, K. Debnath, J. Alexander, C. W. Zollitsch, M. Sim˙enas,<sup>ˇ</sup> A. Hashim, C. N. Thomas, S. Withington, I. Siddiqi, K. Mølmer, and J. J. L. Morton, Physical Review X **12** , 041014 (2022), publisher: American Physical Society. 

- [14] G. Wolfowicz, A. M. Tyryshkin, R. E. George, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, M. L. W. Thewalt, S. a. Lyon, and J. J. L. Morton, Nature Nanotechnology **8** , 561 (2013). 

- [15] M. Afzelius, N. Sangouard, G. Johansson, M. U. Staudt, and C. M. Wilson, New Journal of Physics **15** , 065008 (2013). 

- [16] B. Julsgaard and K. Mølmer, Physical Review A **86** , 063810 (2012), publisher: American Physical Society. 

- [17] B. Julsgaard and K. Mølmer, Physical Review A **88** , 062324 (2013). 

- [18] J. Z. Bern´ad, M. Schilling, Y. Wen, M. M. M¨uller, T. Calarco, P. Bertet, and F. Motzoi, Journal of Physics B: Atomic, Molecular and Optical Physics **58** , 035501 (2025). 

- [19] G. Wolfowicz, S. Simmons, A. M. Tyryshkin, R. E. George, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, S. A. Lyon, M. L. W. Thewalt, and J. J. L. Morton, Physical Review B **86** , 245301 (2012). 

- [20] M. Shiddiq, D. Komijani, Y. Duan, A. Gaita-Ari˜no, E. Coronado, and S. Hill, Nature **531** , 348 (2016). 

- [21] J. Alexander, G. Dold, O. W. Kennedy, M. Sim˙enas,<sup>ˇ</sup> J. O’Sullivan, C. W. Zollitsch, S. Welinski, A. Ferrier, E. LafitteHoussat, T. Lindstr¨om, P. Goldner, and J. J. L. Morton, Physical Review B **106** , 245416 (2022), publisher: American Physical Society. 

- [22] A. Tiranov, E. Green, S. Hermans, E. Liu, F. Chiossi, D. Serrano, P. Loiseau, A. M. Kumar, S. Bertaina, A. Faraon, and P. Goldner, Sub-second spin and lifetime-limited optical coherences in $ˆ _{_ 171 _}_ $Yb$ˆ _{_ 3+ _}_ $:CaWO$ ~~4~~ $ (2025), arXiv:2504.01592 [quant-ph]. 

- [23] B. Julsgaard, C. Grezes, P. Bertet, and K. Molmer, Physical Review Letters **110** , 10.1103/PhysRevLett.110.250503 (2013). 

- [24] P. Scarlino, J. H. Ungerer, D. J. Van Woerkom, M. Mancini, P. Stano, C. M¨uller, A. J. Landig, J. V. Koski, C. Reichl, W. Wegscheider, T. Ihn, K. Ensslin, and A. Wallraff, Physical Review X **12** , 031004 (2022). 

- [25] A. J. Annunziata, D. F. Santavicca, L. Frunzio, G. Catelani, M. J. Rooks, A. Frydman, and D. E. Prober, Nanotechnology **21** , 445202 (2010). 

- [26] M. R. Vissers, J. Hubmayr, M. Sandberg, S. Chaudhuri, C. Bockstiegel, and J. Gao, Applied Physics Letters **107** , 062601 (2015). 

- [27] Y. Wu, C. Wang, D. Wang, M. Xu, Y. Zhou, and H. X. Tang, Physical Review Applied **24** , 024015 (2025). 

- [28] A. T. Asfaw, A. J. Sigillito, A. M. Tyryshkin, T. Schenkel, and S. A. Lyon, Applied Physics Letters **111** , 032601 (2017). 

- [29] M. Malnou, M. Vissers, J. Wheeler, J. Aumentado, J. Hubmayr, J. Ullom, and J. Gao, PRX Quantum **2** , 010302 (2021). 

- [30] E. Abe, H. Wu, A. Ardavan, and J. J. L. Morton, Applied Physics Letters **98** , 251108 (2011). 

- [31] T. Van Duzer, _Principles of Superconductive Devices and Circuits_ , 2nd ed. (Prentice Hall PTR, 1999). 

- [32] D. J. Parker, M. Savytskyi, W. Vine, A. Laucht, T. Duty, A. Morello, A. L. Grimsmo, and J. J. Pla, Physical Review Applied **17** , 034064 (2022). 

- [33] P. K. Tien, Journal of Applied Physics **29** , 1347 (1958). 

- [34] See Supplemental Material. 

- [35] E. H. Poindexter, P. J. Caplan, B. E. Deal, and R. R. Razouk, Journal of Applied Physics **52** , 879 (1981). 

- [36] A. Bahr, M. Boselli, B. Huard, and A. Bienfait, Applied Physics Letters **124** , 114004 (2024). 

- [37] M. H. Mohammady, G. W. Morley, and T. S. Monteiro, Physical Review Letters **105** , 067602 (2010). 

- [38] G. W. Morley, M. Warner, A. M. Stoneham, P. T. Greenland, J. Van Tol, C. W. M. Kay, and G. Aeppli, Nature Materials **9** , 725 (2010). 

- [39] R. E. George, W. Witzel, H. Riemann, N. V. Abrosimov, N. N¨otzel, M. L. W. Thewalt, and J. J. L. Morton, Physical Review Letters **105** , 067601 (2010). 

- [40] The hyperfine coupling constant _A_ , and consequently the CT configurations, are strain-dependent [43] and thus vary between samples [14, 38, 53]. 

- [41] A. Bienfait, J. J. Pla, Y. Kubo, M. Stern, X. Zhou, C. C. Lo, C. D. Weis, T. Schenkel, M. L. W. Thewalt, D. Vion, D. Esteve, B. Julsgaard, K. Mølmer, J. J. L. Morton, and P. Bertet, Nature Nanotechnology **11** , 253 (2016). 

- [42] J. J. Pla, A. Bienfait, G. Pica, J. Mansir, F. A. Mohiyaddin, Z. Zeng, Y. M. Niquet, A. Morello, T. Schenkel, J. J. L. Morton, and P. Bertet, Physical Review Applied **9** , 044014 (2018). 

- [43] V. Ranjan, B. Albanese, E. Albertinale, E. Billaud, D. Flanigan, J. J. Pla, T. Schenkel, D. Vion, D. Esteve, E. Flurin, J. J. L. Morton, Y. M. Niquet, and P. Bertet, Physical Review X **11** , 031036 (2021). 

- [44] A. Bienfait, J. Pla, Y. Kubo, X. Zhou, M. Stern, C.-C. Lo, C. Weis, T. Schenkel, D. Vion, D. Esteve, J. Morton, and 

11 

   - P. Bertet, Nature **531** , 74 (2016). 

- [45] B. Albanese, S. Probst, V. Ranjan, C. W. Zollitsch, M. Pechal, A. Wallraff, J. J. L. Morton, D. Vion, D. Esteve, E. Flurin, and P. Bertet, Nature Physics , 1 (2020). 

- [46] V. Ranjan, Y. Wen, A. K. V. Keyser, S. E. Kubatkin, A. V. Danilov, T. Lindstr¨om, P. Bertet, and S. E. de Graaf, Physical Review Letters **129** , 180504 (2022), publisher: American Physical Society. 

- [47] S. E. de Graaf, A. Jayaraman, S. E. Kubatkin, A. V. Danilov, and V. Ranjan, Applied Physics Letters **124** , 024001 (2024). 

- [48] V. Damon, M. Bonarota, A. Louchet-Chauvet, T. Chaneli`ere, and J.-L. L. Gou¨et, New Journal of Physics **13** , 093031 (2011). 

- [49] A. M. Tyryshkin, S. Tojo, J. J. L. Morton, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, T. Schenkel, M. L. W. Thewalt, K. M. Itoh, and S. A. Lyon, Nature Materials **11** , 143 (2012). 

- [50] A. J. Sigillito, H. Malissa, A. M. Tyryshkin, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, M. L. W. Thewalt, K. M. Itoh, J. J. L. Morton, A. A. Houck, D. I. Schuster, and S. A. Lyon, Applied Physics Letters **104** , (2014). 

- [51] B. C. Rose, A. M. Tyryshkin, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, M. L. W. Thewalt, K. M. Itoh, and S. A. Lyon, Physical Review X **7** , 031002 (2017). 

- [52] B. Yurke and J. S. Denker, Physical Review A **29** , 1419 (1984). 

- [53] G. Feher, Phys. Rev. **114** , 1219 (1959). 

