# Scientific reading map

The smallest achievable particle-count Fano factor of the ideal serial conductor scales as $`N^{-2}`$. At fixed common contact rate $`\Gamma`$, the largest leading current at that noise scale is $`\Gamma/(2\log N)`$. The same construction attains the leading frontier across a range of vanishing noise ceilings.

## Connected route

1. [Model, observables, and claims](model.md) defines the Hamiltonian, reservoir occupations, physical rate convention, current, noise, and optimization domain.
2. [Universal size bound](size_bound.md) turns the serial chain's constant transmission numerator into a degree-$`2N`$ nonnegative polynomial and applies Markov's inequality.
3. [Legendre family](legendre_family.md) identifies an inherited least-squares filter, proves its full-line Fano upper bound, and derives its logarithmic contact-rate cost.
4. [Physical realization](realization.md) constructs a rational scattering matrix, obtains positive rank-one Cayley residues, and uses a source Krylov basis to produce exactly $`N`$ sites with endpoint contacts.
5. [Contact-rate theorem](contact_rate.md) evaluates the logarithmic reflection integral, retains asymmetric contacts, and converts it into a measured current-noise constraint.
6. [Fixed-contact current frontier](fixed_contact_frontier.md) moves the two outer Chebyshev reflection zeros and matches the current converse.
7. [Interpretation](interpretation.md) compares fixed bandwidth with fixed contact strength and explains the relation to correlated clocks and calibrated elapsed-time estimates.

## Proof dependencies

| Statement | Inputs | Conclusion |
|---|---|---|
| Universal size converse | Serial endpoint cofactor, scattering unitarity, Markov's derivative inequality | $`F\geq1/(18N^2+2)`$ |
| Constructive Fano upper bound | Legendre derivative norm and a positive-coefficient tail bound | $`F_N=O(N^{-2})`$ for the stated transmission |
| Exact site count | Stable factor, Cayley transform, positive residues, cyclic Lanczos reduction | The transmission belongs to an admissible $`N`$-site chain |
| Matching-area bound | Reflection determinant, root-integral identity, trace of the endpoint damping | $`\mathcal A\leq2\pi\Gamma_{\min}`$ |
| Current-noise bound | Transmission-weighted Jensen inequality | $`J\log(1/F)/(1-F)\leq\Gamma_{\min}`$ |
| Legendre throughput baseline | Real reflection zeros, Legendre leading coefficient, nodal-gap estimate | $`J_N/\Gamma_N\sim1/(3\log N)`$ |
| Leading current frontier | Shifted Chebyshev roots, full-line integral estimates, exact area and contact converse | $`J_N^\star(f_N;\Gamma)\sim\Gamma/\log(1/f_N)`$ for vanishing $`f_N\ge C/N^2`$ |

The constructive size law uses both the filter estimate and physical realization. The throughput statement additionally uses the matching-area and logarithmic asymptotic arguments. Finite numerical agreement is an implementation check and is not a premise of these analytical proofs.

## Sources and reproduction

The [related-work account](../references/RELATED_WORK.md) separates the inherited polynomial filter, transport formulas, and matching machinery from the claims proved here. The [bibliography](../references/references.bib) records source identities and versions.

The [verification guide](../verification/README.md) explains exact rational polynomial coefficients, high-precision root refinement, Green-function transmission, full fermionic counting calculations, numerical quadrature, and the figure. It states the tested sizes and distinguishes floating-point diagnostics from rigorous numerical certificates.

Return to the [repository overview](../README.md).

