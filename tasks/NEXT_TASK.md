# NEXT TASK — Stage 67: rational-arc increment geometry

**Research status:** The original three-case conjecture remains open. Stage 66 proved sharp deterministic local and aggregate energy inequalities, but obtained no pointwise arithmetic modulus for genuine prime correlations. Preserve the complete history and work only on the pre-created branch `cocalc/stage67-rational-arc-increment-gram`; do not merge into `main`.

**GitHub publication and PR rule:** The Stage 67 branch now exists in the remote. Read `docs/cocalc_github_pr_workflow.md` before starting. Push verified commits via SSH Git, but do **not** require the `gh` CLI to create a PR; ChatGPT's separately authenticated GitHub connector handles draft PRs. If `gh` is unavailable, report the exact branch URL and compare URL rather than calling the research publication a failure.

## 1. Safe start and required audit

1. In `/home/user/goldbach-research-github`, verify the working tree is clean and fetch using the existing dedicated GitHub SSH deploy key with `IdentitiesOnly=yes`. Never disclose private key contents.
2. Check out the existing Stage 67 branch without overwriting local or remote work.
3. Read the Stage 66 final report, independent audit, exact result files, source manifest, and Stage 67 task setup. Rerun all Stage 66 Python and SageMath verifiers before extending the analysis.
4. Verify the exact Fourier convention and retain `S_w^2` for prime sums. `|S_w|^2` encodes prime differences and must not be substituted.

## 2. Main theorem target: rational-arc Gram geometry

For a finite set of distinct nonzero integer shifts `J` and a measurable arc union `E` on the circle, study the vectors
\[
g_j(\alpha)=e(-N\alpha)(e(-j\alpha)-1),\qquad j\in J.
\]
Derive the exact restricted Gram matrix
\[
G_E(j,k)=\int_E g_j(\alpha)\overline{g_k(\alpha)}\,d\alpha
\]
and its operator norm. Determine its dependence on arc centers, widths, rational denominators, and shift residues. In particular, separate reduced centers `a/q` with `q | j` from those for which the multiplier at the center is nonzero.

Prove any proposed Gram bound, identify equality cases or sharp counterexamples, and compare it to the full-circle matrix `I+11*` and the exact Stage 66 energy threshold. State whether any gain survives uniformly over the complete minor-arc set used by the cited prime theorem.

## 3. Arithmetic application and falsification

1. Apply the exact geometry to the genuine-prime coefficient
\[
m_w(N)=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)\,d\alpha.
\]
Keep the target phase and signed multiplier. Do not assume a representation exists at the target.
2. Determine whether the conditional global fourth moment, any cited localized moment, and the arc Gram operator can give a target-specific increment or block-energy estimate strong enough to exclude an isolated zero representation.
3. State exact uniformity in `N`, shifts, `X`, weights, arcs, constants, and zero-free hypotheses for every conditional claim.
4. Construct abstract extremizers whenever the available norm data allow an isolated bad target. Separate such countermodels from true prime counterexamples.
5. Keep the original residual set and three-case formulation unchanged. Wheel admissibility and singular-series predictions are not primality.

## 4. Deliverables

Save under `results/stage67/`:

- a rigorous report with proofs, hypotheses, counterexamples, and the first remaining analytic estimate;
- a reproducible Python/SageMath implementation and independent verifier for new exact identities;
- machine-readable exact data and a SHA-256 provenance manifest;
- an adversarial review recording invalid implications and circularity checks;
- a concise final assessment and the next justified research question.

Use exact rational or algebraic arithmetic for finite identities. Record commands, tested ranges, runtime, memory where available, and limitations. Do not expand finite Goldbach searches unless they test a new mathematical inequality.

## 5. Completion criteria

Complete all feasible milestones without routine check-ins: verify inherited work; prove the arc-Gram identities; test localization claims and sharpness; compare against actual prime-correlation inputs; document the remaining gap; independently reproduce results; commit and push only to the Stage 67 branch. Do not force-push, modify `main`, install software, incur costs, delete files, or claim universal coverage without a complete non-circular proof.

All repository content must be written in English.
