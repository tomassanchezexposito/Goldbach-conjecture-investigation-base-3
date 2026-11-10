# Stage 65 — Literature comparison and hypothesis audit

**Scope and date.** This comparison uses the Stage 64 source audit dated 2026-11-10, which records the examined source versions, theorem hypotheses, external PDF hashes, and metadata checks. It does not claim a fresh download or a proof-level re-audit of those papers. The sources are classified by their recorded status on that date.

| Source and status in the Stage 64 audit | Estimate relevant to this stage | Hypotheses and what it does not establish |
|---|---|---|
| Li–Liu, arXiv:2610.26756v1, preprint | A prime-only smoothed minor-arc fourth moment $int_{\mathfrak m}|S_w|^4\ll X^{5/2}(\log X)^{100}$; a major-arc main term of order $X$; an exceptional-set bound of order $X^{1/2}(\log X)^{100}$. | Conditional on a single uniform real-part bound for zeros of every primitive Dirichlet $L$-function, including $\zeta$, and on the stated smooth weight and arc parameters. The moment permits one exceptional coefficient of size $\asymp X$. It gives no pointwise shift regularity for $m_w(N+h)-m_w(N)$. The Stage 65 conditional Fejér criterion requires precisely such an additional estimate. |
| Pintz–Althöfer, arXiv:2610.15559v1, preprint | Exceptional-set exponents under common zero hypotheses; the strongest recorded refinement requires a common zero bound at most $2/3$. | Theorems are explicitly conditional; a positive-power exceptional-set upper bound does not eliminate a singleton. No signed target-localized coefficient estimate is recorded. |
| Althöfer–Chen–Perelli–Pintz, arXiv:2611.09386v1, preprint | Polynomial-index exceptional-set exponents using the Li–Liu moment and major arcs. | The theorem concerns polynomial target subsequences of degree at least two and retains uniform zero and Li–Liu inputs. It is not a pointwise theorem on every even target and does not imply local shift regularity. |
| Bhowmik–Grimmelt, *Analysis Mathematica* 52 (2026), 767–808, peer-reviewed article | An exceptional-set bound under a common zero-real-part hypothesis. | A positive-power bound leaves room for an exceptional target; no local signed correlation estimate is supplied by the result recorded in Stage 64. |
| Pintz, arXiv:1804.09084v2, preprint | An unconditional exceptional-set estimate $E(X)<X^{0.72}$ for sufficiently large $X$, with ineffective threshold as recorded in Stage 64. | This does not give a zero-exception conclusion or a target-localized shift estimate. |
| OpenAI Math, *The Quasi-Riemann Hypothesis*, September 2026 manuscript and Lean source snapshot | Claims a uniform $7/8$ zero-free half-plane; its statements are used as a possible input to the conditional Goldbach estimates above. | Stage 64 inspected the source-level scope but did not run Lean or independently certify transitive dependencies or downstream applications. It is not a Goldbach positivity theorem. |

## Comparison with the proposed localization inequality

The only external quantitative input used in the new conditional inequality is the Li–Liu global fourth moment, with the exact normalization above. Parseval gives a global coefficient energy bound, and finite Fejér averaging changes its Cauchy–Schwarz factor from $1$ to $\|\omega\|_2\asymp H^{-1/2}$. That gain is offset by the central mass $\omega_0=1/(H+1)$: recovering the center requires a new local shift estimate. None of the audited sources supplies a bound for the signed genuine-prime quantity
\[
m_w(N+h)-m_w(N)
=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)(e(-h\alpha)-1)\,d\alpha
\]
uniformly in every residual target, without a representation hypothesis.

The CRT wheel count and the full singular series are local-density or conjectural-main-term objects. They are not a substitute for that missing signed estimate. Likewise, a sieve upper bound on surviving candidates cannot furnish the required lower bound for simultaneous prime values. No theorem in the audited source list closes this gap.

## Dependency cautions

1. The Li–Liu fourth moment and major-arc assertion remain conditional on the common zero hypothesis stated in the Stage 64 audit; this report does not remove that condition.
2. Exceptional-set estimates allow a finite nonempty exceptional set, including a singleton.
3. A cited formalization or theorem in a preprint does not by itself verify a downstream application; Stage 64 explicitly records that no Lean build was run.
4. The statements here reflect the dated source/version check in Stage 64. Any later version must be checked before reuse.

## References

See the complete bibliographic records, theorem hypotheses, source metadata, and local source fingerprints in `../stage64/01_2026_primary_sources.md` and `../stage64/source_manifest.json`. In particular: Li–Liu, arXiv:2610.26756v1; Pintz–Althöfer, arXiv:2610.15559v1; Althöfer–Chen–Perelli–Pintz, arXiv:2611.09386v1; Bhowmik–Grimmelt, DOI `10.1007/s10476-026-00191-z`; and Pintz, arXiv:1804.09084v2.
