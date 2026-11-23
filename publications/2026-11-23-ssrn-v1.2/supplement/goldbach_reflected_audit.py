"""Exact finite audit for the Goldbach working paper; Python 3 standard library.
Run: python3 goldbach_reflected_audit.py [even_limit] > audit.json
"""
import json
from math import gcd, isqrt, prod
import sys


def additive_primes(limit):
    if limit < 3:
        return []
    primes, markers = [3], {9: [3]}
    for c in range(5, limit + 1, 2):
        hits = markers.pop(c, None)
        if hits is None:
            primes.append(c)
            markers.setdefault(c*c, []).append(c)
        else:
            for p in hits:
                markers.setdefault(c + 2*p, []).append(p)
    return primes


def eratosthenes(limit):
    prime = bytearray(b'\1') * (limit + 1)
    prime[:2] = b'\0\0'
    for d in range(2, isqrt(limit) + 1):
        if prime[d]:
            prime[d*d::d] = b'\0' * (1 + (limit-d*d)//d)
    return prime


def audit(limit):
    primes = additive_primes(limit)
    prime = eratosthenes(limit)
    assert primes == [x for x in range(3, limit+1) if prime[x]]
    stats = {s: dict(targets=0, pairs=0, min_R=None, first_min=None,
                     zero_targets=0, wheel_false_positive_pairs=0,
                     wheel_omitted_prime_pairs=0) for s in ('all', 'H', 'H1')}
    examples = {'false_positive': None, 'omitted_prime': None}
    selected = {}
    for n in range(4, limit + 1, 2):
        z = isqrt(max(0, n-3))
        batch = [p for p in primes if p <= z]
        P = prod(batch)
        s = n//2-3
        good, direct, wheel = set(), set(), set()
        for a in range(max(0, (s+1)//2)):
            p, q = 3+2*a, n-3-2*a
            # A factor in the batch is allowed only when the endpoint equals it.
            if gcd(p*q, P) == 1 or ((p in batch or gcd(p, P) == 1)
                                    and (q in batch or gcd(q, P) == 1)):
                good.add(p)
            if prime[p] and prime[q]:
                direct.add(p)
            if gcd(p*q, 210) == 1:
                wheel.add(p)
        assert good == direct, (n, good ^ direct)
        # Independently apply the scheduling rule, mirrored in a.
        count = max(0, (s+1)//2)
        alive = bytearray(b'\1') * count
        for ell in batch:
            first = (ell*ell-3)//2
            for a in range(first, count, ell):
                alive[a] = 0
            for b in range(first + ((s-count+1-first+ell-1)//ell if s-count+1 > first else 0)*ell, s+1, ell):
                alive[s-b] = 0
        assert good == {3+2*a for a, ok in enumerate(alive) if ok}, n
        fp, omitted = wheel-direct, direct-wheel
        for key, members in [('false_positive',fp), ('omitted_prime',omitted)]:
            if members and examples[key] is None:
                p = min(members)
                examples[key] = [n,p,n-p]
        r = len(good)
        for key in ['all'] + ([] if prime[n//2] else ['H1' if prime[n-1] else 'H']):
            d = stats[key]
            d['targets'] += 1
            d['pairs'] += r
            d['zero_targets'] += int(r==0)
            d['wheel_false_positive_pairs'] += len(fp)
            d['wheel_omitted_prime_pairs'] += len(omitted)
            if d['min_R'] is None or r < d['min_R']:
                d['min_R'], d['first_min'] = r, n
        if n in (4, 6, 8, 16, 28, 54, 100, 210, 7928, 7930):
            selected[n] = [len(wheel), r, len(fp), len(omitted)]
    return dict(range=[4,limit,2], odd_primes=len(primes), status='PASS',
                stats=stats, wheel_examples=examples, selected=selected)

if __name__ == '__main__':
    lim = int(sys.argv[1]) if len(sys.argv)>1 else 7930
    if lim < 4 or lim % 2:
        raise SystemExit('Provide an even limit >= 4.')
    print(json.dumps(audit(lim), indent=2))
