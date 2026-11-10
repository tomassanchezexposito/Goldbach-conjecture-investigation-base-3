#!/usr/bin/env sage -python
"""Stage 58 exact moment and shifted four-prime computation.

Run from any directory with:
    sage -python results/stage58/compute_second_moment.sage.py

This is a bounded exact computation. It is not a Goldbach proof. The companion
verify_second_moment.py uses only Python's standard library and a separate
prime sieve to check the saved JSON independently.
"""

from fractions import Fraction
from functools import lru_cache
import json
import platform
from pathlib import Path

from sage.all import QQ, is_prime
from sage.version import version as sage_version


OUT = Path(__file__).with_name("second_moment_exact.json")
WHEEL_PRIMES = (2, 3, 5, 7)
MAX_ANCHOR = 300
MAX_SHIFT = 10
SMALL_PRIMES = (2, 3, 5, 7)
CATEGORIES = ("shared_low_low", "shared_low_high", "shared_high_low",
              "shared_high_high", "four_distinct")


@lru_cache(maxsize=None)
def prime(n):
    return n >= 2 and bool(is_prime(n))


def composite(n):
    return n > 1 and not prime(n)


def in_h(n):
    return n >= 4 and n % 2 == 0 and composite(n - 1) and composite(n // 2)


def wheel_a(n):
    value = 1
    for ell in WHEEL_PRIMES:
        value *= ell - (1 if n % ell == 0 else 2)
    return value


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def wheel_by_residues(n):
    return sum(gcd(a, 210) == 1 and gcd((n - a) % 210, 210) == 1
               for a in range(210))


def representations(n):
    """Unordered distinct-prime pairs, in low/high order."""
    return [(p, n - p) for p in range(2, n // 2 + 1)
            if p < n - p and prime(p) and prime(n - p)]


def classify_pair_products(left, right):
    counts = dict.fromkeys(CATEGORIES, 0)
    for p, q in left:
        for r, s in right:
            matches = (p == r, p == s, q == r, q == s)
            if sum(matches) > 1:
                raise AssertionError("A positive shift cannot share two primes")
            if not any(matches):
                counts["four_distinct"] += 1
            else:
                counts[CATEGORIES[matches.index(True)]] += 1
    return counts


def classify_direct_scan(n, m):
    """Independent p,r candidate scan, without representation-list products."""
    counts = dict.fromkeys(CATEGORIES, 0)
    for p in range(2, n // 2 + 1):
        q = n - p
        if p >= q or not prime(p) or not prime(q):
            continue
        for r in range(2, m // 2 + 1):
            s = m - r
            if r >= s or not prime(r) or not prime(s):
                continue
            matches = (p == r, p == s, q == r, q == s)
            if sum(matches) > 1:
                raise AssertionError("A positive shift cannot share two primes")
            if not any(matches):
                counts["four_distinct"] += 1
            else:
                counts[CATEGORIES[matches.index(True)]] += 1
    return counts


def qtext(value):
    value = QQ(value)
    return str(value.numerator()) if value.denominator() == 1 else (
        f"{value.numerator()}/{value.denominator()}")


def fraction_from_q(value):
    value = QQ(value)
    return Fraction(int(value.numerator()), int(value.denominator()))


def moment_record(ns, counts):
    xs = [QQ(counts[n]) / wheel_a(n) for n in ns]
    k = len(xs)
    mu = sum(xs, QQ(0)) / k
    second = sum((x * x for x in xs), QQ(0)) / k
    variance = second - mu * mu
    threshold = QQ(k) / (k - 1) * mu * mu if k > 1 else None
    return {
        "count": k,
        "zero_representation_counts": sum(counts[n] == 0 for n in ns),
        "mean": qtext(mu),
        "second_moment": qtext(second),
        "centered_sum_squares": qtext(k * variance),
        "single_zero_threshold": None if threshold is None else qtext(threshold),
        "variance_to_threshold_ratio": None if not threshold else qtext(k * variance / threshold),
        "normalized_values": [qtext(x) for x in xs],
    }


def weighted_moment_checks():
    # Exact equality cases and exhaustive small nonnegative rational vectors.
    weight_vectors = [tuple(QQ(x) for x in (QQ(1) / 2, QQ(1) / 3, QQ(1) / 6)),
                      tuple(QQ(1) / 4 for _ in range(4))]
    checked = 0
    equality_cases = []
    for weights in weight_vectors:
        assert sum(weights) == 1
        for j, wj in enumerate(weights):
            values = [QQ(2) if i != j else QQ(0) for i in range(len(weights))]
            mu = sum((w * x for w, x in zip(weights, values)), QQ(0))
            second = sum((w * x * x for w, x in zip(weights, values)), QQ(0))
            assert second == mu * mu / (1 - wj)
            equality_cases.append({"weights": [qtext(w) for w in weights],
                                   "zero_index": j,
                                   "mean": qtext(mu),
                                   "second_moment": qtext(second),
                                   "sharp_lower_bound": qtext(mu * mu / (1 - wj))})

        # Exhaust all vectors in {0,1,2,3}^k; every zero must obey its
        # coordinate-specific weighted Cauchy-Schwarz lower bound.
        from itertools import product
        for values in product(range(4), repeat=len(weights)):
            mu = sum((w * x for w, x in zip(weights, values)), QQ(0))
            second = sum((w * x * x for w, x in zip(weights, values)), QQ(0))
            for j, xj in enumerate(values):
                if xj == 0:
                    assert second >= mu * mu / (1 - weights[j])
            checked += 1
    return {"finite_vectors_checked": checked,
            "entry_values": [0, 1, 2, 3],
            "weight_vectors": [[qtext(w) for w in ws] for ws in weight_vectors],
            "sharp_equality_cases": equality_cases,
            "all_coordinate_zero_bounds_pass": True}


def main():
    targets = list(range(4, 502, 2))
    wheel_equalities = [n for n in targets if wheel_a(n) == wheel_by_residues(n)]

    # Prime-pair counts and independent same-target identity bookkeeping.
    even_targets = list(range(4, MAX_ANCHOR + 1, 2))
    pair_lists = {n: representations(n) for n in even_targets}
    diagonal_rows = []
    for n in even_targets:
        pairs = pair_lists[n]
        products = [(left, right) for left in pairs for right in pairs]
        diagonal = sum(left == right for left, right in products)
        exactly_one_shared = sum(
            sum((left[0] == right[0], left[0] == right[1],
                 left[1] == right[0], left[1] == right[1])) == 1
            for left, right in products)
        four_distinct = sum(len(set(left + right)) == 4 for left, right in products)
        ordered = sum(prime(p) and prime(n - p) for p in range(2, n - 1))
        half_diagonal = int(prime(n // 2))
        assert diagonal == len(pairs)
        assert exactly_one_shared == 0
        assert four_distinct == len(pairs) * (len(pairs) - 1)
        assert ordered == 2 * len(pairs) + half_diagonal
        diagonal_rows.append({"N": n, "R_distinct": len(pairs),
                              "unordered_pair_product_diagonal": diagonal,
                              "one_shared_position": exactly_one_shared,
                              "four_distinct_off_diagonal": four_distinct,
                              "ordered_fourier_count": ordered,
                              "ordered_diagonal": half_diagonal})

    residuals = [n for n in even_targets if in_h(n)]
    shifted_rows = []
    shift_totals = {}
    for h in range(1, MAX_SHIFT + 1):
        totals = dict.fromkeys(CATEGORIES, 0)
        small_exception_total = 0
        all_large_four_total = 0
        for n in residuals:
            m = n + 2 * h
            left = pair_lists[n]
            right = pair_lists.get(m)
            if right is None:
                right = representations(m)
            by_lists = classify_pair_products(left, right)
            by_scan = classify_direct_scan(n, m)
            assert by_lists == by_scan, (n, h, by_lists, by_scan)
            assert sum(by_lists.values()) == len(left) * len(right)

            small_q4 = sum(
                1 for (p, q) in left for (r, s) in right
                if len({p, q, r, s}) == 4 and min(p, q, r, s) <= 7)
            large_q4 = by_lists["four_distinct"] - small_q4
            assert small_q4 + large_q4 == by_lists["four_distinct"]
            # Prime 2 cannot occur in a distinct representation of an even target.
            assert all(2 not in pair for pair in left + right)
            for p, q, r, s in ((p, q, r, s) for p, q in left for r, s in right
                               if len({p, q, r, s}) == 4 and min(p, q, r, s) > 7):
                assert all(gcd(x, 210) == 1 for x in (p, q, r, s))
                assert (p + q - n) % 210 == 0 and (r + s - m) % 210 == 0

            row = {"N": n, "h": h, "M": m,
                   "R_N": len(left), "R_M": len(right),
                   "categories": by_lists,
                   "four_distinct_with_prime_at_most_7": small_q4,
                   "four_distinct_all_primes_above_7": large_q4,
                   "A_210_N": wheel_a(n), "A_210_M": wheel_a(m),
                   "normalized_shifted_correlation": qtext(
                       QQ(len(left) * len(right)) / (wheel_a(n) * wheel_a(m)))}
            shifted_rows.append(row)
            for category in CATEGORIES:
                totals[category] += by_lists[category]
            small_exception_total += small_q4
            all_large_four_total += large_q4
        shift_totals[str(h)] = {
            "anchor_count": len(residuals),
            "row_count": len(residuals),
            "raw_counts_by_category": totals,
            "four_distinct_with_prime_at_most_7": small_exception_total,
            "four_distinct_all_primes_above_7": all_large_four_total,
            "normalized_sum": qtext(sum(
                (QQ(row["R_N"] * row["R_M"]) / (row["A_210_N"] * row["A_210_M"])
                 for row in shifted_rows if row["h"] == h), QQ(0)))
        }

    rep_counts = {n: len(pair_lists[n]) for n in even_targets}
    block_rows = {}
    for lo, hi in ((50, 150), (50, 200), (202, 300)):
        ns = [n for n in residuals if lo <= n <= hi]
        block_rows[f"{lo}-{hi}"] = moment_record(ns, rep_counts)

    result = {
        "title": "Stage 58 exact pointwise moment and shifted four-prime checks",
        "classification": "bounded exact computations; not a universal prime-pair proof",
        "runtime": {"python": platform.python_version(), "sagemath": str(sage_version)},
        "parameters": {"wheel_even_targets_inclusive": [4, 500],
                       "diagonal_even_targets_inclusive": [4, MAX_ANCHOR],
                       "residual_anchor_even_targets_inclusive": [4, MAX_ANCHOR],
                       "positive_shifts_h": [1, MAX_SHIFT],
                       "shifted_targets_maximum": MAX_ANCHOR + 2 * MAX_SHIFT,
                       "small_exceptional_prime_cutoff": 7},
        "wheel_formula_vs_residue_enumeration": {
            "targets_checked": len(wheel_equalities), "all_equal": len(wheel_equalities) == len(targets),
            "A_210_examples": {str(n): wheel_a(n) for n in (4, 6, 10, 30, 42, 50)}},
        "same_target_decomposition": {
            "targets_checked": len(diagonal_rows),
            "identity": "R_distinct^2 = R_distinct diagonal + R_distinct*(R_distinct-1) four-distinct terms",
            "ordered_fourier_identity": "ordered_count = 2*R_distinct + 1_(N/2 prime)",
            "one_shared_position_count": 0,
            "rows": diagonal_rows},
        "finite_residual_pair_search": {
            "even_target_range_inclusive": [4, MAX_ANCHOR],
            "residual_targets_checked": len(residuals),
            "zero_representation_counts": sum(rep_counts[n] == 0 for n in residuals),
            "classification": "finite computational observation only"},
        "positive_shift_decomposition": {
            "categories": list(CATEGORIES),
            "identity": "R(N)R(N+2h) = sum(four shared-position classes) + four_distinct",
            "position_formula": {
                "shared_low_low": "p=r; q=N-p and s=q+2h",
                "shared_low_high": "p=s; impossible for p<q and r<s when h>0",
                "shared_high_low": "q=r; s=p+2h and p<q<p+2h",
                "shared_high_high": "q=s; r=p+2h and p+2h<q"},
            "rows_checked": len(shifted_rows),
            "shift_totals": shift_totals,
            "rows": shifted_rows},
        "small_prime_exception_audit": {
            "distinct_even_target_pair_contains_2": False,
            "primes_at_most_7_requiring_separate_residue_treatment": [3, 5, 7],
            "all_four_distinct_configurations_with_all_positions_above_7_are_reduced_mod_210": True,
            "meaning": "A_210 is a local admissibility count; small-prime configurations remain exact separate terms."},
        "finite_block_moments": block_rows,
        "weighted_sharp_moment_lemma_checks": weighted_moment_checks(),
        "exact_arithmetic": "SageMath QQ rational arithmetic and integer prime tests",
        "independent_verification": "verify_second_moment.py uses a standard-library Eratosthenes sieve and Fraction arithmetic"
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(OUT),
                      "wheel_targets": len(wheel_equalities),
                      "same_target_even_targets": len(diagonal_rows),
                      "residual_anchors": len(residuals),
                      "shifted_rows": len(shifted_rows),
                      "blocks": {k: {key: val for key, val in v.items()
                                     if key != "normalized_values"}
                                for k, v in block_rows.items()},
                      "weighted_vectors_checked": result["weighted_sharp_moment_lemma_checks"]["finite_vectors_checked"]},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
