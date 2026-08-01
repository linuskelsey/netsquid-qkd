https://doi.org/10.1038/s41467-021-21256-7 



## ARTICLE 



### **OPEN** 

# microwave readout of a Cavity-enhanced solid-state sensor spin 

Erik R. Eisenach 1,2, John F. Barry2✉, Michael F. O’Keeffe2, Jennifer M. Schloss2, Matthew H. Steinecker2, Dirk R. Englund 1 & Danielle A. Braje2 

Overcoming poor readout is an increasingly urgent challenge for devices based on solid-state spin defects, particularly given their rapid adoption in quantum sensing, quantum information, and tests of fundamental physics. However, in spite of experimental progress in specific systems, solid-state spin sensors still lack a universal, high-fidelity readout technique. Here we demonstrate high-fidelity, room-temperature readout of an ensemble of nitrogen-vacancy centers via strong coupling to a dielectric microwave cavity, building on similar techniques commonly applied in cryogenic circuit cavity quantum electrodynamics. This strong collective interaction allows the spin ensemble’s microwave transition to be probed directly, thereby overcoming the optical photon shot noise limitations of conventional fluorescence readout. Applying this technique to magnetometry, we show magnetic sensitivity approaching the Johnson–Nyquist noise limit of the system. Our results pave a clear path to achieve unity readout fidelity of solid-state spin sensors through increased ensemble size, reduced spinresonance linewidth, or improved cavity quality factor. 

> 1 Massachusetts Institute of Technology, Cambridge, MA, USA. 2 MIT Lincoln Laboratory, Lexington, MA, USA. ✉email: john.barry@ll.mit.edu 

1 

NATURE COMMUNICATIONS | (2021) 12:1357 | https://doi.org/10.1038/s41467-021-21256-7 | www.nature.com/naturecommunications 

< 



<!-- Start of picture text -->
a) no b) 12 1 c) Directional Phase<br>sh BR - coupler shifter<br>} ~~idyd532m 637Jnm E 6 asm,b—-— . 08806 2ES) oN) o > Li<br>A——| /:; pe-ail F ogrEat iBae|| F—1aassetSess:Jal|| : 04: E§ sourceMW Ciroulator©Composite C aE Sm s 8EE)<br>_ : o. [= gi | ; g resonat or aS e<br>AN : a -6 ee 8 025 By ~ Photodiode<br>ANRY :OT i 12 |ela— ’ Pumplaser 532nmey f ie I o> =< al<br>A, CRY J eT EPI Width0 (mm) 6 12 0 Bias magnetov TestWJ coil 2MPifier Lownoe detector<br><!-- End of picture text -->

ARTICLE 

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-21256-7 

jms ¼ 0i state and the jms ¼ ±1i states. Application of a tunable bias magnetic field<sup>!</sup> B 0<sup>liftsthedegeneracyofthe</sup> j<sup>m</sup> s<sup>¼±1</sup> i states, allowing either of the jms ¼ 0i $ jms ¼ ±1i MW transitions to be individually addressed spectroscopically. The external bias field<sup>!</sup> B 0<sup>is oriented along the diamond’s 〈100〉axis to project</sup> equally onto all four NV<sup>−</sup> orientations. The MWs are applied with drive frequency ωd near-resonant with the jms ¼ 0i $ jms ¼ þ1i transition (with resonance frequency ωs), and we restrict our discussion to the effective two-level system formed by these states. The composite MW cavity consists of two concentric cylindrical dielectric resonators surrounding a high-NV<sup>-</sup> -density diamond mounted on a mechanical support wafer. We define the bare cavity resonance frequency ωc as the resonance frequency of the system in the absence of laser-induced spin polarization. Positioning the diamond at the MW magnetic field antinode, as shown in Fig. 1b, maximizes the ensemble-photon coupling. An adjustable input coupling loop couples the MW field into the composite cavity. A circulator allows for reflection measurements, while a supplementary output coupling loop allows for transmission measurements, as depicted in Fig. 1c. The composite MW cavity exhibits an unloaded quality factor of Q0 = 22,000. 

For magnetometry, the applied MW drive frequency ωd is tuned to the bare cavity resonance ωc. The bias field magnitude B0 is set so that ωs = ωc. Small changes in B0, representing the test magnetic field to be detected, cause ωs to vary about ωc. These changes in B0 (and thus ωs) are detected by monitoring MWs reflected from the cavity. To understand the readout mechanism, we first consider only the dispersive effect of the NV<sup>−</sup> ensemble, neglecting the effect of absorption. (This simplification is valid for sufficiently high-MW power, where the absorptive effect is suppressed relative to the dispersive effect; see Supplementary Note 5.) With ωs = ωc (and neglecting absorption), reflection from the cavity remains unchanged regardless of the state of the NV<sup>−</sup> ensemble (e.g., regardless of whether optical spin-polarization light is applied). As ωs shifts away from ωc, however, the NV<sup>−</sup> ensemble produces a dispersive shift that modifies the composite cavity’s resonance frequency, resulting in an increase in reflected MW power. Moreover, the dispersive effect produces a phase shift in the reflected voltage ΓVIn relative to the incident MWs (where Γ is the complex reflection coefficient and VIn is the incident MW voltage), and the sign of this phase shift depends on the sign of ωs − ωc. This allows the use of a phase-sensitive measurement technique by monitoring the quadrature port of an IQ mixer. Because the voltage on this port changes sign for deviations of ωs above or below ωc, with a zero-crossing for ωs = ωc, this measurement technique inherently provides unity contrast (see Methods). 

Spin–cavity interaction. The interaction between a MW photon and a single spin is described by the Jaynes–Cummings Hamiltonian<sup>36</sup> , 



where ^a<sup>y</sup> and ^a are the creation and annihilation operators, respectively (for photons at the bare cavity frequency ωc); ωs is the spin resonance frequency; and σ^z, σ^<sup>þ</sup> , and σ^<sup>�</sup> are the Pauli-z, raising, and lowering operators. The single-spin-photon couplingfi fi fi f gs at the cavity antinode is<sup>37–39</sup> gs ¼ 2γ<sup>n?</sup> q_Vωcavcμ0 ~~,~~ where γ is the electron gyromagnetic ratio, μ0 is the vacuum permeability, ℏ is the reduced Planck constant, and Vcav is the mode volume of the microwave cavity resonance. The coefficient n? ≤ 1 is a geometrical factor, which is required because only the component of the cavity field transverse to the spin quantization axis can drive transitions (and the spin quantization axis may be set by a 

crystallographic axis, at an energy scale much greater than that of the coupling between the magnetic field and the spin). When the cavity and spin resonances are nearly degenerate, which is the regime employed in this work, the hybridized spin–cavity modes result in the familiar spectroscopic feature known as Rabi splitting. 

For an ensemble of N polarized spins, the Jaynes–Cummings model is generalized to the Tavis–Cummings model<sup>40,41</sup> , withfi f gs replaced by the effective collective coupling geff ¼ gspN42. Predictions of this model are consistent with measurements of the MW response of solid-state spin ensembles strongly coupled to dielectric resonators at room temperature<sup>18,19</sup> . Since the MW cavity magnetic field varies by only a small amount (≈±3.5%) over the diamond volume, we assume each spin has an identical coupling strength gs. In order to provide a connection with the physical parameters of the experimental apparatus, it is convenient to develop a description of the system in terms of an equivalent circuit model. (The derivation of which is described in Supplementary Note 3.) The resulting RLC circuit model provides expressions for the reflection and transmission coefficients, which can then be formulated in terms of the quantum mechanical parameters of the system. With an ensemble undergoing constant opticalpumping-induced spin polarization at a rate κop ¼ 1=T<sup>op</sup> 1<sup>,the</sup> voltage reflection coefficient is given by 



where the cavity loss rate κc ≡ κc0 + κc1 + κc2 is the sum of the unloaded, input port, and output port loss rates, respectively; κs = 2/T2 is the homogeneous width of the spin resonance (with decoherence time T2); and ncav is the average number of cavity photons. (See Methods for the corresponding expression for the transmission coefficient and the Supplementary Note 3 for additional information on the derivation of these expressions.) Here, to simplify the presentation, we have omitted in (2) integration over the inhomogeneous distribution of spin resonance frequencies; this distribution can be included following the methods of refs.<sup>43,44</sup> . We find that the inhomogeneous linewidth must be accounted for to produce optimal agreement in numerical models used to fit the experimental data. 

Neglecting absorption, the imaginary part of the reflection coefficient can be approximately expressed in a more illuminating form within a particular regime relevant to magnetometry. For critical input coupling (κc1 = κc0), no output coupling (κc2 = 0), and ωd = ωc, the reflection coefficient in the limiting case of small spin–cavity detunings (∣ωs − ωc∣≪ κs/2) is approximately given by 



where κ<sup>�</sup> s characterizes the inhomogeneous linewidth. This approximate expression is valid for ncav high enough to saturate the homogeneous linewidth ncav � κ2ogpκ<sup>2</sup> s s<sup>but below the number to</sup> produce substantial power broadening ncav ≲ κ2opgκ<sup>2</sup> s<sup>�</sup> s<sup>~~.~~Equation(3)</sup> highlights the potential of this technique for high-sensitivity magnetometry, as Im[Γ] is proportional to spin–cavity detuning. The prefactor ðκ8<sup>�</sup> sg Þ<sup>2</sup> <u>eff</u><sup><u>2</u></sup> κc<sup>in(3)iscloselyrelatedtothecollective</sup> cooperativity, a dimensionless figure of merit for the ensemblecavity coupling strength typically defined as ξ ¼ 4κgs<sup>2</sup> κeffc <u>45.</u> To maximize spin readout fidelity, it is important to engineer the cooperativity of the ensemble-cavity system to be as large as possible. The system’s cooperativity is experimentally determined 

3 

NATURE COMMUNICATIONS | (2021) 12:1357 | https://doi.org/10.1038/s41467-021-21256-7 | www.nature.com/naturecommunications 

ARTICLE 

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-21256-7 





<!-- Start of picture text -->
B0 (Gauss)<br>-9 -6 -3 0 3 6 9<br>1.0 1.0<br>0.05<br>0.8 0.8<br>0.6 0.6<br>0.4 0.4<br>0.2 0.2<br>x19<br>0.97<br>0.0 0.0<br>-20 -15 -10 - 5 0 5 10 15 20<br>( s c) / 2 ) (MHz<br>Norm. reflected MW power<br>Norm. collected fluorescence<br>) (<br><!-- End of picture text -->

Fig. 2 Strong ensemble-cavity coupling under ambient conditions. The spin resonance frequency is swept relative to the bare cavity resonance (horizontal axis) by varying the applied magnetic field; simultaneously varying the MW drive frequency (vertical axis) reveals the spin-ensemblemodified composite cavity resonance. Data are recorded both in reflection (a) and transmission (b). The data are fit (c, d) to (2) and (4) using a 2D nonlinear least-squares solver. The fit gives geff = 2π × 0.70 MHz; see Methods for additional fit parameters. Each plot is normalized to unity, and recorded data are taken with −56 dBm of MW drive power. 

Fig. 3 Comparison of contrast and linewidth in MW cavity readout magnetic resonance and ODMR. The signal associated with the NV<sup>−</sup> ��ms ¼ 0� $ ��ms ¼ þ1� magnetic resonance is recorded simultaneously using MW cavity readout (blue solid line) and conventional optical readout (red solid line). The MW cavity readout realizes contrast C = 0.97, limited by imperfect circulator isolation, while conventional optical readout realizes contrast C = 0.05 (see Methods). For ease of comparison with the ODMR lineshape, MW cavity readout is performed here using a phase-insensitive measurement of reflected MW power, rather than the phase-sensitive technique; see Methods. Fits from the inhomogeneously-broadened numerical model (blue dashed line) and a Lorentzian model of ODMR (red dashed line) are also shown; see Supplementary Note 5. All<sup>14</sup> N hyperfine transitions are included in both models, but the hyperfine structure is not resolved due to the substantial inhomogeneous broadening. The inset shows both readout signals scaled to the same peak-to-peak values, highlighting the ≈2 × narrowing of the magnetic resonance feature observed with MW cavity readout. The leftright asymmetry in the MW cavity readout signal is attributed to ≈−20 kHz detuning of the applied microwaves from the bare cavity resonance. The applied MW power is 10 dBm. 

from the avoided crossing observed in recorded reflected and transmitted MW power, which are measured as the spin resonance frequency ωs and MW drive frequency ωd vary with respect to the bare cavity resonance ωc. These measurements, shown in Fig. 2, are performed at low MW drive power to avoid perturbing the system. For the data in Fig. 2, both coupling loops are under-coupled, resulting in a full-width-half-maximum (FWHM) loaded cavity linewidth of κc = 2π × 200 kHz (given the measured loaded quality factor QL = 14,500). We extract 2geff = 2π × 1.4 MHz (see Methods). Because the spin resonance linewidth arises from both homogeneous (e.g., dipolar interactions) and inhomogeneous (e.g., strain) mechanisms, with differing effects on the behavior of the system (see Supplementary Notes 3 and 5), the appropriate value of κs for calculating the cooperativity is not obvious. We model the cooperativity, including inhomogeneous broadening, using the method of ref.<sup>46</sup> (see Methods). This analysis produces a value ξ = 1.8 under the experimental conditions used for measurement (i.e., κc = 2π × 200 kHz) or ξ = 2.8 assuming negligible losses to input and output coupling (i.e., κc = κc0). 

Fig. 3, which shows a MW cavity readout magnetic resonance signal plotted alongside a conventional optically detected magnetic resonance (ODMR) signal recorded simultaneously. The MW cavity readout feature exhibits a FWHM linewidth of 4 MHz, while the ODMR linewidth is 8.5 MHz (FWHM). To understand this narrowing, consider the resonance feature associated with reflection from the bare cavity (i.e., the composite cavity without laser light applied) vs. MW drive frequency ωd. The cavity linewidth κc is independent of the spin resonance linewidth κs and, in principle, can be made narrower than the spin resonance by improving the cavity quality factor Q0. The linewidth of the cavitymediated magnetic resonance feature, however, is a function of both the cavity linewidth and the spin resonance linewidth; roughly speaking, the former determines the dispersive shift needed to reflect 80% input power, while the latter partially determines the size of the dispersive shift for a given change in magnetic field. Moreover, the size of the dispersive shift for a given change in magnetic field is not determined solely by the spin resonance linewidth; the size of this shift increases with increased cooperativity. Thus, the cavity-mediated linewidth can be narrower than the spin resonance linewidth for sufficiently large values of geff and sufficiently small values of κc. The cavitymediated narrowing is advantageous to magnetometer operation, as narrower magnetic resonance features can be localized with greater precision. The line narrowing effect is in agreement with 

Cavity-enhanced magnetometry. While useful for characterizing spin–cavity coupling strength, operation at low applied MW power is undesirable for high-fidelity spin readout due to the fixed contribution of Johnson noise. Applying higher MW power minimizes the fractional contribution of Johnson noise and other additive noise sources, but higher applied power will also produce deleterious broadening of the spin ensemble resonance; the optimum power is set by a balance between these two considerations (see Methods). We empirically determine that approximately 10 dBm is optimal for the present system (see Supplementary Note 5), resulting in a maximum reflected power of −2.4 dBm. The high peak reflected MW power (3.0 × 10<sup>20</sup> MW photons/s) for the NV<sup>−</sup> ensemble of ≈1.4 × 10<sup>15</sup> polarized spins, combined with unity contrast, ensures that MW photon shot noise does not limit the achievable readout fidelity (given experimentally relevant readout timescales; see Supplementary Note 1). 

The readout method also provides a cavity-mediated narrowing of the magnetic resonance feature. This narrowing is illustrated in 

4 

NATURE COMMUNICATIONS | (2021) 12:1357 | https://doi.org/10.1038/s41467-021-21256-7 | www.nature.com/naturecommunications 



<!-- Start of picture text -->
~<br>EE EE EE FIER TEE DCE EEE EE (a<br>Sie i p<br>e e es 383883388883148 84 48B804880<br><!-- End of picture text -->

. 

ARTICLE 

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-21256-7 

amplifier followed by a crystal detector (which measures a correlate of the reflected power); or through an amplifier to the RF port of an IQ mixer, with the local oscillator (LO) port driven by the reference MW component. Transmission occurs through an additional wire loop (the output coupling loop) on a translation stage and is measured on a crystal detector. 

Slight modifications of the setup are employed to collect the data shown in Figs. 2, 3 and 4, as described below. 

Strong coupling. Reflection and transmission data in Fig. 2 are collected simultaneously. For both transmission and reflection measurements, the MWs are detected using a crystal detector operating in the linear regime. During this measurement, both the input and output coupling loops are undercoupled (QL = 14,500, compared to Q0 = 22,000).<sup>!</sup> B coil<sup>is increased from approximately −6.8 G to</sup> +6.8 G (altering ωs) in steps of 0.068 G while the MW drive ωd/(2π) is varied relative to ωc/(2π) over the range −800 kHz to +800 kHz. At each step of the bias field (<sup>!</sup> B coil<sup>) sweepandat each MW drive frequency, the reflected and transmitted</sup> MWs are measured. The 2D power data are then fit to the square of the voltage reflection (equation (2)) and the square of the voltage transmission, given by 



The reflection and transmission coefficients are consistent with those derived from a quantum mechanical treatment of the electromagnetic field<sup>61–63</sup> using input-output theory<sup>64,65</sup> . The final fit parameters are geff = 2π × 0.70 MHz, κc0 = 2π × 125 kHz, κc1 = 2π × 25.3 kHz, κc2 = 2π × 33.4 kHz, and κs = 2π × 5.24 MHz. Here, the fit κs should be interpreted as an effective linewidth including inhomogeneous broadening; see Supplementary Notes 3 and 5. 

Cavity-mediated narrowing and contrast. The data in Fig. 3 are also collected employing the crystal detector to measure reflected MW power. The MW drive is set to the bare cavity resonance, ωd = ωc. The input coupling loop is critically coupled to the composite cavity, and the output coupling loop is removed, so that κc = 2κc0. The spin transition frequency ωs is tuned across the cavity resonance ωc by varying the value of<sup>!</sup> B coil<sup>asdetailedabove.Anauxiliaryphotodiodeallows</sup> simultaneous measurement of the NV<sup>−</sup> fluorescence signal. In this measurement configuration, the contrast is slightly below unity due primarily to the imperfect isolation of the MW circulator. (For CW measurements, as performed here, we define the contrast C ¼ <u>a�a b</u><sup>whereaandbdenotetherespectivemaximaand</sup> minima signal values when the bias field is swept over the magnetic resonance.) 

Magnetometry measurements and sensitivity. For magnetometry, MWs 

reflected from the composite cavity are amplified, band-pass filtered, and mixed with an attenuated and phase-shifted reference component. The reflected signal is mixed to base band using an IQ mixer. The phase of the reference component, which drives the mixer local oscillator (LO) port, is adjusted until the absorptive ( ∝ Re[Γ]VIn) and dispersive ( ∝ Im[Γ]VIn) components are isolated to the in-phase (I) and quadrature (Q) channels respectively. 

The magnetometry sensisitivity is characterized by monitoring the Q channel as a 1 μT (RMS) field is applied via the test coil. The test field is calibrated using the known dependence of the ODMR resonances on the applied field. The RMS amplitude of the test field is checked with a commercial magnetometer and also via calculation from the known coil geometry and applied current. The magnetometer sensitivity is given by 





where en is the RMSfi fi fvoltagei **f** noise floor (at the digitizer) of the double-sided spectrum (20 nV=p Hz , which occurs between 5 and 10 kHz), B<sup>RMS</sup> test<sup>is a 1 μT RMS</sup> amplitude magnetic field at 10 Hz frequency, and VDig is the RMS voltage recorded at the digitizer in response to the test magnetic field. 

Although applying higher MW power decreases fractional Johnson noise, it also broadens the dispersive resonance feature<sup>66</sup> . Hence, there exists an optimal power P to achieve a maximum absolute value of the slope jdð Im ½Γ�VRMSÞ=dωsj (where VRMS is the RMS incident MW voltage) and thus maximal sensitivity to changes in ωs. For the present system, we empirically determine that P = 10 dBm is optimal (see Supplementary Note 5), which results in a maximum reflected power of −2.4 dBm. 

In the high-MW-drive-power (i.e., primarily dispersive) regime, the maximal slope is achieved in the Q channel when ωs = ωc = ωd. By using only the permanent magnet to set ωs = ωc, we ensure that the test coil current source does not contribute to the noise floor of the magnetometer. 

#### Data availability 

The data in Figs. 1–4 that support the findings of this study are available from the corresponding author upon reasonable request. 

#### Code availability 

The code that supports the findings of this study are available from the corresponding author upon reasonable request. 

Received: 18 July 2020; Accepted: 20 January 2021; 



#### References 

1. Taylor, J. M. et al. High-sensitivity diamond magnetometer with nanoscale resolution. Nat. Phys. 4, 810–816 (2008). 

2. Chen, E. H. et al. High-sensitivity spin-based electrometry with an ensemble of nitrogen-vacancy centers in diamond. Phys. Rev. A 95, 053417 (2017). 

3. Hodges, J. S. et al. Timekeeping with electron spin states in diamond. Phys. Rev. A 87, 032118 (2013). 

4. Neumann, P. et al. High-precision nanoscale temperature sensing using single defects in diamond. Nano Lett. 13, 2738–2742 (2013). 

5. Degen, C. L., Reinhard, F. & Cappellaro, P. Quantum sensing. Rev. Mod. Phys. 89, 035002 (2017). 

6. Barry, J. F. et al. Sensitivity optimization for NV-diamond magnetometry. Rev. Mod. Phys. 92, 015004 (2020). 

7. Jiang, L. et al. Repetitive readout of a single electronic spin via quantum logic with nuclear spin ancillae. Science 326, 267–272 (2009). 

8. Neumann, P. et al. Single-shot readout of a single nuclear spin. Science 329, 542–544 (2010). 

9. Lovchinsky, I. et al. Nuclear magnetic resonance detection and spectroscopy of single proteins using quantum logic. Science 351, 836–841 (2016). 

10. Shields, B. J., Unterreithmeier, Q. P., de Leon, N. P., Park, H. & Lukin, M. D. Efficient readout of a single spin state in diamond via spin-to-charge conversion. Phys. Rev. Lett. 114, 136402 (2015). 

11. Jaskula, J. C. et al. Improved quantum sensing with a single solid-state spin via spin-to-charge conversion. Phys. Rev. Appl. 11, 064003 (2019). 

12. Bluvstein, D., Zhang, Z. & Jayich, A. C. B. Identifying and mitigating charge instabilities in shallow diamond nitrogen-vacancy centers. Phys. Rev. Lett. 122, 076101 (2019). 

13. Hopper, D. A., Grote, R. R., Exarhos, A. L. & Bassett, L. C. Near-infraredassisted charge control and spin readout of the nitrogen-vacancy center in diamond. Phys. Rev. B 94, 241201 (2016). 

14. Steiner, M., Neumann, P., Beck, J., Jelezko, F. & Wrachtrup, J. Universal enhancement of the optical readout fidelity of single electron spins at nitrogen-vacancy centers in diamond. Phys. Rev. B 81, 035205 (2010). 

15. Bourgeois, E. et al. Photoelectric detection of electron spin resonance of nitrogen-vacancy centres in diamond. Nat. Commun. 6, 8577 (2015). 

16. Siyushev, P. et al. Photoelectrical imaging and coherent spin-state readout of single nitrogen-vacancy centers in diamond. Science 363, 728–731 (2019). 

17. Chatzidrosos, G. et al. Miniature cavity-enhanced diamond magnetometer. Phys. Rev. Appl. 8, 044019 (2017). 

18. Breeze, J. D., Salvadori, E., Sathian, J., Alford, N. M. & Kay, C. W. M. Continuous-wave room-temperature diamond maser. Nature (London) 555, 493–496 (2018). 

19. Breeze, J. D., Salvadori, E., Sathian, J., Alford, N. M. & Kay, C. W. M. Roomtemperature cavity quantum electrodynamics with strongly coupled dicke states. npj Quantum Inf. 3, 40 (2017). 

20. Dicke, R. H. Coherence in spontaneous radiation processes. Phys. Rev. 93, 99–110 (1954). 

21. Angerer, A. et al. Ultralong relaxation times in bistable hybrid quantum systems. Sci. Adv. 3, e1701626 (2017). 

22. Le Floch, J. M. et al. Towards achieving strong coupling in threedimensional-cavity with solid state spin resonance. J. Appl. Phys. 119, 153901 (2016). 

23. Putz, S. et al. Protecting a spin ensemble against decoherence in the strongcoupling regime of cavity QED. Nat. Phys. 10, 720–724 (2014). 

24. Imamoǧlu, A. Cavity QED based on collective magnetic dipole coupling: spin ensembles as hybrid two-level systems. Phys. Rev. Lett. 102, 083602 (2009). 

25. Kubo, Y. et al. Strong coupling of a spin ensemble to a superconducting resonator. Phys. Rev. Lett. 105, 140502 (2010). 

26. Astner, T. et al. Coherent coupling of remote spin ensembles via a cavity bus. Phys. Rev. Lett. 118, 140502 (2017). 

27. Probst, S. et al. Anisotropic rare-earth spin ensemble strongly coupled to a superconducting resonator. Phys. Rev. Lett. 110, 157001 (2013). 

28. Amsüss, R. et al. Cavity QED with magnetically coupled collective spin states. Phys. Rev. Lett. 107, 060502 (2011). 

29. Blais, A., Huang, R.-S., Wallraff, A., Girvin, S. M. & Schoelkopf, R. J. Cavity quantum electrodynamics for superconducting electrical circuits: 

6 

NATURE COMMUNICATIONS | (2021) 12:1357 | https://doi.org/10.1038/s41467-021-21256-7 | www.nature.com/naturecommunications 

ARTICLE 

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-21256-7 

   - an architecture for quantum computation. Phys. Rev. A 69, 062320 (2004). 

30. Wallraff, A. et al. Approaching unit visibility for control of a superconducting qubit with dispersive readout. Phys. Rev. Lett. 95, 060501 (2005). 

31. Xiang, Z.-L., Ashhab, S., You, J. Q. & Nori, F. Hybrid quantum circuits: superconducting circuits interacting with other quantum systems. Rev. Mod. Phys. 85, 623–653 (2013). 

32. Poole, C. P. Electron Spin Resonance: A Comprehensive Treatise on Experimental Techniques. (Interscience Publishers, New York, 1967). 

33. Loubser, J. H. N. & van Wyk, J. A. Electron spin resonance in the study of diamond. Rep. Prog. Phys. 41, 1201–1248 (1978). 

34. Eaton, G. R., Eaton, S. S., Barr, D. P. & Weber, R. T. Quantitative EPR (Springer-Verlag Wien, 2010). 

35. Tseitlin, M., Quine, R. W., Rinard, G. A., Eaton, S. S. & Eaton, G. R. Combining absorption and dispersion signals to improve signal-to-noise for rapid-scan EPR imaging. J. Magn. Resonance 203, 305–310 (2010). 

36. Clerk, A. A., Devoret, M. H., Girvin, S. M., Marquardt, F. & Schoelkopf, R. J. Introduction to quantum noise, measurement, and amplification. Rev. Mod. Phys. 82, 1155–1208 (2010). 

37. Zhang, X., Zou, C.-L., Jiang, L. & Tang, H. X. Strongly coupled magnons and cavity microwave photons. Phys. Rev. Lett. 113, 156401 (2014). 

38. Schuster, D. I., Bishop, L. S., Chuang, I. L., DeMille, D. & Schoelkopf, R. J. Cavity QED in a molecular ion trap. Phys. Rev. A 83, 012311 (2011). 

39. Angerer, A. et al. Collective strong coupling with homogeneous Rabi frequencies using a 3D lumped element microwave resonator. Appl. Phys. Lett. 109, 033508 (2016). 

40. Tavis, M. & Cummings, F. W. Exact solution for an n-molecule—radiationfield hamiltonian. Phys. Rev. 170, 379 (1968). 

41. Kockum, A. F., Miranowicz, A., De Liberato, S., Savasta, S. & Nori, F. Ultrastrong coupling between light and matter. Nat. Rev. Phys. 1, 19–40 (2019). 

42. Colombe, Y. et al. Strong atom-field coupling for Bose–Einstein condensates in an optical cavity on a chip. Nature (London) 450, 272–276 (2007). 

43. Diniz, I. et al. Strongly coupling a cavity to inhomogeneous ensembles of emitters: potential for long-lived solid-state quantum memories. Phys. Rev. A 84, 063810 (2011). 

44. Krimer, D. O., Putz, S., Majer, J. & Rotter, S. Non-Markovian dynamics of a single-mode cavity strongly coupled to an inhomogeneously broadened spin ensemble. Phys. Rev. A 90, 043852 (2014). 

45. Tanji-Suzuki, H. et al. Interaction between atomic ensembles and optical resonators. Adv. Atomic Mol. Opt. Phys. 60, 201–237 (2011). 

46. Zens, M., Krimer, D. O. & Rotter, S. Critical phenomena and nonlinear dynamics in a spin ensemble strongly coupled to a cavity. II. Semiclassical-toquantum boundary. Phys. Rev. A 100, 013856 (2019). 

47. Fescenko, I. et al. Diamond magnetometer enhanced by ferrite flux concentrators. Phys. Rev. Res. 2, 023394 (2020). 

48. Barry, J. F. et al. Optical magnetic detection of single-neuron action potentials using quantum defects in diamond. Proc. Natl Acad. Sci. 113, 14133–14138 (2016). 

49. Bauch, E. et al. Ultralong dephasing times in solid-state spin ensembles via quantum control. Phys. Rev. X 8, 031025 (2018). 

50. Ebel, J. et al. Dispersive readout of room temperature spin qubits. Preprint at https://arxiv.org/abs/2003.07562 (2020). 

51. Morales, S. et al. Magnetocardiography measurements with<sup>4</sup> He vector optically pumped magnetometers at room temperature. Phys. Med. Biol. 62, 7267 (2017). 

52. Boto, E. et al. Moving magnetoencephalography towards real-world applications with a wearable system. Nature 555, 657–661 (2018). 

53. Falk, A. L. et al. Polytype control of spin qubits in silicon carbide. Nat. Commun. 4, 1–7 (2013). 

54. Mizuochi, N. et al. Continuous-wave and pulsed EPR study of the negatively charged silicon vacancy with s ¼ <u>32</u><sup>and C3v symmetry in n-type 4H-SiC. Phys.</sup> Rev. B 66, 235202 (2002). 

55. Castelletto, S. & Boretti, A. Silicon carbide color centers for quantum applications. J. Phys.: Photonics 2, 022001 (2020). 

56. Flower, G., Goryachev, M., Bourhill, J. & Tobar, M. E. Experimental implementations of cavity-magnon systems: from ultra strong coupling to applications in precision measurement. New J. Phys. 21, 095004 (2019). 

57. Michl, J. et al. Robust and accurate electric field sensing with solid state spin ensembles. Nano Lett. 19, 4904–4910 (2019). 

58. Vins, V. Technique of production of fancy red diamonds. U.S. Patent Application 2007/0053823 A1 (2007). 

59. Bauch, E. et al. Decoherence of ensembles of nitrogen-vacancy centers in diamond. Phys. Rev. B 102, 134210 (2020). 

60. Alsid, S. T. et al. Photoluminescence decomposition analysis: a technique to characterize N-V creation in diamond. Phys. Rev. Appl. 12, 044003 (2019). 

61. Huebl, H. et al. High cooperativity in coupled microwave resonator ferrimagnetic insulator hybrids. Phys. Rev. Lett. 111, 127003 (2013). 

62. Ghirri, A. et al. Coherently coupling distinct spin ensembles through a high-Tc superconducting resonator. Phys. Rev. A 93, 063855 (2016). 

63. Tabuchi, Y. et al. Hybridizing ferromagnetic magnons and microwave photons in the quantum limit. Phys. Rev. Lett. 113, 083603 (2014). 

64. Gardiner, C. W. & Collett, M. J. Input and output in damped quantum systems: quantum stochastic differential equations and the master equation. Phys. Rev. A 31, 3761–3774 (1985). 

65. Walls, D. F. & Milburn, G. J. Quantum Optics (Springer, 2007). 

66. Abragam, A. Principles of Nuclear Magnetism (Oxford Univ. Press, 1961). 

#### Acknowledgements 

The authors acknowledge L. M. Pham and J. A. Majumder for helpful discussions and assistance in determining properties of the experimental sample, R. McConnell for useful discussions on circuit and cavity quantum electrodynamics, and C. Panuski for helpful discussions on EPR and early theory developments. E.R.E. was supported by the National Science Foundation (NSF) through the NSF Graduate Research Fellowships Program. This material is based upon work supported by the Under Secretary of Defense for Research and Engineering under Air Force Contract No. FA8702-15-D-0001. Any opinions, findings, conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the Under Secretary of Defense for Research and Engineering. 

#### Author contributions 

J.F.B. and M.F.O. conceived the project. E.R.E. and J.F.B. designed and constructed the experimental apparatus, with D.A.B. providing technical guidance. E.R.E. performed the experiments and developed analysis software. M.F.O. developed the theory, with J.F.B., E.R.E., J.M.S., and D.A.B. providing additional theory development. E.R.E., J.M.S., M.H.S., J.F.B., and M.F.O. prepared the manuscript and contributed to data analysis. All authors discussed results and revised the manuscript. D.A.B. and D.R.E. supervised the project. 

#### Competing interests 

The authors declare no competing interests. 

#### Additional information 

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-021-21256-7. 

Correspondence and requests for materials should be addressed to J.F.B. 

Peer review information Nature Communications thanks Audrey Bienfait and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Peer reviewer reports are available. 

Reprints and permission information is available at http://www.nature.com/reprints 

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/ licenses/by/4.0/. 

© The Author(s) 2021 

7 

NATURE COMMUNICATIONS | (2021) 12:1357 | https://doi.org/10.1038/s41467-021-21256-7 | www.nature.com/naturecommunications 

