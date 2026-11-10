#!/usr/bin/env python3
"""Exact Stage 63 M1 checks for shared-prime CRT factors.

The modular count is candidate admissibility only; it is never used as a
primality test. All primality tests below use exact trial division.
"""
from functools import lru_cache
from math import gcd, isqrt, prod
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name("01_exact_cases.json")


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def direct_residue_count(n, m, W):
    return sum(
        1
        for x in range(W)
        if gcd(x * (n - x) * (m - x), W) == 1
    )


def product_residue_count(n, m, primes):
    return prod(p - len({0, n % p, m % p}) for p in primes)


@lru_cache(None)
def pairs(n):
    return tuple(
        (p, n - p)
        for p in range(2, n // 2 + 1)
        if p < n - p and is_prime(p) and is_prime(n - p)
    )


def shared_by_common_prime(n, m):
    count = 0
    for x in range(2, min(n, m) - 1):
        if (x != n // 2 and x != m // 2 and is_prime(x)
                and is_prime(n - x) and is_prime(m - x)):
            count += 1
    return count


def shared_by_pair_intersection(n, m):
    return sum(
        len(set(left).intersection(right)) == 1
        for left in pairs(n)
        for right in pairs(m)
    )


def pair_position_categories(n, m):
    categories = {"low_low": 0, "low_high": 0,
                  "high_low": 0, "high_high": 0, "four_distinct": 0}
    for (p, q) in pairs(n):
        for (r, s) in pairs(m):
            equalities = (p == r, p == s, q == r, q == s)
            if not any(equalities):
                categories["four_distinct"] += 1
            else:
                assert sum(equalities) == 1
                categories[("low_low", "low_high", "high_low", "high_high")
                           [equalities.index(True)]] += 1
    return categories


def main():
    moduli = ((2, 3, 5, 7), (2, 3, 5, 11))
    modular_cases = 0
    obstructions_210 = 0
    for primes in moduli:
        W = prod(primes)
        for n in range(4, 42, 2):
            for m in range(n + 2, 44, 2):
                direct = direct_residue_count(n, m, W)
                by_product = product_residue_count(n, m, primes)
                assert direct == by_product
                modular_cases += 1
                if W == 210 and direct == 0:
                    obstructions_210 += 1
                    assert {n % 3, m % 3} == {1, 2}

    # Actual-prime contraction and independent pair-set classification.
    actual_pairs = 0
    for n in range(4, 82, 2):
        for m in range(n + 2, 84, 2):
            x_count = shared_by_common_prime(n, m)
            intersection_count = shared_by_pair_intersection(n, m)
            categories = pair_position_categories(n, m)
            assert x_count == intersection_count
            assert sum(categories[k] for k in
                       ("low_low", "low_high", "high_low", "high_high")) == x_count
            assert sum(categories.values()) == len(pairs(n)) * len(pairs(m))
            assert categories["low_high"] == 0
            actual_pairs += 1

    # Cross-check every h=1 row in the checked-in Stage 57 dataset by a
    # common-prime scan and, independently, pair-set intersections.
    stage57 = json.loads((ROOT / "results/stage57/shifted_correlations.json")
                         .read_text(encoding="utf-8"))
    stage57_rows = [row for row in stage57["rows"] if row["h"] == 1]
    for row in stage57_rows:
        n, m = row["N"], row["M"]
        categories = pair_position_categories(n, m)
        expected = row["shared_prime_position_counts"]
        assert categories["low_low"] == expected["low_low"]
        assert categories["low_high"] == expected["low_high"]
        assert categories["high_low"] == expected["high_low"]
        assert categories["high_high"] == expected["high_high"]
        assert categories["four_distinct"] == row["four_distinct_off_diagonal_count"]
        assert shared_by_common_prime(n, m) == sum(expected.values())

    exceptions = []
    for x, n, m in ((3, 8, 10), (5, 8, 12), (7, 12, 18)):
        assert is_prime(x) and is_prime(n - x) and is_prime(m - x)
        assert x != n // 2 and x != m // 2
        shared_count = shared_by_common_prime(n, m)
        assert shared_count >= 1
        wheel_count = direct_residue_count(n, m, 210)
        if x == 3:
            assert wheel_count == 0
        exceptions.append({"x": x, "n": n, "m": m,
                           "other_primes": [n - x, m - x],
                           "total_shared_prime_count": shared_count,
                           "wheel_210_count": wheel_count})

    # The only prime 2 can make an even sum with another prime is its
    # diagonal 2+2=4; that diagonal is excluded from R by p<q.
    assert all(all(2 not in pair for pair in pairs(n))
               for n in range(4, 202, 2))
    assert pairs(4) == ()

    data = {
        "evidence": "exact finite checks; the CRT identity is proved in the report",
        "moduli_checked": [prod(p) for p in moduli],
        "modular_n_m_cases": modular_cases,
        "wheel_210_local_obstruction_cases_in_grid": obstructions_210,
        "actual_target_pairs_checked": actual_pairs,
        "stage57_h1_rows_independently_rechecked": len(stage57_rows),
        "actual_prime_exception_examples": exceptions,
        "prime_2_distinct_pair_check_targets": 100,
        "methods": {
            "modular_method_1": "direct enumeration of all x modulo W",
            "modular_method_2": "independent product of local factor counts",
            "prime_method_1": "scan the common prime x and test both complements",
            "prime_method_2": "Cartesian product of pair lists and set intersections",
        },
        "assertions_passed": True,
        "universal_prime_claim": False,
    }
    OUT.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
