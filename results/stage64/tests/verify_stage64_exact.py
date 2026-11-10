#!/usr/bin/env python3
"""Exact standard-library checks for selected Stage 64 identities.

Method A uses trial division; Method B uses an Eratosthenes sieve and an
independent representation-set partition. This is finite verification, not an
asymptotic result.
"""
from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path


def is_prime_trial(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, math.isqrt(n) + 1))


def sieve(limit):
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if flags[p]:
            flags[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [n for n, flag in enumerate(flags) if flag]


def reps_trial(target):
    return {
        (p, target - p)
        for p in range(2, target // 2 + 1)
        if p < target - p
        and is_prime_trial(p)
        and is_prime_trial(target - p)
    }


def reps_sieve(target, primes):
    prime_set = set(primes)
    return {
        (p, target - p)
        for p in primes
        if p < target - p and target - p in prime_set
    }


def primitive_root(p):
    factors = set()
    n = p - 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.add(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        factors.add(n)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise AssertionError("primitive root not found")


def verify_finite_field_parseval(length, modulus):
    primes = [n for n in range(length) if is_prime_trial(n)]
    a = [int(n in primes) for n in range(length)]
    conv = [
        sum(a[i] * a[(k - i) % length] for i in range(length))
        for k in range(length)
    ]
    g = primitive_root(modulus)
    zeta = pow(g, (modulus - 1) // length, modulus)
    assert pow(zeta, length, modulus) == 1
    assert all(pow(zeta, j, modulus) != 1 for j in range(1, length))
    fourier = [
        sum(conv[n] * pow(zeta, j * n, modulus) for n in range(length))
        % modulus
        for j in range(length)
    ]
    lhs = sum(fourier[j] * fourier[-j % length] for j in range(length))
    rhs = length * sum(x * x for x in conv)
    assert lhs % modulus == rhs % modulus
    return {
        "length": length,
        "prime_modulus": modulus,
        "primitive_root": g,
        "root_of_unity": zeta,
        "prime_positions": primes,
        "cyclic_convolution": conv,
        "lhs_mod_p": lhs % modulus,
        "rhs_mod_p": rhs % modulus,
    }


def main():
    targets = (50, 68, 100, 112)
    primes = sieve(max(targets))
    pair_rows = []
    for n, m in combinations(targets, 2):
        rn_a, rm_a = reps_trial(n), reps_trial(m)
        rn_b, rm_b = reps_sieve(n, primes), reps_sieve(m, primes)
        assert rn_a == rn_b and rm_a == rm_b
        shared_from_sets = sum(bool(set(a) & set(b)) for a in rn_a for b in rm_a)
        four_distinct = sum(not (set(a) & set(b)) for a in rn_a for b in rm_a)
        shared_from_formula = sum(
            is_prime_trial(x)
            and is_prime_trial(n - x)
            and is_prime_trial(m - x)
            and x != n - x
            and x != m - x
            for x in range(2, min(n, m) + 1)
        )
        assert len(rn_a) * len(rm_a) == shared_from_sets + four_distinct
        assert shared_from_formula == shared_from_sets
        pair_rows.append(
            {
                "n": n,
                "m": m,
                "R_n": len(rn_a),
                "R_m": len(rm_a),
                "product": len(rn_a) * len(rm_a),
                "shared": shared_from_sets,
                "shared_formula": shared_from_formula,
                "four_distinct": four_distinct,
                "representations_n": sorted(map(list, rn_a)),
                "representations_m": sorted(map(list, rm_a)),
            }
        )

    # Direct residue enumeration and independent local-product calculation.
    modulus = 210
    direct_wheel = sum(
        math.gcd(a, modulus) == 1 and math.gcd((-a) % modulus, modulus) == 1
        for a in range(modulus)
    )
    local_product = math.prod(p - 1 for p in (2, 3, 5, 7))
    assert direct_wheel == local_product == 48

    # Exact common finite singular-series factor: C2 cancels, leaving this ratio.
    odd_factors_210 = {p for p in (3, 5, 7) if 210 % p == 0}
    odd_factors_420 = {p for p in (3, 5, 7) if 420 % p == 0}
    ratio_210 = math.prod(
        (Fraction(p - 1, p - 2) for p in sorted(odd_factors_210)),
        start=Fraction(1),
    )
    ratio_420 = math.prod(
        (Fraction(p - 1, p - 2) for p in sorted(odd_factors_420)),
        start=Fraction(1),
    )
    assert odd_factors_210 == odd_factors_420 and ratio_210 == ratio_420

    # Two independent exact residual checks for the exhibit.
    residual_trial = {
        n: n >= 4 and n % 2 == 0 and not is_prime_trial(n - 1)
        and n - 1 > 1 and not is_prime_trial(n // 2) and n // 2 > 1
        for n in (210, 420)
    }
    prime_list = sieve(420)
    prime_set = set(prime_list)
    residual_sieve = {
        n: n >= 4 and n % 2 == 0 and n - 1 not in prime_set
        and n - 1 > 1 and n // 2 not in prime_set and n // 2 > 1
        for n in (210, 420)
    }
    assert residual_trial == residual_sieve == {210: True, 420: False}
    assert 209 == 11 * 19 and 105 == 3 * 5 * 7
    assert 419 in prime_set

    parseval = [
        verify_finite_field_parseval(16, 97),
        verify_finite_field_parseval(16, 193),
    ]
    result = {
        "classification": "FINITE_EXACT_VERIFICATION",
        "python_method_a": "trial division and direct common-prime formula",
        "python_method_b": "Eratosthenes sieve and representation-set intersection",
        "wheel_210": {
            "targets": [210, 420],
            "residue_modulus": 210,
            "direct_residue_count": direct_wheel,
            "independent_local_product": local_product,
        },
        "residual_status": {
            "trial_division": {str(k): v for k, v in residual_trial.items()},
            "sieve": {str(k): v for k, v in residual_sieve.items()},
        },
        "singular_series_odd_factor": {
            "210": str(ratio_210),
            "420": str(ratio_420),
            "shared_odd_prime_divisors": sorted(odd_factors_210),
        },
        "four_prime_partition_checks": pair_rows,
        "finite_field_parseval_checks": parseval,
        "limits": [
            "Finite computations verify identities and examples only.",
            "Finite-field Parseval checks do not prove the analytic circle-method estimate.",
            "No universal Goldbach or residual-coverage claim is made.",
        ],
    }
    out = Path(__file__).with_name("stage64_exact_results.json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
