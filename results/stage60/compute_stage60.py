#!/usr/bin/env python3
"""Exact bounded audit of Stage 60 local four-position identities.

This is a finite computation, not an analytic estimate for all targets.
Only Python's standard library is required.
"""

from fractions import Fraction
import json
from pathlib import Path


OUT = Path(__file__).with_name("stage60_exact_results.json")
EVEN_MAX = 300


def sieve(limit):
    prime = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        prime[0] = 0
    if limit >= 1:
        prime[1] = 0
    for p in range(2, int(limit**0.5) + 1):
        if prime[p]:
            prime[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return prime


def wheel_a(n):
    ans = 1
    for ell in (2, 3, 5, 7):
        ans *= ell - (1 if n % ell == 0 else 2)
    return ans


def wheel_scan(n):
    return sum(
        1
        for a in range(210)
        if __import__("math").gcd(a, 210) == 1
        and __import__("math").gcd(n - a, 210) == 1
    )


def representations(n, prime):
    """Distinct unordered prime pairs, in low/high position order."""
    return [(p, n - p) for p in range(2, n // 2 + 1) if p < n - p and prime[p] and prime[n - p]]


def shifted_classes(low_pairs, high_pairs):
    """Classify ordered representation pairs by shared positions."""
    counts = {"shared_low_low": 0, "shared_low_high": 0,
              "shared_high_low": 0, "shared_high_high": 0,
              "four_distinct": 0}
    for p, q in low_pairs:
        for r, s in high_pairs:
            matches = (p == r, p == s, q == r, q == s)
            if sum(matches) > 1:
                raise AssertionError("Two shared positions force identical unordered pairs and sums")
            if not any(matches):
                counts["four_distinct"] += 1
            else:
                counts[("shared_low_low", "shared_low_high",
                        "shared_high_low", "shared_high_high")[matches.index(True)]] += 1
    return counts


def frac(x):
    return f"{x.numerator}/{x.denominator}"


def is_residual(n, prime):
    return n >= 4 and n % 2 == 0 and not prime[n - 1] and not prime[n // 2]


def candidate_budget(n):
    """Number of odd p with 3 <= p < n/2 for even n."""
    return max(0, (n - 4) // 4)


def main():
    prime = sieve(EVEN_MAX + 2)
    pair_cache = {n: representations(n, prime) for n in range(4, EVEN_MAX + 3, 2)}
    rows = []
    wheel_checks = 0
    for n in range(8, EVEN_MAX + 1, 2):
        targets = (n - 2, n, n + 2)
        pairs = [pair_cache[t] for t in targets]
        wheels = [wheel_a(t) for t in targets]
        for t, a in zip(targets, wheels):
            assert a == wheel_scan(t)
            wheel_checks += 1

        counts = [len(ps) for ps in pairs]
        xs = [Fraction(r, a) for r, a in zip(counts, wheels)]
        mean = sum(xs, Fraction()) / 3
        energy = (xs[1] - xs[0]) ** 2 + (xs[2] - xs[1]) ** 2

        same_target = []
        for r in counts:
            diagonal = r
            four_distinct = r * (r - 1)
            assert diagonal + four_distinct == r * r
            same_target.append({"diagonal": diagonal, "four_distinct": four_distinct,
                                "ordered_product": r * r})

        left = shifted_classes(pairs[0], pairs[1])
        right = shifted_classes(pairs[1], pairs[2])
        assert left["shared_low_high"] == right["shared_low_high"] == 0
        assert sum(left.values()) == counts[0] * counts[1]
        assert sum(right.values()) == counts[1] * counts[2]
        expanded_energy = (
            Fraction(counts[0], wheels[0]) ** 2
            + 2 * Fraction(counts[1], wheels[1]) ** 2
            + Fraction(counts[2], wheels[2]) ** 2
            - 2 * Fraction(counts[0] * counts[1], wheels[0] * wheels[1])
            - 2 * Fraction(counts[1] * counts[2], wheels[1] * wheels[2])
        )
        assert expanded_energy == energy

        budgets = [candidate_budget(t) for t in targets]
        assert all(r <= b for r, b in zip(counts, budgets))
        energy_upper = Fraction(budgets[0] ** 2 + 2 * budgets[1] ** 2
                                + budgets[2] ** 2, 225)
        assert energy <= energy_upper
        rows.append({
            "center": n,
            "is_in_H": is_residual(n, prime),
            "targets": list(targets),
            "R": counts,
            "A_210": wheels,
            "X": [frac(x) for x in xs],
            "mean": frac(mean),
            "path_energy": frac(energy),
            "sharp_center_constant": "2/9",
            "certificate_strict": mean > 0 and mean * mean > Fraction(2, 9) * energy,
            "same_target_ordered_products": same_target,
            "shifted_N_minus_2_to_N": left,
            "shifted_N_to_N_plus_2": right,
            "candidate_budgets_B": budgets,
            "four_distinct_upper_bounds": [budgets[0] * budgets[1], budgets[1] * budgets[2]],
            "path_energy_upper_bound": frac(energy_upper),
        })

    residual_rows = [r for r in rows if r["is_in_H"]]
    result = {
        "title": "Stage 60 exact bounded local four-position audit",
        "evidence_status": "Finite exact computation only; the elementary candidate bounds are proved in report.md.",
        "parameters": {"even_centers_inclusive": [8, EVEN_MAX],
                       "step": 2, "residual_centers": len(residual_rows),
                       "wheel_target_checks": wheel_checks},
        "definitions": {"H": "even n >= 4 with n-1 composite and n/2 composite",
                        "R": "unordered distinct prime pairs p<q with p+q=n",
                        "A_210": "exact locally admissible residue count modulo 210",
                        "X": "R/A_210"},
        "summary": {
            "residual_centers_with_zero_R": sum(any(v == 0 for v in r["R"][1:2]) for r in residual_rows),
            "residual_centers_passing_measured_path_certificate": sum(r["certificate_strict"] for r in residual_rows),
            "residual_centers": len(residual_rows),
            "max_R_over_candidate_budget": max(
                (Fraction(rv, b) for row in rows for rv, b in zip(row["R"], row["candidate_budgets_B"]) if b),
                default=Fraction(0)),
        },
        "rows": rows,
    }
    result["summary"]["max_R_over_candidate_budget"] = frac(result["summary"]["max_R_over_candidate_budget"])
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["parameters"] | result["summary"], indent=2))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
