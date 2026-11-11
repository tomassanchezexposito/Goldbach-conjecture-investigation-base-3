#!/usr/bin/env python3
"""Exact finite regression, formal independent prime logarithms; no prime sweep.

Run: python3 -B results/stage73/verify_stage73.py
Prints deterministic JSON; never changes historical results.
"""
from collections import Counter
from fractions import Fraction as F
from math import gcd, isqrt
import json


def factors(n):
    out = Counter()
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] += 1
            n //= d
        d += 1
    if n > 1:
        out[n] += 1
    return out


def mu(n):
    f = factors(n)
    return 0 if any(k > 1 for k in f.values()) else (-1)**len(f)


def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]


def phi(n):
    return sum(gcd(k, n) == 1 for k in range(n))


def lam(n):
    f = factors(n) if n > 1 else {}
    return Counter({next(iter(f)): 1}) if len(f) == 1 else Counter()


def add(dest, src, scalar=1):
    for p, a in src.items():
        dest[p] += scalar*a


def clean(v):
    return {p:a for p,a in v.items() if a}


def vaughan(n, U, V):
    terms = [Counter() for _ in range(4)]
    if n <= V:
        add(terms[0], lam(n))
    for d in divisors(n):
        if d <= U:
            add(terms[1], factors(n//d), mu(d))
            for m in divisors(n//d):
                if m <= V:
                    add(terms[2], lam(m), mu(d))
        if d > U:
            for m in divisors(n//d):
                if m > V:
                    add(terms[3], lam(m), mu(d))
    return terms


def product(a, b):
    c = Counter()
    for p,x in a.items():
        for q,y in b.items():
            c[tuple(sorted((p,q)))] += x*y
    return c


def main():
    checks = 0
    params = [(1,1), (2,3), (4,4), (5,2), (12,10)]
    for U,V in params:
        for n in range(1,121):
            t = vaughan(n,U,V)
            total = Counter()
            for sign,a in zip([1,1,-1,1],t):
                add(total,a,sign)
            assert clean(total) == clean(lam(n)), (n,U,V)
            c = Counter()
            for d in divisors(n):
                if d<=U and n//d<=V:
                    add(c,lam(n//d),mu(d))
            assert all(abs(a)<=factors(n)[p] for p,a in c.items())
            checks += 1
    binary = []
    for N in [16,28,40,64,100,120]:
        # Unit support on 1<=n<N, with true formal Lambda logarithms.
        direct = Counter()
        pieces = [Counter() for _ in range(4)]
        for n in range(1,N):
            add(direct, product(lam(n),lam(N-n)))
            for j,t in enumerate(vaughan(n,3,4)):
                add(pieces[j],product(t,lam(N-n)))
        combined = Counter()
        for sign,t in zip([1,1,-1,1],pieces):
            add(combined,t,sign)
        assert clean(combined) == clean(direct)
        binary.append({'N':N, 'formal_log_monomials':len(clean(direct)), 'identity':True})
    D = 210
    units = [r for r in range(D) if gcd(r,D)==1]
    rows = []
    for N in range(0,D,2):
        A = sum((N-r)%D in units for r in units)
        crt = 1
        local = F(1)
        for p in [2,3,5,7]:
            nu = 1 if N%p==0 else 2
            crt *= p-nu
            local *= F(p*(p-nu),(p-1)**2)
        ram = sum((F(mu(q)**2,phi(q)**2)*sum(d*mu(q//d) for d in divisors(gcd(q,N)))
                   for q in divisors(D)), F(0))
        assert A == crt
        assert F(D*A,phi(D)**2) == local == ram
        rows.append({'N_mod_210':N,'A_210':A,'F_210':str(local)})
    assert min(F(r['F_210']) for r in rows) == F(175,128)
    assert all((F(r['F_210'])==F(175,128)) == (gcd(r['N_mod_210'],105)==1) for r in rows)
    # Exact kernel-bound hypothesis on decisive endpoint/support inputs.
    for X,N in [(16,8),(16,16),(600,300),(600,400),(600,540)]:
        for p in range(1,X):
            # Extremal pair q=1 or X-1 suffices because difference is affine.
            for q in [1,X-1]:
                assert abs(F(p+q-N,3*X)) <= F(1,2)
    out={'status':'PASS','arithmetic':'integer/Fraction; log primes are formal independent variables',
         'typeI_coefficient_bounds_checked':checks,'vaughan_identity_checks':checks,'n_range':[1,120],'truncations':params,
         'binary_formal_checks':binary,'wheel_residues_checked':105,
         'minimum_F210':'175/128','wheel_rows':rows,
         'limitations':'Finite algebra regressions; no asymptotic prime-pair or PNT verification.'}
    print(json.dumps(out,indent=2))

if __name__ == '__main__':
    main()
