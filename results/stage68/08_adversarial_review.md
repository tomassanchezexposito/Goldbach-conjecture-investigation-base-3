# Stage 68 — independent adversarial review

This review treats the conclusions in `00_operator_allocation_and_uniform_gram.md` as claims requiring falsification. It also audits the new Stage 68 lemmas. It is an independent logical pass over the written derivations, not an independent peer review or a new external-source audit.

## 1. Conjugation, signs, and exact matrix orientation

For $D_r(f)_j=\int f g_j$ and the inner product linear in its first argument, $D_r^*z=\sum_jz_j\overline{g_j}$. Therefore
\[
(D_rD_r^*z)_j=\sum_k z_k\int g_j\overline{g_k}=(G_rz)_j,
\]
with $(G_r)_{jk}=\int g_j\overline{g_k}$. The dual scalar is $\sum_j\bar z_jD_r(f)_j=\int f\sum_j\bar z_jg_j$; its norm squared is $z^*G_rz$. The phase-saturating choice $f\propto\overline{\sum_j\bar z_jg_j}$ is correct. This check finds no conjugation defect.

The Fourier difference is
\[
m_w(N+j)-m_w(N)=\int_{\mathfrak m}S_w^2e(-N\alpha)(e(-j\alpha)-1)d\alpha,
\]
so it involves $S_w^2$. Replacing the square by $|S_w|^2$ would impose a prime difference condition and is invalid. The identity uses no prime pair at $N$.

## 2. M1 sharpness and equality audit

The exact optimum (A) is attained because the output space is finite dimensional and the unit sphere is compact; each piece's support functional is attained by an $L^2$ function proportional to the conjugate multiplier, or is zero when that multiplier/budget vanishes. The triangle inequality (B) is an equality iff some maximizing unit vector belongs to every positive-budget, positive-top-eigenvalue top eigenspace. If $B_r=0$ or $G_r=0$, that term imposes no eigendirection condition. This handles repeated top eigenvalues correctly.

The two-interval matrices have nonzero off-diagonal entries, hence simple eigenvalues in dimension two. Their commutator is nonzero, so no eigenvector is shared. Thus triangle strictness is established for actual interval multipliers, not merely abstract PSD matrices. This only concerns arbitrary complex inputs; it is not asserted that a prime-square input attains either optimum.

The density-matrix lifting example is a valid warning: for orthogonal rank-one matrices and $B_1=B_2=1$, the rank-one unit-vector optimum is $\sqrt2$, while the trace-one PSD relaxation permits value 2. Any report that calls this relaxation exact would be false.

## 3. M2 uniformity and exceptional scales

For every finite set of distinct nonzero shifts, $G_{\mathbb T}=I+\mathbf1\mathbf1^*$ and $G_{\mathfrak m}=G_{\mathbb T}-G_{\mathfrak M}$. Since $G_{\mathfrak M}\succeq0$, the upper eigenvalue bound is valid. The all-ones Rayleigh vector and $|g_j|\le2$ give the lower bound with absolute loss $4m|\mathfrak M|$. Dividing by $m+1$ gives a uniform relative loss at most $4|\mathfrak M|$, including when $m=m(X)$ grows. No hidden fixed-$m$ assumption is needed. The lower bound is uninformative if its right side is negative; it is not used as a positive estimate then.

At rational $a/q$, the center multiplier vanishes exactly for $q\mid j$; finite width changes the cubic resonant estimate and linear nonresonant estimate as Stage 67 states. No selected-arc estimate controls the rest of the full minor set. The least-common-multiple observation rules out a bounded nonzero shift resonating at every denominator up to an increasing cutoff, but does not claim all denominators are arithmetically relevant with equal mass.

## 4. M3 strict criterion and scope

The implication uses three independent premises: a positive major lower bound, a total minor-energy upper bound, and an increment-energy upper bound. If $R(N)=0$, the full weighted coefficient is zero and the minor coefficient cancels the major coefficient; Parseval and the aggregate variance inequality then contradict a strict threshold. The contradiction is non-circular only if all analytic bounds are proved independently and uniformly at the target. Arcwise complex coefficients are not individually positive; only their sum's real part can enter a sign argument. If $w$ can be negative, the full coefficient is no longer a nonnegative representation count. These qualifications are necessary.

The global-moment scale arithmetic is internally consistent: $B/A^2\asymp X^{1/2}(\log X)^{100}$, which sets the minimum useful shift count. With that many shifts, the required mean square increment is on the $X^2$ scale, while the generic moment-Gram bound is larger by the same factor $X^{1/2}(\log X)^{100}$. Constants matter for a strict inequality and are intentionally not presented as numerically known from big-O statements.

## 5. M4 adversarial cases

- The sparse polynomial example has positive coefficients and target 28 in the residual set; its full coefficient vanishes while its symmetric major-restricted coefficient is positive, forcing a negative complementary coefficient. It demonstrates the failure of the abstract coefficient-cone inference. It is not a counterexample for the set of all primes: the actual pair $5+23$ exists.
- Half-periodicity holds for an odd-supported polynomial's square. Translation invariance of a restricted region is an additional condition, not automatic for a rational-core cutoff whose reduced denominator and radius change under half translation.
- The base-3 coordinates are $p=3+2a$, $q=3+2b$, $a+b=N/2-3$. The $a=0$ exception for 3 must not be classified as a composite obstruction. Avoiding 3,5,7 applies only to larger primes; CRT survivorship is not primality.
- The Stage 63 shared/four-distinct decomposition is a count identity. A strict lower bound on a four-distinct count that includes target $N$ would already imply a representation at $N$, so proving it by a target-pair argument risks circularity.

## 6. Literature and evidence audit

The three relevant 2026 arXiv v1 PDFs were freshly downloaded and their versions, theorem statements, and relevant dependencies checked on 2026-11-10; the exact PDF hashes and hypotheses are recorded in `06_sources.json`. This is not a line-by-line proof audit. Li–Liu is conditional on the stated common Dirichlet zero hypothesis and supplies global moment/major-arc statements, not the needed target-local signed estimate. Pintz–Althöfer gives exceptional-set estimates, and the polynomial-values paper treats fixed polynomial subsequences. Bhowmik–Grimmelt, Pintz 2018, and the OpenAI manuscript notes remain inherited from Stage 64. No Lean build was performed.

## 7. Refuted implications and first failed steps

| Proposed implication | First invalid step | Counterexample/evidence | Verdict |
|---|---|---|---|
| Nonnegative prime-polynomial coefficients force a nonnegative minor coefficient | Assuming multiplication by $1_{\mathfrak m}$ preserves nonnegative Fourier coefficients | Sparse $S=e(3\alpha)+e(5\alpha)$ at target 28 | REFUTED as a general coefficient-cone claim; no claim about all-prime support |
| Many shifts force a relative Gram saving | Treating the $O(m|\mathfrak M|)$ absolute perturbation as an $O(1)$ relative error | Exact bound has relative loss only $O(|\mathfrak M|)$ for any finite $m$ | REFUTED |
| A small resonant arc controls the full minor increment | Dropping or assigning a sign to the complementary minor set | No complement estimate; complete-minor Gram remains near full-circle top eigenvalue | REFUTED inference |
| A positive off-center four-prime correlation forces center representation | Inferring a target-specific factor from nonnegative products | If center is zero, cross-product identity is zero and both terms can vanish | REFUTED inference |
| Exceptional-set power bound implies no exceptions | Replacing a nonzero upper bound by zero | Every $O(X^\eta)$ with $\eta>0$ permits a singleton | REFUTED inference |

## 8. Independent verification and final disposition

The SymPy and SageMath scripts independently reproduce exact interval Gram entries, the nonzero commutator, the full-circle Gram identity on several shift sets, the PSD relaxation gap, and the sparse polynomial support. These are **FINITE VERIFICATION** checks of exact formulas; they do not establish the all-parameter operator proofs and do not scan primes.

No false algebraic identity was found in the inherited Stage 68 note. A precision improvement is added: the note's initially abstract strictness illustration is supplemented by a rational-centered interval realization and explicit triangle-equality conditions. The central prime-specific candidate (P68) in `07_primary_analytic_attempt.md` remains **OPEN**. The report's main conclusion survives adversarial review: the new results sharpen the geometric optimization but do not yield universal pointwise Goldbach coverage.
