# Project milestones

This map contains exactly 30 understanding targets for Quantum Transport Precision. The first 14 milestones form the **background/preliminaries** phase. They progress from particle counts and individual orbitals to the complete transport model and the mathematical tools needed to analyze it. The remaining 16 form the **narrative/innovation** phase. They assemble the universal size converse, an exactly realizable attaining family, the contact-current constraint, and their physical meaning.

The 14/16 allocation reflects the project's connection between mesoscopic transport, polynomial approximation, and passive realization. Each phase ends with a synthesis milestone: [M14](#m14) integrates the model and resources; [M30](#m30) integrates the claims, attribution, scope, and evidence. The map identifies the load-bearing ideas needed for global understanding; specialist details remain in the canonical proofs.

The educational anchor is **Supriyo Datta, [Electronic Transport in Mesoscopic Systems](https://doi.org/10.1017/CBO9780511805776) (Cambridge University Press, 1995)**. The [Datta bridge](DATTA_BRIDGE.md) translates the anchor into this project's conventions and supplies the route to material developed locally. References to Datta below use the verified Ch. 2, Ch. 3, Ch. 6, Ch. 8, or Sec. 8.7 as appropriate. The count-statistics convention, approximation-theory arguments, realization proof, and resource theorems have explicit local and primary-research source pointers.

Every dependency names an earlier milestone. The records describe conceptual understanding, with distinct fields for the question, target, dependencies, story role, connection, and sources.

## Background/preliminaries: M01–M14

<a id="m01"></a>

### M01: Particle counts, mean current, and variance

**Phase:** background/preliminaries.

**Central question:** How can two particle streams have the same average output and different fluctuations?

**Understanding target:** Distinguish the random accumulated count $`K_t`$ from its mean and variance, and understand $`J=\lim_{t\to\infty}\mathbb E K_t/t`$ and $`D=\lim_{t\to\infty}\mathrm{Var}K_t/t`$ as different long-time properties. A statement about accumulated counts need not determine the distribution of individual waiting times.

**Dependencies:** None.

**Story role:** Establishes the measured output before introducing a microscopic device or an optimization criterion.

**Conceptual connection:** Connects repeated particle detection to the two observable rates that the transport theory must explain.

**Source pointers:** Local: [model, current and counting noise](../science/model.md#4-current-and-counting-noise) and [interpretation, correlated clocks](../science/interpretation.md#5-relation-to-correlated-clocks). Research attribution: [counting-statistics sources](../references/RELATED_WORK.md#counting-statistics).

<a id="m02"></a>

### M02: Fermions and a serial Hamiltonian

**Phase:** background/preliminaries.

**Central question:** What physical system is represented by a chain of fermionic orbitals?

**Understanding target:** Explain site occupation, fermionic exclusion, onsite energy, and coherent nearest-neighbor hopping in the noninteracting Hamiltonian. Distinguish the $`N\times N`$ single-particle matrix from the $`2^N`$-dimensional fermionic Fock space, and identify which of these resources the project counts.

**Dependencies:** M01.

**Story role:** Introduces the local degrees of freedom and the serial geometry that will later constrain transmission.

**Conceptual connection:** Connects a many-particle counting experiment to a coherent single-particle propagation problem without identifying their state spaces.

**Source pointers:** Datta: Ch. 3 for the coherent single-particle transport description. Local: [model, physical model](../science/model.md#1-physical-model) and [interpretation, resource counted](../science/interpretation.md#1-what-is-optimal). The finite fermionic Hamiltonian and orbital resource convention are specified locally.

<a id="m03"></a>

### M03: Full and empty reservoirs and physical contact rates

**Phase:** background/preliminaries.

**Central question:** How do the reservoirs drive the chain, and what does a contact rate measure?

**Understanding target:** Understand a full source and empty drain as occupation assumptions over the whole energy axis, with local, energy-independent endpoint couplings. Track the physical rates $`\Gamma_L,\Gamma_R`$ and their half-rate contributions to retarded damping, including the case in which both reservoirs couple to the same orbital.

**Dependencies:** M01, M02.

**Story role:** Fixes the environment, driving, and rate convention before any Green function or spectral width is used.

**Conceptual connection:** Connects irreversible exchange with reservoirs to the open-system terms in an otherwise coherent finite conductor.

**Source pointers:** Datta: Ch. 2 for reservoirs and transmission-based transport; Ch. 8 for the open transport framework. Local: [model, physical model](../science/model.md#1-physical-model) and [scattering convention](../science/model.md#2-scattering-convention). The exact full/empty Lindblad model and physical-rate normalization are supplied locally.

<a id="m04"></a>

### M04: Retarded Green functions and decaying resonances

**Phase:** background/preliminaries.

**Central question:** How does the open chain encode propagation from its source to its drain?

**Understanding target:** Interpret $`G(E)=(EI-H_{\mathrm{eff}})^{-1}`$ as the retarded propagation matrix, with $`H_{\mathrm{eff}}=H-i(\Gamma_L\Pi_L+\Gamma_R\Pi_R)/2`$. Relate its endpoint matrix element to transport and its lower-half-plane poles to decay, while keeping propagation amplitudes distinct from transmission probabilities.

**Dependencies:** M02, M03.

**Story role:** Provides the spectral language that connects the Hamiltonian to scattering, polynomial denominators, and contact-rate sums.

**Conceptual connection:** Connects finite-dimensional linear response and causal decay to measurable transmission through an open quantum device.

**Source pointers:** Datta: Ch. 3 and Ch. 8 for Green-function transport. Local: [model, scattering convention](../science/model.md#2-scattering-convention) and [contact-rate proof, root location](../science/contact_rate.md#location-and-sums-of-the-roots). The strict pole-location argument for this connected chain is local.

<a id="m05"></a>

### M05: The single-level resonance as a complete physical example

**Phase:** background/preliminaries.

**Central question:** What can one orbital already reveal about resonance width, contact asymmetry, and transmission?

**Understanding target:** Read the Lorentzian $`T(E)=\Gamma_L\Gamma_R/[(E-\epsilon)^2+(\Gamma_L+\Gamma_R)^2/4]`$ as the result of two contacts acting on one level. Explain why equal contacts allow unit peak transmission and why changing the total rate changes the width, so the physical rate and the half-width cannot be interchanged.

**Dependencies:** M03, M04.

**Story role:** Makes the conventions concrete in the smallest admissible device before introducing general two-port relations.

**Conceptual connection:** Connects a familiar resonance profile to the same endpoint damping and normalization used for every chain size.

**Source pointers:** Datta: Ch. 6, Double-barrier tunneling, for coherent resonant-transport context. Local: [contact-rate proof, one-site check](../science/contact_rate.md#one-site-check) and [realization, one-site check](../science/realization.md#8-one-site-check-and-numerical-scope).

<a id="m06"></a>

### M06: Two-port scattering and probability conservation

**Phase:** background/preliminaries.

**Central question:** How do transmission and reflection fit into a unitary description of the two reservoirs?

**Understanding target:** Understand $`\mathcal S=I_2-iV^\dagger GV`$, with contact amplitudes in $`V`$, as a map from incoming to outgoing port amplitudes. Explain how unitarity gives $`|r_L|^2+T=1`$ and $`0\leq T\leq1`$, even though the effective device Hamiltonian contains damping.

**Dependencies:** M03, M04, M05.

**Story role:** Turns an open-device propagator into a probability-conserving scattering description.

**Conceptual connection:** Connects loss of amplitude from the finite device to transfer into explicitly included reservoir channels.

**Source pointers:** Datta: Ch. 3, Transmission function, S-matrix and Green's functions. Local: [model, scattering convention](../science/model.md#2-scattering-convention) and [contact-rate proof, scattering and determinants](../science/contact_rate.md#transmission-and-reflection-determinants).

<a id="m07"></a>

### M07: The Landauer particle current

**Phase:** background/preliminaries.

**Central question:** How does an energy-dependent transmission probability determine the mean particle flux?

**Understanding target:** Explain the occupation-weighted Landauer integral and its full-source, empty-drain reduction $`J=(2\pi)^{-1}\int_{\mathbb R}T(E)\,dE`$ when $`\hbar=1`$. Distinguish particle current from electrical current and transmission at one energy from the energy-integrated throughput.

**Dependencies:** M01, M03, M06.

**Story role:** Connects the spectral description to the first measured counting rate.

**Conceptual connection:** Connects the number of occupied incoming modes, their transmission probabilities, and the mean rate of detected particles.

**Source pointers:** Datta: Ch. 2, Conductance from transmission, and Sec. 8.7 for the connection between noninteracting Green-function and Landauer descriptions. Local: [model, current and counting noise](../science/model.md#4-current-and-counting-noise).

<a id="m08"></a>

### M08: Partition noise and the Fano factor

**Phase:** background/preliminaries.

**Central question:** Why does nearly deterministic transmission reduce counting fluctuations relative to current?

**Understanding target:** Define $`I_0=\int T\,dE`$ and $`V_0=\int T(1-T)\,dE`$, and understand the full-bias variance rate $`D=V_0/(2\pi)`$ and dimensionless ratio $`F=D/J=V_0/I_0`$. Relate the factor $`T(1-T)`$ to partition uncertainty, and distinguish the count-variance rate from conventions for electrical noise spectral density. The ratio requires positive current.

**Dependencies:** M01, M06, M07.

**Story role:** Defines the precision observable that the size and contact theorems constrain.

**Conceptual connection:** Connects energy-resolved transmission uncertainty to a long-time fluctuation measure normalized by useful output.

**Source pointers:** Local: [model, current and counting noise](../science/model.md#4-current-and-counting-noise) and [interpretation, nearly perfect transmission](../science/interpretation.md#2-why-nearly-perfect-transmission-reduces-noise). Research attribution: [counting-statistics formulas and noise conventions](../references/RELATED_WORK.md#counting-statistics). These fluctuation formulas are supplied through the project and its primary sources.

<a id="m09"></a>

### M09: The serial cofactor and all-pole transmission

**Phase:** background/preliminaries.

**Central question:** Why does serial nearest-neighbor geometry impose a special algebraic form on transmission?

**Understanding target:** Explain why the endpoint cofactor is the energy-independent product of the nonzero hoppings, giving $`T=C/|\chi_N|^2`$ with $`C>0`$ and a degree-$`N`$ characteristic determinant. Understand why an extra path or side branch can change the numerator and therefore the later degree argument.

**Dependencies:** M02, M04, M06.

**Story role:** Identifies the geometric property that makes a universal site-count converse possible.

**Conceptual connection:** Connects the unique path through a Jacobi matrix to a constant-numerator spectral filter.

**Source pointers:** Datta: Ch. 3 for the Green-function route to transmission. Local: [model, serial geometry](../science/model.md#3-why-serial-geometry-matters) and [size proof, polynomial constraint](../science/size_bound.md#the-polynomial-constraint). Research context: [quantum-dot filters](../references/RELATED_WORK.md#ehrlich2021).

<a id="m10"></a>

### M10: Polynomial degree and limits on spectral variation

**Phase:** background/preliminaries.

**Central question:** What does a fixed polynomial degree prevent a transmission denominator from doing?

**Understanding target:** Understand Markov's derivative inequality $`\|u'\|_{[-1,1]}\leq m^2\|u\|_{[-1,1]}`$ and how its scale changes on an interval of length $`\ell`$. Relate the degree to a limit on how rapidly a bounded polynomial can vary near an interval endpoint, while keeping this classical approximation-theory statement separate from the physical dynamics.

**Dependencies:** M09.

**Story role:** Supplies the mathematical obstruction that will be converted into a noise lower bound.

**Conceptual connection:** Connects a finite number of serial orbitals to the sharpness of possible spectral transitions.

**Source pointers:** Local: [size proof, interval derivative estimate](../science/size_bound.md#a-derivative-bound-on-each-conducting-interval). Primary attribution: [A. A. Markov's inequality](../references/RELATED_WORK.md#markov). This mathematical ingredient is supplied locally.

<a id="m11"></a>

### M11: Legendre orthogonality and endpoint normalization

**Phase:** background/preliminaries.

**Central question:** How can orthogonal polynomials organize a low-reflection profile with a fixed endpoint value?

**Understanding target:** Understand the normalization $`P_m(1)=1`$, Legendre orthogonality, parity, and the normalized derivative $`p_N=2P'_{N+1}/[(N+1)(N+2)]`$. Explain why fixing an endpoint value removes a trivial amplitude rescaling and why an integrated square is a useful measure of passband reflection.

**Dependencies:** M08, M10.

**Story role:** Introduces the polynomial vocabulary needed for the explicit family after the universal obstruction is established.

**Conceptual connection:** Connects orthogonal expansions and boundary normalization to a controlled distribution of reflection across an energy interval.

**Source pointers:** Local: [Legendre family, definition and kernel](../science/legendre_family.md#1-definition-and-classical-least-squares-characterization). Primary attribution: [Malvar and Calôba's least-squares family](../references/RELATED_WORK.md#malvar1980). Orthogonal-polynomial details are supplied locally.

<a id="m12"></a>

### M12: Stable factors, Cayley transforms, and passivity

**Phase:** background/preliminaries.

**Central question:** How can a real transmission profile become a causal, probability-conserving scattering object?

**Understanding target:** Distinguish the positive real-axis polynomial $`1+p^2`$ from a stable factor $`d`$ whose roots lie in the lower half-plane and satisfy $`dd^\#=1+p^2`$. Understand the role of a rational inner scattering matrix and why its Cayley transform carries the analytic sign condition associated with a passive finite system.

**Dependencies:** M04, M06, M10.

**Story role:** Provides the analytic language for constructing a physical device from a desired filter.

**Conceptual connection:** Connects spectral magnitude, causal analyticity, and a positive-residue representation of internal modes.

**Source pointers:** Local: [realization, stable factor](../science/realization.md#2-stable-spectral-factor-including-multiplicities) and [rational inner scattering matrix](../science/realization.md#3-a-rational-inner-scattering-matrix). Research attribution: [classical synthesis ingredients](../references/RELATED_WORK.md#synthesis). The factorization and Cayley arguments are supplied locally.

<a id="m13"></a>

### M13: Spectral measures, Krylov spaces, and Jacobi chains

**Phase:** background/preliminaries.

**Central question:** When can internal modes be represented as a connected nearest-neighbor chain?

**Understanding target:** Understand a contact spectral measure as mode energies with nonnegative coupling weights, and a cyclic source vector as one whose Hamiltonian powers span every mode. Explain how Lanczos orthogonalization produces a Jacobi matrix with positive hoppings, while recognizing that locating a second contact at the opposite endpoint requires additional moment information.

**Dependencies:** M02, M04, M12.

**Story role:** Introduces the bridge from an abstract passive realization to the geometry and site count used by the theorem.

**Conceptual connection:** Connects a change of basis, orthogonal polynomials, and physically localized endpoint couplings.

**Source pointers:** Local: [realization, residues](../science/realization.md#4-exactly-n-real-cayley-poles-and-positive-rank-one-residues) and [Lanczos reduction](../science/realization.md#5-lanczos-reduction-puts-the-two-contacts-at-opposite-endpoints). Research attribution: [spectral measures and Jacobi matrices](../references/RELATED_WORK.md#synthesis).

<a id="m14"></a>

### M14: The integrated model, counted resources, and ordered limits

**Phase:** background/preliminaries.

**Central question:** What complete physical and mathematical problem do the two resource laws address?

**Understanding target:** Connect particle counts, the serial fermionic Hamiltonian, endpoint damping, scattering, and the current/noise integrals into one model. Identify $`N`$, contact rates, and current as distinct resources; explain why a common energy rescaling preserves $`F`$ but changes speed. State the order of limits: define the long-time rates at each finite $`N`$ before studying large $`N`$.

**Dependencies:** M01, M02, M03, M04, M05, M06, M07, M08, M09, M10, M11, M12, M13.

**Story role:** Completes the background phase by integrating the physical setup and mathematical tools into a precise optimization problem.

**Conceptual connection:** Connects the prerequisite representations to the project's two questions: the best precision allowed by serial size and the current compatible with that precision at fixed contacts.

**Source pointers:** Datta: Ch. 2, Ch. 3, and Sec. 8.7 for the coherent transport framework. Local: [model and exact claims](../science/model.md), [scientific proof dependencies](../science/README.md#proof-dependencies), and [interpretation and scope](../science/interpretation.md).

## Narrative/innovation: M15–M30

<a id="m15"></a>

### M15: Transmission becomes a nonnegative degree constraint

**Phase:** narrative/innovation.

**Central question:** How can every admissible chain be represented by the same kind of polynomial object?

**Understanding target:** Understand $`q=T^{-1}-1=|\chi_N|^2/C-1`$ as a globally nonnegative real polynomial of degree $`2N`$. Interpret $`T=1/(1+q)`$ and $`T(1-T)=q/(1+q)^2`$ as the translation of useful transmission and noise into functions of that common object.

**Dependencies:** M08, M09, M10, M14.

**Story role:** Starts the research narrative with a reduction that applies to every chain in the optimization domain.

**Conceptual connection:** Connects serial geometry and unitarity to a constrained polynomial, making an approximation-theory argument relevant to transport.

**Source pointers:** Local: [size proof, polynomial constraint](../science/size_bound.md#the-polynomial-constraint) and [model, serial geometry](../science/model.md#3-why-serial-geometry-matters).

<a id="m16"></a>

### M16: Conducting regions and their total width

**Phase:** narrative/innovation.

**Central question:** How can a converse treat one broad transmission band and many separated bands on equal terms?

**Understanding target:** Understand the compact set $`\{q\leq1\}=\{T\geq1/2\}`$ as finitely many conducting intervals, possibly with isolated points, and let $`L`$ denote their total length. Explain why each nondegenerate component has $`q=1`$ at both endpoints and why its length, rather than a simple-root assumption or a chosen band shape, is the useful quantity.

**Dependencies:** M10, M15.

**Story role:** Organizes arbitrary spectral shapes into components on which the same local argument can be applied and then summed.

**Conceptual connection:** Connects level-set geometry to a total conducting width that can later be compared with integrated current.

**Source pointers:** Local: [size proof, conducting intervals and degeneracies](../science/size_bound.md#a-derivative-bound-on-each-conducting-interval).

<a id="m17"></a>

### M17: A degree limit forces noisy boundary regions

**Phase:** narrative/innovation.

**Central question:** Why must every conducting interval contain a definite amount of partition noise?

**Understanding target:** Explain how applying Markov's inequality to $`q-1/2`$ limits the slope on an interval of length $`\ell`$, forcing endpoint strips with $`1/2\leq q\leq1`$. Understand why these strips occupy a fraction of order $`N^{-2}`$ of that interval and carry a noise density bounded away from zero.

**Dependencies:** M10, M15, M16.

**Story role:** Identifies the physical mechanism of the lower bound: finite polynomial degree prevents arbitrarily narrow noisy transitions.

**Conceptual connection:** Connects an endpoint derivative inequality to a lower bound on integrated fluctuations, component by component.

**Source pointers:** Local: [size proof, derivative estimate](../science/size_bound.md#a-derivative-bound-on-each-conducting-interval) and [noise in each interval](../science/size_bound.md#every-conducting-interval-contributes-noise). Primary ingredient: [Markov](../references/RELATED_WORK.md#markov).

<a id="m18"></a>

### M18: The universal Fano-factor converse

**Phase:** narrative/innovation.

**Central question:** How does unavoidable noise in conducting regions constrain the full energy-integrated ratio?

**Understanding target:** Explain why the complement, where $`T<1/2`$, contributes at least half as much noise as current, giving $`I_0\leq L+2V_0`$. Combine this with the conducting-width estimate to understand $`F\geq1/(18N^2+2)`$ for arbitrary admissible onsite energies, hoppings, and contacts, including spectra with no interval above half transmission.

**Dependencies:** M08, M16, M17.

**Story role:** Closes the universal-converse branch by joining local spectral restrictions to the global measured observable.

**Conceptual connection:** Connects high-transmission boundary noise and low-transmission inefficiency into one lower bound that cannot be evaded by redistributing spectral weight.

**Source pointers:** Local: [size proof, width and total current](../science/size_bound.md#from-conducting-width-to-total-current) and [scope](../science/size_bound.md#scope-of-the-result).

<a id="m19"></a>

### M19: The inherited least-squares kernel as a constructive choice

**Phase:** narrative/innovation.

**Central question:** Why does the normalized Legendre derivative provide a natural low-reflection candidate?

**Understanding target:** Understand the endpoint reproducing kernel in the fixed-parity Legendre space and its unique least-squares minimizer $`p_N`$, with $`\int_{-1}^1p_N^2=4/[(N+1)(N+2)]`$. Distinguish this inherited quadratic optimization from minimizing the nonlinear full-line Fano ratio over physical conductors.

**Dependencies:** M11, M18.

**Story role:** Introduces an attributed candidate for attaining the converse order without asserting that it solves the exact finite-size optimization.

**Conceptual connection:** Connects endpoint-constrained approximation to a small integrated reflection proxy in the passband.

**Source pointers:** Local: [Legendre family, least-squares characterization](../science/legendre_family.md#1-definition-and-classical-least-squares-characterization). Primary attribution: [Malvar and Calôba](../references/RELATED_WORK.md#malvar1980).

<a id="m20"></a>

### M20: Passband and tail control give the constructive noise order

**Phase:** narrative/innovation.

**Central question:** Why is small passband reflection sufficient only after the exterior transmission is also controlled?

**Understanding target:** Explain how the Legendre norm bounds passband noise and lost current, while positive Taylor coefficients at the endpoint control both exterior tails. Understand the resulting $`F_N=O(N^{-2})`$ and $`I_{0,N}=2+O(N^{-2})`$ as statements about a specified transmission profile whose physical realization must also be established.

**Dependencies:** M08, M19.

**Story role:** Shows that the candidate has the required full-line transport performance, including energy regions outside the nominal passband.

**Conceptual connection:** Connects a classical least-squares objective to the actual current-normalized partition noise through separate passband and tail estimates.

**Source pointers:** Local: [Legendre family, finite-size Fano bound](../science/legendre_family.md#2-a-finite-size-upper-bound-on-the-fano-factor).

<a id="m21"></a>

### M21: From a stable factor to an inner scattering matrix

**Phase:** narrative/innovation.

**Central question:** How can the candidate transmission be embedded in a causal two-port scattering law?

**Understanding target:** Understand the lower-half-plane spectral factor of $`1+p_N^2`$ and the matrix $`S=d^{-1}\begin{pmatrix}p_N&i\\ i&p_N\end{pmatrix}`$. Explain why it is unitary on the real axis, contractive in the upper half-plane, and has exactly the desired transmission modulus, while allowing repeated stable-factor roots.

**Dependencies:** M06, M12, M19, M20.

**Story role:** Begins the physical-attainment argument by placing the mathematical profile inside a passive scattering construction.

**Conceptual connection:** Connects filter magnitude to a complete amplitude-level description whose analyticity constrains possible internal realizations.

**Source pointers:** Local: [realization, stable spectral factor](../science/realization.md#2-stable-spectral-factor-including-multiplicities) and [inner scattering matrix](../science/realization.md#3-a-rational-inner-scattering-matrix). Research attribution: [synthesis](../references/RELATED_WORK.md#synthesis).

<a id="m22"></a>

### M22: Cayley poles certify positive finite-mode structure

**Phase:** narrative/innovation.

**Central question:** Why does the passive scattering construction contain exactly the required number of internal modes?

**Understanding target:** Explain how the Cayley transform's sign condition forces simple real poles and positive-semidefinite residues. Understand why its nonzero off-diagonal numerator prevents pole cancellation, so the degree-$`N`$ denominator gives exactly $`N`$ poles, and why the spectral-factor identity makes each residue rank one with a strictly positive coupling weight.

**Dependencies:** M12, M21.

**Story role:** Certifies a finite positive realization and rules out an uncounted enlargement of the internal mode space.

**Conceptual connection:** Connects analytic passivity and polynomial degree to the mode count and positive contact spectral weights.

**Source pointers:** Local: [realization, real poles and positive residues](../science/realization.md#4-exactly-n-real-cayley-poles-and-positive-rank-one-residues).

<a id="m23"></a>

### M23: Cyclic Lanczos reduction gives exactly N sites and endpoint contacts

**Phase:** narrative/innovation.

**Central question:** What makes the passive mode realization an admissible serial quantum chain?

**Understanding target:** Understand why positive weights at distinct real mode energies make the source cyclic, producing a full $`N`$-site Jacobi matrix with nonzero hoppings. Explain how the vanishing low-order source-drain cross moments place the drain at the final Lanczos site, so both geometry and exact site count are certified.

**Dependencies:** M13, M22.

**Story role:** Completes the passage from a passive scattering object to the precise physical architecture counted by the size theorem.

**Conceptual connection:** Connects source reachability, orthogonalization, and cross-moment cancellation to a connected nearest-neighbor chain with local contacts.

**Source pointers:** Local: [realization, Lanczos and endpoint support](../science/realization.md#5-lanczos-reduction-puts-the-two-contacts-at-opposite-endpoints).

<a id="m24"></a>

### M24: Symmetry, physical rates, and attained size order

**Phase:** narrative/innovation.

**Central question:** Which physical properties does the constructed chain have, and what theorem does its existence complete?

**Understanding target:** Explain how parity gives zero onsite energies and equal endpoint spectral measures give mirror symmetry. For the passive realization's contact vectors $`b_\alpha`$, track $`\Gamma_\alpha=2\|b_\alpha\|^2`$ and the equal physical rates determined by the stable poles. Combine the admissible realization with the profile upper bound and universal converse to obtain $`\inf F=\Theta(N^{-2})`$, while leaving optimal constants and the exact finite-size minimizer open.

**Dependencies:** M05, M14, M18, M20, M23.

**Story role:** Integrates the converse, inherited filter, and exact geometry into the completed size-law claim.

**Conceptual connection:** Connects mathematical attainment to finite physical couplings and makes explicit that these rates must be charged in the next part of the argument.

**Source pointers:** Local: [realization, symmetry](../science/realization.md#6-zero-onsite-energies-and-mirror-symmetry), [physical contact rate](../science/realization.md#7-spectral-sum-and-the-physical-contact-rate), and [Legendre family, size bound](../science/legendre_family.md#2-a-finite-size-upper-bound-on-the-fano-factor).

<a id="m25"></a>

### M25: Reflection determinants and the logarithmic root identity

**Phase:** narrative/innovation.

**Central question:** How does integrated reflection suppression reveal the spectral cost of a conductor?

**Understanding target:** Understand $`r_L=Q_L/\chi_N`$ and the matching area $`\mathcal A=\int-\log(1-T)\,dE`$ as a difference of logarithmic root potentials. Explain why the absolute imaginary parts of poles and reflection zeros enter with opposite signs, why real reflection zeros cause integrable singularities, and why the complete polynomial ratio has a convergent integral.

**Dependencies:** M04, M06, M09, M12, M24.

**Story role:** Opens the contact-resource branch with an exact identity valid beyond the particular attaining family.

**Conceptual connection:** Connects the broad-band suppression of reflection to the linewidth sum of the physical damped Hamiltonian.

**Source pointers:** Local: [contact-rate proof, determinants](../science/contact_rate.md#transmission-and-reflection-determinants), [root-integral lemma](../science/contact_rate.md#a-logarithmic-root-integral-lemma), and [exact reflection integral](../science/contact_rate.md#exact-reflection-integral-and-the-asymmetric-bound). Classical attribution: [Bode and Fano](../references/RELATED_WORK.md#bode).

<a id="m26"></a>

### M26: The asymmetric contact budget and transmission-weighted convexity

**Phase:** narrative/innovation.

**Central question:** How can a spectral reflection budget become a bound on measured current and Fano factor?

**Understanding target:** Explain why the trace of the reflection roots sharpens the area bound to $`\mathcal A\leq2\pi\Gamma_{\min}`$, where $`\Gamma_{\min}=\min(\Gamma_L,\Gamma_R)`$. Understand the probability measure $`T(E)dE/I_0`$, under which $`1-T`$ has mean $`F`$, and the convex function $`-\log x/(1-x)`$ that yields $`J\log(1/F)/(1-F)\leq\Gamma_{\min}`$.

**Dependencies:** M07, M08, M25.

**Story role:** Converts the classical logarithmic-reflection method into the project's observable current-noise constraint.

**Conceptual connection:** Connects asymmetric reservoir coupling, the distribution of actually transmitted particles over energy, and a universal throughput cost of precision.

**Source pointers:** Local: [contact-rate proof, asymmetric area bound](../science/contact_rate.md#exact-reflection-integral-and-the-asymmetric-bound), [weighted Jensen step](../science/contact_rate.md#converting-reflection-into-a-fano-factor-bound), and [resource consequences](../science/contact_rate.md#consequences-for-physical-resources).

<a id="m27"></a>

### M27: Sturm and Poincare control of angular root spacing

**Phase:** narrative/innovation.

**Central question:** How can the Legendre reflection roots be controlled uniformly across the entire passband?

**Understanding target:** Understand the angular substitution $`x=\cos\theta`$ and the transformed Jacobi equation as a way to bound every nodal gap by a Dirichlet Poincare argument. Explain why the singular endpoints still permit integration by parts and how the resulting angular grid estimate controls all roots, including those near the band edges.

**Dependencies:** M11, M19, M25.

**Story role:** Supplies the global root-distribution control needed to compute the attaining family's contact cost.

**Conceptual connection:** Connects an orthogonal-polynomial differential equation to a uniform spectral estimate with bounded accumulated error.

**Source pointers:** Local: [Legendre family, root-spacing estimate](../science/legendre_family.md#4-a-self-contained-root-spacing-estimate). The Sturm, endpoint-integrability, and Poincare steps are supplied in that proof.

<a id="m28"></a>

### M28: Logarithmic potentials determine the contact-rate asymptotic

**Phase:** narrative/innovation.

**Central question:** Why does the attaining family's contact rate grow logarithmically with the number of sites?

**Understanding target:** Understand how the leading coefficient of $`p_N`$ and the sum of its root potentials cancel their terms proportional to $`N`$, leaving $`\int_{-1}^1\log|p_N|=-3\log N+O(1)`$. Connect the controlled tails and real reflection zeros to $`\mathcal A_N=6\log N+O(1)`$ and the physical rate $`\Gamma_N=(3/\pi)\log N+O(1)`$.

**Dependencies:** M20, M24, M25, M27.

**Story role:** Evaluates the actual contact resource of the constructed chain rather than inferring it from a fixed passband current.

**Conceptual connection:** Connects root distribution, logarithmic matching area, and the physically normalized damping sum.

**Source pointers:** Local: [Legendre family, matching area](../science/legendre_family.md#3-the-matching-area-determines-the-contact-rate), [logarithmic asymptotic](../science/legendre_family.md#5-logarithmic-asymptotic-of-the-matching-area), and [realization, rate normalization](../science/realization.md#7-spectral-sum-and-the-physical-contact-rate).

<a id="m29"></a>

### M29: Fixed-contact throughput and calibrated elapsed time

**Phase:** narrative/innovation.

**Central question:** What precision is obtained when the contact strength is fixed and the output is used to estimate elapsed time?

**Understanding target:** Compare fixed-passband and fixed-contact normalizations, using $`J_N/\Gamma\sim1/(3\log N)`$ after rescaling to equal fixed contacts. For the calibrated estimate $`\widehat t=K_t/J`$, understand $`\mathrm{Var}\widehat t=(F/J)t+o(t)`$ and the constructed coefficient $`F_N/J_N=\Theta(\log N/(\Gamma N^2))`$. Keep the finite-size long-time limit distinct from a size-uniform transient claim.

**Dependencies:** M01, M08, M14, M26, M28.

**Story role:** Combines the precision and throughput laws into their physical and timing interpretation.

**Conceptual connection:** Connects relative count fluctuations to an absolute elapsed-time variance coefficient while accounting for the rate cost of producing the counts.

**Source pointers:** Local: [Legendre family, fixed-contact throughput](../science/legendre_family.md#6-charged-throughput-and-limits-of-the-conclusion), [interpretation, contact budget](../science/interpretation.md#3-the-contact-budget-per-transmitted-particle), and [calibrated elapsed-time estimate](../science/interpretation.md#5-relation-to-correlated-clocks).

<a id="m30"></a>

### M30: Global synthesis: optimal order, physical scope, attribution, and evidence

**Phase:** narrative/innovation.

**Central question:** What is established by the complete project, what supplies its proof, and where do its conclusions stop?

**Understanding target:** Explain the combined result: optimal $`N^{-2}`$ Fano order for the stated serial class, an exact physical attaining family, a universal contact-current constraint, and an attained logarithmic throughput cost in order. Distinguish inherited transport, filter, polynomial, and synthesis ingredients from the conclusions assembled here; separate analytical proof from finite floating-point checks. Identify the unresolved constants, the unanalysed sensitivity to control errors, and the limits involving finite bias, general networks, interactions, and transient convergence.

**Dependencies:** M14, M18, M24, M26, M28, M29.

**Story role:** Completes the narrative phase by integrating all proof branches into a calibrated account of the scientific contribution.

**Conceptual connection:** Connects local mechanisms and mathematical certificates to the global claim, its observable meaning, its resource accounting, and the strength of its supporting evidence.

**Source pointers:** Local: [scientific reading map](../science/README.md), [exact claims](../science/model.md#5-main-statements), [interpretation](../science/interpretation.md), and [verification guide](../verification/README.md). Attribution and comparison: [related work](../references/RELATED_WORK.md).

Return to the [learning overview](README.md) or the [scientific reading map](../science/README.md).

