#!/usr/bin/env python3
"""Exact Stage 74 finite identities using Fraction and sparse formal logarithms.
Print JSON; no file writes or Goldbach sweep. Run with python3 -B.
"""
from fractions import Fraction as F
from collections import defaultdict
from math import gcd
import json


def factor(n):
    out={}
    d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1
            n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out


def mu(n):
    a=factor(n)
    return 0 if any(e>1 for e in a.values()) else (-1)**len(a)


def phi(n):
    v=n
    for p in factor(n):v=v//p*(p-1)
    return v


def A(N,U):return sum((F(mu(d),phi(d)) for d in range(1,U+1) if gcd(d,N)==1),F(0))


def add(v,p,a):v[p]+=a


def clean(v):return {str(p):str(a) for p,a in sorted(v.items()) if a}


def primepowers(V):
    out=[]
    for m in range(2,V+1):
        f=factor(m)
        if len(f)==1:out.append((m,next(iter(f))))
    return out


def Cdirect(N,U,V):
    c=defaultdict(F)
    for d in range(1,U+1):
        for m,p in primepowers(V):
            if gcd(d*m,N)==1:add(c,p,F(mu(d),phi(d*m)))
    return c


def Csplit(N,U,V):
    c=defaultdict(F)
    for m,p in primepowers(V):
        if N%p:add(c,p,A(N,U)/phi(m))
    for p in range(2,min(U,V)+1):
        if factor(p)!={p:1} or N%p==0:continue
        power=1
        while power*p<=V:power*=p
        add(c,p,F(power-1,power*(p-1)**3)*A(N*p,U//p))
    return c


def g(N,n,omit=None):
    ans=F(1)
    for p,j in factor(n).items():
        if p==omit:return F(0)
        ans*=F(1,p**j) if N%p==0 else -F(1,p**j*(p-1))
    return ans


def convmu(N,n,omit=None):
    return sum((F(mu(d),d)*g(N,n//d,omit) for d in range(1,n+1) if n%d==0),F(0))


def main():
    Ns=[2,6,16,28,210,2310,30030,510510]
    kernel=0; convolution=0; removed=0
    for N in Ns:
        for U in range(1,13):
            for V in range(1,13):
                assert clean(Cdirect(N,U,V))==clean(Csplit(N,U,V)),(N,U,V)
                # Independent grouped c_l representation, retaining every gcd.
                grouped=defaultdict(F)
                for l in range(1,U*V+1):
                    cl=defaultdict(int)
                    for d in range(1,U+1):
                        if l%d==0 and l//d<=V:
                            f=factor(l//d)
                            if len(f)==1:add(cl,next(iter(f)),mu(d))
                    for p,v in cl.items():assert abs(v)<=factor(l).get(p,0)
                    if gcd(l,N)==1:
                        for p,v in cl.items():add(grouped,p,F(v,phi(l)))
                assert clean(grouped)==clean(Cdirect(N,U,V))
                kernel+=1
        for n in range(1,65):
            expect=F(mu(n),phi(n)) if gcd(n,N)==1 else F(0)
            assert convmu(N,n)==expect
            convolution+=1
        for p in [3,5,7,11]:
            if N%p==0:continue
            for j in [1,2,3]:
                for U in range(1,13):
                    lhs=sum((F(mu(d),phi(d*p**j)) for d in range(1,U+1) if gcd(d,N)==1),F(0))
                    rhs=sum((convmu(N,d,omit=p) for d in range(1,U+1)),F(0))/phi(p**j)
                    assert lhs==rhs,(N,p,j,U)
                    removed+=1
    # Boundary counterexample with residual N=16 and the first permitted shared prime 3.
    correct=Cdirect(16,3,3)
    naive=defaultdict(F)
    for m,p in primepowers(3):
        if 16%p:add(naive,p,A(16,3)/phi(m))
    assert correct[3]==F(1,3) and naive[3]==F(1,4)
    assert phi(9)==6 and phi(3)*phi(3)==4
    assert not mu(4) and phi(1)==1 and A(16,1)==1
    # Nonreduced-class prime-power bookkeeping, exact integer inequalities.
    power_checks=0
    for X in [16,32,64]:
        for p in [2,3,5,7]:
            n=1;k=0
            while n*p<=X:n*=p;k+=1
            assert n<=X<n*p
            power_checks+=1
    print(json.dumps({'status':'PASS','method':'Fraction, trial factorization, sparse formal logarithms',
        'parameters':{'N':Ns,'U':[1,12],'V':[1,12],'convolution_n':[1,64]},
        'kernel_and_grouping_cases':kernel,'g_convolution_cases':convolution,'removed_local_factor_cases':removed,
        'nonreduced_power_boundary_cases':power_checks,
        'exact_counterexample':{'N':16,'U':3,'V':3,'C_coefficient_of_log3':str(correct[3]),
          'naive_C_coefficient_of_log3':str(naive[3]),'difference':'1/12','phi9':6,'phi3_squared':4},
        'scope':'Finite algebra only; no check or proof of asymptotic rates or Goldbach.'},indent=2))

if __name__=='__main__':main()
