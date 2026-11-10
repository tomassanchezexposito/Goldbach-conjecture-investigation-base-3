# Stage 58 summary

## Established mathematically

- The sharp one-zero and multiple-zero second-moment bounds follow from Cauchy–Schwarz. Their equality cases are attained when all nonzero coordinates are equal.
- For arbitrary positive weights and an unknown zero coordinate, equal weights maximize the worst-coordinate threshold obtainable from only the first two moments.
- Same-target representation products split into the identical-pair diagonal and four-distinct-prime terms. At distinct shifted targets, the product splits into four explicitly described shared-position classes and a four-distinct-prime class; the low/high shared case is impossible for a positive shift.
- The wheel count $A_{210}(N)$ is an exact local residue count. Prime summands 3, 5, and 7 require separate treatment; congruence admissibility does not establish primality.

## Refuted or limited

- The strict Stage 56 variance condition is not automatic on every block: $H\cap[50,150]$ has no zero counts, but its exact variance-to-threshold ratio is $1716160/1568187>1$.
- Positive shifted averages and positive-semidefinite covariance constraints alone do not imply coordinatewise positivity; the exact length-10 cyclic countermodel is recorded in the report and verification output.
- Neither the wheel normalization nor exact four-prime identities provide the missing pointwise estimate.

## Exact finite observations

- SageMath computed 149 same-target even cases, 62 residual anchors through 300, and 620 shifted correlation rows for shifts 1 through 10. No zero representation count occurred among those 62 anchors.
- The wheel formula matched direct enumeration of 210 residues for all 249 even targets through 500.
- A separate Python 3.14.4 verifier using a sieve and rational `Fraction` arithmetic independently checked the same-target identities, all shifted categories, all exceptional-prime counts, and the block moments. It passed all checks.
- Existing Stage 57 and Stage 58 verifiers and all four repository unit tests passed.

These are finite computations, not a proof for all $N\in H$.

## Remaining obligation and next step

Universal positivity remains open. The missing input is an unconditional non-circular pointwise lower bound for $R(N)$, or independent block-moment bounds meeting the sharp zero-exclusion threshold on a covering family of blocks. The next step is to obtain or rule out a concrete analytic estimate for the four-distinct prime quadruple contribution with explicit uniform errors; another finite correlation sweep alone cannot discharge this obligation.
