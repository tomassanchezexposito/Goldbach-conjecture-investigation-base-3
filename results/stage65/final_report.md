# Stage 65 — Corrected Fourier localization and prime-correlation gap

**Branch:** `cocalc/stage65-corrected-fourier-localization`
**Classification:** exact Fourier corrections and localization identities; a deterministic limitation and a non-circular conditional criterion; no new unconditional prime estimate.

## A. Proven mathematical results

For $S_w(\alpha)=\sum_p a_pe(p\alpha)$, the coefficient of $S_w^2$ at $N$ counts weighted ordered prime sums $p+q=N$, while the coefficient of $|S_w|^2$ counts weighted differences $p-q=N$. Their major/minor arc integrals cannot be interchanged. The $N=8$ polynomial example gives coefficients 2 and 0. Parseval for the minor-arc coefficient sequence still yields the fourth moment $\int_{\mathfrak m}|S_w|^4$.

For every finite shift sequence $\lambda$, the exact target identity is
\[
\sum_h\lambda_hm_w(N+h)=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)K_\lambda(\alpha)\,d\alpha,
\quad K_\lambda(\alpha)=\sum_h\lambda_he(-h\alpha),
\]
and full-circle Parseval gives $\|K_\lambda\|_2^2=\sum_h|\lambda_h|^2$. The stated Dirichlet and Fejér coefficient-weight sums, circle integrals, norms, and first absolute moments follow by exact finite sums.

If the only information is a global coefficient-energy bound, it cannot exclude an isolated coefficient of size $cX$ when the energy budget is $CX^{5/2}(\log X)^{100}$. Any exact linear recovery of the center has central weight one and $\ell^2$ norm at least one; a normalized averaging kernel attenuates a singleton by its central weight. These are deterministic statements about the class of abstract sequences, not arithmetic counterexamples.

Under a valid major-arc lower bound $a_w(N)\geq cX$, a conditional pointwise conclusion follows from the independently assumed shift estimate $|m_w(N+h)-m_w(N)|\leq L_X|h|$ and the Li–Liu fourth moment if
\[
\sqrt{C_4}X^{5/4}(\log X)^{50}\sqrt{\frac{2H^2+4H+3}{3(H+1)^3}}
+L_X\frac{H(H+2)}{3(H+1)}<cX.
\]
This condition itself does not assume a representation at $N$ or its neighbors. It has not been shown to hold for the actual prime coefficients.

## B. Computational observations

The exact regression passes at all 16 frequencies modulo 97 using direct pair enumeration and an independent DFT. Python `Fraction` checks verify the normalized kernels for $0\leq H\leq16$, the signed finite shift identity, and a negative singleton model. SageMath 10.9 independently verifies a length-32 DFT modulo 97, the product coefficient, Parseval, and the Fejér norm numerators. Inherited Stage 63 and Stage 64 verifiers also pass; exact commands and outputs are in `checkpoint_log.md`, and source hashes are in `source_manifest.json`.

The exact local arithmetic example is $A_{210}(210)=A_{210}(420)=48$ and both full singular series have the same finite odd factor $16/5$. Yet 210 lies in $H$ and 420 does not. This is a finite factorization observation, not evidence against Goldbach.

## C. Refuted approaches and first invalid steps

- **Fourier substitution:** replacing $S_w^2$ by $|S_w|^2$ changes sums into differences. This invalidates the original arc-coefficient identity; see `00_erratum.md`.
- **Global moment implies no exceptions:** thresholding yields a possible exceptional count of order $X^{1/2}(\log X)^{100}$, not zero. Replacing that diverging upper bound by zero is invalid.
- **Average implies center:** a singleton survives the global norm while its normalized shift average tends to zero relative to its central value. The missing step is independent local regularity.
- **Residual factors force a prime pair:** CRT and singular-series factors describe local admissibility; they do not prove primality. The 210/420 example rules out factor-only recovery of residual membership.
- **Anchored correlation:** choosing a prime representation at the target under investigation assumes $R(N)>0$ and is circular.

## D. Conditional results

The Fejér criterion above gives a sufficient condition for positivity when its hypotheses hold. For large $H$, the competing requirements are approximately
\[
H>\frac{2C_4}{3c^2}X^{1/2}(\log X)^{100},\qquad H<\frac{3cX}{L_X}.
\]
Thus one needs shift regularity roughly stronger than $L_X<(9c^2/(2C_4))X^{1/2}(\log X)^{-100}$, with strict quantitative margins. The fourth-moment and major-arc inputs themselves are conditional on the common zero hypothesis recorded in the dated Stage 64 source audit.

## E. Remaining analytic obstruction

There is no established, non-circular, target-uniform bound for the signed true-prime increment $m_w(N+h)-m_w(N)$ at the scale needed by the Fejér criterion, nor a target-specific estimate proving $m_w(N)>-a_w(N)$. Existing exceptional-set and global moment estimates permit a singleton exception. No new true-prime four-position lower bound was found. Universal positivity for $N\in H$, and hence the author's original three-case conjecture, remains unproved.

## F. Next research objective

Seek a uniform additive shift-modulus estimate for the signed genuine-prime minor-arc coefficient, without assuming a representation at the target or its shifts. First determine the weakest weighted shift norm that can replace the Lipschitz hypothesis while still making the exact Fejér inequality strict. If no available arithmetic mechanism reaches the necessary scale, prove a sharper no-go result for the proposed localization family and identify a different target-localized input. See the updated `tasks/NEXT_TASK.md`.

## Deliverable map

- Fourier correction and regression audit: `00_erratum.md`, `tests/verify_sum_difference.py`.
- Kernel proofs and localization limitation: `01_localized_kernel_identities.md`, `02_fourier_localization_limits.md`.
- Base-position, wheel, and correlation conventions: `03_prime_correlation_arithmetic.md`.
- Literature, analytic attempt, and adversarial check: `04_primary_literature.md`, `05_new_analytic_attempt.md`, `06_independent_review.md`.
- Reproducibility and provenance: `checkpoint_log.md`, `source_manifest.json`, `tests/`.
