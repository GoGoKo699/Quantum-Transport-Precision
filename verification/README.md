# Verification and reproduction

The analytical claims are proved in the [scientific account](../science/README.md). The calculations here test the finite physical construction, normalization conventions, numerical integrals, and agreement of independent formulations.

## Environment and complete check

The committed record was generated with Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, and mpmath 1.3.0. The figure uses Matplotlib 3.10.8. All four package versions are pinned in [requirements.txt](requirements.txt).

From the repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r verification/requirements.txt
.venv/bin/python verification/run_all.py
```

The last command recomputes the numerical checks, compares the current and noise observables with the committed records using explicit floating-point tolerances, and checks relative Markdown links and basic mathematical-delimiter structure. It does not change the stored results.

## What each calculation establishes

| Calculation | Implementation | Recorded domain | Evidence |
|---|---|---|---|
| Exact polynomial coefficients and physical synthesis | [filters.py](filters.py), [check_filters.py](check_filters.py) | $`N=1,2,3,4,6,8,12,16`$ | Positive residues and hoppings, exactly $`N`$ sites, endpoint drain support, zero onsite energies, mirror symmetry, and target transmission |
| Full-line polynomial integrals and contact area | [check_filters.py](check_filters.py) | $`N=1,2,3,4,6,8,12,16,32,64,128`$ | Current, count noise, finite analytical bounds, and the contact-rate constraint |
| Direct Green-function integration | [check_filters.py](check_filters.py) | $`N=1,4,16`$ | Integrated physical transmission agrees with the target polynomial integrals |
| Refined quadrature | [check_filters.py](check_filters.py) | $`N=32,128`$ | Stability when tightening tolerances in the narrow edge layer |
| Full fermionic counting dynamics | [check_counting.py](check_counting.py) | Eight cases with $`1\leq N\leq4`$ | Lindblad current and noise agree with scattering integrals and covariance current |
| Figure reproduction | [plot_results.py](plot_results.py) | Committed quadrature rows | The displayed curves follow the stored data and stated analytical formulas |

The data are in [filter_results.json](data/filter_results.json) and [counting_results.json](data/counting_results.json). Each record identifies its methods and conventions.

## Physical synthesis

The normalized Legendre polynomial is first generated with exact rational coefficients. Double-precision orthogonal-basis roots provide initial guesses, followed by 90-digit root refinement. The code forms the stable spectral factor, computes the real Cayley poles and positive rank-one residues, and performs reorthogonalized Lanczos reduction.

Zero onsite energies and mirror symmetry are not imposed on the computed matrix. Their residuals are measured, as are orthogonality, tridiagonal structure, and drain support outside the last site. The resulting matrix and physical contact rates are then converted to double precision for the independent Green-function evaluation.

The transmission comparison samples the passband, all reflection zeros, the $`O(N^{-2})`$ edge layer, and distant tails. It also checks the invariance under a common rescaling of energies and physical rates. The root solver is a moderate-size numerical realization, not a certified arbitrary-order compiler.

## Current and noise quadrature

The target transmission is evaluated through the Gegenbauer representation of the normalized Legendre derivative. The code computes $`T(1-T)`$ as $`p^2/(1+p^2)^2`$, avoiding cancellation near perfect transmission.

Interior quadrature is split at the real reflection zeros. Exterior quadrature uses the scaled coordinate $`y=N^2(x-1)`$ to resolve the edge layer. For the matching area, the integrable logarithmic singularities are integrated analytically through the real-root product; only smooth corrections are handled numerically.

At the two refinement sizes, the absolute tolerance changes from $`2\times10^{-12}`$ to $`5\times10^{-14}`$ and the relative tolerance from $`2\times10^{-11}`$ to $`5\times10^{-13}`$. The recorded observables did not change at the stored precision. QUADPACK error estimates do not bound every possible rounding or root error.

## Independent full counting calculation

For each small test chain, [check_counting.py](check_counting.py) constructs the annihilation operators on the full $`2^N`$-dimensional fermionic Fock space. It builds the Lindblad superoperator directly, counts only the drain jump, and obtains the stationary state from a trace-constrained linear system.

Let $`\mathcal L`$ be the un-tilted generator, $`\mathcal J`$ the drain-jump superoperator, and $`\rho_0`$ the stationary state. The first counting-field response obeys

```math
\mathcal L\rho_1=J\rho_0-\mathcal J\rho_0,
\qquad
\operatorname{tr}\rho_1=0.
```

Differentiating the tilted-generator eigenvalue equation gives

```math
J=\operatorname{tr}(\mathcal J\rho_0),
\qquad
D=J+2\operatorname{tr}(\mathcal J\rho_1).
```

This calculation obtains the noise without using the transmission-noise integral. It is compared with direct Green-function quadrature, while the stationary covariance Lyapunov equation supplies a third calculation of the current.

The eight cases comprise two one-site conductors, three disordered chains with unequal contacts, and the constructed chains at $`N=2,3,4`$. Density-matrix trace, positivity to numerical tolerance, stationarity, and the counting-response residual are also checked. The exact one-site current and Fano formulas test both asymmetric rates and the factor of two between physical rates and retarded half-widths.

## Recorded numerical agreement

| Comparison | Maximum absolute discrepancy |
|---|---:|
| Physical Green transmission versus target filter | $`4.78\times10^{-15}`$ |
| Spectral-factor contact rate versus matching area | $`9.33\times10^{-15}`$ |
| Integrated physical current/noise versus polynomial calculation | $`4.45\times10^{-16}`$ |
| Full Lindblad versus scattering/covariance statistics | $`1.00\times10^{-15}`$ |

These are observed floating-point discrepancies, rounded upward for display. They are not rigorous interval bounds and need not reproduce bit-for-bit on every platform. The validation scripts use documented numerical tolerances.

Selected values from the constructed family are:

| $`N`$ | $`F_N`$ | $`N^2F_N`$ | $`J_N/\Gamma_N`$ |
|---:|---:|---:|---:|
| 16 | 0.00763706632649 | 1.95508897958 | 0.123223100087 |
| 32 | 0.002075612439 | 2.125427138 | 0.099358599 |
| 64 | 0.0005423289553 | 2.221379401 | 0.082803834 |
| 128 | 0.000138699999280 | 2.27246078820 | 0.070811931467 |

The analytical proofs establish the inverse-square order and logarithmic rate cost. The numerical values above do not determine an optimal leading Fano constant.

## Individual commands and result regeneration

```bash
.venv/bin/python verification/check_filters.py
.venv/bin/python verification/check_counting.py
.venv/bin/python verification/plot_results.py
```

The figure command reads the committed data and writes [precision_throughput.svg](../science/figures/precision_throughput.svg). Its shaded region consists of the proved lower and upper bounds on the optimum; the construction and Butterworth curves are separate achievable examples. The current panel evaluates the contact bound at the constructed Fano factors.

To deliberately regenerate the numerical records after reviewing a scientific or implementation change:

```bash
.venv/bin/python verification/check_filters.py --write-results
.venv/bin/python verification/check_counting.py --output verification/data/counting_results.json
.venv/bin/python verification/plot_results.py
.venv/bin/python verification/run_all.py
```

The complete check also verifies the stored observables against newly computed values. Basic source checks do not certify hosted mathematical rendering. The numerical suite does not prove the theorems, test finite-temperature or interacting extensions, establish a transient crossover law, or certify physical robustness against control errors.

