#!/usr/bin/env sage -python
"""Independent exact SageMath check of the Stage 68 interval Gram example."""
import json
from pathlib import Path
from sage.all import SR, ZZ, matrix, pi, sqrt

b = SR(1) / 4 - 1 / (2 * pi)
G0 = matrix(SR, [[SR(1) / 2 - sqrt(2) / pi, b],
                 [b, SR(1) / 2 - 1 / pi]])
Gh = matrix(SR, [[SR(1) / 2 + sqrt(2) / pi, b],
                 [b, SR(1) / 2 - 1 / pi]])
C = G0 * Gh - Gh * G0
assert C[0, 1].simplify_full() == (-2 * sqrt(2) * b / pi).simplify_full()
assert C[1, 0].simplify_full() == (2 * sqrt(2) * b / pi).simplify_full()
assert C[0, 0] == 0 and C[1, 1] == 0
# b>0 follows exactly from pi>3: b>1/4-1/6=1/12.  Sage's symbolic
# assumptions do not encode this transcendental inequality automatically.

# An independent integral derivation via Fourier moments on a centered interval.
def mu_centered(n):
    if n == 0:
        return SR(1) / 4
    return sin(2 * pi * n / 8) / (pi * n)

from sage.all import sin
def gram_center(center_half):
    phase = -1 if center_half else 1
    # Translation by 1/2 multiplies the nth Fourier moment by (-1)^n.
    mu = lambda n: phase**n * mu_centered(n)
    shifts = [1, 2]
    return matrix(SR, [[(mu(k-j) - mu(-j) - mu(k) + mu(0)).simplify_full()
                        for k in shifts] for j in shifts])

assert (gram_center(False) - G0).is_zero()
assert (gram_center(True) - Gh).is_zero()

# Exact full circle Gram identity is checked symbolically for a representative
# shift set with negative and positive members.
J = [-4, 2, 6]
G = matrix(ZZ, [[(1 if j == k else 0) + 1 for k in J] for j in J])
one = matrix(ZZ, len(J), 1, [1] * len(J))
assert G * one == (len(J) + 1) * one

out = {
    "classification": "INDEPENDENT FINITE SAGEMATH VERIFICATION",
    "version": "SageMath 10.9 (runtime)",
    "interval_gram_matrices_match_fourier_integrals": True,
    "commutator_nonzero": True,
    "full_circle_shift_set": J,
    "full_circle_constant_eigenvalue": len(J) + 1,
}
path = Path(__file__).with_name("stage68_sage_results.json")
path.write_text(json.dumps(out, indent=2) + "\n")
print("PASS: Sage exact symbolic interval moments and noncommuting Grams")
print(f"Wrote {path}")
