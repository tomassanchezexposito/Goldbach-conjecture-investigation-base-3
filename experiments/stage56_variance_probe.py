"""Stage 56: exact finite diagnostic of the wheel-210 variance criterion.

The outputs are computational observations, NOT a universal Goldbach proof.
This Python 3 script runs unchanged in a SageMath Jupyter kernel.
"""
from fractions import Fraction
from math import gcd, isqrt


def is_prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def in_residual_set(n):
    return (n >= 4 and n % 2 == 0
            and not is_prime(n - 1) and not is_prime(n // 2))


def prime_pairs(n):
    return [(p, n - p) for p in range(3, n // 2, 2)
            if is_prime(p) and is_prime(n - p)]


def wheel_factor(n):
    factor = 1
    for ell in (3, 5, 7):
        factor *= ell - 1 if n % ell == 0 else ell - 2
    return factor


def analyze_block(low, high):
    numbers = [n for n in range(low, high + 1)
               if in_residual_set(n)]
    values = [Fraction(len(prime_pairs(n)), wheel_factor(n))
              for n in numbers]
    k = len(numbers)
    if k < 2:
        raise ValueError("At least two residual even numbers are required")
    mean = sum(values, Fraction(0)) / k
    centered_sum = sum(((v - mean) ** 2 for v in values), Fraction(0))
    threshold = Fraction(k, k - 1) * mean ** 2
    return k, sum(v == 0 for v in values), mean, centered_sum, threshold


assert [len(prime_pairs(n)) for n in (50, 52, 56)] == [4, 3, 3]
assert [wheel_factor(n) for n in (50, 52, 56)] == [20, 15, 18]
for n in (50, 52, 56, 100):
    direct = sum(gcd(a, 210) == 1 and gcd(n - a, 210) == 1
                 for a in range(210))
    assert direct == wheel_factor(n)

n = 100
four_prime_count = sum(
    1 for p in range(3, n // 2, 2)
    for r in range(3, n // 2, 2)
    if all(is_prime(t) for t in (p, n-p, r, n-r))
)
assert four_prime_count == len(prime_pairs(n)) ** 2 == 36

print("N=100: ordered four-prime configurations =", four_prime_count)
for low, high in ((50, 100), (50, 200)):
    k, zeros, mean, variance_sum, threshold = analyze_block(low, high)
    print("Block", low, "to", high, "| K=", k, "| zeros=", zeros)
    print("  mean =", mean, "| variance =", round(float(variance_sum), 6))
    print("  threshold =", round(float(threshold), 6),
          "| criterion passes =", mean > 0 and variance_sum < threshold)

assert analyze_block(50, 100)[1] == 0
assert analyze_block(50, 200)[1] == 0
assert analyze_block(50, 100)[3] < analyze_block(50, 100)[4]
assert analyze_block(50, 200)[3] >= analyze_block(50, 200)[4]
print("All exact finite checks passed.")
