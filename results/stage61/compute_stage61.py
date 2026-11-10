#!/usr/bin/env python3
"""Focused exact checks for the Stage 61 signed path-correlation identity.

Uses a sieve for a small, fixed set of target triples.  The independent
companion verifier uses trial division and does not import this module.
This is not a large Goldbach search and is not a universal proof.
"""

from fractions import Fraction
import json
from pathlib import Path


OUT = Path(__file__).with_name("stage61_exact_results.json")
CENTERS = (8, 10, 20, 34, 50, 100, 200, 500)


def sieve(limit):
    prime = bytearray(b"\x01") * (limit + 1)
    prime[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if prime[p]:
            prime[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return prime


def wheel_a(n):
    value = 1
    for ell in (2, 3, 5, 7):
        value *= ell - (1 if n % ell == 0 else 2)
    return value


def reps(n, prime):
    return [(p, n - p) for p in range(3, n // 2 + 1, 2)
            if p < n - p and prime[p] and prime[n - p]]


def shifted_classes(first, second):
    keys = ("shared_low_low", "shared_low_high", "shared_high_low",
            "shared_high_high", "four_distinct")
    counts = dict.fromkeys(keys, 0)
    for p, q in first:
        for r, s in second:
            matches = (p == r, p == s, q == r, q == s)
            if sum(matches) > 1:
                raise AssertionError("two shared positions force identical targets")
            if any(matches):
                counts[keys[matches.index(True)]] += 1
            else:
                counts["four_distinct"] += 1
    return counts


def text(value):
    return f"{value.numerator}/{value.denominator}"


def residual(n, prime):
    return n >= 4 and n % 2 == 0 and not prime[n - 1] and not prime[n // 2]


def candidate_budget(n):
    return max(0, (n - 4) // 4)


def main():
    prime = sieve(max(CENTERS) + 2)
    rows = []
    for center in CENTERS:
        targets = (center - 2, center, center + 2)
        pair_sets = [reps(n, prime) for n in targets]
        counts = [len(pairs) for pairs in pair_sets]
        wheels = [wheel_a(n) for n in targets]
        x = [Fraction(r, a) for r, a in zip(counts, wheels)]
        a, b, c = x
        mean = (a + b + c) / 3
        energy = (a - b) ** 2 + (b - c) ** 2
        d_direct = mean * mean - Fraction(2, 9) * energy
        d_expanded = (-a*a - 3*b*b - c*c + 6*a*b + 2*a*c + 6*b*c) / 9
        assert d_direct == d_expanded

        left = shifted_classes(pair_sets[0], pair_sets[1])
        outer = shifted_classes(pair_sets[0], pair_sets[2])
        right = shifted_classes(pair_sets[1], pair_sets[2])
        for parts, i, j in ((left, 0, 1), (outer, 0, 2), (right, 1, 2)):
            assert sum(parts.values()) == counts[i] * counts[j]
            assert parts["shared_low_high"] == 0

        # Every signed contribution to 9 D, split into same-target diagonals,
        # same-target four-distinct terms, shared-prime contractions, and Q4.
        signed = {}
        same_coefficients = (-1, -3, -1)
        for i, label in enumerate(("minus", "center", "plus")):
            r = counts[i]
            den = wheels[i] ** 2
            signed[f"same_{label}_diagonal"] = Fraction(same_coefficients[i] * r, den)
            signed[f"same_{label}_four_distinct"] = Fraction(
                same_coefficients[i] * r * (r - 1), den)
        for label, parts, i, j, coeff in (
            ("minus_center", left, 0, 1, 6),
            ("minus_plus", outer, 0, 2, 2),
            ("center_plus", right, 1, 2, 6),
        ):
            shared = sum(parts[k] for k in (
                "shared_low_low", "shared_low_high", "shared_high_low", "shared_high_high"))
            signed[f"cross_{label}_shared"] = Fraction(coeff * shared, wheels[i] * wheels[j])
            signed[f"cross_{label}_Q4"] = Fraction(
                coeff * parts["four_distinct"], wheels[i] * wheels[j])
        assert sum(signed.values(), Fraction()) == 9 * d_direct

        rows.append({
            "center": center,
            "is_in_H": residual(center, prime),
            "targets": list(targets),
            "R": counts,
            "A_210": wheels,
            "B_candidate_upper_bounds": [candidate_budget(n) for n in targets],
            "X": [text(v) for v in x],
            "mean": text(mean),
            "path_energy": text(energy),
            "D_direct": text(d_direct),
            "D_expanded": text(d_expanded),
            "same_target_ordered_squares": [
                {"diagonal": r, "four_distinct": r * (r - 1), "total": r * r}
                for r in counts
            ],
            "shifted_position_classes": {
                "minus_center": left, "minus_plus": outer, "center_plus": right
            },
            "signed_contributions_to_9D": {k: text(v) for k, v in signed.items()},
            "signed_contributions_sum_to_9D": text(sum(signed.values(), Fraction())),
        })

    # The abstract count model is only a logical countermodel to deductions
    # from wheel normalization and candidate upper bounds; it is not asserted
    # to be realized by primes.
    n = 100
    targets = (n - 2, n, n + 2)
    abstract_r = (1, 0, 1)
    abstract_a = tuple(wheel_a(t) for t in targets)
    abstract_b = tuple(candidate_budget(t) for t in targets)
    abstract_x = tuple(Fraction(r, q) for r, q in zip(abstract_r, abstract_a))
    abstract_d = (sum(abstract_x, Fraction()) / 3) ** 2 - Fraction(2, 9) * (
        (abstract_x[1] - abstract_x[0]) ** 2 + (abstract_x[2] - abstract_x[1]) ** 2)
    assert not prime[n - 1] and not prime[n // 2]
    assert all(r <= cap for r, cap in zip(abstract_r, abstract_b))
    assert abstract_d == -(abstract_x[0] - abstract_x[2]) ** 2 / 9 <= 0

    # Exact finite grid check of the signed-error bound in the conditional lemma.
    # For x_i=lambda(1+eps_i), |eps_i|<=1/3, D/lambda^2 >= 8/81.
    eps_grid = (Fraction(-1, 3), Fraction(0), Fraction(1, 3))
    grid_cases = 0
    grid_minimum = None
    for e0 in eps_grid:
        for e1 in eps_grid:
            for e2 in eps_grid:
                u, v, w = (1 + e0, 1 + e1, 1 + e2)
                d = (-u*u - 3*v*v - w*w + 6*u*v + 2*u*w + 6*v*w) / 9
                assert d >= Fraction(8, 81)
                grid_minimum = d if grid_minimum is None else min(grid_minimum, d)
                grid_cases += 1

    result = {
        "title": "Stage 61 focused signed true-prime correlation audit",
        "evidence_status": "Exact finite computation and algebraic checks; no universal prime-pair claim.",
        "method": "Python standard library; sieve for the producer, independent trial division in verifier.",
        "parameters": {"centers": list(CENTERS), "target_triples": len(CENTERS),
                       "largest_target": max(CENTERS) + 2,
                       "wheel_modulus": 210,
                       "abstract_countermodel_center": n,
                       "conditional_error_grid_cases": grid_cases},
        "definitions": {
            "H": "even N >= 4 with N-1 and N/2 composite",
            "R": "unordered distinct genuine-prime pairs p<q with p+q=N",
            "A_210": "exact modulo-210 admissible residue count",
            "X": "R/A_210",
            "D": "((X[N-2]+X[N]+X[N+2])/3)^2 - (2/9)*((X[N]-X[N-2])^2+(X[N+2]-X[N])^2)"},
        "abstract_upper_bound_countermodel": {
            "status": "logical countermodel only; not a prime-realizability claim",
            "center": n, "targets": list(targets), "is_in_H": True,
            "R_abstract": list(abstract_r), "A_210": list(abstract_a),
            "candidate_upper_bounds": list(abstract_b),
            "X_abstract": [text(v) for v in abstract_x],
            "D": text(abstract_d), "D_nonpositive": abstract_d <= 0},
        "conditional_relative_error_check": {
            "assumption": "X[N+j]=lambda*(1+epsilon_j), lambda>0, |epsilon_j|<=1/3, j in {-2,0,2}",
            "proved_lower_bound_for_D_over_lambda_squared": "8/81",
            "exact_grid_cases": grid_cases,
            "grid_minimum": text(grid_minimum),
            "effective_threshold_if_error_is_C_over_log_N": "N >= max(N0, ceil(exp(3*C)))"},
        "rows": rows,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"centers": list(CENTERS), "rows": len(rows),
                      "residual_centers": sum(row["is_in_H"] for row in rows),
                      "abstract_D": text(abstract_d),
                      "conditional_grid_cases": grid_cases,
                      "conditional_grid_minimum": text(grid_minimum),
                      "output": str(OUT)}, indent=2))


if __name__ == "__main__":
    main()
