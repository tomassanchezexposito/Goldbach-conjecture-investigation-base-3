# Stage 68 — integrated research report

## Executive result

Stage 68 proves an exact allocation theorem for multiple disjoint arcwise $L^2$ budgets, characterizes equality in its simpler spectral bound, and exhibits strictness using two genuine rational-centered interval Gram matrices. It also proves that if only a total fourth-moment budget is known, any such allocation collapses exactly to the single full-minor operator norm. The full-minor Gram remains close in relative top-eigenvalue to the full-circle Gram uniformly for every finite shift set, even when its size grows with $X$.

These are useful operator-level refinements and obstructions. They do **not** produce a new signed arithmetic estimate for genuine prime correlations. All available external fourth-moment and exceptional-set results remain too coarse to exclude one prescribed missing representation. The original three-case conjecture and residual set are unchanged; universal coverage remains **OPEN**.

The preserved formulation is: for even $N>2$, at least one of
$$
N=p+1,\qquad N=2p,\qquad N=p+q\quad(p<q,\ p,q\text{ genuine primes})
$$
holds; in the third case $N-2p=2q-N$, which follows algebraically from $p+q=N$ and does not imply primality. The unresolved residual set remains
$$
H=\{N\ge4:\ N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\},
$$
with $R(N)=\#\{p<q:\ p,q\text{ genuine primes},\ p+q=N\}$ and the open objective $R(N)>0$ for every $N\in H$.

## A. Proven mathematical results

1. **Exact disjoint-budget optimization (Theorem 1 in `02_exact_budget_optimization.md`).** For finite $J$, measurable disjoint $E_r$, and complex $L^2(E_r)$ balls with budgets $B_r$, the exact supremum of the increment-vector norm is
   \[
   \max_{\|z\|_2=1}\sum_r\sqrt{B_r}\sqrt{z^*G_rz}.
   \]
   Two derivations are given: support functions/Hilbert duality with an explicit extremizer, and the adjoint/Minkowski-sum ellipsoid argument. Equality in the eigenvalue-sum bound holds exactly when the active positive-top-eigenvalue matrices share a unit vector in their top eigenspaces; zero budgets and zero matrices impose no constraint.
2. **Strictness for actual interval Grams.** For $J=\{1,2\}$ and intervals of radius $1/8$ centered at 0 and $1/2$, exact Gram matrices fail to commute and have simple top eigenvalues. Their top directions therefore do not align, and the triangle bound is strictly larger than the exact allocation optimum. This supplements the abstract orthogonal-rank-one example.
3. **Total-budget collapse.** If only $\sum_r B_r\le B$ is known, then the optimal allocation supremum is exactly $\sqrt{B\lambda_{\max}(\sum_rG_r)}$. Merely splitting a disjoint set into named arcs cannot create information.
4. **Uniform shift-count obstruction.** For any finite $J(X)$ of distinct nonzero shifts and major-set measure $\mu$, the complete-minor Gram obeys
   \[
   m+1-4m\mu\le\lambda_{\max}(G_{\mathfrak m})\le m+1,
   \]
   so its relative loss from the full-circle top eigenvalue is at most $4\mu$, independent of how $m$ grows. This is a geometric statement, not a prime estimate.
5. **Pointwise certificate remains conditional.** A positive major coefficient, total minor-energy upper bound, and independently proved increment-energy upper bound imply positivity only if the strict Stage 66 threshold is met. This implication does not presuppose a representation; the contradiction begins under $R(N)=0$.
6. **Prime-specific exact identities.** Coefficient positivity applies to the full square, not a restricted minor piece. Half-periodicity of the full square need not persist on nonsymmetric rational-core partitions. Base-3 reflection is only a reindexing. Shared/four-distinct identities do not give a positive lower bound at the center.

## B. Computational observations

The targeted SymPy and SageMath verifiers independently confirm the exact two-interval matrices and their nonzero commutator; the full-circle Gram identity on three small shift sets; the rank-one PSD relaxation gap; and the sparse positive-coefficient countermodel. The scripts are exact regression checks, not proofs of all-parameter theorems or computational evidence about prime representations. Commands, runtimes, output hashes, and environment are recorded in `verification_manifest.json`.

## C. Refuted approaches

- A nonnegative coefficient sequence need not have nonnegative Fourier coefficients after multiplication by a minor-set indicator. The sparse polynomial at residual target 28 supplies a countermodel to that abstract implication, but not to the genuine all-prime problem.
- Increasing the number of shifts alone does not yield a relative Gram saving on the complete minor set.
- A selected resonant-arc bound does not control the complement.
- A positive four-distinct correlation lower bound involving a target pair would itself imply the target representation; nonnegativity alone has no such force.
- A positive-power exceptional-set bound permits a singleton and is not universal coverage.

## D. Conditional and external results

The three 2026 arXiv preprints in `06_sources.json` were freshly version-checked and their relevant theorem statements and dependencies inspected on 2026-11-10. The Li–Liu results require the paper’s common Dirichlet-$L$ zero hypothesis and fixed smooth-weight/arc setup; they give a global minor fourth moment of order $X^{5/2}(\log X)^{100}$ and a positive major coefficient in the stated range. Pintz–Althöfer gives exceptional-set bounds, while Althöfer–Chen–Perelli–Pintz concerns fixed polynomial subsequences. These claims were not re-proved line by line. The Bhowmik–Grimmelt, 2018 Pintz, and OpenAI manuscript notes remain inherited from Stage 64; no Lean build was run. None supplies the target-uniform signed estimate required here.

## E. Remaining analytic obstruction

With major scale $A_X\asymp X$ and global energy $B_X\asymp X^{5/2}(\log X)^{100}$, the sharp local-energy criterion needs roughly $m>B_X/A_X^2\asymp X^{1/2}(\log X)^{100}$ shifts. At that scale it also needs a target-uniform signed increment energy below a constant multiple of $mX^2$. The generic moment-Gram upper bound is of order $mB_X$, worse by $X^{1/2}(\log X)^{100}$. Neither an arc partition with only a total budget nor a rational resonance identity closes that gap.

The missing theorem is a genuinely prime-specific estimate, uniform for every $N\in H\cap[X/2,X]$, of the signed even-shift increment vector or of a fully localized arc-energy profile plus phase control that implies the strict threshold. It must state weight, arc, shift, and zero-hypothesis dependencies and cannot normalize by $R(N)$.

## F. Next research stage

Stage 69 should focus narrowly on proving or refuting a target-uniform bilinear/correlation estimate for the genuine prime sum that implies the explicit threshold in `07_primary_analytic_attempt.md` (P68). First test whether any established mean-square theorem can be localized to each target with a loss smaller than $X^{1/2}(\log X)^{100}$; otherwise construct an arithmetic obstruction or prove a conditional theorem with the exact missing premise. Do not repeat the general arc allocation or large finite Goldbach searches.

**Evidence labels:** operator and reindexing identities are **PROVED**; finite symbolic calculations are **FINITE VERIFICATION**; Li–Liu and other imported analytic inputs are **EXTERNAL THEOREM** statements as recorded, with the stated ones **CONDITIONAL**; invalid general implications are **REFUTED**; the prime-specific signed estimate and universal Goldbach coverage are **OPEN**.
