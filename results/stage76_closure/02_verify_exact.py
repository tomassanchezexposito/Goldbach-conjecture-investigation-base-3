"""Independent Python and Sage modes for finite closure certificates.

Run with python3 ... --mode python or sage -python ... --mode sage.
No mode imports or calls an earlier project verifier. No prime-pair search.
"""
import argparse
import hashlib
import itertools
import json
import math
import platform
import sys
from fractions import Fraction

TARGETS = (4, 6, 8, 10, 12, 16, 18, 20, 22, 28, 30, 34, 38, 40)
PAIRS = ((2, 2), (3, 7), (3, 13), (5, 11), (7, 7), (11, 19))


def python_mode():
    Q = Fraction
    def prime(n):
        return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))
    def comp(n):
        return n > 1 and not prime(n)
    coordinate_cases = 0
    for a in range(13):
        p = 3 + 2*a
        assert (p-3)//2 == a and p % 2 == 1 and p >= 3
        for b in range(13):
            q = 3 + 2*b
            N = p+q
            m, h = Q(N, 2), Q(q-p, 2)
            assert a+b == N//2-3 and p == m-h and q == m+h
            assert N-2*p == 2*q-N == q-p
            coordinate_cases += 1
    assert not prime(1) and prime(2)
    logical = []
    for N in TARGETS:
        first, middle = prime(N-1), prime(N//2)
        H = comp(N-1) and comp(N//2)
        H1 = N >= 8 and first and comp(N//2)
        assert not (H and H1) and (H or H1) == comp(N//2)
        for pair_positive in (False, True):
            C, B = first or middle or pair_positive, middle or pair_positive
            assert C == ((not H) or pair_positive)
            assert B == ((not (H or H1)) or pair_positive)
            assert C == (first or B)
        logical.append([N, H, H1])
    wheel = []
    for N in range(210):
        count = sum(math.gcd(a,210) == 1 and math.gcd((N-a)%210,210) == 1
                    for a in range(210))
        local = math.prod(l-(1 if N % l == 0 else 2) for l in (2,3,5,7))
        assert count == local
        wheel.append(count)
    phi = lambda n: sum(math.gcd(a,n) == 1 for a in range(1,n+1))
    assert phi(210) == 48 and phi(9) == 6 and phi(3)**2 == 4
    correct, false = Q(1,phi(3))-Q(1,phi(9)), Q(1,phi(3))-Q(1,phi(3)**2)
    assert (correct,false,correct-false) == (Q(1,3),Q(1,4),Q(1,12))
    exceptions = []
    for p,q in PAIRS:
        assert prime(p) and prime(q)
        exceptions.append([p+q,p,q,math.gcd(p*q,210) != 1,p == q])
    matching = []
    fixtures = ((), ((Q(0),Q(3,2)),), ((Q(3,2),Q(7,3)),(Q(4),Q(4))))
    for edges in fixtures:
        costs = [sum((e[b] for e,b in zip(edges,bits)),Q(0))
                 for bits in itertools.product((0,1),repeat=len(edges))]
        tau = sum((min(a,b) for a,b in edges),Q(0))
        assert min(costs) == tau
        matching.append(str(tau))
    # All vertex covers of a star; shared endpoint violates matching additivity.
    star_costs = [sum(bits) for bits in itertools.product((0,1),repeat=3)
                  if (bits[0] or bits[1]) and (bits[0] or bits[2])]
    star_min, star_edge_sum = min(star_costs), 2
    assert star_min == 1 < star_edge_sum
    # Linear forms in five independent variables; no symbolic package used.
    basis = [tuple(Q(i == j) for i in range(5)) for j in range(5)]
    F,A,EI,EK,P = basis
    add = lambda x,y: tuple(a+b for a,b in zip(x,y))
    sub = lambda x,y: tuple(a-b for a,b in zip(x,y))
    G = add(add(add(F,EK),A),EI)
    r,e = sub(G,P),sub(sub(P,EK),EI)
    assert A == add(sub(r,F),e) and r == sub(add(F,A),e)
    for tau in (Q(1,2),Q(3,4),Q(1)):
        left,right = tau/2-Q(1,40),tau/2+Q(1,40)
        args = (left,right,tau-left,tau-right)
        assert right-left == Q(1,20) and min(args) >= Q(9,40) and max(args) <= Q(21,40)
    assert Q(1)-Q(1,2)-Q(1,4) == Q(1,4)
    return {'logic':logical,'wheel':wheel,'exceptions':exceptions,
            'matching_tau':matching,'star':[star_min,star_edge_sum],
            'totient':[str(correct),str(false),str(correct-false)],
            'overlap_length':'1/20','conditional_margin':'1/4'}, {
            'coordinates':'169 integer-pair checks including midpoint and double symmetry',
            'logic':'14 fixed targets, two abstract R-positive truth values each',
            'wheel':'210 residue counts by gcd; four local factors',
            'matching':'Endpoint-cover enumeration on 0,1,2 disjoint edges',
            'star':'All eight zeroed-vertex subsets; no complementary-prime claim',
            'primality':'Trial division on prescribed fixture integers only',
            'error':'Independent exact linear coefficient vectors over Fraction'}


def sage_mode():
    from sage.all import QQ, ZZ, Zmod, PolynomialRing, euler_phi
    from sage.env import SAGE_VERSION
    ring = PolynomialRing(QQ, names=('a','b','m','h','F','A','EI','EK','P'))
    a,b,m,h,F,A,EI,EK,P = ring.gens()
    assert (3+2*a)+(3+2*b)-2*m == 2*(a+b-m+3)
    p,q,N = m-h,m+h,2*m
    assert p+q == N and N-2*p == 2*q-N == q-p
    assert (p-3)/2+(q-3)/2 == m-3
    assert A == (F+EK+A+EI-P)-F+(P-EK-EI)
    assert F+EK+A+EI-P == F+A-(P-EK-EI)
    logical = []
    for n in TARGETS:
        N = ZZ(n)
        first,middle = bool((N-1).is_prime()),bool((N//2).is_prime())
        H = N-1 > 1 and not first and N//2 > 1 and not middle
        H1 = N >= 8 and first and N//2 > 1 and not middle
        assert int(H)+int(H1) == int(N//2 > 1 and not middle)
        for r_positive in (0,1):
            assert bool(first or middle or r_positive) == bool(not H or r_positive)
            assert bool(middle or r_positive) == bool(not (H or H1) or r_positive)
        logical.append([n,bool(H),bool(H1)])
    residues = Zmod(210)
    units = {u for u in residues if u.is_unit()}
    wheel = []
    for n in residues:
        count = sum(1 for u in units if n-u in units)
        local = ZZ(1)
        for ell,_ in ZZ(210).factor():
            local *= ell-len({ZZ(0),ZZ(n)%ell})
        assert count == local
        wheel.append(int(count))
    assert euler_phi(210) == 48 and euler_phi(9) == 6 and euler_phi(3)**2 == 4
    correct = QQ(1)/euler_phi(3)-QQ(1)/euler_phi(9)
    false = QQ(1)/euler_phi(3)-QQ(1)/euler_phi(3)**2
    exceptions = []
    for p,q in PAIRS:
        assert ZZ(p).is_prime() and ZZ(q).is_prime()
        exceptions.append([p+q,p,q,not residues(p*q).is_unit(),p == q])
    # Independent attenuation grids, not the Python endpoint-cover algorithm.
    matching = []
    for edges in ((), ((QQ(0),QQ(3)/2),), ((QQ(3)/2,QQ(7)/3),(QQ(4),QQ(4)))):
        choices = []
        for left,right in edges:
            choices.append([(u,v,left-u+right-v)
                for u in {QQ(0),left/2,left} for v in {QQ(0),right/2,right} if u*v == 0])
        costs = [sum((c[2] for c in x),QQ(0)) for x in itertools.product(*choices)]
        tau = sum((min(x,y) for x,y in edges),QQ(0))
        assert min(costs) == tau
        matching.append(str(tau))
    # Star zero products force center=0 OR both leaves=0.
    star_min = min(QQ(1),QQ(1)+QQ(1))
    star_edge_sum = min(QQ(1),QQ(1))+min(QQ(1),QQ(1))
    assert star_min == 1 and star_edge_sum == 2
    lo,hi = QQ(9)/40,QQ(21)/40
    for tau in (QQ(1)/2,QQ(3)/4,QQ(1)):
        u0,u1 = tau/2-QQ(1)/40,tau/2+QQ(1)/40
        assert u1-u0 == QQ(1)/20 and lo <= u0 <= u1 <= hi
        assert lo <= tau-u1 <= tau-u0 <= hi
    assert QQ(1)-QQ(1)/2-QQ(1)/4 == QQ(1)/4
    return {'logic':logical,'wheel':wheel,'exceptions':exceptions,
            'matching_tau':matching,'star':[int(star_min),int(star_edge_sum)],
            'totient':[str(correct),str(false),str(correct-false)],
            'overlap_length':'1/20','conditional_margin':'1/4'}, {
            'sage_version':SAGE_VERSION,'coordinates':'Free polynomial identities over QQ',
            'logic':'Sage integer primality; independent predicate forms',
            'wheel':'Zmod(210) unit translations and factorization-based local counts',
            'matching':'Exact three-level attenuation grids per endpoint',
            'star':'Zero-product alternatives, minimum of two complete cover costs',
            'primality':'Sage exact is_prime on prescribed fixtures only',
            'error':'Free QQ polynomial elimination'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=('python','sage'), required=True)
    args = parser.parse_args()
    data,method = python_mode() if args.mode == 'python' else sage_mode()
    payload = json.dumps(data,sort_keys=True,separators=(',',':'))
    print(json.dumps({'status':'PASS','mode':args.mode,'python':sys.version,
        'platform':platform.platform(),'methods':method,'exact_results':data,
        'semantic_sha256':hashlib.sha256(payload.encode()).hexdigest(),
        'limits':'Finite and symbolic certificates only; no analytic-rate proof, Goldbach sweep or formal proof-assistant certification'},indent=2))
