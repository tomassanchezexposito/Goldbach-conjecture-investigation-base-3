# Research statement and exact notation

## Author's three-case statement (open conjecture)

For every even integer N > 2, at least one of the following holds:

1. **Prime plus one:** N = p + 1, with p prime.
2. **Twice a prime:** N = p + p, with p prime.
3. **Two distinct primes with equidistant doubles:** N = p + q for primes p < q, with N - 2p = 2q - N.

These three cases are not mutually exclusive.

The equidistance condition in case 3 is **algebraically equivalent** to p + q = N. It is not an additional restriction and does not itself establish primality.

## Residual set

Define H as the set of even integers N >= 4 for which both N-1 and N/2 are composite.

For an even N not in H, at least one of the first two cases holds automatically. For N in H, the universal coverage obligation is:

> Prove that there exist distinct primes p < q such that p + q = N, **for every N in H**.

This remains **unproved**. This three-case statement is weaker than the strong Goldbach conjecture because it also permits prime + 1; it is nevertheless closely related to the same unsolved binary prime-correlation problem.

## Coordinates of the original reflected-arrow representation

An odd candidate has the form 3 + 2a, with integer a >= 0. For an even N >= 6, complementary indices satisfy

    a + b = N/2 - 3.

The involution a -> N/2 - 3 - a reflects the indices. Positional symmetry is always true; whether both endpoints are prime is the open arithmetic issue.

The wheel modulo 210 captures congruence admissibility. It is distinct from ternary (base-3 numeral) notation and from an arithmetic progression with common difference 3.

## Representation count

Let R_distinct(N) denote the number of unordered distinct prime pairs p < q with p + q = N. The main goal is to show R_distinct(N) > 0 for every N in H. The project does not claim this has been proved.

## Scope and publication caution

Definitions, conditional theorems, verified computations, and externally published results should be documented separately. A mathematical reformulation can be published as a definition or framework, but novel universal claims require full proofs and independent scrutiny.
