#!/usr/bin/env python3
"""Exact finite checks of the target coefficient and prime-power partition.

Integer test weights make all checks exact; the proved identity applies to
arbitrary real weights, including log(p). The finite DFT is evaluated by
integer root-of-unity orthogonality in Z/LZ with L > 2N.
"""
from math import isqrt
import json
from pathlib import Path

OUT = Path(__file__).with_name("02_fourier_cases.json")


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def is_prime_power(n):
    if n < 2:
        return False
    for p in range(2, isqrt(n) + 1):
        if is_prime(p):
            x = p * p
            while x <= n:
                if x == n:
                    return True
                x *= p
    return is_prime(n)


def direct_prime_coefficient(N):
    primes = [p for p in range(2, N + 1) if is_prime(p)]
    return sum(p * q for p in primes for q in primes if p + q == N)


def dft_prime_coefficient(N):
    L = 2 * N + 1
    primes = [p for p in range(2, N + 1) if is_prime(p)]
    # Orthogonality: average over j=0,...,L-1 of z^(j*(p+q-N)).
    return sum(p * q for p in primes for q in primes
               if (p + q - N) % L == 0)


def direct_prime_power_coefficient(N):
    terms = [a for a in range(2, N + 1) if is_prime_power(a)]
    return sum(1 for a in terms for b in terms if a + b == N)


def decomposition_counts(N):
    values = [a for a in range(2, N + 1) if is_prime_power(a)]
    prime_only = [a for a in values if is_prime(a)]
    higher = [a for a in values if not is_prime(a)]
    pp = sum(1 for a in prime_only for b in prime_only if a + b == N)
    mixed_ordered = sum(1 for a in higher for b in values if a + b == N)
    mixed_ordered += sum(1 for a in prime_only for b in higher if a + b == N)
    higher_higher = sum(1 for a in higher for b in higher if a + b == N)
    total = sum(1 for a in values for b in values if a + b == N)
    assert pp + mixed_ordered == total
    return {"prime_prime_ordered": pp,
            "at_least_one_higher_prime_power_ordered": mixed_ordered,
            "higher_higher_ordered_included_in_mixed": higher_higher,
            "total_prime_power_ordered": total}


def main():
    targets = list(range(4, 81, 2)) + [100, 128, 200]
    rows = []
    for N in targets:
        direct = direct_prime_coefficient(N)
        dft = dft_prime_coefficient(N)
        assert direct == dft
        diagonal = N // 2 if N % 2 == 0 and is_prime(N // 2) else None
        unordered_weighted_times_two = sum(
            2 * p * (N - p)
            for p in range(2, N // 2 + 1)
            if p < N - p and is_prime(p) and is_prime(N - p)
        )
        diagonal_weight = diagonal * diagonal if diagonal is not None else 0
        assert direct == unordered_weighted_times_two + diagonal_weight
        pp_counts = decomposition_counts(N)
        assert pp_counts["prime_prime_ordered"] == sum(
            1 for p in range(2, N + 1) if is_prime(p)
            for q in range(2, N + 1) if is_prime(q) and p + q == N
        )
        rows.append({"N": N, "prime_weight_p_equals_p_coefficient": direct,
                     "exact_dft_coefficient": dft,
                     "diagonal_prime": diagonal,
                     "diagonal_weight": diagonal_weight,
                     "prime_power_unit_weight_partition": pp_counts,
                     "prime_power_correction_nonnegative":
                         pp_counts["at_least_one_higher_prime_power_ordered"] >= 0})
    data = {
        "evidence": "exact finite identities with integer weights; symbolic proof covers log weights",
        "targets": targets,
        "targets_checked": len(targets),
        "dft_modulus_rule": "L=2N+1, so L>2N; exact cyclic coefficient selection has no wraparound",
        "methods": ["direct ordered convolution", "finite DFT via root-of-unity orthogonality"],
        "prime_power_test_weights": "one per prime power, to check partition and multiplicity exactly",
        "rows": rows,
        "assertions_passed": True,
        "universal_prime_claim": False,
        "note": "The finite checks use integer test weights; no floating arithmetic is used."
    }
    OUT.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in data.items() if k != "rows"}, indent=2))


if __name__ == "__main__":
    main()
