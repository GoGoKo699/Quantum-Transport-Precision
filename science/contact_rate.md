# Contact rates, current and precision

Suppressing partition noise over a finite energy range requires a large integrated logarithmic suppression of reflection. In a finite chain, the endpoint contact rates bound that integral. Combining the exact pole-and-zero identity with convexity gives

```math
\boxed{\displaystyle
J\,\frac{\log(1/F)}{1-F}
\leq \min(\Gamma_L,\Gamma_R).}
```

The rates here are the physical rates: each contributes $`-i\Gamma_\alpha/2`$ to the effective Hamiltonian. All logarithms are natural. The logarithmic-reflection method has its classical origin in the work of [Bode and Fano](../references/RELATED_WORK.md#bode). The precise identity and its application to particle-current noise are derived below, including real reflection zeros and unequal contacts.

## Assumptions and normalization

Use the connected serial chain of [model.md](model.md), with $`N\geq1`$ sites, a Hermitian nearest-neighbor Hamiltonian $`H`$, nonzero hoppings, and positive, energy-independent rates $`\Gamma_L,\Gamma_R`$. The source is full and the drain empty over the whole real energy axis. Set $`\hbar=1`$ and write

```math
\Pi_L=|1\rangle\langle1|,\qquad
\Pi_R=|N\rangle\langle N|.
```

For $`N=1`$, these projectors coincide; both contact contributions must still be included.

Define

```math
I_0=\int_{\mathbb R}T(E)\,dE,\qquad
V_0=\int_{\mathbb R}T(E)[1-T(E)]\,dE,
```

```math
J=\frac{I_0}{2\pi},\qquad
D=\frac{V_0}{2\pi},\qquad
F=\frac{V_0}{I_0}=\frac{D}{J}.
```

The integrals are finite, $`I_0>0`$, and $`0<F<1`$. Indeed, transmission is positive everywhere and decays at infinity, so $`0<V_0<I_0`$. A disconnected chain or a vanishing contact instead gives zero transmitted current; its current-normalized Fano factor is undefined and is excluded from the theorem.

## Transmission and reflection determinants

Let

```math
H_{\mathrm{eff}}
=H-\frac{i\Gamma_L}{2}\Pi_L-\frac{i\Gamma_R}{2}\Pi_R,
\qquad
G(E)=(EI-H_{\mathrm{eff}})^{-1},
```

and define the monic degree-$`N`$ polynomials

```math
\chi_N(z)=
\det\!\left[zI-H+\frac{i\Gamma_L}{2}\Pi_L
+\frac{i\Gamma_R}{2}\Pi_R\right],
```

```math
Q_L(z)=
\det\!\left[zI-H-\frac{i\Gamma_L}{2}\Pi_L
+\frac{i\Gamma_R}{2}\Pi_R\right].
```

Introduce the $`N\times2`$ contact matrix

```math
V=\begin{pmatrix}\sqrt{\Gamma_L}|1\rangle&
\sqrt{\Gamma_R}|N\rangle\end{pmatrix}.
```

The two-channel scattering matrix is

```math
\mathcal S(E)=I_2-iV^\dagger G(E)V.
```

For real $`E`$,

```math
G(E)-G(E)^\dagger
=-iG(E)VV^\dagger G(E)^\dagger.
```

Substitution shows that $`\mathcal S(E)\mathcal S(E)^\dagger=I_2`$. In particular, the left reflection and transmission amplitudes satisfy

```math
r_L(E)=1-i\Gamma_L G_{11}(E),\qquad
|r_L(E)|^2+T(E)=1.
```

The matrix determinant lemma gives

```math
r_L(E)=\frac{Q_L(E)}{\chi_N(E)}.
```

For the serial chain, the endpoint cofactor is the product of its hoppings, so

```math
T(E)=\Gamma_L\Gamma_R|G_{N1}(E)|^2
=\frac{C}{|\chi_N(E)|^2},
\qquad
C=\Gamma_L\Gamma_R\prod_{j=1}^{N-1}|t_j|^2>0.
```

The empty product for $`N=1`$ is one. Consequently,

```math
1-T(E)=\frac{|Q_L(E)|^2}{|\chi_N(E)|^2},
\qquad
|\chi_N(E)|^2-|Q_L(E)|^2=C
\quad(E\in\mathbb R).
```

These formulas do not require equal contacts or reflection symmetry.

## Location and sums of the roots

Let $`\zeta_1,\ldots,\zeta_N`$ be the roots of $`\chi_N`$, counted with algebraic multiplicity. They are eigenvalues of $`H_{\mathrm{eff}}`$. For a nonzero right eigenvector $`v`$ with eigenvalue $`\zeta`$,

```math
\operatorname{Im}\zeta
=-\frac{\Gamma_L|v_1|^2+\Gamma_R|v_N|^2}
{2\|v\|^2}.
```

If the imaginary part were zero, both endpoint components would vanish. The eigenvalue equation at the first site would then force $`v_2=0`$, and the nonzero nearest-neighbor hoppings would propagate this conclusion through the chain. This contradicts $`v\neq0`$. For $`N=1`$, the same displayed formula is directly strictly negative. Therefore every root lies strictly in the lower half-plane, and the resolvent is well defined on the real axis.

Taking the trace, with algebraic multiplicity and without requiring diagonalizability, yields

```math
\sum_{j=1}^N|\operatorname{Im}\zeta_j|
=-\operatorname{Im}\operatorname{tr}H_{\mathrm{eff}}
=\frac{\Gamma_L+\Gamma_R}{2}.
\tag{1}
```

Let $`\eta_1,\ldots,\eta_N`$ be the roots of $`Q_L`$, also with algebraic multiplicity. They are the eigenvalues of

```math
H+\frac{i\Gamma_L}{2}\Pi_L-\frac{i\Gamma_R}{2}\Pi_R.
```

No half-plane restriction is assumed for these roots. Their trace gives

```math
\sum_{j=1}^N\operatorname{Im}\eta_j
=\frac{\Gamma_L-\Gamma_R}{2},
\qquad
\sum_{j=1}^N|\operatorname{Im}\eta_j|
\geq\frac{|\Gamma_L-\Gamma_R|}{2}.
\tag{2}
```

Both sets of roots have the same real sum,

```math
\operatorname{Re}\sum_j\zeta_j
=\operatorname{Re}\sum_j\eta_j
=\operatorname{tr}H.
\tag{3}
```

For $`N=1`$, the two endpoint contributions in each trace add on the same orbital. Equations (1)-(3) retain exactly the stated form.

## A logarithmic root-integral lemma

**Lemma.** Let $`A`$ and $`B`$ be monic polynomials of the same degree, with roots $`a_j`$ and $`b_j`$ counted with multiplicity. Suppose

```math
\operatorname{Re}\sum_j a_j=\operatorname{Re}\sum_j b_j.
```

Then the logarithm below is absolutely integrable, with the values at its finitely many real zeros understood almost everywhere, and

```math
\int_{\mathbb R}
\log\frac{|A(E)|^2}{|B(E)|^2}\,dE
=
2\pi\left[
\sum_j|\operatorname{Im}a_j|
-\sum_j|\operatorname{Im}b_j|
\right].
\tag{4}
```

A common real root can be canceled first or treated by combining its logarithmic contributions. The result is the same.

### Proof

First consider one root $`z=a+ib`$, with real $`a,b`$. Almost everywhere,

```math
\log|E-z|^2-\log E^2
=
\log\!\left(1+\frac{b^2}{(E-a)^2}\right)
+\log\frac{(E-a)^2}{E^2}.
\tag{5}
```

The first term is nonnegative and integrable. For $`y\neq0`$,

```math
\log\!\left(1+\frac{b^2}{y^2}\right)
=\int_0^{|b|}\frac{2s}{y^2+s^2}\,ds.
```

Tonelli's theorem applies to this nonnegative integrand, giving

```math
\int_{\mathbb R}
\log\!\left(1+\frac{b^2}{y^2}\right)\,dy
=
\int_0^{|b|}
\left(\int_{\mathbb R}\frac{2s}{y^2+s^2}\,dy\right)ds
=2\pi|b|.
\tag{6}
```

The integrand at $`s=0`$ is irrelevant to the integral; for every $`s>0`$, the inner integral is $`2\pi`$. Equation (6) also covers $`b=0`$.

The horizontal-shift term in (5) has symmetric integral, for $`R>|a|`$,

```math
\begin{aligned}
\int_{-R}^{R}\log\frac{(E-a)^2}{E^2}\,dE
=2\big[
&(R-a)\log(R-a)+(R+a)\log(R+a)\\
&-2R\log R
\big].
\end{aligned}
```

This expression tends to zero as $`R\to\infty`$. Thus the symmetric-cutoff contribution of one root, relative to a root at zero, is $`2\pi|b|`$.

Factor the two polynomials and sum these finitely many root contributions. Their equal degrees cancel all reference terms $`\log E^2`$, so the symmetric limit equals the right-hand side of (4).

It remains to check that this limit is the ordinary, absolutely convergent integral. At any finite real root, the only possible singularity is a finite multiple of $`\log|E-E_0|`$, which is locally absolutely integrable. At infinity,

```math
\log|A(E)|^2
=
2n\log|E|
-\frac{2\operatorname{Re}\sum_j a_j}{E}
+O(E^{-2}),
```

where $`n`$ is the common degree. The analogous expansion for $`B`$, together with the hypothesis on the real root sums, cancels both displayed leading terms. Their difference is $`O(E^{-2})`$. This proves absolute integrability and completes the proof.

## Exact reflection integral and the asymmetric bound

Define

```math
\mathcal A=\int_{\mathbb R}-\log[1-T(E)]\,dE.
```

Perfect-transmission energies are real roots of $`Q_L`$. They are a finite set. If such a root has multiplicity $`k`$, the integrand has local form $`-2k\log|E-E_0|+O(1)`$, which is integrable. At infinity it is $`O(|E|^{-2N})`$. Thus $`\mathcal A`$ is finite despite its values being infinite at isolated perfect-transmission energies.

Apply the lemma to $`\chi_N`$ and $`Q_L`$, using (3). Equations (1) and (4) give the exact identity

```math
\boxed{\displaystyle
\mathcal A
=
2\pi\left[
\frac{\Gamma_L+\Gamma_R}{2}
-\sum_{j=1}^N|\operatorname{Im}\eta_j|
\right].}
\tag{7}
```

This identity retains the contribution of every reflection zero, on either side of the real axis. In particular, it does not assume a minimum-phase reflection amplitude.

The triangle inequality (2) now yields

```math
\mathcal A
\leq
2\pi\left[
\frac{\Gamma_L+\Gamma_R}{2}
-\frac{|\Gamma_L-\Gamma_R|}{2}
\right]
=
2\pi\min(\Gamma_L,\Gamma_R).
\tag{8}
```

For equal contacts $`\Gamma_L=\Gamma_R=\Gamma`$, equality in (8) holds exactly when all reflection zeros are real. For unequal contacts, equality holds exactly when all nonzero imaginary parts of the reflection zeros have the same sign. These statements concern the spectral bound (8); the convexity step below is a separate inequality.

## Converting reflection into a Fano-factor bound

Use transmission to define a probability measure on energy,

```math
d\nu(E)=\frac{T(E)}{I_0}\,dE,
```

and the random variable $`X(E)=1-T(E)`$. Its mean is the Fano factor:

```math
\mathbb E_\nu[X]
=\frac{1}{I_0}\int_{\mathbb R}T(E)[1-T(E)]\,dE
=F.
```

For $`0<x<1`$, define

```math
g(x)=\frac{-\log x}{1-x}
=\int_0^1\frac{dt}{x+(1-x)t},
\qquad g(1)=1.
```

Differentiating under the finite $`t`$ integral at any $`x>0`$ gives

```math
g'(x)=-\int_0^1
\frac{1-t}{[x+(1-x)t]^2}\,dt<0,
```

```math
g''(x)=2\int_0^1
\frac{(1-t)^2}{[x+(1-x)t]^3}\,dt>0.
```

Thus $`g`$ is decreasing and strictly convex. The possible points with $`X=0`$ form a finite set of $`\nu`$ measure zero. Away from them,

```math
T(E)\,g(1-T(E))=-\log[1-T(E)].
```

Consequently $`g(X)`$ is integrable under $`\nu`$, with

```math
\mathbb E_\nu[g(X)]=\frac{\mathcal A}{I_0}<\infty.
```

Jensen's inequality is therefore applicable without a cutoff or an interchange of divergent integrals:

```math
\frac{\mathcal A}{I_0}
\geq g(F)=\frac{\log(1/F)}{1-F}.
\tag{9}
```

Combining (8), (9), and $`I_0=2\pi J`$ proves

```math
\boxed{\displaystyle
J\,\frac{\log(1/F)}{1-F}
\leq \Gamma_{\min},
\qquad
\Gamma_{\min}:=\min(\Gamma_L,\Gamma_R).}
\tag{10}
```

For any finite connected chain, transmission is nonconstant, and the probability measure $`\nu`$ has positive density everywhere. Strict convexity therefore makes (9) strict. Equation (10) is stated in weak form because it is a universal bound and is useful for limits of families.

## Consequences for physical resources

For a prescribed target $`0<\varepsilon<1`$, achieving $`F\leq\varepsilon`$ requires, by monotonicity of $`g`$,

```math
\frac{J}{\Gamma_{\min}}
\leq\frac{1-\varepsilon}{\log(1/\varepsilon)}.
\tag{11}
```

Equivalently, at fixed positive current and fixed contact rates, the Fano factor cannot approach zero merely by adding sites. A simpler, weaker explicit form of (10) is

```math
F\geq\exp\!\left(-\frac{\Gamma_{\min}}{J}\right).
```

If a family achieves the optimal size order $`F_N=\Theta(N^{-2})`$, then

```math
\frac{J_N}{\Gamma_{\min,N}}
\leq\frac{1+o(1)}{2\log N}.
\tag{12}
```

The [Legendre family](legendre_family.md) attains this necessary logarithmic decrease in order. In the normalization where its reference interval is $`[-1,1]`$, that page proves

```math
J_N=\frac{1}{\pi}+O(N^{-2}),
\qquad
\Gamma_{L,N}=\Gamma_{R,N}
=\frac{3}{\pi}\log N+O(1).
```

The second relation follows from (7), the all-real reflection zeros of the [symmetric realization](realization.md), and the proved logarithmic integral asymptotic. Hence

```math
\frac{J_N}{\Gamma_{L,N}}
\sim\frac{1}{3\log N}.
```

Rescaling all energies and rates to a fixed endpoint rate $`\Gamma`$ leaves $`F_N`$ unchanged and gives $`J_N\sim\Gamma/(3\log N)`$. The necessary and attained logarithmic orders match. The coefficients $`1/2`$ in (12) and $`1/3`$ for this family differ, so these results do not determine an exact optimal current-precision frontier.

## One-site check

For one orbital with onsite energy $`\epsilon`$, the formulas reduce to

```math
T(E)=
\frac{\Gamma_L\Gamma_R}
{(E-\epsilon)^2+(\Gamma_L+\Gamma_R)^2/4},
```

```math
J=\frac{\Gamma_L\Gamma_R}{\Gamma_L+\Gamma_R},
\qquad
F=\frac{\Gamma_L^2+\Gamma_R^2}
{(\Gamma_L+\Gamma_R)^2}.
```

There is one transmission pole and one reflection zero:

```math
\zeta=\epsilon-\frac{i}{2}(\Gamma_L+\Gamma_R),
\qquad
\eta=\epsilon+\frac{i}{2}(\Gamma_L-\Gamma_R).
```

Equation (7) gives

```math
\mathcal A=2\pi\min(\Gamma_L,\Gamma_R).
```

For equal physical rates $`\Gamma`$,

```math
J=\frac{\Gamma}{2},\qquad
F=\frac12,\qquad
\mathcal A=2\pi\Gamma.
```

The left-hand side of (10) is then $`\Gamma\log2<\Gamma`$. This checks the contact-rate convention, the factor $`2\pi`$ in the current, and the distinction between saturation of the spectral identity and saturation of Jensen's inequality.

## Relation to the size law

The [size theorem](size_bound.md) bounds how much precision a fixed number of serial orbitals can provide. Equation (10) bounds the current compatible with that precision at specified contact rates. Both constraints apply to the same ideal full-source, empty-drain model, and both are invariant under a common rescaling when expressed through $`F`$ and $`J/\Gamma_{\min}`$.

Finite-bias occupation factors, energy-dependent contacts, and additional reservoirs change the problem and are outside these claims. This contact-rate theorem is a spectral transport statement; it is not an entropy-production bound or a bound on transient convergence. Further physical interpretation is given in [interpretation.md](interpretation.md), and the relation to earlier work is documented in [the references](../references/RELATED_WORK.md).

