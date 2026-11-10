"""Finite regression tests; passing these does not prove universal coverage."""
import unittest
from math import gcd

from src.prime_reflections import (
    covers,
    distinct_prime_pairs,
    in_residual_set,
    is_prime,
    reflection_index_pairs,
    representations,
    wheel_210_admissible_classes,
)


class PrimeReflectionTests(unittest.TestCase):
    def test_prime_basics(self):
        self.assertEqual([n for n in range(2, 20) if is_prime(n)],
                         [2, 3, 5, 7, 11, 13, 17, 19])

    def test_three_cases(self):
        self.assertTrue(representations(4)["prime_plus_one"])
        self.assertTrue(representations(6)["prime_plus_one"])
        self.assertTrue(representations(6)["double_prime"])
        self.assertTrue(in_residual_set(56))
        self.assertIn((3, 53), distinct_prime_pairs(56))
        self.assertTrue(covers(56))
        self.assertFalse(in_residual_set(14))

    def test_reflections_match_enumeration(self):
        for n in range(8, 120, 2):
            pair_set = set(distinct_prime_pairs(n))
            by_indices = {
                (3 + 2*a, 3 + 2*b)
                for a,b in reflection_index_pairs(n)
                if is_prime(3 + 2*a) and is_prime(3 + 2*b)
            }
            self.assertEqual(pair_set, by_indices)

    def test_wheel_classes_exact(self):
        for n in range(4, 420, 2):
            brute = sum(gcd(r, 210) == 1 and gcd(n-r, 210) == 1
                        for r in range(210))
            self.assertEqual(wheel_210_admissible_classes(n), brute)


if __name__ == "__main__":
    unittest.main()
