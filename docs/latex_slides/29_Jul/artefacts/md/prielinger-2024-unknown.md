# **Surrogate-guided optimization in quantum networks** 

## **Luise Prielinger**<sup>1,2,*</sup> **, Alvaro G. I˜nesta**<sup>**´**1,2</sup> **, and Gayane Vardoyan**<sup>1,2,3</sup> 

1QuTech, Delft University of Technolgy, Delft, The Netherlands. 

2EEMCS, Delft University of Technology, Delft, The Netherlands. 

3CICS, University of Massachusetts, Amherst, USA. 

*l.p.prielinger@tudelft.nl 

## **ABSTRACT** 

We propose an optimization algorithm to improve the design and performance of quantum communication networks. When physical architectures become too complex for analytical methods, numerical simulation becomes essential to study quantum network behavior. Although highly informative, these simulations involve complex numerical functions without known analytical forms, making traditional optimization techniques that assume continuity, differentiability, or convexity inapplicable. Additionally, quantum network simulations are computationally demanding, rendering global approaches like Simulated Annealing or genetic algorithms, which require extensive function evaluations, impractical. We introduce a more efficient optimization workflow using machine learning models, which serve as surrogates for a given objective function. We demonstrate the effectiveness of our approach by applying it to three well-known optimization problems in quantum networking: quantum memory allocation for multiple network nodes, tuning an experimental parameter in all physical links of a quantum entanglement switch, and finding efficient protocol settings within a large asymmetric quantum network. The solutions found by our algorithm consistently outperform those obtained with our baseline approaches – Simulated Annealing and Bayesian optimization – in the allotted time limit by up to 18% and 20%, respectively. Our framework thus allows for more comprehensive quantum network studies, integrating surrogate-assisted optimization with existing quantum network simulators. 

## **Introduction** 

Quantum network infrastructure has the potential to be integrated with today’s Internet, serving entangled states to users who request them<sup>1</sup> . These networks will enable a number of applications provably beyond the capabilities of classical technologies alone. Examples include verifiably secure communication<sup>2,3</sup> , advanced sensing tasks<sup>4,5</sup> and blind quantum computation<sup>6,7</sup> , among others. For quantum networks to achieve their intended potential, diverse solutions for all layers of the system stack have been put forward in recent years. At the physical layer, for example, so-called quantum repeaters have been proposed to assist with quantum information transport over long distances (see e.g., ref.<sup>8</sup> for an in-depth review on quantum repeaters). The primary task at the software layer is to create efficient protocols that coordinate and control the intricate physical processes within the quantum network system stack<sup>9</sup> . To this end, both software and hardware components have been extensively studied<sup>10–19</sup> using analytical tools as well as numerical simulation to find feasible architectures and bring quantum network technology a step closer to the real world. These efforts include the use of optimization and machine learning techniques, which have been used, for example, to design new entanglement distribution protocols<sup>20–22</sup> . While these studies are greatly informative, they generally assess only small-sized networks or operate under simplified assumptions, such as ideal hardware models or highly symmetric network typologies. 

In this study, our primary goal is to utilize a surrogate-assisted optimization workflow to discover effective protocol and hardware parameter values under realistic conditions. To this end, we extend previous efforts and integrate comprehensive numerical simulators, such as NetSquid<sup>23</sup> and SeQUeNCe<sup>24</sup> in our optimization framework. In essence, a surrogate model<sup>25,26</sup> is an approximation of a given objective function, which is built using data obtained from evaluations of the actual objective function. Importantly, instead of directly optimizing the computationally expensive objective function – a common approach in global optimization techniques such as Simulated Annealing or genetic algorithms (see ref.<sup>27</sup> for a review of numerical optimization methods) – we employ a surrogate model to guide the iterative optimization process. 

Common surrogate models like Gaussian processes<sup>28</sup> (used in Bayesian optimization) and neural networks<sup>29</sup> are based on complex theoretical frameworks. Gaussian processes, for example, depend significantly on the choice of a kernel function and they are known to be most effective in smaller, continuous search spaces with fewer than 20 variables<sup>30</sup> . Neural networks, which consist of various specialized layers<sup>31</sup> , require substantial data for 

optimal performance. Additionally, the outputs from these complex models are often more difficult to interpret compared to those from simpler models<sup>32</sup> . As a consequence, we opted for two well-known but less complex models – Support Vector Regression<sup>33</sup> (SVR) and Random Forest Regression<sup>34</sup> (RF) – due to their explainability, computational efficiency, and straightforward evaluation. Surrogate models have been utilized since the late 80s and ever since applied to various scientific domains, such as chemical engineering<sup>35,36</sup> and materials science<sup>37</sup> . In quantum sensing, Bayesian optimization has been utilized for quantum detectors<sup>38</sup> and in quantum networking to find minimum hardware requirements<sup>39</sup> in small repeater chains and to calibrate experimental parameters<sup>40</sup> . To the best of our knowledge, surrogates have not yet been applied to any software component of quantum communication. 

In this work we introduce a surrogate-optimization framework and apply it to three quantum network use cases simulated in NetSquid<sup>23</sup> , SeQUeNCe<sup>24</sup> and OptimizingCD<sup>41</sup> , respectively. Our contributions are as follows: 

- **Optimization algorithm integrating scientific software:** Our framework utilizes detailed simulations of practical quantum network scenarios. This method allows us to avoid reliance on purely theoretical predictions, which are often specific to certain architectural or software stack characteristics like node connectivity or expected protocol behavior<sup>13,20,24,42</sup> . Furthermore, whereas traditional techniques might need hundreds or even thousands of optimization cycles<sup>18,43</sup> , our approach shows substantial improvements within less than a hundred cycles. This efficiency allows us to integrate computationally intensive simulations – which can take several minutes to execute – into our optimization process. 

- **Handling of many parameters:** The scenarios we test encompass up to 100 network parameters. For the largest variable set, reference methods perform comparably to random search, whereas our approach significantly outperforms both. This capability is largely due to the simplicity of the SVR and RF models utilized, which exhibit only linear time complexity with the number of variables<sup>44</sup> . 

- **Addressing multiple objectives:** In a quantum network where different parties might have their individual quality-of-service goals, our analysis allows us to determine an empirical estimate of the Pareto frontier. Using this solution set, we can assess the effectiveness of parameter settings in the context of multi-objective optimization. 

- **Diverse applicability:** The selected use cases present well-known optimization challenges of distributing entangled states in quantum networks. The solutions we find introduce competitive candidates to existing solutions found in literature. Furthermore, we test the applicability of our approach on a range of different entanglement distribution protocols, involving on-demand and continuous-distribution protocols<sup>41,45</sup> . 

We compare our approach to a Bayesian optimizer developed by Meta<sup>46</sup> , a traditional global optimization algorithm termed Simulated Annealing<sup>47</sup> , and uniform random search as baselines. In the scenarios we investigate, surrogate optimization consistently outperforms the selected reference methods by up to 20% within the allotted time limits. 

In the following sections, we first introduce our surrogate-guided search for quantum network configurations, including the necessary preliminaries in Section 1. In Section 2 we demonstrate the usability of our approach in various quantum network setups and detail its relation to previous work in Section 3. Finally, Section 4 describes our simulation experiments and the optimization methods used for comparison. 

## **1 Results** 

### **1.1 Preliminaries** 

Consider a vector function _f_ ( **x** ) : _X →_ R<sup>_m f_</sup> of arbitrary size _m f ∈_ N describing a performance metric of a quantum network (e.g., the average fidelity of entangled states provided to a pair of nodes). The input to this function **x** = _{x_ 1 _, x_ 2 _,..., xN}_ represents a set of quantum network parameter values, which may include both fixed (nonconfigurable) as well as tunable features. A parameter _xp_ of a network configuration **x** is defined on a domain _Xp_ . Together, the parameter domains form the input space: _X_ = _X_ 1 _× X_ 2 _×···× XN._ We do not restrict _xp_ to a specific datatype. For continuous and discrete values, _xp_ is confined within some minimum-maximum bounds, _x_<sup>min</sup> _p_ and _x_<sup>max</sup> _p_ , respectively, while ordinal and categorical parameters are represented as value sets. 

Based on _f_ , we can formulate an objective function _U_ ( _f ,_ **x** ) reflecting the way in which a quantum network perceives _utility_<sup>13</sup> . Essentially, while _f_ ( **x** ) describes some output of the network, the function _U_ ( _f ,_ **x** ) : R<sup>_mf_</sup> _× X →_ R<sup>_m_</sup> , _m ∈_ N, assesses how much utility can be derived from this output. Although _U_ can in principle represent any general objective, in our analyzed use cases, one element of _U_ , denoted _U_<sup>(</sup><sup>_i_)</sup> , consistently represents the utility perceived by a network user _i_ . We will explore some relevant examples of utility functions _U_ based on distillable entanglement<sup>48</sup> , request completions<sup>24</sup> , and virtual connectivity<sup>41</sup> . 

In a quantum network, many processes are inherently probabilistic. For example, creating entanglement between nodes often requires multiple attempts following a geometric distribution<sup>8</sup> . As a consequence, we assume _f_ and thus also the utility _U_ ( _f ,_ **x** ) to be _stochastic_ functions. We denote the utility perceived by user _i_ with a random variable _Y_<sup>(</sup><sup>_i_)</sup> _∼ U_<sup>(</sup><sup>_i_)</sup> ( _f ,_ **x** ) with expectation value _E_ [ _Y_<sup>(</sup><sup>_i_)</sup> ]. As _f_ ( **x** ) is evaluated via numerical simulation, we retrieve 

**2/20** 

a sample _{U_ 1<sup>(</sup><sup>_i_)(</sup><sup>_f,_</sup><sup>**x**)</sup><sup>_,U_</sup> 2<sup>(</sup><sup>_i_)(</sup><sup>_f,_</sup><sup>**x**)</sup><sup>_,...,U_</sup> _n_<sup>(</sup><sup>_i_)(</sup><sup>_f,_</sup><sup>**x**)</sup><sup>_}_via</sup><sup>_n_simulation runs to estimate the expected behaviour</sup><sup>_E_[</sup><sup>_Y_(</sup><sup>_i_)]</sup> for each user _i_ with the sample mean _U_<sup>¯(</sup><sup>_i_)</sup> ( _f ,_ **x** ) =<sup><u>1</u></sup> _n_<sup>∑</sup><sup>_n_</sup> _j_ =1<sup>_U_</sup> _j_<sup>(</sup><sup>_i_)(</sup><sup>_f,_</sup><sup>**x**).In this work, our optimization objective is to</sup> maximize the aggregate utility of the network, i.e., the sum of all individual user utilities. **Definition 1.1** (Utility maximization over configurable variables) **.** _We aim to maximize the aggregate utility over all users by configuring parameter values within the tunable portion of the domain X, X_ conf _⊆ X. This results in the objective_ max **s** _Uaggr_ ( _f ,_ **s** ) := ∑<sup>_m_</sup> _i_ =1<sup>_U_¯(</sup><sup>_i_)(</sup><sup>_f,_</sup><sup>**s**)</sup><sup>_, where_</sup><sup>**s**</sup><sup>_∈X_conf</sup><sup>_. Here, the set X \X_conf</sup><sup>_denotes all parameters which_</sup> _are fixed._ 

### **1.2 Surrogate-assisted Search** 

We present our optimization workflow depicted in Figure 1, which progresses through successive cycles _t ∈ {_ 0 _,..., T }_ . It begins by randomly generating _k_ 0 initial input sets _{_ **s** 1 _,_ **s** 2 _,...,_ **s** _k_ 0 _}_ from the search domain _X_ conf, where each set is a unique configuration of parameter values. Then, for each input set **s** _i_ , a quantum network simulation is run _n_ times to produce mean utility outputs [ _U_<sup>¯(1)</sup> ( _f ,_ **s** _i_ ) _, ··· ,U_<sup>¯(</sup><sup>_m_)</sup> ( _f ,_ **s** _i_ )]. Each of the _n_ runs lasts _T_ sim simulation time units. The input configurations together with the associated utility outputs form the initial _dataset_ , concluding the first cycle, _t_ = 0. At the beginning of the next cycle, _t_ = 1, the two machine learning models (SVR, RF) are evaluated using five-fold cross validation; thereby the models are trained on 80% of the dataset (the training set) and evaluated on the remaining data (the test set). Their performance is measured using the mean absolute error between predicted and actual values in the test set. For further details on the model training refer to Supplementary Notes 1 and 2. 

In the subsequent _acquisition process_ , the currently better performing machine learning model is used to select new configurations. To this end, _for each_ of _l_ so far best performing configurations _{_ **s**<sup>top</sup> 1<sup>_,...,_</sup><sup>**s**top</sup> _l_<sup>_}_,a</sup> promising neighbor is identified: first, a number of points near a configuration **s**<sup>top</sup> _i_ is sampled from truncated normal distributions centered around each parameter value in **s**<sup>top</sup> _i_<sup>.Formally, parameter values are sampled from</sup> _N_ trunc( _µp, σp_ ( _t, d_ )). These distributions have mean _µp_ = _xp_ , standard deviation _σp_ ( _t, d_ ) = _γ_ ( _t, d_ )( _x_<sup>max</sup> _p − x_<sup>min</sup> _p_<sup>)</sup><sup>_/_2,</sup> and are truncated at the bounds _x_<sup>min</sup> _p_ and _x_<sup>max</sup> _p_ (see Section 1.1). We gradually shift from exploration towards exploitation by progressively narrowing the standard deviation using a monotonically-decreasing transition function _γ_ ( _t, d_ ) depending on the elapsed cycles _t_ and an exploitation degree _d ≥_ 1. This adjustment ensures that as each cycle progresses, the focus on exploring unknown points in _X_ conf turns to exploiting known good areas of the search space (see Supplementary Notes 1 for further details on the exploitation strategy). Furthermore, the number of sampling points increases incrementally with each cycle _t_ . This approach allows for less costly computation during early cycles, when the models’ performance is lower, and progressively dedicating more time as the models improve and accumulate knowledge (see details in Supplementary Note 2). 

Once the points are passed to a model, it predicts utility values based on its current knowledge, and the configuration associated with the _highest_ utility is returned. This leads to _l_ new configurations _{_ **s**<sup>next</sup> 1 _,...,_ **s**<sup>next</sup> _l }_ to be evaluated by the simulation. Finally the newly generated parameter sets and associated simulation outputs are added to the dataset, _k_ 1 = _k_ 0 + _l_ , which completes the optimization cycle _t_ = 1. This cycle repeats until a time limit or maximum number of iterations, _t_ = _T_ is reached. By default, _k_ 0 and _l_ are chosen according to the number of compute resources available for parallel execution. Table 1 summarizes the parameters used. 

|Symbol|**Description**|
|---|---|
|_T_|Optimization limit, can be specifed as wall-clock time limit<br>or maximum number of optimization cycles|
|_t_|Elapsed time_t ∈_[0_,T_]or cycle_t ∈{_0_,...,T}_|
|_n_|Number of simulation evaluations used to compute <sup>¯</sup>_U_|
|_l_|Number of points explored in an optimization cycle|
|_d_|Exploitation degree (see Supplementary Note 1)|
|_kt_|Number of points in the dataset at cycle_t_, where_kt_+1=_kt_+_l_ and_k_0=_l_|
|_T_sim|Simulation time of thequantum network model(specifc to use case)|



**Table 1.** Parameters used in surrogate-assisted search. 

Every algorithm comes with its limitations: heuristic approaches, like the one described, do not guarantee a globally optimal solution but instead provide approximations once a termination criterion is met<sup>27</sup> . This criterion is primarily dictated by the available computational resources. For example, considering the computationally demanding nature of our simulation functions, we set the termination criterion to not exceed _T_ = 100 optimization cycles. Further, we must rely on seeds to guarantee reproducibility as both the simulation as well as the machine learning models used in the acquisition process are inherently stochastic. In addition, selecting settings for workflow parameters like the degree of exploitation _d_ is crucial and requires understanding their specific function (see 

**3/20** 



<!-- Start of picture text -->
oT —_— ~~) Acquisition Process<br>oo” ee Bem xd eiee] U- 0 ‘ x3 Draw samples<br>; s2 . a 1. BS | : from truncated<br>: : : ] | H ’ normal distribution<br>ES wre —<br>k different network configurations ~~ Simulation execution ~~ Outcome 2. Evaluate models ——=—=1 1<br>I |<br>3. Select most (8 _a)<br>promising ~~ ee me 20 )<br>mapiq 3co365 ee >@SVR 4 simulationmeow mmm- i [0 gO<br>I. : ] Random Forest<br>[ Bell State Measurement > “1<br>Ba eB ! i Model Training =oo =2a<br>| Switch [i 1] H<br>|| Gn)< Netsquid7) Dataset _— Po kelkel OX 2 XSaawe<br>|| A ®o 45’ currentSelect | <kconfigurations best Enriched dataset<br>Import quantum network simulator if time/iteration limit reached<br><!-- End of picture text -->

f f 



<!-- Start of picture text -->
Time =t = : Time =t + At<br>SX 1<br>(0)\oelJ © Entanglementg  Swap 0){og Server :' P ™N—oO (6%00© 9) server<br>Pa /1. ya ~~ 4 B-6 ' \ 0 @f _<br>Switch ) o, . 9c<br>0.00 / : Switch |<br>Am —— '<br>O2y 1 ' S—<br>M to buff H © Quantum memory (unoccupied)<br>User \Z/[ ody Le ove loner ;! Au Coo: J\ O2 -2,§ MidpointEntangledEntangled photon stationqubit<br>B=5 ser (© #. Time stamp<br>:<br>1<br>1}<br>:<br><!-- End of picture text -->



<!-- Start of picture text -->
Te 2.5 { memmmmg<br>0 1 2 3 4 0 1 2 3 4<br>User<br>J a Se Ra<br>> 0.92 1 ~~<br>@ > so —e— Surrogate<br>i 0-90 SP Ee 3 --== Meta<br>0.88 =1+ ASgrLe” -v--=--- SimulatedRandom Search Annealing<br>0 1 2 3 4<br>User<br><!-- End of picture text -->



<!-- Start of picture text -->
_<br>_-—<br>_—<br>_—<br><!-- End of picture text -->



<!-- Start of picture text -->
O © Node pair requesting entanglement NU-Evaston<br>q  # Memory qubits @2D = +<br>——— Physical channel 5)<br>—— Reserved path q=4 UChicago-HC<br>StarLight i TN<br>—~ UChicago-PME Op<br>~~On) oJOOoR q=3 A<br>q=6 v<br>Fermilab-2 Fermilab-1 q=7 = n<br>{08 08 9=5 *<br>\q=4o NN\ q=4© Argonne-tyou{gxeA10©O ~~~)“2~' Argonne-3 - +<br>( Qo q=5<br>\O< Argonne-2<br>q=3<br><!-- End of picture text -->

continuous-distribution protocols distribute entanglement nonstop throughout the network<sup>45</sup> . This allows for immediate use of entanglement by any node as needed, supporting applications that continuously operate and consume entanglement in the background. In particular, we consider the continuous-distribution protocol introduced in ref.<sup>41</sup> , and we aim to find parameter values that optimize its performance. This protocol operates in discrete time. In each time slot, all physically neighboring pairs of nodes in the network (i.e., nodes that share a physical communication channel, such as optical fiber) attempt entanglement generation simultaneously, where each attempt succeeds with probability _p_ gen. For simplicity, we assume that all link lengths are the same. A pair of nodes can successfully generate entanglement in successive time slots and hold multiple entangled links, limited only by the number of qubits available at the nodes (see Figure 6). Each node _i_ holds a number of memory qubits proportional to the number of physical neighbors: _r · di_ , where _r ∈_ N is a parameter specified in the protocol and _di_ is the degree of node _i_ . 

Entanglement between non-neighboring nodes _j_ and _k_ can be generated via entanglement swapping at a node _i_ if entangled links _i − j_ and _i − k_ already exist. In each time slot, each node _i_ randomly chooses two links _i − j_ and _i − k_ , and performs a swap operation on them with probability _q_ swap _,i ∈_ [0 _,_ 1] (otherwise, the swap is not performed and the links stay as they are). A successful swap consumes both links and produces a _j − k_ link. We assume that swaps succeed deterministically. As every swap decreases the quality of the entanglement<sup>8</sup> , limiting the number of consecutive swaps presents a practical measure to prevent excessive decoherence. In the considered protocol, the number of adjacent swaps is limited to involve a maximum of _M_ physical links. Furthermore, as the quality of an entangled link generally worsens with time<sup>8,56</sup> , links that exist for longer than some cutoff time _t_ cut are removed to exclude low-quality entanglement from the network. Lastly, we assume that there is an application running on the network that consumes the entangled links generated by the protocol. Specifically, pairs of nodes consume an existing entangled link at each time slot with probability _p_ cons. We simulate this protocol over _Tsim_ time slots, where _Tsim_ is a number of discrete time units. 

The utility in this use case quantifies the ability of a user to run background applications. This is determined by the number of readily available entangled links to other nodes in the network. Nodes connected by at least one entangled link are termed _virtual neighbors_ . The objective therefore is to maximize the number of virtual neighbors for all users, which can be accomplished by tuning the swap probability _q_ swap _,i_ at each node _i_ . We use the vector **q** swap = [ _q_ swap _,_ 0 _, q_ swap _,_ 1 _,..., q_ swap _,N−_ 1] to represent all _N_ nodes’ swap probabilities. 

In contrast to previous use cases, our analysis of continuous-distribution protocols goes beyond aggregating objectives: it includes examining the individual user’s goal to increase their own number of virtual neighbors. This approach is based on the Pareto frontier, a method of assessing multi-objective optimality, formally defined in e.g., ref.<sup>41</sup> . As outlined in Section 1.2, the surrogate optimization process naturally collects instances of _{_ **q** swap _}_ and their simulation outcomes (objective values) as training data. We will refer to the former as the _collected set S_ of solutions. From this data, we can find the dominating set _S_ dom _⊆S_ , which functions as an empirical estimate of the Pareto optimal set. It is important to note that this analysis of the collected solutions is not exclusive to this use case but could be applied to the other presented use cases as well. For clarity and illustrative purposes, however, we include this analysis only as part of this last section. 

**Definition 2.3** (Dominating Set _S_ dom) **.** _Let S represent the set of all solutions collected during the surrogate optimization process, and let S_ dom _denote the subset of these solutions that form the dominating set. A solution_ **q**<sup>_∗_</sup> swap<sup>_∈Sbelongs to S_dom</sup><sup>_if and only if there does not exist another solution_</sup><sup>**q**swap</sup><sup>_∈Ssuch that_</sup><sup>**q**swap</sup><sup>_dominates_</sup> **q**<sup>_∗_</sup> swap<sup>_.A solution_</sup><sup>**q**swap</sup><sup>_dominates_</sup><sup>**q**</sup><sup>_∗_</sup> swap<sup>_if:_</sup> 



_Thus, each solution in S_ dom _is non-dominated with respect to the objectives {U_<sup>(1)</sup> _,...,U_<sup>(</sup><sup>_m_)</sup> _}, and any solution in S \S_ dom _is dominated by at least one solution in S_ dom _._ 

For an intuitive explanation, see Supplementary Figure 3. In our approach, _U_<sup>¯(</sup><sup>_i_)</sup> ( _f ,_ **q** swap) denotes the average number of virtual neighbors per user _i_ , which is generated by the simulation function _f_ ( **q** swap) of ref.<sup>41</sup> . 

First, we investigate a simple three-node quantum network, where all three nodes are users who are able to swap entanglement. Then, we extend our study to two larger asymmetric topologies involving 20 and 100 nodes, respectively. All three layouts are depicted in Figure 6. In the two larger networks, all nodes are again able to swap entanglement, but only the leaf nodes (nodes with one physical neighbor) are considered _users_ . We explore the different setups by analyzing the dominating set of the collected solutions. However, we will also demonstrate that as the number of objective functions (i.e., the number of users) increases, a larger proportion of solutions is non-dominated, which is a well-known consequence of multi-objective optimization in high dimensional spaces<sup>57</sup> . Lastly, we conduct the already familiar comparison of aggregated objectives (sum over all users) found by surrogate optimization to the reference methods in the largest network topology. In our experiments we simulate continuous 

**8/20** 



<!-- Start of picture text -->
User 0<br>Ale<br>Entanglement Swap Bos\./ ~~ 11)<br>N \ 10,<br>NE A 0 Va<br>TaNBA Q oy Aa7<br>User 1 oe [0] User 2 so No A<br>rd<br>— Physical link 3 ~~<br>© Memory qubit A 5 _ gp —12—<br>© Qubit sharing entanglement<br>O Qubit selected for entanglement swap<br>Js Probability of executing entanglement swap<br>BAD wa 888B<br>A .28a A<br>Na<br>A A AN 980<br>Ba—a A, Toa Ng? ’<br>A o—a—— a=VAp=ND 4 a<br>A arg A 8 5 N A<br>a a HBR ssa BH<br>A 5>1 9) 7 BR 1As<br>a <9?<br>Ta,Pats a)<br>7573yrANEA<br><!-- End of picture text -->



<!-- Start of picture text -->
A 1.0<br>RY, 0.8<br>19 A<br>er RB 04°<br>A . 8 Aguap standard deviation> 10% 02<br>0.0<br><!-- End of picture text -->



<!-- Start of picture text -->
I<br><!-- End of picture text -->



<!-- Start of picture text -->
80.0<br>77.5<br>75.0<br>Method<br>72.5 Surrogate<br>Meta<br>70.0 Simulated Annealing<br>Random Search<br>67.5<br>65.0<br>62.5<br>2 4 6 8 10<br>Time Limit [h]<br>Aggregated Number of Virtual Neighbors<br><!-- End of picture text -->

**Figure 8. Aggregated number of virtual neighbors for 100-node network and best found solution.** The best of ten solutions (of ten independent repetitions conducted, see 4.2) according to the objective function is selected. and a subsequent simulation involving runs. We find that all but Meta benefit from enlarged time constraints. Each point in the graph plot shown presents the mean of _nexec_ = 10<sup>3</sup> simulation runs (with standard errors smaller than marker size). Execution parameters used in the surrogate workflow: _T_ = [1 _,_ 5 _,_ 10] h, _d_ = 4, _n_ = 20. 

below Simulated Annealing; this is likely because the 100 variables present in this network are far beyond the recommended limit of 20<sup>30</sup> . Conversely, the models used by our surrogate optimizer are evidently not limited by the large number of variables, showing significant improvement with increased time limit. Note that even though random search identifies a solution within a ten-hour limit – using _n_ = 20 simulation runs – that exhibits more virtual neighbors than the solution found in the five-hour limit, the use of _nexec_ = 10<sup>3</sup> simulation runs of the result depicted in Figure 8 provides a more accurate estimate of the average, albeit a smaller one. 

To conclude this section, we summarize the most relevant findings: across different quantum network sizes, the collected dominating set can provide relevant insights to the behaviour of parameters in continuous-distribution protocols when multiple objectives are to be met. Even for a 20-node setup, swap probability distributions are concentrated at some nodes, which can guide the configuration of these parameters in a protocol. However, the ratio of non-dominated to dominated solutions increases significantly with the number of objectives; in the largest network studied, this leads to all parameter distributions being closer to a uniform than to a normal distribution. Although the dominating set provided limited insights in the largest setup, we could still find a promising solution to the single-objective case, i.e., maximizing the sum over all users’ virtual neighbors. The latter comprises 79 virtual neighbors on average, which is 18% and 20% higher than the best solutions found by Simulated Annealing and Bayesian optimization, respectively. 

## **3 Related Work** 

In addition to the work discussed in the above scenarios, relevant prior studies were carried out by Ferreira da Silva et al.<sup>18</sup> , Wallnhöfer et al.<sup>20</sup> , Khatri et al.<sup>21</sup> and Haldar et al.<sup>22</sup> . Ref.<sup>18</sup> utilized genetic algorithms combined with simulation of repeater chains in NetSquid. In contrast to genetic algorithms, our approach utilized simple machine learning models to save on extensive evaluation of the expensive objective function, which helped to traverse the search space more efficiently. Further, ref.<sup>18</sup> focused on optimizing for minimum requirements to satisfy target benchmarks, while we investigated diverse utility functions based on different use cases. Similar to our approach, the other studies<sup>20–22</sup> used machine learning techniques to find optimal quantum network protocols. These studies were based on the theoretical framework of decision processes. Ref.<sup>20</sup> introduced for the first time learning agents for quantum networks, which by trial and error manipulate quantum states and thereby construct communication protocols. Ref.<sup>21</sup> and ref.<sup>22</sup> devised a mathematical framework to optimize link-level entanglement generation in general networks allowing for said learning agents to discover policies. In contrast to our approach, learning agents are able discover complete protocols (devising optimal sequences of actions), while surrogate optimization is limited to finding improved parameter settings _within_ protocols. However, our approach offers two distinct advantages: 1) It is applicable to enhancing hardware configurations, such as the allocation of memory qubits per node. In contrast, learning agents operate within a static architectural environment, limiting them to discover only quantum network protocols; 2) We employ detailed quantum network simulations, in contrast to the purely mathematical or overly simplified models used in other studies. This allows us to address complex network topologies beyond, e.g., simple linear repeater chains typically considered in prior work. 

**11/20** 

## **4 Methods** 

### **4.1 Baselines** 

In order to evaluate our approach, we utilize the following baselines: 1) _Uniform random search_ : this method chooses sets of parameter values uniformly at random from _X_ conf to execute the simulation. We employ this method as our foundational baseline because its constraints are easily managed through time or iteration limits. Uniform sampling prevents being constrained to a specific area of the search domain, a limitation that might be encountered by a time- or iteration-limited exhaustive grid search. 2) _Simulated Annealing_<sup>47</sup> : this conventional global optimization method starts by accepting less optimal solutions with high probability, thus enabling exploration of the search space and escaping from local optima using the so-called Metropolis criterion. We implemented the algorithm using the fast annealing schedule<sup>27</sup> and found objective values of various benchmark functions<sup>60</sup> comparable to the L-BFGS-B method<sup>61</sup> . 3) _Bayesian optimization API by Meta_ : Bayesian optimization<sup>62</sup> is a surrogate method based on Gaussian processes, which is mostly used to optimize unknown but continuous functions; empirical studies suggest optimal performance below 20 variables<sup>30</sup> . The Service/Loop API, developed by Meta, incorporates a Bayesian optimization algorithm<sup>46</sup> , where we adhere to the default configuration settings recommended in their official documentation (https://ax.dev/docs/bayesopt). 

### **4.2 Simulation Experiments** 

For each use case scenario, we compared optimization methods by conducting ten independent repetitions, each with an allotted time limit of _T_ hours. To compute averages _U_<sup>¯(</sup><sup>_i_)</sup> ( _f ,._ ) we used _n_ = 20 simulation runs by default. We report on the distribution of the ten repetitions in Supplementary Note 6. From all repetitions, the solution that performed best according to the objective function is selected, and a subsequent simulation involving _nexec_ = 10<sup>3</sup> simulation runs were executed. This approach leads to statistically robust solutions, characterized by small standard errors (explicit values given in captions of respective result figures). In the scenarios, where we did not compare to reference methods, _T_ is a set number of optimization cycles and _n ≥_ 100. Note that in scenarios involving time constraints for comparison between reference methods, the outcomes are specific to our computing system. For instance, let us assume a simulation takes nine seconds to execute on our system but ten seconds on another computer. If we impose a time limit that permits ten executions on our system, the same time limit would only allow nine executions on the slower one, resulting in different outcomes. Since execution times depend on multiple aspects of a computing node (processor speed, RAM, operating system), to ensure exact reproducibility of output data, it is advisable to use a fixed number of iterations; we diverged from this to enable fair comparison between used optimization methods. Each optimization method was allocated ten cores on an Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz and 64 GB of memory. 

## **Conclusion** 

We introduced a surrogate-based optimization workflow that integrates detailed quantum network simulations. Through three distinct use cases, we demonstrated the workflow’s broad applicability to practical optimization problems and its effectiveness in enhancing the performance of both on-demand and continuous entanglement distribution protocols across various network topologies. Particularly, the application to a five-user quantum entanglement switch and a metropolitan network performing purification protocols, showed our method’s efficacy to handle complex and highly asymmetric quantum networking scenarios. Our workflow efficiently handled up to 100 network parameters and achieved approximate solutions that significantly outperformed optimization techniques such as Simulated Annealing (up to 18%) and Bayesian optimization (up to 20%) in tested scenarios. Moreover, finding the dominating set of collected solutions allowed us to derive insights from a multi-objective perspective. 

Due to the potentially large computational costs of numerical simulation, our approach is suitable for scenarios where the simulation models an analytically intractable problem, i.e., a problem scenario in which it is justified to invest additional time in simulation and optimization. Overall, this work introduced a scalable and effective optimization tool for the discovery of new beneficial quantum network configurations and demonstrated its contribution in practical use cases. 

## **Acknowledgements** 

This work is supported by QuTech NWO funding 2020–2024 Part I ‘Fundamental Research’, Project Number 601.QT.001-1, financed by the Dutch Research Council (NWO). We further acknowledge support from _NWO QSC grant BGR2 17.269._ Á.G.I. acknowledges financial support from the Netherlands Organisation for Scientific Research (NWO/OCW), as part of the Frontiers of Nanoscience program. 

**12/20** 

## **Data and Code availability** 

Source data, as well as well as generated machine learning models and time profiling data is available at https://doi.org/10.4121/a07a9e97-f34c-4e7f-9f68-1010bfb857d0. The code used to generate reported data, as well as usage guidelines can be found in the Git repository https://github.com/ Luisenden/qnetsur and corresponding documentation https://qnetsur.readthedocs.io. 

## **References** 

**1.** Wehner, S., Elkouss, D. & Hanson, R. Quantum internet: A vision for the road ahead. _Science_ **362** , eaam9288, DOI: 10.1126/science.aam9288 (2018). https://www.science.org/doi/pdf/10.1126/science.aam9288. 

**2.** Bennett, C. H. & Brassard, G. Quantum cryptography: Public key distribution and coin tossing. _Theor. computer science_ **560** , 7–11 (2014). 

**3.** Ekert, A. K. Quantum cryptography and Bell’s theorem. _Quantum Meas. Opt._ 413–418 (1991). 

**4.** Giovannetti, V., Lloyd, S. & Maccone, L. Quantum-enhanced measurements: Beating the standard quantum limit. _Science_ **306** , 1330–1336 (2004). 

**5.** Jozsa, R., Abrams, D. S., Dowling, J. P. & Williams, C. P. Quantum clock synchronization based on shared prior entanglement. _Phys. Rev. Lett._ **85** , 2010 (2000). 

**6.** Broadbent, A., Fitzsimons, J. & Kashefi, E. Universal blind quantum computation. In _2009 50th Annual IEEE Symposium on Foundations of Computer Science_ , 517–526 (IEEE, 2009). 

**7.** Fitzsimons, J. F. & Kashefi, E. Unconditionally verifiable blind quantum computation. _Phys. Rev. A_ **96** , 012303 (2017). 

**8.** Azuma, K. _et al._ Quantum repeaters: From quantum networks to the quantum internet. _Rev. Mod. Phys._ **95** , 045006 (2023). 

**9.** Dahlberg, A. _et al._ A link layer protocol for quantum networks. In _Proceedings of the ACM Special Interest Group on Data Communication_ , SIGCOMM ’19, 159–173, DOI: 10.1145/3341302.3342070 (Association for Computing Machinery, New York, NY, USA, 2019). 

**10.** Van Meter, R., Ladd, T. D. & Nemoto, K. System design for a long-line quantum repeater. _IEEE/ACM Transactions On Netw._ **17** , 1002–1013 (2008). 

**11.** Vardoyan, G., Guha, S., Nain, P. & Towsley, D. On the stochastic analysis of a quantum entanglement switch. _ACM SIGMETRICS Perform. Eval. Rev._ **47** , 27–29 (2019). 

**12.** Iñesta, Á. G., Vardoyan, G., Scavuzzo, L. & Wehner, S. Optimal entanglement distribution policies in homogeneous repeater chains with cutoffs. _arXiv preprint arXiv:2207.06533_ (2022). 

**13.** Vardoyan, G. & Wehner, S. Quantum network utility maximization. In _2023 IEEE International Conference on Quantum Computing and Engineering (QCE)_ , vol. 1, 1238–1248 (IEEE, 2023). 

**14.** Liao, C.-T., Bahrani, S., da Silva, F. F. & Kashefi, E. Benchmarking of quantum protocols. _Sci. Reports_ **12** , 5298 (2022). 

**15.** Avis, G. _et al._ Requirements for a processing-node quantum repeater on a real-world fiber grid. _NPJ Quantum Inf._ **9** , 100 (2023). 

**16.** Ghaderibaneh, M., Gupta, H., Ramakrishnan, C. & Luo, E. Pre-distribution of entanglements in quantum networks. In _2022 IEEE International Conference on Quantum Computing and Engineering (QCE)_ , 426–436 (IEEE, 2022). 

**17.** Kozlowski, W., Dahlberg, A. & Wehner, S. Designing a quantum network protocol. In _Proceedings of the 16th international conference on emerging networking experiments and technologies_ , 1–16 (2020). 

**18.** Da Silva, F. F., Torres-Knoop, A., Coopmans, T., Maier, D. & Wehner, S. Optimizing entanglement generation and distribution using genetic algorithms. _Quantum Sci. Technol._ **6** , 035007 (2021). 

**19.** Dam, J. V. _et al._ Hardware requirements for trapped-ion based verifiable blind quantum computing with a measurement-only client (2024). 2403.02656. 

**20.** Wallnöfer, J., Melnikov, A. A., Dür, W. & Briegel, H. J. Machine learning for long-distance quantum communication. _PRX Quantum_ DOI: 10.1103/prxquantum.1.010301 (2020). 

**21.** Khatri, S. Policies for elementary links in a quantum network. _Quantum_ **5** , 537 (2021). 

**22.** Haldar, S., Barge, P. J., Khatri, S. & Lee, H. Fast and reliable entanglement distribution with quantum repeaters: Principles for improving protocols using reinforcement learning. _Phys. Rev. Appl._ **21** , 024041, DOI: 10.1103/PhysRevApplied.21. 024041 (2024). 

**23.** Coopmans, T. _et al._ Netsquid, a network simulator for quantum information using discrete events. _Commun. Phys._ **4** , 164 (2021). 

**24.** Wu, X. _et al._ Sequence: a customizable discrete-event simulator of quantum networks. _Quantum Sci. Technol._ **6** , 045027 (2021). 

**25.** Box, G. E. & Draper, N. R. _Empirical model-building and response surfaces._ (John Wiley & Sons, 1987). 

**13/20** 

**26.** Queipo, N. V. _et al._ Surrogate-based analysis and optimization. _Prog. aerospace sciences_ **41** , 1–28 (2005). 

**27.** Kochenderfer, M. J. & Wheeler, T. A. _Algorithms for optimization_ (Mit Press, 2019). 

**28.** Shahriari, B., Swersky, K., Wang, Z., Adams, R. P. & de Freitas, N. Taking the human out of the loop: A review of bayesian optimization. _Proc. IEEE_ **104** , 148–175, DOI: 10.1109/JPROC.2015.2494218 (2016). 

**29.** Tripathy, R. K. & Bilionis, I. Deep uq: Learning deep neural network surrogate models for high dimensional uncertainty quantification. _J. computational physics_ **375** , 565–588 (2018). 

**30.** Frazier, P. I. A tutorial on bayesian optimization. _arXiv preprint arXiv:1807.02811_ (2018). 

**31.** Weiss, S. M. & Kulikowski, C. A. _Computer systems that learn: classification and prediction methods from statistics, neural nets, machine learning, and expert systems_ (Morgan Kaufmann Publishers Inc., 1991). 

**32.** Carvalho, D. V., Pereira, E. M. & Cardoso, J. S. Machine learning interpretability: A survey on methods and metrics. _Electronics_ **8** , 832 (2019). 

**33.** Gunn, S. R. _et al._ Support vector machines for classification and regression. _ISIS technical report_ **14** , 5–16 (1998). 

**34.** Breiman, L. Random forests. _Mach. learning_ **45** , 5–32 (2001). 

**35.** Bhosekar, A. & Ierapetritou, M. Advances in surrogate based modeling, feasibility analysis, and optimization: A review. _Comput. & Chem. Eng._ **108** , 250–267 (2018). 

**36.** Wang, J. Y. _et al._ Identifying general reaction conditions by bandit optimization. _Nature_ **626** , 1025–1033 (2024). 

**37.** Kusne, A. G. _et al._ On-the-fly closed-loop materials discovery via bayesian active learning. _Nat. communications_ **11** , 5966 (2020). 

**38.** Popp, J., Haider, M., Franckié, M., Faist, J. & Jirauschek, C. Bayesian optimization of quantum cascade detectors. _Opt. Quantum Electron._ **53** , 287 (2021). 

**39.** Stevense, W. Numerical investigation of the effect of hardware parameters on atomic-ensemble-based repeater protocols. _Master Thesis (not published)_ (2024). 

**40.** Cortes, C. L. _et al._ Sample-efficient adaptive calibration of quantum networks using bayesian optimization. _Phys. Rev. Appl._ **17** , 034067 (2022). 

**41.** Iñesta, Á. G. & Wehner, S. Performance metrics for the continuous distribution of entanglement in multiuser quantum networks. _Phys. Rev. A_ **108** , 052615 (2023). 

**42.** Khammassi, N. _et al._ Openql: A portable quantum programming framework for quantum accelerators. _ACM J. on Emerg. Technol. Comput. Syst. (JETC)_ **18** , 1–24 (2021). 

**43.** Alcazar, J., Ghazi Vakili, M., Kalayci, C. B. & Perdomo-Ortiz, A. Enhancing combinatorial optimization with classical and quantum generative models. _Nat. Commun._ **15** , 2761 (2024). 

**44.** Pedregosa, F. _et al._ Scikit-learn: Machine learning in Python. _J. Mach. Learn. Res._ **12** , 2825–2830 (2011). 

**45.** Chakraborty, K., Rozpedek, F., Dahlberg, A. & Wehner, S. Distributed routing in a quantum internet. _arXiv preprint arXiv:1907.11630_ (2019). 

**46.** Balandat, M. _et al._ Botorch: A framework for efficient monte-carlo bayesian optimization. _Adv. neural information processing systems_ **33** , 21524–21538 (2020). 

**47.** Kirkpatrick, S., Gelatt Jr, C. D. & Vecchi, M. P. Optimization by simulated annealing. _science_ **220** , 671–680 (1983). 

**48.** Rains, E. M. A semidefinite program for distillable entanglement. _IEEE Transactions on Inf. Theory_ **47** , 2921–2933 (2001). 

**49.** Vardoyan, G., Nain, P., Guha, S. & Towsley, D. On the capacity region of bipartite and tripartite entanglement switching. _ACM Transactions on Model. Perform. Eval. Comput. Syst._ **8** , 1–18 (2023). 

**50.** Nain, P., Vardoyan, G., Guha, S. & Towsley, D. On the analysis of a multipartite entanglement distribution switch. _Proc. ACM on Meas. Analysis Comput. Syst._ **4** , 1–39 (2020). 

**51.** Humphreys, P. C. _et al._ Deterministic delivery of remote entanglement on a quantum network. _Nature_ **558** , 268–273 (2018). 

**52.** Bennett, C. H., DiVincenzo, D. P., Smolin, J. A. & Wootters, W. K. Mixed-state entanglement and quantum error correction. _Phys. Rev. A_ **54** , 3824 (1996). 

**53.** Ranˇci´c, M., Hedges, M. P., Ahlefeldt, R. L. & Sellars, M. J. Coherence time of over a second in a telecom-compatible quantum memory storage material. _Nat. Phys._ **14** , 50–54 (2018). 

**54.** Bennett, C. H. _et al._ Purification of noisy entanglement and faithful teleportation via noisy channels. _Phys. review letters_ **76** , 722 (1996). 

**55.** Dür, W. & Briegel, H. J. Entanglement purification and quantum error correction. _Reports on Prog. Phys._ **70** , 1381 (2007). 

**56.** Khatri, S., Matyas, C. T., Siddiqui, A. U. & Dowling, J. P. Practical figures of merit and thresholds for entanglement distribution in quantum networks. _Phys. Rev. Res._ **1** , 023032 (2019). 

**57.** Kukkonen, S. & Lampinen, J. Ranking-dominance and many-objective optimization. In _2007 IEEE Congress on Evolutionary Computation_ , 3983–3990 (IEEE, 2007). 

**14/20** 

**58.** Kung, H.-T., Luccio, F. & Preparata, F. P. On finding the maxima of a set of vectors. _J. ACM (JACM)_ **22** , 469–476 (1975). 

**59.** Lilliefors, H. W. On the Kolmogorov-Smirnov test for normality with mean and variance unknown. _J. Am. statistical Assoc._ **62** , 399–402 (1967). 

**60.** Jamil, M. & Yang, X.-S. A literature survey of benchmark functions for global optimisation problems. _Int. J. Math. Model. Numer. Optimisation_ **4** , 150–194 (2013). 

**61.** Liu, D. C. & Nocedal, J. On the limited memory BFGS method for large scale optimization. _Math. programming_ **45** , 503–528 (1989). 

**62.** Jones, D. R., Schonlau, M. & Welch, W. J. Efficient global optimization of expensive black-box functions. _J. Glob. optimization_ **13** , 455–492 (1998). 

## **Supplementary Note 1 Exploration vs exploitation in surrogate-assisted search** 

We apply the following exploration versus exploitation strategy in the introduced surrogate-assisted search: given a top configuration **s**<sup>top</sup> = _{x_ 1 _,..., xN }_ , each optimization cycle _t_ decreases the standard deviation of a normal distribution _N_ trunc( _µp, σp_ ( _t, d_ )) around each parameter value _µp ≡ xp_ . This way, the focus of discovering new, but less favorable configurations (exploration) gradually shifts towards refining known and well-performing configurations (exploitation). To achieve this, the distribution is truncated at _x_<sup>min</sup> _p_ and _x_<sup>max</sup> _p_ and the standard deviation narrows as _σp_ ( _t, d_ ) = _γ_ ( _t, d_ )( _x_<sup>max</sup> _p − x_<sup>min</sup> _p_ ) _/_ 2, with 

_γ_ ( _t, d_ ) = (1 _−_ ln<sup>2</sup> (1 + _t/T_ ))<sup>_d_</sup> _,_ where _d ≥_ 1 (6) 

is a monotonically decreasing function for _t ∈_ [0 _, T_ ] (see proof below), _T_ is the maximum number of optimization cycles and _d_ is chosen according to desired degree of exploitation. For instance, _d_ = 1 leads to a minimum deviation of _σp_ ( _t_ = _T_ ) = 0 _._ 52 _·_ ( _x_<sup>max</sup> _p − x_<sup>min</sup> _p_ ) _/_ 2. In other words, by the end of the optimization process, the neighborhood, i.e., standard deviation, in which the models are mostly evaluated has been reduced to almost half its initial value; Figure 9 shows four examples of the transition function, each with a different degree of exploitation. 



<!-- Start of picture text -->
1.0<br>0.8<br>0.6<br>0.4 d=0<br>d=2<br>0.2 d=4<br>d=6<br>0.0<br>0.0 0.2 0.4 0.6 0.8 1.0<br>t/T<br>)<br>t<br>(<br><!-- End of picture text -->

**Figure 9.** Transition function, where _t ∈_ [0 _, T_ ], using different exploitation degrees _d_ . 

_Proof._ A function is monotonically decreasing over an interval when its derivative remains negative throughout that interval. Thus our goal is to show that<sup>_∂_</sup><sup>_<u>γ</u>_</sup> _∂_<sup><u>(</u></sup><sup>_t_</sup> _t_<sup>_<u>,d</u>_</sup><sup><u>)</u></sup> _<_ 0 for 0 _≤ t ≤ T_ . 



Since 0 _≤_ ln� _<u>t</u>_ <u>+</u> _TT_ � _<_ 1, the term (1 _−_ ln<sup>2</sup> (<sup>_<u>t</u>_</sup><sup><u>+</u></sup> _T_<sup>_<u>T</u>_))</sup><sup>_d−_1must positive (recall that</sup><sup>_d ≥_1 by assumption).The negative sign in</sup> front of the fraction confirms that<sup>_∂_</sup><sup>_<u>γ</u>_</sup> _∂_<sup><u>(</u></sup><sup>_t_</sup> _t_<sup>_<u>,d</u>_</sup><sup><u>)</u></sup> is less than zero and thus _γ_ ( _t, d_ ) is monotonically decreasing on the interval [0 _, T_ ]. 

## **Supplementary Note 2 Acquisition process in surrogate-assisted search** 

In each cycle _t_ , the algorithm undertakes an acquisition process which involves two stages: model training and model evaluation. Initially, two machine learning models a – Support Vector Regressor and a Decision Tree Regressor – are trained independently. Their performance is then assessed through a five-fold cross-validation, using the mean absolute error as the metric on the current training data. The model demonstrating the lower error progresses to the acquisition phase. 

During the acquisition phase, _Nt_ different configurations are sampled from the current normal distribution _N_ trunc( _µp, σp_ ( _t, d_ )) across all parameters _xp ∈ s_<sup>_top_</sup> _i_ , where _s_<sup>_top_</sup> _i_ is among the _l_ currently best performing parameter sets. Specifically, for each _xp ∼ N_ trunc( _µp_ = _xp, σp_ ( _t, d_ )) we retrieve _Nt_ values, generating _Nt_ sample sets _{s_<sup>eval</sup> 1 _,..., s_<sup>eval</sup> _Nt_<sup>_}_to be evaluated.The number of</sup> 

**15/20** 

samples _Nt_ = _N_ ( _t_ ) drawn increases with the number of elapsed cycles according to the formula _N_ ( _t_ ) = 10 + 10<sup>4</sup> _· T_<sup>_<u>t</u>_, allowing</sup> more computational resources to be dedicated during later cycles as the models gain more insights about the true objective function. The machine learning model’s predicted objective values for the sampled configurations _{s_<sup>eval</sup> 1 _,..., s_<sup>eval</sup> _Nt_<sup>_}_are sorted,</sup> and the highest-rated set is passed to the simulation for execution. The resulting parameter set, along with its simulated objective outcome, is then added to the training set. 

## **Supplementary Note 3 Quantum entanglement switch use case** 

In this supplementary note, we describe the quantum entanglement switch (QES) modelled in NetSquid, along with the results obtained when the switch serves two users. In total the system is simulated over _T_ sim = 5 seconds generating user-server links. 

#### **Supplementary Note 3.1 QES Model** 

In this model, the users and server continuously attempt to generate entangled links with the switch node via the single-click entanglement generation scheme. Once established, these entangled links are stored in available memory qubits, acting as a memory buffer. The primary function of the switch is to facilitate connections between server and each of the users through entanglement swapping. 

1. _Link-level entanglement generation_ : In the single-click scheme assuming high photon losses, the fidelity of the produced states is given by _Fl_ = 1 _− αl_ , where _αl_ is the bright-state population, a tunable experimental parameter. In this scheme, a state of the form 



is generated with probability 

_p_ gen,l = 2 _ηlαl,_ where ��Ψ+� is a Bell state orthogonal to the product state _|↑↑⟩_ , e.g., ��Ψ+� = _~~√~~_ <u>12</u><sup>(</sup><sup>_|↑↓⟩_+</sup><sup>_|↓↑⟩_); and</sup><sup>_ηl_is the transmissivity of</sup> link _l_ with length _Ll_ , given by 

_ηl_ = 10<sup>_−_0</sup><sup>_._1</sup><sup>_βLl_</sup> _,_ 

where _β_ = 0 _._ 2 dB/km is the fiber attenuation coefficient. As the generation probability scales with the bright-state population _αl_ , the latter facilitates a trade-off between rate and fidelity. In our model, we approximate this physical behaviour with a depolarizing error happening with probability _pl_ = 3<sup><u>4</u></sup><sup>_αl_to a maximally entangled state, resulting in a Werner state with</sup> fidelity _F_ = 1 _− αl_ . Specifically, a depolarizing error degrades a perfect Bell state _ρBell_ = ��Ψ+��Ψ<sup>+��</sup> with a probability _pl_ to the quantum state 



The above state is a Werner state _ρw_ = _w · ρBell_ + (1 _− w_ )<sup><u>I</u></sup> 4<sup><u>4</u>withWernerparameter</sup><sup>_w_= 1</sup><sup>_−pl_andfidelity</sup><sup>_F_=</sup><sup><u>3</u></sup><sup>_<u>w</u>_</sup> 4<sup><u>+1</u></sup> . Within the QES simulation, the time interval between successful attempts follows an exponential distribution Exp(1 _/r_ ), with _r_ = _Tp_ attempt _<u>gen,l</u>_<sup>, where</sup><sup>_T_attempt = 10</sup><sup>_−_3s denotes the attempt-repetition time.</sup> 

2. _Memory Buffer_ . When a new entangled state is generated, the state is shared by the so-called communication qubits – one at the node (user/server) and one at the switch side – with the purpose to host entangled states during the generation process. After successful generation, the entangled state is transferred (without any time loss) along with a dedicated timestamp to free memory qubits, one at the node and one at the switch. Once in the buffer, the quantum states are assumed to be perfectly shielded, i.e., no noise is impairing the states. Should the buffer be full, the oldest state is discarded and the memory receives the fresh link. In our model, the users and server have 20 quantum memories at their disposal. 

3. _Entanglement swap._ The switch executes a Bell state measurement on the user-switch, and server-switch links to generate an end-to-end entangled link between user and server. By default, the user who holds the oldest link is chosen for the swap first (first come first served principle). Swaps are assumed to succeed deterministically with perfect gate operations. Further, the switch can only swap one link-pair at a time. After a swap, the state’s fidelity is recorded, and the state immediately discarded. 

#### **Supplementary Note 3.2 QES serving two users** 

We apply our surrogate workflow to a simple QES serving two users located two km from the switch node, while varying the server location between 2 km and 100 km from the switch. We thereby recover a selection of results from the analytical study by ref<sup>13</sup> . Figure 10a shows that the optimization outcomes we find closely mirror the analytical model: utility decreases linearly with the distance of the server-switch link due to the network’s decreasing ability to produce entanglement with high quality at high rates. When it comes to link-level fidelities _Fl_ , see Figure 10b, the server link as expected sacrifices the quality of the entanglement in order to accommodate the rates demanded from both the user sides. With increasing distance of the server to the switch, this trend is intensified; the user links’ quality increases in order to make up for the quality lost in the server link. While not surprisingly the fidelities in Figure 10d do not depend on the botteneck link’s length, the rate exponentially decreases, see Figure 10c. 

**16/20** 



<!-- Start of picture text -->
1.00<br>Analytical<br>6<br>Surrogate 0.98<br>5 Type<br>0.96<br>Server link<br>4 User link<br>0.94<br>3<br>0.92<br>0 20 40 60 80 100 0 25 50 75 100<br>Server Distance Lserver [km] Server Distance Lserver [km]<br>(a)  Utility based on distillable entanglement (b)  Link-level fidelities  Fl = 1 − αl<br>60 1.0<br>Analytical<br>50 Surrogate<br>0.9<br>40<br>30<br>0.8<br>20 Analytical<br>10 Surrogate<br>0.7<br>0 20 40 60 80 100 0 25 50 75 100<br>Server Distance Lserver [km] Server Distance Lserver [km]<br>(c)  End-to-end rates (d)  End-to-end fidelities<br>Utility Fidelity<br>Rate [Hz] Fidelity<br><!-- End of picture text -->

**Figure 10.** Utility maximization over bright-state parameters for a QES serving two users and a server. Triangular markers present outcomes found via surrogate-assisted search, while the analytical model is given by solid lines. (a)-(b) Found aggregate utility and link-level fidelities _Fl_ = 1 _− αl_ . (c)-(d) Rates and fidelities of produced user-server links. Each marker in (a), (c), and (d) indicates the mean and standard deviation of _n_ = 100 runs conducted in one simulation execution. Parameters used in the surrogate workflow: exploitation degree _d_ = 4, _T_ = 100 optimization cycles. 

## **Supplementary Note 4 Metropolitan network use case** 

Here, we detail the modeling of the metropolitan network that serves user requests and outline the memory distribution policies identified using surrogate optimization and reference methods. 

#### **Supplementary Note 4.1 Metropolitan Network Model** 

The network configuration in our study is based on a simulation utilizing the SeQUeNCe software package (Wu et al., 2021). Network performance is assessed by the capacity to fulfill entanglement requests between user pairs. The process involves a user selecting another user uniformly at random and placing an entanglement request. Should a request not meet the required fidelity, it is re-attempted until success. Each user sequentially submits and completes a request, restarting the cycle once all have participated. The simulation time is set to _T_ sim = 20 seconds. 

#### **_Underlying hardware of quantum network model_** 

Below, we present an overview of the quantum network model introduced by Wu et al. (2021) and list the relevant hardware parameters in Table 2. For a complete description of the model, we refer the interested reader to the original work. 

1. _Communication channels:_ Quantum communication over telecommunication fiber links come with a propagation delay _L/c_ , where _L_ is the fiber length and _c_ represents the speed of light within the fiber. Loss rates are quantified by the formula 10<sup>_−L·αo/_10</sup> , where _αo_ indicates the attenuation rate per kilometer in dB/km. To ensure orderly photon transmission, the system employs time-division multiplexing (TDM) to prevent overlap. 

2. _Midpoint station_ : Each midpoint station is equipped with a single-photon detector with a set efficiency, resolution and count rate (modelled as Poisson process). 

3. _Quantum Memories:_ During the process of entanglement generation, pairs of quantum memories located at different nodes undergo cycles of excitation and relaxation (memory frequency). This process results in each memory emitting a photon with probability _η|α|_<sup>2</sup> , depending on its state _α |↑⟩_ + _β |↓⟩_ and its memory efficiency _η_ . At the midpoint station, these photons are detected, and the duration of the entangled state being held in memory is determined by the assumed coherence time<sup>53</sup> , after which the entangled state is discarded by resetting the memory qubits. 

4. _Purification:_ Fidelity _∈_ [0 _,_ 1] is a measure of closeness of a given quantum state with respect to a reference (e.g., desired) state. The initial fidelity of stored states changes when these states are subject to swap or purification operations. The utilized BBPSSW protocol can probabilistically improve the fidelity of an entangled state by sacrificing another entangled state. First, operations are performed locally on both node sides on pairs of qubits holding an entangled state. Then the 

**17/20** 

target qubits are measured in the Z-basis. The protocol then assesses whether to keep or discard the qubit pairs based on the measurement results. When both nodes measure their respective qubits and achieve the same results, it signals a successful purification operation, improving the entanglement fidelity of the unmeasured qubits. Conversely, differing results indicate a failed purification attempt, and the pairs lose their entangled state. 

|**Parameter**|**Value**|
|---|---|
|Memory effciency_η_|0.75|
|Memory frequency|20 kHz|
|Memory coherence time|1.3 s|
|Memory fdelity|0.991|
|Detector effciency|0.8|
|Detector count rate|50 MHz|
|Detector resolution|100 ps|
|Attenuation (_αo_)|0.2 dB/km|
|Channel TDM time frame|20 ns|
|Gate fdelity|0.99|
|Swap success probability|0.64|
|Swapdegradation|0.99|



**Table 2.** Parameter values used in metropolitan network simulation model. 

#### **Supplementary Note 4.2 Memory distribution policies for metropolitan network** 

Table 3 depicts the memory allocations found by surrogate-assisted search and reference methods, alongside a simple uniform allocation, termed Even, and the approach introduced in Wu et al., 2021. 

|Node|Surrogate|Meta|Simulated Annealing|Random Search|Wu et. al, 2021|Even|
|---|---|---|---|---|---|---|
|NU|24|26|32|24|25|50|
|StarLight|73|79|88|34|91|50|
|UChicago PME|65|47|55|46|67|50|
|UChicago HC|26|40|31|33|24|50|
|Fermilab 1|60|54|63|86|67|50|
|Fermilab 2|25|31|43|23|24|50|
|Argonne 1|89|67|61|75|103|50|
|Argonne 2|39|36|29|73|25|50|
|Argonne 3|25|30|43|51|24|50|



**Table 3.** Number of memories allocated per user node. 

## **Supplementary Note 5 Estimated Pareto front of a three-node quantum network using continuous entanglement distribution protocols** 

The surrogate optimization process collects instances of network-parameter values (i.e., parameter sets), which we append to the _collected set S_ . From this data, we find the dominating set _S_ dom _⊆ S_ , which functions as an empirical estimate of the Pareto optimal set. Figure 11 shows an exemplary sample of random data and its collected dominating set _S_ dom in two objectives. In Figure 12 we show the aggregated number of virtual neighbors when executing the simulation over the whole parameter domain alongside the probability values of the dominating solutions _S_ dom. The two swap parameters are clearly distinguishable in _S_ dom: While the swap-probability values of Users 1 and 2 are spread out over the whole range, the swap parameter values of User 0 are concentrated around 0.2 with a relatively small standard deviation (of 0.05). These results can be interpreted as follows: The majority of virtual neighbors are established directly through entanglement generation at the physical links. Consequently, swapping becomes essential primarily for the entanglement shared between Users 1 and 2, who lack a direct physical connection. Since only one third of the entangled links are generated exclusively through swapping at User 0, maintaining a low swap probability for User 0 proves sufficient. 

**18/20** 



<!-- Start of picture text -->
1.00<br>dom<br>0.75 dom<br>0.50<br>0.25<br>0.00<br>0.0 0.5 1.0<br>Objective 1<br>Objective 2<br><!-- End of picture text -->

**Figure 11.** Estimated Pareto frontier _S_ dom in two maximization objectives (using uniform random data). A solution _∈ S_ dom (orange) is not worse in any objective, and better in at least one objective than solutions _∈ S_ (blue). 



<!-- Start of picture text -->
0.0<br>5.0 1.0<br>0.11<br>0.21 4.5<br>0.8<br>0.32<br>4.0<br>0.42<br>0.6<br>0.53 3.5<br>0.63<br>3.0 0.4<br>0.74<br>0.84<br>2.5<br>0.95 0.2<br>0.0<br>qswap, 1 User 0 User 1,2<br>0.00.110.210.320.420.530.630.740.840.95<br>, 0<br>swap<br>q swap<br>q<br>Aggregated Virtual Neighbors<br><!-- End of picture text -->

**(a)** Aggregated number of neighbors for three-user network. 



<!-- Start of picture text -->
(b)  Distribution of parameter values in  S dom.<br><!-- End of picture text -->

**Figure 12.** (a) Aggregated number of virtual neighbors generated by the simulation for different swap probabilities _p_ swap _,_ 1 _/_ 2. Each grid square presents the mean of _n_ exec = 10<sup>3</sup> simulation runs (with a standard error below 0.01). The largest amount (light orange) of virtual neighbors can be provided by the network, when the protocol swap probabilities are small for User 0; the swap probabilities for the Users 1 and 2 have less significant impact. (b) Boxplots present each a distributions of 35 values in the collected solution set _S_ dom out of a over thousand (3.5%) collected solutions. We use the following parameter settings in our surrogate workflow: _T_ = 100 optimization cycles, _d_ = 4, _n_ = 1000. 

## **Supplementary Note 6 Distribution of found objectives and time profiling** 

In this supplementary note, we provide an overview of the distribution of objective values obtained from our surrogate optimizer and reference methods across use cases. Additionally, we detail the time allocation of the surrogate optimizer across different tasks. Table 4 summarizes the distribution of run results, where a smaller sample size _n_ results in a broader distribution. For instance, in the Metropolitan Network use case, a small number of simulation evaluations _n_ = 5 yields a relatively high standard deviation of 10%. In contrast, the standard deviation is below 3% in the QES and continuous-protocols use cases. Table 5 details the time spent in the surrogate-assisted search. As expected simulation consumes most of the optimization time, accounting for 85% up to 99% of the total execution time _T_ across all use cases. 

|||**QES**|**Met**|**ropolitan**|**C**|**ontinuous Protocols**|
|---|---|---|---|---|---|---|
|Utility|Di|stillable|Co|mpleted||Virtual Neighbors|
|based on|Ent|anglment|R|equests||(_T_ =1 _|_5 _|_10 h)|
|**Method**|Mean|Std (rel.%)|Mean|Std (rel.%)|Mean|Std (rel.%)|
|Surrogate|11.1|0.3 (3)|34.7|3.4 (10)<br>70.1|_|_77.1_|_|80.1<br>2.0 (3)_|_1.7 (2)_|_1.3 (2)|
|Meta|11.3|0.1 (1)|28.8|4.6 (16)<br>63.9|_|_65.4_|_|65.8<br>0.7 (1)_|_1.1 (2)_|_0.9 (1)|
|Simulated A.|10.3|0.4 (4)|24.0|8.0 (33)<br>64.0|_|_65.8_|_|66.8<br>1.0 (2)_|_1.2 (2)_|_1.0 (2)|
|Random S.|10.0|0.5 (5)|18.2|9.2 (51)<br>63.3|_|_64.7_|_|65.1<br>1.3 (2)_|_0.8 (1)_|_1.2 (2)|



**Table 4.** Distribution of maximum empirical utility values. Values present mean and (relative) standard deviation of ten independently conducted optimization experiments per method across investigated use cases. 

**19/20** 

||QES(_T_ =30 min)|Metropolitan(_T_ =25 h)|Continuous Protocols(_T_|=1 _|_5 _|_10 h)|
|---|---|---|---|---|
|Simulation|99.1 %|99.78 %|95.0_|_|87.2_|_85.3 %|
|Training|0.1 %|0.01 %|0.|3_|_1.4_|_1.9 %|
|Acquisition|0.6 %|0.2 %|4.5_|_|11.2_|_12.7 %|
|Remaining|0.2 %|0.01 %|0.|2_|_0.2_|_0.1 %|
|# Cycles|26.9|35.2|16.0|_|_72.3_|_112.6|



**Table 5.** Time profiling of ten independently conducted surrogate-assisted optimization experiments. _Simulation_ measures execution time of the simulation function at each optimization step. _Training_ refers to the time taken to construct machine learning models, while _Acquisition_ denotes the time required to identify a promising set of next execution points using these models. _Remaining_ includes initial object instantiation and writing to output files. The number of cycles represents the average count of optimization cycles completed within the prescribed time limit _T_ . Values present averages of ten runs per use case with a standard deviation below 1% in time acquisition and 5% in the optimization cycles. 

**20/20** 

