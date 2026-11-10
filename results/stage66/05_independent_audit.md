# Stage 66 — Independent adversarial audit

## Verdict

The sharp local-modulus theorem and its even-step specialization are correct. The aggregate theorem is also sharp in the arbitrary-sequence class. These are deterministic implications only. No new unconditional or conditional theorem bounding a fixed genuine-prime signed increment at a residual target was obtained. Consequently Stage 66 does not prove universal coverage of the original three cases.

## Proof audit

For each distinct shift, reverse triangle gives a separate lower bound on a separate coordinate, so there is no hidden overlap in the nonuniform theorem. The proposed extremizer satisfies every increment constraint, including $d_h>A$, and proves sharpness. For the aggregate theorem, $f(t)=(A-t)_+^2$ is convex and decreasing on $[0,\infty)$. Jensen gives $\sum f(\delta_j)\ge m f(m^{-1}\sum\delta_j)$; Cauchy gives $m^{-1}\sum\delta_j\le\sqrt{V/m}$. Monotonicity then gives the stated bound. Equal increments $\min(A,\sqrt{V/m})$ attain it. No assumption on prime representations enters either proof.

The even-step endpoint $J=\lceil A/L\rceil-1$ correctly omits a zero term when $A/L$ is an integer. The $L=0$ case is separate and correct. The asymptotic $2A^3/(3L)+O(A^2+AL)$ applies only when the full positive range of shifts is included and $A/L\to\infty$.

## Fourier audit

With $e(t)=e^{2\pi i t}$ and coefficients extracted using $e(-n\alpha)$, the exact multiplier is $e(-j\alpha)-1$. The prime sum square $S_w^2$ encodes sums of two primes; $|S_w|^2$ encodes differences. Parseval's integrand remains $|S_w|^4$. The full-circle multiplier norm is $2$ for every nonzero integer shift, so the global fourth moment gives no small-shift gain. The Gram matrix $I+\mathbf1\mathbf1^*$ gives the stated sharp simultaneous full-circle operator norm $m+1$.

There is a limited exact localization observation. On an arc $\alpha=a/q+\beta$,
$$|e(-2h\alpha)-1|=2|\sin(2\pi h(a/q+\beta))|.$$
If $q\mid 2h$, this is at most $4\pi |h||\beta|$. If $q\nmid 2h$, the value at the center is $2|\sin(2\pi ha/q)|$, which need not be small and can equal $2$. Thus a small-shift factor on every rational minor arc does not follow from proximity to rational centers. Any useful localization must separately control arcs whose denominator divides $2h$ and the remaining arcs, with an arithmetic fourth-moment estimate on the weighted union.

## Prime-correlation audit

At one target, two distinct unordered representations cannot share exactly one prime; the shared value determines the other endpoint. At two distinct targets they cannot share both values. Therefore the diagonal, one-shared-position and four-distinct partitions in `03_fourprime_signed_energy.md` have the stated multiplicities. The cross-target identity remains meaningful if either representation count is zero. No positive lower bound for a target is smuggled into its derivation.

The normalized identities do not have a determined sign from nonnegativity of each individual count. Their difference contains positive self-correlations and negative cross-correlations. To use them pointwise requires independent quantitative comparison of the terms. Wheel-admissible positions and singular-series factors do not supply those comparisons.

## Circularity and theorem dependencies

An anchor selected from $\mathcal P(N)$ is unavailable when testing $R(N)=0$. Any argument that first selects such an anchor and then derives a lower bound for that same target is circular for the desired conclusion. The unanchored coefficient, correlation, and energy identities avoid that logical defect but stop at identities absent a new estimate.

The Li–Liu moment and major-arc inputs cited in the dated Stage 64 audit are conditional on its common uniform zero-free hypothesis and precise weight/arc assumptions. Their global moment and exceptional-set conclusions permit a singleton exceptional target. No result identified in the inherited source audit supplies the fixed-target signed increment or block variation required here. The external source status was not refreshed in Stage 66; verify versions before any later citation.

## First missing implication

The exact missing input is a uniform-in-target bound for
$$\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)(e(-2h\alpha)-1)\,d\alpha$$
or a block estimate for the squared magnitudes of these integrals, with constants strong enough that the sharp energy lower bound exceeds the available $B_X$. It must specify uniformity in $N,h,X$, the weight and arc definitions, and its dependence on the zero-free hypothesis. The global $L^2$ control of the coefficient sequence, its global fourth moment, wheel congruences, or average exceptional-set bounds do not imply this target-specific estimate.

## Verification and limitations

The original Stage 66 verifier, a new standard-library `Fraction` verifier and a separate SageMath verifier were run. They use different prime-generation and algebra paths for finite identities. The exact ranges and output hashes are recorded in `verification_manifest.json`. These regressions validate formulas and multiplicities on the stated finite grids; the proofs above, rather than the computations, establish the general deterministic theorems. No numerical prime search is used as evidence for universal positivity.
