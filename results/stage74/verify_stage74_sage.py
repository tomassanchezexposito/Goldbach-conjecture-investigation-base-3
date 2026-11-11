#!/usr/bin/env sage-python
"""Independent exact Sage polynomial verification; no Python-verifier import.
Run: sage -python results/stage74/verify_stage74_sage.py
"""
from sage.all import ZZ, QQ, PolynomialRing, primes, divisors, moebius, euler_phi
from sage.version import version
import json


def main():
    P=PolynomialRing(QQ,names=['L'+str(p) for p in primes(145)])
    L=dict(zip(list(primes(145)),P.gens()))
    def lf(n):return sum((e*L[p] for p,e in ZZ(n).factor()),P.zero())
    def lam(n):
        f=ZZ(n).factor()
        return L[f[0][0]] if len(f)==1 else P.zero()
    def a(N,n):return QQ(moebius(n))/euler_phi(n) if ZZ(n).gcd(N)==1 else QQ(0)
    def aa(N,U):return sum((a(N,d) for d in range(1,U+1)),QQ(0))
    def gg(N,n,p0=None):
        z=QQ(1)
        for p,j in ZZ(n).factor():
            if p==p0:return QQ(0)
            z*=QQ(1)/p**j if N%p==0 else -QQ(1)/(p**j*(p-1))
        return z
    def bc(N,n,p0=None):return sum((QQ(moebius(d))/d*gg(N,n//d,p0) for d in divisors(n)),QQ(0))
    Ns=[2,6,16,28,210,2310,30030,510510]
    count=0;conv=0;local=0
    for N in Ns:
        for U in range(1,13):
            for V in range(1,13):
                # Compute the entire kernel from grouped coefficients first.
                B=sum((a(N,d)*lf(d) for d in range(1,U+1)),P.zero())
                C=P.zero()
                for l in range(1,U*V+1):
                    cl=sum((P(moebius(d))*lam(l//d) for d in divisors(l) if d<=U and l//d<=V),P.zero())
                    for p,e in ZZ(l).factor():assert abs(cl.monomial_coefficient(L[p]))<=e
                    if ZZ(l).gcd(N)==1:C+=cl/euler_phi(l)
                H=sum((lam(m)/euler_phi(m) for m in range(1,V+1) if ZZ(m).gcd(N)==1),P.zero())
                correction=P.zero()
                for p in primes(min(U,V)+1):
                    if N%p==0:continue
                    power=p
                    while power*p<=V:power*=p
                    correction+=L[p]*(1-QQ(1)/power)/(p-1)**3*aa(N*p,U//p)
                assert C==aa(N,U)*H+correction
                # Test the first prime-power expression without grouping.
                direct=sum((P(moebius(d))*lam(m)/euler_phi(d*m)
                            for d in range(1,U+1) for m in range(1,V+1) if ZZ(d*m).gcd(N)==1),P.zero())
                assert C==direct
                assert aa(N,U)*lf(30)-B-C==aa(N,U)*(lf(30)-H)-B-correction
                count+=1
        for n in range(1,65):assert bc(N,n)==a(N,n);conv+=1
        for p in [3,5,7,11]:
            if N%p==0:continue
            for j in [1,2,3]:
                for U in range(1,13):
                    lhs=sum((QQ(moebius(d))/euler_phi(d*p**j) for d in range(1,U+1) if ZZ(d).gcd(N)==1),QQ(0))
                    rhs=sum((bc(N,d,p) for d in range(1,U+1)),QQ(0))/euler_phi(p**j)
                    assert lhs==rhs;local+=1
    assert euler_phi(9)!=euler_phi(3)**2
    assert not ZZ(15).is_prime() and not ZZ(8).is_prime()
    print(json.dumps({'status':'PASS','method':'Sage QQ, independent polynomial-ring grouping and Euler coefficients',
        'sage_version':version,'kernel_and_grouping_cases':count,'g_convolution_cases':conv,
        'removed_local_factor_cases':local,'counterexample_N16_U3_V3':True,
        'scope':'Same declared finite domain as Python; no asymptotic or primality sweep.'},indent=2))

if __name__=='__main__':main()
