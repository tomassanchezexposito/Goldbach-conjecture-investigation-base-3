#!/usr/bin/env python3
"""Finite Stage 59 short-window wheel-210 experiment; no universal proof.

Run with Python 3: python results/stage59/verify_mod210_pilot.py
Produces stage59_mod210_pilot.json. Exact integer and rational arithmetic.
"""
from functools import lru_cache
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json

LIMIT=35000
TARGETS=range(10000,18000,20)
WINDOW_LENGTHS=(3,5,9,21,51)
SPACINGS=(2,210)

def prime_sieve(n):
    f=bytearray([1])*(n+1)
    f[:2]=bytes(2)
    for p in range(2,isqrt(n)+1):
        if f[p]:
            f[p*p:n+1:p]=bytes((n-p*p)//p+1)
    return f

flags=prime_sieve(LIMIT)
primes=[p for p in range(2,LIMIT+1) if flags[p]]

@lru_cache(None)
def R(n):
    return sum(flags[n-p] for p in primes if 2*p<n)

def wheel(n):
    a=1
    for p in (3,5,7):
        a*=p-1 if n%p==0 else p-2
    return a

def in_H(n):
    return n>=4 and n%2==0 and n-1>1 and n//2>1 and not flags[n-1] and not flags[n//2]

def A(k,j):
    return Fraction(sum(t*t for t in range(1,j+1))+
                    sum(t*t for t in range(1,k-j)),k*k)

def main():
    centers=[n for n in TARGETS if in_H(n)]
    assert len(centers)==295
    results=[]
    for k in WINDOW_LENGTHS:
        assert k%2==1
        j=k//2
        constant=A(k,j)
        for step in SPACINGS:
            passed=valid=0
            for center in centers:
                ns=[center+(i-j)*step for i in range(k)]
                if ns[0]<4 or ns[-1]>LIMIT:
                    continue
                x=[Fraction(R(n),wheel(n)) for n in ns]
                mu=sum(x,Fraction())/k
                E=sum((x[i+1]-x[i])**2 for i in range(k-1))
                assert (x[j]-mu)**2<=constant*E
                passed+=int(mu*mu>constant*E)
                valid+=1
            results.append({"k":k,"spacing":step,"targets":valid,"certified":passed})
            print("k",k,"step",step,"passed",passed,"/",valid)
    expected={
        (3,2):295,(3,210):295,(5,2):295,(5,210):295,
        (9,2):295,(9,210):295,(21,2):295,(21,210):295,
        (51,2):10,(51,210):72,
    }
    assert all(r["targets"]==295 and
               r["certified"]==expected[(r["k"],r["spacing"])] for r in results)
    out={"status":"finite observation, no universal claim",
         "center_grid":{"start":10000,"stop_exclusive":18000,"step":20,
                        "residual_centers":295},
         "sieve_limit":LIMIT,"results":results}
    Path(__file__).with_name("stage59_mod210_pilot.json").write_text(
        json.dumps(out,indent=2)+"\n",encoding="utf-8")

if __name__=="__main__":
    main()
