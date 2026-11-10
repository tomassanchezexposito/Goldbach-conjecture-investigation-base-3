# Stage 69 — target-localized prime energy and signed correlation obstruction

## Research objective

Stage 68 proved that arcwise Hilbert-space allocation is exactly computable, that a total fourth-moment budget collapses to the full-minor operator norm, and that the growing-shift Gram geometry has no uniform relative saving. The missing step is arithmetic: a target-uniform estimate for the actual prime-square input, or a rigorous obstruction showing why available analytic inputs cannot reach the Stage 66/68 threshold.

This stage must investigate one narrower question: **can a genuinely prime-specific theorem localize either the signed increment vector or the fourth-moment mass to target-dependent rational-arc cells strongly enough to exclude one isolated zero representation?** Preserve the original three-case formulation and do not assume a representation at the target.

## Required setup and deliverables

1. Follow the repository workflow to select or create the Stage 69 research branch from the verified research base. Verify a clean tree; fetch with the existing dedicated SSH identity and `IdentitiesOnly=yes`; preserve every prior branch and file. Do not modify `main`.
2. Read this file, `results/stage68/final_report.md`, `results/stage68/04_arc_budget_feasibility.md`, `results/stage68/07_primary_analytic_attempt.md`, `results/stage68/08_adversarial_review.md`, and the relevant Stage 63–67 dependency documents.
3. Keep the exact definitions of the residual set `H`, representation count `R(N)`, smooth prime polynomial `S_w`, major/minor coefficient split, and even shifts from the earlier reports. Re-derive the Fourier signs before use. The prime sum is encoded by `S_w^2`, not `|S_w|^2`.
4. Save a complete report, exact code/data when useful, independent verification, source/dependency ledger, counterexample record, and an adversarial review under `results/stage69/`.

## Mathematical milestones

### M0 — re-audit the Stage 68 target threshold

Re-derive the sharp finite-dimensional inequality from center value and increment energy, including equality configurations. State exactly the independent uniform hypotheses that would imply positivity, with constants and the shifted index range. Test the formula against small exact rational examples and boundary cases (`V=0`, threshold equality, and `V>=mA^2`).

### M1 — target-dependent arc partition

Define a genuinely disjoint partition of the minor arcs into rational-center cells or shells, with explicit treatment of overlaps, reflected cells, the final shell, and denominators dividing an even shift. For each cell derive the exact increment Gram and all available operator-norm bounds. Determine whether the target phase can be retained in the optimization instead of discarded by Cauchy–Schwarz. State what arithmetic information a prime theorem would have to add.

### M2 — localized fourth moment versus signed coefficient

Audit available unconditional and conditional prime exponential-sum estimates for localized forms such as
`integral_E |S_w|^4`, signed integrals `integral_E S_w^2 e(-N alpha)`, and cross-cell covariance. Do not infer targetwise bounds from averages or from the total moment. For every candidate estimate, write its exact quantifiers, weight, modulus/arc, target, shift, zero-free, and constant dependencies. If literature retrieval is unavailable, use checked repository sources and say so; do not invent citations.

### M3 — two distinct proof routes or explicit failure

Develop two mathematically distinct routes toward the required target estimate, for example (i) a signed Fourier/circle-method decomposition with all complementary arcs controlled, and (ii) a local-energy/covariance or bilinear-prime route. Each route must end in either a complete lemma with proof and usable constants, or an explicitly identified first missing estimate. Avoid circularly assuming positivity of the target coefficient or a prime-pair factor.

### M4 — adversarial falsification

Test each proposed implication using exact finite-dimensional countermodels, boundary cases, arithmetic congruence constraints, and any justified small exact computations. Distinguish an abstract coefficient sequence from the genuine prime sequence. Refute invalid transitions such as average-to-supremum, modular admissibility-to-primality, selected-arcs-to-complement, and a four-position lower bound that already encodes the target pair.

### M5 — literature and dependency audit

Use the Stage 68 source ledger as the baseline. Check the exact hypotheses and current versions of every source actually used; separate fresh inspection from inherited notes. State whether a theorem is unconditional, conditional, an external claim, or not independently verified. Do not claim novelty from an unsearched literature space.

### M6 — integrated result and next objective

Give a precise theorem/proof if one is obtained. Otherwise state the strongest conditional theorem, the exact first missing arithmetic estimate, and a quantitative comparison with the pointwise threshold. Preserve the original three-case statement verbatim in the report and explicitly label universal coverage OPEN unless proved non-circularly. Propose the next research stage based on the most informative outcome.

## Pointwise threshold to meet

Let `a_w(N)` and `m_w(N)` be the major and minor coefficients and let `J` contain `m` distinct nonzero even shifts. If a zero representation forces the full nonnegative weighted coefficient to vanish, if `a_w(N)>=A_X>0`, if the global minor energy is at most `B_X`, and the signed increment energy is at most `V_X`, then the sharp necessary lower energy under the zero hypothesis is

`A_X^2 + m * (A_X - sqrt(V_X/m))_+^2`.

A contradiction follows only when this is strictly greater than `B_X`. Stage 68's source chain gives global scale `B_X ~ X^(5/2)(log X)^100` and major scale `A_X ~ X` under its stated conditional hypotheses. The generic Hilbert bound does not close the resulting target-specific gap. Recompute constants if using another weight or source theorem; do not treat big-O constants as numerically favorable.

## Restrictions and completion criteria

- No prime representation at the target may be assumed or used in normalization.
- Keep the author's original three cases unchanged; distinguish `N=p+1`, `N=2p`, and `N=p+q, p<q`.
- Do not claim universal Goldbach coverage absent a complete non-circular proof.
- No main-branch edits, force pushes, destructive Git operations, new credentials, software installation, or additional costs.
- Use English for every repository artifact and commit message.
- Commit and push verified milestones only to the Stage 69 branch using the existing dedicated SSH key.
