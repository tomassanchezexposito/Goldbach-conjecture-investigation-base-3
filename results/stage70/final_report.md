# Stage 70 — Consolidated mathematical report and next proof obligation

**Research date:** 2026-11-10. **Branch:** \`cocalc/stage70-positive-spectrum-cone-audit\`.  
**Provenance:** All Stage 70 mathematics and exact rational checks were performed with ChatGPT and its local/connected tools **without consuming CoCalc Codex quota**. External theorems cited are not newly proved.  
**Original mathematical target:** \(\forall N\in H,\ R(N)>0\), with \(H=\{N\ge4:\text{N even},\ N-1,N/2\text{ composite}\}\), \(R(N)=\#\{p<q:p,q\text{ genuine primes},p+q=N\}\). **OPEN.**

## A. What Stage 70 has actually established

**T70.1 — exact cone inequality (PROVED, functional analysis).** For a nonnegative-coefficient Fourier polynomial on a predetermined finite frequency band, a reflection-symmetric major set and a missing central coefficient, the sharp full-circle energy lower bound is
\[
B\ge\frac{a(N)^2}{D_+(N)},\quad
D_+(N)=\sum_{k\ne N}\max\{\widehat{1_M}(N-k),0\}^2.
\]
This is stronger than the unrestricted complex coefficient bound. It does **not** impose the nonlinear factorization \(F=S_{\rm actual\ primes}^2\).

**T70.2 — half-mass matching deletion (PROVED, finite graph).** For any finite weighted genuine-prime support and target N with no prime diagonal, a matching choice preserves at least half the original total weight, destroys all target representations in the *modified* support and does not increase full fourth-moment energy. Not a Goldbach counterexample.

**T70.3 — actual major-arc Fejér lower bound (PROVED, elementary Fourier).** For \(P=X^\kappa,\ 0<\kappa<1/2\), the true symmetric major arcs and predetermined full even-frequency band, uniformly in even N∈[X/2,X],
\[
D_+(N)\ge P/(50X)
\]
for sufficiently large X. The proof exploits only the q=1 major-arc core and a triangular/Fejér Fourier test with exact signs.

**T70.4 — unconditional no-go for the *specific full-circle cone certificate* (PROVED using classical PNT).** For a fixed nontrivial nonnegative \(w\in C_c^\infty((0,1))\), classical PNT gives \(\int_{\mathbb T}|S_w|^4\gg_w X^3\); independently \(|a_w(N)|\ll_w X(\log X)^2\). Therefore
\[
\frac{\bigl(\int_{\mathbb T}|S_w|^4\bigr)D_+(N)}{|a_w(N)|^2}
\gg_w \frac{X^\kappa}{(\log X)^4}\to+\infty
\]
whenever a_w(N)≠0. Hence the strict sufficient test \(B_XD_+(N)<A_X^2\) cannot be true eventually, even with **exact actual** full-circle energy and actual major coefficient (and thus not with any weaker valid bounds). This rules out the proposed *relaxed* proof certificate, **not the circle method generally** and not a nonlinear prime-factorization theorem.

**T70.5 — asymptotically vanishing relative prime-weight deletion (PROVED deduction from established external sieve/PNT theorems).** Wu's unconditional Goldbach **upper** sieve theorem (Acta Arith. 114.3 (2004), Theorem 1), plus the classical bound \(N/\varphi(N)\ll\log\log N\), gives
\[
R(N)\ll N\log\log N/(\log N)^2,\quad N\in H.
\]
Deleting the lighter endpoint from every complementary prime edge then loses at most \(O_w(X\log\log X/\log X)=o(X)\) weighted mass, uniformly for N∈H∩[X/2,X], while producing **zero** at the target in the **modified** prime-supported polynomial. Thus it preserves \(1-O_w(\log\log X/\log X)\) of the original prime mass and does not increase full fourth-moment energy. By PNT in each **fixed** arithmetic progression, the modified supports still have the same first-order weighted prime asymptotics in each fixed reduced class. The retained set, however, is **not** the true complete fixed prime support.

## B. Falsified reasoning strategies and the exact first invalid inference

- A full-circle positive-spectrum cone energy certificate using the entire even band **cannot** provide the needed strict inequality; the Fejér positivity test forces its denominator to be too large even before prime-specific arithmetic is considered.
- Treating the 2026 *minor-only* fourth-moment upper estimate as a full-circle energy upper bound is categorically invalid: the full energy is \(\gg X^3\).
- Even preserving \(1-o(1)\) of prime mass, all first-order prime asymptotics in every fixed progression, allowed prime frequencies and a nonincreasing fourth moment does not force a representation when *deletion* is permitted. The first false inference is that an average/density constraint controls the pairwise reflected indicator \(1_{\mathbb P}(p)1_{\mathbb P}(N-p)\).
- None of these countermodels represents the complete actual-prime polynomial with its mandatory fixed coefficients. Consequently **none refutes Goldbach**.
- A uniform signed prime-only minor-arc estimate would still suffice when combined with a valid positive major input; no such estimate is established.

## C. Source and reproducibility status

- \`01_positive_spectrum_and_matching.md\`: T70.1–T70.2 and first exact verification.
- \`02_adversarial_limits.md\`: first-cycle countermodel and qualification.
- \`03_actual_arc_cone_nogo.md\`: T70.3–T70.4 complete proofs.
- \`04_actual_arc_adversarial_review.md\`: independent proof scrutiny.
- \`05_vanishing_mass_prime_deletion.md\`: T70.5, Wu citation, singular-series upper bound and fixed-q consequence.
- \`verify_stage70.py\` and \`exact_results.json\`: exact positive-cone and matching checks.
- \`verify_stage70_arc_nogo.py\` and \`arc_nogo_exact_results.json\`: **actually executed** exact fraction checks of four parameter/window configurations, not a universal proof.
- \`verification_manifest.json\`: Git blob and SHA-256 hashes, software scope, caveats.
- Standard Fejér formula: https://dlmf.nist.gov/1.15 and https://www2.math.upenn.edu/~gressman/analysis/08b-summability.html .
- J. Wu (2004), primary original paper https://www.impan.pl/shop/publication/transaction/download/product/82961 . Theorem 1 states an unconditional \(\ll C_NN/\log^2N\) Goldbach **upper**, not lower, bound.
- Classical PNT/PNT in fixed arithmetic progressions and \(N/\varphi(N)\ll\log\log N\) are established *external* theorems, not proved anew here.

## D. One scientifically narrow next question

All the classes above permit coefficient manipulations that the actual fixed prime polynomial does **not** permit. Next, investigate a **quantified theorem that detects or forbids the specific complement-matching deletions** while using only independently established facts about genuine primes.

One possible research framework is a signed residual
\[
\mathcal C_N=\sum_{p\text{ prime}}\bigl(1_{\mathbb P}(N-p)-\text{an independently justified analytic approximation}\bigr)\,a_p
\]
with rigorously controlled sign or error at each prescribed residual N. But an approximation whose error is already required below a positive binary-prime main term is itself nearly the sought Goldbach conclusion; it must be *proved independently*, not postulated. A second option is a higher-dimensional factorization/Toeplitz estimate retaining the **all-prime fixed coefficients**, with a quantitative gap that does not vanish too fast as X grows.

Do **not** spend the next research cycle optimizing D_+ again or increasing finite Goldbach test ranges. Its inability to close the problem with the broad band and full-circle energy is now proved.

**Final status:** Stage 70 internally reviewed and complete; primary Goldbach question OPEN. PR remains draft, \`main\` is untouched, and no Codex/automation is running.
