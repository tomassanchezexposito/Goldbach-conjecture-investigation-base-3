# NEXT TASK — Stage 65: corrected target-localized Fourier arithmetic

**Status:** universal residual coverage OPEN. **Source branch:** \`cocalc/stage65-corrected-fourier-localization\` (based on published Stage 64). Prior stages are never to be overwritten. All repository material is English.

## 0. Mandatory mathematical correction and regression gate

Stage 64's \`results/stage64/02_fourth_moment_to_pointwise_gap.md\` incorrectly defined arc coefficients using \(|S_w(\alpha)|^2\) while defining the full Goldbach coefficient using \(S_w(\alpha)^2\). The first counts **prime differences** and the second counts **prime sums**. This invalidates the original assertion that their integrals partition the same coefficient.

The formulas have been **corrected on this Stage 65 branch only**, and the exact mathematical erratum is at \`results/stage65/00_erratum.md\`. A regression test is at \`results/stage65/tests/verify_sum_difference.py\`.

**DO THIS FIRST before any new analytic work:**

1. Clean working tree; explicit prior SSH deploy identity; fetch origin and check out the new branch. Never display secrets.
2. Read the correction and all Stage 64 reports. Run \`python3 -B results/stage65/tests/verify_sum_difference.py\`. Check both exact independent methods (ordered-pair enumeration and finite-field DFT) and the explicit N=8 contrast: squared coefficient=2, modulus-squared coefficient=0.
3. Independently derive \(\widehat{S_w^2}(N)=\sum_{p+q=N}a_pa_q\) and \(\widehat{|S_w|^2}(N)=\sum_{p-q=N}a_pa_q\) with all factors and signs. Check no other source under Stage 64 continues to make the wrong substitution. Avoid changing previously committed branches.
4. Correctly use \(m_w(N)=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)\,d\alpha\) and \(a_w(N)=\int_{\mathfrak M}S_w(\alpha)^2e(-N\alpha)\,d\alpha\); their sum is the full weighted prime-pair coefficient. For a symmetric arc partition and real weights, these are real. **Parseval still uses \(\int_{\mathfrak m}|S_w(\alpha)|^4\)**.
5. Preserve the separate small-prime correction already made on this branch: even N>4 cannot have a prime representation containing 2; 2+2=4 is an excluded diagonal.
6. Record commands, exact output, SHA-256 and a short audit of the Stage 64 source manifest, which is historical and should not be silently treated as current after corrected source edits.

Do not proceed to the main analytic task unless the sum-vs-difference regression passes. If it fails, debug and explicitly record the first incorrect identity.

## 1. Exact fixed-target localization identities

Let \(w\ge0\) be a fixed smooth prime weight as specified by the externally cited primary paper, \(S_w(\alpha)=\sum_pa_pe(p\alpha)\) with \(a_p=(\log p)w(p/X)\), and let \(f_X(\alpha)=\mathbf1_{\mathfrak m}(\alpha)S_w(\alpha)^2\). Then \(m_w(N)=\widehat f_X(N)\) with a clearly specified Fourier convention.

For an arbitrary *finitely supported* sequence \(\{\lambda_h\}\), derive the exact identity
\[
\sum_h\lambda_h m_w(N+h)
=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)
\left(\sum_h\lambda_he(-h\alpha)\right)\,d\alpha.
\]
Define the localization multiplier \(K_\lambda(\alpha)\) precisely, checking the sign. Prove Parseval:
\[
\|K_\lambda\|_{L^2([0,1])}^2=\sum_h|\lambda_h|^2.
\]
Show what follows from the **global** Li–Liu fourth-moment bound alone:
\[
|\sum_h\lambda_hm_w(N+h)|
\le \left(\int_{\mathfrak m}|S_w|^4\right)^{1/2}
\|K_\lambda\|_2
\ll X^{5/4}(\log X)^{50}\|\lambda\|_{\ell^2}.
\]
Carefully distinguish bounds over the full circle, the minor set, and restricted support. If \(\lambda_0=1\), then \(\|\lambda\|_2\ge1\), so **this direct Cauchy–Schwarz bound alone cannot improve** the single coefficient scale. This statement is a deterministic limitation of this route, not of all possible arithmetic localization methods.

If using a normalized averaging kernel with \(\lambda_0\ll1\), explain why the bound on the average does not automatically control \(m_w(N)\) without an independent local regularity or correlation estimate. Give an exact countermodel where one coefficient is exceptional and all neighbors are small, respecting the assumed global \(\ell^2\) norm.

## 2. Challenge three localization mechanisms

1. **Short-shift Dirichlet/Fejér kernels:** derive their normalization, mass, and effective Fourier supports exactly. Determine the best individual coefficient error after attempting inversion from a local average. Identify the first missing *true-prime* shift regularity theorem.
2. **Arithmetically selected shifts from the user's base-3 positions:** specify the reflection positions \(\{3+2a,N-(3+2a)\}\), wheel and full singular-series factors, and determine whether any independent signed correlation gain is derived from the residual factorization of \(N-1,N/2\). Do not conflate local admissibility with primality.
3. **Target-anchored shared-prime or four-prime correlations:** use the exact M1 and Stage 57 contractions, not a crude product of marginal counts. Seek a verifiable sign-preserving inequality for a Fourier coefficient at N that is genuinely independent of \(R(N)>0\). State precisely where anchored positivity would become circular.

For each technique provide the exact theorem/identity, quantifiers, constants, support conditions, numerical assumptions, counterexample and available source theorem (if any).

## 3. Rigorous no-go and conditional-progress alternatives

Choose at least one of:

- **Proved deterministic no-go:** show a global \(L^2\) coefficient bound as large as \(X^{5/2}(\log X)^{100}\) cannot exclude an isolated coefficient of size \(cX\), even when one applies any finitely supported **linear** localization functional with no independent coefficient constraints. Explicitly define the class of admissible abstract Fourier sequences and show its relationship to the true-prime problem is *only logical*, not arithmetic.
- **Non-circular conditional theorem:** formulate a new additive Fourier regularity hypothesis that does *not* itself assert \(R(N)>0\) or place all true-prime counts inside a positive box. Prove with sharp constants how that hypothesis plus a valid major-arc input would rule out one target. Distinguish genuine arithmetic estimates needed to prove the new hypothesis.
- **Independent genuine-prime arithmetic lemma:** if a usable new signed estimate is found, prove it with all quantifiers and effective constants; test it independently, seek counterexamples and compare to original literature.

Avoid translating a global averaged bound into “all targets” without an explicit localization theorem. Keep third/fourth moments and their normalizations separate from the Stage 63 unsmoothed von Mangoldt discrepancy.

## 4. External literature and verified hypotheses

Start with the original Li–Liu v1 \`arXiv:2610.26756\`, Pintz–Althöfer \`arXiv:2610.15559\`, Althöfer–Chen–Perelli–Pintz \`arXiv:2611.09386\`, and the Bhowmik–Grimmelt published study; verify changes/errata and the OpenAI 7/8 uniform zero-free paper only insofar as relevant. Source and formalization claims require independent checks and clear preprint/peer-reviewed labels.

The relevant fourth-moment estimate is explicitly conditional on uniform Dirichlet zero-real-part assumptions as stated in its source; it gives a global exceptional-count bound but no empty-exception conclusion. A paper's cited formalization is not automatically an independent verification of all downstream results.

If genuinely fresh results are available, inspect **actual** theorem statements, proof dependencies, and date. Do not overclaim that a proven circle-method estimate exists merely because a paper suggests one.

## 5. Independent exact verification, reporting and Git workflow

Create \`results/stage65/\` artifacts:

- \`00_erratum.md\` (already authored, audit independently).
- \`01_localized_kernel_identities.md\` with full proofs and constants.
- \`02_fourier_localization_limits.md\` with sharp countermodels and first missing signed estimate.
- \`03_prime_correlation_arithmetic.md\` (base-3/210 and full-factor analysis).
- \`04_primary_literature.md\` (theorem/hypothesis table).
- \`05_new_analytic_attempt.md\` (strongest genuinely attempted inequality and adversarial verdict).
- \`06_independent_review.md\`.
- \`final_report.md\`, focused scripts, exact outputs, \`checkpoint_log.md\`, \`source_manifest.json\` with hashes, updated \`tasks/NEXT_TASK.md\` for the next narrow target.

Use two independent exact implementations where finite verifiers are appropriate, e.g. integer convolution vs modular finite-field DFT; do not represent floats as proof of an exact identity. Check N=4,6,8 and prime-2/diagonal issues.

**Execution:** progress through all feasible milestones without routine user intervention. Commit and push checkpointed work only to \`cocalc/stage65-corrected-fourier-localization\`. Open a draft PR against Stage 64 when done. Do not modify main, spend money, install software, change GitHub permissions, force-push, delete old results, or claim a proof of the author's three-case conjecture without a fully rigorous universal proof.

**Success** means either a rigorously new independent true-prime estimate or a theorem specifying why the prior fourth-moment plus linear localization cannot yield pointwise positivity, together with a precise new arithmetic input that would overcome the barrier. Increasing finite search ranges is not a substitute.
