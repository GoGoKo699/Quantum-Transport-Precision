# The fixed-contact current frontier

A chain can retain inverse-square particle-count noise while carrying more current than the [Legendre construction](legendre_family.md). Moving the two outer reflection zeros of a Chebyshev polynomial gives a thin transmission edge and an independently adjustable reflection amplitude in the conducting band.

## 1. The leading current at a prescribed noise ceiling

Use the [serial-chain model](model.md) with a filled source, an empty drain and equal wide-band physical contact rates $`\Gamma_L=\Gamma_R=\Gamma`$. Count particles for long times at each finite chain length $`N`$. Write $`J`$ for the mean current and $`F`$ for the count-variance rate divided by that current. For a noise ceiling $`0<f<1`$, let $`J_N^\star(f;\Gamma)`$ be the supremum of $`J`$ over connected $`N`$-site chains at these rates with $`F\le f`$.

**Theorem.** There is an absolute constant $`C>0`$ such that for every sequence $`f_N\to0`$ with $`f_N\ge C/N^2`$ for all sufficiently large $`N`$,

```math
\boxed{\displaystyle
J_N^\star(f_N;\Gamma)\sim\frac{\Gamma}{\log(1/f_N)}.}
```

The lower bound comes from explicit chains with zero onsite energies and mirror-symmetric hoppings. In particular, the construction at inverse-square noise satisfies

```math
F_N=\Theta(N^{-2}),
\qquad
J_N\sim\frac{\Gamma}{2\log N}.
```

This gives a factor $`3/2`$ in leading current compared with the Legendre family at the same physical contact rate and noise exponent. The [contact-rate converse](contact_rate.md) makes the leading coefficient $`1/2`$ optimal at this exponent.

## 2. Move just the outer reflection zeros

Let $`C_N`$ be the Chebyshev polynomial of the first kind, so $`C_N(\cos\theta)=\cos(N\theta)`$ and $`C_N(\cosh t)=\cosh(Nt)`$. Work in raw energy units with the intended conducting band $`[-1,1]`$. For $`N\ge8`$ and $`1/N\le a\le1`$ set

```math
r_N=\cos\!\left(\frac{\pi}{2N}\right),\qquad
s_N=\sqrt{r_N^2-\frac{1}{aN^2}},\qquad
p_{N,a}(x)=a C_N(x)\frac{x^2-s_N^2}{x^2-r_N^2}.
```

The quotient is a polynomial after canceling the two roots at $`\pm r_N`$. Thus $`p_{N,a}`$ has degree $`N`$, leading coefficient $`a2^{N-1}`$, and parity $`N`$. The new roots $`\pm s_N`$ lie inside $`[-1,1]`$ and the other roots stay where they were. This remains true if a new root coincides with an old one.

The [spectral-factor and Jacobi construction](realization.md) realizes

```math
T(x)=\frac{1}{1+p_{N,a}(x)^2}
```

with exactly $`N`$ sites and equal raw physical contact rates $`\Gamma_{\mathrm{raw}}`$. The parity gives zero onsite energies, and the construction gives mirror-symmetric hoppings. Since every reflection zero is real, the [contact-rate identity](contact_rate.md#exact-reflection-integral-and-the-asymmetric-bound) gives

```math
2\pi\Gamma_{\mathrm{raw}}
=\mathcal A,
\qquad
\mathcal A=\int_{\mathbb R}\log\!\big(1+p_{N,a}(x)^{-2}\big)\,dx.
```

The logarithmic singularities at individual zeros are integrable. Real-root preservation is what allows this equality to determine the actual contact cost.

## 3. Bound the noise on the whole energy axis

Inside the band write $`p=p_{N,a}`$ and split it into an adjustable bulk term and an edge term,

```math
p(x)=a C_N(x)+q_N(x),\qquad
q_N(x)=\frac{C_N(x)}{N^2(x^2-r_N^2)}.
```

For $`0\le x\le1`$ the bound $`|C_N(x)|\le1`$ and the derivative estimate $`\|C_N'\|_{[-1,1]}\le N^2`$, applied from the zero at $`r_N`$, give

```math
|q_N(x)|
\le \frac{1}{r_N N^2}\min\{N^2,|x-r_N|^{-1}\}.
```

The derivative estimate follows from $`C_N'(\cos\theta)=N\sin(N\theta)/\sin\theta`$ and $`|\sin(N\theta)|\le N|\sin\theta|`$, with endpoints taken by continuity. Squaring and integrating separately over $`|x-r_N|\le N^{-2}`$ and its complement gives $`\int_0^1 q_N^2\,dx=O(N^{-2})`$. By parity this controls the other half of the band. Consequently,

```math
\int_{-1}^{1}p(x)^2\,dx=O(a^2+N^{-2}).
```

Both $`1-T`$ and $`T(1-T)`$ are at most $`p^2`$ in the band.

Outside the band it suffices by parity to put $`x=\cosh(u/N)`$ with $`u\ge0`$. The edge term is positive and yields

```math
p(x)\ge
\frac{\cosh u}{N^2\sinh^2(u/N)+N^2\sin^2(\pi/(2N))}
\ge c\,\frac{e^{3u/4}}{1+u^2}
```

for an absolute $`c>0`$. The second inequality uses $`\sinh v\le ve^v`$ for $`v\ge0`$ and $`N\ge8`$. The Jacobian satisfies $`dx/du\le u e^{u/N}/N^2`$. The functions $`T`$, $`T(1-T)`$ and $`\log(1+p^{-2})`$ are each at most $`p^{-2}`$ in the exterior. Their integrals over $`|x|\ge1`$ are therefore $`O(N^{-2})`$. All constants in these estimates are independent of $`a`$.

It follows that the raw full-line integrals satisfy

```math
I_0=\int_{\mathbb R}T(x)\,dx=2+O(a^2+N^{-2}),
\qquad
V_0=\int_{\mathbb R}T(x)[1-T(x)]\,dx=O(a^2+N^{-2}).
```

In particular, $`F=V_0/I_0=O(a^2+N^{-2})`$ as $`a\to0`$.

## 4. Compute the contact cost

The exterior contribution to $`\mathcal A`$ is already controlled. Inside the band the identity

```math
\log(1+p^{-2})=
\log(1+p^2)-2\log a-2\log|C_N(x)|
-2\log\!\left|\frac{x^2-s_N^2}{x^2-r_N^2}\right|
```

holds away from the finite set of zeros of the factors. The first term has integral $`O(a^2+N^{-2})`$. The substitution $`x=\cos\theta`$ bounds the integral of $`-\log|C_N(x)|`$ by $`\int_0^\pi-\log|\cos(N\theta)|\,d\theta=\pi\log2`$. The last term is a sum of four root logarithms whose absolute integrals are bounded uniformly for all root positions in $`[-1,1]`$. For example, $`\int_{-1}^1|\log|x-y||\,dx\le2+2\log2`$ for $`y\in[-1,1]`$, by splitting at $`|x-y|=1`$. Hence

```math
\mathcal A=4\log(1/a)+O(1),
\qquad
J_{\mathrm{raw}}=\frac{I_0}{2\pi}
=\frac{1+O(a^2+N^{-2})}{\pi}.
```

Multiply every Hamiltonian coefficient and both physical rates by $`\Gamma/\Gamma_{\mathrm{raw}}`$. The energy integrals for current and count variance scale by the same factor, so $`F`$ stays fixed and the current at the prescribed contact rate becomes

```math
\frac{J}{\Gamma}=\frac{I_0}{\mathcal A}
\sim\frac{1}{2\log(1/a)}
\qquad\text{as }a\to0,\quad a\ge N^{-1}.
```

## 5. Match the all-chain upper bound

For $`a=1/N`$ the construction gives $`F_N=O(N^{-2})`$ and $`J_N\sim\Gamma/(2\log N)`$. The [universal size bound](size_bound.md) supplies the other side of $`F_N=\Theta(N^{-2})`$.

For a general vanishing ceiling $`f_N`$, choose $`a=\lambda\sqrt{f_N}`$ for a sufficiently small constant $`\lambda>0`$. Indeed, let $`K`$ be a uniform constant in $`F\le K(a^2+N^{-2})`$ for small $`a`$ and large $`N`$. Choose $`K\lambda^2\le1/2`$ and then choose $`C\ge\max\{1/\lambda^2,2K\}`$. If $`f_N\ge C/N^2`$, this gives $`a\ge1/N`$ and $`F\le f_N`$. The normalized current has leading value $`1/\log(1/f_N)`$ because $`2\log(1/a)=\log(1/f_N)+2\log(1/\lambda)`$.

For every chain with $`F\le f_N`$, the [contact-rate converse](contact_rate.md) yields

```math
J\le\Gamma\,\frac{1-f_N}{\log(1/f_N)},
```

using that $`\log(1/F)/(1-F)=\int_0^1 [F+(1-F)t]^{-1}dt`$ decreases with $`F`$. This upper bound and the constructed family give the stated supremum asymptotic.

## 6. Scientific scope

The chain synthesis and logarithmic reflection identity are inherited. [Related work](../references/RELATED_WORK.md) gives the sources for nearly rectangular quantum-dot filters, the Butterworth chain and numerical transport optimization. Here the shifted roots control both the full-line noise and the physical contact cost, so the attainable current matches the converse at leading order.

The sufficiently large constant $`C`$ in the target-noise hypothesis marks the proved range. The exact coefficient of the smallest feasible $`N^{-2}`$ noise and the finite-$`N`$ optimizer are open. The result uses full bias, flat wide-band contacts and the limit of long counting times at each finite $`N`$. Finite bias, transient timing, fabrication tolerances and other reservoir or chain models need separate analysis.
