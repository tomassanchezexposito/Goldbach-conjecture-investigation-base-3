#!/usr/bin/env python3
"""Independent exact Stage 69 regression, standard library only.
Checks prime-pair ledgers and sharp center/shift energy. Not a Goldbach proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, isqrt
import json

def prime(n):
    return n>1 and all(n%d for d in range(2,isqrt(n)+1))
def H(n):
    return n>=4 and n%2==0 and not prime(n-1) and not prime(n//2)
P=[p for p in range(2,151) if prime(p)]
r={n:sum(p*q for p,q in product(P,repeat=2) if p+q==n)
   for n in range(4,301)}
U={n:[(p,n-p) for p in P if p<n-p and prime(n-p)]
   for n in (28,36,50,56,66,100,120) if H(n)}
for n,pairs in U.items():
    assert r[n]==2*sum(p*q for p,q in pairs)
    assert r[n]**2==4*sum((p*q)**2 for p,q in pairs)+8*sum(
        p*q*u*v for i,(p,q) in enumerate(pairs) for u,v in pairs[i+1:])
for n,m in combinations(U,2):
    a,b=U[n],U[m]
    shared=sum(p*q*u*v for p,q in a for u,v in b if {p,q}&{u,v})
    disjoint=sum(p*q*u*v for p,q in a for u,v in b if not ({p,q}&{u,v}))
    assert r[n]*r[m]==4*(shared+disjoint)
    anchor=sum(x*x*(n-x)*(m-x) for x in P if prime(n-x) and prime(m-x)
               and x!=n//2 and x!=m//2)
    assert anchor==shared
energy=0
for m,A in product(range(1,8),range(1,7)):
    for d in (F(0),F(A,3),F(A),F(3*A,2),F(2*A),F(3*A)):
        v=m*d*d
        x=max(F(A),F(m,m+1)*d)
        exact=x*x+m*(x-d)**2
        formula=F(A*A)+m*(d-A)**2 if v<=F(A*A*(m+1)**2,m) else v/F(m+1)
        assert exact==formula
        assert exact>=F(A*A)+m*max(F(A)-d,F(0))**2
        energy+=1
s=F(1013,3000); P0,X=13,2000
centers=[(min(abs(s-F(a,q)),1-abs(s-F(a,q))),q,a) for q in range(1,P0+1)
         for a in range(q) if gcd(a,q)==1]
assert min(centers)[1]==3
assert all(dist>F(P0,q*X) for dist,q,a in centers)
out={'stage':69,'status':'PASS','finite_only':True,'checked_unordered_targets':len(U),
     'checked_shifted_target_pairs':len(list(combinations(U,2))),
     'checked_exact_energy_cases':energy,
     'rational_minor_arc_example':{'alpha':'1013/3000','P':13,'X':2000,
         'closest_center_denominator':3,'in_major_arcs':False},
     'interpretation':'Minor-arc membership alone does not imply every nearby rational approximant has denominator>P.'}
print(json.dumps(out,indent=2))
