# Stage 62 summary

## Established mathematical results

- The singular-series arithmetic factor has unbounded adjacent variation on the residual set $H$, even for pairs with identical wheel-210 factors $A_{210}(N)=A_{210}(N+2)=15$ (Theorems 62.1 and 62.1A).
- Using Linnik's least-prime theorem to bound the CRT prime, an explicit sequence $N_y\in H$ has both neighboring full singular-series model profiles negligible relative to the center. The Stage 61 signed quadratic, evaluated on that model profile, satisfies $D/\Phi(N_y)^2\to-1/3$. This is a theorem about the arithmetic model only, not about the actual counts $R(N)$.
- Stage 61's sharpened deterministic bound $D\ge4\Lambda^2/9$ on the relative $1/3$ box is correct and sharp, but the hypothesis already assumes $X_N>0$ and hence $R(N)>0$. It is circular as a proof of target positivity.
- The cross-target product of unordered prime representations splits exactly into shared-one-position and four-distinct-position configurations. For a fixed target, distinct representations are disjoint in prime positions. An exact sufficient signed inequality for true-prime correlation bounds is recorded in the report.

## Computational verification

- The Python producer checks six finite CRT examples with $P$ prefixes of $(11,13,17,19,23,29)$, exact fractions, trial-division primality, and direct wheel enumeration.
- An independent SageMath 10.9 verifier recomputes all six examples with Sage primality, factorization, CRT, direct residue enumeration, and exact rational arithmetic; it also checks the 27 endpoint-grid cases and the signed correlation identity for 49 centers $N=4,6,\ldots,100$.
- The largest finite example has $q=21{,}750{,}492{,}479$, $N=43{,}500{,}984{,}956$, equal wheel factors 15, and exact normalized factor ratio $237573379162112/159281822392641$. These are finite arithmetic observations, not prime-pair-count results.
- No actual counterexample to Goldbach or the original three-case conjecture was found or implied.

## Refuted approaches and remaining obligations

- Wheel-210 factors alone cannot control higher-prime singular-series variation.
- A uniform common positive relative-error baseline for the neighboring true-prime counts is circular for the target positivity and incompatible with the singular-series model on the constructed sequence.
- No unconditional, pointwise lower bound for genuine four-prime correlations, or target-uniform minor-arc estimate, has been established. A proof still needs a non-circular target-specific bound on the signed configuration combination in Section 62.5, or another certificate with a rigorously positive margin.
- Universal coverage of the original three-case conjecture remains open.
