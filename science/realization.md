# Exact endpoint realization of the polynomial filter

This page gives a finite constructive proof that the transmission

```math
T(x)=\frac1{1+p(x)^2}
```

comes from a connected chain with exactly $`N=\deg p`$ sites, two endpoint contacts, and no additional modes. The proof is an explicit instance of classical lossless spectral-factor and reactance synthesis, followed by a Jacobi-matrix realization. These synthesis principles are inherited from classical network theory; see [related work](../references/RELATED_WORK.md#synthesis). The [Legendre family](legendre_family.md) used here is also inherited from [Malvar and Calôba (1980)](../references/RELATED_WORK.md#malvar1980).

The value of spelling out the realization is to verify the particular physical resource count: a two-terminal scattering formula alone would not establish a nearest-neighbor quantum chain with $`N`$ orbitals.

## 1. Statement and conventions

Let $`p`$ be any real polynomial of degree $`N\geq1`$ with positive leading coefficient $`L`$. There exist a real symmetric tridiagonal matrix $`H`$ with strictly positive off-diagonal entries, and equal positive physical rates $`\Gamma_L=\Gamma_R`$, such that

```math
T(x)=\Gamma_L\Gamma_R
\left|
\left[
xI-H+\frac i2
  \big(\Gamma_L|1\rangle\langle1|
      +\Gamma_R|N\rangle\langle N|\big)
\right]^{-1}_{1N}
\right|^2
=\frac1{1+p(x)^2}.
```

For $`N=1`$, both contacts act on the same orbital and their damping contributions add.

If $`p(-x)=(-1)^Np(x)`$, the constructed chain has zero onsite energies. The construction also has mirror-symmetric hoppings. These statements apply in particular to the $`p_N`$ of [legendre_family.md](legendre_family.md).

The broad existence statement does not require real reflection zeros. The exact matching-area equality used for the Legendre contact cost does require them.

## 2. Stable spectral factor, including multiplicities

The polynomial $`1+p(z)^2`$ is strictly positive on the real axis and has degree $`2N`$. Its nonreal zeros occur in conjugate pairs, counted with algebraic multiplicity. Define

```math
d(z)=L\prod_{\substack{1+p(z_j)^2=0\\\Im z_j<0}}
            (z-z_j).
```

There are exactly $`N`$ lower-half-plane zeros counted with multiplicity. Thus

```math
d(z)d^\#(z)=1+p(z)^2,\qquad
d^\#(z)=\overline{d(\bar z)}.
```

The leading coefficient and the choice of half-plane make $`d`$ unique. Multiple zeros of $`1+p^2`$ cause no difficulty: they are retained with their full multiplicity. No assumption that the dissipative poles are simple is needed.

Write

```math
d(z)=A(z)+iB(z)
```

with real polynomials $`A,B`$. Since $`d`$ and $`p`$ share leading coefficient $`L`$, the degree of $`A`$ is $`N`$ and the degree of $`B`$ is at most $`N-1`$. The spectral-factor identity becomes

```math
A^2+B^2=p^2+1.
```

## 3. A rational inner scattering matrix

Define

```math
S(z)=\frac1{d(z)}
\begin{pmatrix}p(z)&i\\ i&p(z)\end{pmatrix}.
```

This matrix is analytic in the upper half-plane and approaches the identity as $`z\to\infty`$. It is unitary on the real axis, because $`|d(x)|^2=1+p(x)^2`$ and the off-diagonal terms in $`S(x)S(x)^\dagger`$ vanish.

The constant even and odd port basis diagonalizes $`S`$ with eigenvalues

```math
s_\pm(z)=\frac{p(z)\pm i}{d(z)}.
```

Each is a rational function analytic in the upper half-plane, has modulus one on the real axis, and tends to one at infinity. The maximum-modulus principle on large half-disks therefore gives $`|s_\pm(z)|\leq1`$ in the upper half-plane. This also proves that $`I+S(z)`$ is invertible there: a contractive scalar analytic function attaining the value $`-1`$ at an interior point would be identically $`-1`$, contradicting its value at infinity.

Take the Cayley transform

```math
K(z)=-i[I-S(z)][I+S(z)]^{-1}.
```

Its imaginary part is negative semidefinite in the upper half-plane. Direct algebra using $`A^2+B^2=p^2+1`$ gives the real symmetric rational expression

```math
\boxed{
K(z)=\frac{B(z)I-\sigma_x}{R(z)},
\qquad
R(z):=A(z)+p(z),
\qquad
\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
}
```

In particular, $`K(z)=O(1/z)`$ at infinity, and its off-diagonal entry is exactly $`-1/R(z)`$.

## 4. Exactly N real Cayley poles and positive rank-one residues

Here is the pole-counting step that excludes hidden states or a larger network.

A real rational scalar function analytic in the upper half-plane and with nonpositive imaginary part there can have only simple real poles, with nonnegative residues. For this special rational setting the argument is elementary. A nonreal pole is excluded by upper-half-plane analyticity and complex-conjugation symmetry. Near a real pole of order at least two, the imaginary part of the leading Laurent term changes sign as the point approaches along different angles in the upper half-plane. A simple real pole $`w/(z-h)`$ has nonpositive imaginary part only if $`w\geq0`$. Apply this argument to every real quadratic form of $`K`$ to obtain positive-semidefinite residue matrices.

The polynomial $`R=A+p`$ has degree exactly $`N`$ and leading coefficient $`2L`$. Its roots cannot cancel from the whole matrix, since $`K_{LR}=-1/R`$ has a constant nonzero numerator. The preceding pole argument consequently proves that $`R`$ has exactly $`N`$ distinct real zeros, denoted by $`h_1,\ldots,h_N`$.

At a zero of $`R`$, the identity $`A^2+B^2=p^2+1`$ gives

```math
A(h_j)=-p(h_j),\qquad B(h_j)^2=1.
```

The residue is therefore

```math
\mathrm{Res}_{z=h_j}K(z)
=\frac1{R'(h_j)}
\begin{pmatrix}B(h_j)&-1\\-1&B(h_j)\end{pmatrix}
=w_j
\begin{pmatrix}1&-B(h_j)\\-B(h_j)&1\end{pmatrix},
\qquad
w_j:=\frac{B(h_j)}{R'(h_j)}>0.
```

It has rank one. Strict positivity of $`w_j`$ follows because the residue is nonzero and positive semidefinite, while its two diagonal entries agree.

Define

```math
H_0=\mathrm{diag}(h_1,\ldots,h_N),\qquad
(b_L)_j=\sqrt{w_j},\qquad
(b_R)_j=-B(h_j)\sqrt{w_j},\qquad
W=(b_L,b_R).
```

Since $`K`$ has no polynomial part,

```math
K(z)=W^{\mathsf T}(zI-H_0)^{-1}W.
```

Inverting the Cayley transform and using the resolvent identity yields

```math
S(z)
=I-2iW^{\mathsf T}
  (zI-H_0+iWW^{\mathsf T})^{-1}W.
```

This already gives a passive $`N`$-mode realization. The next step puts the modes on a serial chain and places the contacts at its endpoints.

## 5. Lanczos reduction puts the two contacts at opposite endpoints

Expand the off-diagonal entry of $`K`$ at infinity:

```math
b_R^{\mathsf T}(zI-H_0)^{-1}b_L
=\sum_{k\geq0}\frac{b_R^{\mathsf T}H_0^kb_L}{z^{k+1}}
=-\frac1{R(z)}=O(z^{-N}).
```

Hence

```math
b_R^{\mathsf T}H_0^kb_L=0,
\qquad k=0,\ldots,N-2.
```

For $`N=1`$, this list is empty, as it should be. Because the $`h_j`$ are distinct and every source weight $`w_j`$ is positive, $`b_L`$ is cyclic: the vectors

```math
b_L,\ H_0b_L,\ \ldots,\ H_0^{N-1}b_L
```

span the full $`N`$-dimensional space. This follows directly from the invertibility of the Vandermonde matrix in the $`h_j`$.

Apply Lanczos orthogonalization to these vectors, starting from $`b_L/\|b_L\|`$, and choose positive recursion coefficients. It produces a real orthogonal matrix $`U`$ for which

```math
H=U^{\mathsf T}H_0U
```

is tridiagonal with all $`N-1`$ hoppings strictly positive. Cyclicity excludes an early termination or a disconnected bond. The first $`N-1`$ Lanczos vectors span the Krylov subspace generated by powers through $`N-2`$. The vanishing cross moments therefore imply

```math
U^{\mathsf T}b_L=\|b_L\|e_1,\qquad
U^{\mathsf T}b_R=\eta\|b_R\|e_N,\qquad \eta\in\{+1,-1\}.
```

The sign $`\eta`$ is an unobservable drain-channel phase. Both contacts act on the same basis vector when $`N=1`$.

Thus

```math
U^{\mathsf T}WW^{\mathsf T}U
=\|b_L\|^2|1\rangle\langle1|
+\|b_R\|^2|N\rangle\langle N|.
```

Comparing with the physical retarded Green function fixes the rates, including the factor of two:

```math
\boxed{
\Gamma_L=2\|b_L\|^2,\qquad
\Gamma_R=2\|b_R\|^2.
}
```

Because $`B(h_j)^2=1`$, the two norms and the two contact rates agree. The physical transmission is the squared modulus of the off-diagonal scattering amplitude, so it is exactly $`1/|d(x)|^2=1/[1+p(x)^2]`$.

There are exactly $`N`$ sites and no hidden dynamical modes: the source Krylov space has dimension $`N`$, and $`S_{LR}=i/d`$ has no polynomial cancellation. In fact, the physical characteristic determinant is precisely $`d(z)/L`$. Repeated roots of $`d`$ are allowed and do not reduce this degree.

## 6. Zero onsite energies and mirror symmetry

Suppose now that $`p(-z)=(-1)^Np(z)`$. The lower-half-plane roots of $`1+p^2`$ are invariant under $`z\mapsto-\bar z`$, including multiplicity. Uniqueness of the normalized stable factor gives

```math
d(-\bar z)=(-1)^N\overline{d(z)}.
```

Accordingly, $`A`$ and $`R`$ have parity $`N`$, while $`B`$ has parity $`N-1`$. The Cayley poles occur in pairs $`h,-h`$, with a possible zero pole, and

```math
\frac{B(-h)}{R'(-h)}=\frac{B(h)}{R'(h)}.
```

The source spectral measure $`\sum_jw_j\delta_{h_j}`$ is therefore even. Its orthogonal polynomials alternate in parity, so every diagonal Lanczos coefficient is zero. This proves $`H_{jj}=0`$ without imposing it by hand.

Mirror symmetry follows from a separate identity and does not need the parity assumption. The equality $`K_{LL}=K_{RR}`$ and equality of the contact norms show that the normalized spectral measures at the first and last sites of the Jacobi matrix coincide. A finite Jacobi matrix with positive hoppings is uniquely reconstructed from its first-site spectral measure by the three-term orthogonal-polynomial recurrence. Reversing the chain converts the last-site measure into the first-site measure. Uniqueness therefore implies

```math
H_{jj}=H_{N+1-j,N+1-j},
\qquad
H_{j,j+1}=H_{N-j,N+1-j}.
```

For the parity-$`N`$ Legendre family, all onsite entries vanish and the positive hoppings are mirror symmetric. No additional contact or control resource was introduced to obtain these properties.

## 7. Spectral sum and the physical contact rate

Write the stable-factor zeros as $`z_j`$ and put

```math
c=-\sum_{j=1}^N\Im z_j>0.
```

The coefficient of $`z^{N-1}`$ in $`d`$ is $`-L\sum_jz_j`$, so

```math
B(z)=Lc\,z^{N-1}+O(z^{N-2}),
\qquad
R(z)=2Lz^N+O(z^{N-1}).
```

Comparing the diagonal Laurent coefficient in $`K`$ gives

```math
\|b_L\|^2=\|b_R\|^2=\frac c2,
\qquad
\boxed{\Gamma_L=\Gamma_R=c.}
```

If all reflection zeros are real, factoring $`d/p`$ into logarithmic potentials gives

```math
\int_{\mathbb R}\log[1+p(x)^{-2}]\,dx
=2\pi c
=\pi(\Gamma_L+\Gamma_R).
```

For complex reflection zeros the equality has a subtraction term; it must not be applied unchanged. The [contact-rate proof](contact_rate.md) gives the general inequality. For the Legendre family every reflection zero is real, and [legendre_family.md](legendre_family.md) proves $`c=(3/\pi)\log N+O(1)`$.

## 8. One-site check and numerical scope

For $`p(x)=x`$,

```math
d(z)=z+i,\quad
R(z)=2z,\quad
K(z)=\frac1{2z}
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
```

Thus $`H=(0)`$, $`\|b_L\|^2=\|b_R\|^2=1/2`$, and the physical rates are both one. The retarded denominator is $`x+i`$, since both half-rates act on the same orbital. Consequently

```math
T(x)=\frac1{1+x^2},\qquad
I_0=\pi,\quad V_0=\frac\pi2,\quad
J=\frac12,\quad D=\frac14,\quad F=\frac12.
```

The implementation in [filters.py](../verification/filters.py) follows this construction with exact rational input coefficients, high-precision refinement of the stable-factor and Cayley roots, and reorthogonalized Lanczos reduction. It does not impose zero onsite energies or mirror symmetry on the computed coefficients. Those properties, the endpoint support of the drain vector, residue positivity, and Green-function agreement are checked numerically.

The recorded physical synthesis tests reach $`N=16`$. Polynomial quadrature extends to $`N=128`$ without synthesizing a large power-basis chain. These are finite floating-point diagnostics and independent implementation checks. They are not interval certificates for the roots, nor a promise that this numerical routine remains well-conditioned at arbitrary $`N`$.

