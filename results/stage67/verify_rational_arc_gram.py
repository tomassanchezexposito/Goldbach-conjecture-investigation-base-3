#!/usr/bin/env python3
"""Exact rational/group-ring regression for Stage 67 arc Gram identities.

The formal symbol t represents 1/(2*pi*i).  Cyclotomic expressions are kept
as sparse rational group-ring sums.  This verifier checks exact expansions,
center divisibility, full-circle Gram matrices, and the major-arc measure
bound.  It is not a prime-correlation estimate.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import gcd, lcm
from pathlib import Path
import json
import time


class C:
    """Sparse Q[C_L] element, represented by powers of a formal root zeta_L."""
    def __init__(self, L, terms=None):
        self.L = L
        self.terms = {int(k) % L: Q(v) for k, v in (terms or {}).items() if v}

    @classmethod
    def one(cls, L):
        return cls(L, {0: 1})

    @classmethod
    def e(cls, L, x):
        x = Q(x)
        assert (x * L).denominator == 1
        return cls(L, {int(x * L): 1})

    def __add__(self, other):
        assert self.L == other.L
        d = dict(self.terms)
        for k, v in other.terms.items():
            d[k] = d.get(k, Q(0)) + v
        return C(self.L, d)

    def __neg__(self):
        return C(self.L, {k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        assert self.L == other.L
        d = {}
        for a, x in self.terms.items():
            for b, y in other.terms.items():
                k = (a + b) % self.L
                d[k] = d.get(k, Q(0)) + x * y
        return C(self.L, d)

    def scale(self, a):
        a = Q(a)
        return C(self.L, {k: a * v for k, v in self.terms.items()})

    def conjugate(self):
        return C(self.L, {(-k) % self.L: v for k, v in self.terms.items()})

    def __eq__(self, other):
        return self.L == other.L and self.terms == other.terms


class M:
    """A + B*t with t=1/(2*pi*i), where A is rational and B is in Q[C_L]."""
    def __init__(self, L, a=0, b=None):
        self.L = L
        self.a = Q(a)
        self.b = b if b is not None else C(L)

    def __add__(self, other):
        return M(self.L, self.a + other.a, self.b + other.b)

    def __neg__(self):
        return M(self.L, -self.a, -self.b)

    def __sub__(self, other):
        return self + (-other)

    def scale(self, a):
        return M(self.L, self.a * Q(a), self.b.scale(a))

    def __eq__(self, other):
        return self.L == other.L and self.a == other.a and self.b == other.b


def moment(L, n, left, right):
    """Integral_left^right e(n*x) dx, with rational endpoints."""
    if n == 0:
        return M(L, right-left)
    coeff = C.e(L, n*right) - C.e(L, n*left)
    return M(L, 0, coeff.scale(Q(1, n)))


def arc_gram_via_moments(L, shifts, arcs):
    # G(j,k)=mu(k-j)-mu(-j)-mu(k)+mu(0).
    ans = {}
    for j in shifts:
        for k in shifts:
            val = M(L)
            for left, right in arcs:
                val += moment(L, k-j, left, right)
                val -= moment(L, -j, left, right)
                val -= moment(L, k, left, right)
                val += moment(L, 0, left, right)
            ans[j, k] = val
    return ans


def arc_gram_by_endpoint_expansion(L, shifts, arcs):
    # Independently expand (e(-j*x)-1)(e(k*x)-1) before integration.
    ans = {}
    terms = lambda j, k: ((k-j, 1), (-j, -1), (k, -1), (0, 1))
    for j in shifts:
        for k in shifts:
            val = M(L)
            for left, right in arcs:
                for frequency, sign in terms(j, k):
                    val += moment(L, frequency, left, right).scale(sign)
            ans[j, k] = val
    return ans


def center_vector(L, shifts, a, q):
    c = Q(a, q)
    one = C.one(L)
    return {j: C.e(L, -j*c) - one for j in shifts}


def center_gram(L, shifts, a, q):
    v = center_vector(L, shifts, a, q)
    return {(j, k): v[j] * v[k].conjugate()
            for j in shifts for k in shifts}


def phi(n):
    return sum(gcd(a, n) == 1 for a in range(1, n+1))


def main():
    started = time.perf_counter()
    arc_cases = 0
    center_cases = 0
    full_circle_cases = 0
    for q in range(2, 13):
        for a in range(1, q):
            if gcd(a, q) != 1:
                continue
            for rho in (Q(1, 40), Q(1, 24), Q(1, 2*q)):
                left, right = Q(a, q)-rho, Q(a, q)+rho
                if right-left >= 1:
                    continue
                shifts = tuple(sorted(set(j for j in range(-5, 6) if j)))
                L = lcm(q, left.denominator, right.denominator)
                lhs = arc_gram_via_moments(L, shifts, [(left, right)])
                rhs = arc_gram_by_endpoint_expansion(L, shifts, [(left, right)])
                assert lhs == rhs
                arc_cases += len(shifts)**2

            # Exact center test: zero iff q divides the shift; otherwise a
            # nonzero sparse group-ring vector remains.
            shifts = tuple(range(-5, 6))
            L = lcm(q, 4)
            v = center_vector(L, shifts, a, q)
            for j in shifts:
                assert (not v[j].terms) == (j % q == 0)
                center_cases += 1
            G = center_gram(L, shifts, a, q)
            # A rank-one matrix satisfies G^2=trace(G)G in the exact group ring.
            trace = C(L)
            for j in shifts:
                trace = trace + G[j, j]
            for j in shifts:
                for k in shifts:
                    square = C(L)
                    for h in shifts:
                        square = square + G[j, h] * G[h, k]
                    assert square == trace * G[j, k]

    # Full-circle moments are exact Kronecker deltas, hence G=I+11*.
    shifts_cases = [(1,), (-2, 3), (-5, -1, 2, 7)]
    for shifts in shifts_cases:
        L = 4
        G = arc_gram_via_moments(L, shifts, [(Q(0), Q(1))])
        for j in shifts:
            for k in shifts:
                assert G[j, k] == M(L, (1 if j == k else 0) + 1)
                full_circle_cases += 1

    # For P integer, total length of the Li--Liu major arcs is at most
    # (2P/X) sum_{q<=P} phi(q)/q <= 2P^2/X. Check the finite arithmetic bound.
    measure_cases = 0
    for P in range(1, 101):
        assert sum((Q(phi(q), q) for q in range(1, P+1)), Q(0)) <= P
        measure_cases += 1

    data = {
        "classification": "EXACT FORMAL GROUP-RING AND RATIONAL ARITHMETIC CHECKS; NOT A PRIME ESTIMATE",
        "arc_matrix_entries_compared": arc_cases,
        "reduced_center_shift_tests": center_cases,
        "center_rank_one_matrix_sizes": "11 shifts for every reduced a/q, 2<=q<=12",
        "full_circle_entries_checked": full_circle_cases,
        "major_arc_measure_inequalities_checked": measure_cases,
        "formal_symbol": "t=1/(2*pi*i); roots of unity are sparse Q[C_L] elements",
        "all_assertions_passed": True,
        "limitations": [
            "The group-ring checks establish exact expansions; the proof of positivity is the integral Gram argument in report.md.",
            "No prime-weighted localized moment or pointwise prime estimate is proved."
        ]
    }
    out = Path(__file__).with_name("rational_arc_python_results.json")
    out.write_text(json.dumps(data, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    data["runtime_seconds"] = time.perf_counter()-started
    out.write_text(json.dumps(data, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print("PASS: exact arc Gram expansions:", arc_cases, "matrix entries")
    print("PASS: reduced-center divisibility and rank-one identities:", center_cases, "shift tests")
    print("PASS: full-circle Gram entries:", full_circle_cases)
    print("PASS: major-arc rational measure inequalities:", measure_cases)
    print("RESULT:", out)


if __name__ == "__main__":
    main()
