#!/usr/bin/env python3
"""Exact Stage 70 checks, Python standard library; no Goldbach proof."""
import json
from collections import Counter
from fractions import Fraction as F
from math import isqrt

M=(0,1,5,6,7,11)
assert Counter(t%6 for t in M)=={0:2,1:2,5:2}
assert sum((-1)**t for t in M)==-2
# Frequency 2 character: two copies of (1 + zeta6 + zeta6^-1)=2*2.
b2=F(4,12)
b6=F(-2,12)
free=b2*b2+b6*b6
positive=b2*b2
assert (free,positive)==(F(5,36),F(1,9))
assert F(1)/positive==9 and F(1)/free==F(36,5)
assert 3*b2==1 and (3*3)==9

def prime(n):
    return n>1 and all(n%d for d in range(2,isqrt(n)+1))
def residual(n):
    return n>=4 and n%2==0 and not prime(n-1) and not prime(n//2)
def conv(weights):
    result={}
    for p,wp in weights.items():
        for q,wq in weights.items():
            result[p+q]=result.get(p+q,0)+wp*wq
    return result

P=[p for p in range(3,201,2) if prime(p)]
weights={p:p+(p%7)**2 for p in P}
full=conv(weights)
full_energy=sum(x*x for x in full.values())
items=[]
for n in (50,100,120,256,300):
    assert residual(n) and full.get(n,0)>0
    kept={}
    seen=set()
    for p in P:
        if p in seen: continue
        q=n-p
        if q in weights:
            assert q!=p
            k=p if weights[p]>=weights[q] else q
            kept[k]=weights[k]
            seen.update((p,q))
        else:
            kept[p]=weights[p]
            seen.add(p)
    pruned=conv(kept)
    assert pruned.get(n,0)==0
    assert 2*sum(kept.values())>=sum(weights.values())
    assert sum(x*x for x in pruned.values())<=full_energy
    assert all(pruned.get(k,0)<=v for k,v in full.items())
    items.append({'N':n,'original':full[n],'pruned':0,
      'kept_weight':sum(kept.values()),'all_weight':sum(weights.values())})

result={'status':'PASS','theorem_scope':'abstract positive Fourier cone and prime-support pruning; not Goldbach',
 'cyclic_model':{'group_size':12,'positive_major_coefficient':1,
 'unrestricted_minimum_full_energy':'36/5','nonnegative_spectrum_minimum_full_energy':'9'},
 'pruned_prime_support':{'max_prime':200,'number_of_primes':len(P),'weights':'p+(p mod 7)^2',
 'targets':items,'all_assertions_passed':True}}
print(json.dumps(result,indent=2))
