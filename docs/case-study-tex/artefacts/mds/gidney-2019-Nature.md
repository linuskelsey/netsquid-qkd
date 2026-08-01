# How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits 

### Craig Gidney<sup>1</sup> and Martin Eker˚a<sup>2</sup> 

> 1Google Inc., Santa Barbara, California 93117, USA 

> 2KTH Royal Institute of Technology, SE-100 44 Stockholm, Sweden Swedish NCSA, Swedish Armed Forces, SE-107 85 Stockholm, Sweden 

We significantly reduce the cost of factoring integers and computing discrete logarithms in finite fields on a quantum computer by combining techniques from Shor 1994, Griffiths-Niu 1996, Zalka 2006, Fowler 2012, Eker˚a-H˚astad 2017, Eker˚a 2017, Eker˚a 2018, Gidney-Fowler 2019, Gidney 2019. We estimate the approximate cost of our construction using plausible physical assumptions for large-scale superconducting qubit platforms: a planar grid of qubits with nearest-neighbor connectivity, a characteristic physical gate error rate of 10<sup>_−_3</sup> , a surface code cycle time of 1 microsecond, and a reaction time of 10 microseconds. We account for factors that are normally ignored such as noise, the need to make repeated attempts, and the spacetime layout of the computation. When factoring 2048 bit RSA integers, our construction’s spacetime volume is a hundredfold less than comparable estimates from earlier works (Van Meter et al. 2009, Jones et al. 2010, Fowler et al. 2012, Gheorghiu et al. 2019). In the abstract circuit model (which ignores overheads from distillation, routing, and error correction) our construction uses 3 _n_ + 0 _._ 002 _n_ lg _n_ logical qubits, 0 _._ 3 _n_<sup>3</sup> + 0 _._ 0005 _n_<sup>3</sup> lg _n_ Toffolis, and 500 _n_<sup>2</sup> + _n_<sup>2</sup> lg _n_ measurement depth to factor _n_ -bit RSA integers. We quantify the cryptographic implications of our work, both for RSA and for schemes based on the DLP in 

## 1 Introduction 

Peter Shor’s introduction in 1994 of polynomial time quantum algorithms for factoring integers and computing discrete logarithms [79, 89] was a historic milestone that greatly increased interest in quantum computing. Shor’s algorithms were the first quantum algorithms that achieved a superpolynomial speedup over classical algorithms, applied to problems outside the field of quantum mechanics, and had obvious applications. In particular, Shor’s algorithms may be used to break the RSA cryptosystem [73] based on the hardness of factoring integers that are the product of two similarly-sized primes (hereafter “RSA integers”), and cryptosystems based on the discrete logarithm problem (DLP), such as the Diffie-Hellman key agreement protocol [19] and the Digital Signature Algorithm [59]. 

The most expensive operation performed by Shor’s factoring algorithm is a modular exponentiation. Modern classical computers can perform modular exponentiations on numbers with thousands of bits in under a second. These two facts may at first glance appear to suggest that factoring a thousand bit number with Shor’s algorithm should only take seconds, but unfortunately (or perhaps fortunately), that is not the case. The modular exponentiation in Shor’s algorithm is performed over a superposition of exponents, meaning a quantum computer is required, and quantum hardware is expected to be many orders of magnitude noisier than classical hardware [3, 48, 78]. This noise necessitates the use of error correction, which introduces overheads that ultimately make performing reliable arithmetic on a quantum computer many orders of magnitude more expensive than on classical computers [15, 28]. 

Craig Gidney: craiggidney@google.com 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

1 

Although Shor’s algorithms run in polynomial time, and although there has been significant historical work focusing on reducing the cost of Shor’s algorithms and large scale quantum computing architectures [7, 13, 16, 17, 21, 26–28, 44, 46, 64, 67, 85, 87, 88] (summarized in [82]), the constant factors hidden by the asymptotic notation remain substantial. These constant factors must be overcome, by heavy optimization at all levels, in order to make the algorithms practical. Current quantum computers are far from being capable of executing Shor’s algorithms for cryptographically relevant problem sizes. 

### 1.1 Our contributions and a summary of our results 

In this work, we combine several novel and existing optimizations to reduce the cost of implementing Shor’s algorithms. The main hurdle to overcome is to implement one or more modular exponentiations efficiently, as these exponentiations dominate the overall cost of Shor’s algorithms. 

We use the standard square-and-multiply approach to reduce the exponentiations into a sequence of modular multiplications. We apply optimizations to reduce the number of multiplications and the cost of each multiplication. 

The number of multiplications is reduced by using windowed arithmetic [35, 51, 83], which uses small table lookups to fuse several multiplications together. It is also reduced by using Eker˚a and H˚astad’s derivatives [21, 23–25] of Shor’s algorithms, that require fewer multiplications to be performed compared to Shor’s original algorithms. 

The cost of each multiplication is reduced by combining several optimizations. We use Zalka’s coset representation of modular integers [91], which allows the use of cheaper non-modular arithmetic circuits to perform modular additions. We use oblivious carry runways [33] to split registers into independent pieces that can be worked on in parallel when performing additions. We bound the approximation error introduced by using oblivious carry runways and the coset representation of modular integers by analyzing them as approximate encoded permutations [33]. We use windowed arithmetic (again) to fuse multiple additions into individual lookup additions [35]. We use a layout of the core lookup addition operation where carry propagation is limited by the reaction time of the classical control system, and where the lookups are nearly reaction limited [37]. Finally, we optimize the overall computation by trying many possible parameter sets (e.g. window sizes and code distances) for each problem size and selecting the best parameter set. 

We estimate the approximate cost of our construction, both in the abstract circuit model, and in terms of its runtime and physical qubit usage in an error corrected implementation under plausible physical assumptions for large-scale superconducting qubit platforms with nearest neighbor connectivity (see Figure 1). Our physical estimates are based on the surface code [28]. We assume distance- _d_ logical qubits are stored using square patches of 2( _d_ + 1)<sup>2</sup> physical qubits (see Figure 8) and are operated on via lattice surgery [27, 44]. We provide concrete cost estimates for several cryptographically relevant problems, such as the RSA integer factoring problem, and various parameterizations of the DLP in finite fields. These cost estimates may be used to inform decisions on when to mandate migration from currently deployed vulnerable cryptosystems to post-quantum secure systems or hybrid systems. 

We caution the reader that, although we report two significant figures in our tables, there are large systemic uncertainties in our estimates. For example, doubling (or halving) the physical gate error rate would increase (or decrease) the number of qubits required by more than 10%. The estimates presented are intended to be ballpark figures that the cryptographic community can use to understand the potential impact of quantum computers; not exacting predictions of the future. 

Compared to previous works, we reduce the Toffoli count when factoring RSA integers by over 10x (see Table 1). To only compare the Toffoli counts as in Table 1 may prove misleading, however, as it ignores the cost of routing, the benefits of parallelization, etc. Ideally, we would like to compare our runtime and physical qubit usage to previous works in the literature. However, this is only possible when such estimates are actually reported and use physical assumptions similar to our own. The number of works for which this requirement is met is limited. 

The works by Jones et al. [46], Fowler et al. [28], and Gheorgiu et al. [30] stand out in that they use the same basic cost model as we use in this paper, enabling reasonable comparisons to be made. We improve on their estimates by over 100x (see Table 2) when accounting for slight remaining differences in the cost model. We also include other historical cost estimates [61, 85], 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

2 



<!-- Start of picture text -->
100000<br>RSA via Ekerå-Håstad, hours<br>50000 RSA via Ekerå-Håstad, megaqubits<br>RSA via Ekerå-Håstad - 0.01% gate error instead of 0.1%, hours<br>RSA via Ekerå-Håstad - 0.01% gate error instead of 0.1%, megaqubits<br>Short DLP or Schnorr DLP via EH, hours<br>10000 Short DLP or Schnorr DLP via EH, megaqubitsSchnorr DLP via Shor, hours<br>5000 Schnorr DLP via Shor, megaqubitsGeneral DLP via EH, hours<br>General DLP via EH, megaqubits<br>General DLP via Shor, hours<br>General DLP via Shor, megaqubits<br>1000<br>500<br>100<br>50<br>10<br>5<br>1<br>modulus length n (bits)<br>expected time (hours) and physical qubit count (megaqubits)<br>1024 2048 3072 4096 5120 6144 7168 8192 10240 12288 14336 16384 20480 24576 28672 32768 40960 49152 57344 65536<br><!-- End of picture text -->

Figure 1: Log-log plot of estimated space and expected-time costs, using our parallel construction, for various problems and problem sizes. See Section 3 for additional details. The jumps in space around _n_ = 32786 occur as the algorithm exceeds the error budget of the CCZ factory from [36] and switches to the T factory from [27]. Generated by ancillary file “estimate ~~c~~ osts.py”. 

||Abstract Qubits|Measurement Depth|Tofoli+T/2 Count|Tofoli+|T/2 Count (|billions)|Min Volu|me (megaq|ubitdays)|
|---|---|---|---|---|---|---|---|---|---|
|Factoring RSA integers||Asymptotic||_n_= 1024|_n_= 2048|_n_= 3072|_n_= 1024|_n_= 2048|_n_= 3072|
|Vedral et al. 1996 [87]|7_n_+ 1|80_n_<sup>3</sup> +_O_(_n_<sup>2</sup>)|80_n_<sup>3</sup> +_O_(_n_<sup>2</sup>)|86|690|2300|240|4100|23000|
|Zalka 1998 (basic) [90]|3_n_+_O_(1)|12_n_<sup>3 </sup>+_O_(_n_)|12_n_<sup>3 </sup>+_O_(_n_<sup>2</sup>)|13|100|350|16|250|1400|
|Zalka 1998 (log add) [90]|5_n_+_O_(1)|600_n_<sup>2 </sup>+_O_(_n_)|52_n_<sup>3 </sup>+_O_(_n_<sup>2</sup>)|56|450|1500|16|160|540|
|Zalka 1998 (ft mult) [90]|_≈_96_n_|_≈_2<sup>17</sup>_n_<sup>1</sup><sup>_._2</sup>|_≈_2<sup>17</sup>_n_<sup>2</sup><br>|140|550|1200|62|260|710|
|Beauregard 2002 [6]|2_n_+ 3|144_n_<sup>3 </sup>lg_n_+_O_(_n_<sup>2 </sup>lg_n_)|576_n_<sup>3 </sup>lg<sup>2</sup> _n_+_O_(_n_<sup>3 </sup>lg_n_)|62000|600000|2200000|32000|380000|1700000|
|Fowler et al. 2012 [28]|3_n_+_O_(1)|40_n_<sup>3 </sup>+_O_(_n_<sup>2</sup>)|40_n_<sup>3 </sup>+_O_(_n_<sup>2</sup>)|43|340|1200|53|850|4600|
|H¨aner et al. 2016 [42]|2_n_+ 2|52_n_<sup>3 </sup>+_O_(_n_<sup>2</sup>)|64_n_<sup>3 </sup>lg_n_+_O_(_n_<sup>3</sup>)|580|5200|19000|230|2800|13000|
|**(ours) 2019**|**3****_n_ + 0****_._002****_n_ lg****_n_**|**500****_n_**<sup>**2 **</sup>**+****_n_**<sup>**2 **</sup>**lg****_n_**|**0****_._3****_n_**<sup>**3 **</sup>**+ 0****_._0005****_n_**<sup>**3 **</sup>**lg****_n_**|**0****_._4**|**2****_._7**|**9****_._9**|**0****_._5**|**5****_._9**|**21**|
|Solving elliptic curve DLPs||Asymptotic||_n_= 160|_n_= 224|_n_= 256|_n_= 160|_n_= 224|_n_= 256|
|Roetteler et al. 2017 [74]|9_n_+_O_(lg_n_)|448_n_<sup>3</sup> lg_n_+ 4090_n_<sup>3</sup>|448_n_<sup>3</sup> lg_n_+ 4090_n_<sup>3</sup>|30|84|130|13|52|83|



Table 1: Expected costs of factoring _n_ bit RSA integers using various constructions proposed in the literature. For comparison, we include a single construction for solving the DLP in _n_ bit prime order elliptic curve groups with comparable classical security levels. The estimated minimum spacetime volumes assume modern surface code constructions, even for older papers. See Appendix A for details on each entry in this table. 



<!-- Start of picture text -->
Physical assumptions Approach Estimated costs<br>Historical cost Physical gate Cycle time Reaction time Physical Distillation Execution Physical qubits Expected runtime Expected volume<br>estimate at n  = 2048 error rate (microseconds) (microseconds) connectivity strategy strategy (millions) (days) (megaqubitdays)<br>Van Meter et al. 2009 [85] 0.2% 49 N/A planar 1000+ T and S distillation limited carry lookahead 6500 410 2600000<br>Jones et al. 2010 [46] 0.1% 0.25 N/A planar 7000 T distillation limited carry lookahead 620 10 6200<br>Fowler et al. 2012 [28] 0.1% 1 0.1 planar 1200 T reaction limited ripple carry 1000 1.1 1100<br>O’Gorman et al. 2017 [61] 0.1% 10 1 arbitrary block CCZ reaction limited ripple carry 230 3.7 850<br>Gheorghiu et al. 2019 [30] 0.1% 0.2 0.1 planar 1100 T reaction limited ripple carry 170 1 170<br>(ours) 2019 (1 factory) 0.1% 1 10 planar 1 CCZ distillation limited ripple carry 16 6 90<br>(ours) 2019 (1 thread) 0.1% 1 10 planar 14 CCZ reaction limited ripple carry 19 0.36 6.6<br>(ours) 2019 (parallel) 0.1% 1 10 planar 28 CCZ reaction limited carry runways 20 0.31 5.9<br><!-- End of picture text -->

Table 2: Historical estimates of the expected costs of factoring _n_ = 2048 bit RSA integers, and the assumptions they used. We caution the reader to carefully consider the physical assumptions of each paper when comparing their expected volumes. For example, assuming a cycle time that is 5x more optimistic will reduce the expected volume by a corresponding factor of 5. See Appendix B for details on each entry in this table. 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

3 

although in these cases the differences in physical assumptions are substantial. 

As most previous works focus either on factoring, or on the DLP in elliptic curve groups, it is hard to find references against which to compare our cost estimates for solving the DLP in multiplicative groups of finite fields. In general, the improvements we achieve for factoring RSA integers are comparable to the improvements we achieve for solving the general DLP in finite fields. As may be seen in Figure 1, the choice of parameterization has a significant impact on the costs. For the short DLP, and the DLP in Schnorr groups, we achieve significant improvements. These are primarily due to our use of derivatives of Shor’s algorithm that are optimized for these parameterizations. 

### 1.2 Notation and conventions 

Throughout this paper, we refer to the modulus as _N_ . The modulus is the composite integer to be factored, or the prime characteristic of the finite field when computing discrete logarithms. The number of bits in _N_ is _n_ = _⌈_ lg _N ⌉_ where lg( _x_ ) = log2( _x_ ). The number of modular multiplication operations to perform (i.e. the combined exponent length in the modular exponentiations) is denoted _ne_ . Our construction has a few adjustable parameters, which we refer to as _c_ exp (the exponent window length), _c_ mul (the multiplication window length), _c_ sep (the runway separation), and _c_ pad (the padding length used in approximate representations). 

In the examples and figures, we consider moduli of length _n_ = 2048 bits when _n_ needs to be explicitly specified. This is because _n_ = 2048 bits is the default modulus length in several widely used software programs [63, 80, 81]. Our optimizations are not specific to this choice of _n_ . Section 3 provides cost estimates for a range of cryptographically relevant modulus lengths _n_ . 

We often quote costs as a function of both the number of exponent qubits _ne_ and the problem size _n_ . We do this because the relationship between _ne_ and _n_ changes from problem to problem, and optimizations that improve _ne_ are orthogonal to optimizations that improve the cost of individual operations. 

### 1.3 On the structure of this paper 

The remainder of this paper is organized as follows: In Section 2, we describe our construction and the optimizations it uses, and show how to estimate its costs. We then proceed in Section 3 to describe how existing widely deployed cryptosystems are impacted by our work. In Section 4, we present several ideas and possible optimizations that we believe are worth exploring in the future. Finally, we summarize our contributions and their implications in Section 5. 

## 2 Our construction 

### 2.1 Quantum algorithms 

In Shor’s original algorithm [79], composite integers _N_ that are not pure powers are factored by computing the order _r_ of a randomly selected element _g ∈_ Z<sup>_∗_</sup> _N_<sup>.Specifically,periodfindingisper-</sup> formed with respect to the function _f_ ( _e_ ) = _g_<sup>_e_</sup> . This involves computing a modular exponentiation with _ne_ = 2 _n_ qubits in the exponent _e_ . 

If _r_ is even and _g_<sup>_r/_2</sup> _≡−_ 1, which holds with probability at least 1 _/_ 2 by [79], this yields nontrivial factors of _N_ . To see why, lift _g_ to Z. As _g_<sup>_r_</sup> _−_ 1 = ( _g_<sup>_r/_2</sup> _−_ 1)( _g_<sup>_r/_2</sup> + 1) _≡_ 0 (mod _N_ ) it suffices to compute gcd(( _g_<sup>_r/_2</sup> _±_ 1) mod _N, N_ ) to factor _N_ . 

In [21, 23, 25], Eker˚a and H˚astad explain how to factor RSA integers _N_ = _pq_ in a different way; namely by computing a short discrete logarithm. This algorithm proceeds as follows: First _y_ = _g_<sup>_N_+1</sup> is computed classically, where as before _g_ is randomly selected from Z<sup>_∗_</sup> _N_<sup>and of unknown</sup> order _r_ . Then the discrete logarithm _d_ = log _g y ≡ p_ + _q_ (mod _r_ ) is computed on the quantum computer. To see why _d ≡ p_ + _q_ (mod _r_ ), note that Z<sup>_∗_</sup> _N_<sup>has order</sup><sup>_φ_(</sup><sup>_N_) = (</sup><sup>_p−_1)(</sup><sup>_q −_1) by Euler’s</sup> totient theorem, so _d ≡ pq_ + 1 _≡ p_ + _q_ (mod _r_ ) as _r_ divides _φ_ ( _N_ ) and _pq_ + 1 _≡ p_ + _q_ (mod _φ_ ( _N_ )), with equality if _r > p_ + _q_ . For large random RSA integers, the order _r > p_ + _q_ with overwhelming probability. Hence, we may assume _d_ = _p_ + _q_ . By using that _N_ = _pq_ and _d_ = _p_ + _q_ , where _N_ 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

4 

and _d_ are both known, it is trivial to deterministically recover the factors _p_ and _q_ as the roots of the quadratic equation _p_<sup>2</sup> _− dp_ + _N_ = 0. 

The quantum part of Eker˚a and H˚astad’s algorithm is similar to the quantum part of Shor’s algorithm, except for the following important differences: there are two exponents _e_ 1 _, e_ 2, of lengths 2 _m_ and _m_ qubits respectively. The value _m_ is a positive integer that must satisfy _p_ + _q <_ 2<sup>_m_</sup> . We set _m_ = 0 _._ 5 _n_ + _O_ (1). Period finding is performed against the function _f_ ( _e_ 1 _, e_ 2) = _g_<sup>_e_1</sup> _y_<sup>_−e_2</sup> rather than the function _f_ ( _e_ ) = _g_<sup>_e_</sup> . The total exponent length is hence _ne_ = 3 _m_ = 1 _._ 5 _n_ + _O_ (1) qubits, compared to 2 _n_ qubits in Shor’s algorithm. It is this reduction in the exponent length that translates into a reduction in the overall number of multiplications that are performed quantumly. 

The two exponent registers are initialized to uniform superpositions of all 2<sup>2</sup><sup>_m_</sup> and 2<sup>_m_</sup> values, respectively, and two quantum Fourier transforms are applied independently to the two registers. This implies that standard optimization techniques, such as the square-and-multiply technique, the semi-classical Fourier transform of Griffiths and Niu [40], recycling of qubits in the exponent registers [58, 66], and so forth, are directly applicable. 

The classical post-processing algorithm used to extract the logarithm from the observed frequencies is by necessity different from Shor’s. It uses lattice-based techniques, and critically does not require _r_ to be known. Eker˚a shows in [23] that the post-processing algorithm has probability above 99% of recovering _d_ . As the factors _p_ and _q_ are recovered deterministically from _d_ and _N_ , this implies that it in general suffices to run the quantum algorithm once. 

In summary, Eker˚a and H˚astad’s algorithm is similar to Shor’s algorithm from an implementation perspective: a sequence of multiplications is computed, where one operand is in a quantum register and one operand is a classical constant. The multiplications are interleaved with the Fourier transform. It is of no significance to our construction what sequence of classical constants are used, or if one or more independent Fourier transforms need to be applied. This fact, coupled with the fact that the algorithms of Eker˚a and H˚astad may be used to solve other relevant problems where _ne_ is a different function of _n_ (see Section 3), lead us to describe our construction in terms of _n_ and _ne_ . 

Note that the above description of the algorithm has been somewhat simplified compared to the algorithm described in [23, 25] in the interest of improved legibility. Furthermore, there are technical conditions that need to be respected for the analysis in [23] to be applicable. For the full details, see Appendix A.2.1 of [23]. 

### 2.2 Reference implementation 

To avoid overloading the reader, we will describe our factoring construction by starting from a simple reference implementation of the quantum part of Shor’s original algorithm and then apply optimizations one by one. 

The reference implementation works the way most implementations of Shor’s algorithm do, by decomposing exponentiation into iterative controlled modular multiplication [6, 31, 42, 87, 90, 91]. A register _x_ is initialized to the _|_ 1 _⟩_ state, then a controlled modular multiplication of the classical constant _g_<sup>2</sup><sup>_j_</sup> (mod _N_ ) into _x_ is performed, controlled by the qubit _ej_ from the exponent _e_ , for each integer _j_ from _ne −_ 1 down to 0. After the multiplications are done, _x_ is storing _g_<sup>_e_</sup> (mod _N_ ) and measuring _x_ completes the hard part of Shor’s algorithm. 

Controlled modular multiplication is still not a primitive operation, so it must also be decomposed. It can be performed by introducing a work register _y_ initialized to _|_ 0 _⟩_ and then performing the following two controlled scaled additions: _y_ += _x · k_ (mod _N_ ) then _x_ += _y ·_ ( _−k_<sup>_−_1</sup> ) (mod _N_ ). After these two operations, _y_ is storing the result and _x_ has been cleared to the _|_ 0 _⟩_ state. Swapping the two registers, so that the result is in _x_ , completes the multiplication. 

Performing a controlled scaled addition with classical scale factor _k_ can be done with a series of _n_ controlled modular additions. For each qubit _qj_ in the input register, you add _k ·_ 2<sup>_j_</sup> (mod _N_ ) into the target, controlled by _qj_ . Controlled modular addition in turn is performed via a series of nonmodular additions and comparisons. For example, [87] uses five additions for this purpose. Finally, using the Cuccaro adder [18], uncontrolled non-modular additions can be performed with _O_ (1) additional workspace using 2 _n_ Toffolis. 

Combining the numbers in the preceding two paragraphs implies a Toffoli count of _ne·_ 2 _n·_ 5 _·_ 2 _n_ = 20 _nen_<sup>2</sup> for the reference implementation. It constitutes the baseline for the optimizations that we 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

5 

apply in the following sections. 

### 2.3 The quantum Fourier transform 

Before proceeding, note that we focus exclusively on costing the controlled modular multiplications, both in the reference implementation and throughout the remainder of this paper. This is because they constitute the hard part of Shor’s algorithm from an implementation perspective. The other part of the algorithm, the quantum Fourier transform (QFT), can be implemented semi-classically [40] and interleaved with the controlled modular multiplications. 

When the QFT is implemented in this manner (see Figure 2) it suffices to have control qubits for the window of controlled modular multiplications currently being processed, as these control qubits may be recycled [58, 66]. In the QFT, a sequence of classically controlled gates that shift the phase by 2 _π/_ 2<sup>_k_</sup> for various integers _k_ up to the QFT dimension are applied to the control qubit for each modular multiplication. This sequence can be combined into a single shift, and implemented using e.g. the technique in [10], to a level of precision far below other sources of error in the algorithm without incurring a noticeable cost. This implies that the cost of implementing the QFT is negligible. 

Note furthermore that when we analyze the success probabilities of Shor’s algorithms, and the various derivatives, we assume the use of an ideal QFT even though the implemented QFT is technically an approximation. 

### 2.4 The coset representation of modular integers 

Following Zalka [91], the first improvement we make over the reference implementation is to switch from the usual representation of integers to the coset representation of modular integers. The usual representation of an integer _k_ in a quantum computer is the computational basis state _|k⟩_ . 

The coset representation is different: It uses a periodic superposition with period _N_ and offset _k_ . In ideal conditions, the integer _k_ (mod _N_ ) is represented by the state _√_ 2<sup>_−c_pad�2</sup> _j_ =0<sup>_c_pad</sup><sup>_−_1</sup> _|jN_ + _k⟩_ where _c_ pad is the number of additional padding qubits placed at the end of the register after the high order bits. The key idea is that the periodicity of the superposition causes a non-modular adder to perform approximate modular addition on this representation, and the error of the approximation can be exponentially suppressed by adding more padding to the register. 

As we will discuss later, the amount of padding required is logarithmic in the number of operations. This small cost enables the large benefit of using non-modular adders instead of modular adders. It is possible to perform a controlled non-modular addition in 4 _n_ Toffolis [18, 32], significantly cheaper than the 10 _n_ we assumed for a controlled modular adder. Therefore switching to the coset representation reduces the leading asymptotic term of the Toffoli count of the reference implementation from 20 _nen_<sup>2</sup> to 8 _nen_<sup>2</sup> . 

### 2.5 Windowed arithmetic 

The next optimization we use is windowed arithmetic [35, 51, 83]. Specifically, we follow the modular exponentiation construction from [35] and use windowing at two levels. 

First, at the level of a multiplication, we window over the controlled additions. We fuse groups of controlled additions into single lookup additions. A lookup addition is an addition where the value to add into a register is the result of a table lookup. Small windows of the qubits that would have been used as controls for the additions are instead treated as addresses into classically precomputed tables of values to unconditionally add into the target. 

Second, at the level of the exponentiation, we window over the controlled multiplications. This is done by including exponent qubits in the addresses of all lookups being performed within the multiplications. We refer the reader to [35] for the exact details of this nested windowed arithmetic construction. 

The cost of windowed arithmetic depends on the size of the windows. Let _c_ exp be the size of the window over exponent qubits that are being used to control multiplications. Increasing _c_ exp proportionally decreases the number of multiplications needed for the modular exponentiation, since more exponent qubits are handled by each multiplication. Let _c_ mul be the size of the window over 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

6 



<!-- Start of picture text -->
| + ⟩ Rz ( ... ) | + ⟩ Rz ( ... ) . . .<br>| + ⟩ Rz ( ... ) | + ⟩ Rz ( ... ) . . .<br>Input e [ ne − 4 :  ne ] QFT Input e [ ne − 8 :  ne − 4] QFT<br>| + ⟩ Rz ( ... ) | + ⟩ Rz ( ... ) . . .<br>| + ⟩ Rz ( ... ) | + ⟩ Rz ( ... ) . . .<br>n<br>/ ×g 2 ne− 4 ·e [ ne− 4: ne ] (mod N ) ×g 2 ne − 8 ·e [ ne− 8: ne− 4] (mod N ) . . .<br><!-- End of picture text -->

Figure 2: Working through the qubits representing an exponent in Shor’s algorithm with a window size _c_ exp of four, while using a semi-classical Fourier transform [40] with recycling [58, 66]. The notation _e_ [ _a_ : _b_ ] = _⌊e/_ 2<sup>_a_</sup> _⌋_ mod 2<sup>_b−a_</sup> refers to a slice of (qu)bits in _e_ from (qu)bit index _a_ (inclusive) to (qu)bit index _b_ (exclusive). Each _Rz_ ( _. . ._ ) gate rotates by an amount determined by previous measurements, e.g. using the technique in [10]. All 16 possible values of the expression _g_<sup>_e_[4:8]24</sup> (mod _N_ ) (and similar expressions) can be precomputed classically, and looked up on demand within the multiplication circuit. This reduces the number of multiplications by a factor of the window size, at the cost of some additional lookup work within the multiplication. 

factor qubits being used to control additions. Increasing _c_ mul proportionally decreases the number of additions needed within each multiplication. By using windowed arithmetic, the _ne_ controlled multiplications we needed to perform become _ne/c_ exp uncontrolled multiplications while the 2 _n_ controlled additions we needed to perform within each multiplication become 2 _n/c_ mul uncontrolled additions. The cost of increasing _c_ exp and _c_ mul is that each addition is now accompanied by a lookup, and the Toffoli count of the lookup operation is 2<sup>_c_exp+</sup><sup>_c_mul</sup> . 

Using Cuccaro et al.’s adder [18], each _n_ -bit addition has a Toffoli count and measurement depth of 2 _n_ . Using Babbush et al.’s QROM read (section 3A of [2]), each table lookup has a Toffoli count and measurement depth of 2<sup>_c_mul+</sup><sup>_c_exp</sup> and uses a negligible _O_ ( _c_ mul + _c_ exp) ancillae. Using measurement-based uncomputation (appendix C of [8]), uncomputing each table lookup has a Toffoli count and measurement depth of 2 _√_ 2<sup>_c_mul+</sup><sup>_c_exp</sup> which is negligible compared to the lookup for the parameters we will be using. 

The measurement-based uncomputation uses max(0 _, √_ 2<sup>_c_mul+</sup><sup>_c_exp</sup> _−n_ ) ancillae (it starts by measuring away _n_ logical qubits of the lookup output register). This ancillae count is always zero for the reasonable values of _c_ mul _, c_ exp, and classically intractable values of _n_ , that we consider in this paper. The overhead due to the logarithmic padding introduced by the coset representation of modular integers is logarithmic in _n_ . 

Thus, by using windowed arithmetic, the leading term of the Toffoli count of the reference implementation has been reduced to _c_ mul2 _<u>nec</u>_ exp _<u>n</u>_<sup>(2</sup><sup>_n_+ 2</sup><sup>_c_mul+</sup><sup>_c_exp).Ifweset</sup><sup>_c_mul=</sup><sup>_c_exp=</sup><sup><u>1</u></sup> 2<sup>lg</sup><sup>_n_then</sup> we achieve a Toffoli count with leading term<sup><u>24</u></sup> lg<sup>_<u>n</u>_</sup><sup><u>2</u></sup><sup>_<u>e</u>_</sup> _n_<sup>_<u>n</u>_2.Intermsofspace,weareusing3</sup><sup>_n_+</sup><sup>_O_(lg</sup><sup>_n_)</sup> logical qubits. The qubits are distributed as follows: _n_ + _O_ (lg _n_ ) for the accumulation register storing the product, _n_ + _O_ (lg _n_ ) for a workspace register during the multiplication, _n_ + _O_ (lg _n_ ) for the lookup output register, and _O_ (lg _n_ ) qubits to hold the part of the exponent needed for the current stage of the semi-classical Fourier transform [40]. 

### 2.6 Oblivious carry runways 

The last major algorithmic optimization we apply is the use of oblivious carry runways [33]. The basic problem addressed by runways is that, normally, a carry signal generated at the bottom of a register must propagate all the way to the top of the register. This process can be short-circuited by instead terminating the carry propagation into an appropriately constructed runway. Runways allow large additions to be performed piecewise, with each piece being worked on in parallel, by terminating carries into appropriately placed runways at the end of each piece. 

As with the coset representation of modular integers, circuits using oblivious carry runways approximate the original circuit instead of perfectly reproducing it. But, as we will discuss later, increasing the runway length _c_ pad exponentially suppresses the approximation error. 

For the full details of how to add, maintain, and remove oblivious runways we refer the reader 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

7 



<!-- Start of picture text -->
register[0 ,c sep) . . . register[0 ,c sep)<br>runway0 Input r 0 . . . Input r 0 runway0<br>register[ c sep ,c sep+ c pad) ≈| + ⟩ ⊗c pad register[ c sep ,c sep+ c pad)<br>+ r 0 −r 0<br>| 0 ⟩ runway ′ 0 . . . | 0 ⟩<br>register[ c sep+ c pad , 2 c sep) . . . register[ c sep+ c pad , 2 c sep)<br>runway1 Input r 1 . . . Input r 1 runway1<br>register[2 c sep , 2 c sep+ c pad) ≈| + ⟩ ⊗c pad register[2 c sep , 2 c sep+ c pad)<br>+ r 1 −r 1<br>| 0 ⟩ runway ′ 1 . . . | 0 ⟩<br>register[2 c sep+ c pad , 3 c sep) . . . register[2 c sep+ c pad , 3 c sep)<br>...<br><!-- End of picture text -->

Figure 3: How to temporarily reduce oblivious carry runways to a single qubit, in preparation for being used as the input factor in a multiply-add operation that must iterate over all qubits in the register. The multiply-add “ should occur during the _. . ._ ” section in the middle. 

to [33]. That being said, we will point out one optimization not mentioned in that paper which applies here. Note that, ultimately, each register we add carry runways to is going to either be measured or discarded. The last thing that would happen to these registers, before they were measured or discarded, is carry runway removal. However, the carry runway removal process is classical; it can be constructed out of Toffoli gates. As a result, the carry runway removal process does not need to be performed under superposition. The register qubits and runway qubits can simply be measured just before the runways would have been removed, and the runway removal process can be performed by classical post-processing of the measurements. 

Note that we use _c_ pad for both the runway length of oblivious carry runways and the padding length of the coset representation. We do this because they have identical error mechanisms, namely unwanted carries into the extra qubits. There is negligible benefit in suppressing one more than the other. 

The major benefit of oblivious carry runways, compared to previous techniques for reducing the depth of addition such as Draper et al.’s logarithmic depth carry-lookahead adder [20], is that oblivious carry runways can be introduced gradually without incurring large overheads. The Toffoli count and workspace overheads are linear in the number of pieces _⌈n/c_ sep _⌉_ (where _c_ sep is the runway spacing) but only logarithmic in _n_ . 

For example, if you place a single runway at the midpoint of a 2048-qubit register, then the number of qubits and the number of Toffolis needed to perform an addition will increase by a couple percent but the depth of the additions is nearly halved. 

### 2.7 Interactions between optimizations 

A major benefit of the set of optimizations we have chosen to use in this paper is that they complement each other. They make orthogonal improvements that compound or reinforce, instead of conflicting. 

For example, when using the coset representation of modular integers, it is important that additions only use offsets less than _N_ . Larger offsets cause larger approximation error. However, because we are using windowed arithmetic, every addition we perform has an offset that is being returned by a table lookup. Since the entries in the tables are classically precomputed, we can classically ensure all offsets are canonicalized into the [0 _, N_ ) range. 

There are two cases where the optimizations do not mesh perfectly. 

First, using oblivious runways reduces the depth of addition but not the depth of lookups. This changes their relative costs, which affects the optimal window sizes to use in windowed arithmetic. When addition is suddenly four times faster than it used to be, the optimal window sizes _c_ exp and _c_ mul decrease by 1 (approximately). 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

8 

Second, when iterating over input qubits during a multiply-add, it is necessary to also iterate over runway qubits and padding qubits. This increases the number of lookup additions that need to be performed in order to complete a windowed multiplication. This issue is partially solved by temporarily adding the runways back into the main register before performing a multiply-add where that register is used as one of the factors (instead of the target). This temporarily reduces each runway to a single carry qubit (see Figure 3). We could reduce the runways to zero qubits, but this would require propagating the carry qubits all the way across the register, so we do not. 

### 2.8 Abstract circuit model cost estimate 

We have now described all the details necessary to estimate the cost of our implementation in the abstract circuit model. The cost depends on the two parameters specified by the problem (the input size _n_ and the number of exponent qubits _ne_ ) and also the four controllable parameters we have discussed (the exponentiation window size _c_ exp, the multiplication window size _c_ mul, the runway separation _c_ sep, and the padding/runway length _c_ pad). 

Although we do consider alternate values when producing tables and figures, in general we have found that the settings _c_ exp = _c_ mul = 5 _, c_ sep = 1024 _, c_ pad = 2 lg _n_ + lg _ne_ + 10 _≈_ 3 lg _n_ + 10 work well. In this overview we will focus on these simple, though slightly suboptimal, values. 

Recall that an exponentiation may be reduced to a sequence of _ne_ multiplications, which we process in groups of size _c_ exp. For each multiplication, we do two multiply-adds. Each multiplyadd will use several small additions to temporarily reduce the runway registers to single qubits. The multiply-add then needs to perform a sequence of additions controlled by the _n_ main register qubits, the _O_ (lg _n_ ) coset padding qubits, and the _n/c_ sep reduced runway qubits. Using windowed arithmetic, these additions are done in groups of size _c_ mul with each group handled by one lookup addition. Therefore the total number of lookup additions we need to perform is 



The lookup additions make up essentially the entire cost of the algorithm, i.e. the total Toffoli count is approximately equal to the Toffoli count of a lookup addition times the lookup addition count. This works similarly for the measurement depth. Ignoring the negligible cost of uncomputing the lookup, the Toffoli count of a lookup addition is 2 _n_ + _nc_ pad _/c_ sep + 2<sup>_c_exp+</sup><sup>_c_pad</sup> and the measurement depth is 2 _c_ sep + 2 _c_ pad + 2<sup>_c_exp+</sup><sup>_c_mul</sup> . Therefore 







These approximate upper bounds, with _ne_ set to 1 _._ 5 _n_ , are the formulae we report in the abstract and in Table 1 for the cost of factoring RSA integers. 

### 2.9 Approximation error 

Because we are using oblivious carry runways and the coset representation of modular integers, the computations we perform are not exact. Rather, they are approximations. This is not a problem in practice, as we may bound the approximation error using concepts and results from [33]. 

The oblivious runways and the coset representation of modular integers are both examples of “approximate encoded permutations” which have a “deviation”. When using a padding/runway 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

9 



<!-- Start of picture text -->
Time<br>[ [1 Workspace<br>Il CCZ Factory<br>[1 CCZ Fixup<br>[I Target Register<br>[J Factor Register<br>] Temp Register<br>Hl Lookup Workspace<br>[J MAJ/JUMA Sweep<br>a]<br>a<br>p=}<br>[of<br>©<br>2S -<br>pa)o<br>©<br>wn<br>2<br>Oo<br>[4<br>Ready Lookup Addition Unlookup Ready<br><!-- End of picture text -->

(Yuantum 

### 2.10 Spacetime layout 

Our implementation of Shor’s algorithm uses a layout that is derived from the (nearly) reaction limited layouts presented in [37]. In these layouts, a lookup addition is performed as follows (see Figure 4). All data qubits are arranged into rows. The rows of qubits making up the target register of the addition are spread out into row pairs with gaps five rows wide in between. In these gaps there will be two rows for the lookup output register, and three rows for access hallways. This arrangement allows the lookup computation two ways to access each output row, doubling the speed at which it can run, while simultaneously ensuring the target register and the lookup output register are interleaved in a convenient fashion. 

After the lookup is completed, the rows of the lookup output register and the addition target register are packed tightly against the top (or equivalently bottom) of the available area. An operating area is prepared below them, and the data is gradually streamed through the operating area while the operating area gradually shifts upward. This performs the MAJ sweep of Cuccaro’s ripple carry adder [18]. Everything then begins moving in the opposite direction in order to perform the UMA sweep on the return stroke. 

The lookup register is quickly uncomputed using measurement-based uncomputation [8], and the system is returned to a state where another lookup addition can be performed. 

In order to perform piecewise additions separated by oblivious carry runways, we simply partition the computation horizontally as shown in Figure 5 and Figure 7. The lookup before each addition prepares registers across the pieces, as shown in Figure 6, but the additions themselves stick to their own piece. 

The width of each piece is determined by the number of CCZ factories needed to run at the reaction limited rate. This number is 14, assuming a code distance of 27 and using the CCZ factories from [36, 37]. Also, assuming a level 1 code distance of 17, the footprint of the factory is 15 _×_ 8 [37]. The factories are laid out into 2 rows of 7, with single logical qubit gaps to allow space for data qubits to be routed in and out. The total width of a piece is 15 _·_ 7 + 7 = 113 logical qubits. The height of the operating area is 33 rows of logical qubits (2 _·_ 8 for the CCZ factories, three for the ripple-carry operating area, six for AutoCCZ fixup boxes, and eight for routing data qubits). The _c_ pad + _c_ sep qubits from each register add another 30 rows (approximately). So, overall, when working on a problem of size _n_ , the computation covers a 113 _w ×_ 63 grid of logical qubits where _w_ = _n/c_ sep = _n/_ 1024. 

### 2.11 Runtime 

Because our implementation is dominated almost entirely by the cost of performing lookup additions, its runtime is approximately equal to the number of lookup additions times the runtime of a single lookup addition. 

During the lookup phase of a lookup addition, the computation is code depth limited. Assuming a code depth of _d_ = 27 and a surface code cycle time of 1 microsecond, it takes 1 _µs·d/_ 2 _·_ 2<sup>_c_exp+</sup><sup>_c_mul</sup> _≈_ 14 milliseconds to perform the lookup using double-access hallways. 

During the addition phase of a lookup addition, the computation is reaction limited. Given a reaction time of 10 microseconds, it takes 2( _c_ sep + _c_ pad) _·_ 10 _µs ≈_ 22 milliseconds to perform the addition. The remaining bits of a lookup addition, such as uncomputing the lookup and rearranging the rows, take approximately 1 millisecond. Thus one lookup addition takes approximately 37 milliseconds. Given this fact, i.e. that we perform quantum lookup additions slower than most video games render entire frames, we can approximate the total runtime: 



Though we caution the reader that this estimate ignores the fact that, at larger problem sizes, lookups become slower due to the minimum code distance increasing. 

This estimate implies that factoring a 2048 bit integer will take approximately 7 hours, assuming only one run of the quantum part of the algorithm is needed. Note that in our reported numerical estimates we achieve lower per-run numbers by using more precise intermediate values and by more carefully selecting parameters. 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

11 



<!-- Start of picture text -->
— mm — 225 logical qubit columns<br>unprocessed 3<br>) o<br>factories Q<br>[a]<br>ripple carry 2<br>Q<br>factories [=2Cc[md<br>processed =g<br>7<br>idle data<br>low half of registers high half of registers<br><!-- End of picture text -->



<!-- Start of picture text -->
—oms O 225 logical qubit columns<br>0<br>w<br>double °c<br>access Q<br>data 8<br>Q<br>unary iiterate &=<br>factor o<br>actories s<br>.idle data wn<br><!-- End of picture text -->



<!-- Start of picture text -->
SORT VIN NST, VOY NT. = FL i . FO [SO . W | TY 3 nil Bem Dale iil NZ ip<br>Pe - Li wor Cad oe Cb w= ab | r= “a OTe A papla R= ARE =pa ARE Sy ARE ARE ag<br><!-- End of picture text -->

(Yuantum 

### 2.12 Distillation error 

In order to perform the 0 _._ 2 _nen_<sup>2</sup> + 0 _._ 0003 _nen_<sup>2</sup> lg _n_ Toffoli gates our implementation uses to factor an _n_ = 2048 bit RSA integer, we need to distill approximately 3 billion CCZ states. According to the spreadsheet included in [36], using a level 1 code distance 17 and a level 2 code distance of 27, this corresponds to a total distillation error of 6.4%. 

This quantity is computed by considering the initial error rate of injecting physical T states, topological error within the factory, and the likelihood of the various stages of distillation producing a false negative. 

### 2.13 Topological error 

Elsewhere in this paper we frame our hardware assumptions in terms of a physical gate error rate. In [29] it is stated that, for a physical gate error rate of 10<sup>_−_3</sup> , the probability of error in a logical qubit of distance _d_ , per surface code cycle, is approximately 10<sup>_−⌈d/_2+1</sup><sup>_⌉_</sup> . We base our cost estimates on the assumption that this scaling relationship holds. Each time the code distance is increased by two, the logical error suppression must jump by at least a factor of 10. We believe a physical error rate of 10<sup>_−_3</sup> is sufficient to achieve this scaling relationship. 

Now that we know the number of logical qubits, the runtime of the algorithm, and the relationship between code distance and logical error rates, we can approximate the probability of a topological error occurring within the surface code during the execution of the algorithm. This will allow us to verify our initial assumption that a code distance of 27 is sufficient in the case where _n_ = 2048. Larger computations will require larger code distances. 

When factoring an _n_ = 2048 bit RSA integer we are using a board of 226 _·_ 63 logical qubits. Approximately 25% of these qubits are being used for distillation, which we already accounted for, and so we do not count them in this calculation. The remaining qubits are kept through 4 _nen ·_ 1000 _≈_ 25 billion surface code cycles, which implies that the probability of a topological error arising is approximately 10<sup>_−⌈_27</sup><sup>_/_2+1</sup><sup>_⌉_</sup> _·_ 226 _·_ 63 _·_ 0 _._ 75 _·_ 25 _·_ 10<sup>9</sup> _≈_ 27%. 

This is a large error rate. Using a code distance of 27 is pushing the limits of feasibility. We would need to repeat the computation roughly 1.4 times, on average, to factor a number. If our goal is to minimize the expected spacetime volume of the computation, perhaps we should increase the code distance to 29. Doing so would increase the physical qubit count by 15%, but the error rate would drop by approximately a factor of 10 and so the expected number of runs would be much closer to 1. Ultimately the choice comes down to one’s preferences for using more space versus taking more time. 

### 2.14 Physical qubit count 

In lattice surgery, a logical qubit covers 2( _d_ + 1)<sup>2</sup> physical qubits where _d_ is the code distance (see Figure 8). Assuming we push the limits and use a code distance of 27 at _n_ = 2048, each logical qubit will cover 1568 physical qubits. Therefore the total physical qubit count is the number of logical qubits 226 _·_ 63 times 1568; approximately 23 million qubits. 

Attentive readers will note that this number disagrees with the estimate in the title of the paper. This is because, throughout this section, we have been sloppily rounding quantities up and choosing fixed parameters in order to keep things simple. The estimate in the title is produced by the ancillary file “estimate ~~c~~ osts.py”, which does not make these simplifications. (In particular, “estimate ~~c~~ osts.py” realizes that the level 1 code distance used during distillation can be reduced from 17 to 15 when _n_ = 2048 and this adjusts the layout in several fortuitous ways.) 

### 2.15 Construction summary 

We now review the basic flow of our implementation of Shor’s algorithm, including some details we would have otherwise left unstated. 

The quantum part of the algorithm starts by preparing two registers, storing zero and one respectively, into the coset representation of modular integers with oblivious carry runways. The cost of this preparation is negligible compared to the cost of the rest of the algorithm. The register 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

13 



Figure 8: Stabilizer configuration diagrams for lattice surgery qubits in the rotated surface code with code distances _d_ of (from left to right) 3, 5, and 11. Each small yellow circle is a data qubit. Each filled shape is a stabilizer that is measured each surface code cycle. Black squares are four body Z stabilizers, gray squares are four body X stabilizers, black semi-circles are two body Z stabilizers, and gray semi-circles are two body X stabilizers. Not all physical qubits are shown; in particular there is a measurement qubit present for each stabilizer. There are 2( _d_ + 1)<sup>2</sup> physical qubits per logical qubit, including the spacing between logical qubits. We assume that each increase of the code distance by 2 suppresses logical errors per surface code cycle by a factor of 10 and that this is achieved with a physical error rate of 10<sup>_−_3</sup> . 

storing one is the accumulation register that will ultimately store the modular exponentiation, while the zero register is a workspace register. 

The bulk of the execution time is then spent performing the modular exponentiation(s). Exponent qubits are iteratively introduced in groups of size _c_ exp. We are performing a semi-classical Fourier transform [40], so the exponent qubits must be phased according to measurements on previous exponent qubits. Performing the phasing operations requires using T factories instead of CCZ factories, but there is so little phasing work compared to CCZ work that we ignore this cost in our estimates. The phased exponent qubits are used as address qubits during a windowed modular multiplication, then measured in the frequency basis and discarded. See Figure 2. Within this step, almost all of the computation time is spent on lookup additions. 

After all of the modular multiplications have been completed, the accumulation register is storing the result of the modular exponentiation. Note that this register still has oblivious carry runways and is still using the coset representation of modular integers. We could decode the register before measuring it but, because the decoding operations are all classical, it is more efficient to simply measure the entire register and perform the decoding classically. As with the cost of initialization of the registers, this cost is completely negligible. 

This completes the quantum part of the algorithm. The exponent qubit measurement results, and the decoded accumulator measurement result, are fed into the classical post-processing code which uses them to derive the solution. If this fails, which can occur e.g. due to a distillation error during quantum execution, the algorithm is restarted. 

Note that there are many minor implementation details that we have not discussed. For example, during a windowed multiplication, one of the registers is essentially sitting idle except that its qubits are being used ( _c_ mul at a time) as address qubits for the lookup additions. We have not discussed how these qubits are routed into and out of the lookup computation as they are needed. It is simply clear that there is enough leeway, in the packing of the computation into spacetime, for this routing task to be feasible and contribute negligible cost. 

### 2.16 Other physical gate error rates 

Throughout this paper, we focus primarily on a physical gate error rate of 0 _._ 1%, because we consider this error rate to be plausibly achievable by quantum hardware, yet sufficiently low to enable error correction with the surface code. 

This being said, it is of course important to be conservative when estimating the security of 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

14 

cryptographic schemes. The reader may therefore also be interested in estimates for lower error rates. With this in mind, in addition to including a 0 _._ 01% curve in Figure 1, we present the following rule of thumb for translating to other error rates: 



Here _V_ ( _p_ ) is the expected spacetime volume, assuming a physical gate error rate of _p_ . The rule of thumb is based on the following observation: 

Each time the code distance of a construction is increased by 2, logical errors are suppressed by a factor roughly equal to the ratio between the code’s threshold error rate and the hardware’s physical error rate. The surface code has a threshold error rate of around 1%. For example, this means that at a physical error rate of 0 _._ 01% you suppress logical errors by 100x each time you increase the code distance by 2, whereas at a physical error rate of 0 _._ 1% the same suppression factor would require increasing the code distance by 4. Consequently, code distances tend to be half as large at a physical error rate of 0 _._ 01%. The code distance is a linear measure, and we are packing the computation into a three-dimensional space (one of the dimensions being time), so proportional improvements to the code distance get cubed. 

Hence the idea is that at a physical error rate of 0 _._ 01% code distances are half as big, meaning the computational pieces being packed into spacetime are 2<sup>3</sup> = 8 times smaller, meaning in turn that the optimal packing will also be roughly eight times smaller. Similarly, at an error rate of 0 _._ 001%, code distances are a third as big, so spacetime volumes should be roughly 27 times smaller. 

Of course, this rule of thumb is imperfect. For example, it does not account for the fact that code distances have to be rounded to integer values, or for the fact that the spacetime tradeoffs being made have to change due to the reaction time of the control system staying constant as the code distance changes, or for the fact that at really low error rates you would switch to different error correcting codes. Regardless, for order of magnitude estimates involving physical error rates between 0 _._ 3% and 0 _._ 001%, we consider this rule of thumb to be a sufficient guide. 

## 3 Cryptographic implications of our construction 

In this section, we consider how the security of RSA, and of cryptographic schemes based on the intractability of the DLP in finite fields, is affected when the optimized construction previously described is used to implement the currently most efficient derivatives of Shor’s algorithms. 

Our goal throughout this section is to minimize the overall expected spacetime volume, including expected repetitions, when factoring RSA integers or computing discrete logarithms. That is to say, we minimize the spacetime volume in each run of the quantum algorithm times the expected number of runs required. 

### 3.1 Methodology 

To minimize the spacetime volume for a given choice of _n_ and _ne_ , we consider all combinations of level 1 and 2 surface code distances _d_ 1 _∈{_ 15 _,_ 17 _, . . . ,_ 23 _}_ and _d_ 2 _∈{_ 25 _,_ 27 _, . . . ,_ 51 _}_ used during distillation and computation, window sizes _c_ mul _∈{_ 4 _,_ 5 _,_ 6 _}_ and _c_ exp _∈{_ 4 _,_ 5 _,_ 6 _}_ , runway spacings _c_ sep _∈{_ 512 _,_ 768 _,_ 1024 _,_ 1536 _,_ 2048 _}_ , and padding offsets _δ_ off _∈{_ 2 _,_ 3 _, . . . ,_ 10 _}_ where _δ_ off = _c_ pad _−_ 2 lg _n −_ lg _ne_ . Furthermore, we consider two different magic state distillation strategies: the CCZ factory from [36, 37] and the T factory from [27]. For each combination of parameters we estimate the execution time _t_ and physical qubit count _s_ , and upper bound the overall probability of errors occurring (to obtain the “retry risk” _ϵ_ ). 

To derive an upper bound on the overall probability of errors occurring, we separately estimate the probabilities of topological errors occurring due to a failure of the surface code to correct errors, of approximation errors occurring due to using oblivious carry runways and the coset representation of modular integers, of magic state distillation errors, and of the classical post-processing algorithm failing to recover the solution from a correct run of the quantum algorithm. We combine these error probabilities, assuming independence, to derive an upper bound on the overall probability of errors occurring. 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

15 

We chose to optimize the quantity _s_<sup>1</sup><sup>_._2</sup> _· t/_ (1 _− ϵ_ ), which we refer to as the “skewed expected spacetime volume”. The _t/_ (1 _− ϵ_ ) factor is the expected runtime, and the _s_<sup>1</sup><sup>_._2</sup> factor grows slightly faster than the space usage. We skew the space usage when optimizing because we have a slight preference for decreasing space usage over decreasing runtime. We consider all combinations of parameters ( _d_ 1 _, d_ 2 _, δ_ off _, c_ mul _, c_ exp _, c_ sep), choose the set that minimizes the skewed expected spacetime volume, and report the corresponding estimated costs. 

### 3.2 Implications for RSA 

Today, the arguably most commonly used modulus size for RSA is _n_ = 2048 bits. Larger moduli are however in widespread use and smaller moduli have been used historically. 

The best published academic record is the factorization of an 829 bit RSA modulus in 2020, see [11] for details regarding this computation. For the earlier record, see [50]. 

In Table 3 and Figure 1, we provide estimates for the resource and time requirements for attacking RSA for various cryptographically relevant modulus lengths _n_ . The estimates are for factoring RSA integers with Eker˚a-H˚astad’s algorithm [23, 25] that computes a short discrete logarithm, see the appendix to [23] for full technical details. As is explained in [23], a single correct run of this quantum algorithm suffices for the RSA integer to be factored with at least 99% success probability in the classical post-processing. 

|||||Para|meters|||Retry|Vol<br>(megaqu|ume<br>bitdays)|Qubits<br>(megaqubits)|Runtime<br>(hours)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|_n_|_ne_|_d_1|_d_2|_δ_of|_c_mul|_c_exp|_c_sep|Risk|per run|expected|per run|per run|
|1024|0|15|27|5|5|5|1024|6%|0_._5|0_._5|9_._7|1_._3|
|2048|_−_4|15|27|4|5|5|1024|31%|4_._1|5_._9|20|5_._1|
|3072|)|17|29|6|4|5|1024|9%|19|21|38|12|
|4096|_−_1|17|31|9|4|5|1024|5%|48|51|55|22|
|8192|_/_2|19|33|4|4|5|1024|5%|480|510|140|86|
|12288|(_n_|19|33|3|4|5|1024|12%|1700|1900|200|200|
|16384|3|19|33|4|4|5|1024|24%|3900|5100|270|350|



Table 3: Factoring an _n_ bit RSA integer by computing a short discrete logarithm. This table was produced by the script in the ancillary file “estimate ~~c~~ osts.py”. 

### 3.3 Implications for finite field discrete logarithms 

Given a generator _g_ of an order _r_ subgroup to Z<sup>_∗_</sup> _N_<sup>,wherethe modulus</sup><sup>_N_isprime,and anelement</sup> _x_ = _g_<sup>_d_</sup> , the finite field discrete logarithm problem is to compute _d_ = log _g x_ . In what follows, we assume _r_ to be prime. If _r_ is composite, the discrete logarithm problem may be decomposed into problems in subgroups of orders dividing _r_ , as shown by Pohlig and Hellman [68]. For this reason, prime order subgroups are used in cryptographic applications. As Z<sup>_∗_</sup> _N_<sup>has order</sup><sup>_N −_1,it must be that</sup><sup>_r_divides</sup><sup>_N −_1, so</sup><sup>_N_= 2</sup><sup>_rk_+1 for some integer</sup><sup>_k≥_1.</sup> The asymptotically best currently known classical algorithms for computing discrete logarithms in subgroups of this form are generic cycle-finding algorithms, such as Pollard’s _ρ_ - and _λ_ -algorithms [69], that run in time _O_ (<sup>_√_</sup> _<u>r</u>_ ) and _O_ ( _√d_ ), respectively, and the general number field sieve (GNFS), that runs in subexponential time in the bit length _n_ of _N_ . 

The idea of factoring via algebraic number fields was originally introduced by Pollard [70] for integers on special forms. It was over time generalized, by amongst others Buhler et al. [14], Lenstra et al. [55] and Pollard [71], to factor general integers, and modified by amongst others Gordon [39] and Schirokauer [75, 76] to compute discrete logarithms in finite fields. Much research effort has since been devoted to optimizing the GNFS in various respects. For an in-depth historical account of the development of the GNFS, see [53, 72]. For the best academic record, see [11]. 

Let _z_ be the number of bits of security provided by the modulus with respect to classical attacks using the GNFS. Let _nd_ and _nr_ be the lengths in bits of _d_ and _r_ , respectively. It then suffices to pick _nd, nr ≥_ 2 _z_ to achieve _z_ bits of classical security, as the generic cycle-finding algorithms are then not more efficient than the GNFS. 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

16 

When instantiating schemes based on the intractability of the finite field discrete logarithm problem, one may hence choose between using a Schnorr group, for which _nd_ = _nr_ = 2 _z_ , or a safe-prime group, for which _nr_ = _n −_ 1. In the latter case, one may in turn choose between using a short exponent, such that _nd_ = 2 _z_ , or a full length exponent, such that _nd_ = _nr_ = _n −_ 1. All three parameterization options provide _z_ bits of classical security. 

#### 3.3.1 What finite field groups are used in practice? 

In practice, Schnorr groups or safe-prime groups with short exponents are often preferred over safeprime groups with full length exponents, as the comparatively short exponents yield considerable performance improvements. 

The discrete logarithm problem in Schnorr groups is of standard form, unlike the short discrete logarithm problem in safe-prime groups, and Schnorr groups are faster to generate than safe-prime groups. A downside to using Schnorr groups is that group elements received from untrusted parties must be tested for membership of the order _r_ subgroup. This typically involves exponentiating the element to the power of _r_ , which is computationally expensive. Safe-prime groups are more flexible than Schnorr groups, in that the exponent length may be adaptively selected depending on the performance requirements. The reader is referred to [86] for a more in-depth comparison and historical recommendations. In more recent years, the use of safe-prime groups would appear to have become increasingly prevalent. Some cryptographic schemes, such as the Diffie-Hellman key agreement protocol, are agnostic to the choice of group, whereas other schemes, such as DSA, use Schnorr groups for efficiency reasons. 

The National Institute of Standards and Technology (NIST) in the United States standardizes the use of cryptography in unclassified applications within the federal government. Up until April of 2018, NIST recommended the use of randomly selected Schnorr groups with moduli of length 2048 bits for Diffie-Hellman key agreement. NIST changed this recommendation in the 3rd revision of SP800-56A [4], and are now advocating using a fixed set of safe-prime groups with moduli of length up to 8192 bits, with short or full length exponents. These groups were originally developed for TLS [38] and IKE [49] where, again, they are used either with short of full length exponents. 

#### 3.3.2 Complexity estimates 

To estimates the resource and time requirements for computing discrete logarithms in finite fields for various modulus lengths _n_ , and for the aforementioned parameterization options, we need to decide on what model to use for estimating _z_ as a function of _n_ . Various models have been proposed over the years, see for instance [9, 52, 54]. For simplicity, we use the same model that NIST uses in SP 800-56A [4]. It is described on p. 110 of FIPS 140-2 IG [60]. Note that NIST rounds _z_ to the closest multiple of eight bits. 

To compute short logarithms in safe-prime groups, the best option is to use Eker˚a-H˚astad’s algorithm [23, 25] that is specialized for this purpose. To compute general discrete logarithms in safe-prime or Schnorr groups, one option is to use Eker˚a’s algorithm [24]. As is explained in [23, 24], a single correct run of these quantum algorithms suffices for the logarithm to be recovered with _≥_ 99% success probability in the classical post-processing. These algorithms do not require the order of the group to be known. See Table 4 and Figure 1 for complexity estimates. 

If the group order is known, a better option for computing general discrete logarithms in safeprime groups and Schnorr groups when not making tradeoffs is to use Shor’s original algorithm [79], modified to work in the order _r_ subgroup rather than in the whole multiplicative group Z<sup>_∗_</sup> _N_<sup>,and</sup> to start with a uniform superposition of all exponent values, as opposed to superpositions of _r_ values. Note that the latter modification is necessary to enable the use of the semi-classical Fourier transform, qubit recycling and the windowing technique. The modified algorithm is described in [22] where a heuristic analysis is also provided. 

When using this modified version of Shor’s algorithm to compute discrete logarithms, the heuristic analysis [22] shows that a single correct run suffices to compute the logarithm with _≥_ 99% success probability, assuming that each of the two exponent registers is padded with 5 bits, and that a small search is performed in the classical post-processing. This implies that Shor’s algorithm outperforms Eker˚a’s algorithm, as Shor’s algorithm performs only approximately 2 _nr_ group operations per run, compared to 3 _nr_ operations in Eker˚a’s algorithm, see Table 5 for complexity 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

17 

|||||||||Para|meters|||Volume<br>Qubits<br>Runtime<br>Retry<br>(megaqubitdays)<br>(megaqubits)<br>(hours)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||_n_|_ne_|_nd_|_nr_|_z_|_d_1|_d_2|_δ_of|_c_mul|_c_exp|_c_sep|Risk<br>per run<br>expected<br>per run<br>per run|
||1024||||80|15|25|4|5|5|1024|10%<br>0_._2<br>0_._2<br>9_._2<br>0_._4|
||2048|_z_|||112|15|27|3|5|5|1024|9%<br>0_._9<br>1_._0<br>20<br>1_._2<br>|
|orr|3072|6|||128|15|27|9|5|5|1024|18%<br>2_._4<br>2_._9<br>29<br>2_._0<br>|
|hn|4096|_r_ =|2_z_|2_z_|152|17|29|7|4|5|1024|4%<br>6_._5<br>6_._8<br>51<br>3_._1|
|Sc|8192|3_n_|||200|17|31|3|4|5|1024|5%<br>38<br>40<br>110<br>8_._3|
||12288||||240|17|31|9|4|5|1024|9%<br>110<br>120<br>170<br>15|
||16384||||272|17|31|5|4|5|1024|17%<br>210<br>250<br>220<br>23|
||1024||||80|15|25|4|5|5|1024|10%<br>0_._2<br>0_._2<br>9_._2<br>0_._4|
||2048|_z_|||112|15|27|3|5|5|1024|9%<br>0_._9<br>1_._0<br>20<br>1_._2|
|rt|3072|6||1|128|15|27|9|5|5|1024|18%<br>2_._4<br>2_._9<br>29<br>2_._0|
|ho|4096|_d_ =|2_z_|_−_|152|17|29|7|4|5|1024|4%<br>6_._5<br>6_._8<br>51<br>3_._1|
|S|8192|3_n_||_n_|200|17|31|3|4|5|1024|5%<br>38<br>40<br>110<br>8_._3|
|me|12288||||240|17|31|9|4|5|1024|9%<br>110<br>120<br>170<br>15|
|pri|16384||||272|17|31|5|4|5|1024|17%<br>210<br>250<br>220<br>23|
|afe-|1024|)|||80|15|27|9|5|5|1024|10%<br>1_._1<br>1_._2<br>9_._7<br>2_._7<br>|
|S<br>th|2048|_−_1|||112|17|29|6|4|5|1024|6%<br>12<br>12<br>26<br>11|
|ng|3072|_n _|1|1|128|17|31|5|4|5|1024|5%<br>41<br>43<br>41<br>24|
|Le|4096|3(|_−_|_−_|152|17|31|7|4|5|1024|9%<br>97<br>110<br>55<br>43|
|ull|8192|_r_ =|_n_|_n_|200|19|33|4|4|5|1024|8%<br>960<br>1100<br>140<br>180|
|F|12288|3_n_|||240|19|33|3|4|5|1024|21%<br>3300<br>4100<br>200<br>390|
||16384||||272|21|35|4|4|5|1024|16%<br>9100<br>11000<br>320<br>700|
|able 4: <br>as prod|Comp<br>uced b|utin<br>y th|g dis<br>e scr|crete <br>ipt i|loga<br>n the|rithm<br> anci|s us<br>llary|ing E<br> fle “e|ker˚a-H<br>stima|˚astad<br>te<br>~~c~~o|’s [23,<br>sts.py”|25] and Eker˚a’s [24] algorithms. This tabl<br>.<br>Volume<br>Qubits<br>Runtime|
||||||||Pa<br>|ramete|rs||Retr<br>|y<br>(megaqubitdays)<br>(megaqubits)<br>(hours)<br><br>|
|_n_<br>|_ne_<br>|_nd_|_nr_|_z_<br>|_d_1<br>|_d_2<br>|_δ_of<br>|_c_mul<br>|_c_exp<br>|_c_sep<br>|Ris<br><br>|per run<br>expected<br>per run<br>per run<br><br><br><br>|
|1024<br>||||80|15|25<br>|6|5|5|102<br>|4<br>8%<br><br>|0_._1<br>0_._1<br>9_._2<br>0_._3<br>|
|2048|)<br>|||112|15|27|8|5|5|102|4<br>6%|0_._6<br>0_._7<br>20<br>0_._8|
|orr<br>3072|+ 5<br>|||128|15|27|6|5|5|102|4<br>13%|1_._6<br>1_._8<br>29<br>1_._3|
|hn<br>4096|_r_ <br>|2_z_|2_z_|152|15|27|3|5|5|102|4<br>25%|3_._3<br>4_._4<br>39<br>2_._1|
|Sc<br>8192|2(_n_<br>|||200|17|29|5|4|5|102|4<br>11%|23<br>26<br>110<br>5_._5|
|1228|8|||240|17|31|4|4|5|102|4<br>8%|68<br>74<br>170<br>10|
|1638|4|||272|17|31|5|4|5|102|4<br>12%|140<br>160<br>220<br>16|
|1024||||80|15|27|3|5|5|102|4<br>8%<br>|0_._7<br>0_._8<br>9_._7<br>1_._8|
|e<br>2048|)<br>|||112|17|29|3|4|5|102|4<br>5%<br>|7_._4<br>7_._8<br>26<br>7_._0<br>|
|rim<br>3072|+ 5<br>|1|1|128|17|29|4|4|5|102|4<br>12%|25<br>29<br>38<br>16|
|-p<br>4096|_r_ <br>|_−_|_−_|152|17|31|4|4|5|102|4<br>8%|65<br>70<br>55<br>29|
|fe<br>|_n_<br>|_n_|_n_||||||||%||
|a<br>819|2(<br>|||200|19|33|3|4|5|102|6|640<br>680<br>140<br>120|
|S<br>1228|8|||240|19|33|4|4|5|102|4<br>15%|2200<br>2600<br>200<br>260|
|1638|4|||272|21|35|2|4|5|102|4<br>12%|6100<br>6900<br>320<br>470|



Table 4: Computing discrete logarithms using Eker˚a-H˚astad’s [23, 25] and Eker˚a’s [24] algorithms. This table was produced by the script in the ancillary file “estimate ~~c~~ osts.py”. 

Table 5: Computing discrete logarithms using Shor’s algorithm [79] modified as described in [21, 22]. This table was produced by the script in the ancillary file “estimate ~~c~~ osts.py”. 

estimates. This is because Eker˚a’s algorithm does not require _r_ to be known. In fact, it computes both _d_ and _r_ . 

Note that for safe-prime groups, _r_ = ( _N −_ 1) _/_ 2, so when _N_ is known to the adversary then so is _r_ . For Schnorr groups, it may be that _r_ is unknown to the adversary, especially if the group is randomly selected. It may be hard to compute _r_ classically, as it amounts to finding a _nr_ = 2 _z_ bit prime factor of ( _N −_ 1) _/_ 2. 

### 3.4 Implications for elliptic curve discrete logarithms 

Over the past decades cryptographic schemes based on the intractability of the DLP in finite fields and the RSA integer factoring problem have gradually been replaced by cryptography based on the intractability of the DLP in elliptic curve groups. This is reflected in standards issued by organizations such as NIST. 

Not all optimizations developed in this paper are directly applicable to arithmetic in elliptic curve groups. It is an interesting topic for future research to study to what extent the optimizations developed in this paper may be adapted to optimize such arithmetic operations (see Section 4.5). This paper should not be perceived to indicate that the RSA integer factoring problem and the DLP in finite fields is in itself less complex than the DLP in elliptic curve groups on quantum computers. The feasibility of optimizing the latter problem must first be properly studied. 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

18 

### 3.5 On the importance of complexity estimates 

It is important to estimate the complexity of attacking widely deployed asymmetric cryptographic schemes using future large-scale quantum computers. Such estimates enable informed decisions to be made on when to mandate migration from existing schemes to post-quantum secure schemes. 

For cryptographic schemes that are used to protect confidentiality, such as encryption and key agreement schemes, a sufficiently long period must elapse inbetween the point in time when the scheme ceases to be used, and the point in time when the scheme is projected to become susceptible to practical attacks. This is necessary so as to ensure that the information that has been afforded protection with the scheme is no longer sensitive once the scheme becomes susceptible to practical attacks. This is because one must assume that encrypted information may be recorded and archived for decryption in the future. 

If the information you seek to protect is to remain confidential for 25 years, you must hence stop using asymmetric schemes such as RSA and Diffie-Hellman at least 25 years before quantum computers capable of breaking these schemes become available to the adversary. For cryptographic schemes that are used to protect authenticity, or for authentication, such as signature schemes, it suffices to migrate to post-quantum secure schemes only right before the schemes become susceptible to practical attacks. This is an important distinction. 

### 3.6 On early adoption of post-quantum secure schemes 

The process of transitioning to post-quantum secure schemes has already begun. However, no established or universally recognized standards are as of yet available. Early adopters may therefore wish to consider implementing schemes conjectured to be post-quantum secure alongside existing classically secure schemes, in such a fashion that both schemes must be broken for the combined hybrid scheme to be broken. 

## 4 Future work 

### 4.1 Investigate asymptotically efficient multiplication 

The multiplication circuits that we are using have a Toffoli count that scales quadratically (up to polylog factors). There are multiplication circuits with asymptotically better Toffoli counts. For example, the Karatsuba algorithm [47] has a Toffoli count of _O_ ( _n_<sup>lg 3</sup> ) and the Sch¨onhage–Strassen algorithm [77] has a Toffoli count of _O_ ( _n_ lg _n_ lg lg _n_ ). However, there are difficulties when attempting to use these asymptotically efficient algorithms in the context of Shor’s algorithm. 

The first difficulty is that efficient multiplication algorithms are typically classical, implemented with non-reversible computation in mind. They need to be translated into a reversible form. This is not trivial. For example, a naive translation of Karatsuba multiplication will result in twice as many recursive calls at each level (due to the need to uncompute), and increase the asymptotic Toffoli count from _O_ ( _n_<sup>lg 3</sup> ) to _O_ ( _n_<sup>lg 6</sup> ). Attempting to fix this problem can result in the space complexity increasing [65], though it is possible to solve this problem [34]. 

The second difficulty is constant factors, both in workspace and in Toffoli count. Clever multiplication circuits have better Toffoli counts for sufficiently large _n_ but, when we do back-of-theenvelope estimates, “sufficiently large” is beyond _n_ = 2048. This difficulty is made worse if the multiplier is incompatible with optimizations that work on naive multipliers, such as windowed arithmetic and the coset representation of modular integers. Clever multiplication circuits also tend to use additional workspace, and it is necessary to contrast using the better multiplier against the opportunity cost of using the space for other purposes (such as distillation of magic states). For example, the first step of the Sch¨onhage–Strassen algorithm is to pad the input up to double length, then split the padded register into _O_ (<sup>_√_</sup> _<u>n</u>_ <u>)</u> pieces and pad each piece up to double length. The target register quadruples in size before even getting into the details of performing the number theoretic transform! This large increase in space means that the quantum variant of the Sch¨onhage–Strassen algorithm is competing with the many alternative opportunities one has when given 6000 more logical qubits of workspace (at _n_ = 2048). For example, that’s enough space for fifty additional CCZ factories. 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

19 

Can multipliers with asymptotically lower Toffolis counts help at practical sizes, such as _n_ = 2048 bits? We believe that they do not, but only a careful investigation can properly determine the answer to this question. 

### 4.2 Optimize distillation 

To produce our magic states, we use slightly-modified copies of the CCZ factory from [36] as explained in [37]. We have many ideas for improving on this approach. 

First, the factory we are using is optimized for the case where it is working in isolation. But, generally speaking, error correcting codes get better when working over many objects instead of one object. It is likely that a factory using a block code to produce multiple CCZ states at once would perform better than the factory we used. For example, [41] presents a distillation protocol that produces good CCZ states ten at a time. 

Second, since publishing [36], we have realized there are two obvious-in-hindsight techniques that could be used to reduce the volume of the factories in that paper. First, we assumed that topological errors that can occur within the factories were undetected, but actually many of them are heralded as distillation failures. By taking advantage of this heralding, it should be possible to reduce the code distance used in many parts of the factories. Second, when considering the set of S gates to apply to correct T gate teleportations performed by the factories, there are redundancies that we were not previously aware of. In particular, for each measured X stabilizer, one can toggle whether or not every qubit in that stabilizer has an S gate applied to it. This freedom makes it possible to e.g. apply dynamically chosen corrections while guaranteeing that the number of S gate fixups in the 15-to-1 T factory is at most 5 (instead of 15), or to ensure a particular qubit will never need an S gate fixup (removing some packing constraints). 

Third, we believe it should be possible to use detection events produced by the surface code to estimate how likely it is that an error occurred, and that this information can be use to discard “risky factory runs” in a way that increases reliability. This would allow us to trade the increased reliability for a decreased code distance. As an extreme example, suppose that instead of attempting to correct errors during a factory run we simply discarded the run if there were any detection events where a local stabilizer flipped. Then the probability that a factory run would complete without being discarded would be approximately zero, but when a run did pass the chance of error would be amazingly low. We believe that by picking the right metric (e.g. number of detections or diameter of alternating tree during matching), then interpolating a rejection threshold between the extreme no-detections-anywhere rule and the implicit hope-all-errors-were-corrected rule that is used today, there will be a middle ground with lower expected volume per magic state. (Even more promisingly, this thresholded error estimation technique should work on any small state production task and almost all quantum computation can be reformulated as a series of small state production tasks.) 

Reducing the volume of distillation would improve the space and time estimates in this paper. But turning some combination of the above ideas into a concrete factory layout, with understood error behavior, is too large of a task for one paper. Of course, the problem of finding small factories is a problem that the field has been exploring for some time. In fact, in the week before we first released this paper, Daniel Litinsky made [56] available. He independently arrived at the idea of using distillation to herald errors within the factory, and provided rough numerics indicating this may reduce the volume of distillation by as much as a factor of 10. Therefore we leave optimizing distillation not as future work, but as ongoing work. 

### 4.3 Optimize qubit encoding 

Most of the logical qubits in our construction spend most of their time sitting still, waiting for other qubits to be processed. It should be possible to store these qubits in a more compact, but less computationally convenient, form. A simple example is that resting qubits do not need the “padding layer” between qubits implicit in Figure 8, because this layer is only there to make surgery easier. Another example is that there may to be ways to pack lattice surgery qubits that use less area while preserving the code distance (e.g. the “bulbs” shown in Figure 9). 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

20 



Figure 9: A possible dense packing for idle qubits, using 1 _._ 5 _d_<sup>2</sup> + _O_ ( _d_ ) physical qubits instead of 2( _d_ + 1)<sup>2</sup> . In the diagram, there is one distance 13 logical qubit per “bulb”. The X and Z observables of one of the logical qubits are shown in red and blue respectively. The pattern continues past the cut-off at the left and right sides. 

One could also imagine encoding the resting qubits into a block code. The difficulty is in finding a block code that a) works with small groups of qubits, b) can be encoded and decoded fast enough and compactly enough to fit into the existing computation, and c) is sufficiently better than the surface code that the benefits (reduced code distance within the surface code) outweigh the costs (redundant additional qubits). 

Finally, there are completely different ways of storing information in the surface code. For example, qubits stored using dislocations [43] could be denser than qubits stored using lattice surgery. However, dislocations also create runs of stabilizers over not-quite-adjacent physical qubits. Measuring these stabilizers requires additional physical operations, creating more opportunities for errors, and so errors will propagate more quickly along these runs. 

Do the “qubit houses” in Figure 9 actually work, or is there some unexpected error mechanism? Can dislocation qubits be packed more tightly than lattice surgery qubits while achieving an equivalent logical error rate? Is there a block code that is sufficiently beneficial when layered over surface code qubits? Until careful simulations are done it will be unclear what the answer to these questions is, and so we leave the answers to future work. 

### 4.4 Distribute the computation 

An interesting consequence of how we parallelize addition, by segmenting registers into pieces terminated by carry runways, is that there is limited interaction between the different pieces. In fact, the additions themselves require _no_ communication between the pieces; it is only the lookup procedure preparing the input of the additions that requires communication. If we place each piece on a separate quantum computer, only a small amount of communication is needed to seed the lookups and keep the computation progressing. 

Given the parameters we chose for our construction, each lookup is controlled by ten address qubits. Five of those qubits come from the exponent and are re-used hundreds of times. The other five come from the factor register, which is being iterated over during multiplication. If the computation was to be distributed over multiple machines, the communication cost would be dominated by broadcasting the successive groups of five qubits from the factor register. 

Recall from Section 2 that each lookup addition takes approximately 37 milliseconds. Five qubits must be broadcast per lookup addition. Therefore, if each quantum computer had a 150 qb/s quantum channel, the necessary qubits could be communicated quickly enough to keep up with the lookup additions. This would distribute the factoring computation. 

For example, a network topology where the computers were arranged into a linear chain and were constantly forwarding the next set of factor qubits to each other would be sufficient. Each quantum computer in the distributed computation would have a computational layout basically equivalent to the left half (or right half) of Figure 7. Factoring an _n_ = 2048 bit number could 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

21 

be performed with two machines each having perhaps 11 million physical qubits, instead of one machine with 20 million physical qubits. 

We can decrease the size of each individual quantum computer by decreasing the piece size we use for the additions. For example, suppose we used an addition piece size of _c_ sep = 256 and distributed an _n_ = 2048 RSA factoring computation over 8 machines. Normally using smaller pieces would proportionally accelerate the addition, but the number of magic state factories has not changed (they have simply been distributed) so each lookup addition will still take approximately the same amount of time. So a 150 qb/s quantum channel per computer should still be sufficient. One caveat here is that each of these much smaller machines has to run its own copy of the lookup operation, and because there are so few factories per machine the lookup will take much longer. The optimal windows sizes of the lookups will decrease, and the total computation time will approximately double. 

Based on this surface analysis it seems that, instead of using 1 machine with 20 million qubits, we could use 8 machines each with perhaps 4 million qubits, as long as they were connected by quantum channels with bandwidths of 150qb/s. But we have not carefully explored the question of how to distribute a quantum computation structured in this way and, although there has been significant previous work done on distributing quantum computations such as [45, 62, 84], we think the piecewise nature of carry runway adders makes them well suited to a specialized analysis. 

### 4.5 Revisit elliptic curves 

Many of the optimization techniques that we use in this paper generalize to other contexts where arithmetic is performed. In particular, consider the Toffoli count for computing discrete logarithms over elliptic curves reported in [74]. It can likely be improved substantially by using windowed arithmetic. On the other hand, because of the need to compute modular inverses, it is not clear if the coset representation of modular integers is applicable. 

Which of our optimizations can be ported over, and which ones cannot? How much of an improvement would result? These are interesting questions for future research work. 

## 5 Conclusion 

In this paper, we combined several techniques and optimizations into an efficient construction for factoring integers and computing discrete logarithms over finite fields. We estimated the approximate cost of our construction, both in the abstract circuit model and under plausible physical assumptions for large-scale quantum computers based on superconducting qubits. We presented concrete cost estimates for several cryptographically relevant problems. Our estimated costs are orders of magnitude lower than in previous works with comparable physical assumptions. 

In [57], Mosca poses the rhetorical question: “How many physical qubits will we need to break RSA-2048? [...] Current estimates range from tens of millions to a billion physical qubits”. One of the sources estimating a billion physical qubits is [28]. Our physical assumptions are more pessimistic than the physical assumptions used in that paper (see Table 2) so it is reasonable to say that, in the four years since 2015, the upper end of the estimate of how many qubits will be needed to factor 2048 bit RSA integers has dropped nearly two orders of magnitude; from a billion to twenty million. 

Clearly the low end of Mosca’s estimate should also drop. However, the low end of the estimate is highly sensitive to advances in the design of quantum error correcting codes, the engineering of physical qubits, and the construction of quantum circuits. Predicting such advances is beyond the scope of this paper. 

Post-quantum cryptosystems are in the process of being standardized [1], and small-scale experiments with deploying such systems on the internet have been performed [12]. However, a considerable amount of work remains to be done to enable large-scale deployment of post-quantum cryptosystems. We hope that this paper informs the rate at which this work needs to proceed. 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

22 

## Contributions 

Craig Gidney designed the efficient construction for modular exponentiation, produced initial cost estimates for RSA, and assembled results from other papers for comparison. Martin Eker˚a did the cryptographic impact analysis, and extended the construction and cost estimates to problems beyond factoring RSA integers and to algorithms beyond Shor’s factoring algorithm. 

## Acknowledgements 

We thank Adam Langley, Ilya Mironov, Ananth Raghunathan, and Ryan Babbush for reading a draft of this paper and providing useful feedback which improved it. We thank Austin Fowler and Johan H˚astad for useful feedback and discussions. Craig Gidney thanks Hartmut Neven for creating an environment where this research was possible in the first place. 

## References 

- [1] G. Alagic, J. Alperin-Sheriff, D. Apon, D. Cooper, Q. Dang, Y.-K. Liu, C. Miller, D. Moody, R. Peralta, R. Perlner, A. Robinson, and D. Smith-Tone. Status Report on the First Round of the NIST Post-Quantum Cryptography Standardization Process. Technical Report NIST Internal Report (NISTIR) 8240, NIST, January 2019. DOI: 10.6028/NIST.IR.8240. 

- [2] R. Babbush, C. Gidney, D. W. Berry, N. Wiebe, J. McClean, A. Paler, A. Fowler, and H. Neven. Encoding Electronic Spectra in Quantum Circuits with Linear T Complexity. _Physical Review X_ , 8(4):041015(1–36), 2018. DOI: 10.1103/PhysRevX.8.041015. arXiv:1805.03662. 

- [3] R. Barends, J. Kelly, A. Megrant, A. Veitia, D. Sank, E. Jeffrey, T. C. White, J. Mutus, A. G. Fowler, B. Campbell, Y. Chen, Z. Chen, B. Chiaro, A. Dunsworth, C. Neill, P. O’Malley, P. Roushan, A. Vainsencher, J. Wenner, A. N. Korotkov, A. N. Cleland, and J. M. Martinis. Superconducting quantum circuits at the surface code threshold for fault tolerance. _Nature_ , 508:500–503, April 2014. DOI: 10.1038/nature13171. arXiv:1402.4848. 

- [4] E. Barker, L. Chen, A. Roginsky, A. Vassilev, and R. Davis. Recommendation for Pair-Wise Key-Establishment Schemes Using Discrete Logarithm Cryptography. Technical Report NIST Special Publication (SP) 800-56A, Rev. 3, NIST, April 2018. DOI: 10.6028/NIST.SP.80056Ar3. 

- [5] E. Barker, L. Chen, A. Roginsky, A. Vassilev, R. Davis, and S. Simon. Recommendation for Pair-Wise Key Establishment Using Integer Factorization Cryptography. Technical Report NIST Special Publication (SP) 800-56B, Rev. 2, NIST, March 2019. DOI: 10.6028/NIST.SP.800-56Br2. 

- [6] S. Beauregard. Circuit for Shor’s algorithm using 2 _n_ + 3 qubits. _Quantum Information & Computation_ , 3(2):175–185, 2003. DOI: 10.26421/QIC3.2-8. arXiv:quant-ph/0205095. 

- [7] D. Beckman, A. N. Chari, S. Devabhaktuni, and J. Preskill. Efficient networks for quantum factoring. _Physical Review A_ , 54(2):1034, 1996. DOI: 10.1103/PhysRevA.54.1034. arXiv:quantph/9602016. 

- [8] D. W. Berry, C. Gidney, M. Motta, J. R. McClean, and R. Babbush. Qubitization of Arbitrary Basis Quantum Chemistry Leveraging Sparsity and Low Rank Factorization. _Quantum_ , 3:208, 2019. DOI: 10.22331/q-2019-12-02-208. arXiv:1902.02134. 

- [9] BlueKrypt. Cryptographic Key Length Recommendation. `https://www.keylength.com` , 2019. URL `https://www.keylength.com` . Accessed: 2019-03-03. 

- [10] A. Bocharov, M. Roetteler, and K. M. Svore. Efficient Synthesis of Universal RepeatUntil-Success Quantum Circuits. _Physical Review Letters_ , 114:080502, Feb 2015. DOI: 10.1103/PhysRevLett.114.080502. arXiv:1404.5320. 

- [11] F. Boudot, P. Gaudry, A. Guillevic, N. Heninger, E. Thom´e, and P. Zimmermann. Comparing the Difficulty of Factorization and Discrete Logarithm: A 240-Digit Experiment. In _Advances in Cryptology – CRYPTO 2020_ , volume 12171 of _Lecture Notes in Computer Science (LNCS)_ , pages 62–91. Springer, 2020. DOI: 10.1007/978-3-030-56880-1˙3. 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

23 

- [12] M. Braithwaite. Experimenting with post-quantum cryptography. `https://security. googleblog.com/2016/07/experimenting-with-post-quantum.html` , July 2016. URL `https://security.googleblog.com/2016/07/experimenting-with-post-quantum.html` . 

- [13] S. Bravyi and A. Kitaev. Universal quantum computation with ideal Clifford gates and noisy ancillas. _Physical Review A_ , 71(2):022316, 2005. DOI: 10.1103/PhysRevA.71.022316. arXiv:quant-ph/0403025. 

- [14] J. P. Buhler, H. W. Lenstra Jr., and C. Pomerance. Factoring integers with the number field sieve. In _The Development of the Number Field Sieve_ , volume 1554 of _Lecture Notes in Mathematics (LNM)_ , pages 50–94. Springer, 1993. DOI: 10.1007/BFb0091539. 

- [15] E. Campbell, A. Khurana, and A. Montanaro. Applying quantum algorithms to constraint satisfaction problems. _Quantum_ , 3:167, 2019. DOI: 10.22331/q-2019-07-18-167. arXiv:1810.05582. 

- [16] R. Cleve and J. Watrous. Fast parallel circuits for the quantum Fourier transform. In _Proceedings 41st Annual Symposium on Foundations of Computer Science_ , pages 526–536. IEEE, 2000. DOI: 10.1109/SFCS.2000.892140. 

- [17] D. Copsey, M. Oskin, F. Impens, T. Metodiev, A. Cross, F. T. Chong, I. L. Chuang, and J. Kubiatowicz. Toward a scalable, silicon-based quantum computing architecture. _IEEE Journal of Selected Topics in Quantum Electronics_ , 9(6):1552–1569, 2003. DOI: 10.1109/JSTQE.2003.820922. 

- [18] S. A. Cuccaro, T. G. Draper, S. A. Kutin, and D. P. Moulton. A new quantum ripple-carry addition circuit. _arXiv preprint quant-ph/0410184_ , 2004. URL `https://arxiv.org/abs/ quant-ph/0410184` . 

- [19] W. Diffie and M. E. Hellman. New Directions in Cryptography. _IEEE Transactions on Information Theory_ , IT-22(6):644–654, 1976. DOI: 10.1109/TIT.1976.1055638. 

- [20] T. G. Draper, S. A. Kutin, E. M. Rains, and K. M. Svore. A logarithmic-depth quantum carry-lookahead adder. _Quantum Information & Computation_ , 6(4–5):351–369, 2006. DOI: 10.26421/QIC6.4-5-4. arXiv:quant-ph/0406142. 

- [21] M. Eker˚a. Modifying Shor’s algorithm to compute short discrete logarithms. _Cryptology ePrint Archive, Report 2016/1128_ , 2016. URL `https://eprint.iacr.org/2016/1128` . 

- [22] M. Eker˚a. Revisiting Shor’s quantum algorithm for computing general discrete logarithms. _arXiv preprint arXiv:1905.09084_ , 2019. URL `https://arxiv.org/abs/1905.09084` . 

- [23] M. Eker˚a. On post-processing in the quantum algorithm for computing short discrete logarithms. _Designs, Codes and Cryptography_ , 88(11):2313–2335, 2020. DOI: 10.1007/s10623-02000783-2. iacr:2017/1122. 

- [24] M. Eker˚a. Quantum algorithms for computing general discrete logarithms and orders with tradeoffs. _Journal of Mathematical Cryptology_ , 15(1):359–407, 2021. DOI: 10.1515/jmc-20200006. (To appear.) iacr:2018/797. 

- [25] M. Eker˚a and J. H˚astad. Quantum Algorithms for Computing Short Discrete Logarithms and Factoring RSA Integers. In _Post-Quantum Cryptography_ , volume 10346 of _Lecture Notes in Computer Science (LNCS)_ , pages 347–363. Springer, 2017. DOI: 10.1007/978-3-319-598796˙20. 

- [26] A. G. Fowler. Time-optimal quantum computation. _arXiv preprint arXiv:1210.4626_ , 2012. URL `https://arxiv.org/abs/1210.4626` . 

- [27] A. G. Fowler and C. Gidney. Low overhead quantum computation using lattice surgery. _arXiv preprint arXiv:1808.06709_ , 2018. URL `https://arxiv.org/abs/1808.06709` . 

- [28] A. G. Fowler, M. Mariantoni, J. M. Martinis, and A. N. Cleland. Surface codes: Towards practical large-scale quantum computation. _Physical Review A_ , 86(3):032324, 2012. DOI: 10.1103/PhysRevA.86.032324. arXiv:1208.0928. 

- [29] A. G. Fowler, S. J. Devitt, and C. Jones. Surface code implementation of block code state distillation. _Scientific Reports_ , 3:1939, 2013. DOI: 10.1038/srep01939. arXiv:1301.7107. 

- [30] V. Gheorghiu and M. Mosca. Benchmarking the quantum cryptanalysis of symmetric, publickey and hash-based cryptographic schemes. _arXiv preprint arXiv:1902.02332_ , 2019. URL `https://arxiv.org/abs/1902.02332` . 

- [31] C. Gidney. Factoring with _n_ + 2 clean qubits and _n −_ 1 dirty qubits. _arXiv preprint arXiv:1706.07884_ , 2017. URL `https://arxiv.org/abs/1706.07884` . 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

24 

- [32] C. Gidney. Halving the cost of quantum addition. _Quantum_ , 2:74, 2018. DOI: 10.22331/q2018-06-18-74. arXiv:1709.06648. 

- [33] C. Gidney. Approximate encoded permutations and piecewise quantum adders. _arXiv preprint arXiv:1905.08488_ , 2019. URL `https://arxiv.org/abs/1905.08488` . 

- [34] C. Gidney. Asymptotically Efficient Quantum Karatsuba Multiplication. _arXiv preprint arXiv:1904.07356_ , 2019. URL `https://arxiv.org/abs/1904.07356` . 

- [35] C. Gidney. Windowed quantum arithmetic. _arXiv preprint arXiv:1905.07682_ , 2019. URL `https://arxiv.org/abs/1905.07682` . 

- [36] C. Gidney and A. G. Fowler. Efficient magic state factories with a catalyzed _|_ CCZ _⟩_ to 2 _|_ T _⟩_ transformation. _Quantum_ , 3:135, 2019. DOI: 10.22331/q-2019-04-30-135. arXiv:1812.01238. 

- [37] C. Gidney and A. G. Fowler. Flexible layout of surface code computations using AutoCCZ states. _arXiv preprint arXiv:1905.08916_ , 2019. URL `https://arxiv.org/abs/1905.08916` . 

- [38] D. Gillmor. RFC 7919: Negotiated Finite Field Diffie-Hellman Ephemeral Parameters for Transport Layer Security (TLS), August 2016. DOI: 10.17487/RFC7919. 

- [39] D. M. Gordon. Discrete logarithms in GF( _p_ ) using the Number Field Sieve. _SIAM Journal on Discrete Mathematics_ , 6(1):124–138, 1993. DOI: 10.1137/0406010. 

- [40] R. B. Griffiths and C.-S. Niu. Semiclassical Fourier Transform for Quantum Computation. _Physical Review Letters_ , 76(17):3228–3231, April 1996. DOI: 10.1103/PhysRevLett.76.3228. arXiv:quant-ph/9511007. 

- [41] J. Haah and M. B. Hastings. Codes and Protocols for Distilling _T_ , controlled- _S_ , and Toffoli Gates. _Quantum_ , 2:71, 2018. DOI: 10.22331/q-2018-06-07-71. arXiv:1709.02832. 

- [42] T. H¨aner, M. Roetteler, and K. M. Svore. Factoring using 2 _n_ + 2 qubits with Toffoli based modular multiplication. _Quantum Information & Computation_ , 17(7–8):673–684, 2017. DOI: 10.26421/QIC17.7-8-7. arXiv:1611.07995. 

- [43] M. B. Hastings and A. Geller. Reduced Space-Time and Time Costs Using Dislocation Codes and Arbitrary Ancillas. _Quantum Information & Computation_ , 15(11–12):962–986, 2015. DOI: 10.26421/QIC15.11-12-6. arXiv:1408.3379. 

- [44] C. Horsman, A. G. Fowler, S. Devitt, and R. Van Meter. Surface code quantum computing by lattice surgery. _New Journal of Physics_ , 14(12):123011, 2012. DOI: 10.1088/13672630/14/12/123011. arXiv:1111.4022. 

- [45] L. Jiang, J. M. Taylor, A. S. Sørensen, and M. D. Lukin. Scalable quantum networks based on few-qubit registers. _International Journal of Quantum Information_ , 8(01n02):93–104, 2010. DOI: 10.1142/S0219749910006058. 

- [46] N. C. Jones, R. Van Meter, A. G. Fowler, P. L. McMahon, J. Kim, T. D. Ladd, and Y. Yamamoto. Layered Architecture for Quantum Computing. _Physical Review X_ , 2(3):031007, 2012. DOI: 10.1103/PhysRevX.2.031007. arXiv:1010.5022. 

- [47] A. A. Karatsuba and Y. P. Ofman. Multiplication of many-digital numbers by automatic computers. _Doklady Akademii Nauk SSSR_ , 145(2):293–294, 1962. URL `http://mi.mathnet. ru/eng/dan/v145/i2/p293` . 

- [48] Y. Kim, R. Daly, J. Kim, C. Fallin, J. H. Lee, D. Lee, C. Wilkerson, K. Lai, and O. Mutlu. Flipping bits in memory without accessing them: An experimental study of DRAM disturbance errors. In _2014 ACM/IEEE 41st International Symposium on Computer Architecture (ISCA)_ , pages 361–372. IEEE, 2014. DOI: 10.1109/ISCA.2014.6853210. 

- [49] T. Kivinen and M. Kojo. RFC 3526: More Modular Exponentiation (MODP) Diffie-Hellman groups for Internet Key Exchange (IKE), May 2003. DOI: 10.17487/RFC3526. 

- [50] T. Kleinjung, K. Aoki, J. Franke, A. K. Lenstra, E. Thom´e, J. W. Bos, P. Gaudry, A. Kruppa, P. L. Montgomery, D. A. Osvik, t. R. Herman, A. Timofeev, and P. Zimmermann. Factorization of a 768-Bit RSA Modulus. In _Advances in Cryptology – CRYPTO 2010_ , volume 6223 of _Lecture Notes in Computer Science (LNCS)_ , pages 333–350. Springer, 2010. DOI: 10.1007/978-3-642-14623-7˙18. 

- [51] S. A. Kutin. Shor’s algorithm on a nearest-neighbor machine. _arXiv preprint quantph/0609001_ , 2006. URL `https://arxiv.org/abs/quant-ph/0609001` . 

- [52] A. K. Lenstra. Key Lengths. In _The Handbook of Information Security_ , chapter 6. 2004. URL `https://infoscience.epfl.ch/record/164539/files/NPDF-32.pdf` . 

- [53] A. K. Lenstra and H. W. Lenstra Jr., editors. _The Development of the Number Field Sieve_ , volume 1554 of _Lecture Notes in Mathematics (LNM)_ . Springer, 1993. DOI: 10.1007/BFb0091534. 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

25 

- [54] A. K. Lenstra and E. R. Verheul. Selecting Cryptographic Key Sizes. _Journal of Cryptology_ , 14:225–293, 2001. DOI: 10.1007/s00145-001-0009-4. 

- [55] A. K. Lenstra, H. W. Lenstra Jr., M. S. Manasse, and J. M. Pollard. The number field sieve. In _Proceedings of the Twenty-Second Annual ACM Symposium on Theory of Computing_ , pages 564–572. ACM, 1990. DOI: 10.1145/100216.100295. 

- [56] D. Litinski. Magic State Distillation: Not as Costly as You Think. _Quantum_ , 3:205, 2019. DOI: 10.22331/q-2019-12-02-205. arXiv:1905.06903. 

- [57] M. Mosca. Cybersecurity in an Era with Quantum Computers: Will We Be Ready? _IEEE Security & Privacy_ , 16(5):38–41, 2018. DOI: 10.1109/MSP.2018.3761723. iacr:2015/1075. 

- [58] M. Mosca and A. Ekert. The Hidden Subgroup Problem and Eigenvalue Estimation on a Quantum Computer. In _Quantum Computing and Quantum Communications_ , volume 1509 of _Lecture Notes in Computer Science (LNCS)_ , pages 174–188. Springer, 1999. DOI: 10.1007/3540-49208-9˙15. 

- [59] NIST. Digital Signature Standard (DSS). Technical Report Federal Information Processing Standards Publications (FIPS PUBS) 186-4, July 2013. DOI: 10.6028/NIST.FIPS.186-4. 

- [60] NIST and CCCS. Implementation Guidance for FIPS 140-2 and the Cryptographic Module Validation Program. Technical report, May 2019. URL `https: //csrc.nist.gov/csrc/media/projects/cryptographic-module-validation-program/ documents/fips140-2/fips1402ig.pdf` . Accessed: 2019-05-10, Document Revision: 2019-05-07. 

- [61] J. O’Gorman and E. T. Campbell. Quantum computation with realistic magic-state factories. _Physical Review A_ , 95(3):032338, 2017. DOI: 10.1103/PhysRevA.95.032338. arXiv:1605.07197. 

- [62] D. K. L. Oi, S. J. Devitt, and L. C. L. Hollenberg. Scalable error correction in distributed ion trap computers. _Physical Review A_ , 74(5):052313, 2006. DOI: 10.1103/PhysRevA.74.052313. arXiv:quant-ph/0606226. 

- [63] OpenSSL Software Foundation. OpenSSL source code: Line 32 of `apps/dhparam.c` . `https: //github.com/openssl/openssl/blob/07f434441e7ea385f975e8df8caa03e62222ca61/ apps/dhparam.c#L32` , 2018. URL `https://github.com/openssl/openssl/blob/ 07f434441e7ea385f975e8df8caa03e62222ca61/apps/dhparam.c#L32` . Accessed: 201812-11. 

- [64] M. Oskin, F. T. Chong, and I. L. Chuang. A practical architecture for reliable quantum computers. _Computer_ , 35(1):79–87, 2002. DOI: 10.1109/2.976922. 

- [65] A. Parent, M. Roetteler, and M. Mosca. Improved reversible and quantum circuits for Karatsuba-based integer multiplication. In _12th Conference on the Theory of Quantum Computation, Communication and Cryptography (TQC 2017)_ , volume 73 of _Leibniz International Proceedings in Informatics (LIPIcs)_ , pages 7:1–7:15. Schloss Dagstuhl – Leibniz-Zentrum f¨ur Informatik, 2018. DOI: 10.4230/LIPIcs.TQC.2017.7. arXiv:1706.03419. 

- [66] S. Parker and M. B. Plenio. Efficient Factorization with a Single Pure Qubit and log _N_ Mixed Qubits. _Physical Review Letters_ , 85(14):3049, October 2000. DOI: 10.1103/PhysRevLett.85.3049. arXiv:quant-ph/0001066. 

- [67] A. Pavlidis and D. Gizopoulos. Fast quantum modular exponentiation architecture for Shor’s factorization algorithm. _Quantum Information & Computation_ , 14(7–8):649–682, 2014. DOI: 10.26421/QIC14.7-8-8. arXiv:1207.0511. 

- [68] S. C. Pohlig and M. E. Hellman. An Improved Algorithm for Computing Logarithms over GF( _p_ ) and Its Cryptographic Significance. _IEEE Transactions on Information Theory_ , IT-24 (1):106–110, 1978. DOI: 10.1109/TIT.1978.1055817. 

- [69] J. M. Pollard. Monte Carlo Methods for Index Computation (mod _p_ ). _Mathematics of Computation_ , 32(143):918–924, 1978. DOI: 10.1090/s0025-5718-1978-0491431-9. 

- [70] J. M. Pollard. Factoring with cubic integers. In _The Development of the Number Field Sieve_ , volume 1554 of _Lecture Notes in Mathematics (LNM)_ , pages 4–10. Springer, 1993. DOI: 10.1007/BFb0091536. 

- [71] J. M. Pollard. The lattice sieve. In _The Development of the Number Field Sieve_ , volume 1554 of _Lecture Notes in Mathematics (LNM)_ , pages 43–49. Springer, 1993. DOI: 10.1007/BFb0091538. 

- [72] C. Pomerance. A Tale of Two Sieves. _Notices of the AMS_ , 43(12):1473–1485, 1996. URL `https://www.ams.org/notices/199612/pomerance.pdf` . 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

26 

- [73] R. L. Rivest, A. Shamir, and L. Adleman. A Method for Obtaining Digital Signatures and Public-Key Cryptosystems. _Communications of the ACM_ , 21(2):120–126, 1978. DOI: 10.1145/359340.359342. 

- [74] M. Roetteler, M. Naehrig, K. M. Svore, and K. Lauter. Quantum Resource Estimates for Computing Elliptic Curve Discrete Logarithms. In _Advances in Cryptology – ASIACRYPT 2017_ , volume 10625 of _Lecture Notes in Computer Science (LNCS)_ , pages 241–270. Springer, 2017. DOI: 10.1007/978-3-319-70697-9˙9. 

- [75] O. Schirokauer. _On pro-finite groups and on discrete logarithms_ . PhD thesis, University of California, Berkeley, May 1992. 

- [76] O. Schirokauer. Discrete Logarithms and Local Units. _Philosophical Transactions of the Royal Society of London A_ , 345(1676):409–423, 1993. DOI: 10.1098/rsta.1993.0139. 

- [77] A. Sch¨onhage and V. Strassen. Schnelle Multiplikation großer Zahlen. _Computing_ , 7(3–4): 281–292, 1971. DOI: 10.1007/BF02242355. 

- [78] B. Schroeder, E. Pinheiro, and W.-D. Weber. DRAM Errors in the Wild: A Large-Scale Field Study. _SIGMETRICS Performance Evaluation Review_ , 37(1):193–204, 2009. DOI: 10.1145/1555349.1555372. 

- [79] P. W. Shor. Algorithms for Quantum Computation: Discrete Logarithms and Factoring. In _Proceedings 35th Annual Symposium on Foundations of Computer Science_ , pages 124–134. IEEE, 1994. DOI: 10.1109/SFCS.1994.365700. 

- [80] The GnuPG Project. GnuPG Frequently Asked Questions: Why does GnuPG default to 2048 bit RSA-2048? `https://www.gnupg.org/faq/gnupg-faq.html#default_rsa2048` , 2018. URL `https://www.gnupg.org/faq/gnupg-faq.html#default_rsa2048` . Accessed: 2018-1211. 

- [81] The OpenSSH Project. Linux Documentation: Man Page for `ssh-keygen(1)` . `https://linux.die.net/man/1/ssh-keygen` , 2018. URL `https://linux.die.net/man/1/ ssh-keygen` . Accessed: 2018-12-11. 

- [82] R. Van Meter. A #QuantumComputerArchitecture Tweetstorm, 2019. DOI: 10.5281/zenodo.3496597. 

- [83] R. Van Meter and K. M. Itoh. Fast quantum modular exponentiation. _Physical Review A_ , 71 (5):052320, 2005. DOI: 10.1103/PhysRevA.71.052320. arXiv:quant-ph/0408006. 

- [84] R. Van Meter, W. J. Munro, K. Nemoto, and K. M. Itoh. Arithmetic on a distributedmemory quantum multicomputer. _ACM Journal on Emerging Technologies in Computing Systems (JETC)_ , 3(4):1–23, 2008. DOI: 10.1145/1324177.1324179. 

- [85] R. Van Meter, T. D. Ladd, A. G. Fowler, and Y. Yamamoto. Distributed quantum computation architecture using semiconductor nanophotonics. _International Journal of Quantum Information_ , 8(01n02):295–323, 2010. DOI: 10.1142/S0219749910006435. arXiv:0906.2686. 

- [86] P. C. van Oorschot and M. J. Wiener. On Diffie-Hellman Key Agreement with Short Exponents. In _Advances in Cryptology – EUROCRYPT ’96_ , volume 1070 of _Lecture Notes in Computer Science (LNCS)_ , pages 332–343. Springer, 1996. DOI: 10.1007/3-540-68339-9˙29. 

- [87] V. Vedral, A. Barenco, and A. Ekert. Quantum networks for elementary arithmetic operations. _Physical Review A_ , 54(1):147–153, 1996. DOI: 10.1103/PhysRevA.54.147. arXiv:quantph/9511018. 

- [88] M. G. Whitney, N. Isailovic, Y. Patel, and J. Kubiatowicz. A fault tolerant, area efficient architecture for Shor’s factoring algorithm. In _Proceedings of the 36th Annual International Symposium on Computer Architecture_ , pages 383–394. ACM, 2009. DOI: 10.1145/1555754.1555802. 

- [89] Wikipedia. Timeline of quantum computing. `https://en.wikipedia.org/wiki/Timeline_ of_quantum_computing` , 2018. URL `https://en.wikipedia.org/wiki/Timeline_of_ quantum_computing` . Accessed: 2018-12-18. 

- [90] C. Zalka. Fast versions of Shor’s quantum factoring algorithm. _arXiv preprint quantph/9806084_ , 1998. URL `https://arxiv.org/abs/quant-ph/9806084` . 

- [91] C. Zalka. Shor’s algorithm with fewer (pure) qubits. _arXiv preprint quant-ph/0601097_ , 2006. URL `https://arxiv.org/abs/quant-ph/0601097` . 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

27 

## A Notes on Table 1 

### A.1 Columns 

- **Abstract Qubits** : The number of logical qubits used in the abstract circuit model. Ignores qubits used for distillation and routing. 

- **Measurement Depth** : The length of the longest chain of dependent measurements, which determines the reaction limited runtime of an algorithm. These numbers are not adjusted to account for the chance of retrying. 

- **Toffoli+T/2** : Number of magic states required by the algorithm. The “/2” adjustment is intended to account for the fact that T states take less volume to distill than Toffoli states. These numbers are not adjusted to account for the chance of retrying. 

- **Min volume** : Expected spacetime cost of the computation, including retries. The papers included in the table span decades, and a range of assumptions about the architecture of quantum computers, and generally do not provide spacetime volumes. To assign volumes to these papers, we plugged their asymptotic formulas into various possible realizations of that algorithm (serial, parallel, and intermediate) using ancillary file “fill-in-table.py”. Each volume entry is the minimum volume achieved by the different possible realizations. We assumed all papers but our own had a negligible retry chance. 

### A.2 Entries 

Some entries in the table are directly from a paper, others had to be inferred by hand, and others were filled in using the output of the ancillary file “fill-in-table.py”. Here is where each entry in the table came from: 

- Vedral et al. 1996 [87]: 

   - Toffoli+T/2 Count: 80 _n_<sup>3</sup> derived from figures at end of the paper. 

   - Abstract Qubits: Paper says 7 _n_ + 1 (end of section IV). Verified using figures at end of paper. Paper mentions this can be improved to 4 _n_ +3, but the described method would radically increase the Toffoli count. 

   - Measurement Depth: Equal to the Toffoli count. The circuit construction is serial. 

   - Numbers at specific _n_ : from “fill-in-table.py”. 

- Zalka 1998 (basic) [90]: 

   - Toffoli+T/2 Count: Paper says 12 _n_<sup>3</sup> (title of section 1.4.1). 

   - Abstract Qubits: Paper says 3 _n_ (title of section 1.4.1). 

   - Measurement Depth: Equal to the Toffoli count. The circuit construction is serial. 

   - Numbers at specific _n_ : from “fill-in-table.py”. 

- Zalka 1998 (log add) [90]: 

   - Toffoli+T/2 Count: Paper says 52 _n_<sup>3</sup> (section 5, bottom of page 18). 

   - Abstract Qubits: Paper says 5 _n_ (section 5, bottom of page 18). 

   - Measurement Depth: Paper says 600 _n_<sup>2</sup> (section 5, top of page 19). 

   - Numbers at specific _n_ : from “fill-in-table.py”. 

- Zalka 1998 (fft mult) [90]: 

   - Toffoli+T/2 Count: Paper says 2<sup>17</sup> _n_<sup>2</sup> (section 5, middle of page 19). 

   - Abstract Qubits: Paper says 96 _n_ (section 5, middle of page 19). 

   - Measurement Depth: Paper says 2<sup>17</sup> _n_<sup>1</sup><sup>_._2</sup> (section 5, middle of page 19). 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

28 

   - Numbers at specific _n_ : from “fill-in-table.py”. 

- Beauregard 2002 [6]: 

   - Toffoli+T/2 Count: Derived from figures in the paper. Our estimate has an additional factor of lg _n_ to account for the need to approximate arbitrary phase rotations using T states. 

   - Abstract Qubits: Stated in the title of the paper. 

   - Measurement Depth: Derived from figures in the paper. Our estimate has an additional factor of lg _n_ to account for the need to approximate arbitrary phase rotations using T states. 

   - Numbers at specific _n_ : from “fill-in-table.py”. 

- Fowler et al. 2012 [28]: 

   - Toffoli+T/2 Count: From table I in the paper. 

   - Abstract Qubits: The paper erroneously claims 2 _n_ in table I due to overlooking a necessary workspace register. We corrected this to 3 _n_ + _O_ (1). 

   - Measurement Depth: From table I in the paper. 

   - Numbers at specific _n_ : from “fill-in-table.py”. 

- H¨aner et al. 2016 [42]: 

   - Toffoli+T/2 Count: From table 2 of [74]. 

   - Abstract Qubits: From paper’s title. 

   - Measurement Depth: Derived 52 _n_<sup>3</sup> from the circuit diagrams included in the paper. 

   - Numbers at specific _n_ : from “fill-in-table.py”. 

- (ours) 2019: Asymptotic bounds explained in Section 2. Concrete numbers at specific sizes come from ancillary file “estimate ~~c~~ osts.py”. The Toffoli count does not account for the chance of retrying (because it is mostly insensitive to changes that lower this chance), but the volume does account for it (i.e. it is the expected total volume to factor, not the per-run volume). 

- Roetteler et al. 2017 [74]: 

   - Toffoli+T/2 Count (asymptotic): From the paper’s abstract. 

   - Abstract Qubits: From the paper’s abstract. 

   - Measurement Depth: Assumed same as Toffoli count. 

   - Toffoli+T/2 Count (at _n_ = 224): From Table 2. 

   - Numbers at specific _n_ : from “fill-in-table.py”. 

Note that an _n_ bit prime order elliptic curve group provides approximately _n/_ 2 bits of classical security (see Appendix D to [4]), since the best classical attacks are cycle-finding attacks, whilst RSA-1024, RSA-2048 and RSA-3072 provide approximately 80, 112 and 128 bits of classical security, respectively, according to the model used by NIST (see Appendix D to [5]). There are several other models [9, 52, 54]. The table compares problem instances that provide the same level of classical security according to the NIST model. 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

29 

## B Notes on Table 2 

### B.1 Columns 

- **Physical gate error rate** : The probability that executing a physical gate will introduce Pauli errors onto targeted qubits. 

- **Cycle time** : The amount of time it takes to measure all of the surface code’s stabilizers once. 

- **Reaction time** : The amount of time it takes the classical control system to trigger a logical measurement, collect and error-correct the result, and decide on which measurement basis to use for the next set of measurements. 

- **Physical connectivity** : Which physical qubits can interact with each other. Planar means only adjacent qubits on a planar grid can interact (typical of superconducting qubits). Arbitrary means qubits can interact with other qubits as needed by the construction (typical of ion traps). 

- **Distillation strategy** : The dominant kind of magic states being distilled, and the number or type of factory being used to distill them. 

- **Execution strategy** : Notes on how the computation progresses at a low level. Each construction spends most of its time performing additions, so this column ended up describing addition strategies. The suffixes “carry lookahead”, “ripple carry”, and “carry runways” describe the type of adder being used. The prefixes “distillation limited” and “reaction limited” describe what is preventing the adder from running faster. Distillation limited means that the adder is bottlenecked on magic states being produced. Reaction limited means that the adder is bottlenecked on the control system resolving long chains of dependent measurement bases. 

- **Physical qubits** : The number of physical qubits used by the computation, using the original historical assumptions. 

- **Expected runtime** : The average amount of time before the computation has completed successfully, using the original historical assumptions. 

- **Expected volume** : The average number of physical qubit-rounds before the computation has completed successfully, using the original historical assumptions. 

### B.2 Entries 

- Van Meter et al. 2009 [85]: Numbers are derived from Table 2 of [85]. The paper does not use reaction limited computation, so the reaction time is not included. 

- Jones et al. 2009 [46]: Numbers are derived from Figure 15, Table II, and Table VII of [46]. The paper does not use reaction limited computation, so the reaction time is not included. 

- Fowler et al. 2012 [28]: Numbers are from the background section of [28]. This paper’s expected volume is directly comparable to ours, despite the different reaction time assumption, because their volume estimate is dominated by distillation and changing the reaction time does not distillation volume. 

- O’Gorman et al. (2017) [61]: Numbers are derived from table I of [61]. The physical qubit count of 2 _._ 18 _·_ 10<sup>8</sup> from their table only includes distillation; we increased it by 3 _·_ 2048 _·_ (2 _·_ 32<sup>2</sup> ) _≈_ 0 _._ 13 _·_ 10<sup>8</sup> to account for three _n_ -logical-qubit data registers. 

- Gheorghiu et al. (2019) [30] The physical gate error rate, qubit count, and time are stated in the caption of fig 45 (“B. RSA-2048”) of the paper. The surface code cycle time is stated to be 200 nanoseconds in Section B, soon after equation 3. The T factory count was inferred by dividing the stated T count of 2 _._ 4 _·_ 10<sup>12</sup> by the production rate of the T factory from [27], which is approximately 25kHz for the given surface code cycle time. The paper does not 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

30 

state a reaction time, but the T states are being used to perform chains of dependent Toffolis. This implies the reaction time must be faster than the number factories times the per-factory production rate divided by 4 (the number of Ts needed to perform a Toffoli). So a 0.2 microsecond reaction time would not be sufficient, but a 0.1 microsecond reaction time would be, and so we state the reaction time as 0.1 microseconds. 

- Ours (2019): The parallel entry is the implementation described in Section 2 and produced by ancillary file “estimates ~~c~~ osts.py”. The single threaded and serial distillation entries use the same basic architecture, but with fewer factories and without piecewise additions or double-speed lookups. 

Accepted in Quantum 2021-03-29, click title to verify. Published under CC-BY 4.0. 

31 

