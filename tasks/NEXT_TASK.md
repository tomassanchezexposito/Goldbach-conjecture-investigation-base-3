# NEXT TASK — Stage 64: audit 2026 fourth-moment advances and the last pointwise gap

**Mathematical status:** the author's three-case universal coverage on H remains an OPEN conjecture. **Research branch:** \`cocalc/stage64-2026-minor-arc-gap\`, a direct descendant of Stage 63. Do not alter \`main\`, merge prior draft PRs, or claim a Goldbach proof.

## 0. Environment and continuity

Local clone: \`/home/user/goldbach-research-github\`. Use the previously authenticated GitHub deploy key explicitly if SSH defaults fail; never print any private key. Verify clean worktree, fetch, and check out the existing Stage 64 remote branch. Read Stage 63 reports and tests, Stage 62 model obstruction, and \`docs/research_protocol.md\`.

Stage 63 completed milestones M0–M6, added exact CRT shared-prime identities, prime-only Fourier coefficient and a conditional dyadic-energy criterion, and left both arithmetic input estimates unproved. Review [draft PR #12](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/pull/12).

**Mandatory textual erratum:** Stage 63 M1 says that the shared primes for (n,m)=(12,18) are x=7 and x=11. This is false: x=11 makes n−x=1, which is nonprime. Correct x values are **5 and 7**, producing prime triples (5,7,13) and (7,5,11). Confirm by direct primality independently, preserve original history, correct the inherited source file in this branch with a transparent commit, and record the erratum in Stage 64 report. The original general shared-prime lemma is unaffected.

## 1. New external sources that MUST be examined before extrapolation

Several October/November 2026 preprints postdate or materially refine Stage 63's reviewed 2018-era exceptional-set comparisons. Verify each original PDF/arXiv version, theorem hypotheses, proof dependencies and publication status. The following are references to **research claims/preprints**, not automatically independent fully established theorems:

1. **Huixi Li and Zhixin Liu**, *Fourth moments of prime exponential sums and exceptional sets for sums and differences of primes*, arXiv:2610.26756 (2026-10-19), https://arxiv.org/abs/2610.26756 . Its Theorem 1 gives, assuming a common uniform Dirichlet-L zero-real-part bound \(\Theta<11/12\), a minor-arc fourth-moment estimate
   \[
   \int_{\mathfrak m}|S_w(\alpha)|^4\,d\alpha\ll_{\Theta,w}X^{5/2}(\log X)^{100},
   \]
   and exceptional-set bound \(\ll X^{1/2}(\log X)^{100}\). Verify the exact choice of smoothed prime weight, \(\kappa\) interval, zero condition, and all quantifiers.
2. **János Pintz and Ingo Althöfer**, *The Goldbach exceptional set: an exponent 7/12 and conditional refinement*, arXiv:2610.15559 (2026-10-11), https://arxiv.org/abs/2610.15559 . It states \(E(X)\ll_\epsilon X^{7/12+\epsilon}\) under a fixed common zero-free half-plane \(\Re s\le\Theta_0<1\), plus conditional refinements. Verify exact external reliance and whether stronger newer preprints supersede it.
3. **I. Althöfer, D. Chen, A. Perelli, J. Pintz**, *The exceptional set of Goldbach numbers among polynomial values*, arXiv:2611.09386 (2026-11-06), https://arxiv.org/abs/2611.09386 . Its claim concerns almost-all polynomial targets, NOT every even target. It cites both recent results. Identify any usable genuinely pointwise special case and distinguish degree k>=2 from linear/full-even targets.
4. **OpenAI math**, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s)>7/8*, September 2026 release, https://github.com/openai/math/tree/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026 and Lean scope note https://github.com/openai/math/blob/main/lean/docs/003.md . The 2026 preprints invoke this as an external uniform Dirichlet \(L\)-function zero-free theorem. Audit claimed exact scope, formalization versus mathematical manuscript, theorem dependencies and any corrections; do not independently assert its proof solely because a preprint cites it.

Read and cite primary sources with exact sections/theorem statements. Distinguish journal peer-reviewed material, preprints and a formalization's actual scope. Check newer v2/revisions if available; do not fabricate bibliographic metadata. If Internet is unavailable, record this and use already downloaded sources without claiming fresh verification.

## 2. Main mathematical obligation: evaluate new fourth moments against Stage 63 M5

Let \(C_\Lambda(N)=\sum_{a+b=N}\Lambda(a)\Lambda(b)\), \(\mathfrak S(N)=2C_2\prod_{p\mid N,p>2}(p-1)/(p-2)\), and
\[
\mathcal E(X)=\sum_{\substack{X/2\le N\le X\\N\ {\rm even}}}|C_\Lambda(N)-N\mathfrak S(N)|^2.
\]
Stage 63 proves *conditionally*: if \(\mathcal E(X)=o(X^2)\) (or an explicit sufficiently small threshold after the prime-power correction), then all sufficiently large residual N have a distinct prime pair.

**Prove/disprove a derivation** of the needed \(\mathcal E(X)\) bound from the reviewed Li–Liu fourth-moment estimate with exact normalization of \(S_w\), smoothing, major-arc error, and prime-power terms. Do not confuse the smoothed prime-only coefficient with the unsmoothed von Mangoldt convolution.

A crucial expected bottleneck to audit exactly: the standard Parseval/Bessel step bounds the entire minor-arc coefficient square sum by \(\int_{\mathfrak m}|S_w|^4\ll X^{5/2}\log^{100}X\), which is **larger** than the \(o(X^2)\) target. A single coefficient can have size up to \(X^{5/4}\log^{50}X\) under this norm bound, larger than the expected major term \(\asymp X\). Confirm signs and constants and identify which stronger **localized** estimate would be needed to bound a prescribed residual N.

**Do not** claim that an exceptional-set estimate \(\ll X^{1/2+\epsilon}\) excludes a single exceptional N. Its right-hand side still diverges; even a singleton is compatible with it.

## 3. Compare approaches without circularity

Research three tracks in parallel conceptually, but execute sequentially to conserve resources:

A. **Sign-preserving pointwise minor arc:** an explicit independent uniform bound on the real minor-arc contribution at each N in H that is smaller in magnitude than a proven positive major-arc contribution. Track all changes of weights, arcs and exclusions. Show whether existing estimates actually supply it.

B. **Signed four-prime target correlation:** exact \(Q_4(N,M)\) and shared-prime contractions, including whether anchored positivity has been assumed. Critically assess whether an L4 estimate over shifts/moduli can be localized to a specific N without losing a factor X. Display the precise first failed step.

C. **Residual arithmetic structure:** test whether \(N-1\) and \(N/2\) composite plus position coordinates \(p=3+2a\) produce a *proved* distribution restriction not implied by the wheel and the full singular series. No numerical coincidence or sieve survival will count as proof of simultaneous primality. Avoid repeating Stage 62 local-smoothness criteria refuted by its arithmetic model.

For each candidate, provide (i) exact theorem statement; (ii) scope and quantifiers; (iii) proof or first missing lemma; (iv) whether its premise itself implies R(N)>0; (v) targeted counterexample check; (vi) the strongest relevant published theorem and exact gap.

## 4. Required mathematical deliverables and independent verification

Save English artifacts in \`results/stage64/\`:

- \`00_stage63_erratum_and_provenance.md\`: M1 x=11 correction, underlying code verification, inherited branch/commit fingerprints.
- \`01_2026_primary_sources.md\`: full detailed theorem/assumption table comparing 2026 sources, classic Pintz, Bhowmik–Grimmelt, and zero-free claims; references as live URLs with accessed date, preprint/journal/formalization status.
- \`02_fourth_moment_to_pointwise_gap.md\`: complete analytic derivations and the sharpest verified mismatch of exponents, logs, constants, and target quantifiers.
- \`03_signed_fourprime_alternatives.md\`: exact target-anchored expansions and non-circularity checks; genuinely independent new lemmas or detailed obstructions.
- \`04_research_attempt.md\`: one focused attempt to prove a nontrivial, non-circular prime-only estimate (or a rigorously demonstrated failure); include actual proof steps and adversarial challenge.
- \`05_adversarial_review.md\`: independent review of all new mathematical claims, classification PROVED/EXTERNAL/CONDITIONAL/REFUTED/FINITE/OPEN.
- \`final_report.md\`, \`source_manifest.json\`, \`tests/...\` where relevant, \`checkpoint_log.md\`, and updated \`tasks/NEXT_TASK.md\` specifying Stage 65's narrow mathematically meaningful target.

Use exact integer or rational computations, two independent methods for new finite identities, and mathematical symbolic derivations. Finite examples verify algebra only; do not scan millions of even numbers without a lemma to test. Record software versions, parameters, errors, and SHA256 file hashes. If an external source is inaccessible or a proof is incomplete, say so.

## 5. Long execution / checkpoint protocol

The user may again be unavailable for several hours. Once authorized by the pasted CoCalc instruction, Codex should advance through every feasible subtask without routine check-ins, committing separate reviewable checkpoints to \`cocalc/stage64-2026-minor-arc-gap\` between major milestones. Continue after nonfatal dead ends, documenting the first invalid implication. Do not invent progress or promise indefinite background execution. Respect CoCalc runtime, Goal budgets, memberships and idle limits; a Goal or active run does not guarantee multi-hour continuation.

No additional spending, package installs, security/SSH changes, deletion of prior research, destructive Git operations, force push, public release, or merge into main. Preserve all prior research in its original branches. Open a draft PR at the end when available; otherwise publish the branch and provide its compare URL. Use English for everything committed.

**Completion criterion:** the strongest verified non-circular pointwise analytic advance or a detailed independent proof that the specific proposed derivation from stated fourth-moment hypotheses fails to close the target gap. **Never claim universal coverage without complete proof.**
