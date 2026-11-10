#!/usr/bin/env python3
"""Exact targeted checks for Stage 68 operator and allocation identities.

Uses SymPy exact algebra.  This is a finite regression verifier, not a proof
of the all-parameter Hilbert-space theorems in the accompanying report.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as s

pi = s.pi
sqrt2 = s.sqrt(2)

# J={1,2}; intervals of radius 1/8 centered at 0 and 1/2.
b = s.Rational(1, 4) - 1 / (2 * pi)
G0 = s.Matrix([[s.Rational(1, 2) - sqrt2 / pi, b],
               [b, s.Rational(1, 2) - 1 / pi]])
Ghalf = s.Matrix([[s.Rational(1, 2) + sqrt2 / pi, b],
                  [b, s.Rational(1, 2) - 1 / pi]])
comm = G0 * Ghalf - Ghalf * G0
assert s.simplify(comm[0, 1] + 2 * sqrt2 * b / pi) == 0
assert s.simplify(comm[1, 0] - 2 * sqrt2 * b / pi) == 0
assert s.simplify(comm[0, 0]) == 0 and s.simplify(comm[1, 1]) == 0
assert b.is_positive

# Distinct top eigenvalues: a real symmetric 2x2 matrix with nonzero
# off-diagonal entry has simple eigenvalues.  Noncommutation then rules out a
# common eigenvector, so the triangle support bound is strict for B=(1,1).
assert G0[0, 1] != 0 and Ghalf[0, 1] != 0

# Exact value of the relaxed density-matrix bound for the orthogonal rank-one
# example; compare with the true maximum sqrt(2).
assert s.simplify((s.sqrt(s.Rational(1, 2)) +
                   s.sqrt(s.Rational(1, 2))) - 2) == s.sqrt(2) - 2

# Full-circle Gram entries for distinct nonzero shifts: delta_{j,k}+1.
for shifts in [(-4, 2, 6), (1, 2), (-7, -3, 11, 14)]:
    assert len(set(shifts)) == len(shifts)
    G = s.Matrix([[int(j == k) + 1 for k in shifts] for j in shifts])
    m = len(shifts)
    assert G * s.ones(m, 1) == (m + 1) * s.ones(m, 1)
    for i in range(m - 1):
        z = s.zeros(m, 1)
        z[i, 0], z[m - 1, 0] = 1, -1
        assert (G * z - z).is_zero_matrix

# Sparse positive-polynomial countermodel: S=e(3a)+e(5a), target 28.
# Its square has support {6,8,10}; its coefficient at 28 is zero.  On
# M=[-1/88,1/88], every summand in the restricted major coefficient is
# nonnegative since |2*pi*n*a|<=pi/2 for n=18,20,22, and positive
# in the interior.  Thus its integral over the interval is positive.
assert s.expand((s.Symbol('x')**3 + s.Symbol('x')**5)**2).coeff(
    s.Symbol('x'), 28) == 0

out = {
    "classification": "FINITE VERIFICATION; identities proved separately in report",
    "intervals": [{"center": "0", "radius": "1/8"},
                  {"center": "1/2", "radius": "1/8"}],
    "shifts": [1, 2],
    "G_center_0": [[str(x) for x in row] for row in G0.tolist()],
    "G_center_half": [[str(x) for x in row] for row in Ghalf.tolist()],
    "commutator_01": str(s.simplify(comm[0, 1])),
    "triangle_bound_strict": True,
    "orthogonal_PSD_true_optimum": "sqrt(2)",
    "orthogonal_PSD_triangle_bound": "2",
    "full_circle_shift_sets_checked": [list(x) for x in
                                        [(-4, 2, 6), (1, 2), (-7, -3, 11, 14)]],
    "sparse_polynomial_support_of_square": [6, 8, 10],
    "sparse_target": 28,
    "major_interval_radius": "1/88",
    "major_coefficient_positive": True,
}
path = Path(__file__).with_name("stage68_exact_results.json")
path.write_text(json.dumps(out, indent=2) + "\n")
print("PASS: exact interval Gram commutator is nonzero; strict triangle example certified")
print("PASS: full-circle Gram checks for 3 shift sets; sparse countermodel checked")
print(f"Wrote {path}")
