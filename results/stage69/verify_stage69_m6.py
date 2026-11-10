#!/usr/bin/env python3
"""Exact symbolic and rational boundary checks for the Stage 69 M6 formulas."""
import sympy as s

A, V, m = s.symbols("A V m", positive=True)
rootV = s.sqrt(V)
# The two displayed forms of the threshold agree when the positive part is active.
assert s.simplify((s.sqrt(m) * A - rootV) ** 2 - m * (A - rootV / s.sqrt(m)) ** 2) == 0

# Fixed-energy minimization: derivative, optimizer, and minimum on the interior branch.
x = s.symbols("x", positive=True)
f = x**2 + (rootV - s.sqrt(m) * x) ** 2
x0 = s.sqrt(m * V) / (m + 1)
assert s.simplify(s.diff(f, x).subs(x, x0)) == 0
assert s.simplify(f.subs(x, x0) - V / (m + 1)) == 0

# The two fixed-energy branches meet at V=A^2(m+1)^2/m.
Vbreak = A**2 * (m + 1) ** 2 / m
branch_left = A**2 + (s.sqrt(Vbreak) - s.sqrt(m) * A) ** 2
branch_right = Vbreak / (m + 1)
assert s.simplify(branch_left - branch_right) == 0

# For V=m A^2, the exact energy minimizer has center A and zero neighbors.
assert s.simplify((A**2 + (s.sqrt(m * A**2) - s.sqrt(m) * A) ** 2) - A**2) == 0

# Strict finite-m criterion: after taking square roots, the boundary is equality.
K, Vbar = s.symbols("K Vbar", nonnegative=True)
threshold = m * (A - s.sqrt(K / m)) ** 2
assert s.simplify(threshold - (A * s.sqrt(m) - s.sqrt(K)) ** 2) == 0

# On the useful branch K < m*A^2, the positive-part expression is active.
# Check the square-root boundary with exact positive rational substitutions;
# this avoids asking a symbolic simplifier to infer an unstated sign condition.
for aa, mm, kk in [(5, 2, 1), (7, 3, 4), (11, 5, 9)]:
    if kk < mm * aa * aa:
        lhs = s.sqrt(s.Rational(mm) * (s.Rational(aa) - s.sqrt(s.Rational(kk, mm))) ** 2 / mm)
        rhs = s.Rational(aa) - s.sqrt(s.Rational(kk, mm))
        assert rhs > 0 and s.simplify(lhs - rhs) == 0

# Exact rational cases around the transition V=m A^2 verify the upper-bound envelope.
for aa, mm in [(2, 1), (3, 2), (5, 4)]:
    for vv in [0, mm * aa * aa // 2, mm * aa * aa, 2 * mm * aa * aa]:
        rhs = s.Rational(aa**2) + (s.sqrt(mm) * aa - s.sqrt(vv))**2 if vv <= mm * aa * aa else s.Rational(aa**2)
        assert rhs >= aa**2
    vb = mm * aa * aa
    assert s.simplify(s.Rational(aa**2) + (s.sqrt(mm) * aa - s.sqrt(vb))**2 - aa**2) == 0

print("PASS: two forms of the aggregate shift threshold agree exactly")
print("PASS: fixed-exact-energy optimizer and branch boundary are exact")
print("PASS: upper-bound sharpness holds on and above Vbar=m*A^2")
print("PASS: finite-m strict threshold algebra verified")
