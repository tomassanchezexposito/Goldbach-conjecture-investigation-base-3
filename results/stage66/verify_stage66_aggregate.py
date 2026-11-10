#!/usr/bin/env python3
"""Exact Python checks for Stage 66 aggregate modulus and prime partitions.

Uses only the standard library and Fraction. This is an independent finite
regression, not an asymptotic prime-correlation estimate.
"""
from fractions import Fraction as Q
from itertools import product
from math import isqrt
from pathlib import Path
import json


def prime_flags(limit):
    flags = [True] * (limit + 1)
    if limit >= 0:
        flags[0] = False
    if limit >= 1:
        flags[1] = False
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            flags[p*p:limit+1:p] = [False] * (((limit-p*p)//p)+1)
    return flags


def rep_pairs(n, flags):
    return [(p, n-p) for p in range(2, n//2+1)
            if n-p < len(flags) and flags[p] and flags[n-p] and p < n-p]


def aggregate_bound_holds(A, V, m, actual_increment_energy):
    """Compare exactly with m*(A-sqrt(V/m))_+^2, without floats."""
    W = V / m
    if W >= A*A:
        return actual_increment_energy >= 0
    # Need e >= (A-sqrt(W))^2, where e is the mean increment energy.
    e = actual_increment_energy / m
    c = e - A*A - W
    return c >= 0 or c*c <= 4*A*A*W


def main():
    # Exhaustively test Jensen's sharp aggregate bound over a rational grid.
    aggregate_cases = 0
    extremizers = 0
    grid = [Q(k, 4) for k in range(9)]
    for m in range(1, 5):
        for A in (Q(1), Q(3, 2), Q(3)):
            for deltas in product(grid, repeat=m):
                V = sum((d*d for d in deltas), Q(0))
                actual = A*A + sum((max(A-d, Q(0))**2 for d in deltas), Q(0))
                assert aggregate_bound_holds(A, V, m, actual-A*A), (A, deltas, V, actual)
                aggregate_cases += 1
        # Verify the stated extremizer attains the bound at representative V.
        for A in (Q(1), Q(3, 2), Q(3)):
            for s in (Q(0), Q(1, 3), Q(1), Q(2)):
                V = m*s*s
                s = min(A, s)
                energy = A*A + m*(A-s)**2
                bound = A*A + m*max(A-s, Q(0))**2
                assert energy == bound
                extremizers += 1

    # Independent sieve and pair-list partition of all target products.
    flags = prime_flags(160)
    targets = list(range(4, 122, 2))
    reps = {n: rep_pairs(n, flags) for n in targets}
    cross_cases = 0
    shared_total = four_distinct_total = 0
    for u in targets:
        for v in targets:
            if u == v:
                R = len(reps[u])
                assert R*R == R + R*(R-1)
                assert all(not (set(P) & set(Qpair))
                           for i, P in enumerate(reps[u])
                           for Qpair in reps[u][i+1:])
                continue
            shared = sum(len(set(P) & set(Qpair)) == 1
                         for P in reps[u] for Qpair in reps[v])
            four_distinct = sum(len(set(P) & set(Qpair)) == 0
                                for P in reps[u] for Qpair in reps[v])
            common_formula = sum(
                1 for x in range(2, min(u, v)+1)
                if flags[x] and x != u//2 and x != v//2
                and u-x >= 2 and v-x >= 2
                and flags[u-x] and flags[v-x]
            )
            assert shared == common_formula
            assert shared + four_distinct == len(reps[u])*len(reps[v])
            shared_total += shared
            four_distinct_total += four_distinct
            cross_cases += 1

    data = {
        "classification": "EXACT FINITE PYTHON VERIFICATION ONLY",
        "aggregate_grid_cases": aggregate_cases,
        "aggregate_extremizers_checked": extremizers,
        "prime_method": "Eratosthenes sieve and unordered representation-set intersections",
        "target_range_even": [4, 120],
        "ordered_cross_target_cases": cross_cases,
        "shared_position_configurations": shared_total,
        "four_distinct_configurations": four_distinct_total,
        "all_assertions_passed": True,
        "limitations": [
            "Finite identities and examples only.",
            "No pointwise asymptotic prime estimate or Goldbach coverage is proved."
        ]
    }
    out = Path(__file__).with_name("stage66_aggregate_python_results.json")
    out.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: exact aggregate Jensen tests:", aggregate_cases, "rational vectors")
    print("PASS: prime-pair products:", cross_cases, "ordered distinct-target cases")
    print("RESULT:", out)


if __name__ == "__main__":
    main()
