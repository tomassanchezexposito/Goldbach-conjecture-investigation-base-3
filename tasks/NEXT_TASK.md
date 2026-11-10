# NEXT TASK — Stage 66: target-uniform signed shift modulus

**Status:** universal coverage of the original three-case conjecture remains OPEN. Continue from the verified Stage 65 branch and preserve all earlier results. All repository material must be in English.

## Objective

Investigate whether the exact Fejér localization criterion in `results/stage65/01_localized_kernel_identities.md` and `05_new_analytic_attempt.md` can be closed by a non-circular, target-uniform arithmetic estimate for the genuine-prime signed minor-arc coefficient
\[
m_w(N)=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)\,d\alpha.
\]
The first task is to determine the weakest weighted shift-modulus condition that, together with the global fourth moment and a valid positive major-arc estimate, forces $m_w(N)>-a_w(N)$. Do not assume a prime-pair representation at $N$ or any neighboring target.

## Required work

1. Independently verify Stage 65's exact Fourier, Fejér, countermodel, and conditional-criterion formulas; rerun the Stage 65 Python and Sage verifiers.
2. Derive necessary and sufficient coefficient conditions for a finite shift kernel to detect a negative central coefficient under a global $\ell^2$ constraint. Distinguish arbitrary sequences from genuine prime coefficients.
3. Investigate whether a weighted average of increments, a localized energy, a covariance inequality, or a short-shift exponential-sum estimate can provide the missing bound. State exact ranges and constants.
4. Compare each proposed estimate with the audited conditional moment/major-arc results in `results/stage65/04_primary_literature.md`. Preserve all zero-free hypotheses and publication-status qualifications.
5. Actively find counterexamples, sign errors, target-index issues, invalid swaps between $S_w^2$ and $|S_w|^2$, and circular uses of $R(N)>0$.
6. If no usable arithmetic estimate follows, prove a precise no-go theorem for the relevant family of localization functionals and identify a concrete alternative analytic input.
7. Record proven results, failed inequalities, conditional consequences, exact reproducible computations, resource use, and remaining proof obligations under a new `results/stage66/` directory. Use independent exact verification when finite identities are checked.
8. Work on `cocalc/stage66-weighted-shift-modulus`, based on the latest verified research branch. Fetch with the existing dedicated SSH identity and `IdentitiesOnly=yes`; never overwrite or delete historical work. Commit and push only to Stage 66, and do not modify `main`.

## Mathematical limits

The original residual set is
\[
H=\{N\geq4:N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\}.
\]
The original cases $N=p+1$, $N=2p$, and $N=p+q$ for distinct primes remain the objective. Modular admissibility and singular-series density are not primality. Averages do not imply pointwise positivity without a stated localization theorem. Do not claim universal coverage without a complete, rigorous, non-circular proof.

Do not install software, incur costs, modify GitHub permissions, force-push, or modify `main`.
