# NEXT TASK — Stage 62: verify singular-series local variation and seek a target-anchored arithmetic error

**Evidence status: OPEN universal-coverage problem.** The mathematical theorem in Stage 62 concerns the *singular-series arithmetic factor*, NOT the existence or asymptotic number of genuine prime pairs.

## Read first

- \`results/stage62/report.md\`: proved CRT/Dirichlet/Euler construction of unbounded local singular-series jumps even with wheel-210 normalization and N in the author's residual set H; sharpened but logically insufficient Stage 61 conditional box bound.
- \`results/stage62/verify_singular_series.py\`: finite exact CRT constructions (stdlib only), independent residue enumeration, exact factorization and fractions.
- \`results/stage61/report.md\`: signed four-prime expansion and missing pointwise estimate.
- \`results/stage60/integration_review.md\` and \`docs/stage60_integration_handoff.md\`: provenance.
- [Stage 61 draft PR #10](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/pull/10).

## Target and status

For every even N in H (N>=4, N-1 composite, N/2 composite), prove the existence of a pair of **genuine distinct primes** p<q with p+q=N, without assuming it or using congruence survivors as proxies.

The theorem about \`F(n)=prod_{p|n,p>2}(p-1)/(p-2)\` is unconditional; the Hardy–Littlewood pointwise approximation \`R(n) ~ S(n)n/(2 log² n)\` is **conjectural**, not an established estimate.

## Authorized CoCalc execution

1. Verify Git SSH through the existing dedicated deploy key. Work only on \`cocalc/stage62-singular-series-local-variation\`, whose tracked branch already includes the Stage 62 report and verifier. Do not modify \`main\`.
2. Read the report closely. Independently audit the CRT residue \`q=1 mod P,\ q=4 mod 5\`, use Dirichlet correctly to obtain infinitely many primes q, confirm \(N=2(q-1)\in H\), and justify the divergent product via Euler's divergence of reciprocal primes. Correct any invalid step; mark the result as a standard-theorem consequence, not a claimed novel deep number-theory theorem.
3. Execute \`python3 -B results/stage62/verify_singular_series.py\` and independently confirm the exact ratios with a separate SageMath or Python algorithm; record parameters, wall time, source hashes and finite sample results in \`results/stage62/\`.
4. Audit Proposition 62.3 (sharp \`D>=4Lambda²/9\` for positive triples all within a relative 1/3 box). Confirm that the assumption **already implies** the target \(X_N>0\), so this is **not a non-circular proof method**. Do not relabel deterministic constant refinement as arithmetic progress.
5. Compare local normalization by the finite wheel \`A_210(N)\` with the full arithmetic singular series \`S(N)\`: the proved unbounded jump applies only to \`S(N)/A_210(N)\`, not unconditionally to real prime-pair counts.
6. Focus on an independent target-anchored signed correlation or circle-method error. Formulate exactly what *uniform genuine-prime information* would be required to make the Stage 61 \(D_N>0\) inequality effective for all N in H, and audit whether it is genuinely weaker than simply assuming \(R(N)>0\). Do not introduce a condition that directly assumes a positive target count.
7. Seek concrete published unconditional estimates (major arcs, minor arcs, exceptional sets, parity barrier), carefully noting missing uniformity, constants and target dependence. Give precise verifiable sources; distinguish references from proofs. **Do not claim a proof of Goldbach.**
8. Save an English report, executable code, an independent verification result, and a SHA-256 manifest. If an attempt fails, record the first invalid logical step.
9. Commit and push only the Stage 62 branch. Open a draft PR if possible. Do not install new software, incur costs, delete existing files or merge to \`main\`.

## Successful outcome

Either a genuinely independent proved pointwise lower bound for genuine primes with a positive margin and effective cutoff, **or** a clear rigorous obstruction proving that the candidate local condition cannot follow from the current wheel, singular-series heuristic, and finite/averaged data. A finite extension alone is not success.

All repository content, scripts, reports, and commit messages must be in English.
