# Next mathematically justified objective: Stage 64 gap audit for pointwise analytic bounds

## Priority and status

Preserve the primary goal: prove $R(N)>0$ for every residual even integer $N\in H$ in the author's original three-case statement. Stage 63 did not prove universal coverage. The next task should examine whether established analytic machinery can supply a non-circular pointwise input, rather than treating a mean or a finite scan as a substitute.

## Proposed Stage 64 question

For the explicitly defined target-anchored coefficient in `results/stage63/02_fourier_pointwise_framework.md`, determine rigorously whether a currently established *unconditional* circle-method estimate can yield, for every sufficiently large residual target, an independently justified positive major-arc lower bound and a signed minor-arc lower bound strong enough to force positivity. In parallel, audit the M5 dyadic energy condition against the strongest exact mean-square results actually available in the cited sources. Do not assume either missing estimate.

The precise M5 sufficient threshold to retain is: with $c_*=2C_2$ and the Stage 63 prime-power correction $D(X)$, a dyadic block contains no residual zero if

$$D(X)\le c_*X/4,\qquad \mathcal E(X)<c_*^2X^2/16.$$

The open asymptotic route is $\mathcal E(X)=o(X^2)$. The alternate Fourier route must specify arc parameters, a finite cutoff, constants, and an inequality for every residual $N$, not almost all targets.

## Required work sequence

1. Read the primary sources or full theorem statements for any proposed mean-square, minor-arc, zero-density, or exceptional-set result. Record the exact weights, summation range, parity, local singular factor, error exponent, quantifiers, and effectiveness.
2. Re-derive the M2 prime-only coefficient and diagonal correction; keep the von Mangoldt prime-power terms separate. Verify every proposed comparison inequality with signs and constants.
3. Check whether a cited estimate is actually stronger than the M5 threshold. If it is only an exceptional-set or average result, state the quantifier obstruction explicitly. Do not weaken “every residual target” to “almost every target.”
4. Attempt one concrete derivation of the target-specific signed bound using existing unconditional estimates. If a known estimate loses the sign or target localization, isolate the first step where that information is lost and quantify the loss.
5. If no theorem supplies the needed bound, give a rigorous conditional implication or an explicit logical countermodel to an overly strong inference. Do not claim an impossibility theorem about actual prime counts without proof.
6. Re-run exact checks for $N=4,6,8$ and selected residual examples, and use an independent computational path only to validate identities, not as support for an asymptotic theorem.
7. Save a theorem/source matrix, code where it adds reproducibility, parameter/version manifest, and a candid report. Commit and push checkpoints only on a new Stage 64 branch; never modify or merge `main`.

## Acceptance and evidence labels

A successful Stage 64 outcome can be either (a) a fully proved new unconditional estimate that gives genuine progress toward the target-specific margin, (b) an audited conditional theorem with an explicit external hypothesis and cutoff, or (c) a rigorous demonstration that a proposed inference from currently cited average bounds is invalid. Mark all finite work as computation. The main existence question remains **OPEN** unless a complete universal proof is supplied.

Do not install software, spend money, run an unbounded scan, or treat a singular-series heuristic as a prime-count theorem.
