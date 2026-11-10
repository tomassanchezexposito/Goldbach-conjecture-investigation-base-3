#!/usr/bin/env python3
"""Stage 59 exact finite checks. NOT a universal prime-pair theorem."""
from fractions import Fraction
from math import gcd, isqrt

LIMIT = 5000

def sieve(limit):
    b = bytearray([1]) * (limit+1)
    b[0:2] = b"\0\0"
    for d in range(2, isqrt(limit)+1):
        if b[d]:
            b[d*d:limit+1:d] = b"\0" * (((limit-d*d)//d)+1)
    return b

def trial_prime(n):
    return n>1 and all(n%d for d in range(2,isqrt(n)+1))

def wheel(n):
    return (2 if n%3==0 else 1)*(4 if n%5==0 else 3)*(6 if n%7==0 else 5)

def pairs(n, prime):
    return [(p,n-p) for p in range(3,n//2,2) if prime[p] and prime[n-p]]

def residual(n, prime):
    return n>=4 and n%2==0 and n-1>1 and n//2>1 and not prime[n-1] and not prime[n//2]

def energy(v):
    m=len(v)
    return sum((v[(j+1)%m]-v[j])**2 for j in range(m))

def certificate(v):
    m=len(v)
    return (sum(v)/m)**2 > Fraction(m*m-1,12*m)*energy(v)

def shared_pairs(n,h,prime):
    P=pairs(n,prime)
    Q=pairs(n+2*h,prime)
    return sum(bool(set(a) & set(b)) for a in P for b in Q)

def shared_direct(n,h,prime):
    m=n+2*h
    # For a common summand t, the two complements are uniquely determined.
    # This counts each shared-prime configuration exactly once.
    return sum(
        bool(prime[t] and prime[n-t] and prime[m-t] and t != n-t and t != m-t)
        for t in range(3,n-2)
        if n-t>=2 and m-t>=2
    )

def main():
    prime=sieve(LIMIT)
    for n in range(4,LIMIT+1,2):
        assert len(pairs(n,prime)) == sum(
            trial_prime(p) and trial_prime(n-p) for p in range(3,n//2,2))
    for n in range(4,402,2):
        assert wheel(n) == sum(
            gcd(a,210)==1 and gcd(n-a,210)==1 for a in range(210))
    x={n:Fraction(len(pairs(n,prime)),wheel(n)) for n in range(4,LIMIT+1,2)}
    failures=[]
    Htests=0
    for n in range(8,LIMIT-1,2):
        v=(x[n-2],x[n],x[n+2])
        good=certificate(v)
        if not good: failures.append(n)
        if residual(n,prime):
            Htests+=1
            assert good
    assert failures == [8], failures
    for m in (3,5,7,11):
        v=[Fraction(j*(m-j),2*m) for j in range(m)]
        mu=sum(v)/m
        K=Fraction(m*m-1,12*m)
        assert v[0]==0 and all(t>0 for t in v[1:])
        assert mu**2 == K*energy(v)
    for n in range(50,300,2):
        for h in (1,2):
            assert shared_pairs(n,h,prime)==shared_direct(n,h,prime),(n,h)
    print("Exact finite checks passed")
    print("range: even centers 8..%d"%(LIMIT-2))
    print("failed 3-point certificates:",failures)
    print("residual targets passing:",Htests)
    print("shared-prime configurations checked: 250 target-shift configurations")
    print("sharp constants checked for m=3,5,7,11")
    print("FINITE OBSERVATION ONLY; NOT A UNIVERSAL GOLDBACH PROOF")

if __name__ == "__main__":
    main()
