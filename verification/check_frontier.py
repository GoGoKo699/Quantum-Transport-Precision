#!/usr/bin/env python3
"""Check the shifted-Chebyshev construction and its fixed-contact scaling."""

from __future__ import annotations

import json
import math

import numpy as np

from check_filters import physical_integrals, require
from filters import chain_transmission
from frontier_filters import (
    frontier_integrals,
    frontier_transmission,
    reflection_roots,
    synthesize_frontier_chain,
)


SYNTHESIS_SIZES = (4, 5, 8, 9, 12, 13)
QUADRATURE_SIZES = (*SYNTHESIS_SIZES, 16, 32, 64, 128, 256, 512)


def check_observables(n: int, power: float) -> dict:
    amplitude = n ** (-power)
    row = frontier_integrals(n, amplitude)
    cap = 4 / n**2 if power == 1 else 1 / n
    row["noise_ceiling"] = cap
    row["J_log_inverse_ceiling_over_Gamma"] = (
        row["J_over_Gamma"] * math.log(1 / cap)
    )
    label = f"N={n}, amplitude=N^-{power}"
    require(row["F"] >= 1 / (18 * n * n + 2) - 2e-12,
            f"{label}: size lower bound violated")
    require(row["F"] <= cap, f"{label}: numerical noise ceiling missed")
    require(row["contact_bound_ratio"] <= 1 + 2e-11,
            f"{label}: contact-rate bound violated")
    if n in (128, 512):
        refined = frontier_integrals(n, amplitude, epsabs=5e-14, epsrel=5e-13)
        for key in ("I0", "V0", "matching_area"):
            require(math.isclose(row[key], refined[key], rel_tol=2e-10, abs_tol=2e-12),
                    f"{label}: refined {key} differs")
    return row


def check_physical_chain(row: dict) -> dict:
    n, amplitude = row["N"], row["amplitude"]
    label = f"N={n}, amplitude={amplitude}"
    roots = reflection_roots(n, amplitude)
    require(len(roots) == n and np.all(np.abs(roots) < 1),
            f"{label}: degree or reflection-root domain differs")
    require(np.max(np.abs(roots + roots[::-1])) < 5e-15,
            f"{label}: reflection polynomial lost its parity")
    chain = synthesize_frontier_chain(n, amplitude)
    matrix = chain["H"]
    diagnostics = chain["diagnostics"]
    require(matrix.shape == (n, n), f"{label}: incorrect site count")
    require(np.all(chain["hoppings"] > 0), f"{label}: disconnected chain")
    require(diagnostics["minimum_source_residue"] > 0,
            f"{label}: source residue was not positive")
    for key in (
        "spectral_factor_relative_coefficient_residual",
        "off_tridiagonal_residual",
        "drain_nonendpoint_norm",
        "onsite_maximum",
        "hopping_mirror_residual",
        "equal_contact_residual",
        "contact_spectral_sum_residual",
    ):
        require(diagnostics[key] < 2e-12, f"{label}: {key} differs")

    contact_error = max(abs(chain[key] - row["Gamma"]) for key in ("Gamma_L", "Gamma_R"))
    require(contact_error < 5e-12, f"{label}: matching area and physical rates disagree")
    edges = 1 + np.array([-2, -0.25, 0, 0.25, 2, 8]) / n**2
    energies = np.concatenate((np.linspace(-1.4, 1.4, 161), roots, edges, -edges, [-4, 4]))
    transmission_error = max(
        abs(chain_transmission(chain, x) - frontier_transmission(n, amplitude, x))
        for x in energies
    )
    require(transmission_error < 5e-12,
            f"{label}: Green transmission differs from the target")

    scale = 1 / chain["Gamma_L"]
    unit_chain = {**chain, "H": matrix * scale,
                  "Gamma_L": chain["Gamma_L"] * scale,
                  "Gamma_R": chain["Gamma_R"] * scale}
    # The independent Green integrator uses a tridiagonal banded solve.
    # It reads hoppings separately from H, so rescale those coefficients too.
    unit_chain["hoppings"] = chain["hoppings"] * scale
    physical = physical_integrals(unit_chain)
    current_error = abs(physical["I0"] / (2 * math.pi) - row["J_over_Gamma"])
    fano_error = abs(physical["F"] - row["F"])
    require(max(current_error, fano_error) < 5e-12,
            f"{label}: unit-contact Green integrals disagree with the polynomial")
    return {
        "N": n, "amplitude": amplitude, "contact_error": contact_error,
        "transmission_error": float(transmission_error),
        "unit_contact_current_error": current_error, "fano_error": fano_error,
    }


def run_checks() -> dict:
    quadrature = [check_observables(n, power)
                  for n in QUADRATURE_SIZES for power in (1, 0.5)]
    physical = [check_physical_chain(row) for row in quadrature
                if row["N"] in SYNTHESIS_SIZES]
    error_keys = ("contact_error", "transmission_error", "unit_contact_current_error", "fano_error")
    return {
        "quadrature": quadrature,
        "physical": physical,
        "maximum_absolute_discrepancy": {key: max(row[key] for row in physical)
                                         for key in error_keys},
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2))
