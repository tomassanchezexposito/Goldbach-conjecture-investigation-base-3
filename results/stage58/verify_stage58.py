#!/usr/bin/env python3
"""Exact, targeted checks for the Stage 58 pointwise-certificate audit.

Run from any directory with Python 3:
    python results/stage58/verify_stage58.py

Only the standard library is used. The script checks finite instances of the
wheel count, the diagonal/off-diagonal bookkeeping, the block-moment lemma,
and two retained counterexamples. It is not a Goldbach search or proof.
"""

from fractions import Fraction
from itertools import product
import json
import platform
from pathlib import Path


OUT = Path(__file__).with_name("verification.json")
WHEEL_PRIMES = (2, 3, 5, 7)


def sieve(limit: int) -> bytearray:
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    p = 2
    while p * p <= limit:
        if flags[p]:
            start = p * p
            flags[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
        p += 1
    return flags


def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def is_composite_trial(n: int) -> bool:
    return n > 1 and not is_prime_trial(n)


def residual(n: int) -> bool:
    return (n >= 4 and n % 2 == 0
            and is_composite_trial(n - 1)
            and is_composite_trial(n // 2))


def wheel_formula(n: int) -> int:
    out = 1
    for ell in WHEEL_PRIMES:
        out *= ell - (1 if n % ell == 0 else 2)
    return out


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def wheel_by_residues(n: int) -> int:
    return sum(
        gcd(a, 210) == 1 and gcd((n - a) % 210, 210) == 1
        for a in range(210)
    )


def pairs_trial(n: int) -> list[tuple[int, int]]:
    return [
        (p, n - p)
        for p in range(2, n // 2 + 1)
        if p < n - p and is_prime_trial(p) and is_prime_trial(n - p)
    ]


def pairs_sieve(n: int, flags: bytearray) -> list[tuple[int, int]]:
    return [
        (p, n - p)
        for p in range(2, n // 2 + 1)
        if p < n - p and flags[p] and flags[n - p]
    ]


def x_values(lower: int, upper: int, flags: bytearray) -> tuple[list[int], list[Fraction]]:
    ns = [n for n in range(lower + lower % 2, upper + 1, 2) if residual(n)]
    xs = [Fraction(len(pairs_sieve(n, flags)), wheel_formula(n)) for n in ns]
    return ns, xs


def fraction_text(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> None:
    # Exact wheel formula versus an independent direct scan of all residues.
    wheel_targets = list(range(4, 502, 2))
    for n in wheel_targets:
        assert wheel_formula(n) == wheel_by_residues(n), n

    # Exact pair-list check of the diagonal convention on a small range.
    # The ordered count is 2R plus one diagonal iff N/2 is prime.
    fourier_check_limit = 300
    flags_fourier = sieve(fourier_check_limit)
    for n in range(4, fourier_check_limit + 1, 2):
        unordered = pairs_trial(n)
        ordered_count = sum(
            bool(flags_fourier[p] and flags_fourier[n - p])
            for p in range(2, n - 1)
        )
        diagonal = int(bool(flags_fourier[n // 2]))
        assert ordered_count == 2 * len(unordered) + diagonal, n

    # Exhaustively check the finite-vector implication behind the block test.
    vectors_tested = 0
    vector_bound = 3
    max_k = 6
    for k in range(2, max_k + 1):
        threshold_factor = Fraction(k, k - 1)
        for values in product(range(vector_bound + 1), repeat=k):
            vectors_tested += 1
            mean = Fraction(sum(values), k)
            second = Fraction(sum(v * v for v in values), k)
            centered_sum = sum((Fraction(v) - mean) ** 2 for v in values)
            threshold_sum = threshold_factor * mean * mean
            if 0 in values:
                assert centered_sum >= threshold_sum
            if centered_sum < threshold_sum:
                assert all(v > 0 for v in values)

    # General countermodel: every nonzero cyclic shift has positive mean
    # product although one coordinate is zero. All quantities are rational.
    k = 10
    toy = [0] + [1] * (k - 1)
    toy_mean = Fraction(sum(toy), k)
    toy_shift_checks = []
    for h in range(1, k):
        mean_product = Fraction(sum(toy[i] * toy[(i + h) % k] for i in range(k)), k)
        covariance = mean_product - toy_mean * toy_mean
        assert toy_mean > 0 and mean_product > 0 and covariance == Fraction(-1, k * k)
        toy_shift_checks.append({
            "cyclic_shift": h,
            "mean_product": fraction_text(mean_product),
            "product_of_means": fraction_text(toy_mean * toy_mean),
            "covariance": fraction_text(covariance),
        })

    # Recheck the Stage 56 variance-threshold counterexample independently.
    flags = sieve(500)
    variance_ns, variance_xs = x_values(50, 150, flags)
    k_var = len(variance_ns)
    mu = sum(variance_xs, Fraction()) / k_var
    centered = sum((x - mu) ** 2 for x in variance_xs)
    threshold = Fraction(k_var, k_var - 1) * mu * mu
    variance_ratio = centered / threshold
    assert k_var == 21
    assert all(len(pairs_trial(n)) > 0 for n in variance_ns)
    assert variance_ratio == Fraction(1716160, 1568187) and variance_ratio > 1

    # Recheck the Stage 57 negative-covariance window with a fresh sieve and
    # direct pair enumeration, without reading its saved result rows.
    cov_flags = sieve(400)
    cov_ns, cov_xs = x_values(262, 362, cov_flags)
    h = 1
    cov_ys = [Fraction(len(pairs_sieve(n + 2 * h, cov_flags)), wheel_formula(n + 2 * h))
              for n in cov_ns]
    cov_mean_x = sum(cov_xs, Fraction()) / len(cov_xs)
    cov_mean_y = sum(cov_ys, Fraction()) / len(cov_ys)
    cov_mean_xy = sum((x * y for x, y in zip(cov_xs, cov_ys)), Fraction()) / len(cov_xs)
    covariance = cov_mean_xy - cov_mean_x * cov_mean_y
    assert len(cov_ns) == 25
    assert covariance == Fraction(-127, 3000000)

    result = {
        "title": "Stage 58 exact targeted verification",
        "classification": "finite computational checks; no universal prime-pair claim",
        "runtime": platform.python_version(),
        "wheel_formula_vs_residue_scan": {
            "even_targets": len(wheel_targets),
            "range": [4, 500],
            "all_equal": True,
        },
        "ordered_pair_diagonal_identity": {
            "even_targets": (fourier_check_limit - 4) // 2 + 1,
            "range": [4, fourier_check_limit],
            "identity": "ordered_count = 2*R_distinct + 1_(N/2 prime)",
            "all_equal": True,
        },
        "block_moment_implication": {
            "vectors_tested": vectors_tested,
            "lengths": [2, max_k],
            "entries": [0, vector_bound],
            "all_implications_hold": True,
        },
        "positive_shift_average_countermodel": {
            "vector": toy,
            "cyclic_length": k,
            "zero_coordinate_present": True,
            "mean": fraction_text(toy_mean),
            "all_nonzero_shift_means_positive": True,
            "shift_records": toy_shift_checks,
        },
        "stage56_variance_counterexample": {
            "even_interval": [50, 150],
            "residual_count": k_var,
            "zero_representation_count": sum(len(pairs_trial(n)) == 0 for n in variance_ns),
            "variance": fraction_text(centered),
            "threshold": fraction_text(threshold),
            "ratio": fraction_text(variance_ratio),
        },
        "stage57_shifted_covariance_counterexample": {
            "anchor_interval": [262, 362],
            "shift_h": h,
            "residual_anchor_count": len(cov_ns),
            "covariance": fraction_text(covariance),
            "mean_product": fraction_text(cov_mean_xy),
            "product_of_means": fraction_text(cov_mean_x * cov_mean_y),
        },
        "exact_arithmetic": True,
        "large_sweep_performed": False,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
