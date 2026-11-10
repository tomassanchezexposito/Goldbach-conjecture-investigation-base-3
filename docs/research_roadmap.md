# Research roadmap and proof obligations

## Completed foundational tasks (algebraic)

- State the three allowed representations precisely.
- Identify the residual set H, where both elementary alternatives fail.
- Translate reflected arrows into exact coordinates 3 + 2a and a + b = N/2 - 3.
- Define an integer-valued representation count and the local wheel factor C_210(N).
- Construct exact finite test algorithms with independent regression checks.

These completed items do **not** demonstrate universal coverage.

## Priority: pointwise second-moment feasibility audit

For even N, let R_distinct(N) count unordered pairs of distinct primes p < q with p + q = N. Let

    x_N = R_distinct(N) / C_210(N),

where C_210(N) > 0 is the number of admissible residue pairs modulo 210.

For a finite block B of K >= 2 even integers in the residual set H, define the average mu_B and the centered sum of squares V_B of x_N. The deterministic inequality

    mu_B > 0 and V_B < K * mu_B^2 / (K-1)

forces every x_N in B to be positive.

This is only a sufficient **criterion**. We have no proof that it holds for every block, and it may be too demanding for the true fluctuations of prime correlations.

### Next analytical milestones

1. Express the second moment using four genuine prime indicators, keeping the exact reflected sum constraint.
2. Separate diagonal, local-factor, and off-diagonal contributions without assuming the existence of any target prime pair.
3. Test whether the proposed variance threshold is compatible with known analytic bounds and plausible fluctuations; discard it as a universal criterion if a counterexample appears.
4. Seek a **pointwise unilateral lower bound**, rather than replacing the unresolved pointwise claim with an average.
5. Reconcile any new estimate with the singular series, local congruence factors, and the parity barrier in sieve theory.
6. Obtain rigorous effective constants or thresholds if any argument purports to handle every sufficiently large N.
7. Handle the finite range separately only after a valid analytic threshold has been proved.

## Acceptance conditions for a universal solution

A complete proof must cover **every N in H** with the correct quantifiers and without circular use of prime-pair existence. Verify the proof independently; only then consider Lean formalization and publication of the universal theorem.

## Current status

**Open.** No pointwise estimate currently established in this repository guarantees R_distinct(N) > 0 for every N in H.
