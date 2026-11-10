# NEXT TASK — Stage 70 (QUEUED, NOT RUNNING): prime-support separation from abstract Fourier one-hole extremizers

**Project research status:** universal Goldbach coverage of the original three-case residual set H remains OPEN.  
**Stage 69 M0–M9 internal documentary review:** closed on \`cocalc/stage69-deep-prime-specific-localization\`.  
**IMPORTANT RESOURCE CONTROL:** the user's weekly Codex quota is nearly exhausted. **Do not start CoCalc/Codex or enable a Goal automatically.** This task is a stored scientific proposal only; launch it only after a later explicit user request and available allowance.

## Required starting state when the user authorizes work

1. Read \`results/stage69/final_report.md\`, \`results/stage69/08_adversarial_review.md\`, \`results/stage69/09_final_synthesis.md\`, \`results/stage69/theorem_dependency_ledger.md\`, and \`results/stage69/review_verification_manifest.json\`.
2. Preserve and read the true mathematical definitions:
   \[
   H=\{N\ge4:N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\},\qquad
   R(N)=\#\{p<q:p,q\text{ prime},\ p+q=N\}.
   \]
   The author's \(p=3+2a\) for odd primes is a position coordinate, not ternary digits, congruence modulo 3, or simultaneous primality.
3. Follow \`docs/cocalc_github_pr_workflow.md\`. Use Git SSH and the already dedicated identity; no \`gh\` install, private API token, new credentials, branch deletion, force push, \`main\` merge, added subscriptions or costs.
4. On explicit authorization, create a **new Stage 70 branch from the audited Stage 69 head**, not from the historically incomplete handoff or Stage 68. Do not run until authorized.

## Focused mathematical question

Stage 69 proves that an unrestricted \(L^2\) function on a major/minor partition of measures \(\nu,\mu>0\), with prescribed major Fourier coefficient \(a\) and zero full coefficient, must spend energy at least
\[
\int_{\mathbb T}|F|^2\ge\frac{|a|^2}{\mu\nu}.
\]
That extremal function is typically not the square of a finite polynomial with nonnegative weights on **genuine prime frequencies**. A *qualitative* exclusion from a polynomial subspace does not produce a uniform arithmetic saving.

The **single research challenge** is to quantify the gap between (a) an abstract complex \(L^2\) one-hole extremizer and (b) the actual prime-supported square
\[
S_w(\alpha)^2,\qquad S_w(\alpha)=\sum_{p\ {\rm prime}}(\log p)w(p/X)e(p\alpha),
\]
in such a way that its effect on a **specific residual coefficient \(N\)** is sufficient to rule out \(R(N)=0\), without assuming a pair exists at N.

### Scientific milestones (depth, not more brute-force)

**I. Functional-analytic proof of the exact restricted variational problem.** Define a fixed finite frequency-support space and its coefficient Gram/Toeplitz operator on the actual major and minor sets. Derive sharp norm/cancellation bounds for a *general* finite polynomial \(S=\sum_{p\in \mathcal P_X}s_pe(p\alpha)\) with \(s_p\ge0\), \(0\le s_p\le(\log p)\), separating the variable cone from the **fixed actual** weights \((\log p)w(p/X)\). Determine equality and all dependence on X, major-arc measure and support dimension. **Do not replace the nonlinear square constraint by an unconstrained Fourier polynomial without recording the resulting loss.**

**II. Quantitative separation or rigorous limitation.** Try to prove a uniform inequality of the form
\[
\inf_{\text{admissible prime-square inputs with specified a and }r(N)=0}
\frac{\int_{\mathbb T}|S|^4}{|a|^2/(\mu\nu)}\ge1+\delta_X,
\]
with exactly specified class, normalization, \(\delta_X\), and nonemptiness convention. Determine the **minimum asymptotic scale** \(\delta_X\) needed to beat the currently known fourth-moment bounds. If the infimum is over an empty class because fixed weights already represent N, **do not claim to have proved Goldbach**: proving emptiness requires independent arithmetic information. For a broad nonnegative coefficient cone, construct any valid counterexample to a claimed uniform gap, keeping the actual-prime case distinct.

**III. Bilinear arithmetic content.** Identify whether the hypothetical separation can be reduced to a *genuine-prime* signed short-shift correlation, a Type I/II bilinear exponential sum, or an exact support-restricted Toeplitz quadratic form. For each attempted reduction give the first missing theorem with fixed variables, denominators, shifts, weights, error size and strict margin. Do not assert Hardy–Littlewood asymptotics, positive wheel residues or a target anchor pair as proved facts.

**IV. Independent proof route and literature.** Independently pursue a target-indexed circle-method signed estimate that preserves the phase \(e(-N\alpha)\), and compare mathematically with the positivity-constrained polynomial route. Recheck the original paper hypotheses for 2026 conditional fourth-moment and exceptional-set estimates before claiming an implication. Explain why a positive-power exceptional-set bound never excludes one target.

**V. Adversarial review.** Search for the first false step in each failed approach; handle \(p=q\), prime 2, prime 3, weight support zeros, even shift parity, real-versus-complex arc coefficients, exact versus upper energy bounds, and the Stage 69 low-denominator minor-arc erratum. Two distinct derivations for any claimed theorem and a genuinely independent reviewer check are required.

**VI. Completion and handoff.** Publish exact theorems/conditional propositions, countermodels, source ledger, minimal focused verification, SHA-256 manifest, failure analysis and the next precise open obligation to a new Stage 70 research branch; keep every prior stage unchanged.

## Evidence and success standard

Success means **a mathematically non-circular prime-specific bound with a demonstrable strict gain at each N**, or a rigorous negative theorem showing a carefully defined broad input class cannot supply such a gain, narrowing the true-prime problem. An abstract inequality that merely rephrases \(r_w(N)>0\), a longer list of finite Goldbach checks, or a restatement of the unchanged global fourth moment is **not** progress.

Classify every item as **PROVED**, **EXTERNAL**, **CONDITIONAL**, **FINITE**, **REFUTED**, or **OPEN**. Never present the hypothesis \(R(N)>0\) or a positive anchored product as an input in its own proof.

**Status: PREPARED ONLY. No Codex session, remote background agent or scheduled automation is running because of this file.**
