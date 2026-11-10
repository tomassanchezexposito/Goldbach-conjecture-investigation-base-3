# NEXT TASK — Stage 61: signed true-prime correlations with a non-circular pointwise error

**State: OPEN.** This branch is created from the published Stage 60 integration branch. Do not merge into main or claim universal coverage.

## Provenance to audit before new work

- Stage 60 integrated branch: \`cocalc/stage60-integrated-research\`.
- Stage 60 report: \`results/stage60/report.md\`; independent checks: \`results/stage60/compute_stage60.py\` and \`results/stage60/verify_stage60.py\`.
- Stage 60 draft PR #9: https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/pull/9
- Coordination issue #8: https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/issues/8
- Stage 58 weighted moment supplement and both Stage 59 local path/cycle/graph lines are preserved in the integrated branch.

CoCalc's SSH deploy key works for Git fetch and push. The private issue #8 was not readable by \`gh\` (not installed) or unauthenticated REST (HTTP 404); this **does not** imply the issue is missing. Read the checked-in \`docs/stage60_integration_handoff.md\` and \`results/stage60/integration_review.md\` for the mirrored task context. Do not print private key material or require a new token just to read issue #8.

## Core mathematical objective

For every even N in the author's residual set H (N>=4, N-1 composite and N/2 composite), seek a non-circular rigorous pointwise proof that R(N)>0, where R counts unordered distinct genuine-prime pairs p<q, p+q=N.

Let A(N) be the exact modulo-210 admissible residue count and X_N=R(N)/A(N). In the three-even-target path, use
\[
a=X_{N-2},\quad b=X_N,\quad c=X_{N+2},\quad
\mu=(a+b+c)/3,\quad E=(a-b)^2+(b-c)^2.
\]
The proved deterministic implication is
\[
\mu^2>\frac29 E \Longrightarrow b>0.
\]
**The arithmetic implication at all targets remains OPEN**; this condition must be proved from independent prime-distribution information, not assumed.

## Stage 61 research obligations

1. **Logical no-go lemma.** Show explicitly that wheel-210 admissibility and Stage 60's upper bounds \`0<=R(n)<=B(n)=floor((n-4)/4)\` cannot exclude a zero center: for any sufficiently large even N, the abstract admissible nonnegative counts \`R(N-2)=1\`, \`R(N)=0\`, \`R(N+2)=1\` satisfy all these upper bounds. For \`b=0\`,
\[
\mu^2-\frac29E=-\frac{(a-c)^2}{9}\le0.
\]
This is a countermodel to deduction from candidate bounds alone, not a claimed counterexample to actual Goldbach.
2. **Target-index precision.** Correct the ambiguous assertion in Stage 60: a genuine \`Q_4(N,M)>0\` necessarily entails \`R(N)>0\` and \`R(M)>0\` by definition; an off-center \`Q_4(N-2,N+2)>0\` does not entail a representation at N. A non-circular positive lower estimate for \`Q_4(N,M)\` would be strong enough but is not available merely from the identity.
3. **Signed decomposition.** Derive the exact identity for the signed difference \`D_N=\mu^2-(2/9)E\` with all coefficients of \`R(t)^2\`, \`R(s)R(t)\`, exact wheel factors, same-target diagonals, shared-prime contractions and four-distinct configurations. Check expansions independently in exact rational arithmetic.
4. **Analyze the critical cancellation.** Identify which signed four-prime terms would have to dominate which negative terms for each N, and formulate an explicit uniform inequality with quantified error and an effective threshold. Do not simply assume a positive R(N) or a positive anchored product.
5. **Literature and methods.** Compare genuine prime-only circle-method or sieve results, including the parity obstruction and published exceptional-set bounds. Cite original papers with accurate hypotheses and distinguish average/exceptional-set/conditional/pointwise estimates. Do not claim that published results already give strict pointwise positivity for all N.
6. **Independent computation.** Compute only focused exact test cases and counterexamples to *new* inequalities (not another vast Goldbach search). Use two independent routines, document ranges, exact outputs, and runtime.
7. **Outcome.** Either supply a rigorously proved non-circular bound on signed four-prime correlations valid for every sufficiently large residual N, with explicit constants and a verified finite cutoff, or state exactly the first missing arithmetic estimate and why the existing unconditional estimates fail to imply it.
8. **Delivery.** Save English mathematical report, source, independent verifier, exact output and SHA-256 manifest under \`results/stage61/\`. Commit and push solely to \`cocalc/stage61-signed-correlation-gap\`, and open a draft PR; do not overwrite previous stages, modify main, install software or incur costs without approval.

## Evidence labels required

PROVED MATHEMATICAL LEMMA; ESTABLISHED EXTERNAL THEOREM; FINITE COMPUTATIONAL OBSERVATION; REFUTED CLAIM; CONDITIONAL STATEMENT; OPEN PROOF OBLIGATION.

**Do not use density-only or modular-survivor counts as if they were a genuine prime-pair correlation estimate.**
