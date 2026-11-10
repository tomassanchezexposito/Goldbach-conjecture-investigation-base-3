#!/usr/bin/env python3
"""Exact rational checks for Stage 63 M3 energy and correlation claims."""
from fractions import Fraction as F
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name("03_exact_checks.json")


def path_energy(x):
    return sum((x[i + 1] - x[i]) ** 2 for i in range(len(x) - 1))


def d_certificate(x):
    a, b, c = x
    return (-a*a - 3*b*b - c*c + 6*a*b + 2*a*c + 6*b*c) / 9


def quadratic_coefficients(y):
    a, b, c = y
    return -a*a - 3*b*b - c*c + 6*a*b + 2*a*c + 6*b*c


def main():
    grid = [F(k, 3) for k in range(-6, 7)]
    checked = 0
    zero_center = 0
    for a, b, c in itertools.product(grid, repeat=3):
        direct = ((a + b + c) / 3) ** 2 - F(2, 9) * path_energy((a, b, c))
        assert direct == d_certificate((a, b, c))
        assert 9 * direct == quadratic_coefficients((a, b, c))
        checked += 1
        if b == 0:
            assert 9 * direct == -(a - c) ** 2 <= 0
            zero_center += 1

    # Exact sharp center-versus-energy inequality for the three-vertex path,
    # equal arithmetic weights: tau=(e_1-1/3*1)^T L^+ (e_1-1/3*1)=2/9.
    tau = F(2, 9)
    for a, c in itertools.product(grid, repeat=2):
        mu = (a + c) / 3  # center value is zero
        energy = a*a + c*c
        assert mu * mu <= tau * energy
    # Equality witness (1,0,1): mu^2=tau*E=4/9.
    assert F(4, 9) == tau * F(2)

    # Abstract correlation countermodels. At center zero, off-center
    # four-distinct correlation can be positive while the signed certificate
    # is non-positive (the exact value is invariant under any positive scales
    # once rewritten in X=R/A coordinates).
    abstract = []
    for left, right in ((1, 1), (1, 2), (2, 5)):
        center = 0
        x = (F(left), F(center), F(right))
        d = d_certificate(x)
        off_center_product = F(left * right)
        assert d == -F(left - right) ** 2 / 9
        assert off_center_product > 0 and d <= 0
        abstract.append({"R_minus": left, "R_center": 0,
                         "R_plus": right,
                         "off_center_product_Rminus_Rplus": str(off_center_product),
                         "9D": str(9 * d), "D": str(d)})

    # Recheck Stage 61's saved finite signed certificates without trusting its
    # displayed D column: reconstruct from integer counts and A_210 values.
    source = json.loads((ROOT / "results/stage61/stage61_exact_results.json")
                        .read_text(encoding="utf-8"))
    rows_checked = 0
    for row in source["rows"]:
        R = row["R"]
        A = row["A_210"]
        x = tuple(F(r, a) for r, a in zip(R, A))
        direct = d_certificate(x)
        assert str(direct) == row["D_direct"]
        assert str(direct) == row["D_expanded"]
        rows_checked += 1

    data = {
        "evidence": "exact rational identities and finite countermodels",
        "rational_grid_denominator": 3,
        "quadratic_vectors_checked": checked,
        "zero_center_vectors_checked": zero_center,
        "three_path_pseudoinverse_constant": str(tau),
        "zero_center_energy_cases_checked": len(grid) ** 2,
        "stage61_saved_rows_independently_reconstructed": rows_checked,
        "abstract_off_center_correlation_countermodels": abstract,
        "assertions_passed": True,
        "universal_prime_claim": False
    }
    OUT.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
