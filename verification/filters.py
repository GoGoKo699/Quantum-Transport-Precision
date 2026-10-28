"""Polynomial filters and exact-model serial-chain synthesis.

The analytic construction is documented in science/realization.md.  Numerical
root refinement is performed at arbitrary precision; returned Hamiltonians and
rates are double-precision arrays for independent transport checks.  These are
numerical calculations, not interval-certified statements.

Public API
----------
    chain = synthesize_chain(n, dps=90)
    chain["H"], chain["Gamma_L"], chain["Gamma_R"]
    chain_transmission(chain, energy)
    filter_integrals(n)

Gamma_L and Gamma_R are physical Lindblad rates.  The retarded Green function
contains Gamma_L/2 and Gamma_R/2.  Both contacts act on the same mode when n=1.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
import math
import warnings

import mpmath as mp
import numpy as np
from numpy.polynomial import legendre as leg
from scipy.integrate import quad
from scipy.linalg import solve_banded
from scipy.special import eval_gegenbauer, gammaln, roots_jacobi


def _validate_n(n: int) -> None:
    if isinstance(n, bool) or int(n) != n or n < 1:
        raise ValueError("n must be a positive integer")


@lru_cache(maxsize=None)
def reflection_power_coefficients(n: int) -> tuple[Fraction, ...]:
    """Exact ascending coefficients of p_n=2 P'_(n+1)/[(n+1)(n+2)]."""
    _validate_n(n)
    previous = [Fraction(1)]
    current = [Fraction(0), Fraction(1)]
    for k in range(1, n + 1):
        following = [Fraction(0)] * (k + 2)
        for j, value in enumerate(current):
            following[j + 1] += Fraction(2 * k + 1, k + 1) * value
        for j, value in enumerate(previous):
            following[j] -= Fraction(k, k + 1) * value
        previous, current = current, following
    factor = Fraction(2, (n + 1) * (n + 2))
    return tuple(factor * (j + 1) * current[j + 1] for j in range(n + 1))


def reflection_legendre_coefficients(n: int) -> np.ndarray:
    """Ascending Legendre-basis coefficients, used to seed root refinement."""
    _validate_n(n)
    coefficients = np.zeros(n + 1)
    for k in range(n, -1, -2):
        coefficients[k] = 2 * (2 * k + 1) / ((n + 1) * (n + 2))
    return coefficients


def legendre_reflection(n: int, x):
    """Evaluate the inherited Q_n^a reflection polynomial p_n(x)."""
    _validate_n(n)
    with np.errstate(over="ignore", invalid="ignore"):
        return 2 * eval_gegenbauer(n, 1.5, x) / ((n + 1) * (n + 2))


def _probabilities(p: float) -> tuple[float, float]:
    """Return T and T(1-T), avoiding subtraction near T=1 and overflow."""
    magnitude = abs(float(p))
    if math.isnan(magnitude):
        raise FloatingPointError("unexpected NaN in reflection polynomial")
    if magnitude <= 1:
        square = magnitude * magnitude
        denominator = 1 + square
        return 1 / denominator, square / denominator**2
    inverse = 1 / magnitude
    square = inverse * inverse
    denominator = 1 + square
    return square / denominator, square / denominator**2


def legendre_transmission(n: int, energy: float) -> float:
    return _probabilities(legendre_reflection(n, energy))[0]


def _mp_value(coefficients, z):
    value = mp.mpc(0) if isinstance(z, mp.mpc) else mp.mpf(0)
    for coefficient in reversed(coefficients):
        value = value * z + coefficient
    return value


def _mp_derivative(coefficients):
    return [j * coefficients[j] for j in range(1, len(coefficients))]


def _mp_multiply(left, right):
    result = [mp.mpc(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def _mp_dot(left, right):
    return mp.fsum(a * b for a, b in zip(left, right))


def synthesize_chain(n: int, dps: int = 90) -> dict:
    """Construct the N-site endpoint-only realization of 1/(1+p_n^2).

    The exact rational polynomial is refined with mpmath.  Orthogonal-basis
    double-precision roots are starting points only.  No zero onsite energy or
    mirror symmetry is imposed on the computed chain; their residuals are
    independently reported.  This routine is intended for moderate N, as used
    in the verification record, rather than as an arbitrary-size certified
    filter compiler.
    """
    _validate_n(n)
    if dps < 40:
        raise ValueError("use at least 40 decimal digits for root refinement")
    initial_coefficients = reflection_legendre_coefficients(n).astype(complex)
    initial_coefficients[0] -= 1j
    initial_roots = leg.legroots(initial_coefficients)

    with mp.workdps(dps):
        p = [mp.mpf(c.numerator) / c.denominator
             for c in reflection_power_coefficients(n)]
        dp = _mp_derivative(p)
        tolerance = mp.power(10, -dps + 12)
        roots = []
        for initial in initial_roots:
            z = mp.findroot(
                lambda z: _mp_value(p, z) - 1j,
                mp.mpc(float(initial.real), float(initial.imag)),
                df=lambda z: _mp_value(dp, z), solver="newton",
                tol=tolerance, maxsteps=80,
            )
            roots.append(z)
        if n > 1:
            separation = min(abs(a - b) for i, a in enumerate(roots)
                             for b in roots[i + 1:])
            if separation < mp.sqrt(tolerance):
                raise ArithmeticError("root refinement did not retain distinct roots")
        root_residual = max(abs(_mp_value(p, z) - 1j) for z in roots)
        lower_roots = [mp.mpc(z.real, -abs(z.imag)) for z in roots]
        if not all(z.imag < 0 for z in lower_roots):
            raise ArithmeticError("spectral-factor pole is not in the lower half-plane")

        d = [mp.mpc(p[-1])]
        for z in lower_roots:
            d = _mp_multiply(d, [-z, 1])
        a = [mp.re(c) for c in d]
        b = [mp.im(c) for c in d]
        denominator = [a[j] + p[j] for j in range(n + 1)]
        ddenominator = _mp_derivative(denominator)
        # Convert to a Legendre companion only for starting values.
        scaled = np.array([float(c / denominator[-1]) for c in denominator])
        initial_poles = leg.legroots(leg.poly2leg(scaled))
        poles = []
        for initial in initial_poles:
            if abs(complex(initial).imag) > 1e-5:
                raise ArithmeticError("real-pole initialization became ill-conditioned")
            h = mp.findroot(
                lambda z: _mp_value(denominator, z), mp.mpf(float(np.real(initial))),
                df=lambda z: _mp_value(ddenominator, z), solver="newton",
                tol=tolerance, maxsteps=80,
            )
            poles.append(mp.re(h))
        poles.sort()
        if n > 1 and min(poles[k + 1] - poles[k] for k in range(n - 1)) <= mp.sqrt(tolerance):
            raise ArithmeticError("Cayley poles are not distinct")
        pole_residual = max(abs(_mp_value(denominator, h)) for h in poles)
        values_b = [_mp_value(b, h) for h in poles]
        weights = [value / _mp_value(ddenominator, h)
                   for value, h in zip(values_b, poles)]
        if not all(weight > 0 for weight in weights):
            raise ArithmeticError("a Cayley source residue is not positive")
        source = [mp.sqrt(weight) for weight in weights]
        # B(h)=+/-1 exactly; preserving its computed value tests that identity.
        drain = [-value * entry for value, entry in zip(values_b, source)]
        damping_left = _mp_dot(source, source)
        damping_right = _mp_dot(drain, drain)
        vector = [entry / mp.sqrt(damping_left) for entry in source]
        basis = []
        for k in range(n):
            basis.append(vector)
            if k == n - 1:
                break
            residual = [h * entry for h, entry in zip(poles, vector)]
            for _ in range(2):
                for old in basis:
                    overlap = _mp_dot(old, residual)
                    residual = [entry - overlap * component
                                for entry, component in zip(residual, old)]
            norm = mp.sqrt(_mp_dot(residual, residual))
            if norm <= mp.sqrt(tolerance):
                raise ArithmeticError("source Krylov space terminated before N sites")
            vector = [entry / norm for entry in residual]

        transformed = [[mp.fsum(poles[k] * basis[i][k] * basis[j][k]
                                for k in range(n))
                        for j in range(n)] for i in range(n)]
        onsite = [transformed[k][k] for k in range(n)]
        hoppings = [transformed[k][k + 1] for k in range(n - 1)]
        if not all(coupling > 0 for coupling in hoppings):
            raise ArithmeticError("Lanczos hopping is not positive")
        transformed_drain = [_mp_dot(v, drain) for v in basis]
        off_tridiagonal = max([abs(transformed[i][j]) for i in range(n)
                              for j in range(n) if abs(i - j) > 1] or [mp.mpf(0)])
        gram_error = max(abs(_mp_dot(basis[i], basis[j]) - int(i == j))
                         for i in range(n) for j in range(n))
        factor_square = _mp_multiply(d, [mp.conj(c) for c in d])
        target_square = _mp_multiply(p, p)
        target_square[0] += 1
        factor_error = max(abs(left - right) for left, right
                           in zip(factor_square, target_square))
        factor_relative = factor_error / max(abs(x) for x in target_square)
        c_n = -mp.fsum(z.imag for z in lower_roots)

        matrix = np.diag([float(x) for x in onsite])
        if n > 1:
            hopping_array = np.array([float(x) for x in hoppings])
            matrix += np.diag(hopping_array, 1) + np.diag(hopping_array, -1)
        else:
            hopping_array = np.array([], dtype=float)
        diagnostics = {
            "precision_decimal_digits": dps,
            "spectral_root_residual": float(root_residual),
            "cayley_pole_residual": float(pole_residual),
            "spectral_factor_relative_coefficient_residual": float(factor_relative),
            "minimum_source_residue": float(min(weights)),
            "residue_sign_identity_residual": float(max(abs(x*x - 1) for x in values_b)),
            "basis_orthogonality_residual": float(gram_error),
            "off_tridiagonal_residual": float(off_tridiagonal),
            "drain_nonendpoint_norm": float(mp.sqrt(mp.fsum(x*x for x in transformed_drain[:-1]))),
            "onsite_maximum": float(max(abs(x) for x in onsite)),
            "hopping_mirror_residual": float(max([abs(hoppings[k] - hoppings[-1-k])
                                                   for k in range(len(hoppings))] or [mp.mpf(0)])),
            "equal_contact_residual": float(abs(damping_left - damping_right)),
            "contact_spectral_sum_residual": float(abs(2*damping_left - c_n)),
        }
        return {
            "N": n, "H": matrix, "hoppings": hopping_array,
            "Gamma_L": float(2*damping_left), "Gamma_R": float(2*damping_right),
            "diagnostics": diagnostics,
            "high_precision": {
                "onsite": [mp.nstr(x, 30) for x in onsite],
                "hoppings": [mp.nstr(x, 30) for x in hoppings],
                "Gamma_L": mp.nstr(2*damping_left, 30),
                "Gamma_R": mp.nstr(2*damping_right, 30),
            },
        }


def chain_transmission(chain: dict, energy: float) -> float:
    """Transmission from the physical chain, independently of its polynomial."""
    matrix = np.asarray(chain["H"], dtype=float)
    n = len(matrix)
    banded = np.zeros((3, n), dtype=complex)
    banded[1] = energy - np.diag(matrix)
    if n > 1:
        banded[0, 1:] = -np.diag(matrix, 1)
        banded[2, :-1] = -np.diag(matrix, -1)
    banded[1, 0] += 0.5j * chain["Gamma_L"]
    banded[1, -1] += 0.5j * chain["Gamma_R"]
    source = np.zeros(n, dtype=complex)
    source[-1] = 1
    green_column = solve_banded((1, 1), banded, source,
                                check_finite=True, overwrite_ab=False)
    return float(chain["Gamma_L"] * chain["Gamma_R"] * abs(green_column[0])**2)


def analytic_fano_upper(n: int) -> float:
    _validate_n(n)
    b_n = 4/((n+1)*(n+2))
    return (b_n + (math.pi+2)/(n*(n+3)))/(2-b_n)


def filter_integrals(n: int, *, epsabs: float = 2e-12,
                     epsrel: float = 2e-11) -> dict:
    """Compute full-bias integrals and the exact-model matching-area rate.

    The logarithmic singularities at reflection zeros are integrated through
    the polynomial's real-root product, not sampled numerically.  Remaining
    smooth integrals use adaptive quadrature.  Error estimates are QUADPACK
    diagnostics, not certified bounds on every rounding or root error.
    """
    _validate_n(n)
    zeros = roots_jacobi(n, 1, 1)[0]
    points = zeros[(zeros > 0) & (zeros < 1)].tolist()
    options = dict(epsabs=epsabs, epsrel=epsrel, limit=max(300, 4*n))

    def probabilities(x):
        return _probabilities(legendre_reflection(n, x))

    def log_small(x):
        p = abs(float(legendre_reflection(n, x)))
        return math.log1p(p*p)

    def log_tail(x):
        p = abs(float(legendre_reflection(n, x)))
        if math.isinf(p):
            return 0.0
        inverse = 1/p
        return math.log1p(inverse*inverse)

    with warnings.catch_warnings():
        warnings.simplefilter("error")
        inside_i, ei = quad(lambda x: probabilities(x)[0], 0, 1,
                            points=points, **options)
        inside_v, ev = quad(lambda x: probabilities(x)[1], 0, 1,
                            points=points, **options)
        inside_log, el = quad(log_small, 0, 1, points=points, **options)
        outside_i, eoi = quad(lambda y: probabilities(1+y/n**2)[0]/n**2,
                              0, np.inf, **options)
        outside_v, eov = quad(lambda y: probabilities(1+y/n**2)[1]/n**2,
                              0, np.inf, **options)
        outside_log, eol = quad(lambda y: log_tail(1+y/n**2)/n**2,
                                0, np.inf, **options)

    log_leading = (gammaln(2*n+3) - 2*gammaln(n+2)
                   - n*math.log(2) - math.log(n+2))
    potential_sum = math.fsum((1+x)*math.log1p(x) + (1-x)*math.log1p(-x) - 2
                             for x in zeros)
    integral_log_p = 2*log_leading + potential_sum
    matching_area = float(-2*integral_log_p + 2*(inside_log+outside_log))
    gamma = matching_area/(2*math.pi)
    i0 = 2*(inside_i+outside_i)
    v0 = 2*(inside_v+outside_v)
    fano = v0/i0
    current = i0/(2*math.pi)
    noise = v0/(2*math.pi)
    return {
        "N": n, "I0": i0, "V0": v0, "J": current, "D": noise,
        "F": fano, "N_squared_F": n*n*fano,
        "analytic_F_lower": 1/(18*n*n+2),
        "analytic_F_upper": analytic_fano_upper(n),
        "matching_area": matching_area,
        "Gamma_L": gamma, "Gamma_R": gamma,
        "current_at_unit_contact_rate": current/gamma,
        "contact_bound_ratio": current*math.log(1/fano)/((1-fano)*gamma),
        "quadrature_error_estimates": {
            "I0": 2*(ei+eoi), "V0": 2*(ev+eov),
            "matching_area_smooth_parts": 2*(el+eol),
        },
    }
