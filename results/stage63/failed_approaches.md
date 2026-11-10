# Stage 63 failed approaches and first invalid implications

This register preserves negative results and distinguishes a failed sufficient criterion from a counterexample to the conjecture. No entry below is an arithmetic counterexample to the author's representation statement unless explicitly labeled as one; none is such a counterexample.

## 1. Strict finite-block variance as a universal route

**Tempting implication:** positive average representation count plus a variance strictly below the one-zero threshold should force every block coordinate positive.

**First failure:** the threshold is a valid deterministic *sufficient condition*, but it is not established for every block. The exact residual block $[50,150]$ from Stage 56 has 21 entries, no zero representation, and centered-variance to threshold ratio $1716160/1568187>1$. Thus the criterion fails even on a block where every coordinate is positive. Failure of the criterion says nothing about whether a zero exists. Reweighting cannot by itself repair an unknown zero when the zero coordinate is not known in advance; Stage 58's sharp weighted moment calculation found no improvement from unequal weights in that setting.

**Evidence:** `results/stage56/` and `results/stage58/`; provenance and critical interpretation in `00_provenance_and_audit.md`.

## 2. Positive shifted covariance / correlation

**Tempting implication:** neighboring representation sequences should have nonnegative covariance or a positive aggregate correlation, which could help force a zero coordinate positive.

**First failure:** the sign is not determined by combinatorial symmetry. The exact Stage 57 interval $[262,362]$ at shift 1 has covariance $-127/3000000$. The four-prime expansion partitions products into shared-position and four-distinct classes, but supplies no sign or independent lower bound for the terms.

**Evidence:** Stage 57 report and verifier, cross-referenced in `00_provenance_and_audit.md`.

## 3. Wheel survivors as prime-pair evidence

**Tempting implication:** a positive wheel-210 factor, or many admissible residue pairs, should ensure a genuine prime pair or triple.

**First failure:** coprimality with 210 is a local congruence filter, not primality. The exact CRT product counts admissible residues only; it provides neither a lower bound for primes nor a target-specific prime correlation. Moreover, the sieve removes values divisible by 3, 5, or 7 even when a candidate equals that small prime and is genuinely prime. The M1 examples show genuine triples can survive even when the wheel triple factor vanishes.

**Evidence:** proof and explicit examples in `01_shared_prime_modular_lemma.md`; direct/product comparisons in `01_verify_modular.py`.

## 4. Four-prime partition identity as a positivity estimate

**Tempting implication:** decomposing $R(n)R(m)$ into shared-prime and four-distinct configurations gives enough positive structure to force $R(n)>0$.

**First failure:** the partition is an identity, not a one-sided estimate. If a target count is zero, every product anchored at it is zero. In the Stage 61 three-point quadratic, setting the center to zero gives exactly $-(a-c)^2\le0$. A positive off-center term such as the product of the two neighboring counts cannot overcome this algebraic identity without additional independently proved restrictions.

**Evidence:** exact identity and abstract triples in `03_adjusted_energy_comparison.md` and `03_exact_checks.json`.

## 5. Local-smoothness or common-relative-error certificate

**Tempting implication:** normalized neighboring counts are all close to a common positive level, so the signed path certificate is positive.

**First failure:** a common relative-error hypothesis on the *actual three representation counts* already forces the center positive; it is circular if offered as an independent arithmetic input. Replacing the wheel factor by the full conventional singular series avoids one normalization mismatch but does not prove actual counts are smooth. In fact Stage 62.4 constructs an infinite singular-series profile on which the original unadjusted path certificate is negative. That refutes universal feasibility for that model certificate, not positivity of actual prime counts. Rescaling to make the formal model constant changes coordinates only; it does not establish that real normalized counts are near that model.

**Evidence:** Stage 61/62 reports, `00_provenance_and_audit.md`, and the Track A adversarial analysis in `03_adjusted_energy_comparison.md`.

## 6. Graph energy or altered weights without arithmetic input

**Tempting implication:** a sharper graph, Green kernel, or target-dependent weights might turn a mean into coordinate positivity.

**First failure:** the pseudoinverse inequality is sharp, and the one-zero vector attains the relevant path threshold. Changing weights can change the deterministic constant but cannot supply an independently established lower mean or upper energy for genuine-prime counts. If a weight or mean bound itself depends on center positivity, the argument is circular.

**Evidence:** exact inequality and equality case in `03_adjusted_energy_comparison.md`; Stage 59 source checks are cited there.

## 7. Candidate upper bounds and singular series as lower bounds for primes

**Tempting implication:** the candidate cap, local density, or positive singular series rules out zero representations.

**First failure:** an upper bound for candidate positions has the wrong direction to imply existence. A positive singular series is the arithmetic factor in a conjectural/conditional asymptotic, not a proved pointwise lower bound for the actual count at every even target. Stage 62's exact singular-series construction concerns the formal profile, not the prime-pair function.

**Evidence:** Stage 60/62 reports and the M0 audit.

## 8. Almost-all and exceptional-set estimates as all-target results

**Tempting implication:** a density-zero or power-saving exceptional set must eventually be empty.

**First failure:** a fixed singleton exceptional set has cardinality $1$, which satisfies any upper bound tending to infinity, including $O(X^{1-\delta})$ and $X^{0.72}$ for large enough $X$. This is a quantifier countermodel, not a claim that any particular integer is arithmetically exceptional. The sparse Hardy–Littlewood hypothesis in the reviewed 2026 paper is conditional and permits exceptions; its zero-free conclusion is not Goldbach coverage.

**Evidence:** exact implication matrix in `04_literature_and_implications.md`.

## 9. M5 dyadic energy criterion as if it were unconditional

**Tempting implication:** the proved conditional criterion settles all sufficiently large residual targets.

**First failure:** the implication is valid, but its premise

$$\mathcal E(X)=\sum_{X/2\le N\le X,\ N\text{ even}}|C_\Lambda(N)-N\mathfrak S(N)|^2=o(X^2)$$

has not been proved. A known conditional mean-square estimate recorded in M4 is too weak at the GRH parameter. An abstract one-exception block has energy at least $c^2X^2/4$ for target scale $cN$, so merely proving $O(X^2)$ with an unrestricted constant would not satisfy the derived threshold. The finite examples at 28, 50, 56 or the M6 scan cannot verify an asymptotic mean-square statement.

**Evidence:** full conditional derivation, constants, alternative block-maximum proof, and countermodel in `05_primary_analytic_attempt.md`, `05_countermodels.py`, and `05_proof_obligation.json`.

## 10. Finite exhaustive verification

**Tempting implication:** no counterexample through a large cutoff establishes universal coverage.

**First failure:** the quantifier “for every $N\in H$” is infinite. The M6 scan through 1000 is a reproducible finite observation, with two independent primality algorithms; it is neither a proof nor evidence that the analytic energy hypothesis holds. The three-case statement remains open beyond and independent of that finite range.
