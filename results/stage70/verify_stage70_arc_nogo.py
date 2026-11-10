#!/usr/bin/env python3
"""Exact rational regression of Stage 70's Fejer/Fourier geometric constants.

All assertions are finite checks of the displayed algebra and endpoint windows.
The universal Fourier/PNT theorem is proved in 03_actual_arc_cone_nogo.md,
not by executing this program.
"""
from fractions import Fraction
import json

cases = [(10**6,100),(10**8,1000),(10**10,10000),(10**12,100000)]
rows = []
for X,P in cases:
    L = X // (4*P)
    nu_max = Fraction(2*P*P,X)
    Q = Fraction(L*(2*L+1),3*(L+1))
    lower_D = Fraction(1,100) / Q
    target_D = Fraction(P,50*X)
    assert L >= 1 and nu_max <= Fraction(1,10)
    assert Fraction(1,4*(L+1)) <= Fraction(P,X)  # Fejer core inside q=1
    assert Q == 2*sum((Fraction(L+1-j,L+1))**2 for j in range(1,L+1)) if L<10000 else Q == Fraction(L*(2*L+1),3*(L+1))
    assert lower_D >= target_D
    for N in (X//2,X):
        assert N % 2 == 0 and N-2*L>=6 and N+2*L<=2*X
    rows.append({"X":X,"P":P,"L":L,"nu_max":str(nu_max),
                 "Q":str(Q),"D_from_Cauchy":str(lower_D),
                 "D_target":str(target_D),"passed":True})

print(json.dumps({"status":"PASS","scope":"Exact parameter/window checks; not a proof of Goldbach",
                  "cases":rows},indent=2))
