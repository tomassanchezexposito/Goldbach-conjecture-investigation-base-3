"""Exact, dependency-free reference calculations for the three-case statement.

These finite calculations are NOT evidence of a universal proof.
"""
from math import isqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def is_composite(n: int) -> bool:
    return n > 1 and not is_prime(n)


def in_residual_set(n: int) -> bool:
    """N is even >=4, with both N-1 and N/2 composite."""
    return n >= 4 and n % 2 == 0 and is_composite(n - 1) and is_composite(n // 2)


def distinct_prime_pairs(n: int) -> list[tuple[int, int]]:
    """List distinct unordered (p,q), p<q, p+q=n, p and q prime."""
    if n < 8 or n % 2:
        return []
    return [
        (p, n - p)
        for p in range(3, n // 2, 2)
        if is_prime(p) and is_prime(n - p)
    ]


def reflection_index_pairs(n: int) -> list[tuple[int, int]]:
    """Indices (a,b) with 3+2a < 3+2b and (3+2a)+(3+2b)=n.

    Includes composite endpoints: this is a positional identity, not a prime test.
    """
    if n < 8 or n % 2:
        return []
    t = n // 2 - 3
    return [(a, t - a) for a in range((t + 1) // 2) if a < t - a]


def representations(n: int) -> dict[str, object]:
    """Classify all three allowed mechanisms for one even integer."""
    if n <= 2 or n % 2:
        raise ValueError("Expected an even integer N > 2")
    return {
        "prime_plus_one": is_prime(n - 1),
        "double_prime": is_prime(n // 2),
        "distinct_prime_pairs": distinct_prime_pairs(n),
    }


def covers(n: int) -> bool:
    result = representations(n)
    return bool(
        result["prime_plus_one"]
        or result["double_prime"]
        or result["distinct_prime_pairs"]
    )


def wheel_210_admissible_classes(n: int) -> int:
    """Count odd residues r (mod 210) with gcd(r,210)=gcd(n-r,210)=1.

    For even n this equals the product of local factors for primes 3,5,7.
    """
    if n % 2:
        raise ValueError("Expected an even integer")
    result = 1
    for ell in (3, 5, 7):
        result *= ell - 1 if n % ell == 0 else ell - 2
    return result
