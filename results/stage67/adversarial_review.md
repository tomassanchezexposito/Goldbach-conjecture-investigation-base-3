# Stage 67 — Adversarial mathematical review

## Findings that survive audit

1. **Fourier sign and target phase.** Expanding $(e(-j\alpha)-1)(e(k\alpha)-1)$ gives frequencies $k-j,-j,k,0$ with signs $+,-,-,+$. The common $e(-N\alpha)$ cancels from the Gram matrix. This agrees with the coefficient convention $\widehat f(n)=\int f(\alpha)e(-n\alpha)d\alpha$.
2. **Positivity and norm.** The displayed matrix is an integral Gram matrix, so it is positive semidefinite. Its operator norm is its largest eigenvalue; no claim is made that a trace or entrywise maximum equals that eigenvalue.
3. **Resonance.** At a reduced center $a/q$, $e(-ja/q)=1$ iff $q\mid j$. For parity-preserving shift $j=2h$, the correct criterion is $q\mid2h$, not $q\mid h$. When divisibility fails, the multiplier can be order one.
4. **Finite-width error.** The derivative bound is $2\pi|j|$ componentwise. Integrating the rank-one perturbation inequality over a symmetric interval yields exactly $2L_J\|v(c)\|\rho^2+(2/3)L_J^2\rho^3$. The resonant singleton expansion has leading coefficient $(8/3)\pi^2j^2\rho^3$.
5. **Complete minor set.** The cited major-arc union has measure at most $2P^2/X$ because $\varphi(q)/q\le1$. For fixed $m$, an entrywise Gram perturbation of at most $4|\mathfrak M|$ gives operator perturbation at most $4m|\mathfrak M|$. Since $\kappa<1/2$, the minor Gram approaches $I+\mathbf1\mathbf1^*$.
6. **Prime application.** The vector Cauchy–Schwarz inequality is uniform in the target and uses $S_w^2$, not $|S_w|^2$. It is valid if a target has zero representations. It gives no new arithmetic saving because the only cited moment is global on the full minor set.

## Refuted or unsupported implications

- “Every rational arc is resonant for short shifts.” False; $q=3,j=2$ has center multiplier squared $3$.
- “Major-arc excision makes the complete minor-arc Gram small.” False for fixed shifts; the excised set has vanishing measure, so its Gram removal vanishes.
- “A cubic resonant-arc norm controls the full increment.” Invalid unless the complement is independently bounded or its signed contribution is controlled.
- “The Gram identity turns a global fourth moment into the necessary pointwise prime estimate.” Invalid. It is a sharp operator bound for arbitrary $L^2$ inputs; no arithmetic constraint has been used to improve it.
- “Equal wheel factors or local congruence admissibility guarantee prime endpoints.” Invalid and unchanged from prior stages.
- “An anchor representation may be chosen at the target under proof.” Circular if the case being treated is zero representations. No such anchor is used here.

## Remaining gap and scope

The required input remains a target-uniform signed estimate for the genuine-prime minor-arc increment vector, or a localized fourth-moment decomposition controlling every arc piece with sufficient constants. The inherited conditional global fourth moment and exceptional-set results do not exclude a singleton. No prime counterexample, Goldbach proof, or unconditional pointwise saving is claimed. The dated Stage 64 literature inventory was not refreshed in this stage.

## Verification boundary

The Python group-ring and SageMath cyclotomic checks audit exact finite formulas. They do not prove the analytic bound on $S_w$, validate the cited preprints, establish the common zero-free hypothesis, or certify universal coverage. Those limitations are intentional and are included in the final assessment.
