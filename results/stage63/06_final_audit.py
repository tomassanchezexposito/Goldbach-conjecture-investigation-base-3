#!/usr/bin/env python3
"""Independent exact finite audit for the Stage 63 final report.

This intentionally uses trial division for primality and a separate Eratosthenes
sieve for the second implementation. It checks definitions and identities on a
bounded interval; it does not assert a universal Goldbach result.
"""
from __future__ import annotations

import json
import math
import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "results/stage63/06_final_audit.json"
LIMIT = 1000


def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def sieve(limit: int) -> list[bool]:
    flags = [True] * (limit + 1)
    if limit >= 0:
        flags[0] = False
    if limit >= 1:
        flags[1] = False
    for p in range(2, math.isqrt(limit) + 1):
        if flags[p]:
            for k in range(p * p, limit + 1, p):
                flags[k] = False
    return flags


def residual_by_trial(n: int) -> bool:
    return n >= 4 and n % 2 == 0 and not is_prime_trial(n - 1) and not is_prime_trial(n // 2)


def pairs_by_sieve(n: int, flags: list[bool]) -> list[list[int]]:
    return [[p, n - p] for p in range(2, n // 2 + 1)
            if flags[p] and flags[n - p] and p < n - p]


def pairs_by_trial(n: int) -> list[list[int]]:
    return [[p, n - p] for p in range(2, n // 2 + 1)
            if p < n - p and is_prime_trial(p) and is_prime_trial(n - p)]


def wheel_direct(n: int, modulus: int = 210) -> int:
    return sum(math.gcd(x * (n - x), modulus) == 1 for x in range(modulus))


def wheel_product(n: int) -> int:
    product = 1
    for ell in (2, 3, 5, 7):
        residues = {0 % ell, n % ell}
        product *= ell - len(residues)
    return product


def shared_direct(n: int, m: int, modulus: int = 210) -> int:
    return sum(math.gcd(x * (n - x) * (m - x), modulus) == 1
               for x in range(modulus))


def shared_product(n: int, m: int) -> int:
    product = 1
    for ell in (2, 3, 5, 7):
        product *= ell - len({0 % ell, n % ell, m % ell})
    return product


def main() -> None:
    flags = sieve(LIMIT)
    even_targets = list(range(4, LIMIT + 1, 2))
    residuals = [n for n in even_targets if residual_by_trial(n)]
    pair_counts = {}
    for n in even_targets:
        via_sieve = pairs_by_sieve(n, flags)
        via_trial = pairs_by_trial(n)
        assert via_sieve == via_trial, (n, via_sieve, via_trial)
        pair_counts[str(n)] = len(via_sieve)
    residual_without_pairs = [n for n in residuals if pair_counts[str(n)] == 0]

    # The small boundaries make the diagonal distinction explicit.
    assert pairs_by_trial(4) == []                 # (2,2) is not distinct.
    assert pairs_by_trial(6) == []                 # (3,3) is not distinct.
    assert pairs_by_trial(8) == [[3, 5]]
    assert residual_by_trial(4) is False            # N/2=2 is prime.
    assert residual_by_trial(6) is False            # N/2=3 is prime.
    assert residual_by_trial(8) is False            # N-1=7 is prime.
    assert residual_by_trial(28) is True
    assert pairs_by_trial(28) == [[5, 23], [11, 17]]

    wheel_targets = list(range(4, 302, 2))
    for n in wheel_targets:
        assert wheel_direct(n) == wheel_product(n), n
    shared_cases = [(n, m) for n in range(4, 102, 2)
                    for m in range(n + 2, 104, 2)]
    for n, m in shared_cases:
        assert shared_direct(n, m) == shared_product(n, m), (n, m)

    payload = {
        "purpose": "Independent finite audit of definitions, exact pair counts, and wheel CRT identities",
        "evidence_classification": "Computational observation; the code does not prove universal coverage",
        "python": platform.python_version(),
        "implementation_1": "Eratosthenes sieve for pair enumeration",
        "implementation_2": "independent trial-division primality for pair enumeration and residual membership",
        "limit": LIMIT,
        "even_targets_checked": len(even_targets),
        "residual_targets_checked": len(residuals),
        "residual_targets": residuals,
        "residual_targets_without_pairs_in_finite_range": residual_without_pairs,
        "finite_observation_all_residual_targets_covered": not residual_without_pairs,
        "genuine_distinct_pair_counts": pair_counts,
        "boundary_checks": {"N=4": [], "N=6": [], "N=8": [[3, 5]], "N=28": [[5, 23], [11, 17]]},
        "wheel_210_direct_vs_product_targets": len(wheel_targets),
        "shared_wheel_210_direct_vs_product_pairs": len(shared_cases),
        "assertions": "all passed",
        "claims_not_made": ["No universal Goldbach proof", "No universal residual coverage claim"],
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in payload.items() if k != "genuine_distinct_pair_counts"}, indent=2))
    print(f"Exact pair-count table written to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
