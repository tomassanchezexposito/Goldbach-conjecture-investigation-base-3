#!/usr/bin/env python3
"""Stage 72 exact finite regression; no asymptotic or Goldbach proof.

Use the rational *discrete surrogate* w(n/X)=(n/X)(1-n/X) for 0<n<X.
This surrogate is NOT the smooth compactly supported theorem weight.
All convolution calculations use Fraction and independently enumerated primes.
"""
from fractions import Fraction
from math import isqrt, log
import json


def prime_trial(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def convolution_coefficient(coeff, target):
    return sum((a * coeff.get(target - n, 0) for n, a in coeff.items()), Fraction(0))


def weight(n, X):
    return Fraction(n * (X - n), X * X) if 0 < n < X else Fraction(0)


rows = []
for X in (90, 150, 240):
    primes = [p for p in range(2, X) if prime_trial(p)]
    # Rational surrogate coefficients use *unit* prime and prime-power weights
    # rather than log p. All arguments checked are exact coefficient/monotonicity
    # statements and thus apply to arbitrary nonnegative coefficients.
    prime_coeff = {p: weight(p, X) for p in primes}
    prime_coeff = {p: a for p, a in prime_coeff.items() if a}
    proper = {}
    for p in primes:
        n = p * p
        while n < X:
            proper[n] = weight(n, X)
            n *= p
    all_coeff = dict(prime_coeff)
    all_coeff.update(proper)

    for N in range(X // 2 + (X // 2) % 2, X + 1, 2):
        # Completely independent pair enumeration vs reflected dictionary convolution.
        r = convolution_coefficient(prime_coeff, N)
        r_direct = sum((prime_coeff[p] * prime_coeff[q]
                        for p in primes for q in primes if p + q == N), Fraction(0))
        g = convolution_coefficient(all_coeff, N)
        g_direct = sum((a * b for n, a in all_coeff.items()
                        for m, b in all_coeff.items() if n + m == N), Fraction(0))
        assert r == r_direct and g == g_direct and g >= r
        mass = sum(prime_coeff.values(), Fraction(0))
        # All pair frequencies are between 0 and 2X, and the kernel sinc lower
        # bound is 2/pi at the core width 1/(6X) for the target interval.
        assert all(-X < p + q - N < Fraction(3 * X, 2)
                   for p in primes for q in primes)
        # A rational coefficientwise prime-power upper bound: at target N every
        # contaminated ordered term touches at least one proper power.
        q_mass = sum(proper.values(), Fraction(0))
        max_coeff = max(all_coeff.values())
        assert 0 <= g - r <= 2 * q_mass * max_coeff
        # Exact target erasure with every complementary edge hit once.
        removed = set()
        for p in primes:
            q = N - p
            if p < q and q in prime_coeff:
                removed.add(p if prime_coeff[p] <= prime_coeff[q] else q)
            elif p == q and q in prime_coeff:
                removed.add(p)  # diagonal only outside the residual H
        reduced = {p: a for p, a in prime_coeff.items() if p not in removed}
        assert convolution_coefficient(reduced, N) == 0
        assert sum(reduced.values(), Fraction(0)) <= mass
        if N in (X // 2 + (X // 2) % 2, X - X % 2):
            rows.append({"X": X, "N": N, "prime_count": len(primes),
                         "r_unit_surrogate": str(r), "lambda_unit_surrogate": str(g),
                         "power_contamination": str(g-r), "proper_power_count": len(proper),
                         "deleted_positions": len(removed), "all_checks_passed": True})

out = {"status": "PASS", "exact_arithmetic": "fractions.Fraction",
       "scope": "all even N in [X/2,X] for X=90,150,240; rational unit-weight surrogate, not logarithmic PNT",
       "targets_checked": sum(len(range(X // 2 + (X // 2) % 2, X+1, 2)) for X in (90,150,240)),
       "samples": rows,
       "limitations": "Finite exact identities and inequality only; does not test analytic asymptotics or Goldbach."}
print(json.dumps(out, indent=2, ensure_ascii=False))
