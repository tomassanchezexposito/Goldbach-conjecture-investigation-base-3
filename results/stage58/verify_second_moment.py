#!/usr/bin/env python3
"""Independent standard-library verifier for the Stage 58 Sage results.

Run after compute_second_moment.sage.py:
    python results/stage58/verify_second_moment.py

This script uses an Eratosthenes sieve and Fraction arithmetic. It does not
import Sage or call the Sage computation's prime-pair/correlation routines.
"""

from fractions import Fraction
from itertools import product
import json
import platform
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUT = HERE / "second_moment_exact.json"
OUTPUT = HERE / "second_moment_verification.json"
WHEEL_PRIMES = (2, 3, 5, 7)
CATEGORIES = ("shared_low_low", "shared_low_high", "shared_high_low",
              "shared_high_high", "four_distinct")


def sieve(limit):
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0: min(2, limit + 1)] = b"\x00" * min(2, limit + 1)
    p = 2
    while p * p <= limit:
        if flags[p]:
            start = p * p
            flags[start: limit + 1: p] = b"\x00" * (((limit - start) // p) + 1)
        p += 1
    return flags


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def wheel_formula(n):
    out = 1
    for ell in WHEEL_PRIMES:
        out *= ell - (1 if n % ell == 0 else 2)
    return out


def wheel_scan(n):
    return sum(gcd(a, 210) == 1 and gcd((n - a) % 210, 210) == 1
               for a in range(210))


def is_h(n, flags):
    return (n >= 4 and n % 2 == 0 and n - 1 > 1 and not flags[n - 1]
            and n // 2 > 1 and not flags[n // 2])


def pairs(n, flags):
    return [(p, n - p) for p in range(2, n // 2 + 1)
            if p < n - p and flags[p] and flags[n - p]]


def text_fraction(value):
    return str(value.numerator) if value.denominator == 1 else (
        f"{value.numerator}/{value.denominator}")


def direct_category_scan(n, m, flags):
    """Candidate-position scan, independently of saved pair-list products."""
    out = dict.fromkeys(CATEGORIES, 0)
    for p in range(2, n // 2 + 1):
        q = n - p
        if p >= q or not flags[p] or not flags[q]:
            continue
        for r in range(2, m // 2 + 1):
            s = m - r
            if r >= s or not flags[r] or not flags[s]:
                continue
            equalities = (p == r, p == s, q == r, q == s)
            if sum(equalities) > 1:
                raise AssertionError(("two shared values", n, m, p, q, r, s))
            if any(equalities):
                out[CATEGORIES[equalities.index(True)]] += 1
            else:
                out["four_distinct"] += 1
    return out


def pair_list_category(left, right):
    """Second independent construction: Cartesian products of explicit pairs."""
    out = dict.fromkeys(CATEGORIES, 0)
    for p, q in left:
        for r, s in right:
            equalities = (p == r, p == s, q == r, q == s)
            if sum(equalities) > 1:
                raise AssertionError("two shared values at distinct targets")
            if any(equalities):
                out[CATEGORIES[equalities.index(True)]] += 1
            else:
                out["four_distinct"] += 1
    return out


def main():
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    params = data["parameters"]
    wheel_low, wheel_high = params["wheel_even_targets_inclusive"]
    max_anchor = params["residual_anchor_even_targets_inclusive"][1]
    max_shift = params["positive_shifts_h"][1]
    max_target = max_anchor + 2 * max_shift
    flags = sieve(max(wheel_high, max_target))

    wheel_ns = list(range(wheel_low, wheel_high + 1, 2))
    assert all(wheel_formula(n) == wheel_scan(n) for n in wheel_ns)
    assert data["wheel_formula_vs_residue_enumeration"]["targets_checked"] == len(wheel_ns)

    even_ns = list(range(4, max_anchor + 1, 2))
    diagonal_rows = {row["N"]: row for row in data["same_target_decomposition"]["rows"]}
    assert set(diagonal_rows) == set(even_ns)
    for n in even_ns:
        ps = pairs(n, flags)
        r_count = len(ps)
        row = diagonal_rows[n]
        assert row["R_distinct"] == r_count
        assert row["unordered_pair_product_diagonal"] == r_count
        assert row["one_shared_position"] == 0
        assert row["four_distinct_off_diagonal"] == r_count * (r_count - 1)
        ordered = sum(flags[p] and flags[n - p] for p in range(2, n - 1))
        assert row["ordered_fourier_count"] == ordered
        assert ordered == 2 * r_count + int(bool(flags[n // 2]))

    residuals = [n for n in even_ns if is_h(n, flags)]
    shifted_rows = {(row["N"], row["h"]): row
                    for row in data["positive_shift_decomposition"]["rows"]}
    assert len(shifted_rows) == len(residuals) * max_shift
    for n in residuals:
        left = pairs(n, flags)
        assert 2 not in {x for pair in left for x in pair}
        for h in range(1, max_shift + 1):
            m = n + 2 * h
            right = pairs(m, flags)
            row = shifted_rows[n, h]
            by_pairs = pair_list_category(left, right)
            by_scan = direct_category_scan(n, m, flags)
            assert by_pairs == by_scan == row["categories"], (n, h)
            assert sum(by_scan.values()) == len(left) * len(right)
            small_q4 = sum(
                min(p, q, r, s) <= 7
                for p, q in left for r, s in right
                if len({p, q, r, s}) == 4)
            assert row["four_distinct_with_prime_at_most_7"] == small_q4
            assert row["four_distinct_all_primes_above_7"] == (
                by_scan["four_distinct"] - small_q4)
            for p, q in left:
                for r, s in right:
                    if len({p, q, r, s}) == 4 and min(p, q, r, s) > 7:
                        assert all(gcd(x, 210) == 1 for x in (p, q, r, s))
                        assert (p + q - n) % 210 == 0
                        assert (r + s - m) % 210 == 0

    # Independently reconstruct all finite block moments from the sieve counts.
    block_checks = {}
    for label, block in data["finite_block_moments"].items():
        low, high = map(int, label.split("-"))
        ns = [n for n in residuals if low <= n <= high]
        xs = [Fraction(len(pairs(n, flags)), wheel_formula(n)) for n in ns]
        k = len(xs)
        mean = sum(xs, Fraction()) / k
        second = sum((x * x for x in xs), Fraction()) / k
        centered = sum(((x - mean) ** 2 for x in xs), Fraction())
        threshold = Fraction(k, k - 1) * mean * mean if k > 1 else None
        assert block["count"] == k
        assert block["zero_representation_counts"] == sum(x == 0 for x in xs)
        assert block["mean"] == text_fraction(mean)
        assert block["second_moment"] == text_fraction(second)
        assert block["centered_sum_squares"] == text_fraction(centered)
        assert block["single_zero_threshold"] == (None if threshold is None
                                                   else text_fraction(threshold))
        ratio = None if not threshold else centered / threshold
        assert block["variance_to_threshold_ratio"] == (
            None if ratio is None else text_fraction(ratio))
        block_checks[label] = {"residual_count": k,
                               "zero_count": sum(x == 0 for x in xs),
                               "mean": text_fraction(mean),
                               "second_moment": text_fraction(second),
                               "centered_sum_squares": text_fraction(centered),
                               "centered_to_zero_threshold_ratio": (
                                   None if ratio is None else text_fraction(ratio))}

    # Finite exact audit of the weighted Cauchy-Schwarz inequality and its sharpness.
    weighted = data["weighted_sharp_moment_lemma_checks"]
    vectors_checked = 0
    equality_checks = 0
    for weight_texts in weighted["weight_vectors"]:
        weights = [Fraction(x) for x in weight_texts]
        assert sum(weights) == 1
        for values in product(range(4), repeat=len(weights)):
            mean = sum(w * x for w, x in zip(weights, values))
            second = sum(w * x * x for w, x in zip(weights, values))
            for j, xj in enumerate(values):
                if xj == 0:
                    assert second >= mean * mean / (1 - weights[j])
            vectors_checked += 1
        for j, wj in enumerate(weights):
            values = [Fraction(2) if i != j else Fraction(0)
                      for i in range(len(weights))]
            mean = sum(w * x for w, x in zip(weights, values))
            second = sum(w * x * x for w, x in zip(weights, values))
            assert second == mean * mean / (1 - wj)
            equality_checks += 1
    assert vectors_checked == weighted["finite_vectors_checked"]

    result = {
        "status": "all independent exact checks passed",
        "runtime": platform.python_version(),
        "method": "Python standard-library Eratosthenes sieve and fractions.Fraction",
        "wheel_targets_checked": len(wheel_ns),
        "same_target_even_targets_checked": len(even_ns),
        "residual_anchors_checked": len(residuals),
        "positive_shift_rows_checked": len(shifted_rows),
        "pair_list_vs_direct_scan_category_counts": "all equal row by row",
        "finite_block_moment_checks": block_checks,
        "weighted_zero_coordinate_vectors_checked": vectors_checked,
        "weighted_sharp_equality_cases_checked": equality_checks,
        "universal_claim": False,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                      encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
