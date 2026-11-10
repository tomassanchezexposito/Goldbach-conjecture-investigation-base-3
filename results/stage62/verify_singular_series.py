#!/usr/bin/env python3
"""Finite exact CRT examples for Stage 62's singular-series theorem.

Never infer actual Goldbach pair counts from these arithmetic examples.
The infinite theorem uses Dirichlet's theorem and Euler's prime reciprocal divergence.
"""
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod
import json
from pathlib import Path


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def odd_prime_divisors(n):
    out = []
    while n % 2 == 0:
        n //= 2
    p = 3
    while p*p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        out.append(n)
    return out


def singular_factor(n):
    value = Fraction(1)
    for p in odd_prime_divisors(n):
        value *= Fraction(p-1, p-2)
    return value


def wheel(n):
    return prod(p-(1 if n % p == 0 else 2) for p in (2,3,5,7))


def wheel_direct(n):
    return sum(gcd(a,210)==1 and gcd(n-a,210)==1 for a in range(210))


def find_crt_prime(primes):
    P = prod(primes)
    # q=1+t*P, with q=4 (mod 5) -> t*P=3 (mod 5)
    t = (3*pow(P,-1,5))%5
    first = 1+t*P
    modulus = 5*P
    for j in range(2500):
        q = first+j*modulus
        if q > max(primes) and is_prime(q):
            assert q%5 == 4 and all(q%p == 1 for p in primes)
            return q
    raise AssertionError("Finite search failed; this does not contradict Dirichlet")


def main():
    small_primes = (11,13,17,19,23,29)
    rows = []
    for k in range(1,len(small_primes)+1):
        P = small_primes[:k]
        q = find_crt_prime(P)
        n = 2*(q-1)
        assert is_prime(q) and n%2 == 0
        assert n//2 > 2 and not is_prime(n//2)
        assert n-1 > 5 and (n-1)%5 == 0 and not is_prime(n-1)
        assert wheel(n) == wheel_direct(n)
        assert wheel(n+2) == wheel_direct(n+2)
        sn = singular_factor(n)
        sn2 = singular_factor(n+2)
        assert sn2 == Fraction(q-1,q-2)
        product_lower = prod((Fraction(p-1,p-2) for p in P),start=Fraction(1))
        assert sn >= product_lower
        ratio = sn/sn2*Fraction(wheel(n+2),wheel(n))
        assert ratio >= Fraction(15,96)*product_lower
        rows.append({"P":list(P),"q":q,"N":n,
                     "wheel_N":wheel(n),"wheel_N_plus_2":wheel(n+2),
                     "odd_prime_factors_N":odd_prime_divisors(n),
                     "singular_factor_ratio":str(sn/sn2),
                     "wheel_normalized_ratio":str(ratio),
                     "proved_lower_bound":str(Fraction(15,96)*product_lower)})
    grid=[]
    for e in product((Fraction(-1,3),Fraction(0),Fraction(1,3)),repeat=3):
        a,b,c=[1+t for t in e]
        d=(-a*a-3*b*b-c*c+6*a*b+2*a*c+6*b*c)/9
        grid.append(d)
    assert len(grid)==27 and min(grid)==Fraction(4,9)
    result={"status":"Finite exact examples only; universal theorem proved separately",
            "examples":rows,"conditional_grid_minimum":str(min(grid))}
    out=Path(__file__).with_name("finite_examples.json")
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"examples":len(rows),"conditional_grid_minimum":"4/9",
                      "last_example":rows[-1],"file":str(out)},indent=2))


if __name__=="__main__":
    main()
