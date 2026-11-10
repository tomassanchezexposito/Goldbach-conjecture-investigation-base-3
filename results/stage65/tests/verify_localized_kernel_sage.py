#!/usr/bin/env sage -python
"""Independent SageMath finite-field DFT audit of Stage 65 localization.

Run with: sage -python results/stage65/tests/verify_localized_kernel_sage.py
"""
import json
from pathlib import Path

from sage.all import Integers, ZZ
from sage.version import version as sage_version


def primitive_root(p):
    g = ZZ(2)
    while g < p:
        if all(pow(g, (p-1)//q, p) != 1 for q in (2, 3)):
            return g
        g += 1
    raise AssertionError("primitive root not found")


def main():
    L, p = 32, 97
    F = Integers(p)
    g = primitive_root(p)
    zeta = F(g) ** ((p-1)//L)
    assert zeta**L == 1 and all(zeta**j != 1 for j in range(1, L))
    invL = F(L)**(-1)
    c = [ZZ((7*n*n + 5*n + 13) % 101) for n in range(L)]
    lam = {-4: ZZ(3), -2: ZZ(-5), 0: ZZ(7), 1: ZZ(11), 3: ZZ(-2)}
    N = 9
    direct = sum(ZZ(lam[h])*c[(N+h) % L] for h in lam)

    samples_f, samples_k = [], []
    for j in range(L):
        samples_f.append(sum(F(c[n])*zeta**(j*n) for n in range(L)))
        samples_k.append(sum(F(lam[h])*zeta**(-j*h) for h in lam))
    inverse_product_coefficient = invL * sum(
        samples_f[j]*samples_k[j]*zeta**(-j*N) for j in range(L)
    )
    assert inverse_product_coefficient == F(direct)

    # Parseval for K_lambda is checked as a separate finite-field identity.
    k_l2 = sum(ZZ(lam[h])**2 for h in lam)
    dft_parseval = invL * sum(samples_k[j]*samples_k[(-j) % L] for j in range(L))
    assert dft_parseval == F(k_l2)

    fejer = []
    for H in range(17):
        weights = [ZZ(H+1-abs(h)) for h in range(-H, H+1)]
        numerator = sum(x*x for x in weights)
        # The displayed closed form is rational; compare after clearing 3.
        assert 3*numerator == 2*H**3 + 6*H**2 + 7*H + 3
        fejer.append({"H": int(H), "unnormalized_l2_numerator": int(numerator)})

    out_data = {
        "classification": "INDEPENDENT SAGEMATH FINITE-FIELD DFT CHECK",
        "sage_version": str(sage_version),
        "DFT_length": int(L),
        "prime_modulus": int(p),
        "primitive_root": int(g),
        "root_of_unity": int(zeta),
        "target_N": int(N),
        "direct_shift_sum": int(direct),
        "DFT_product_coefficient_mod_p": int(inverse_product_coefficient),
        "lambda_l2_squared": int(k_l2),
        "DFT_parseval_lhs": int(dft_parseval),
        "fejer_norm_rows": fejer,
        "assertions_passed": True,
        "limits": [
            "Finite-field DFT checks verify finite coefficient algebra modulo p.",
            "They do not estimate a genuine-prime minor-arc coefficient.",
        ],
    }
    out = Path(__file__).with_name("localized_kernel_sage_results.json")
    out.write_text(json.dumps(out_data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out_data, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
