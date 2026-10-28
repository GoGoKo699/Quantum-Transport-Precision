#!/usr/bin/env python3
"""Independent small-system checks of the scattering/counting convention.

This uses the full 2**N-dimensional fermionic Lindblad generator. It does
not infer noise by differentiating the transmission formula. Only the
finite cases reported here are tested; the all-N statements have proofs.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve_continuous_lyapunov


def annihilator(n: int, site: int) -> np.ndarray:
    """Jordan-Wigner annihilation in the binary occupation basis."""
    dim = 1 << n
    c = np.zeros((dim, dim), dtype=complex)
    for state in range(dim):
        if state & (1 << site):
            sign = (-1) ** ((state & ((1 << site) - 1)).bit_count())
            c[state ^ (1 << site), state] = sign
    return c


def lindblad_statistics(H: np.ndarray, gamma_left: float, gamma_right: float):
    """Mean and count-variance rates from the stationary tilted generator."""
    n = len(H)
    dim = 1 << n
    eye = np.eye(dim, dtype=complex)
    cs = [annihilator(n, j) for j in range(n)]
    many_H = sum(H[i, j] * cs[i].conj().T @ cs[j]
                 for i in range(n) for j in range(n))
    left = np.sqrt(gamma_left) * cs[0].conj().T
    right = np.sqrt(gamma_right) * cs[-1]
    L = -1j * (np.kron(eye, many_H) - np.kron(many_H.T, eye))
    for jump in (left, right):
        a = jump.conj().T @ jump
        L += np.kron(jump.conj(), jump)
        L -= 0.5 * (np.kron(eye, a) + np.kron(a.T, eye))
    counted_jump = np.kron(right.conj(), right)
    trace = eye.reshape(-1, order="F")
    size = dim * dim
    augmented = np.zeros((size + 1, size + 1), dtype=complex)
    augmented[:size, :size] = L
    augmented[:size, -1] = trace / dim
    augmented[-1, :size] = trace
    rhs = np.zeros(size + 1, dtype=complex)
    rhs[-1] = 1
    rho = np.linalg.solve(augmented, rhs)[:size]
    current = float(np.real(trace @ (counted_jump @ rho)))
    # L rho' = J rho - counted_jump rho, trace(rho') = 0.
    rhs[:size] = current * rho - counted_jump @ rho
    rhs[-1] = 0
    response = np.linalg.solve(augmented, rhs)[:size]
    noise = current + 2 * float(np.real(trace @ (counted_jump @ response)))
    density = rho.reshape((dim, dim), order="F")
    return {
        "J": current,
        "D": noise,
        "F": noise / current,
        "stationarity_residual": float(np.linalg.norm(L @ rho)),
        "trace_error": float(abs(trace @ rho - 1)),
        "minimum_density_eigenvalue": float(np.linalg.eigvalsh(
            (density + density.conj().T) / 2).min()),
        "poisson_residual": float(np.linalg.norm(
            L @ response - current * rho + counted_jump @ rho)),
    }


def scattering_statistics(H: np.ndarray, gamma_left: float, gamma_right: float):
    n = len(H)
    loss = np.zeros((n, n), dtype=complex)
    loss[0, 0] += gamma_left / 2
    loss[-1, -1] += gamma_right / 2
    source = np.eye(n, dtype=complex)[:, 0]

    def transmission(energy):
        amplitude = np.linalg.solve(
            energy * np.eye(n) - H + 1j * loss, source)[-1]
        return gamma_left * gamma_right * abs(amplitude) ** 2

    I0, i_error = quad(transmission, -np.inf, np.inf,
                       epsabs=2e-11, epsrel=2e-11, limit=400)
    V0, v_error = quad(lambda x: transmission(x) * (1 - transmission(x)),
                       -np.inf, np.inf, epsabs=2e-11, epsrel=2e-11, limit=400)
    A = -1j * H - loss
    injection = np.zeros_like(H)
    injection[0, 0] = gamma_left
    covariance = solve_continuous_lyapunov(A, -injection)
    lyapunov_current = gamma_right * float(np.real(covariance[-1, -1]))
    return {
        "J": I0 / (2 * np.pi),
        "D": V0 / (2 * np.pi),
        "F": V0 / I0,
        "lyapunov_J": lyapunov_current,
        "quadrature_error_I0": i_error,
        "quadrature_error_V0": v_error,
    }


def check_case(label, H, gamma_left, gamma_right):
    H = np.asarray(H, dtype=float)
    full = lindblad_statistics(H, gamma_left, gamma_right)
    scattering = scattering_statistics(H, gamma_left, gamma_right)
    discrepancy = max(abs(full[k] - scattering[k]) for k in ("J", "D", "F"))
    discrepancy = max(discrepancy, abs(full["J"] - scattering["lyapunov_J"]))
    rate_lhs = full["J"] * np.log(1 / full["F"]) / (1 - full["F"])
    assert discrepancy < 5e-9, (label, discrepancy)
    assert full["stationarity_residual"] < 1e-10
    assert full["poisson_residual"] < 1e-10
    assert full["minimum_density_eigenvalue"] > -1e-10
    assert full["F"] >= 1 / (18 * len(H) ** 2 + 2) - 1e-10
    assert rate_lhs <= min(gamma_left, gamma_right) + 1e-10
    return {
        "label": label,
        "N": len(H),
        "H": H.tolist(),
        "Gamma_L": gamma_left,
        "Gamma_R": gamma_right,
        "lindblad": full,
        "scattering": scattering,
        "maximum_statistics_discrepancy": discrepancy,
        "contact_bound_left_hand_side": rate_lhs,
        "contact_bound_right_hand_side": min(gamma_left, gamma_right),
    }


def run_checks(include_filters=True):
    cases = [
        ("single_symmetric", [[0.0]], 1.0, 1.0),
        ("single_asymmetric", [[0.2]], 0.7, 1.3),
        ("two_disordered", [[-0.3, 0.6], [0.6, 0.5]], 0.9, 1.4),
        ("three_disordered", [[0.2, 0.7, 0], [0.7, -0.4, 1.1],
                              [0, 1.1, 0.8]], 1.3, 0.8),
        ("four_disordered", [[0.4, 0.4, 0, 0], [0.4, -0.2, 1.1, 0],
                             [0, 1.1, 0.1, 0.75], [0, 0, 0.75, -0.6]], 0.6, 1.7),
    ]
    results = [check_case(*case) for case in cases]
    if include_filters:
        from filters import synthesize_chain
        for n in (2, 3, 4):
            chain = synthesize_chain(n)
            results.append(check_case("legendre_" + str(n), chain["H"],
                                      chain["Gamma_L"], chain["Gamma_R"]))
    for row in results[:2]:
        gl, gr = row["Gamma_L"], row["Gamma_R"]
        assert abs(row["lindblad"]["J"] - gl * gr / (gl + gr)) < 1e-12
        assert abs(row["lindblad"]["F"] - (gl * gl + gr * gr) / (gl + gr) ** 2) < 1e-12
    return {
        "conventions": "hbar=1; physical Gamma; D=lim Var(K_t)/t; F=D/J",
        "method": "Full fermionic Lindblad stationary state and tilted-generator Poisson equation; compared with Green-function quadrature and covariance Lyapunov equation.",
        "scope": "Finite deterministic cases, not an all-N proof or rigorous floating-point certificate.",
        "cases": results,
        "maximum_statistics_discrepancy": max(
            x["maximum_statistics_discrepancy"] for x in results),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--without-filters", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run_checks(not args.without_filters)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"cases": len(result["cases"]),
                      "maximum_statistics_discrepancy":
                      result["maximum_statistics_discrepancy"]}, indent=2))

