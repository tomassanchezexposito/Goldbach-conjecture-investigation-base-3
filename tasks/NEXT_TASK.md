# NEXT TASK — Stage 66: sharp local modulus, genuine-prime signed increments and independent proof gap

**Status:** original three-case conjecture remains OPEN. Research branch \`cocalc/stage66-sharp-local-energy-modulus\`, descended from the completed Stage 65, is pre-created and contains a new proved deterministic theorem and exact verifier. Preserve all history and never merge into \`main\` without approval.

## 0. Start safely, confirm sources and independently verify the new lemma

1. In the existing CoCalc clone \`/home/user/goldbach-research-github\`, ensure the working tree is clean and fetch the latest branch using the dedicated GitHub SSH key with \`IdentitiesOnly=yes\`. Do not disclose credentials.
2. Check out the existing \`cocalc/stage66-sharp-local-energy-modulus\` branch. Read \`results/stage66/00_sharp_modulus_energy.md\` and \`results/stage66/verify_stage66.py\` and run \`python3 -B results/stage66/verify_stage66.py\`. Check its output and both the theorem and proof **independently**, without trusting the code's own claims.
3. Read \`results/stage65/final_report.md\`, \`results/stage65/02_fourier_localization_limits.md\`, the Fourier sum/difference erratum, and Stage 64 literature hypotheses. Verify the essential corrected \`S_w^2\` versus \`|S_w|^2\` distinction. Rerun Stage 65 tests where feasible.
4. If any error is found in the new theorem, record the first faulty implication, correct the report in a transparent new commit on this branch and stop using the inaccurate version.

## 1. Main exact mathematical theorem to investigate

For a specified center coefficient \(|c(N)|\ge A>0\), finite *distinct* shifts \(h\in I\) and independently bounded increments \(|c(N+h)-c(N)|\le d_h\), the proved sharp deterministic energy inequality is
\[
\|c\|_{\ell^2(\mathbb Z)}^2
\ge A^2+\sum_{h\in I}(A-d_h)_+^2.
\]
The extremizer in the *arbitrary-sequence class* is \(c(N)=-A\), \(c(N+h)=-(A-d_h)_+\), zero elsewhere. This proves exact necessity and sufficiency for existence of an abstract coefficient sequence under a global energy budget; it does NOT prove anything about the availability of such a sequence from primes.

For parity-preserving shifts \(\{\pm2,\ldots,\pm2H\}\) with \(|c(N+2h)-c(N)|\le L|h|\), derive and independently verify the exact closed formula
\[
B\ge A^2+2\sum_{h=1}^H(A-Lh)_+^2
=A^2+2\left[JA^2-ALJ(J+1)+\frac{L^2J(J+1)(2J+1)}6\right],
\quad J=\min(H,\max(0,\lceil A/L\rceil-1))
\]
for \(L>0\), with the \(L=0\) case \((2H+1)A^2\).

**Research questions:** Is there a genuinely weaker and independently provable arithmetic *aggregate* modulus (not a pointwise Lipschitz assumption) that still forces the energy to exceed the available global fourth moment at a single missing target? Analyze the exact optimal constants and distinguish the fixed-target inference from a global exceptional-set argument.

## 2. Independent arithmetic problem: actual genuine-prime minor-arc increments

With the corrected prime-only coefficient
\[
m_w(N)=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)\,d\alpha
\]
derive for every integer h:
\[
m_w(N+2h)-m_w(N)
=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)(e(-2h\alpha)-1)\,d\alpha.
\]

The global fourth-moment bound from Li–Liu **is conditional on the stated common uniform zero-free hypothesis** and gives \(B_X\ll X^{5/2}(\log X)^{100}\), not a pointwise signed estimate. The independently positive major arc, under its source assumptions, gives \(A\asymp cX\). Prove precisely the missing compatible increment scale, e.g. \(L\) smaller than a constant times \(X^{1/2}(\log X)^{-100}\) with adequate shift span \(H\gtrsim A/L\), or identify an alternative sufficient modulus.

Every new conjectural estimate must state exact uniformity in N, h, X, weights, arcs, and constants. Distinguish even-step increments \(\Delta_2m_w(N)\) from one-step increments, since even and odd prime-pair targets behave differently. Never presume that actual prime representations exist.

## 3. Explore four genuinely different lines, stop unproductive ones early

A. **Optimized abstract modulus**: derive a sharp theorem for nonuniform \(d_h\), weighted aggregate shift variation, or discrete Sobolev energy (no hidden positivity), and compare logically to the Fejér criterion. Seek extremizers.

B. **Fourier geometry**: derive exact multiplier \(e(-2h\alpha)-1\), separate arcs and rational centers, and test whether the existing moment bound offers any *localized* gain. Do not replace \(S_w^2\) by \(|S_w|^2\). Check signs and whether the bound acts on the entire minor set, not just near 0.

C. **True-prime four-position correlations**: expand the signed squared increments into true-prime representation quadruples plus contractions. Specify diagonal/shared-position multiplicities, normalization, and how the arithmetic sign would be controlled independently. Do not infer primality from 210-wheel survivors.

D. **Original residual arithmetic**: evaluate the factorization conditions \(N-1\) and \(N/2\), the base-3 position coordinate \(3+2a\), and full singular series for a target-specific increment estimate; audit parity-barrier arguments and Stage 62's model obstruction. Demonstrate a genuinely new restriction or explicitly refute the proposed inference.

## 4. Deep external contrast and active falsification

Consult exact theorem statements in the 2026 Li–Liu, Pintz–Althöfer and Bhowmik–Grimmelt sources where available; include source dates/status and all uniform zero-free assumptions. Check whether any available theorem actually controls a fixed even target, a signed increment, or a sufficiently localized weighted energy. A large averaged moment that allows a singleton is insufficient.

Test *new* claims with exact finite mathematical examples or rational abstract sequences using at least two independent methods (Python+SageMath when available). Explicitly classify numerical observations versus proofs. If a proposed bound fails, record the first invalid step and counterexample promptly. Avoid merely extending the finite Goldbach range.

## 5. Milestones and durable output for user absence

Proceed through all feasible milestones M0–M5 **without routine user check-ins** inside CoCalc's existing runtime and allowance limits, checkpointing each independently verified result on this research branch.

- M0: audit Stage 65 and verify Stage 66 prewritten theorem/finite regression.
- M1: independently prove sharp arbitrary-modulus lower bound and compute optimal even-step threshold.
- M2: derive exact Fourier/correlation expansion and investigate sign-preserving arithmetic input.
- M3: attack aggregate/discrete energy or analytic localization as a less restrictive substitute for Lipschitz; reject circular routes.
- M4: external theorem and assumptions audit, independent countermodels, proof-dependency ledger.
- M5: complete rigorous integrated report, independent verifier, code/data/source hashes, next mathematically justified Stage 67 task and draft PR (no automatic merge).

Save all new work in \`results/stage66/\`: \`01_review_and_proofs.md\`, \`02_arithmetic_modulus.md\`, \`03_fourprime_signed_energy.md\`, \`04_countermodels_and_literature.md\`, \`05_independent_audit.md\`, \`final_report.md\`, reproducible scripts/results, a SHA-256 provenance manifest and \`checkpoint_log.md\`. The prewritten \`00_sharp_modulus_energy.md\` and \`verify_stage66.py\` must remain fully reviewable. Update \`tasks/NEXT_TASK.md\` for Stage 67 *only after* the work is genuinely completed. Commit and push milestone checkpoints as feasible.

**No** installation, spending, credential changes, destructive Git commands, force-push, unreviewed merge to main or public claim of resolving Goldbach. Every source file and GitHub report must remain in English. No guarantee of uninterrupted multi-hour execution is made.

**Mathematical success:** either an independently proved genuine-prime modulus sufficiently strong to exclude a missing residual target, or the sharpest rigorously established deterministic theorem with a precise unsolved true-prime estimate and documented failure of candidate approaches. Do not label conditional/finite results universal.
