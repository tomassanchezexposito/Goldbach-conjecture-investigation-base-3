#!/usr/bin/env python3
"""Stage 59: exact graph-Laplacian multi-shift zero-exclusion certificates.

Finite verification only. Generic graph-Sobolev bounds are established
mathematics; no universal prime-pair theorem is claimed.
Python standard library only.
"""
from fractions import Fraction
from functools import lru_cache
from math import isqrt
from pathlib import Path
import json

LIMIT=35000
K=51
J=25
CENTER_RANGE=range(10000,18000,20)
LAGS=(1,2,5,10,50)
SPACINGS=(2,210)
OUT=Path(__file__).with_name("graph_energy_pilot.json")

def sieve(n):
    flags=bytearray([1])*(n+1)
    flags[:2]=bytes(2)
    for p in range(2,isqrt(n)+1):
        if flags[p]:
            flags[p*p:n+1:p]=bytes((n-p*p)//p+1)
    return flags

PRIME=sieve(LIMIT)
PRIMES=[p for p in range(2,LIMIT+1) if PRIME[p]]

@lru_cache(maxsize=None)
def R(n):
    return sum(PRIME[n-p] for p in PRIMES if 2*p<n)

def H(n):
    return n>=4 and n%2==0 and n-1>1 and n//2>1 and not PRIME[n-1] and not PRIME[n//2]

def A210(n):
    a=1
    for p in (3,5,7):
        a*=p-1 if n%p==0 else p-2
    return a

def solve(A,b):
    """Exact Gaussian elimination for a positive-definite integer matrix."""
    n=len(b)
    M=[[Fraction(A[i][j]) for j in range(n)]+[Fraction(b[i])] for i in range(n)]
    for i in range(n):
        p=M[i][i]
        assert p>0
        for c in range(i,n+1):
            M[i][c]/=p
        for row in range(i+1,n):
            coeff=M[row][i]
            if coeff:
                for c in range(i,n+1):
                    M[row][c]-=coeff*M[i][c]
    x=[Fraction(0)]*n
    for i in reversed(range(n)):
        x[i]=M[i][n]-sum((M[i][j]*x[j] for j in range(i+1,n)),Fraction())
    assert all(sum((Fraction(A[i][j])*x[j] for j in range(n)),Fraction())==b[i]
               for i in range(n))
    return x

def graph(k,lag,j):
    """Unit conductances on edges of lengths 1,...,lag."""
    assert 1<=lag<k
    L=[[0]*k for _ in range(k)]
    edges=[]
    for i in range(k):
        for t in range(i+1,min(k,i+lag+1)):
            L[i][i]+=1
            L[t][t]+=1
            L[i][t]-=1
            L[t][i]-=1
            edges.append((i,t))
    # (kL+J)v=k e_j-1; thus L v=e_j-1/k with mean(v)=0.
    M=[[k*L[i][t]+1 for t in range(k)] for i in range(k)]
    rhs=[k*(i==j)-1 for i in range(k)]
    v=solve(M,rhs)
    assert sum(v,Fraction())==0
    constant=v[j]
    # Nonnegative equality witness from the discrete maximum principle.
    assert all(v[j]>=v[i] for i in range(k))
    x=[v[j]-v[i] for i in range(k)]
    mu=sum(x,Fraction())/k
    energy=sum((x[i]-x[t])**2 for i,t in edges)
    assert x[j]==0 and all(q>=0 for q in x)
    assert mu**2==constant*energy
    return constant,edges

def main():
    centers=[n for n in CENTER_RANGE if H(n)]
    assert len(centers)==295
    rows=[]
    for lag in LAGS:
        constant,edges=graph(K,lag,J)
        for step in SPACINGS:
            passed=0
            max_ratio=Fraction(0)
            for center in centers:
                ns=[center+(i-J)*step for i in range(K)]
                assert ns[0]>=4 and ns[-1]<=LIMIT
                x=[Fraction(R(n),A210(n)) for n in ns]
                mean=sum(x,Fraction())/K
                E=sum((x[i]-x[t])**2 for i,t in edges)
                passed+=int(mean**2>constant*E)
                max_ratio=max(max_ratio,constant*E/mean**2)
            rows.append({"lag_cutoff":lag,"spacing":step,"checked":len(centers),
                         "certified":passed,"constant":str(constant),
                         "max_energy_ratio":str(max_ratio)})
            print(f"lag={lag}, spacing={step}, certified={passed}/{len(centers)}")
    expected={
        (1,2):10,(1,210):72,
        (2,2):287,(2,210):294,
        (5,2):295,(5,210):295,
        (10,2):295,(10,210):295,
        (50,2):295,(50,210):10,
    }
    assert all(q["certified"]==expected[(q["lag_cutoff"],q["spacing"])]
               for q in rows)
    out={"status":"finite exact check and generic sharp graph bound; universal coverage open",
         "target_range":[10000,17980,20],"residual_centers":len(centers),
         "k":K,"central_index":J,"sieve_limit":LIMIT,"rows":rows}
    OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")

if __name__=="__main__":
    main()
