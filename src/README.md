# Computational sources

The file prime_reflections.py provides a small, exact Python reference implementation for:

- Primality by deterministic trial division.
- The author's three allowed representations.
- The residual set H.
- Index reflection on the progression 3 + 2a.
- The number of wheel-210 admissible residue classes.

Run the reference checks from the repository root using:

    python -m unittest discover -s tests -v

The implementation is intended for small exact checks and baseline correctness, **not** for large-scale prime counting or a proof of universal coverage. Future SageMath/C++ methods should be compared against this baseline on overlapping domains.
