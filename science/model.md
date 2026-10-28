# Model, observables, and exact claims

A finite coherent conductor can suppress particle-count fluctuations by transmitting almost perfectly over an energy interval. The relevant question is how closely a chain with a fixed number of sites can approach that limit, and what happens to its current when the reservoir coupling is held fixed.

The resource counted here is the number of orbitals in a **serial nearest-neighbor chain**. The many-body Hilbert space has dimension $`2^N`$; no theorem in this project identifies those two resources.

## 1. Physical model

Set $`\hbar=1`$. Let $`c_j`$ annihilate a fermion on site $`j`$. The number-conserving Hamiltonian is

```math
\widehat H=\sum_{j=1}^N\epsilon_j c_j^\dagger c_j
+\sum_{j=1}^{N-1}t_j(c_j^\dagger c_{j+1}+c_{j+1}^\dagger c_j).
```

The onsite energies are real and finite, and every hopping is nonzero. Phases on a serial chain can be removed by local basis changes, so $`t_j>0`$ can be assumed without changing transport. The corresponding single-particle Hamiltonian $`H`$ is a real symmetric Jacobi matrix.

A filled source couples only to site 1, and an empty drain only to site $`N`$. Their physical rates are $`\Gamma_L,\Gamma_R>0`$. In the ideal wide-band, full-bias model, the dynamics is

```math
\dot\rho=-i[\widehat H,\rho]
+\Gamma_L\mathcal D[c_1^\dagger]\rho
+\Gamma_R\mathcal D[c_N]\rho,
\qquad
\mathcal D[L]\rho=L\rho L^\dagger
-\tfrac12\{L^\dagger L,\rho\}.
```

The occupations are exactly one and zero over the entire energy axis. This is an ideal reservoir model; a finite chemical-potential window introduces different occupation factors into both current and noise. There is no internal dephasing, interaction, bypass, side branch, or extra terminal.

For $`N=1`$, both reservoirs couple to the same orbital and both damping contributions are retained. A disconnected chain or a vanishing contact has zero transmitted current and an undefined current-normalized Fano factor, so it is excluded.

## 2. Scattering convention

Define the endpoint projectors $`\Pi_L=|1\rangle\langle1|`$ and $`\Pi_R=|N\rangle\langle N|`$, and

```math
H_{\mathrm{eff}}
=H-\frac{i}{2}(\Gamma_L\Pi_L+\Gamma_R\Pi_R),
\qquad
G(E)=(E I-H_{\mathrm{eff}})^{-1}.
```

The physical rate is $`\Gamma_\alpha`$; the retarded half-width is $`\Gamma_\alpha/2`$. The transmission probability is

```math
T(E)=\Gamma_L\Gamma_R|G_{N1}(E)|^2.
```

This convention agrees with the reservoir jump rates in the master equation. For example, a single orbital gives

```math
T(E)=
\frac{\Gamma_L\Gamma_R}
{(E-\epsilon_1)^2+(\Gamma_L+\Gamma_R)^2/4}.
```

To see unitarity directly, put $`V=(\sqrt{\Gamma_L}|1\rangle,\sqrt{\Gamma_R}|N\rangle)`$. Then

```math
S(E)=I_2-iV^\dagger G(E)V.
```

The resolvent identity $`G-G^\dagger=-iGVV^\dagger G^\dagger`$ gives $`SS^\dagger=I_2`$ on the real axis. Consequently $`0<T(E)\le1`$ for a connected chain.

Every pole of $`G`$ lies strictly below the real axis. If $`H_{\mathrm{eff}}v=zv`$, then

```math
\Im z\,\|v\|^2
=-\tfrac12(\Gamma_L|v_1|^2+\Gamma_R|v_N|^2).
```

A real pole would require vanishing endpoint components. The Jacobi recurrence and the nonzero hoppings would then force every component to vanish. This also ensures convergence of the stationary covariance integral.

## 3. Why serial geometry matters

Let

```math
\chi_N(E)=\det(EI-H_{\mathrm{eff}}),
\qquad
C=\Gamma_L\Gamma_R\prod_{j=1}^{N-1}t_j^2.
```

The endpoint cofactor of a tridiagonal matrix contains only the unique path across the chain. Therefore

```math
T(E)=\frac{C}{|\chi_N(E)|^2}.
```

Here $`\chi_N`$ has degree $`N`$ and $`C>0`$ is independent of energy. In particular,

```math
q(E)=\frac{|\chi_N(E)|^2}{C}-1
```

is a real nonnegative polynomial of degree $`2N`$. This polynomial reduction is the load-bearing input to the [size bound](size_bound.md).

A network with coherent parallel paths or side-coupled resonances can have an energy-dependent transmission numerator. The polynomial argument does not establish a size law for that larger class.

## 4. Current and counting noise

Let $`K_t`$ count particles transferred into the drain during a stationary observation of duration $`t`$. Define

```math
J=\lim_{t\to\infty}\frac{\mathbb E K_t}{t},
\qquad
D=\lim_{t\to\infty}\frac{\mathrm{Var}K_t}{t},
\qquad
F=\frac{D}{J}.
```

The full-bias fermionic counting formula is

```math
\lim_{t\to\infty}\frac1t
\log\mathbb E e^{sK_t}
=\frac{1}{2\pi}\int_{\mathbb R}
\log\!\left[1+T(E)(e^s-1)\right]dE.
```

Its first two derivatives yield

```math
I_0=\int_{\mathbb R}T(E)\,dE,
\qquad
V_0=\int_{\mathbb R}T(E)[1-T(E)]\,dE,
```

```math
J=\frac{I_0}{2\pi},
\qquad
D=\frac{V_0}{2\pi},
\qquad
F=\frac{V_0}{I_0}.
```

The factor $`1-T`$ is the fermionic partition-noise suppression. These are established [scattering and counting-statistics identities](../references/RELATED_WORK.md#counting-statistics). In this account $`D`$ is the count-variance rate; electrical noise spectral-density conventions can contain an additional factor of two.

All these integrals converge because $`T(E)=O(|E|^{-2N})`$. The chain is finite when the long-time limit is taken; the size asymptotic is considered afterward.

A global rescaling $`H\mapsto aH`$, $`\Gamma_\alpha\mapsto a\Gamma_\alpha`$ with $`a>0`$ sends $`J,D\mapsto a(J,D)`$ and leaves $`F`$ unchanged. A common onsite-energy shift also leaves these full-line integrals unchanged.

## 5. Main statements

Define $`F_N^\star`$ as the infimum of $`F`$ over all connected chains satisfying the assumptions above, with arbitrary finite onsite energies, nonzero hoppings, and positive endpoint rates.

### Size law

For every such chain,

```math
F\ge\frac{1}{18N^2+2}.
```

For each $`N\ge1`$, define

```math
p_N(x)=\frac{2P'_{N+1}(x)}{(N+1)(N+2)},
\qquad
T_N(x)=\frac{1}{1+p_N(x)^2},
```

where $`P_k`$ is the Legendre polynomial normalized by $`P_k(1)=1`$. This inherited classical filter has an exact physical realization with $`N`$ sites, zero onsite energies, mirror-symmetric positive hoppings, and equal endpoint rates. It obeys

```math
F_N\le
\frac{
\dfrac{4}{(N+1)(N+2)}
+\dfrac{\pi+2}{N(N+3)}
}{
2-\dfrac{4}{(N+1)(N+2)}
}.
```

Consequently,

```math
F_N^\star=\Theta(N^{-2}).
```

The exponent is optimal. The numerical constants in the upper and lower bounds do not match, and the construction is not asserted to minimize $`F`$ at each finite $`N`$. The same optimal order is attainable when both contact rates are fixed to any prescribed common positive value, by global rescaling.

Proofs: [universal lower bound](size_bound.md), [filter estimates](legendre_family.md), and [exact serial realization](realization.md).

### Contact-rate constraint

Every admissible chain also satisfies

```math
J\,\frac{\log(1/F)}{1-F}
\le\min(\Gamma_L,\Gamma_R).
```

This follows from a logarithmic reflection sum rule and a convexity step weighted by transmitted current. The [contact-rate proof](contact_rate.md) retains asymmetric rates and fixes the root-integral normalization explicitly.

For the constructed family, with its energy variable normalized to a passband $`[-1,1]`$,

```math
J_N=\frac1\pi+O(N^{-2}),
\qquad
\Gamma_{L,N}=\Gamma_{R,N}
=\frac3\pi\log N+O(1).
```

Rescaling both rates to a fixed $`\Gamma`$ gives

```math
J_N\sim\frac{\Gamma}{3\log N},
\qquad
F_N=\Theta(N^{-2}).
```

Thus the required logarithmic loss of current is attained in order. An optimal leading current constant or a complete joint size-current-noise frontier is not established.

## Reading route

Continue with the [size bound](size_bound.md), [Legendre family](legendre_family.md), [physical synthesis](realization.md), and [contact-rate bound](contact_rate.md). The [interpretation](interpretation.md) explains the resource consequences and the relation to correlated clocks. The [verification guide](../verification/README.md) separates finite numerical checks from the analytical statements.

