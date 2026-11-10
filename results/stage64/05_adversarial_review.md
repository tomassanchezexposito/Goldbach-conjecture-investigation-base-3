# Stage 64 — Adversarial mathematical review

Review status: claims below are classified by what is proved in this repository. External preprint theorems are not promoted to unconditional established results.

| Claim | Classification | Review |
|---|---|---|
| The Stage 63 example for targets 12 and 18 has common prime positions 5 and 7, not 7 and 11. | **PROVED** | Directly, 12−5=7, 18−5=13, 12−7=5, and 18−7=11 are prime. The purported x=11 fails because 12−11=1. |
| For distinct even targets, the product of unordered distinct representation counts partitions into one-shared-position and four-distinct-position pairs. | **PROVED** | A pair of representations cannot share both primes unless the targets coincide. A shared prime is unique, so there is no orientation multiplicity. |
| For a same target, the square of the count is diagonal plus pairs of disjoint representations. | **PROVED** | Two distinct unordered representations of the same sum cannot share exactly one prime. |
| The 210 wheel count and full conventional singular-series factor agree for 210 and 420, while their residual-set membership differs. | **FINITE / PROVED** | Exact factorizations give 210 in H and 420 outside H. The common wheel count is 48 and the common odd singular-series factor is 16/5. This refutes determination of H membership by those factors alone. |
| Parseval converts the stated minor-arc fourth moment into a global coefficient-square bound. | **PROVED, conditional on the stated function and arcs** | This is ordinary Fourier Parseval. The fourth-moment upper bound itself is an external conditional preprint theorem. |
| The resulting O(X^(1/2)(log X)^100) exceptional count proves there are no exceptions. | **REFUTED** | The bound diverges and is compatible with one exception. |
| The global norm bound alone excludes a coefficient of size cX. | **REFUTED** | An abstract vector supported at one coordinate with value cX satisfies the norm bound for large X. This is a logical obstruction, not a prime-arithmetic counterexample. |
| A zero representation forces the weighted prime coefficient to vanish for every cited smooth weight. | **PROVED** | The coefficient is a sum over prime pairs. If there are no prime pairs, every summand is absent, independent of support. Conversely, a positive weighted coefficient gives a prime pair; for N in H it is distinct because N/2 is composite. |
| The cited fourth moment gives a target-specific signed minor-arc bound. | **REFUTED AS AN INFERENCE** | Parseval supplies only global energy and an unsigned pointwise norm bound. No localization or sign theorem follows from that hypothesis alone. |
| The residual conditions N-1 composite and N/2 composite force a positive prime-pair count. | **OPEN** | No argument here derives simultaneous primality from these conditions. Congruence admissibility and singular-series positivity are insufficient. |
| Recent exceptional-set and fourth-moment preprints prove universal coverage. | **REFUTED** | Their statements allow exceptional sets and/or rely on explicit common zero-free hypotheses. An exceptional-set upper bound tending to infinity does not eliminate a singleton. |
| The OpenAI Quasi-Riemann Hypothesis preprint's downstream applications are all formally verified. | **NOT ESTABLISHED** | The inspected Lean scope note lists formalized zero-free and Siegel-gap components but explicitly excludes later applications. No complete Lean build or transitive proof audit was performed in this stage. |

## First invalid implications found

1. The exceptional-set inference changes a growing upper bound into zero.
2. The global Parseval norm is used as though it were a bound at a prescribed target.
3. The major-arc main term is treated as though it had the sign of the full prime coefficient; the minor-arc term is signed and can cancel it.
4. Wheel or singular-series admissibility is treated as actual primality.
5. The existence of a positive combinatorial correlation is confused with a positive lower bound independent of the target representation.

No universal proof is obtained. The strongest proved new result in Stage 64 is the exact decomposition and localization audit, together with the explicit 210/420 arithmetic example and the corrected Stage 63 example.
