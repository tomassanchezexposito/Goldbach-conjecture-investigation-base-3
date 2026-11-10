#!/usr/bin/env python3
"""Independent checker for Stage 57 JSON output (standard library only)."""
from fractions import Fraction
import json
from pathlib import Path

DATA = Path(__file__).with_name("shifted_correlations.json")
WHEEL_PRIMES = (2, 3, 5, 7)
CATEGORIES = ("low_low", "low_high", "high_low", "high_high", "four_distinct")


def sieve(n):
    prime = bytearray(b"\x01") * (n + 1)
    prime[0:2] = b"\x00\x00"
    p = 2
    while p * p <= n:
        if prime[p]:
            for m in range(p * p, n + 1, p):
                prime[m] = 0
        p += 1
    return prime


def wheel_direct(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return sum(
        gcd(a, 210) == 1 and gcd((n - a) % 210, 210) == 1
        for a in range(210)
    )


def wheel_product(n):
    value = 1
    for ell in WHEEL_PRIMES:
        value *= ell - (1 if n % ell == 0 else 2)
    return value


def representation_pairs(n, prime):
    pairs = []
    for p in range(2, n // 2 + 1):
        q = n - p
        if p < q and prime[p] and prime[q]:
            pairs.append((p, q))
    return pairs


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    limit = data["parameters"]["maximum_even_target"]
    prime = sieve(limit)
    even_targets = range(4, limit + 1, 2)
    h_targets = [n for n in even_targets if n - 1 > 1 and not prime[n - 1]
                 and n // 2 > 1 and not prime[n // 2]]
    assert len(h_targets) == data["finite_summary"]["residual_count_through_2000"]
    assert not [n for n in h_targets if not representation_pairs(n, prime)]
    for n in even_targets:
        assert wheel_product(n) == wheel_direct(n)

    aggregates = {
        str(h): {"rows": 0, "both_in_H": 0, "counts": dict.fromkeys(CATEGORIES, 0),
                 "normalized": {c: Fraction() for c in CATEGORIES}}
        for h in data["parameters"]["shifts_h"]
    }
    for row in data["rows"]:
        n, m, h = row["N"], row["M"], row["h"]
        assert n in h_targets and m == n + 2 * h and m <= limit
        left, right = representation_pairs(n, prime), representation_pairs(m, prime)
        assert (len(left), len(right)) == (row["R_N"], row["R_M"])
        assert row["A_210_N"] == wheel_direct(n)
        assert row["A_210_M"] == wheel_direct(m)
        counts = dict.fromkeys(CATEGORIES, 0)
        for p, q in left:
            for r, s in right:
                matches = (p == r, p == s, q == r, q == s)
                assert sum(matches) <= 1
                if not any(matches):
                    category = "four_distinct"
                else:
                    category = CATEGORIES[matches.index(True)]
                counts[category] += 1
        assert counts == {
            **row["shared_prime_position_counts"],
            "four_distinct": row["four_distinct_off_diagonal_count"],
        }
        total = len(left) * len(right)
        assert sum(counts.values()) == total == row["ordered_representation_pair_count"]
        denominator = wheel_direct(n) * wheel_direct(m)
        assert Fraction(total, denominator) == Fraction(row["normalized_shifted_correlation"])
        assert row["normalized_category_terms"] == {
            c: str(Fraction(counts[c], denominator).numerator)
            if Fraction(counts[c], denominator).denominator == 1
            else f"{Fraction(counts[c], denominator).numerator}/{Fraction(counts[c], denominator).denominator}"
            for c in CATEGORIES
        }
        bucket = aggregates[str(h)]
        bucket["rows"] += 1
        bucket["both_in_H"] += int(m in h_targets)
        for c in CATEGORIES:
            bucket["counts"][c] += counts[c]
            bucket["normalized"][c] += Fraction(counts[c], denominator)

    for h, bucket in aggregates.items():
        source = data["aggregates_by_shift"][h]
        assert bucket["rows"] == source["anchor_count_N_in_H"]
        assert bucket["both_in_H"] == source["anchor_count_with_N_plus_2h_in_H"]
        assert bucket["counts"] == source["raw_ordered_pair_counts_by_category"]
        assert sum(bucket["counts"].values()) == source["raw_ordered_pair_count_total"]
        for c in CATEGORIES:
            assert bucket["normalized"][c] == Fraction(source["sum_of_normalized_category_terms"][c])

    print(f"Independent verifier passed: {len(data['rows'])} rows, {len(h_targets)} residual targets, "
          f"all {limit // 2 - 1} wheel values, all five correlation categories and shift aggregates.")


if __name__ == "__main__":
    main()
