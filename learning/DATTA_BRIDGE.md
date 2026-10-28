# From Datta's transport framework to the precision bounds

The textbook anchor is **Supriyo Datta, *Electronic Transport in Mesoscopic Systems*, Cambridge University Press, 1995**: [official book and chapter listing](https://www.cambridge.org/core/books/electronic-transport-in-mesoscopic-systems/1E55DEF5978AA7B843FF70337C220D8B/listing), [book DOI](https://doi.org/10.1017/CBO9780511805776). Cambridge records the print publication as 14 September 1995 and the online publication as 5 June 2013. The latter date does not identify a different edition.

The connection is a chain of physical and mathematical descriptions. A finite Hamiltonian determines a retarded Green function; the Green function determines transmission; transmission determines the mean current and its counting fluctuations. Serial geometry then constrains the transmission strongly enough to prove a size-dependent noise bound. Passive synthesis constructs a chain attaining that bound in order, while a reflection sum rule accounts for the required contact strength.

## 1. Where the textbook connects

The chapter titles and page ranges below are verified against the [publisher's contents](https://www.cambridge.org/core/books/abs/electronic-transport-in-mesoscopic-systems/contents/92727F4AAC4758D4EA351BE023399646) and chapter listing. The final column describes this project's connection to that background.

| Datta, 1995 edition | Pages | Connection to this project |
|---|---:|---|
| Chapter 2, Conductance from transmission | 48–116 | Convert an energy-dependent transmission probability into a mean current. |
| Chapter 3, Transmission function, S-matrix and Green's functions | 117–174 | Calculate transmission from a finite Hamiltonian and its contacts. |
| Chapter 6, Double-barrier tunneling | 246–275 | Interpret the single resonant orbital before extending to several coupled orbitals. |
| Chapter 8, Non-equilibrium Green's function formalism | 293–342 | Connect the reservoir and Green-function descriptions. The publisher explicitly identifies §8.7 as the connection to Landauer–Büttiker transport. |

The counting-variance formula and the approximation and synthesis arguments are supplied below and in the linked project proofs. Their primary-source attribution is in [related work](../references/RELATED_WORK.md). These references support the research statements; Datta remains the textbook anchor.

<a id="notation"></a>

## 2. Notation, units, and the precise model

For one spin-resolved transport channel, restoring physical constants gives the particle and electrical currents

```math
J=\frac1h\int T(E)[f_L(E)-f_R(E)]\,dE,
\qquad
I=eJ,
\qquad h=2\pi\hbar.
```

Here $`e>0`$ is the charge magnitude and the current orientation follows particle transfer from source to drain. A spin-degeneracy factor sometimes included in a transport formula is not implicit here: this model has one fermionic orbital per site and one channel at each contact.

| Quantity | Convention used here |
|---|---|
| $`H`$ | The $`N\times N`$ single-particle Hamiltonian. Its entries have energy units. |
| $`T(E)`$ | A dimensionless transmission probability between zero and one. |
| $`\Gamma_\alpha`$ | A physical particle exchange rate, numerically also an energy because $`\hbar=1`$. With units restored, the corresponding energy broadening is $`\hbar\Gamma_\alpha`$. |
| $`J`$ | Mean number of transferred particles per unit time. |
| $`D`$ | Long-time particle-count variance per unit time. |
| $`F=D/J`$ | A dimensionless Fano factor. |
| $`S(0)`$ | Under the symmetrized electrical-noise convention used for comparison, $`S(0)=2e^2D`$ and $`F=S(0)/(2eI)`$. |

The Hamiltonian is a connected nearest-neighbor chain:

```math
H=\sum_{j=1}^N\epsilon_j|j\rangle\langle j|
+\sum_{j=1}^{N-1}t_j
\bigl(|j\rangle\langle j+1|+|j+1\rangle\langle j|\bigr),
\qquad t_j>0.
```

The model is noninteracting, with no internal dephasing or additional terminals. The source couples only to site 1 and the drain only to site $`N`$. Two separate idealizations matter. **Wide band** means the contact couplings are independent of energy; a constant real energy shift can be included in $`H`$. **Full source and empty drain** mean $`f_L(E)=1`$ and $`f_R(E)=0`$ over the entire real axis. Wide band alone does not imply those occupations. Finite voltage windows and thermal occupations require different weights in both current and noise.

With $`\hbar=1`$, the retarded Green function is

```math
G(E)=\left[
EI-H+\frac i2\bigl(\Gamma_L|1\rangle\langle1|
+\Gamma_R|N\rangle\langle N|\bigr)
\right]^{-1},
\qquad
T(E)=\Gamma_L\Gamma_R|G_{N1}(E)|^2.
```

Each contact contributes its half-rate to the retarded damping. For one orbital, both contributions act on the same matrix entry. The equivalent full/empty reservoir master equation has jump operators $`\sqrt{\Gamma_L}c_1^\dagger`$ and $`\sqrt{\Gamma_R}c_N`$, where $`c_j`$ annihilates a fermion. The many-body space has dimension $`2^N`$; the size resource in the theorem is the number $`N`$ of orbitals. These assumptions are collected in [model.md](../science/model.md).

<a id="counting"></a>

## 3. Transmission determines two different integrals

Let $`K_t`$ count particles entering the drain during a stationary observation of duration $`t`$. The long-time definitions are

```math
J=\lim_{t\to\infty}\frac{\mathbb E K_t}{t},
\qquad
D=\lim_{t\to\infty}\frac{\operatorname{Var}K_t}{t}.
```

For each occupied incoming energy mode, transmission has a Bernoulli contribution: its mean is $`T`$ and its variance is $`T(1-T)`$. Fermionic full counting statistics combines these contributions into the established generator

```math
\psi(s)=\lim_{t\to\infty}\frac1t\log\mathbb E e^{sK_t}
=\frac1{2\pi}\int_{\mathbb R}
\log[1+T(E)(e^s-1)]\,dE.
```

Differentiating at $`s=0`$ gives

```math
I_0=\int T(E)\,dE,\qquad
V_0=\int T(E)[1-T(E)]\,dE,
```

```math
J=\frac{I_0}{2\pi},\qquad
D=\frac{V_0}{2\pi},\qquad
F=\frac{V_0}{I_0}.
```

Thus current measures transmitted spectral area. Noise measures that area multiplied by the probability of reflection. Energies with $`T\simeq1`$ carry substantial current with little partition noise; energies with small $`T`$ carry little current but almost Poissonian noise per transmitted particle. The desired shape is consequently close to one over a useful interval and close to zero elsewhere. The transitions and tails matter.

This energy-mode statement does not assume independent waiting times between drain detections. Removing one fermion need not reset the remaining chain state, so consecutive detections can retain correlations. The formulas concern the long-time cumulants of the complete process. The limit $`t\to\infty`$ is taken at each finite $`N`$ before examining the size asymptotic. See the [counting-statistics sources](../references/RELATED_WORK.md#counting-statistics) for the established framework.

<a id="single-orbital"></a>
<a id="one-orbital"></a>

## 4. A complete single-orbital calculation

Put the orbital energy at zero and choose equal physical rates $`\Gamma_L=\Gamma_R=\Gamma`$. The two half-rates add, so

```math
G(E)=\frac1{E+i\Gamma},
\qquad
T(E)=\frac{\Gamma^2}{E^2+\Gamma^2}.
```

The resonance has $`T(0)=1`$. To calculate the current, set $`x=E/\Gamma`$:

```math
I_0=\Gamma\int_{-\infty}^{\infty}\frac{dx}{1+x^2}
=\pi\Gamma.
```

For the noise, use $`V_0=I_0-\int T^2`$. The substitution $`x=\tan\theta`$ gives

```math
\int T(E)^2\,dE
=\Gamma\int_{-\pi/2}^{\pi/2}\cos^2\theta\,d\theta
=\frac{\pi\Gamma}{2}.
```

Therefore

```math
\boxed{
J=\frac\Gamma2,\qquad
D=\frac\Gamma4,\qquad
F=\frac12.
}
```

The mean also has a direct occupation check. If $`n`$ is the mean orbital occupation, injection and removal give $`\dot n=\Gamma(1-n)-\Gamma n`$. Stationarity gives $`n=1/2`$, and the drain rate is $`\Gamma n=\Gamma/2`$. This equation checks the mean; it does not determine the counting variance by itself.

Perfect transmission at one energy does not remove noise from the partially transmitting energies around it. Relative to a Poisson count process of the same mean rate, whose variance rate would be $`D=J`$, this orbital has half the noise. In electrical units, $`I=e\Gamma/2`$ and $`S(0)=e^2\Gamma/2`$, again giving $`S(0)/(2eI)=1/2`$.

Increasing $`\Gamma`$ widens the resonance and raises both $`J`$ and $`D`$ proportionally. It leaves $`F`$ unchanged. This distinguishes changing an overall time scale from improving the transmission shape.

<a id="serial-polynomial"></a>

## 5. The serial geometry becomes a polynomial restriction

Define the damped characteristic polynomial

```math
\chi_N(z)=\det\left[zI-H+
\frac i2(\Gamma_L|1\rangle\langle1|
+\Gamma_R|N\rangle\langle N|)\right].
```

An inverse matrix entry is a cofactor divided by its determinant. In a tridiagonal chain, the cofactor joining the two endpoints contains the unique path across the chain: the product $`\prod_{j=1}^{N-1}t_j`$. It contains no energy variable. Consequently,

```math
T(E)=\frac{C}{|\chi_N(E)|^2},
\qquad
C=\Gamma_L\Gamma_R\prod_{j=1}^{N-1}t_j^2>0.
```

For $`N=1`$, the empty product equals one. Since $`\chi_N`$ has degree $`N`$ and unitarity gives $`T\le1`$,

```math
q(E)=\frac{|\chi_N(E)|^2}{C}-1
```

is a nonnegative real polynomial of degree $`2N`$. Both observables are now functions of that single polynomial:

```math
T=\frac1{1+q},
\qquad
T(1-T)=\frac{q}{(1+q)^2}.
```

This is the step that turns the number of physical orbitals into a mathematical constraint. It also fixes the scope: a side branch or parallel coherent path can produce an energy-dependent numerator. The same polynomial argument would then require modification.

<a id="converse"></a>

## 6. Why finite degree forces noise

Consider a nondegenerate connected component of $`\{E:q(E)\le1\}`$, equivalently $`\{E:T(E)\ge1/2\}`$. It is a closed interval of length $`\ell>0`$. Maximality and continuity give $`q=1`$ at both endpoints. Markov's classical derivative inequality, applied to $`q-1/2`$ and rescaled to this interval, gives

```math
|q'|\le\frac{m^2}{\ell},\qquad m=2N.
```

The polynomial therefore cannot drop from one to below one half immediately. The two endpoint strips have total length $`\ell/m^2`$ on which $`1/2\le q\le1`$. There the noise density satisfies $`q/(1+q)^2\ge2/9`$.

Let $`L`$ be the total length of all such conducting intervals. Their contributions add, even if transmission has several separated bands:

```math
V_0\ge\frac{2L}{9m^2}.
```

Inside those intervals, transmitted area is at most $`L`$. Outside them, $`T<1/2`$, so $`T\le2T(1-T)`$. Hence

```math
I_0\le L+2V_0
\le\left(\frac{9m^2}{2}+2\right)V_0,
```

which proves

```math
\boxed{F\ge\frac1{18N^2+2}.}
```

The argument charges both sharp transitions and weakly transmitting tails. No assumption of a single symmetric passband enters the converse. The [complete proof](../science/size_bound.md) treats isolated level-set points and degenerate roots as well. The [Markov inequality](../references/RELATED_WORK.md#markov) is inherited; its conversion into this integrated noise bound is the project argument.

<a id="legendre"></a>

## 7. An inherited filter attains the quadratic order

For the upper construction, let $`P_k`$ denote the Legendre polynomial normalized by $`P_k(1)=1`$, and define

```math
p_N(x)=\frac{2P'_{N+1}(x)}{(N+1)(N+2)},
\qquad
T_N(x)=\frac1{1+p_N(x)^2}.
```

This is Malvar and Calôba's classical $`Q_N^a`$ least-squares filter in Legendre notation, with the filter parameter set to one. Its [attribution](../references/RELATED_WORK.md#malvar1980) is explicit. The generic polynomial $`q`$ above need not be a square; this construction uses the particular subclass $`q=p_N^2`$.

The useful passband identity is

```math
\int_{-1}^{1}p_N(x)^2\,dx
=\frac4{(N+1)(N+2)}.
```

Because $`1-T_N\le p_N^2`$, this controls the integrated transmission defect inside the band. The endpoint derivative $`p_N'(1)=N(N+3)/4`$ and monotonic growth outside the band control the tails. Together these yield

```math
I_{0,N}=2+O(N^{-2}),
\qquad
V_{0,N}=O(N^{-2}).
```

After physical realization, the universal lower bound supplies the reverse order estimate. Thus the attainable optimum over serial chains is $`\Theta(N^{-2})`$. The [filter proof](../science/legendre_family.md) gives finite-size constants. Least-squares optimality of $`p_N`$ is not a claim that this chain minimizes the different Fano-factor objective at each finite size.

<a id="synthesis"></a>

## 8. Why the filter uses exactly N physical sites

A valid transmission profile must still be realized by the permitted Hamiltonian. Classical lossless synthesis provides the starting point. Factor $`1+p(z)^2=d(z)d^\#(z)`$ using the $`N`$ lower-half-plane zeros in $`d`$, with $`d^\#(z)=\overline{d(\bar z)}`$. Normalize $`d`$ to have the same positive leading coefficient as $`p`$. Then

```math
S(z)=\frac1{d(z)}
\begin{pmatrix}p(z)&i\\ i&p(z)\end{pmatrix}
```

is a unitary two-port scattering matrix on the real axis, has the desired transmission, and tends to the identity at infinity. Its Cayley transform

```math
K(z)=-i[I-S(z)][I+S(z)]^{-1}
```

has exactly $`N`$ distinct real poles with positive semidefinite rank-one residues and nonzero source weight at every pole. Those residues provide an $`N`$-mode representation $`K=W^{\mathsf T}(zI-H_0)^{-1}W`$, with source and drain vectors $`b_L,b_R`$ as the columns of $`W`$. Distinct poles and nonzero source weights make $`b_L`$ cyclic: the $`N`$ vectors $`b_L,H_0b_L,\ldots,H_0^{N-1}b_L`$ span the full mode space.

Lanczos orthogonalization of these vectors therefore takes exactly $`N`$ steps and converts $`H_0`$ into a tridiagonal matrix with positive hoppings. A further identity is essential: $`K_{LR}(z)=O(z^{-N})`$, so

```math
b_R^{\mathsf T}H_0^k b_L=0,
\qquad k=0,\ldots,N-2.
```

The drain vector is consequently orthogonal to the first $`N-1`$ Lanczos vectors and sits at the last site. This verifies both endpoint support and the exact orbital count. For the parity-$`N`$ polynomial $`p_N`$, the spectral measure is even, giving zero onsite energies; equality of the endpoint measures gives mirror symmetry. The physical rates are $`\Gamma_\alpha=2\|b_\alpha\|^2`$ and are equal.

The [realization proof](../science/realization.md) supplies the pole, residue, and symmetry details. The general [synthesis principles](../references/RELATED_WORK.md#synthesis) are classical; their explicit application certifies the geometry and resource count needed for this theorem.

<a id="contact-cost"></a>

## 9. Reflection accounts for the current cost

Let $`R(E)=1-T(E)`$ be reflection probability. A Bode–Fano logarithmic reflection argument, with the physical endpoint-rate normalization, gives

```math
A:=\int_{\mathbb R}-\log R(E)\,dE
\le2\pi\min(\Gamma_L,\Gamma_R).
```

Strong suppression of reflection over a broad band consumes this finite integral budget. The [proof](../science/contact_rate.md) tracks the scattering poles and reflection zeros, including the correction when reflection zeros are not real. The [logarithmic method](../references/RELATED_WORK.md#bode) is inherited.

To connect that budget to counting noise, introduce the probability measure $`d\mu(E)=T(E)dE/I_0`$. It weights energies by their contribution to current. Then

```math
\mathbb E_\mu R=F,
\qquad
\frac{A}{I_0}=\mathbb E_\mu g(R),
\qquad
g(r)=\frac{-\log r}{1-r}.
```

The function $`g`$ is convex; for example,

```math
g(r)=\int_0^1\frac{du}{u+(1-u)r}
```

expresses it as an average of convex functions of $`r>0`$. Jensen's inequality therefore gives $`A/I_0\ge g(F)`$. Using $`I_0=2\pi J`$ yields

```math
\boxed{
J\,\frac{\log(1/F)}{1-F}
\le\min(\Gamma_L,\Gamma_R).
}
```

For the single orbital, the left side equals $`\Gamma\log2`$, consistent with its contact rate $`\Gamma`$. More generally, fixed positive current and bounded contact rates cannot coexist with $`F\to0`$.

For the constructed family on the normalized band $`[-1,1]`$, the [root and integral analysis](../science/legendre_family.md) gives

```math
J_N=\frac1\pi+O(N^{-2}),
\qquad
\Gamma_N=\frac3\pi\log N+O(1).
```

Rescaling every Hamiltonian entry and both contact rates by the same positive factor rescales $`J,D`$ equally and preserves $`F`$. Fixing the contacts to a prescribed common rate $`\Gamma`$ therefore produces

```math
J_N\sim\frac{\Gamma}{3\log N},
\qquad F_N=\Theta(N^{-2}).
```

The logarithmic current cost is necessary in order and attained in order. The coefficient three is a property of this construction; an optimal leading coefficient or a complete joint frontier is not established.

## 10. How the bridge fits the milestone map

The [background milestones M01–M14](MILESTONES.md#m01) connect the physical objects, transmission and counting conventions, and the polynomial, Legendre, Cayley, and Krylov tools to the integrated model. The [research narrative M15–M30](MILESTONES.md#m15) follows the converse, upper family, endpoint realization, contact constraint, root asymptotic, and their combined physical meaning. The model assumptions remain attached to every stage: a connected noninteracting serial chain, flat contacts, exactly full/empty occupations, and a long-time counting limit at finite size.

The resulting claim concerns the optimal size exponent and the order of its current cost. It does not assign that exponent to arbitrary coherent networks, interacting devices, finite bias windows, or independent-tick models.
