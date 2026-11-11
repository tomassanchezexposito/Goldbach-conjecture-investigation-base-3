# Stage 71 — Review checkpoints and execution provenance

**Date:** 2026-11-11. **Branch:** `cocalc/stage71-sharp-deletion-sensitivity`.  
**Work origin:** Direct ChatGPT mathematical research, a local Python runtime, and the connected private GitHub integration. **No CoCalc/Codex quota consumed.** No timer, scheduled/background agent, or unattended work started.

## Proven research cycle

- A Stage 71 branch was created from the audited Stage 70 branch, without touching `main`.
- `01_exact_target_robustness_and_lp.md` proves the sharp matching-deletion radius in `l^s`, the complete cost/remaining-target greedy curve with two mathematical proofs, and the exact reflected-gradient identity.
- The same paper proves, from established Wu upper-sieve/PNT input, asymptotic **relative** proximity in all fixed global Fourier `L^q` norms for the modified prime-supported polynomial and its square, despite an exactly missing target coefficient in that modified input.
- A separate adversarial audit `02_adversarial_review.md` diagnoses the sharpness hypotheses and precisely explains why this **does not** give an actual Goldbach counterexample or target-uniform lower bound.
- The executable `verify_stage71.py` was actually run with Python 3.13.5, then the GitHub source was checked to be **byte-identical** to the executed file using `git hash-object`. The same was done for `exact_results.json`. Source SHA-256: `b9decd6f739f9c734589ddc7408bba7781a9dcaac98b876e039f9c5d282b5aa0`; output SHA-256: `50840ea61f45811cbf961bab0d83e89559b060a70ad650f61fa6313a1d98ba0b`.
- The exact validation covers only 15 integer-budget cases for the two-endpoint deletion DP and five explicitly residual finite targets for weighted convolution/Young's inequality; the **general proofs** do not rely on this sample size.
- `verification_manifest.json` records source provenance, external established theorems and the original target-status limitations.
- `final_report.md` consolidates the theorem strengths, exact limiting comparison and next research need.
- `tasks/NEXT_TASK.md` stores **Stage 72 as a proposal**, with no agent started.

## Scientific labels

**PROVED:** exact matching and weight-attenuation optimization; exact reflected convolution perturbation; normalized Fourier/Lp closeness as a deduction from cited established unconditional external bounds.

**EXTERNAL established:** J. Wu (2004) **upper** Goldbach sieve; classical prime number theorem, (N/\varphi(N)) estimate; elementary Fourier/Young inequalities.

**FINITE:** independent Python exact budget/weighted convolution regressions.

**OPEN:** genuine fixed full-prime target `R(N)>0` for every residual H, and independently proved signed target-specific prime error estimate.

**Publication:** keep the Stage 71 PR in **DRAFT**; no public proof announcement, merge or modification of past research history.
