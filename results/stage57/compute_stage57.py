#!/usr/bin/env python3
"""Exact finite Stage 57 shifted prime-pair correlation experiment.

Uses only the Python standard library. Run from any directory with Python 3:
    python results/stage57/compute_stage57.py
The script rewrites only its sibling shifted_correlations.json file.
"""

from fractions import Fraction
import json
import platform
from pathlib import Path

MAX_N = 2000
SHIFTS = tuple(range(1, 11))
WHEEL_PRIMES = (2, 3, 5, 7)
OUTPUT = Path(__file__).with_name("shifted_correlations.json")


def is_prime_trial(n: int) -> bool:
    """Exact trial-division primality test, independent of the sieve below."""
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
    """H = even N >= 4 with N-1 and N/2 both composite."""
    return n >= 4 and n % 2 == 0 and is_composite_trial(n - 1) and is_composite_trial(n // 2)


def wheel_A(n: int) -> int:
    """Exact number of compatible residue classes modulo 210."""
    out = 1
    for ell in WHEEL_PRIMES:
        out *= ell - (1 if n % ell == 0 else 2)
    return out


def direct_wheel_count(n: int) -> int:
    """Independent direct enumeration of compatible reduced residues mod 210."""
    return sum(
        1
        for a in range(210)
        if _gcd(a, 210) == 1 and _gcd((n - a) % 210, 210) == 1
    )


def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def pairs_by_trial(n: int) -> list[tuple[int, int]]:
    """Enumerate p<q, p+q=n using trial division for every primality call."""
    pairs = []
    for p in range(2, n // 2 + 1):
        q = n - p
        if p < q and is_prime_trial(p) and is_prime_trial(q):
            pairs.append((p, q))
    return pairs


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


def classify(shared_low_low: int, shared_low_high: int,
             shared_high_low: int, shared_high_high: int) -> str:
    matches = (shared_low_low, shared_low_high, shared_high_low, shared_high_high)
    if sum(matches) == 0:
        return "four_distinct"
    if sum(matches) != 1:
        raise AssertionError("Positive shifts cannot share both primes")
    return ("low_low", "low_high", "high_low", "high_high")[matches.index(1)]


CATEGORIES = ("low_low", "low_high", "high_low", "high_high", "four_distinct")


def classify_pair_lists(left: list[tuple[int, int]], right: list[tuple[int, int]],
                        shift: int) -> dict[str, int]:
    counts = dict.fromkeys(CATEGORIES, 0)
    for p, q in left:
        for r, s in right:
            ll, lh, hl, hh = int(p == r), int(p == s), int(q == r), int(q == s)
            if shift > 0 and ll + lh + hl + hh > 1:
                raise AssertionError("Two shared summands force equal target sums")
            counts[classify(ll, lh, hl, hh)] += 1
    return counts


def classify_direct_nested(n: int, m: int, flags: bytearray) -> dict[str, int]:
    """Direct p,r scan using sieve flags; does not call the pair-list routine."""
    counts = dict.fromkeys(CATEGORIES, 0)
    for p in range(2, n // 2 + 1):
        q = n - p
        if p >= q or not flags[p] or not flags[q]:
            continue
        for r in range(2, m // 2 + 1):
            s = m - r
            if r >= s or not flags[r] or not flags[s]:
                continue
            ll, lh, hl, hh = int(p == r), int(p == s), int(q == r), int(q == s)
            if ll + lh + hl + hh > 1:
                raise AssertionError("Two shared summands force equal target sums")
            counts[classify(ll, lh, hl, hh)] += 1
    return counts


def fraction_text(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def covariance_record(anchors: list[int], shift: int, reps: dict[int, int]) -> dict:
    xs = [Fraction(reps[n], wheel_A(n)) for n in anchors]
    ys = [Fraction(reps[n + 2 * shift], wheel_A(n + 2 * shift)) for n in anchors]
    products = [x * y for x, y in zip(xs, ys)]
    k = len(anchors)
    if not k:
        return {"count": 0, "mean_x": None, "mean_y": None,
                "mean_product": None, "product_of_means": None, "covariance": None,
                "factorization_inequality_passes": None}
    mean_x, mean_y = sum(xs, Fraction()) / k, sum(ys, Fraction()) / k
    mean_product = sum(products, Fraction()) / k
    product_of_means = mean_x * mean_y
    return {
        "count": k,
        "mean_x": fraction_text(mean_x),
        "mean_y": fraction_text(mean_y),
        "mean_product": fraction_text(mean_product),
        "product_of_means": fraction_text(product_of_means),
        "covariance": fraction_text(mean_product - product_of_means),
        "factorization_inequality_passes": mean_product >= product_of_means,
    }


def main() -> None:
    residuals = [n for n in range(4, MAX_N + 1, 2) if residual(n)]
    trial_pairs = {n: pairs_by_trial(n) for n in range(4, MAX_N + 1, 2)}
    flags = sieve(MAX_N)

    # Independently obtain R(N) by a direct scan over all lower summands with sieve flags.
    sieve_counts = {}
    for n in range(4, MAX_N + 1, 2):
        sieve_counts[n] = sum(
            1 for p in range(2, n // 2 + 1)
            if p < n - p and flags[p] and flags[n - p]
        )
        assert sieve_counts[n] == len(trial_pairs[n]), ("prime-pair methods disagree", n)

    # Exact wheel formula is checked against all compatible residues for each target.
    wheel_values = {}
    for n in range(4, MAX_N + 1, 2):
        wheel_values[n] = wheel_A(n)
        assert wheel_values[n] == direct_wheel_count(n), ("wheel methods disagree", n)

    rows = []
    aggregate_by_shift = {}
    for h in SHIFTS:
        shift_aggregates = dict.fromkeys(CATEGORIES, 0)
        normalized_sums = {category: Fraction() for category in CATEGORIES}
        both_residual_anchors = 0
        anchors = [n for n in residuals if n + 2 * h <= MAX_N]
        for n in anchors:
            m = n + 2 * h
            method1 = classify_pair_lists(trial_pairs[n], trial_pairs[m], h)
            method2 = classify_direct_nested(n, m, flags)
            assert method1 == method2, ("correlation methods disagree", n, h, method1, method2)
            total = sum(method1.values())
            assert total == len(trial_pairs[n]) * len(trial_pairs[m])
            assert total == sieve_counts[n] * sieve_counts[m]
            assert sum(method1[c] for c in CATEGORIES[:-1]) + method1["four_distinct"] == total
            if residual(m):
                both_residual_anchors += 1
            denominator = wheel_A(n) * wheel_A(m)
            row = {
                "N": n,
                "h": h,
                "M": m,
                "N_in_H": True,
                "M_in_H": residual(m),
                "R_N": len(trial_pairs[n]),
                "R_M": len(trial_pairs[m]),
                "A_210_N": wheel_A(n),
                "A_210_M": wheel_A(m),
                "shared_prime_position_counts": {c: method1[c] for c in CATEGORIES[:-1]},
                "four_distinct_off_diagonal_count": method1["four_distinct"],
                "ordered_representation_pair_count": total,
                "normalized_category_terms": {
                    c: fraction_text(Fraction(method1[c], denominator)) for c in CATEGORIES
                },
                "normalized_shifted_correlation": fraction_text(Fraction(total, denominator)),
            }
            rows.append(row)
            for category in CATEGORIES:
                shift_aggregates[category] += method1[category]
                normalized_sums[category] += Fraction(method1[category], denominator)

        total_ordered = sum(shift_aggregates.values())
        assert total_ordered == sum(
            len(trial_pairs[n]) * len(trial_pairs[n + 2 * h]) for n in anchors
        )
        aggregate_by_shift[str(h)] = {
            "anchor_count_N_in_H": len(anchors),
            "anchor_count_with_N_plus_2h_in_H": both_residual_anchors,
            "raw_ordered_pair_counts_by_category": shift_aggregates,
            "raw_ordered_pair_count_total": total_ordered,
            "sum_of_normalized_category_terms": {
                c: fraction_text(normalized_sums[c]) for c in CATEGORIES
            },
            "sum_of_normalized_shifted_correlations": fraction_text(sum(normalized_sums.values(), Fraction())),
            "mean_normalized_shifted_correlation": fraction_text(
                sum(normalized_sums.values(), Fraction()) / len(anchors)
            ) if anchors else None,
            "factorization_covariance_on_all_residual_anchors": covariance_record(anchors, h, sieve_counts),
        }

    # Search a concrete family of proposed stronger-than-identity heuristic inequalities:
    # on a block of residual anchors, mean(X_N X_(N+2h)) >= mean(X_N) mean(X_(N+2h)).
    # This is not needed by the exact identity and is not presumed to be a theorem.
    covariance_windows = []
    tested_covariance_windows = 0
    window_width = 100  # even-integer endpoints [L,L+100], inclusive
    for h in SHIFTS:
        for lower in range(4, MAX_N - window_width + 1, 2):
            anchors = [n for n in residuals if lower <= n <= lower + window_width and n + 2 * h <= MAX_N]
            if len(anchors) >= 2:
                tested_covariance_windows += 1
                record = covariance_record(anchors, h, sieve_counts)
                if not record["factorization_inequality_passes"]:
                    covariance_windows.append({
                        "h": h,
                        "even_integer_interval": [lower, lower + window_width],
                        "anchor_count": len(anchors),
                        "covariance": record["covariance"],
                        "mean_product": record["mean_product"],
                        "product_of_means": record["product_of_means"],
                    })

    pointwise_zeros = [n for n in residuals if sieve_counts[n] == 0]
    output = {
        "title": "Stage 57 exact shifted four-prime correlations",
        "evidence_classification": "Computational observation on the stated finite domain",
        "definitions": {
            "H": "even N >= 4 such that N-1 and N/2 are composite",
            "R(N)": "number of unordered distinct-prime pairs (p,q) with p<q and p+q=N",
            "A_210(N)": "number of compatible ordered residue classes a mod 210 with gcd(a,210)=gcd(N-a,210)=1",
            "C_210_note": "Stage 56 also used C_210 for this compatible-pair count; A_210 and that C_210 have the same integer value here, while the notation is kept explicit",
            "X_N": "R(N)/A_210(N)",
            "shifted_count": "R(N)R(N+2h), ordered choices of one representation at each target",
            "shared_positions": ["low_low: p=r", "low_high: p=s", "high_low: q=r", "high_high: q=s"],
            "off_diagonal": "four distinct prime values; for h>0 two shared positions are impossible",
        },
        "parameters": {
            "maximum_even_target": MAX_N,
            "shifts_h": list(SHIFTS),
            "target_relation": "M=N+2h",
            "anchor_domain": "N in H, 4<=N<=2000, and M<=2000",
            "python_version": platform.python_version(),
            "implementation": "Python standard library only; exact integers and fractions.Fraction",
        },
        "finite_summary": {
            "residual_count_through_2000": len(residuals),
            "residual_zero_representation_targets_through_2000": pointwise_zeros,
            "rows": len(rows),
            "wheel_factor_values_checked_against_direct_mod_210_enumeration": 999,
            "prime_pair_counts_checked_between_trial_division_and_sieve": 999,
        },
        "exact_identity": "R(N)R(M)=S_LL+S_LH+S_HL+S_HH+Q_4; X_N X_M is this identity divided by A_210(N)A_210(M)",
        "aggregates_by_shift": aggregate_by_shift,
        "covariance_heuristic": {
            "candidate_inequality": "mean(X_N X_(N+2h)) >= mean(X_N) mean(X_(N+2h)) on a specified residual-anchor block",
            "status": "Finite audit only; no theorem asserted",
            "window_even_integer_width": window_width,
            "sliding_window_step": 2,
            "windows_with_at_least_two_eligible_anchors_tested": tested_covariance_windows,
            "counterexample_count": len(covariance_windows),
            "counterexamples": covariance_windows,
            "logical_limitation": "Even if this average inequality held, it would not imply R(N)>0 at each target; an independent pointwise lower bound is still required.",
        },
        "rows": rows,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("Stage 57 exact computations completed.")
    print(f"Residual targets N<=2000: {len(residuals)}; zero counts: {len(pointwise_zeros)}")
    print(f"Correlation rows (N in H, N+2h<=2000, h=1..10): {len(rows)}")
    print(f"Shifted covariance-window counterexamples: {len(covariance_windows)}")
    for h in SHIFTS:
        a = aggregate_by_shift[str(h)]
        print(f"h={h}: anchors={a['anchor_count_N_in_H']}, both_in_H={a['anchor_count_with_N_plus_2h_in_H']}, "
              f"sum_X_product={a['sum_of_normalized_shifted_correlations']}")
    print(f"Wrote {OUTPUT.name}")


if __name__ == "__main__":
    main()
