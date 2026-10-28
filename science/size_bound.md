# A size bound for every serial chain

A finite serial chain cannot make its transmission change from almost zero to almost one over an arbitrarily small fraction of its conducting energy range. Its transmission denominator is a polynomial whose degree is fixed by the number of sites. The classical Markov derivative inequality turns that degree constraint into a lower bound on partition noise.

## Statement and conventions

Consider the connected, noninteracting, nearest-neighbor chain in [the model definition](model.md). There are $`N\geq 1`$ sites, every hopping is nonzero, and the full source and empty drain have positive, energy-independent physical contact rates $`\Gamma_L,\Gamma_R`$. Set $`\hbar=1`$. For its transmission probability $`T(E)`$, define

```math
I_0=\int_{\mathbb R}T(E)\,dE,\qquad
V_0=\int_{\mathbb R}T(E)[1-T(E)]\,dE,
```

```math
J=\frac{I_0}{2\pi},\qquad
D=\frac{V_0}{2\pi},\qquad
F=\frac{D}{J}=\frac{V_0}{I_0}.
```

Here $`D`$ is the long-time particle-count variance per unit time, with the convention specified in [model.md](model.md).

**Theorem.** Every such chain satisfies

```math
\boxed{\displaystyle F\geq\frac{1}{18N^2+2}.}
```

The constant is not asserted to be optimal. The [Legendre family](legendre_family.md), together with its [physical realization](realization.md), supplies the matching order $`F=O(N^{-2})`$. Consequently, the infimum over the stated class is $`\Theta(N^{-2})`$.

If a contact or a hopping vanishes, the transmitted current is zero. The ratio defining $`F`$ is then undefined, so no Fano-factor assertion is made for that case.

## The polynomial constraint

Let $`H`$ be the single-particle Jacobi Hamiltonian, with hopping amplitudes $`t_j`$, and let $`\Pi_L=|1\rangle\langle1|`$ and $`\Pi_R=|N\rangle\langle N|`$. Write

```math
\chi_N(z)=
\det\!\left[
zI-H+\frac{i\Gamma_L}{2}\Pi_L+\frac{i\Gamma_R}{2}\Pi_R
\right],
```

```math
C=\Gamma_L\Gamma_R\prod_{j=1}^{N-1}|t_j|^2>0.
```

For $`N=1`$, the product is one and both contact contributions act on the same orbital. The endpoint-to-endpoint cofactor of a Jacobi matrix is independent of energy. Thus

```math
T(E)=\frac{C}{|\chi_N(E)|^2},\qquad 0<T(E)\leq 1.
```

The denominator has no real zero. This follows from the strict lower-half-plane location of all damped-chain eigenvalues, proved in [the contact-rate analysis](contact_rate.md#location-and-sums-of-the-roots). Unitarity supplies the upper bound on transmission.

Define the real polynomial

```math
q(E)=\frac{|\chi_N(E)|^2}{C}-1.
```

More formally, its polynomial extension is $`C^{-1}\chi_N(z)\overline{\chi_N(\bar z)}-1`$. It has real coefficients, degree $`m=2N`$, and positive leading coefficient. On the real axis,

```math
q(E)\geq 0,\qquad
T(E)=\frac{1}{1+q(E)},\qquad
T(E)[1-T(E)]=\frac{q(E)}{[1+q(E)]^2}.
```

Since $`T(E)=O(|E|^{-2N})`$ at infinity, both $`I_0`$ and $`V_0`$ are finite. They are strictly positive: $`T`$ is positive everywhere, and it is strictly less than one outside a bounded energy interval.

The proof below uses only these polynomial facts. In particular, it does not require reflection symmetry, equal contacts, or real reflection zeros.

## A derivative bound on each conducting interval

The classical [Markov polynomial inequality](../references/RELATED_WORK.md#markov) states that a real polynomial $`f`$ of degree at most $`m`$ obeys

```math
\|f'\|_{\infty,[-1,1]}\leq
m^2\|f\|_{\infty,[-1,1]}.
```

Rescaling to an interval $`[a,b]`$ of length $`\ell=b-a>0`$ gives

```math
\|f'\|_{\infty,[a,b]}
\leq \frac{2m^2}{\ell}\|f\|_{\infty,[a,b]}.
```

Consider the half-transmission set

```math
S=\{E:q(E)\leq 1\}=\{E:T(E)\geq\tfrac12\}.
```

It is compact because $`q(E)\to+\infty`$ at both ends of the real axis. Since $`q-1`$ is a nonconstant polynomial, $`S`$ consists of finitely many nondegenerate closed intervals, possibly together with isolated points. Write the nondegenerate connected components as

```math
K_j=[a_j,b_j],\qquad
\ell_j=b_j-a_j>0,\qquad
L=\sum_j\ell_j.
```

The sum can be empty. Isolated points have zero measure and do not contribute to $`L`$.

Continuity and maximality of a nondegenerate component imply

```math
q(a_j)=q(b_j)=1,\qquad 0\leq q(E)\leq 1
\quad(E\in K_j).
```

This remains true when a level-set root is multiple or the polynomial touches the threshold inside a component. No nondegeneracy of the roots is assumed.

Apply the rescaled Markov inequality to $`q-\tfrac12`$. Its absolute value is at most one half on $`K_j`$, so

```math
\sup_{E\in K_j}|q'(E)|\leq \frac{m^2}{\ell_j}.
```

## Every conducting interval contributes noise

Set

```math
\delta_j=\frac{\ell_j}{2m^2}.
```

On the left endpoint strip $`[a_j,a_j+\delta_j]`$, the derivative bound gives

```math
q(E)\geq q(a_j)-\frac{m^2}{\ell_j}(E-a_j)
\geq\frac12.
```

The same conclusion holds on the right strip $`[b_j-\delta_j,b_j]`$. On both strips, $`q\leq1`$ also holds. The strips are disjoint because $`m=2N\geq2`$, and their combined length is $`\ell_j/m^2`$.

For $`1/2\leq q\leq1`$,

```math
\frac{q}{(1+q)^2}\geq\frac{2}{9}.
```

Therefore each nondegenerate component contributes at least

```math
\int_{K_j}T(E)[1-T(E)]\,dE
\geq \frac{2\ell_j}{9m^2}.
```

Summing over components yields

```math
V_0\geq\frac{2L}{9m^2}.
\qquad\text{(1)}
```

The estimate adds the contributions of all conducting intervals. Splitting the transmission into several separated bands does not remove it.

## From conducting width to total current

On $`S`$, transmission is at most one, so

```math
\int_S T(E)\,dE\leq L.
```

On its complement, $`q>1`$ and $`T<1/2`$. Hence

```math
T(E)[1-T(E)]\geq\frac12T(E)
\quad(E\notin S),
```

which implies

```math
\int_{\mathbb R\setminus S}T(E)\,dE\leq2V_0.
```

Combining these estimates with (1),

```math
I_0\leq L+2V_0
\leq\left(\frac{9m^2}{2}+2\right)V_0.
```

Division by the strictly positive $`I_0`$ and substitution of $`m=2N`$ prove

```math
F=\frac{V_0}{I_0}
\geq\frac{2}{9m^2+4}
=\frac{1}{18N^2+2}.
```

If $`S`$ is empty or consists only of isolated points, then $`L=0`$. The outside-set estimate directly gives the stronger bound $`F\geq1/2`$, and the displayed theorem remains valid.

## Scope of the result

The degree argument applies to the constant-numerator, or all-pole, transmission of a serial nearest-neighbor chain. A general coherent network can have an energy-dependent transmission numerator. Loops, side branches, additional terminals, and energy-dependent reservoirs therefore require a separate argument.

The proof integrates over the full real energy axis with a filled source and an empty drain. It does not establish the same bound for a finite occupation window, where different energy weights enter current and noise.

The Fano factor is invariant under a common rescaling of all energies and contact rates. Such a rescaling changes the current. The [contact-rate bound](contact_rate.md) makes this distinction quantitative: approaching the quadratic size law at fixed contact rate requires a current that decreases at least logarithmically with size. A zero-frequency Fano-factor bound alone also makes no assertion about the time required to reach the long-time counting regime.

