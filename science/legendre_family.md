# The inherited Legendre filter and its transport bounds

This page proves the constructive half of the size law and computes the contact-rate cost. The polynomial is the classical least-squares $`Q_N^a`$ family of [Malvar and Calôba (1980)](../references/RELATED_WORK.md#malvar1980), expressed as a normalized Legendre derivative. The superscript $`a`$ names their subclass; it is not an adjustable parameter. The polynomial family and its least-squares characterization are inherited. The application to the full-bias Fano factor, its combination with the size converse, and the charged throughput are the claims studied here.

The [model](model.md) fixes physical rates $`\Gamma_L,\Gamma_R`$, retarded damping $`\Gamma_L/2,\Gamma_R/2`$, and

```math
I_0=\int_{\mathbb R}T(x)\,dx,\qquad
V_0=\int_{\mathbb R}T(x)[1-T(x)]\,dx,\qquad
J=\frac{I_0}{2\pi},\quad D=\frac{V_0}{2\pi},\quad F=\frac{V_0}{I_0}.
```

Energies in this page use a passband with endpoints $`-1,1`$. Rescaling every Hamiltonian coefficient and contact rate changes the speed but leaves $`F`$ unchanged.

## 1. Definition and classical least-squares characterization

Let $`P_m`$ be the Legendre polynomial normalized by $`P_m(1)=1`$. For every integer $`N\geq1`$, set

```math
p_N(x)=\frac{2P_{N+1}'(x)}{(N+1)(N+2)}
      =\frac{P_N^{(1,1)}(x)}{N+1},
\qquad
T_N(x)=\frac{1}{1+p_N(x)^2}.
```

Here $`P_N^{(1,1)}`$ is a Jacobi polynomial. The polynomial $`p_N`$ has degree $`N`$, parity $`N`$, and $`p_N(1)=1`$. Rolle's theorem applied to $`P_{N+1}`$ gives exactly $`N`$ simple real zeros in $`(-1,1)`$.

For completeness, consider the space spanned by $`P_N,P_{N-2},\ldots`$, with norm squared $`\int_0^1r(x)^2\,dx`$. Its reproducing kernel at the endpoint is

```math
K_N(x,1)=\sum_{\substack{0\leq k\leq N\\k\equiv N\pmod2}}
             (2k+1)P_k(x)=P_{N+1}'(x),
\qquad
K_N(1,1)=\frac{(N+1)(N+2)}2.
```

The derivative identity follows by telescoping
$`P_{k+1}'-P_{k-1}'=(2k+1)P_k`$. Orthogonality and Cauchy-Schwarz give

```math
1=r(1)^2
\leq K_N(1,1)\int_0^1r(x)^2\,dx
```

for every polynomial in this parity space with $`r(1)=1`$. Equality holds uniquely for $`r=K_N(\,\cdot\,,1)/K_N(1,1)=p_N`$. This identifies the normalized derivative with the classical $`Q_N^a`$ least-squares construction. It does not assert that this polynomial minimizes the nonlinear transport Fano factor.

In particular,

```math
b_N:=\int_{-1}^1p_N(x)^2\,dx
=\frac{4}{(N+1)(N+2)}.
```

## 2. A finite-size upper bound on the Fano factor

On the passband,

```math
T_N(1-T_N)=\frac{p_N^2}{(1+p_N^2)^2}\leq p_N^2,
\qquad
T_N\geq1-p_N^2.
```

Thus the passband contributes at most $`b_N`$ to $`V_0`$ and at least $`2-b_N`$ to $`I_0`$.

The tails require a separate estimate. Every Taylor coefficient of $`p_N`$ about $`x=1`$ is nonnegative. This follows, for example, from

```math
P_m^{(k)}(1)=\frac{(m+k)!}{2^k k!(m-k)!},
\qquad 0\leq k\leq m.
```

Consequently,

```math
p_N(x)\geq1+a_N(x-1)\quad(x\geq1),
\qquad
a_N=p_N'(1)=\frac{N(N+3)}4.
```

The function $`u^2/(1+u^2)^2`$ decreases for $`u\geq1`$. Parity makes the two transmission tails equal, so

```math
\begin{aligned}
\int_{|x|\geq1}T_N(x)[1-T_N(x)]\,dx
&\leq\frac2{a_N}\int_1^\infty\frac{u^2}{(1+u^2)^2}\,du\\
&=\frac2{a_N}\left(\frac\pi8+\frac14\right)
=\frac{\pi+2}{N(N+3)}.
\end{aligned}
```

Combining the passband and tail estimates proves, for every $`N\geq1`$,

```math
\boxed{
F_N\leq
\frac{\displaystyle \frac4{(N+1)(N+2)}
                  +\frac{\pi+2}{N(N+3)}}
     {\displaystyle 2-\frac4{(N+1)(N+2)}}.
}
```

The bound is deliberately simple and is not useful as a sharp estimate at $`N=1`$. Its leading upper coefficient is $`(\pi+6)/2`$. Together with the [universal serial-chain converse](size_bound.md), it establishes an order statement,

```math
\inf_{\text{connected }N\text{-site serial chains}} F
=\Theta(N^{-2}),
\qquad F_N=\Theta(N^{-2}).
```

Neither an optimal leading constant nor an exact finite-size optimizer is determined here.

The same tail argument gives

```math
2-b_N\leq I_{0,N}
\leq2+\frac2{a_N}\int_1^\infty\frac{du}{1+u^2}
=2+\frac{\pi}{2a_N},
```

and therefore

```math
I_{0,N}=2+O(N^{-2}),
\qquad
J_N=\frac1\pi+O(N^{-2}).
```

This nonzero limiting current uses fixed passband units. The next sections compute the contact rates required in those units.

## 3. The matching area determines the contact rate

The [exact realization](realization.md) uses the degree-$`N`$ stable spectral factor

```math
d_N(z)d_N^\#(z)=1+p_N(z)^2,
\qquad
d_N^\#(z)=\overline{d_N(\bar z)},
```

with all zeros of $`d_N`$ in the lower half-plane and the same positive leading coefficient as $`p_N`$. Write those zeros as $`z_j`$ and define

```math
c_N=-\sum_{j=1}^N\Im z_j>0.
```

The realization has equal physical contact rates

```math
\Gamma_{L,N}=\Gamma_{R,N}=c_N.
```

Since every zero of $`p_N`$ is real, the logarithmic matching area satisfies the exact identity

```math
\mathcal A_N
:=\int_{\mathbb R}-\log[1-T_N(x)]\,dx
=\int_{\mathbb R}\log[1+p_N(x)^{-2}]\,dx
=2\pi c_N.
```

The integrand has integrable logarithmic singularities at the reflection zeros. The equality follows by factoring $`d_N`$ and $`p_N`$ into roots and integrating the difference of logarithmic potentials. A pole at $`a-ib`$, with $`b>0`$, contributes $`2\pi b`$ to the integral of the logarithm of the squared modulus ratio. Real numerator roots contribute zero. Equal leading coefficients and equal sums of root real parts make the complete difference integrable at infinity. This is the saturated, real-reflection-zero case of the [contact-rate matching bound](contact_rate.md).

## 4. A self-contained root-spacing estimate

The following estimate is used only to control the matching area to an additive constant. It is not needed for the Fano upper bound.

Write the zeros of $`p_N`$ as $`\cos\theta_k`$, with

```math
0<\theta_1<\cdots<\theta_N<\pi.
```

The Jacobi equation for $`p_N`$ is

```math
(1-x^2)p_N''(x)-4xp_N'(x)+N(N+3)p_N(x)=0.
```

With

```math
y(\theta)=(\sin\theta)^{3/2}p_N(\cos\theta),
\qquad \lambda=N+\frac32,
```

it becomes

```math
y''(\theta)+
\left[\lambda^2-\frac{3}{4\sin^2\theta}\right]y(\theta)=0.
```

Include $`\theta_0=0`$ and $`\theta_{N+1}=\pi`$. On each nodal interval of length $`\ell_k=\theta_{k+1}-\theta_k`$, integration by parts gives

```math
\int |y'|^2
=\lambda^2\int|y|^2-\frac34\int\frac{|y|^2}{\sin^2\theta}
\leq\lambda^2\int|y|^2.
```

The endpoint intervals are legitimate: $`y=O(\theta^{3/2})`$ and $`y'=O(\theta^{1/2})`$ near zero, with analogous behavior near $`\pi`$. All integrals converge and the boundary term vanishes. The Dirichlet Poincare inequality gives

```math
\frac{\pi^2}{\ell_k^2}\int|y|^2
\leq\int|y'|^2,
\qquad
\ell_k\geq\frac{\pi}{N+3/2}.
```

Summing gaps from the left and from the right yields

```math
\frac{k\pi}{N+3/2}
\leq\theta_k
\leq\frac{(k+1/2)\pi}{N+3/2},
\qquad
\left|\theta_k-\frac{k\pi}{N+1}\right|
\leq\frac{\pi}{2(N+3/2)}.
```

This uniform angular control, including the first and last zeros, is sufficient for the logarithmic asymptotic.

## 5. Logarithmic asymptotic of the matching area

The positive leading coefficient of $`p_N`$ is

```math
L_N=2^{-N}\frac{\binom{2N+2}{N+1}}{N+2},
\qquad
\log L_N=N\log2-\frac32\log N+O(1),
```

where the second identity follows from Stirling's formula. For a real zero $`r\in(-1,1)`$, define

```math
f(r):=\int_{-1}^1\log|x-r|\,dx
=(1+r)\log(1+r)+(1-r)\log(1-r)-2.
```

The function $`g(\theta)=f(\cos\theta)`$ extends continuously to both endpoints and is Lipschitz. Indeed,

```math
|g'(\theta)|
=\sin\theta\left|\log\frac{1+\cos\theta}{1-\cos\theta}\right|
\leq2.
```

To see the bound, set $`\cos\theta=\tanh u`$; the expression becomes $`2|u|/\cosh u\leq2`$. The angular estimate above therefore gives a bounded error when replacing the roots by a uniform angular grid. An ordinary Riemann-sum estimate then gives

```math
\sum_{k=1}^N f(\cos\theta_k)
=N\,\frac1\pi\int_0^\pi f(\cos\theta)\,d\theta+O(1)
=-2N\log2+O(1).
```

For the last equality, interchange the two finite, integrable logarithmic integrals and use

```math
\frac1\pi\int_0^\pi\log|x-\cos\theta|\,d\theta=-\log2,
\qquad -1\leq x\leq1.
```

This elementary identity follows from the difference-of-cosines formula and the integral of $`\log\sin`$ over a period.

Factoring $`p_N`$ now gives

```math
\begin{aligned}
\int_{-1}^1\log|p_N(x)|\,dx
&=2\log L_N+\sum_{k=1}^N f(\cos\theta_k)\\
&=-3\log N+O(1).
\end{aligned}
```

On the passband,

```math
\log(1+p_N^{-2})
=-2\log|p_N|+\log(1+p_N^2),
\qquad
0\leq\int_{-1}^1\log(1+p_N^2)\,dx\leq b_N.
```

Outside the passband,

```math
0\leq\int_{|x|>1}\log(1+p_N^{-2})\,dx
\leq2\int_1^\infty p_N(x)^{-2}\,dx
\leq\frac2{a_N}.
```

Both correction terms are $`O(N^{-2})`$. Hence

```math
\boxed{
\mathcal A_N=6\log N+O(1),
\qquad
\Gamma_{L,N}=\Gamma_{R,N}
=\frac3\pi\log N+O(1).
}
```

All logarithms are natural. The asymptotic statements apply as $`N\to\infty`$; the exact spectral-factor and matching-area identities hold also at $`N=1`$.

## 6. Charged throughput and limits of the conclusion

If the two physical contact rates are fixed to a common value $`\Gamma_*`$, rescale the constructed Hamiltonian and both contacts by $`s_N=\Gamma_*/c_N`$. The rescaled transmission is $`T_N(E/s_N)`$, so

```math
F_N^{(\Gamma_*)}=F_N=\Theta(N^{-2}),
\qquad
\frac{J_N^{(\Gamma_*)}}{\Gamma_*}
=\frac{I_{0,N}}{2\pi c_N}
\sim\frac1{3\log N}.
```

The chain therefore achieves the best possible order in the number of sites while its current decreases logarithmically at fixed contact strength. It does not maintain a nonzero limiting current and a vanishing Fano factor at fixed rates.

The contact converse

```math
J\,\frac{\log(1/F)}{1-F}\leq\min(\Gamma_L,\Gamma_R)
```

shows that a logarithmic loss of current is unavoidable for any family with $`F=\Theta(N^{-2})`$ and fixed contact rates. This construction attains that order. Its ratio to the displayed contact bound tends to $`2/3`$, because $`\log(1/F_N)=2\log N+O(1)`$. This is an order-optimal tradeoff, not saturation of the converse constant.

For $`N=1`$, the exact check is

```math
p_1(x)=x,\quad
T_1(x)=\frac1{1+x^2},\quad
\Gamma_L=\Gamma_R=1,\quad
J=\frac12,\quad D=\frac14,\quad F=\frac12.
```

Finite computations are recorded in [filter_results.json](../verification/data/filter_results.json) and generated by [check_filters.py](../verification/check_filters.py). They test the physical realization and the stated finite bounds. They do not replace the proofs, certify arbitrary-precision roots by intervals, or establish an optimal asymptotic Fano constant.

