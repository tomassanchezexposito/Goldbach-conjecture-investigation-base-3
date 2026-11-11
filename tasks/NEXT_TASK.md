# NEXT TASK — Stage 72 (QUEUED ONLY): target-rigid genuine-prime correlations beyond global norm stability

**Status as of 2026-11-11:** Stage 71 mathematical report complete, with two internally proved theorem families and exact independent finite regression. The user's original three-case universal Goldbach coverage is still **OPEN**. **Do not automatically start Codex or CoCalc Goal**; the user's weekly Codex quota was limited and this is a stored mathematical research handoff, not an authorization for a new run.

## Read these source records before continuing

1. \`results/stage71/final_report.md\`, \`01_exact_target_robustness_and_lp.md\`, \`02_adversarial_review.md\`, and \`verification_manifest.json\`.
2. Stage 70 \`03_actual_arc_cone_nogo.md\` and \`05_vanishing_mass_prime_deletion.md\`: broad full-even-band Fourier cone is quantitatively insufficient, and an \(o(X)\)-mass deletion retains first-order prime progressions while erasing a target.
3. Stage 69 \`07_primary_analytic_route_A.md\`, \`07_primary_arithmetic_route_B.md\`, \`09_final_synthesis.md\`: both analytic and reflected-arithmetic routes still lack a pointwise true-prime estimate.
4. Follow \`docs/cocalc_github_pr_workflow.md\` for GitHub publication; GitHub CLI \`gh\` is optional and cannot be treated as a failure to push branches.

## Why the approach must pivot again

Stage 71 proved, using unconditional Wu/PNT input, that after deliberately deleting a vanishing proportion of genuine-prime frequencies the resulting modified polynomial can be **globally close to the original in every fixed normalized Fourier \(L^q\) norm**, and even its square can be globally close in **every fixed \(L^r\)**, while its coefficient at a prescribed residual target is **exactly zero**.

The exact \(\ell^1\) deletion radius to zero is the sum over target-complement edges of their smaller weight:
\[
\tau_N=\sum_{p<q,\ p+q=N}\min(a_p,a_q).
\]
Proving \(\tau_N>0\) for the **complete true-prime support** is essentially the unresolved Goldbach assertion; it cannot be adopted as an independent lemma. The sharp finite matching and greedy optimization do **not** supply a nonzero arithmetic lower bound.

**Therefore Stage 72 MUST NOT** repeat: global-fourth-moment optimization, exact but arithmetic-neutral Gram identities, general Fourier \(L^p\) closeness, larger finite Goldbach sweeps, or weighted-support countermodels with arbitrary prime deletions. Their explanatory roles are now fully documented.

## One sharply focused true-prime problem

Find and **prove from independent arithmetic results** a signed or absolute target-local estimate involving the exact fixed genuine-prime coefficients
\[
a_p=(\log p)w(p/X),\qquad
r_w(N)=\sum_{\substack{p+q=N\\p,q\ {\rm prime}}}a_pa_q
\]
whose conclusion forces \(r_w(N)>0\) for **each** specified residual \(N\in H\cap[X/2,X]\), with \[
H=\{N\ge4:N\text{ even},\ N-1,N/2\text{ composite}\}.
\]
If a smoothed weight fails to include any pair region for a target, positivity of its coefficient is not equivalent to Goldbach; prove and state the exact nonvanishing interval conditions on w. The user's odd-prime position map \(p=3+2a\) and reflected index \(a+b=N/2-3\) are retained, but not treated as prime distribution theorems.

### Research route A: quantitative target-error with real genuine primes

1. Start with the exact prime-only circle decomposition \(r_w(N)=a_w(N)+m_w(N)\) using \(S_w^2\), **not** \(|S_w|^2\). For non-symmetric arc pieces use paired regions and real parts.
2. Audit each available external major-arc theorem's true uniformity, smoothing, conditional common-zero-free hypotheses and effective constants. If a positive lower bound \(a_w(N)\ge cX\) is only conditional, retain that qualifier.
3. Derive a *new*, independently proven **signed true-prime** minor-arc estimate with a strict margin below the major coefficient, or identify the first unavailable bilinear estimate and why existing global fourth moments cannot yield it.
4. When using \(\Lambda\) or von Mangoldt, explicitly subtract genuine prime powers and diagonal terms with deterministic errors. Never pass from a weak upper estimate on an exceptional-set count to the absence of one prescribed exceptional target.

### Research route B: prime-specific reciprocal matching rigidity

1. Study whether the actual fixed sequence \(a_p\) has any arithmetic statistic that **changes by an order-one target-relevant amount under the optimal matching deletion** but can be estimated independently of Goldbach. Examples: signed reflected bilinear sums, modulus-dependent covariance, or a genuinely local dispersion identity. Avoid merely defining a statistic equal to \(r_w(N)\) and assuming a positive lower bound.
2. Prove exact identities for the deletion gradient \(2a_{N-p}\), distinguishing ordinary first-order distribution from paired primality.
3. Test conditional short-interval or arithmetic-progression inputs against the specific \(O_w(X\log\log X/\log X)\) deletion mass. If a proposed estimate is unaffected by the deletion, it cannot force target positivity in the broad modified class. A meaningful genuine-prime theorem must exclude that class by an independently justified assumption, not by assuming a representation.
4. Preserve the sieve parity barrier, the cases p=2, p=3, p=q, and the distinction between the 210 wheel's survivor counts and actual simultaneous primality.

### Required proof discipline

For each candidate inequality record:
- exact domain and quantifiers \(X,N,p,q,h,\kappa,w\);
- constants, asymptotic exponents, weight support, uniformity and source theorem dependencies;
- first strictly arithmetic step not already implied by global norm identities;
- independent proof or first invalid implication; proof by contradiction must not select a target prime pair;
- whether the hypothesis is weaker, equivalent to or stronger than the desired target positivity;
- a small exact countermodel only when it tests a nontrivial algebraic assertion, not brute-force evidence.

Retain two mathematically distinct proof paths and an adversarial audit. Mark statements **PROVED / EXTERNAL / CONDITIONAL / FINITE / REFUTED / OPEN**. If no new prime-theoretic signed estimate can be proved, the valid result is a precise barrier theorem or an identified minimal missing lemma, not an unsupported solution claim.

## Publication and resource restrictions

**Queued but not started.** When explicitly authorized, branch from \`cocalc/stage71-sharp-deletion-sensitivity\`, save source files and proof ledger, add only decisive reproducible tests, and open a draft PR through the connected GitHub tool. No \`main\` modification, force push, new credentials, package installations, increased spending or Codex usage without express approval.

**Scientific success:** a non-circular, genuinely prime-specific pointwise estimate with sufficient quantitative strength, or a valid new obstruction narrowing the remaining proof obligation. Goldbach remains OPEN until a complete proof is found and independently audited.
