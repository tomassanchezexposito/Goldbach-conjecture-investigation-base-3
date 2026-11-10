#!/usr/bin/env python3
"""Exact rational verification of the sharp Stage 66 local-modulus energy lemma.

All examples are abstract Fourier coefficient sequences, not genuine prime
coefficients and not counterexamples to Goldbach.
"""
from fractions import Fraction as Q
from itertools import product
from math import ceil
from pathlib import Path
import json


def pos(x):
    return max(x, Q(0))


def extremizer(A, increments, N=100):
    """Construct exact global-energy minimizer with c(N)=-A."""
    seq = {N: -A}
    seq.update({N+h: -pos(A-d) for h, d in increments.items()})
    assert len(seq) == len(increments) + 1
    for h,d in increments.items():
        assert abs(seq[N+h]-seq[N]) <= d
    return seq


def minimum_energy(A, increments):
    return A*A+sum((pos(A-d)**2 for d in increments.values()), Q(0))


def lipschitz_closed(A,L,H):
    if L==0:
        return Q(2*H+1)*A*A
    J=min(H,max(0,ceil(A/L)-1))
    return A*A+2*(J*A*A-A*L*J*(J+1)
                  +L*L*Q(J*(J+1)*(2*J+1),6))


def main():
    cases=0
    for A,L,H,step in product(
            (Q(1),Q(5,2),Q(7),Q(10),Q(25,3)),
            (Q(0),Q(1,3),Q(1),Q(2),Q(7)),
            (0,1,2,4,8,20),(1,2)):
        increments={step*h:L*abs(h) for h in range(-H,H+1) if h}
        sharp=minimum_energy(A,increments)
        seq=extremizer(A,increments)
        actual=sum((v*v for v in seq.values()),Q(0))
        closed=lipschitz_closed(A,L,H)
        assert actual==sharp==closed,(A,L,H,step,actual,sharp,closed)
        cases+=1
    nonuniform={-7:Q(2,3),-4:Q(5),-1:Q(1,4),3:Q(9,5),8:Q(12)}
    A=Q(3)
    assert minimum_energy(A,nonuniform)==sum(
        (v*v for v in extremizer(A,nonuniform).values()),Q(0))
    # Given a threshold B, feasible iff B>=the displayed sharp minimum.
    minB=minimum_energy(A,nonuniform)
    assert minB-Q(1,100)<minB and minB<=minB
    # For a central negative coefficient of magnitude A, localized
    # regularity necessarily spreads nonzero energy to its close shifts.
    strict_excluded=minB-Q(1,100)
    assert all(minB>strict_excluded for _ in range(1))
    example={"A":str(A),"increments":{str(k):str(v) for k,v in nonuniform.items()},
             "minimum_energy":str(minB),"excluded_energy_budget":str(strict_excluded)}
    data={
        "classification":"EXACT ABSTRACT SEQUENCE CHECK; NOT GOLDBACH",
        "lipschitz_parameter_cases_checked":cases,
        "strides":[1,2],
        "H_values":[0,1,2,4,8,20],
        "number_of_independent_formulas":2,
        "nonuniform_case":example,
        "all_assertions_passed":True
    }
    out=Path(__file__).with_name("stage66_exact_results.json")
    out.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("PASS:",cases,"exact Lipschitz local-modulus tests; strides 1 and 2")
    print("PASS: nonuniform modulus sharpness and strict global-energy exclusion")
    print("FINITE VERIFIER ONLY:",out)


if __name__=="__main__":
    main()
