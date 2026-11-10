#!/usr/bin/env python3
"""Independent exact verifier for the focused Stage 61 output.

Uses trial division and direct enumeration modulo 210.  It does not import
compute_stage61.py or trust the producer's prime and wheel routines.
"""

from fractions import Fraction
from math import gcd, isqrt
import json
from pathlib import Path


DATA = Path(__file__).with_name("stage61_exact_results.json")
VERIFICATION = Path(__file__).with_name("stage61_verification.json")


def prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def reps(target):
    out = []
    for p in range(3, target // 2 + 1, 2):
        q = target - p
        if p < q and prime(p) and prime(q):
            out.append((p, q))
    return out


def wheel(target):
    return sum(gcd(r, 210) == 1 and gcd(target - r, 210) == 1
               for r in range(210))


def residual(target):
    return (target >= 4 and target % 2 == 0
            and not prime(target - 1) and not prime(target // 2))


def candidate_budget(target):
    return max(0, (target - 4) // 4)


def classes(first, second):
    # A set-intersection implementation independent of the producer's boolean
    # position tuple: each shared prime value is assigned its two positions.
    names = ("shared_low_low", "shared_low_high", "shared_high_low",
             "shared_high_high", "four_distinct")
    out = dict.fromkeys(names, 0)
    for (p, q) in first:
        for (r, s) in second:
            shared_values = set((p, q)).intersection((r, s))
            assert len(shared_values) <= 1
            if not shared_values:
                out["four_distinct"] += 1
                continue
            z = next(iter(shared_values))
            first_position = 0 if z == p else 1
            second_position = 0 if z == r else 1
            out[names[2 * first_position + second_position]] += 1
    return out


def f(text):
    a, b = text.split("/")
    return Fraction(int(a), int(b))


def t(value):
    return f"{value.numerator}/{value.denominator}"


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    rows = data["rows"]
    assert [r["center"] for r in rows] == data["parameters"]["centers"]
    assert len(rows) == 8
    for row in rows:
        center = row["center"]
        targets = (center - 2, center, center + 2)
        assert list(targets) == row["targets"]
        ps = [reps(n) for n in targets]
        rs = [len(pairs) for pairs in ps]
        aa = [wheel(n) for n in targets]
        assert rs == row["R"]
        assert aa == row["A_210"]
        assert row["B_candidate_upper_bounds"] == [candidate_budget(n) for n in targets]
        assert all(r <= cap for r, cap in zip(rs, row["B_candidate_upper_bounds"]))
        assert row["is_in_H"] == residual(center)
        xx = [Fraction(r, a) for r, a in zip(rs, aa)]
        assert [t(z) for z in xx] == row["X"]

        mu = sum(xx, Fraction()) / 3
        energy = (xx[0] - xx[1]) ** 2 + (xx[1] - xx[2]) ** 2
        direct = mu**2 - Fraction(2, 9) * energy
        expanded = (-xx[0]**2 - 3*xx[1]**2 - xx[2]**2
                    + 6*xx[0]*xx[1] + 2*xx[0]*xx[2]
                    + 6*xx[1]*xx[2]) / 9
        assert t(mu) == row["mean"]
        assert t(energy) == row["path_energy"]
        assert t(direct) == row["D_direct"] == row["D_expanded"] == t(expanded)

        expected_same = [{"diagonal": r, "four_distinct": r*(r-1), "total": r*r}
                         for r in rs]
        assert expected_same == row["same_target_ordered_squares"]
        for key, i, j in (("minus_center", 0, 1), ("minus_plus", 0, 2),
                          ("center_plus", 1, 2)):
            part = classes(ps[i], ps[j])
            assert part == row["shifted_position_classes"][key]
            assert sum(part.values()) == rs[i] * rs[j]
            assert part["shared_low_high"] == 0

        signed = {}
        for i, name, coeff in ((0, "minus", -1), (1, "center", -3), (2, "plus", -1)):
            r = rs[i]
            signed[f"same_{name}_diagonal"] = Fraction(coeff*r, aa[i]**2)
            signed[f"same_{name}_four_distinct"] = Fraction(coeff*r*(r-1), aa[i]**2)
        for name, key, i, j, coeff in (
            ("minus_center", "minus_center", 0, 1, 6),
            ("minus_plus", "minus_plus", 0, 2, 2),
            ("center_plus", "center_plus", 1, 2, 6),
        ):
            part = row["shifted_position_classes"][key]
            contracted = sum(part[z] for z in (
                "shared_low_low", "shared_low_high", "shared_high_low", "shared_high_high"))
            signed[f"cross_{name}_shared"] = Fraction(coeff*contracted, aa[i]*aa[j])
            signed[f"cross_{name}_Q4"] = Fraction(coeff*part["four_distinct"], aa[i]*aa[j])
        assert {k: t(v) for k, v in signed.items()} == row["signed_contributions_to_9D"]
        assert sum(signed.values(), Fraction()) == 9*direct
        assert t(9*direct) == row["signed_contributions_sum_to_9D"]

    model = data["abstract_upper_bound_countermodel"]
    assert model["status"] == "logical countermodel only; not a prime-realizability claim"
    assert model["is_in_H"] and model["center"] == 100
    assert model["R_abstract"] == [1, 0, 1]
    assert all(r <= cap for r, cap in zip(model["R_abstract"], model["candidate_upper_bounds"]))
    xx = [Fraction(r, a) for r, a in zip(model["R_abstract"], model["A_210"])]
    model_d = (sum(xx, Fraction())/3)**2 - Fraction(2, 9)*(
        (xx[1]-xx[0])**2 + (xx[2]-xx[1])**2)
    assert t(model_d) == model["D"] and model_d <= 0
    assert model_d == -(xx[0]-xx[2])**2/9

    # The grid is checked by evaluating the path expression independently;
    # this verifies the claimed conservative lower bound, not just the output.
    grid = (Fraction(-1, 3), Fraction(0), Fraction(1, 3))
    values = []
    for e0 in grid:
        for e1 in grid:
            for e2 in grid:
                x = (1+e0, 1+e1, 1+e2)
                mu = sum(x, Fraction())/3
                energy = (x[0]-x[1])**2 + (x[1]-x[2])**2
                d = mu*mu - Fraction(2, 9)*energy
                assert d >= Fraction(8, 81)
                values.append(d)
    conditional = data["conditional_relative_error_check"]
    assert len(values) == conditional["exact_grid_cases"] == 27
    assert t(min(values)) == conditional["grid_minimum"]
    assert conditional["proved_lower_bound_for_D_over_lambda_squared"] == "8/81"

    result = {"independent_method": "trial division; direct modulo-210 enumeration; exact Fractions",
              "triples_verified": len(rows),
              "target_counts_verified": 3 * len(rows),
              "representation_count_incidences": sum(sum(r["R"]) for r in rows),
              "residual_centers": sum(r["is_in_H"] for r in rows),
              "signed_component_identities": len(rows),
              "abstract_zero_center_model_checked": True,
              "conditional_grid_cases": len(values),
              "all_assertions_passed": True}
    VERIFICATION.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
