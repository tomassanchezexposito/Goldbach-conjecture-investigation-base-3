#!/usr/bin/env python3
"""Exact checks for the Stage 63 dyadic-energy criterion.

All synthetic energy arithmetic uses fractions. The small prime examples use
trial division and direct enumeration only; they are definition checks, not an
asymptotic computation.
"""

from fractions import Fraction
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def is_composite(n):
    return n > 1 and not is_prime(n)


def residual(n):
    return n >= 4 and n % 2 == 0 and is_composite(n - 1) and is_composite(n // 2)


def distinct_prime_pairs(n):
    return [(p, n - p) for p in range(2, n // 2 + 1)
            if p < n - p and is_prime(p) and is_prime(n - p)]


def prime_powers(n):
    """Return prime powers p^k <= n with k >= 2."""
    out = []
    for p in range(2, n + 1):
        if not is_prime(p):
            continue
        value = p * p
        while value <= n:
            out.append(value)
            value *= p
    return sorted(out)


def prime_power_pair_count(n):
    """Unit-weight ordered prime-power convolution, for structural checking."""
    pp = {m for m in range(2, n + 1) if is_prime(m)} | set(prime_powers(n))
    return sum(1 for a in pp if n - a in pp)


def ordered_prime_pair_count(n):
    return sum(1 for p in range(2, n) if is_prime(p) and is_prime(n - p))


def exact_one_exception_energy(x, c, n0):
    """Model W_N=cN, observed=0 at n0, exact elsewhere."""
    assert x % 2 == 0 and n0 % 2 == 0 and x // 2 <= n0 <= x
    return (c * n0) ** 2


def main():
    # The selected examples satisfy both composite side conditions.
    observed = {}
    for n in (28, 50, 56):
        assert residual(n)
        pairs = distinct_prime_pairs(n)
        assert pairs
        assert len(pairs) == len(set(pairs))
        # On residual targets the ordered prime convolution is exactly twice
        # the genuine unordered distinct count (there is no prime diagonal).
        assert ordered_prime_pair_count(n) == 2 * len(pairs)
        # Every remaining unit-weight prime-power ordered pair has at least
        # one higher prime power in its positions.
        prime_set = {m for m in range(2, n + 1) if is_prime(m)}
        pp_set = prime_set | set(prime_powers(n))
        nonprime_power_terms = sum(
            1 for a in pp_set if n - a in pp_set and
            (a not in prime_set or n - a not in prime_set)
        )
        assert prime_power_pair_count(n) - ordered_prime_pair_count(n) == nonprime_power_terms
        observed[n] = pairs

    # A single zero target in a dyadic block has energy at least c^2 X^2/4.
    x, n0, c = 100, 52, Fraction(3, 7)
    energy = exact_one_exception_energy(x, c, n0)
    assert energy == Fraction(9 * 52 * 52, 49)
    assert energy >= c * c * x * x / 4
    assert energy > c * c * x * x / 16

    # A per-block max discrepancy follows exactly from the block energy.
    entries = [Fraction(1, 3), Fraction(-2, 5), Fraction(7, 11)]
    total_energy = sum((v * v for v in entries), Fraction(0))
    assert all(v * v <= total_energy for v in entries)

    print({"status": "PASS", "residual_prime_examples": observed,
           "one_exception_energy": str(energy),
           "normalized_lower_bound": str(c * c * x * x / 4),
           "criterion_threshold": str(c * c * x * x / 16),
           "exact_block_max_check": "PASS"})


if __name__ == "__main__":
    main()
