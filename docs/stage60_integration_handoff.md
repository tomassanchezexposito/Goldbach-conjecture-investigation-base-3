# Stage 60 — integration and analytic research handoff

**Status:** integration branch initialized from `cocalc/stage59-local-second-moment`. The three sibling branches have **not yet been consolidated**. Do not treat the existence of this file as evidence that merges have been performed.

## Source branches and immutable reference

- Stage 58 CoCalc supplement: `cocalc/stage58-pointwise-second-moment`, commit `689c3d696ce750610bed6ad69cdd476fdcaee464` (new weighted moment proofs and verified 620-row data). Review: https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/pull/7
- Stage 59 local cycle bound: `cocalc/stage59-local-second-moment`, including report, independent Python/C verification and original `tasks/NEXT_TASK.md`. Review: https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/pull/6
- Stage 59 path/multi-shift graph energy: `cocalc/stage59-sharp-local-energy`, including separate research note and three verifiers. Review: https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/pull/5
- Coordination issue: https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/issues/8

## Work only on this separate integration branch

1. Verify a clean working tree, fetch through explicit SSH key path (do not print any private key).
2. Check out `cocalc/stage60-integrated-research` tracking its remote.
3. Verify that the seven files from Stage 58 CoCalc are absent before applying the commit. Then `git cherry-pick 689c3d696ce750610bed6ad69cdd476fdcaee464`. If there are conflicts, stop and report before any overwrite.
4. Merge `origin/cocalc/stage59-sharp-local-energy` into this branch **with a merge commit**. Retain all distinct `results/stage59/` files and both mathematical approaches. If `tasks/NEXT_TASK.md` conflicts, resolve to the original Stage 60 objective in the parent branch and cite both Stage 59 protocols in a concise note. Do not silently drop either file set.
5. Run independently reproducible scripts from Stages 57, 58, and 59, including the native C test as resources permit. Compare reported outputs with independent checks. Do not rerun arbitrarily larger Goldbach ranges as a substitute for analytic progress.
6. Produce `results/stage60/integration_review.md` with exact file inventory, commit provenance, theorem-status table, unresolved estimates, test commands/results and any conflict resolution.
7. Only after a clean integration, study a signed, independently provable, **pointwise** bound for the true-prime four-position energy or a direct prime-pair lower bound, with all constants and exceptions. If known theorems do not supply it, specify the first missing inequality and report the exact dependence on N.
8. Save all new code, exact data and reports in `results/stage60/`, commit to this branch and push. Open a *draft* PR. Never merge into `main` or force-push existing branches.

## Mathematical evidence discipline

Proved: elementary wheel count, sharp finite-dimensional zero-moment inequalities, discrete graph-energy inequalities, and exact four-prime bookkeeping identities, subject to full verification of proof details.

Computational only: all finite observed nonzero prime-pair counts and numerical compliance with local-energy certificates.

Open: independent prime-correlation estimates adequate to prove `R(N)>0` for **each** residual even N. Neither positive average moments, finite wheel density, nor a finite search establishes this. Keep the author's three-case formulation unchanged.

All repository reports, source files and comments in English. Do not modify project files outside the new branch, install software or incur costs without approval.
