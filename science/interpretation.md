# Precision, current, and the serial-chain resource

The size theorem and the contact theorem answer different physical questions. The first fixes the best asymptotic reduction in relative counting noise when the number of sites grows. The second determines the current that can accompany that reduction when the contact rates are bounded.

## 1. What is optimal

For the [model defined here](model.md), the infimum over all connected serial chains obeys

```math
F_N^\star=\Theta(N^{-2}).
```

The lower bound allows arbitrary onsite energies, nonzero nearest-neighbor hoppings, and unequal positive contacts. The upper construction needs only zero onsite energies, mirror-symmetric hoppings, and equal contacts. Global rescaling makes its two contact rates equal to any prescribed common positive value without changing $`F`$.

The theorem establishes an optimal exponent. Its explicit constants leave a gap, and the inherited least-squares filter is not proved to be the exact finite-size minimizer of the full-line Fano ratio. The number of sites is also a geometric resource: the constant transmission numerator comes from the unique path along the chain. Counting all states in the fermionic Fock space would give a different resource, $`2^N`$.

No bound on the hopping magnitudes or manufacturing errors is included in the optimization. The construction gives finite couplings at each finite size; precision of their physical control is a separate implementation question.

## 2. Why nearly perfect transmission reduces noise

At full bias, each energy mode contributes $`T`$ to current and $`T(1-T)`$ to the count-variance rate. A perfectly transmitting interval would carry current with no partition noise. A finite chain has a rational transmission with smooth edges and residual reflection, and these regions contribute to $`V_0`$.

The [size proof](size_bound.md) makes this obstruction quantitative without choosing a special filter. On a region with transmission at least one half, the polynomial $`q=T^{-1}-1`$ must rise to one at the boundary. A degree-$`2N`$ polynomial cannot make those transitions arbitrarily narrow relative to the region's length. Markov's derivative inequality forces enough partition noise to obtain the universal lower bound.

The [Legendre family](legendre_family.md) allocates its reflection so that both the passband contribution and the exterior contribution are of order $`N^{-2}`$. The [synthesis](realization.md) turns this transmission into a physical serial chain with exactly the counted number of sites.

## 3. The contact budget per transmitted particle

The operational form of the contact theorem is

```math
\frac{\min(\Gamma_L,\Gamma_R)}{J}
\ge
\frac{\log(1/F)}{1-F}.
```

Its left side is a contact-rate budget measured per unit transmitted current. For small $`F`$, the required budget grows as $`\log(1/F)`$. Therefore increasing the number of sites cannot make $`F`$ vanish while both the contact rates and a positive current remain fixed.

For any family with $`F_N=\Theta(N^{-2})`$,

```math
\frac{J_N}{\Gamma_{\min,N}}
\le
\frac{1}{2\log N+O(1)}.
```

The explicit construction gives

```math
\frac{J_N}{\Gamma_N}
\sim\frac{1}{3\log N}.
```

These statements match in logarithmic order. They do not fix the best leading coefficient under a prescribed noise prefactor.

The resource can be accounted for in either of two equivalent normalizations:

| Quantity | Fixed passband $`[-1,1]`$ | Fixed equal contact rate $`\Gamma`$ |
|---|---|---|
| Fano factor | $`\Theta(N^{-2})`$ | $`\Theta(N^{-2})`$ |
| Mean current | $`1/\pi+O(N^{-2})`$ | $`\Gamma/[3\log N]\,(1+o(1))`$ |
| Rate at each contact | $`(3/\pi)\log N+O(1)`$ | $`\Gamma`$ |

The first normalization spends an increasing contact rate. The second rescales the conductor's entire energy axis and pays the same cost through a decreasing current. The Fano factor is invariant under that rescaling.

## 4. The ideal boxcar limit

For a reflection probability $`1-T`$ that is at most $`\varepsilon`$ throughout an interval of width $`B`$, the logarithmic reflection sum rule immediately gives

```math
B\log(1/\varepsilon)
\le
\int_{\mathbb R}-\log[1-T(E)]\,dE
\le2\pi\Gamma_{\min}.
```

This is the familiar bandwidth-reflection content of a matching-area bound. The [current-weighted convexity step](contact_rate.md) converts that spectral constraint into a statement involving measured current and noise, without assuming a prescribed passband.

A nonzero-width, perfectly transmitting boxcar has $`F=0`$ and $`J>0`$. Approaching it within the stated contact model requires an increasing contact budget. A claim about an infinite perfect-transmission system must therefore specify which rates, bandwidths, or reservoir assumptions change in the limit.

## 5. Relation to correlated clocks

The endpoint-driven chain in [Meier et al.](../references/RELATED_WORK.md#meier2026) provides a direct clock interpretation: an emitted particle is counted as a tick. Their finite-chain optimization reports an approximate $`N^{-1.86}`$ noise law, while the earlier Butterworth family has an inverse-linear law. The present size result establishes the asymptotically optimal exponent for the same serial transport class and supplies an explicit attaining family.

The current $`J`$ is the mean tick rate. Small $`F`$ describes correlations that reduce fluctuations in the accumulated count. It does not by itself determine the variance of an individual waiting time or how long a finite-time logarithmic variance regime persists.

A direct operational consequence can be stated for the calibrated elapsed-time estimate $`\widehat t=K_t/J`$. For each fixed finite chain in its long-time regime,

```math
\mathrm{Var}\widehat t
=\frac{F}{J}\,t+o(t).
```

For the constructed family at fixed contact rate,

```math
\frac{F_N}{J_N}
=\Theta\!\left(\frac{\log N}{\Gamma N^2}\right).
```

The logarithmic throughput cost consequently enters an absolute timing-variance measure as well as the mean tick rate. This is an ordered-limit statement: first the long-time coefficient is defined for finite $`N`$, and then its size dependence is examined. No size-uniform relaxation time or finite-time crossover law is inferred.

## 6. Scope of the physical conclusion

The proof uses fully occupied and empty flat reservoirs, noninteracting transport, local energy-independent contacts, and a serial nearest-neighbor Hamiltonian. A finite bias window or nonzero reservoir temperature changes the current and noise weights. Interactions and dephasing change the scattering description. Parallel paths, side resonances, and structured reservoirs can remove the constant-numerator reduction underlying the size theorem.

These boundaries locate the result in a concrete class of coherent devices. The [related-work account](../references/RELATED_WORK.md) identifies the inherited filter, scattering, polynomial, and matching ingredients. The [verification guide](../verification/README.md) documents the finite checks supporting the implementations and normalization conventions.

