# Stage 69 — Theorem dependency and epistemic-status ledger

**Date:** 2026-11-10. **Source distinction:** M0–M7 originally authored by CoCalc Codex; M8–M9 independent connected review and exact Python checks. All statements below retain original quantifiers and do not imply the strong Goldbach conjecture.

| ID | Theorem/statement | Source | Status | Dependencies and limits |
|---|---|---|---|---|
| 69.0a | Two orthogonal diagonal projector vector and PSD-lift maximum both \(\sqrt2\) | \`00_independent_psd_erratum_audit.md\` | **PROVED** | Arithmetic of trace-one PSD matrices; Stage 68 claimed a false gap of 2 |
| 69.0b | Six Pauli projectors: pure maximum \(3\sqrt{1+\sqrt{2/3}}\), mixed \(3\sqrt2\) | \`00_erratum_psd_lifting.md\` and M0 audit | **PROVED** | Complex Hermitian \(2\times2\) matrices; no realization by prime arc Grams claimed |
| 69.1a | Exact genuine-prime ordered convolution \(\hat{S_w^2}(N)=\sum_{p+q=N}a_pa_q\) | \`01_prime_specific_exact_convolution.md\` | **PROVED** | Finite support, explicit weights, diagonal excluded on H |
| 69.1b | Exact von Mangoldt–prime-power correction \(U_w^2-S_w^2=2S_wQ_w+Q_w^2\) | M1 | **PROVED** | Same weight and finite support; crude bound depends on endpoints |
| 69.1c | Full-circle fourth moment \(\int |S_w|^4=\sum_n r_w(n)^2\) | M1 | **PROVED** | Parseval, ordered multiplicities; not a pointwise estimate |
| 69.2a | Sharp restricted Fourier coefficient \(|c(N)|\le\sqrt{\mu B}\) for arbitrary \(L^2(\mathfrak m)\) | \`02_information_hierarchy_and_no_go.md\` | **PROVED** | \(\mu=|\mathfrak m|>0\); arbitrary functions, not prime polynomials |
| 69.2b | Full-circle one-hole energy threshold \(B\ge |a|^2/(\mu\nu)\) | M2 | **PROVED** | \(0<\mu,\nu<1\), full-circle budget and prescribed major coefficient |
| 69.3a | Rational-center resonance \(q\mid j\) and signed shift Fourier identity | \`03_target_phase_and_arc_decomposition.md\` | **PROVED** | Distinct from an arithmetic gain; low-denominator minor-arc phrasing qualified by M8 |
| 69.4a | Exact finite CRT survivor density for \(x,N-x\) | \`04_residual_arithmetic_and_sieve_barrier.md\` | **PROVED** | Necessary modular compatibility only; prime endpoints exceptional |
| 69.4b | Shifted three-prime/shared-anchor and four-distinct partition | \`04_anchor_correlation_ledger.md\` | **PROVED** | Two distinct targets, unordered pairs, precise fourfold orientations |
| 69.5 | 2026 external prime exponential-sum and exception estimates | \`05_verified_primary_literature.md\` | **EXTERNAL / some CONDITIONAL** | ArXiv preprints, fixed weights, L-zero assumptions; abstracts independently checked by reviewer, not full proofs |
| 69.6a | Sharp fixed-exact-V energy envelope with breakpoint \(A^2(m+1)^2/m\) | \`06_sharp_target_criterion_and_robust_errors.md\` | **PROVED** | Arbitrary \(\ell^2\), m distinct shifts, \(|c(N)|\ge A\) |
| 69.6b | Sharp *upper-budget* energy lower bound and strict exclusion condition | M6 | **PROVED deterministic / CONDITIONAL for primes** | Must independently bound actual prime-only shift energy \(\bar V\), global energy \(\bar B\), positive major coefficient A |
| 69.7a | Global shifted fourth-moment bridge \(\int |S_w|^4e(-j\alpha)=\sum_n r_w(n+j)r_w(n)\) | \`07_bridge_and_comparison.md\` | **PROVED** | Global, no target selection |
| 69.7b | Candidate A: uniform signed minor coefficient below positive major bound | \`07_primary_analytic_route_A.md\` | **OPEN** | Strong enough to yield quantitative Goldbach under source hypotheses, but not established |
| 69.7c | Candidate B: uniform lower bound for reflected genuine-prime correlation | \`07_primary_arithmetic_route_B.md\` | **OPEN** | Would directly imply \(R(N)>0\) on H; sieve-wheel survivors not sufficient |
| 69.8 | Adversarial review, minor rational approximation erratum, exact regression | \`08_adversarial_review.md\` | **COMPLETED DOCUMENT REVIEW / FINITE CHECK** | Separate local Python runtime, not CoCalc or refereeing |
| 69.9 | Final synthesis, narrow future objective | \`09_final_synthesis.md\` | **COMPLETED DOCUMENT REVIEW** | Does not advance a new universal arithmetic bound |

**Proof-obligation chain:** Genuine-prime \(S_w^2\) identity (69.1a) + independently proved positive target major contribution + a **genuinely new target-uniform signed true-prime minor estimate** (OPEN 69.7b), or a sufficiently strong independently verified true-prime shift-energy bound for 69.6b, would yield \(R(N)>0\) on H. No cited existing moment/exceptional-set theorem discharges the missing bound.

**Finite-verification status:** seven weighted residual targets; 21 distinct-target correlations; 252 exact energy instances; one exact minor-arc denominator example, in \`verify_m8_independent.py\` and its output. These checks are *not* evidence that all remaining even targets have prime pairs.

**Conjecture status:** \(\forall N\in H:R(N)>0\) **OPEN**. Do not merge to main solely because the M8/M9 internal review is complete.
