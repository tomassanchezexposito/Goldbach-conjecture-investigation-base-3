#!/usr/bin/env python3
"""Exact finite checks for Stage 71 matching stability; not a Goldbach proof."""
import json
from math import isqrt


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def convolution(weights):
    c = {}
    for p, a in weights.items():
        for q, b in weights.items():
            c[p + q] = c.get(p + q, 0) + a * b
    return c


def min_product_dp(edges):
    """Independent exact integer allocation over both endpoints."""
    d = {0: 0}
    for a, b in edges:
        nd = {}
        for cost, score in d.items():
            for x in range(a + 1):
                for y in range(b + 1):
                    k = cost + x + y
                    nd[k] = min(nd.get(k, 10**18), score + (a-x)*(b-y))
        d = nd
    return [min(v for k, v in d.items() if k <= eta)
            for eta in range(sum(b for a, b in edges) + 1)]


edges = [(9, 6), (8, 7), (3, 1)]
exact = min_product_dp(edges)
greedy = []
for eta in range(sum(b for a, b in edges) + 1):
    remain = sum(a*b for a, b in edges)
    budget = eta
    for a, b in sorted(edges, reverse=True):
        t = min(budget, b)
        remain -= a*t
        budget -= t
    greedy.append(remain)
assert exact == greedy
assert exact[-1] == 0 and exact[-2] > 0

P = [p for p in range(3, 201, 2) if is_prime(p)]
w = {p: p + (p % 7)**2 for p in P}
c = convolution(w)
energy = sum(v*v for v in c.values())
rows = []
for N in (50, 100, 120, 256, 300):
    seen = set()
    retained = {}
    tau = 0
    for p in P:
        if p in seen:
            continue
        q = N-p
        if q in w:
            assert p != q
            chosen = p if w[p] >= w[q] else q
            retained[chosen] = w[chosen]
            tau += min(w[p],w[q])
            seen.update((p,q))
        else:
            retained[p] = w[p]
            seen.add(p)
    removed = {p:w[p] for p in P if p not in retained}
    assert sum(removed.values()) == tau
    cr = convolution(retained)
    assert c[N] > 0 and cr.get(N,0) == 0
    assert all(cr.get(k,0) <= v for k,v in c.items())
    assert sum(v*v for v in cr.values()) <= energy
    delta = convolution(removed)
    d1 = sum(removed.values())
    d2 = sum(a*a for a in removed.values())
    assert sum(v*v for v in delta.values()) <= d1*d1*d2
    assert all((c.get(k,0)-cr.get(k,0)) >= 0 for k in c)
    rows.append({'N':N, 'representations_coefficient':c[N],
                 'minimum_erasure_cost':tau,
                 'relative_mass_retained':f'{sum(retained.values())}/{sum(w.values())}',
                 'target_after_erasure':0,
                 'fourth_moment_monotone':True, 'young_L4_checked':True})

print(json.dumps({'status':'PASS','scope':'finite exact algebra only',
                  'independent_greedy_vs_brute_integer_dp_cases':len(exact),
                  'integer_dp_values':exact, 'prime_support_targets':rows},
                 indent=2))
