"""Independent SageMath check of Stage 64 finite arithmetic examples.

Run with: sage -python results/stage64/tests/verify_stage64_sage.py
"""
import json
from pathlib import Path

from sage.all import Integers, ZZ, gcd, is_prime, prod
from sage.version import version as sage_version


def sage_representations(n):
    return {
        (ZZ(p), ZZ(n - p))
        for p in range(2, n // 2 + 1)
        if p < n - p and is_prime(p) and is_prime(n - p)
    }


def main():
    M = ZZ(210)
    wheel_direct = sum(
        1
        for a in range(M)
        if gcd(a, M) == 1 and gcd(ZZ(0) - a, M) == 1
    )
    wheel_local = prod(ZZ(p - 1) for p in (2, 3, 5, 7))
    assert wheel_direct == wheel_local == 48

    residual = {}
    for n in (210, 420):
        residual[n] = (
            n >= 4
            and n % 2 == 0
            and ZZ(n - 1) > 1
            and not is_prime(n - 1)
            and ZZ(n // 2) > 1
            and not is_prime(n // 2)
        )
    assert residual == {210: True, 420: False}
    assert list(ZZ(209).factor()) == [(ZZ(11), 1), (ZZ(19), 1)]
    assert list(ZZ(105).factor()) == [(ZZ(3), 1), (ZZ(5), 1), (ZZ(7), 1)]
    assert is_prime(419)

    targets = (50, 68, 100, 112)
    rows = []
    for i, n in enumerate(targets):
        for m in targets[i + 1 :]:
            rn, rm = sage_representations(n), sage_representations(m)
            shared = sum(bool(set(a) & set(b)) for a in rn for b in rm)
            disjoint = sum(not (set(a) & set(b)) for a in rn for b in rm)
            shared_direct = sum(
                1
                for x in range(2, min(n, m) + 1)
                if is_prime(x)
                and is_prime(n - x)
                and is_prime(m - x)
                and x != n - x
                and x != m - x
            )
            assert len(rn) * len(rm) == shared + disjoint
            assert shared == shared_direct
            rows.append(
                {
                    "n": int(n),
                    "m": int(m),
                    "R_n": len(rn),
                    "R_m": len(rm),
                    "shared": shared,
                    "four_distinct": disjoint,
                    "product": len(rn) * len(rm),
                    "representations_n": sorted([list(map(int, x)) for x in rn]),
                    "representations_m": sorted([list(map(int, x)) for x in rm]),
                }
            )

    odd_primes = [p for p in (3, 5, 7) if 210 % p == 0]
    finite_factor = prod(ZZ(p - 1) / ZZ(p - 2) for p in odd_primes)
    finite_factor_420 = prod(
        ZZ(p - 1) / ZZ(p - 2) for p in (3, 5, 7) if 420 % p == 0
    )
    assert finite_factor == finite_factor_420

    result = {
        "classification": "INDEPENDENT_SAGEMATH_FINITE_CHECK",
        "sage_version": str(sage_version),
        "wheel_210_direct": int(wheel_direct),
        "wheel_210_local_product": int(wheel_local),
        "residual_status": {str(k): bool(v) for k, v in residual.items()},
        "factorizations": {"209": str(ZZ(209).factor()), "105": str(ZZ(105).factor())},
        "singular_series_common_odd_factor": str(finite_factor),
        "four_prime_partition_checks": rows,
        "limits": [
            "SageMath primality and factorization form an independent implementation path.",
            "Finite checks verify only these examples and exact identities.",
        ],
    }
    out = Path(__file__).with_name("stage64_sage_results.json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
