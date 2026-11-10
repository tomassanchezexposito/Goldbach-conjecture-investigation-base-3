# NEXT TASK — Stage 64 pointwise analytic gap audit

## Primary objective

Continue the original three-case representation conjecture in `docs/research_statement.md`. The goal remains universal coverage of the residual set

$$H=\{N\ge4:N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\}$$

by genuine distinct prime pairs: prove $R(N)>0$ for every $N\in H$. This is open. Do not replace the pointwise target by an average theorem or infer existence from a positive singular series.

## Stage 63 handoff

Read `results/stage63/final_report.md`, `theorems_and_dependencies.md`, `failed_approaches.md`, `next_objective.md`, and `checkpoint_log.md`. Stage 63 proved exact shared-prime CRT and target-anchored Fourier identities, reviewed the relevant literature, and proved a conditional dyadic energy criterion. It did **not** prove the criterion's hypothesis or universal coverage. The central routes left open are:

1. A target-uniform signed minor-arc bound paired with an independently proved positive major-arc lower bound; or
2. The M5 estimate $\mathcal E(X)=o(X^2)$ for the von Mangoldt convolution discrepancy, or a sufficiently small explicit threshold after the recorded prime-power correction.

## Stage 64 work

1. Check the exact hypotheses and theorem statements in primary/full sources for the strongest relevant unconditional binary Goldbach mean-square, circle-method minor-arc, and exceptional-set bounds available in the cited bibliography. Do not rely on abstracts alone where a full source is available.
2. Compare their exact weights, local factors, parity restrictions, summation ranges, error exponents, quantifiers, constants, and effective cutoffs against the Stage 63 target bounds.
3. Attempt one explicit derivation from established unconditional estimates to a target-specific signed inequality. Show every transformation and constant. If the derivation loses target localization or sign, identify and quantify the first loss.
4. Independently check the M5 prime-power correction, diagonal convention, and threshold. Determine whether a cited theorem actually reaches the strict energy threshold; do not treat a weaker $O(X^2)$ estimate as sufficient without its constant.
5. If no unconditional route works, record a precise conditional theorem or a rigorous logical countermodel to the attempted inference. Do not claim an impossibility result about actual primes without proof.
6. Keep focused exact checks for $N=4,6,8$, the small-prime cases $2,3,5,7$, and selected residual examples. Use finite calculations only to validate identities, not to claim asymptotic coverage.
7. Save English reports, a theorem/quantifier comparison table, reproducible verification code or data when it adds value, a parameter/version/hash manifest, and the next precise research objective under a new `results/stage64/` directory.

## Evidence and branch controls

Use the evidence labels in `docs/research_protocol.md`. Distinguish proven identities, conditional implications, established literature, finite computation, conjecture, and open obligations. Preserve all prior stages. Work on a separate Stage 64 branch based on the current Stage 63 branch; do not alter or merge `main`. Commit and push reviewable checkpoints on the Stage 64 branch only when the authorized task begins.

Do not install software, start paid services, delete prior research, run unbounded scans, expose credentials, or claim a solution to Goldbach/the three-case statement without a complete rigorous proof. All repository content and commit messages must remain in English.
