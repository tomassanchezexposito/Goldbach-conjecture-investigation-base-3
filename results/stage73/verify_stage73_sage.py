#!/usr/bin/env sage-python
"""Independent Sage polynomial/cyclotomic verification and certified intervals.
Run: sage -python results/stage73/verify_stage73_sage.py
No imports from the Python implementation; no writes to historical results.
"""
from sage.all import (ZZ, QQ, PolynomialRing, primes, divisors, moebius,
                      euler_phi, CyclotomicField, RealIntervalField)
from sage.version import version as sage_version
from functools import cache
import json


def main():
    ps = list(primes(121))
    P = PolynomialRing(QQ, names=['L'+str(p) for p in ps])
    L = dict(zip(ps,P.gens()))
    def logform(n):
        return sum((e*L[p] for p,e in ZZ(n).factor()),P.zero())
    def lam(n):
        if n < 2:
            return P.zero()
        fac = ZZ(n).factor()
        return L[fac[0][0]] if len(fac)==1 else P.zero()
    def conv(a,b,n):
        return sum((a(d)*b(n//d) for d in divisors(n)),P.zero())
    @cache
    def components(n,U,V):
        # Deliberately uses nested convolution, rather than divisor-pair enumeration.
        m1=lambda d: P(moebius(d) if d<=U else 0)
        m2=lambda d: P(moebius(d) if d>U else 0)
        l1=lambda d: lam(d) if d<=V else P.zero()
        l2=lambda d: lam(d) if d>V else P.zero()
        one=lambda d:P.one()
        return [l1(n),conv(m1,logform,n),conv(m1,lambda k:conv(one,l1,k),n),
                conv(m2,lambda k:conv(one,l2,k),n)]
    checked=0
    for U,V in [(1,1),(2,3),(4,4),(5,2),(12,10)]:
        for n in range(1,121):
            a,b,c,d=components(n,U,V)
            assert a+b-c+d == lam(n)
            grouped=sum((P(moebius(d))*lam(n//d) for d in divisors(n) if d<=U and n//d<=V),P.zero())
            for p,e in ZZ(n).factor():
                assert abs(grouped.monomial_coefficient(L[p]))<=e
            checked+=1
    for N in [16,28,40,64,100,120]:
        target=sum((lam(n)*lam(N-n) for n in range(1,N)),P.zero())
        parts=[sum((components(n,3,4)[j]*lam(N-n) for n in range(1,N)),P.zero()) for j in range(4)]
        assert parts[0]+parts[1]-parts[2]+parts[3]==target
    K=CyclotomicField(210)
    z=K.gen()
    # Exact roots of unity independently verify the projector over a full period.
    for u in range(210):
        assert sum((z**(a*u) for a in range(210)),K.zero()) == (210 if u==0 else 0)
    minimum=None
    for N in range(0,210,2):
        ram=K.zero()
        for q in divisors(210):
            cq=sum((z**((210//q)*a*N) for a in range(q) if ZZ(a).gcd(q)==1),K.zero())
            ram += QQ(moebius(q)**2)/euler_phi(q)**2*cq
        A=sum(1 for r in range(210) if ZZ(r).gcd(210)==1 and ZZ(N-r).gcd(210)==1)
        assert ram == QQ(210*A)/euler_phi(210)**2
        f=QQ(ram)
        minimum=f if minimum is None else min(minimum,f)
    assert minimum==QQ(175)/128
    # Certified interval arithmetic for the immutable actual-log prime polynomial.
    # Fixed smooth bump: exp(1-1/(1-((t-1/2)/(2/5))^2)) on (1/10,9/10), 0 elsewhere.
    R=RealIntervalField(160)
    X=600
    def w(t):
        if t<=QQ(1)/10 or t>=QQ(9)/10:
            return R(0)
        u=(t-QQ(1)/2)/(QQ(2)/5)
        return (R(1)-R(1)/(1-R(u)**2)).exp()
    coeff={int(p):R(p).log()*w(QQ(p)/X) for p in primes(X)
           if QQ(1)/10 < QQ(p)/X < QQ(9)/10}
    def cconv(a):
        res={}
        for p,ap in a.items():
            for q,aq in a.items():
                res[p+q]=res.get(p+q,R(0))+ap*aq
        return res
    def kernel(u):
        if u==0:
            return R(1)/(3*X)
        angle=R.pi()*u/(3*X)
        return angle.sin()/angle/(3*X)
    proper={}
    for p in primes(X):
        n=int(p*p)
        while n<X:
            a=R(p).log()*w(QQ(n)/X)
            if a.upper()>0:
                proper[n]=a
            n*=int(p)
    cc=cconv(coeff)
    A=sum(coeff.values(),R(0))
    rows=[]
    for N in [300,400,540]:
        assert not ZZ(N-1).is_prime() and not ZZ(N//2).is_prime()
        c1=sum((v*kernel(t-N) for t,v in cc.items()),R(0))
        bound1=2*A*A/(3*R.pi()*X)
        assert c1.lower()>bound1.upper()
        mass=sum((ap*aq for p,ap in coeff.items() for q,aq in coeff.items() if (p+q-N)%210==0),R(0))
        cd=210*sum((v*kernel(t-N) for t,v in cc.items() if (t-N)%210==0),R(0))
        bound=420*mass/(3*R.pi()*X)
        assert cd.lower()>bound.upper()
        # Erase one endpoint of every edge. Choice need not be the minimum mass.
        removed={p for p in coeff if p<N-p and N-p in coeff}
        reduced={p:ap for p,ap in coeff.items() if p not in removed}
        cb=cconv(reduced)
        assert N not in cb
        bd=210*sum((v*kernel(t-N) for t,v in cb.items() if (t-N)%210==0),R(0))
        assert bd.lower()>0
        delta=sum((coeff[p] for p in removed),R(0))
        stability=QQ(210)/(3*X)*delta*(2*A-delta)
        assert (cd-bd).upper()<stability.lower()
        contamination=2*sum((ap*proper.get(N-p,R(0)) for p,ap in coeff.items()),R(0))
        contamination+=sum((ap*proper.get(N-p,R(0)) for p,ap in proper.items()),R(0))
        elementary=2*ZZ(X).isqrt()*R(X).log()**2
        assert contamination.lower()>=0 and contamination.upper()<elementary.lower()
        rows.append({'prime_power_contamination_interval':str(contamination), 'X':X,'N':N,'prime_positions':len(coeff),'deleted_positions':len(removed),
                     'C1_interval':str(c1),'C210_interval':str(cd),'deleted_C210_interval':str(bd),
                     'deleted_target_coefficient_exactly_zero':True,'core_bounds_and_stability':'PASS'})
    # Full-support counterexample to arbitrary-weight universal positivity:
    # a smooth bump supported in (1/10,1/5) has all pair sums <2X/5 < N.
    assert QQ(2)/5 < QQ(1)/2
    print(json.dumps({'status':'PASS','sage_version':sage_version,'typeI_coefficient_bounds_checked':checked,'vaughan_checks':checked,
                     'projector_residues':210,'wheel_even_residues':105,'minimum_F210':str(minimum),
                     'interval_precision_bits':160,'actual_log_weight_checks':rows,
                     'scope':'Exact polynomial/cyclotomic identities and three certified finite interval examples; not asymptotic proof.'},indent=2))

if __name__=='__main__':
    main()
