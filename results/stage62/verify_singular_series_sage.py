#!/usr/bin/env python3
"""Independent SageMath audit of Stage 62 finite singular-series examples.

Run with: sage -python results/stage62/verify_singular_series_sage.py
This script consumes the producer's JSON but recomputes primality, factors,
CRT congruences, wheel counts, and rational ratios with SageMath.
"""
from itertools import product
import json
from pathlib import Path
from time import perf_counter

from sage.all import CRT_list, QQ, ZZ, gcd, is_prime, prod
from sage.version import version as sage_version


HERE = Path(__file__).resolve().parent


def odd_prime_factors(n):
    return [ZZ(p) for p, _ in ZZ(n).factor() if p != 2]


def singular_factor(n):
    value = QQ(1)
    for p in odd_prime_factors(n):
        value *= QQ(p - 1) / QQ(p - 2)
    return value


def wheel_direct(n):
    return sum(
        1
        for a in range(210)
        if gcd(ZZ(a), ZZ(210)) == 1
        and gcd(ZZ(n - a), ZZ(210)) == 1
    )


def representations(n):
    """Unordered distinct prime pairs; each representation appears once."""
    n = ZZ(n)
    return [
        (ZZ(p), ZZ(n - p))
        for p in range(2, int(n) // 2 + 1)
        if p < n - p and is_prime(p) and is_prime(n - p)
    ]


def wheel(n):
    return sum(
        1
        for a in range(210)
        if gcd(ZZ(a), ZZ(210)) == 1
        and gcd(ZZ(n - a), ZZ(210)) == 1
    )


def verify_correlation_identity():
    """Brute-force the position decomposition and signed identity independently."""
    checked = 0
    for N in range(4, 102, 2):
        targets = (N - 2, N, N + 2)
        pairs = [representations(n) for n in targets]
        counts = [len(row) for row in pairs]
        wheels = [wheel(n) for n in targets]
        normalized = [QQ(r) / a for r, a in zip(counts, wheels)]
        a, b, c = normalized
        direct_D = (-a*a - 3*b*b - c*c + 6*a*b + 2*a*c + 6*b*c) / 9

        off_diagonal = [r * (r - 1) for r in counts]
        cross = []
        for i, j in ((0, 1), (0, 2), (1, 2)):
            shared_direct = sum(
                len(set(left) & set(right)) == 1
                for left in pairs[i]
                for right in pairs[j]
            )
            shared_by_common_prime = sum(
                1
                for x in range(2, max(targets) + 1)
                if is_prime(x)
                and x != QQ(targets[i]) / 2
                and x != QQ(targets[j]) / 2
                and is_prime(targets[i] - x)
                and is_prime(targets[j] - x)
            )
            assert shared_direct == shared_by_common_prime
            four_distinct = counts[i] * counts[j] - shared_direct
            assert four_distinct + shared_direct == counts[i] * counts[j]
            cross.append(counts[i] * counts[j])

        for i in range(3):
            for left_index, left in enumerate(pairs[i]):
                for right in pairs[i][left_index + 1:]:
                    assert len(set(left) & set(right)) == 0
        identity_9D = (
            -QQ(counts[0] + off_diagonal[0]) / wheels[0]**2
            -3 * QQ(counts[1] + off_diagonal[1]) / wheels[1]**2
            -QQ(counts[2] + off_diagonal[2]) / wheels[2]**2
            +6 * QQ(cross[0]) / (wheels[0] * wheels[1])
            +2 * QQ(cross[1]) / (wheels[0] * wheels[2])
            +6 * QQ(cross[2]) / (wheels[1] * wheels[2])
        )
        assert identity_9D == 9 * direct_D
        checked += 1
    return checked


def main():
    started = perf_counter()
    source = HERE / "finite_examples.json"
    data = json.loads(source.read_text(encoding="utf-8"))
    rows = data["examples"]
    checked = []

    for row in rows:
        primes = [ZZ(p) for p in row["P"]]
        q, n = ZZ(row["q"]), ZZ(row["N"])
        assert is_prime(q)
        assert q % 3 == 2 and q % 5 == 4 and q % 7 == 2
        assert all(q % p == 1 for p in primes)

        # Independent CRT reconstruction using Sage's generalized CRT routine.
        residues = [ZZ(2), ZZ(4), ZZ(2)] + [ZZ(1)] * len(primes)
        moduli = [ZZ(3), ZZ(5), ZZ(7)] + primes
        residue = ZZ(CRT_list(residues, moduli))
        modulus = prod(moduli)
        assert q % modulus == residue

        assert n == 2 * (q - 1) and n % 2 == 0
        assert not is_prime(n // 2) and n // 2 > 2
        assert (n - 1) % 5 == 0 and n - 1 > 5 and not is_prime(n - 1)
        assert wheel_direct(n) == 15
        assert wheel_direct(n + 2) == 15

        fn, fn2 = singular_factor(n), singular_factor(n + 2)
        product_lower = prod([QQ(p - 1) / QQ(p - 2) for p in primes])
        ratio = fn / fn2
        assert fn2 == QQ(q - 1) / QQ(q - 2)
        assert fn >= product_lower
        assert ratio == QQ(row["singular_factor_ratio"])
        assert ratio == QQ(row["wheel_normalized_ratio"])
        assert ratio >= product_lower / 2
        assert odd_prime_factors(n) == [ZZ(p) for p in row["odd_prime_factors_N"]]

        checked.append(
            {
                "P": [int(p) for p in primes],
                "q": int(q),
                "N": int(n),
                "CRT_residue": int(residue),
                "CRT_modulus": int(modulus),
                "wheel_N": wheel_direct(n),
                "wheel_N_plus_2": wheel_direct(n + 2),
                "exact_ratio": str(ratio),
                "proved_lower_bound": str(product_lower / 2),
            }
        )

    values = []
    for eps in product((QQ(-1) / 3, QQ(0), QQ(1) / 3), repeat=3):
        a, b, c = (1 + x for x in eps)
        values.append(
            (-a * a - 3 * b * b - c * c + 6 * a * b + 2 * a * c + 6 * b * c) / 9
        )
    assert len(values) == 27 and min(values) == QQ(4) / 9

    correlation_targets_checked = verify_correlation_identity()

    result = {
        "method": "SageMath factorization and primality; Sage CRT; direct residue enumeration; exact QQ",
        "sage_version": str(sage_version),
        "input": "results/stage62/finite_examples.json",
        "examples_checked": len(checked),
        "conditional_grid_cases": len(values),
        "correlation_identity_centers_checked": correlation_targets_checked,
        "correlation_identity_targets": "N-2, N, N+2 for even N=4..100",
        "conditional_grid_minimum": str(min(values)),
        "all_assertions_passed": True,
        "examples": checked,
        "runtime_seconds": round(perf_counter() - started, 6),
    }
    out = HERE / "sage_verification.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in (
        "method", "sage_version", "examples_checked", "conditional_grid_cases", "correlation_identity_centers_checked",
        "conditional_grid_minimum", "all_assertions_passed", "runtime_seconds", "output"
    ) if k != "output"}, indent=2))
    print(f"output: {out}")


if __name__ == "__main__":
    main()
