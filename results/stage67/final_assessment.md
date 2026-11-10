# Stage 67 — Final assessment

## Proven

- The exact rational-arc Gram matrix is $G_E(j,k)=\mu_E(k-j)-\mu_E(-j)-\mu_E(k)+\mu_E(0)$, independent of target phase and positive semidefinite.
- At a reduced center $a/q$, the multiplier vanishes precisely for shifts divisible by $q$. The finite-width Gram differs from its rank-one center approximation by the explicit bound in `report.md`; resonant arcs have cubic-order energy.
- The complete Li–Liu minor-arc Gram matrix for a fixed finite shift set tends to the full-circle matrix $I+\mathbf1\mathbf1^*$, because the major-arc union has measure $O(X^{2\kappa-1})=o(1)$.
- For each target and any measurable piece $E$ of the minor set, the signed increment vector obeys $\sum_{j\in J}|\Delta_j^E(N)|^2\le B_E\lambda_{max}(G_E)$.

## Refuted / not obtained

- Uniform small-shift suppression on all rational arcs is false.
- Removing only the cited major-arc cores does not yield a global minor-arc Gram saving for fixed shifts.
- No localized prime fourth-moment profile plus signed complement control is available from the inherited source assumptions.
- The Stage 66 sharp energy criterion is vacuous for fixed shift-block size at this global moment scale. For larger blocks, it requires mean squared increments below a threshold approaching the $X^2$ scale; the available Gram upper bound is only at the $X^{5/2}(\log X)^{100}$ scale.

## Conditional and unresolved

The cited Li–Liu estimates remain conditional on their fixed smooth weight, arc construction, common uniform zero-free hypothesis, and stated target ranges. Accepting them does not yield universal pointwise positivity. The first missing theorem is a non-circular, target-uniform signed estimate for the genuine-prime increment vector below the Stage 66 energy threshold, or a fully localized moment decomposition with signed control of every nonresonant remainder.

The original residual set and three-case formulation remain unchanged. Universal coverage is not proved.

## Exact checks

- Python: 13,500 exact rational/group-ring arc entries; reduced-center, full-circle, and 100 major-arc measure checks. See `rational_arc_python_results.json`.
- SageMath: independent exact cyclotomic-field interval Gram and Hermitian checks, 1,651 center divisibility tests, and full-circle matrices. See `rational_arc_sage_results.json`.
- The inherited Stage 66 Python and SageMath verifiers were rerun and passed. See `verification_manifest.json`.

## Next justified objective

Stage 68 should formulate and test a **localized minor-arc moment allocation theorem**: quantify the best pointwise signed increment bound obtainable from a specified family of arc-local fourth-moment budgets $B_r$ and exact arc Gram matrices, including the nonresonant complement. First determine the sharp convex/operator allocation inequality and its extremizers for arbitrary inputs. Then compare the required $B_r$ thresholds with actual unconditional or explicitly conditional prime exponential-sum estimates. If the available inputs still permit a singleton target, record the exact missing prime-only estimate rather than extending finite Goldbach searches.
