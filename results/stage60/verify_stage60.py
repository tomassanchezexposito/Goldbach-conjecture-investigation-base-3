#!/usr/bin/env python3
"""Independent trial-division verifier for Stage 60 exact results.

This deliberately does not import compute_stage60.py and uses no sieve.
Only Python's standard library is required.
"""

from fractions import Fraction
from math import gcd, isqrt
import json
from pathlib import Path


DATA = Path(__file__).with_name("stage60_exact_results.json")


def prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def reps(n):
    return [(p, n - p) for p in range(2, n // 2 + 1)
            if p < n - p and prime(p) and prime(n - p)]


def wheel_direct(n):
    return sum(gcd(a, 210) == gcd(n - a, 210) == 1 for a in range(210))


def wheel_product(n):
    out = 1
    for ell in (2, 3, 5, 7):
        out *= ell - (1 if n % ell == 0 else 2)
    return out


def classifications(first, second):
    out = [0, 0, 0, 0, 0]
    for p, q in first:
        for r, s in second:
            matches = [p == r, p == s, q == r, q == s]
            assert sum(matches) <= 1
            out[matches.index(True) if any(matches) else 4] += 1
    return out


def residual(n):
    return n >= 4 and n % 2 == 0 and not prime(n - 1) and not prime(n // 2)


def frac_text(value):
    return f"{value.numerator}/{value.denominator}"


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    assert data["parameters"]["even_centers_inclusive"] == [8, 300]
    assert data["parameters"]["step"] == 2
    rows = data["rows"]
    assert len(rows) == 147
    residual_count = zero_count = passing_count = wheel_checks = 0
    for row in rows:
        n = row["center"]
        targets = [n - 2, n, n + 2]
        ps = [reps(t) for t in targets]
        rvals = [len(p) for p in ps]
        avals = [wheel_direct(t) for t in targets]
        assert avals == [wheel_product(t) for t in targets] == row["A_210"]
        wheel_checks += len(targets)
        assert rvals == row["R"]
        assert [residual(n - 2), residual(n), residual(n + 2)][1] == row["is_in_H"]
        xs = [Fraction(r, a) for r, a in zip(rvals, avals)]
        assert [frac_text(x) for x in xs] == row["X"]
        mean = sum(xs, Fraction()) / 3
        energy = (xs[1] - xs[0]) ** 2 + (xs[2] - xs[1]) ** 2
        assert frac_text(mean) == row["mean"]
        assert frac_text(energy) == row["path_energy"]
        assert (mean > 0 and mean * mean > Fraction(2, 9) * energy) == row["certificate_strict"]

        for i, r in enumerate(rvals):
            assert row["same_target_ordered_products"][i] == {
                "diagonal": r, "four_distinct": r * (r - 1), "ordered_product": r * r}
        names = ["shared_low_low", "shared_low_high", "shared_high_low",
                 "shared_high_high", "four_distinct"]
        left = dict(zip(names, classifications(ps[0], ps[1])))
        right = dict(zip(names, classifications(ps[1], ps[2])))
        assert left == row["shifted_N_minus_2_to_N"]
        assert right == row["shifted_N_to_N_plus_2"]
        assert left["shared_low_high"] == right["shared_low_high"] == 0
        assert sum(left.values()) == rvals[0] * rvals[1]
        assert sum(right.values()) == rvals[1] * rvals[2]
        assert all(r <= b for r, b in zip(rvals, row["candidate_budgets_B"]))
        for q, upper in zip((left["four_distinct"], right["four_distinct"]),
                            row["four_distinct_upper_bounds"]):
            assert q <= upper
        assert energy <= Fraction(row["path_energy_upper_bound"])
        if row["is_in_H"]:
            residual_count += 1
            zero_count += int(rvals[1] == 0)
            passing_count += int(row["certificate_strict"])

    assert residual_count == data["parameters"]["residual_centers"]
    assert residual_count == data["summary"]["residual_centers"]
    assert zero_count == data["summary"]["residual_centers_with_zero_R"]
    assert passing_count == data["summary"]["residual_centers_passing_measured_path_certificate"]
    assert wheel_checks == data["parameters"]["wheel_target_checks"]

    # Exhaustive arithmetic check of the sharp 3-point zero obstruction:
    # for all nonnegative integer triples with center zero, mu^2 <= 2E/9.
    triples = 0
    for left in range(16):
        for right in range(16):
            x = (Fraction(left), Fraction(0), Fraction(right))
            mu = sum(x, Fraction()) / 3
            e = (x[1] - x[0]) ** 2 + (x[2] - x[1]) ** 2
            assert mu * mu <= Fraction(2, 9) * e
            triples += 1
    print(json.dumps({"independent_method": "trial division plus direct residue enumeration",
                      "rows_verified": len(rows), "residual_centers": residual_count,
                      "zero_center_counts": zero_count,
                      "measured_certificates": passing_count,
                      "wheel_residue_checks": wheel_checks,
                      "zero_triples_checked": triples,
                      "all_assertions_passed": True}, indent=2))


if __name__ == "__main__":
    main()
