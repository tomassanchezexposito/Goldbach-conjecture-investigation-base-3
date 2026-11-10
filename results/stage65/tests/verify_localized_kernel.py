#!/usr/bin/env python3
"""Exact integer/rational checks for Stage 65 finite localization formulas.

This checks finite coefficient identities and normalized Dirichlet/Fejer
weights. It is an implementation audit, not an estimate for prime sums.
"""
from fractions import Fraction
import json
from pathlib import Path


def fejer_weights(H):
    return {h: Fraction(H + 1 - abs(h), H + 1) for h in range(-H, H + 1)}


def main():
    kernels = []
    for H in range(0, 17):
        d = {h: Fraction(1, 2 * H + 1) for h in range(-H, H + 1)}
        f = {h: v / (H + 1) for h, v in fejer_weights(H).items()}
        d_l2 = sum((v * v for v in d.values()), Fraction(0))
        f_l2 = sum((v * v for v in f.values()), Fraction(0))
        f_l2_formula = Fraction(2 * H * H + 4 * H + 3, 3 * (H + 1) ** 3)
        f_weight_sum = sum(f.values(), Fraction(0))
        f_first_moment = sum((abs(h) * v for h, v in f.items()), Fraction(0))
        f_first_moment_formula = Fraction(H * (H + 2), 3 * (H + 1))
        assert d_l2 == Fraction(1, 2 * H + 1)
        assert f_l2 == f_l2_formula
        assert f_weight_sum == 1
        assert f_first_moment == f_first_moment_formula
        kernels.append({
            "H": H,
            "normalized_dirichlet_l2_squared": str(d_l2),
            "normalized_fejer_l2_squared": str(f_l2),
            "normalized_fejer_weight_sum": str(f_weight_sum),
            "normalized_fejer_first_absolute_moment": str(f_first_moment),
        })

    # Verify sum_h lambda_h c_(N+h) as an exact finite coefficient sum.
    coeffs = {n: 3*n*n - 7*n + 11 for n in range(-12, 13)}
    lam = {-3: Fraction(1, 5), -1: Fraction(-2, 7), 0: Fraction(4, 3),
           2: Fraction(5, 11), 4: Fraction(-3, 8)}
    N = 2
    lhs = sum((lam[h] * coeffs[N+h] for h in lam), Fraction(0))
    # Directly collect the coefficient of frequency N in c(alpha)K_lambda(alpha).
    rhs = sum((coeffs[n] * lam[n-N] for n in coeffs if n-N in lam), Fraction(0))
    assert lhs == rhs

    # A singleton of size A obeys any much larger global l2 budget, while a
    # normalized average sees only its small central weight.
    A = 1000
    H = 20
    spike_dirichlet_average = Fraction(-A, 2*H + 1)
    spike_fejer_average = Fraction(-A, H + 1)
    assert abs(spike_dirichlet_average) < A and abs(spike_fejer_average) < A
    global_energy = A * A
    declared_budget = 10**9
    assert global_energy <= declared_budget

    result = {
        "classification": "EXACT FINITE RATIONAL CHECKS; NO PRIME-ARITHMETIC CLAIM",
        "H_range": [0, 16],
        "kernel_rows": kernels,
        "shift_identity": {
            "target_N": N,
            "lambda": {str(k): str(v) for k, v in lam.items()},
            "left_direct_sum": str(lhs),
            "right_product_coefficient": str(rhs),
        },
        "isolated_spike_countermodel": {
            "spike_amplitude": A,
            "central_coefficient": -A,
            "all_noncentral_coefficients": 0,
            "global_l2_squared": global_energy,
            "permitted_budget": declared_budget,
            "H": H,
            "normalized_dirichlet_average": str(spike_dirichlet_average),
            "normalized_fejer_average": str(spike_fejer_average),
        },
        "assertions_passed": True,
        "limits": [
            "Finite rational identities audit the formulas only.",
            "The spike is an abstract coefficient sequence, not a prime example.",
        ],
    }
    out = Path(__file__).with_name("localized_kernel_exact_results.json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: normalized Dirichlet and Fejer coefficient-weight sums/norms for H=0..16")
    print("PASS: exact signed shift identity; isolated-spike dilution countermodel")
    print("Recorded", out)


if __name__ == "__main__":
    main()
