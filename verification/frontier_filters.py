"""Reflection, full-line transport and synthesis for a shifted Chebyshev filter.

The common Gamma is the physical contact rate, with a retarded half-width of
Gamma/2. Calculations follow science/fixed_contact_frontier.md.
"""

from __future__ import annotations

import math
import warnings

import mpmath as mp
import numpy as np
from scipy.integrate import quad

from filters import synthesize_polynomial_chain


def reflection_roots(n: int, amplitude: float) -> np.ndarray:
    """Return all N real reflection roots, including the moved pair."""
    if n < 3 or amplitude <= 0:
        raise ValueError("require N >= 3 and positive amplitude")
    angles = (np.arange(n) + 0.5) * math.pi / n
    roots = np.cos(angles)
    shifted_square = roots[0] ** 2 - 1 / (amplitude * n * n)
    if not shifted_square >= 0:
        raise ValueError("the moved roots must be real")
    roots[0] = math.sqrt(shifted_square)
    roots[-1] = -roots[0]
    return np.sort(roots)


def _reflection_in_band(n: int, amplitude: float, theta: float) -> float:
    edge_angle = math.pi / (2 * n)
    offset = theta - edge_angle
    # Both numerator and denominator of the quotient vanish at edge_angle.
    # The sine difference formula removes the poorly conditioned subtraction.
    sine_ratio = math.sin(n * offset) / math.sin(offset) if offset else n
    quotient = sine_ratio / math.sin(theta + edge_angle)
    return amplitude * math.cos(n * theta) + quotient / (n * n)


def _log_reflection_outside(n: int, amplitude: float, y: float) -> float:
    """Compute log p at positive x=1+y/N² without forming cosh(N arcosh x)."""
    edge_sine = math.sin(math.pi / (2 * n))
    delta = y / (n * n)
    denominator = y * (2 + delta) + (n * edge_sine) ** 2
    phase = n * math.acosh(1 + delta)
    log_cosh = phase + math.log1p(math.exp(-2 * phase)) - math.log(2)
    return log_cosh + math.log(amplitude + 1 / denominator)


def frontier_transmission(n: int, amplitude: float, x: float) -> float:
    if abs(x) <= 1:
        p = _reflection_in_band(n, amplitude, math.acos(abs(x)))
        return 1 / (1 + p * p)
    inverse_square = math.exp(
        -2 * _log_reflection_outside(n, amplitude, n * n * (abs(x) - 1))
    )
    return inverse_square / (1 + inverse_square)


def frontier_integrals(n: int, amplitude: float, *, epsabs: float = 2e-12,
                       epsrel: float = 2e-11) -> dict:
    """Integrate positive half-lines by symmetry and account for every root.

    The band log singularities are evaluated through the real-root potential.
    The outside quadratures run over the entire infinite scaled half-line.
    """
    roots = reflection_roots(n, amplitude)
    angles = np.sort(np.arccos(roots[(roots > 0) & (roots < 1)]))
    options = dict(epsabs=epsabs, epsrel=epsrel, limit=max(300, 4 * n))

    def inside(theta):
        p = _reflection_in_band(n, amplitude, theta)
        p2 = p * p
        transmission = 1 / (1 + p2)
        weight = math.sin(theta)
        return (transmission * weight, (p * transmission) ** 2 * weight,
                math.log1p(p2) * weight)

    def outside(y):
        p_inverse2 = math.exp(-2 * _log_reflection_outside(n, amplitude, y))
        denominator = 1 + p_inverse2
        weight = 1 / (n * n)
        return (p_inverse2 / denominator * weight,
                p_inverse2 / denominator**2 * weight,
                math.log1p(p_inverse2) * weight)

    with warnings.catch_warnings():
        warnings.simplefilter("error")
        inside_values = [
            quad(lambda theta: inside(theta)[i], 0, math.pi / 2,
                 points=angles, **options)[0]
            for i in range(3)
        ]
        outside_values = [
            quad(lambda y: outside(y)[i], 0, np.inf, **options)[0]
            for i in range(3)
        ]

    log_leading = math.log(amplitude) + (n - 1) * math.log(2)
    root_potential = math.fsum(
        (1 + r) * math.log1p(r) + (1 - r) * math.log1p(-r) - 2
        for r in roots
    )
    integral_log_p = 2 * log_leading + root_potential
    area = 2 * (inside_values[2] + outside_values[2]) - 2 * integral_log_p
    i0 = 2 * (inside_values[0] + outside_values[0])
    v0 = 2 * (inside_values[1] + outside_values[1])
    fano = v0 / i0
    log_normalized = i0 / area * math.log(1 / fano)
    return {
        "N": n, "amplitude": amplitude, "I0": i0, "V0": v0, "F": fano,
        "N_squared_F": n * n * fano, "matching_area": area,
        "Gamma": area / (2 * math.pi), "J_over_Gamma": i0 / area,
        "J_log_inverse_F_over_Gamma": log_normalized,
        "contact_bound_ratio": log_normalized / (1 - fano),
    }


def synthesize_frontier_chain(n: int, amplitude: float, *, dps: int = 90) -> dict:
    """Build the exact-degree real-root polynomial and realize it as a chain."""
    reflection_roots(n, amplitude)
    with mp.workdps(dps):
        a = mp.mpf(amplitude)
        r = mp.cos(mp.pi / (2 * n))
        moved = mp.sqrt(r * r - 1 / (a * n * n))
        # Multiply the root factors in opposite-sign pairs, including x for
        # odd degree. This preserves the exact parity used in the theorem.
        coefficients = [mp.mpf(1)]
        positive_roots = [moved] + [
            mp.cos((k + mp.mpf("0.5")) * mp.pi / n)
            for k in range(1, n // 2)
        ]
        for root in positive_roots:
            product = [mp.mpf(0)] * (len(coefficients) + 2)
            for k, value in enumerate(coefficients):
                product[k] -= root * root * value
                product[k + 2] += value
            coefficients = product
        if n % 2:
            coefficients = [mp.mpf(0), *coefficients]
        p = [a * 2 ** (n - 1) * value for value in coefficients]
        seed_polynomial = np.array(p, dtype=complex)
        seed_polynomial[0] -= 1j
        seeds = np.polynomial.polynomial.polyroots(seed_polynomial)
        return synthesize_polynomial_chain(p, seeds, dps=dps)
