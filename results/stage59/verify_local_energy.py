#!/usr/bin/env python3
"""Stage 59: exact path-energy and four-prime coincidence verification.

Finite test only. No statement about all even integers is proved by this run.
Python standard library only. Output: stage59_local_check.json
"""
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json

MAX_N = 500
BLOCKS = ((50,54),(50,60),(50,100),(50,200),(262,362))

def sieve(limit):
    f = bytearray([1]) * (limit+1)
    f[:2] = bytes(2)
    for p in range(2,isqrt(limit)+1):
        if f[p]:
            f[p*p:limit+1:p] = bytes((limit-p*p)//p+1)
    return f

def trial_prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def wheel(n):
    a=1
    for ell in (3,5,7):
        a *= ell-1 if n%ell==0 else ell-2
    return a

def in_H(n,f):
    return n>=4 and n%2==0 and n-1>1 and n//2>1 and not f[n-1] and not f[n//2]

def pairs(n,f):
    return [(p,n-p) for p in range(2,n//2) if f[p] and f[n-p]]

def A(k,j):
    return Fraction(sum(t*t for t in range(1,j+1))+
                    sum(t*t for t in range(1,k-j)),k*k)

def block(low,high,f):
    ns=list(range(low,high+1,2))
    lists=[pairs(n,f) for n in ns]
    x=[Fraction(len(a),wheel(n)) for n,a in zip(ns,lists)]
    k=len(ns)
    mu=sum(x,Fraction())/k
    energy=sum((x[i+1]-x[i])**2 for i in range(k-1))
    shifted=sum(x[i]*x[i+1] for i in range(k-1))
    assert energy == 2*sum(v*v for v in x)-x[0]**2-x[-1]**2-2*shifted
    certificates=[]
    for j in range(k):
        c=[Fraction(t+1,k) if t<j else -Fraction(k-t-1,k)
           for t in range(k-1)]
        diffs=[x[t+1]-x[t] for t in range(k-1)]
        assert x[j]-mu == sum((a*b for a,b in zip(c,diffs)),Fraction())
        assert sum((a*a for a in c),Fraction()) == A(k,j)
        assert (x[j]-mu)**2 <= A(k,j)*energy
        certificates.append(mu**2 > A(k,j)*energy)
    shared=distinct=0
    for left,right in zip(lists,lists[1:]):
        for p,q in left:
            for r,s in right:
                if len({p,q,r,s})==4:
                    distinct+=1
                else:
                    assert len({p,q,r,s})==3
                    shared+=1
    result={
        "inclusive_interval":[low,high],"k":k,
        "residual_targets":sum(in_H(n,f) for n in ns),
        "actual_zeros":sum(not v for v in x),
        "certified_residual_targets":sum(in_H(n,f) and certificates[j]
                                          for j,n in enumerate(ns)),
        "mean":str(mu),"energy":str(energy),
        "shared_prime_terms":shared,"four_distinct_terms":distinct,
    }
    assert result["actual_zeros"] == 0
    return result

def sharpness():
    cases=0
    for k in (3,4,5,10):
        for j in range(k):
            c=[Fraction(t+1,k) if t<j else -Fraction(k-t-1,k)
               for t in range(k-1)]
            d=[-a for a in c]
            x=[Fraction() for _ in range(k)]
            for t in range(j-1,-1,-1): x[t]=x[t+1]-d[t]
            for t in range(j,k-1): x[t+1]=x[t]+d[t]
            assert x[j]==0 and all(z>=0 for z in x)
            mu=sum(x)/k
            E=sum(z*z for z in d)
            assert mu**2 == A(k,j)*E
            cases+=1
    return cases

def cyclic():
    cases=0
    for k in (10,20,100):
        x=[0]+[1]*(k-1)
        for m in (1,2,3,4):
            avg=Fraction(sum(all(x[(j+t)%k] for t in range(m))
                             for j in range(k)),k)
            assert avg==Fraction(k-m,k)
            cases+=1
    return cases

def main():
    f=sieve(MAX_N)
    for n in range(4,MAX_N+1,2):
        assert pairs(n,f)==[(p,n-p) for p in range(2,n//2)
                            if trial_prime(p) and trial_prime(n-p)]
        assert wheel(n)==sum(gcd(a,210)==1 and gcd(n-a,210)==1
                             for a in range(210))
    rows=[block(l,u,f) for l,u in BLOCKS]
    assert [(r["certified_residual_targets"],r["shared_prime_terms"],
             r["four_distinct_terms"]) for r in rows] == [
             (2,5,22),(3,13,56),(0,80,451),(0,328,2987),(0,368,6712)]
    out={"evidence":"finite exact checks only","blocks":rows,
         "independent_pair_checks":249,"direct_wheel_checks":249,
         "sharpness_cases":sharpness(),"cyclic_moment_cases":cyclic()}
    outpath=Path(__file__).with_name("stage59_local_check.json")
    outpath.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2))

if __name__=="__main__":
    main()
