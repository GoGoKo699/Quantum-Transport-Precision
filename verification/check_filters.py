#!/usr/bin/env python3
"""Finite numerical checks of polynomial filters and endpoint-chain synthesis.

Run from any working directory:
    python verification/check_filters.py
    python verification/check_filters.py --write-results

The default run checks the calculations without changing files.  --write-results
writes the deterministic numerical record, optionally to a supplied path.
These checks are floating-point diagnostics, not interval certificates.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import platform
import warnings

import mpmath
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.special import roots_jacobi

from filters import (
    chain_transmission,
    filter_integrals,
    legendre_transmission,
    synthesize_chain,
)


SYNTHESIS_SIZES = (1, 2, 3, 4, 6, 8, 12, 16)
QUADRATURE_SIZES = (1, 2, 3, 4, 6, 8, 12, 16, 32, 64, 128)
WORKING_DIGITS = 90
DEFAULT_RECORD = Path(__file__).resolve().parent / "data" / "filter_results.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def energy_grid(n: int) -> np.ndarray:
    """Resolve the passband, reflection zeros, edge layer, and distant tails."""
    roots = roots_jacobi(n, 1, 1)[0]
    edge = 1 + np.array([-4, -1, -0.1, 0, 0.1, 1, 4, 16]) / n**2
    return np.unique(np.concatenate([
        np.linspace(-1.4, 1.4, 161), roots, edge, -edge, [-4, 4],
    ]))


def physical_integrals(chain: dict) -> dict:
    """Integrate the chain's Green function without the target polynomial."""
    n = chain["N"]
    positive_roots = roots_jacobi(n, 1, 1)[0]
    positive_roots = positive_roots[positive_roots > 0].tolist()
    options = dict(epsabs=2e-12, epsrel=2e-11, limit=300)

    def current_integrand(x):
        return chain_transmission(chain, x)

    def noise_integrand(x):
        transmission = chain_transmission(chain, x)
        # Roundoff can make T exceed 1 by O(machine precision) at a reflection
        # zero.  Keep that signed roundoff rather than clipping the observable.
        return transmission * (1 - transmission)

    with warnings.catch_warnings():
        warnings.simplefilter("error")
        inside_i, ei = quad(current_integrand, 0, 1,
                            points=positive_roots, **options)
        inside_v, ev = quad(noise_integrand, 0, 1,
                            points=positive_roots, **options)
        outside_i, eoi = quad(
            lambda y: current_integrand(1 + y/n**2)/n**2,
            0, np.inf, **options,
        )
        outside_v, eov = quad(
            lambda y: noise_integrand(1 + y/n**2)/n**2,
            0, np.inf, **options,
        )
    i0 = 2 * (inside_i + outside_i)
    v0 = 2 * (inside_v + outside_v)
    return {
        "N": n, "I0": i0, "V0": v0, "F": v0/i0,
        "quadrature_error_estimates": {"I0": 2*(ei+eoi), "V0": 2*(ev+eov)},
    }


def run_checks() -> dict:
    quadrature = {n: filter_integrals(n) for n in QUADRATURE_SIZES}
    for n, row in quadrature.items():
        require(0 < row["F"] < 1, f"N={n}: F outside (0,1)")
        require(row["F"] >= row["analytic_F_lower"] - 2e-12,
                f"N={n}: lower F bound violated")
        require(row["F"] <= row["analytic_F_upper"] + 2e-12,
                f"N={n}: upper F bound violated")
        require(row["contact_bound_ratio"] <= 1 + 2e-11,
                f"N={n}: contact-rate bound violated")
        b_n = 4/((n+1)*(n+2))
        a_n = n*(n+3)/4
        require(2-b_n-2e-11 <= row["I0"] <= 2+math.pi/(2*a_n)+2e-11,
                f"N={n}: current integral bound violated")

    # The exactly solvable one-orbital conductor checks both contact half-rates
    # and the convention D=lim Var(count)/time, without an extra factor of two.
    one = quadrature[1]
    exact_one = {
        "I0": math.pi, "V0": math.pi/2, "J": 0.5, "D": 0.25,
        "F": 0.5, "Gamma_L": 1.0, "Gamma_R": 1.0,
        "matching_area": 2*math.pi,
    }
    for key, exact in exact_one.items():
        require(abs(one[key]-exact) < 3e-11,
                f"N=1: {key} differs from its analytic value")

    physical = []
    chains = {}
    for n in SYNTHESIS_SIZES:
        chain = synthesize_chain(n, dps=WORKING_DIGITS)
        chains[n] = chain
        matrix = chain["H"]
        require(matrix.shape == (n, n), f"N={n}: incorrect site count")
        require(np.allclose(matrix, matrix.T, rtol=0, atol=1e-14),
                f"N={n}: Hamiltonian is not real symmetric")
        require(all(t > 0 for t in chain["hoppings"]),
                f"N={n}: chain is disconnected or has negative hopping")
        require(chain["Gamma_L"] > 0 and chain["Gamma_R"] > 0,
                f"N={n}: nonpositive contact rate")
        diagnostics = chain["diagnostics"]
        for key, value in diagnostics.items():
            if key.endswith("_residual") or key in (
                "drain_nonendpoint_norm", "onsite_maximum",
            ):
                require(value < 1e-50,
                        f"N={n}: high-precision diagnostic {key}={value}")
        energies = energy_grid(n)
        differences = [
            abs(chain_transmission(chain, float(x))
                - legendre_transmission(n, float(x)))
            for x in energies
        ]
        transmission_error = max(differences)
        require(transmission_error < 2e-11,
                f"N={n}: physical transmission disagrees with target")
        rate_error = max(abs(chain[key] - quadrature[n][key])
                         for key in ("Gamma_L", "Gamma_R"))
        require(rate_error < 5e-11,
                f"N={n}: spectral contact rate disagrees with matching area")

        # Rescaling H and both physical rates must preserve the whole
        # transmission curve in rescaled energy units, hence its Fano factor.
        scale = 1/chain["Gamma_L"]
        scaled = {
            **chain, "H": matrix*scale,
            "Gamma_L": chain["Gamma_L"]*scale,
            "Gamma_R": chain["Gamma_R"]*scale,
        }
        scaling_error = max(
            abs(chain_transmission(scaled, float(x)*scale)
                - chain_transmission(chain, float(x)))
            for x in energies
        )
        require(scaling_error < 2e-11,
                f"N={n}: global energy/rate rescaling failed")
        physical.append({
            "N": n, "H": matrix.tolist(),
            "hoppings": chain["hoppings"].tolist(),
            "Gamma_L": chain["Gamma_L"], "Gamma_R": chain["Gamma_R"],
            "high_precision": chain["high_precision"],
            "diagnostics": diagnostics,
            "transmission_sample_count": len(energies),
            "transmission_max_absolute_error": transmission_error,
            "matching_area_rate_absolute_error": rate_error,
            "rescaled_transmission_max_absolute_error": scaling_error,
        })

    physical_checks = []
    for n in (1, 4, 16):
        row = physical_integrals(chains[n])
        row["absolute_differences_from_polynomial"] = {
            key: abs(row[key] - quadrature[n][key])
            for key in ("I0", "V0", "F")
        }
        require(max(row["absolute_differences_from_polynomial"].values()) < 5e-11,
                f"N={n}: integrated physical current/noise disagrees with filter")
        physical_checks.append(row)

    # Resolve the concrete risk of a narrow O(N^-2) edge layer at the largest
    # quadrature size by tightening tolerances.  No larger physical synthesis
    # is inferred from this polynomial-only calculation.
    refinement_checks = []
    for n in (32, 128):
        refined = filter_integrals(n, epsabs=5e-14, epsrel=5e-13)
        difference = {
            key: abs(refined[key] - quadrature[n][key])
            for key in ("I0", "V0", "F", "Gamma_L")
        }
        require(max(difference.values()) < 5e-11,
                f"N={n}: quadrature changes under tolerance refinement")
        refinement_checks.append({
            "N": n, "refined_epsabs": 5e-14, "refined_epsrel": 5e-13,
            "absolute_differences": difference,
            "refined_quadrature_error_estimates":
                refined["quadrature_error_estimates"],
        })

    return {
        "metadata": {
            "schema_version": 1,
            "generator": "verification/check_filters.py",
            "python": platform.python_version(),
            "dependencies": {
                "numpy": np.__version__, "scipy": scipy.__version__,
                "mpmath": mpmath.__version__,
            },
            "working_decimal_digits_for_synthesis": WORKING_DIGITS,
            "physical_rate_convention": "retarded damping Gamma_L/2 and Gamma_R/2",
            "noise_convention": "D = lim_{t->infinity} Var(count)/t = V0/(2*pi)",
            "synthesis_method": (
                "exact rational input coefficients; orthogonal-basis root seeds; "
                "mpmath Newton refinement; stable spectral factor; Cayley "
                "residues; reorthogonalized Lanczos; double-precision Green solve"
            ),
            "quadrature_method": (
                "Gegenbauer polynomial evaluation; adaptive passband quadrature "
                "split at reflection zeros; tails in y=N^2*(x-1); matching-area "
                "log singularities integrated analytically by real-root product"
            ),
            "scope": (
                "finite floating-point diagnostics, not interval certification; "
                "physical chains through N=16, polynomial quadrature through N=128"
            ),
        },
        "quadrature": list(quadrature.values()),
        "physical_chains": physical,
        "physical_integral_checks": physical_checks,
        "quadrature_refinement_checks": refinement_checks,
        "exact_one_site_values": exact_one,
        "summary": {
            "all_checks_passed": True,
            "maximum_transmission_absolute_error": max(
                row["transmission_max_absolute_error"] for row in physical),
            "maximum_matching_area_rate_absolute_error": max(
                row["matching_area_rate_absolute_error"] for row in physical),
            "maximum_integrated_physical_difference": max(
                value for row in physical_checks
                for value in row["absolute_differences_from_polynomial"].values()),
            "maximum_quadrature_refinement_difference": max(
                value for row in refinement_checks
                for value in row["absolute_differences"].values()),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-results", nargs="?", const=DEFAULT_RECORD, type=Path,
        help="write the numerical record, optionally to the supplied path",
    )
    args = parser.parse_args()
    record = run_checks()
    if args.write_results is not None:
        args.write_results.parent.mkdir(parents=True, exist_ok=True)
        args.write_results.write_text(
            json.dumps(record, indent=2, sort_keys=True, allow_nan=False) + "\n",
            encoding="utf-8",
        )
        print(f"Wrote {args.write_results}")
    print(json.dumps(record["summary"], indent=2, sort_keys=True))
    print("    N              F           N^2 F      Gamma_L       J/Gamma_L")
    for row in record["quadrature"]:
        print(f"{row['N']:5d}  {row['F']:13.8g}  {row['N_squared_F']:13.8g}"
              f"  {row['Gamma_L']:11.8g}  {row['current_at_unit_contact_rate']:13.8g}")


if __name__ == "__main__":
    main()

