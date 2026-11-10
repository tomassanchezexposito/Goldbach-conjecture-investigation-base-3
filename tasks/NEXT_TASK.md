# NEXT TASK — Stage 70, second research cycle: actual-arc positive-spectrum constant

**Research state:** Stage 70's first cycle has been completed independently by ChatGPT without using Codex, and is documented in:
- \`results/stage70/01_positive_spectrum_and_matching.md\` (two internally proved mathematical theorems)
- \`results/stage70/02_adversarial_limits.md\` (strict scope and limitations)
- \`results/stage70/verify_stage70.py\` and \`results/stage70/exact_results.json\` (executed exact verification)
- \`results/stage70/verification_manifest.json\` (verified SHA-256 and Git blob provenance).

**User's weekly Codex allowance is limited. Do not start a new CoCalc or Codex session or a background Goal automatically.** This document queues the next proof task for explicit future authorization or direct non-Codex ChatGPT mathematics.

## Single main mathematical question

For the *actual symmetric major arcs* \(\mathfrak M(X)\) and a predetermined even frequency superset \(K_X\) containing all possible weighted odd-prime sums, define for every residual N
\[
\beta_k(N)=\int_{\mathfrak M(X)}e((k-N)\alpha)\,d\alpha\in\mathbb R,
\quad
D_+(N)=\sum_{k\in K_X\setminus\{N\}}(\max\{\beta_k(N),0\})^2.
\]
A rigorously established major coefficient lower bound \(a_w(N)\ge A_X>0\) and independent *full-circle* fourth moment upper bound \(B_X\) would imply target nonvanishing under the sharp positive-spectrum cone criterion \(B_XD_+(N)<A_X^2\). The abstract argument is proved in Stage 70, but **its arithmetic applicability is OPEN**.

**Do not substitute a minor-only fourth moment for the full-circle \(B_X\).** Under classical PNT, the actual full circle energy is already \(\gg X^3\). The cone geometry would therefore need a very strong \(D_+\) estimate or a different phase-sensitive structure.

## Research cycle

1. Derive a fully explicit expression for the actual major-arc Fourier coefficients \(\beta_k(N)\), retaining all q,a, interval endpoints, overlap/measure conventions, and reflection symmetry.
2. Estimate the positive-part sum \(D_+\) on the **predetermined full even band** \(K_X\), rather than on the unknown Goldbach sumset. Prove lower and upper bounds with constants and their X dependence. A *lower* bound that makes the cone criterion impossible even under optimistic independent upper bounds may be more informative than another unproved positivity hypothesis.
3. Compare to genuine-prime full-circle \(\int|S_w|^4\gg_wX^3\) and sourced **upper** bounds. Identify quantitatively which constants must hold for the strict inequality \(B_XD_+<A_X^2\).
4. Attempt a second theorem retaining **nonnegative factorization** \(c_k=\sum_{p+q=k}s_ps_q\), with the fixed weights \(s_p=(\log p)w(p/X)\) distinguished from the variable-coefficient class. The half-weight deletion theorem shows why bounds from only total prime mass and upper energy cannot certify one target: all actual prime coefficients matter.
5. Adversarially audit any claimed improvement under finite changes to support, weight zeros, the \(p=q\) diagonal, prime 2 and 3, base-3 odd-prime positions and the difference between genuine prime representation and CRT survivors. Provide two independent mathematical derivations if possible, targeted exact checks and a precise first missing arithmetic estimate.
6. Save focused proofs, verifiers, counterexamples, dependencies and a rigorous negative conclusion if actual-arc \(D_+\) fails to give a useful saving. Avoid large finite Goldbach sweeps or generic narrative.

**Success:** an actual-arc quantitative result for the true-prime problem, or a rigorous no-go showing precisely why the positive-spectrum relaxation cannot close the missing target bound. **No Goldbach proof has been obtained or is presumed.**

**Operational:** no \`main\` edits/merge, no force push, no software installs or added paid resources. Codex/GitHub CLI \`gh\` is not required. The user may resume this when their weekly allowance resets, or continue through direct ChatGPT research.
