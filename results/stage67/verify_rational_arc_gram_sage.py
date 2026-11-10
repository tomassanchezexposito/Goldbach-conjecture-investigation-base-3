#!/usr/bin/env sage -python
"""Independent SageMath verification of rational-arc Gram formulae.

Exact roots of unity live in cyclotomic fields; t=1/(2*pi*i) is retained as a
formal polynomial variable.  This checks finite exact identities only.
"""
from sage.all import CyclotomicField, PolynomialRing, QQ, lcm, matrix, identity_matrix, ones_matrix
from itertools import combinations
from pathlib import Path
import json
import time


def common_modulus(shifts, arcs):
    dens = [4]
    for left, right in arcs:
        dens += [left.denominator(), right.denominator()]
    return lcm(dens)


def make_objects(L):
    K = CyclotomicField(L)
    R = PolynomialRing(K, 't')
    return K, R, R.gen()


def exp_rational(K, L, x):
    assert (x*L).denominator() == 1
    return K.gen()**ZZ(x*L)


def moment(K, R, t, L, n, left, right):
    if n == 0:
        return R(right-left)
    return R((exp_rational(K,L,n*right)-exp_rational(K,L,n*left))/n)*t


def conjugate_formal(poly, K, R, t):
    # The actual t=1/(2*pi*i) is purely imaginary, so conjugation maps t to -t.
    return sum(K(c).conjugate()*((-t)**d)
               for d, c in enumerate(poly.list()))


def gram_from_moments(K, R, t, L, shifts, arcs):
    M = matrix(R, len(shifts), len(shifts))
    for a, j in enumerate(shifts):
        for b, k in enumerate(shifts):
            val = R(0)
            for left, right in arcs:
                val += moment(K,R,t,L,k-j,left,right)
                val -= moment(K,R,t,L,-j,left,right)
                val -= moment(K,R,t,L,k,left,right)
                val += moment(K,R,t,L,0,left,right)
            M[a,b] = val
    return M


def gram_from_four_terms(K, R, t, L, shifts, arcs):
    M = matrix(R, len(shifts), len(shifts))
    for a, j in enumerate(shifts):
        for b, k in enumerate(shifts):
            val = R(0)
            for left, right in arcs:
                for n, sign in ((k-j,1),(-j,-1),(k,-1),(0,1)):
                    val += sign*moment(K,R,t,L,n,left,right)
            M[a,b] = val
    return M


def main():
    started = time.perf_counter()
    interval_matrices = 0
    hermitian_entries = 0
    center_tests = 0
    full_circle_entries = 0
    # Several disjoint and single-arc configurations with rational endpoints.
    configs = [
        ((-4,-1,2,5), [(QQ(1)/3-QQ(1)/20, QQ(1)/3+QQ(1)/20)]),
        ((-3,1,4), [(QQ(1)/5-QQ(1)/30, QQ(1)/5+QQ(1)/30),
                    (QQ(4)/5-QQ(1)/40, QQ(4)/5+QQ(1)/40)]),
        ((-7,-2,3,8), [(QQ(1)/7-QQ(1)/50, QQ(1)/7+QQ(1)/50),
                       (QQ(6)/7-QQ(1)/60, QQ(6)/7+QQ(1)/60)]),
        ((-5,2,9), [(QQ(1)/2-QQ(1)/32, QQ(1)/2+QQ(1)/32)]),
    ]
    for shifts, arcs in configs:
        shifts = tuple(shifts)
        L = common_modulus(shifts, arcs)
        K,R,t = make_objects(L)
        G1 = gram_from_moments(K,R,t,L,shifts,arcs)
        G2 = gram_from_four_terms(K,R,t,L,shifts,arcs)
        assert G1 == G2
        interval_matrices += len(shifts)**2
        for a in range(len(shifts)):
            for b in range(len(shifts)):
                assert G1[a,b] == conjugate_formal(G1[b,a],K,R,t)
                hermitian_entries += 1

    # Center vectors and their exact rank-one Gram: divisibility iff zero.
    for q in range(2, 21):
        L = lcm([q,4])
        K,R,t = make_objects(L)
        for a in range(1,q):
            if gcd(a,q) != 1:
                continue
            shifts = tuple(range(-6,7))
            v = []
            for j in shifts:
                val = exp_rational(K,L,-QQ(j*a)/q)-1
                assert (val == 0) == (j % q == 0)
                v.append(val)
                center_tests += 1
            G = matrix(K, len(shifts), len(shifts),
                       lambda r,c: v[r]*v[c].conjugate())
            trace = sum((G[r,r] for r in range(len(shifts))), K(0))
            assert G*G == trace*G

    # Full circle exactly yields I+11* for distinct nonzero shifts.
    for shifts in ((1,),(-2,3),(-5,-1,2,7)):
        shifts = tuple(shifts)
        L=4; K,R,t=make_objects(L)
        G=gram_from_moments(K,R,t,L,shifts,[(QQ(0),QQ(1))])
        expected=identity_matrix(R,len(shifts))+ones_matrix(R,len(shifts))
        assert G==expected
        full_circle_entries += len(shifts)**2

    data = {
        "classification": "INDEPENDENT SAGEMATH EXACT CYCLOTOMIC-FIELD VERIFICATION",
        "sage_version": str(__import__('sage.env',fromlist=['SAGE_VERSION']).SAGE_VERSION),
        "interval_gram_entries_compared": interval_matrices,
        "hermitian_entries_checked": hermitian_entries,
        "reduced_center_shift_tests": center_tests,
        "full_circle_entries_checked": full_circle_entries,
        "all_assertions_passed": True,
        "limitations": [
            "The exact computations verify finite algebraic identities, not an asymptotic estimate.",
            "Positive semidefiniteness follows from the integral Gram representation proved in report.md.",
            "No universal prime representation or pointwise prime saving is established."
        ]
    }
    data["runtime_seconds"] = time.perf_counter()-started
    out=Path(__file__).with_name('rational_arc_sage_results.json')
    out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('PASS: exact interval Gram matrices:', interval_matrices, 'entries')
    print('PASS: formal Hermitian symmetry:', hermitian_entries, 'entries')
    print('PASS: exact cyclotomic center tests:', center_tests)
    print('PASS: full-circle Gram entries:', full_circle_entries)
    print('RESULT:',out)


if __name__ == '__main__':
    from sage.all import gcd, ZZ
    main()
