# Stage 64 final report — 2026 minor-arc gap

## Executive conclusion

Stage 64 audited the Stage 63 shared-prime example, checked the stated 2026 fourth-moment results against a target-specific positivity goal, and tested exact correlation identities independently. The mathematical objective remains open. No universal proof of the author's three-case formulation or of distinct-prime coverage on the residual set was obtained.

The principal analytic conclusion is precise: the reviewed minor-arc fourth moment gives a global coefficient energy of order at most X^(5/2)(log X)^100. A missing target with a positive major-arc term would require one minor-arc coefficient of magnitude at least cX. The global estimate therefore allows as many as O(X^(1/2)(log X)^100) such targets and cannot exclude one. It also does not control the sign at any prescribed target.

## A. Proven mathematical results

1. **Stage 63 erratum.** For the shared-prime example (n,m)=(12,18), the common prime positions are x=5,7. The purported x=11 fails because 12-11=1. The general shared-prime identity is unaffected.
2. **Exact distinct-target identity.** For n≠m, R(n)R(m)=S(n,m)+Q_4(n,m), where S counts pairs sharing their unique prime and Q_4 counts pairs with four distinct prime positions. For n=m, R(n)^2=R(n)+Q_4(n,n), with the first term the identical-representation diagonal.
3. **Parseval consequence.** If m_w(N) is the minor-arc Fourier coefficient of S_w^2, then sum_N |m_w(N)|^2 = integral over minor arcs of |S_w|^4. Under the cited conditional estimate this is O(X^(5/2)(log X)^100), yielding only |m_w(N)|=O(X^(5/4)(log X)^50) pointwise and an exceptional-count bound of order X^(1/2) times logarithms.
4. **Exact local-data counterexample.** Targets 210 and 420 have equal wheel-210 count 48 and the same conventional singular-series factor, but 210 satisfies the residual predicate while 420 does not. Thus those local factors alone do not determine membership in H.
5. **Conditional exclusion lemma.** If a prime-only weighted coefficient decomposes as r_w(N)=a_w(N)+m_w(N), if a_w(N)≥cX, and if an independent estimate proves |m_w(N)|<cX, then r_w(N)>0. The estimate is not established, and applying this to the full unweighted representation count additionally requires handling the weight support and omitted small-prime positions.

Proofs and qualifications are in 00_stage63_erratum_and_provenance.md, 02_fourth_moment_to_pointwise_gap.md, 03_signed_fourprime_alternatives.md, and 04_research_attempt.md.

## B. Computational observations

Two independent programs were run: a standard-library Python verifier using trial division and explicit enumeration, and a SageMath 10.9 verifier using Sage primality/factorization routines. They agree on the 210/420 wheel and residual calculations, exact small-target partition counts, and a finite cyclic Parseval check over two prime fields. Full inputs, outputs, tested targets, and hashes are in tests/ and source_manifest.json.

These are finite checks of algebra and implementation. They do not establish any prime-correlation estimate. During verifier development, two initial assertions were wrong because they incorrectly treated 419 as composite; both checkers were corrected after direct primality verification. The corrected independent runs pass.

## C. Refuted approaches and first invalid steps

- **Fourth moment to zero exceptions:** thresholding gives a growing exceptional-set bound. The first invalid step is declaring that upper bound smaller than one.
- **Global norm to pointwise sign:** a global L2 bound permits a single coordinate of size cX, and taking a square root loses a factor X^(1/4)(log X)^50 relative to the major term. No sign follows.
- **Wheel/singular-series determination:** the exact 210/420 pair refutes determination of residual membership from these factors alone.
- **Four-prime positivity:** exact nonnegative counts have no positive lower bound merely because they count admissible configurations. An anchor conditioned on a representation of the target is circular in the zero case.
- **Smooth coefficient as full representation count:** the weighted coefficient is not identical to the unweighted count, and a transfer to the von Mangoldt sequence requires separate estimates. For the direct positivity implication, however, a positive coefficient is already a prime-pair witness; on H the equal-prime case is excluded by compositeness of N/2.

## D. External and conditional results

The primary-source report records the exact hypotheses and scopes of Li–Liu, Pintz–Althöfer, Althöfer–Chen–Perelli–Pintz, and the OpenAI Quasi-Riemann Hypothesis manuscript and Lean scope note. In particular, the fourth-moment and exceptional-set claims are conditional on common zero-free hypotheses as stated by the authors. The polynomial-target result is not a theorem for all even targets. The inspected Lean scope note does not include the downstream Goldbach applications. These external results are not re-proved here.

## E. Remaining analytic obstruction

It remains to prove an independent, target-uniform signed estimate for the true-prime minor-arc coefficient, strong enough that m_w(N)>-a_w(N) for every residual target in the interval. Alternatively, a target-localized energy bound strictly below the c^2X^2 one-missing-target threshold would suffice. A global o(X^(5/2)) estimate without a better one-target scale or additional localization does not suffice. Transfer from a smoothed prime-only coefficient to the unsmoothed von Mangoldt convolution also requires a separate rigorous argument, including prime powers and support endpoints.

This is an identification of the missing theorem, not a proof that such an estimate is impossible.

## F. Next research stage

Stage 65 should study a fixed-target localized Fourier kernel: derive the exact weighted-shift identity, identify the norm and regularity assumptions that would imply a bound on one signed coefficient, and test those assumptions against the exact prime-only support and the 210/420 model. Its deliverable should be either a new arithmetic localization lemma with proof or a formal obstruction showing which additional input is indispensable. Do not assume a representation at the target.

## Final status

**Universal coverage remains OPEN.** No claim of proving Goldbach's conjecture or the author's three-case statement is made.
