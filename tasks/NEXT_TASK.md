# NEXT TASK — Stage 65: target-localized signed Fourier bounds

**Mathematical status:** the author's original three-case universal coverage remains OPEN. The Stage 64 branch is cocalc/stage64-2026-minor-arc-gap. Create and work on the next research branch cocalc/stage65-target-localized-correlation, preserving all prior history and never modifying main.

## Research objective

Stage 64 reduced universal coverage on the residual set H to a signed, target-specific estimate for the true-prime minor-arc coefficient. A missing target forces a coefficient of size at least cX, while the reviewed global fourth moment only gives energy O(X^(5/2)(log X)^100), which permits a singleton.

Investigate whether a fixed-target localized Fourier kernel, short weighted shift average, or another exact localization device can improve the one-target bound without assuming R(N)>0.

## Required work

1. Read the Stage 64 final report, the exact Parseval derivation, its adversarial review, and the repository research protocol.
2. Define the prime-only smoothed coefficient and all Fourier sign conventions explicitly.
3. Derive an exact identity relating a weighted sum over shifts of minor-arc coefficients to the corresponding Fourier multiplier. Include normalization and endpoint conventions.
4. Determine the strongest pointwise coefficient estimate implied by the available global fourth-moment norm together with each stated kernel norm or regularity condition. Keep all X, logarithm, and shift-window dependencies explicit.
5. Search for counterexamples among abstract coefficient sequences satisfying the proposed norm and regularity constraints. Clearly distinguish such logical models from prime-arithmetic examples.
6. Test whether any additional smoothness or short-shift estimate is actually proved for the genuine-prime coefficients in the cited sources. Do not assume it from the smooth weight alone: the coefficient sequence still depends arithmetically on the target.
7. Preserve the original residual definition and three-case formulation. Do not assume an anchored representation, replace actual primes with wheel survivors, or infer pointwise positivity from an average.
8. Save a rigorous report, reproducible code, independent verification, exact results, and provenance manifest under results/stage65/.
9. State whether a new non-circular localization lemma is proved. If not, identify the first missing inequality and the exact scale that would suffice.
10. Commit and push only to the Stage 65 branch. Do not merge into main or overwrite earlier branches.

## Scope and completion standard

Prioritize a theorem about what follows logically from a global fourth moment and a precisely defined localizer. A conditional result is useful if every hypothesis is explicit and its premise does not encode R(N)>0. Finite computations are checks only. Universal coverage remains open unless a complete proof is independently verified.

All repository content must be in English. Do not install software, incur costs, delete files, force-push, or modify GitHub permissions.
