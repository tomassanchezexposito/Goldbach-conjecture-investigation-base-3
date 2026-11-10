# NEXT TASK — Stage 58: non-circular pointwise positivity certificate

**Evidence status:** open analytic proof obligation. The author's three-case universal coverage statement remains unproved.

## Provenance

- Baseline: the independently reviewed computational Stage 57 branch, including exact shifted four-prime correlation counts and Stage 56 handoff.
- Stage 57 draft review: https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/pull/1
- Detailed Stage 58 tracker: https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/issues/2
- This branch starts from Stage 57 and does not alter main.

## Mathematical objective

For every N in the residual set H of the author's three-case statement (even N >= 4 with N-1 and N/2 composite), seek an independent, rigorously justified pointwise lower bound establishing R(N)>0, where R counts **unordered pairs of distinct genuine primes** p<q with p+q=N.

No statement may assume the target pair exists.

### Obligations

1. **Vacuity audit:** Explain why any putative positive lower bound on X_N X_{N+2h} is circular if it assumes a conclusion equivalent to X_N>0. Give a precise countermodel to positivity inference from averages.
2. **Prime-only Fourier model:** Define S_N(alpha)=sum_{p<=N prime} (log p) exp(2*pi*i*p*alpha). Derive the exact Fourier coefficient for p+q=N. Remove the diagonal p=q when necessary, preserving positivity for distinct primes. The resulting identity alone is not an estimate.
3. **Independent analytic bound requirements:** Formulate major-arc and minor-arc contributions with fully quantified uniform error terms and explicit lower/upper inequalities whose strict dominance would imply R(N)>0. Mark all unavailable estimates as OPEN.
4. **Wheel congruences:** Derive the exact 210-local factor and explain why it does not control the complete singular series or the pointwise error. Respect exceptional primes 2 and 3.
5. **Sieve/parity comparison:** Compare with Chen-type near-prime results and the parity barrier. Do not infer prime-prime representations from semiprime survivors.
6. **Alternative routes:** Attempt a different genuinely non-circular pointwise criterion, audit it for hidden assumptions, and search for finite counterexamples if it has experimentally testable content.
7. **Evidence and reproducibility:** Code only computations testing specific lemmas. Use exact arithmetic and independent validations; no large brute-force Goldbach sweeps as an end in themselves.
8. **Research record:** Save an English report with fully explicit theorem statuses, failed approaches, proofs of elementary lemmas, analytical obstacles, references, and the next objective.

## Execution instructions

Read docs/research_statement.md and docs/research_protocol.md first. Work in this separate research branch; do not modify main or erase Stage 56/57 files. Put new files in results/stage58/. Keep all content, source comments, and commit messages in English. Do not install software, incur costs, or publish to an external website without approval.

Before committing, run any included verifier and document its exact outputs. Push only this branch; ask for a draft PR review, never an automatic merge.

## Success criterion

A useful outcome either rigorously proves an **independent pointwise** positive margin for every sufficiently large residual N with a finite effective cutoff, or identifies the first missing/nonuniform estimate that blocks such a proof. Do not claim the first outcome on the basis of formal manipulation, heuristic asymptotics, average-case estimates, or finite experiments.
