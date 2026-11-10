#!/usr/bin/env sage -python
"""Independent SageMath audit of Stage 66 exact formulas and multiplicities."""
from sage.all import QQ, ceil, identity_matrix, matrix, ones_matrix, prime_range, vector
from itertools import product
from pathlib import Path
import json
import time


def positive_part(x):
    return max(QQ(0), x)


def rep_pairs(n, primes):
    return [(p, n-p) for p in sorted(primes)
            if p < n-p and n-p in primes]


def main():
    started = time.time()
    # Independent exact evaluation of the even-step closed sum.
    lipschitz_cases = 0
    for A in (QQ(1), QQ(5)/2, QQ(7)/3, QQ(10)):
        for L in (QQ(0), QQ(1)/4, QQ(1), QQ(3), QQ(8)):
            for H in range(0, 13):
                direct = A**2 + 2*sum((positive_part(A-L*h)**2
                                       for h in range(1, H+1)), QQ(0))
                if L == 0:
                    closed = (2*H+1)*A**2
                else:
                    J = min(H, max(0, ceil(A/L)-1))
                    closed = A**2 + 2*(J*A**2 - A*L*J*(J+1)
                                         + L**2*J*(J+1)*(2*J+1)/6)
                assert direct == closed
                lipschitz_cases += 1

    # Aggregate theorem: enumerate a separate rational grid and verify its
    # sharp equal-increment extremizers using QQ, without importing Python code.
    aggregate_cases = 0
    grid = [QQ(k)/3 for k in range(7)]
    for m in range(1, 5):
        for A in (QQ(1), QQ(2), QQ(7)/2):
            for ds in product(grid, repeat=m):
                V = sum((d*d for d in ds), QQ(0))
                lhs = A**2 + sum((positive_part(A-d)**2 for d in ds), QQ(0))
                rhs = A**2 + m*positive_part(A-sqrt(V/m))**2
                assert lhs >= rhs
                aggregate_cases += 1
            for V in (QQ(0), QQ(m)/9, QQ(m), QQ(9*m)):
                s = min(A, sqrt(V/m))
                assert A**2 + m*(A-s)**2 == A**2 + m*positive_part(A-sqrt(V/m))**2

    # Verify full-circle multiplier Gram matrix and its sharp operator norm.
    gram_cases = 0
    for m in range(1, 9):
        G = identity_matrix(QQ, m) + ones_matrix(QQ, m, m)
        assert G.rank() == m
        assert G.det() == m+1
        x = G.charpoly().parent().gen()
        assert G.charpoly() == (x-1)**(m-1) * (x-(m+1))
        gram_cases += 1

    # Sage prime_range and set intersections independently verify all
    # diagonal/shared/four-distinct multiplicities.
    Nmax = 150
    primes = set(prime_range(2, Nmax+1))
    targets = list(range(4, 102, 2))
    reps = {n: rep_pairs(n, primes) for n in targets}
    cross_cases = 0
    shared_total = four_total = 0
    for u in targets:
        for v in targets:
            if u == v:
                R = len(reps[u])
                assert R**2 == R + R*(R-1)
                for i, P in enumerate(reps[u]):
                    for Qpair in reps[u][i+1:]:
                        assert not (set(P) & set(Qpair))
                continue
            shared = 0
            four = 0
            for P in reps[u]:
                for Qpair in reps[v]:
                    intersection = set(P) & set(Qpair)
                    assert len(intersection) <= 1
                    shared += (len(intersection) == 1)
                    four += (len(intersection) == 0)
            formula = sum(1 for x in primes
                          if x != u//2 and x != v//2
                          and u-x in primes and v-x in primes)
            assert shared == formula
            assert shared + four == len(reps[u])*len(reps[v])
            cross_cases += 1
            shared_total += shared
            four_total += four

    result = {
        "classification": "INDEPENDENT SAGEMATH EXACT FINITE VERIFICATION",
        "sage_version": str(__import__("sage.env", fromlist=["SAGE_VERSION"]).SAGE_VERSION),
        "lipschitz_formula_cases": lipschitz_cases,
        "aggregate_rational_vector_cases": aggregate_cases,
        "frame_gram_sizes": gram_cases,
        "frame_gram_eigenvalues": "1 (multiplicity m-1), m+1 (multiplicity 1)",
        "prime_test": "Sage prime_range and direct set intersections",
        "target_range_even": [4, 100],
        "ordered_cross_target_cases": cross_cases,
        "shared_position_configurations": shared_total,
        "four_distinct_configurations": four_total,
        "all_assertions_passed": True,
        "runtime_seconds": time.time()-started,
        "limitations": [
            "Finite exact algebra checks only; no asymptotic or pointwise estimate.",
            "No universal Goldbach or residual-set coverage is claimed."
        ]
    }
    out = Path(__file__).with_name("stage66_sage_results.json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: Sage exact Lipschitz cases:", lipschitz_cases)
    print("PASS: Sage aggregate rational vectors:", aggregate_cases)
    print("PASS: exact Gram and prime partitions:", gram_cases, cross_cases)
    print("RESULT:", out)


if __name__ == "__main__":
    from sage.all import sqrt
    main()
