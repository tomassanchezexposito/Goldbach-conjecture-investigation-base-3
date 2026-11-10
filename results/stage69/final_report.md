# Stage 69 — Final integrated mathematical report and review closure

**Review completed:** 2026-11-10.  
**Working branch:** \`cocalc/stage69-deep-prime-specific-localization\`.  
**Draft PR:** https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/pull/18  
**Provenance:** CoCalc Codex published the underlying M0–M7 investigation. The connected ChatGPT reviewer completed M8–M9 with a separate local exact verification. This does not consume the user's weekly CoCalc/Codex allowance.

## Executive mathematical conclusion

**No universal Goldbach or original three-case proof has been obtained.** The unresolved target remains every even
\[
N\in H=\{N\ge4:\ N-1\text{ composite},\ N/2\text{ composite}\}
\quad\Longrightarrow\quad
R(N)=\#\{p<q:p,q\text{ genuine primes},\,p+q=N\}>0.
\]
The base-3-related odd-prime position map \(p=3+2a\) and the reflection equality are retained without confusing them with primality. The rigorous progress is in *mathematical reductions, sharp conditions, and a more accurate diagnosis of the missing true-prime theorem*.

### PROVED internally and independently audited

1. **PSD relaxation correction.** Two orthogonal diagonal rank-one projectors have vector and lifted optima both \(\sqrt2\), while the naive termwise upper bound is 2. A six-Pauli-projector example establishes a real strict lift gap **in abstract Hermitian geometry**, not for genuine prime arcs.
2. **Exact genuine-prime convolution.** \(r_w(N)=\sum_{p+q=N}(\log p)(\log q)w(p/X)w(q/X)\). For N in H the equal-prime diagonal is absent. \(S_w^2\), not \(|S_w|^2\), encodes sums. Prime powers are accounted for explicitly when an auxiliary \(\Lambda\)-weighted polynomial is used.
3. **Sharp target energy condition.** A center \(|c(N)|\ge A\) and distinct shifts with squared increment energy at most \(\bar V\) enforce
   \[
   \|c\|_2^2\ge A^2+m(A-\sqrt{\bar V/m})_+^2.
   \]
   The exact-energy optimization has a distinct piecewise formula; the bound is not sharp for fixed \(V>mA^2\), although it is sharp for a known upper budget. Strictness of the final contradiction is essential.
4. **Global fourth-moment bridge.** \(\int_{\mathbb T}|S_w|^4 e(-j\alpha)=\sum_n r_w(n+j)r_w(n)\). This is an average over targets, not a selected-target nonvanishing theorem.
5. **Information-class sharpness.** An unrestricted \(L^2\) function with major/minor measures \(\nu,\mu>0\), specified major coefficient a and absent full coefficient requires full-circle squared energy at least \(|a|^2/(\mu\nu)\). Its extremizers generally do not have the finite fixed-prime-square structure. **A minor-only moment bound cannot substitute for full-circle energy.**

### REFUTED or corrected

- The Stage 68 claim of a strict PSD lift gap in the two-diagonal-projector example was false; the M0 correction is rigorous.
- A Stage 69 sentence suggesting that all "relevant" rational approximants to minor-arc points must have denominator \(>P\) is too broad without a specified approximation algorithm. An exact minor-arc point \(\alpha=1013/3000\), \(P=13\), \(X=2000\) has nearest reduced low-denominator center \(1/3\). The center resonance theorem remains valid.
- Abstract minor-arc norm, positive coefficient spectrum, finite wheel, and exceptional-set cardinality inputs cannot alone exclude a single target zero.
- A positive anchored four-prime correlation does not become a *proved lower bound* simply by factoring it into products containing the unknown target representation count.

### EXTERNAL and CONDITIONAL

The Li–Liu October 2026 preprint's conditional global minor fourth moment has an upper-bound scale \(X^{5/2}(\log X)^{100}\) under its uniform Dirichlet-L zero hypothesis. The pointwise Cauchy bound derived from that estimate is only \(O(X^{5/4}(\log X)^{50})\), too large to compare with a positive major-arc contribution on the \(X\)-scale. The newer 2026 arXiv exceptional-set bounds still allow isolated exceptions. The published Bhowmik–Grimmelt review/major-arc formula does not remove them either. This review independently checked the available arXiv abstract/version records but **has not rebuilt claimed Lean proofs or re-proved these external analytic estimates**.

### OPEN

The first necessary new arithmetic input is a **target-uniform, independently established, signed prime-only minor-arc estimate** or a quantitative restriction on genuine-prime shift correlations that pushes the sharp center-energy certificate strictly past the available global energy upper bound. Neither route M7A (phase-sensitive circle method) nor route M7B (direct two-prime reflected correlation) has provided it.

## Independent verification: executed, not inferred

In a separate local Python 3.13.5 runtime (not CoCalc) the reviewer ran \`verify_m8_independent.py\` as mirrored in this branch. The regression used exact integers and fractions and passed:

| Check | Cases | Scope |
|---|---:|---|
| Weighted unordered-vs-ordered prime-pair identities | 7 residual even targets | Finite identity audit |
| Shifted shared/four-distinct decompositions | 21 target pairs | Finite multiplicity audit |
| Exact-center-energy and upper-budget relations | 252 rational cases | Finite optimization audit |
| Rational minor-arc counterexample | P=13, X=2000, one point | Exact logical counterexample to unqualified wording |

Previous CoCalc Stage 69 verification scripts and source records were published in M0–M7; the M8 script is **additional**, not a claim that all of those prior scripts were rerun here. A successful finite audit does not validate a universal prime estimate. The GitHub branch and commit history preserve source provenance.

## Documentation and dependencies

- \`00_erratum_psd_lifting.md\`, \`00_independent_psd_erratum_audit.md\`: original abstract matrix correction and independent proof.
- \`01_prime_specific_exact_convolution.md\`: exact prime-support formulas and prime-power correction.
- \`02_information_hierarchy_and_no_go.md\`: sharp two-arc norm bound with hypotheses.
- \`03_target_phase_and_arc_decomposition.md\`: signed rational-arc setup; qualifying erratum now in M8.
- \`04_anchor_correlation_ledger.md\`, \`04_residual_arithmetic_and_sieve_barrier.md\`: exact prime configuration identities and sieve limits.
- \`05_verified_primary_literature.md\`: prior CoCalc source audit (conditionally imported).
- \`06_sharp_target_criterion_and_robust_errors.md\`: sharp energy and error thresholds.
- \`07_primary_analytic_route_A.md\`, \`07_primary_arithmetic_route_B.md\`: *open* independent attempts.
- \`08_adversarial_review.md\`, \`09_final_synthesis.md\`: completed separate reviewer audit and final synthesis.
- \`verify_m8_independent.py\`, \`m8_independent_exact_results.json\`: focused exact recheck.
- \`review_verification_manifest.json\`, \`checkpoint_log.md\`: source provenance and explicitly separated execution/review checkpoints.
- \`tasks/NEXT_TASK.md\`: narrow Stage 70 handoff, **queued but not executed**.

## What happens next

The research user has limited remaining weekly Codex allowance. **No new Codex run or automatic monitoring has been started.** The preferred next mathematical problem is to test whether the *finite fixed genuine-prime polynomial-square structure* supplies a quantitative target-uniform separation from the unrestricted \(L^2\) one-hole extremizer, instead of continuing to optimize the same abstract arc norms.

The M0–M9 internal **document review is closed**, while PR #18 remains a **draft pending external/scientific acceptance and any later CoCalc replay**. Neither \`main\` nor any historical research branch has been merged or overwritten.
