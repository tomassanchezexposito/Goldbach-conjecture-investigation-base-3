#!/usr/bin/env python3
"""Exact regression: S(alpha)^2 counts prime sums, |S(alpha)|^2 counts differences.

Two independent algorithms: direct integer convolution and finite-field DFT,
using a primitive 16th root of unity in GF(97). No floating arithmetic.
"""
import json
from pathlib import Path

PRIMES = (3, 5)
L = 16
MOD = 97


def primitive_root(p):
    for g in range(2,p):
        if pow(g,(p-1)//2,p)!=1 and pow(g,(p-1)//3,p)!=1:
            return g
    raise AssertionError("primitive root missing")


def direct_coefficient(k, kind):
    if kind == "sum":
        return sum(p+q==k for p in PRIMES for q in PRIMES)
    if kind == "difference":
        return sum(p-q==k for p in PRIMES for q in PRIMES)


def main():
    root = pow(primitive_root(MOD),(MOD-1)//L,MOD)
    assert pow(root,L,MOD)==1
    assert all(pow(root,j,MOD)!=1 for j in range(1,L))
    invL = pow(L,-1,MOD)

    freq = [sum(pow(root,p*j,MOD) for p in PRIMES)%MOD for j in range(L)]
    result = []
    for k in range(L):
        sum_dft = invL*sum(
            pow(freq[j],2,MOD)*pow(root,(-j*k)%L,MOD)
            for j in range(L))%MOD
        diff_dft = invL*sum(
            freq[j]*freq[(-j)%L]*pow(root,(-j*k)%L,MOD)
            for j in range(L))%MOD

        sum_direct = sum(direct_coefficient(k+t*L,"sum") for t in range(0,2))
        diff_direct = sum(direct_coefficient(k+t*L,"difference") for t in (-1,0,1))
        assert sum_dft==sum_direct%MOD, (k,sum_dft,sum_direct)
        assert diff_dft==diff_direct%MOD, (k,diff_dft,diff_direct)
        result.append({"k":k,"sum":sum_direct,"difference":diff_direct})
    assert result[8] == {"k":8,"sum":2,"difference":0}

    output={
        "status":"FINITE EXACT REGRESSION CHECK, NOT A GOLDBACH PROOF",
        "primes":list(PRIMES),"DFT_length":L,"prime_modulus":MOD,
        "primitive_root":root,"coefficients":result,
        "N8_sum":result[8]["sum"],"N8_difference":result[8]["difference"],
        "independent_methods":["direct integer ordered-pair enumeration",
                               "finite-field DFT/inverse DFT"],
        "assertions_passed":True
    }
    out=Path(__file__).with_name("sum_difference_exact.json")
    out.write_text(json.dumps(output,indent=2)+"\n",encoding="utf-8")
    print("PASS: N=8 prime sum coefficient 2, prime difference coefficient 0")
    print("PASS: all 16 frequencies agree with exact independent DFT")
    print("Recorded",out)


if __name__=="__main__":
    main()
