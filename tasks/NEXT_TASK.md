# NEXT TASK — Stage 59: sharp pointwise path-energy bound and four-prime correlations

**Goal:** Find a **non-circular, independent pointwise** bound that guarantees a genuine distinct prime pair at every residual even integer of the author's original three-case conjecture.

**Evidence status:** The deterministic path-energy inequality below is proved and sharp, but the required analytic bounds on its right-hand side are **OPEN**. Do not present numerical success as universal proof.

## Provenance and initial research

The new research branch is \`cocalc/stage59-sharp-local-energy\`, based on Stage 58. It contains:

- \`results/stage59/research_note.md\`: proofs of T1–T3 and exact finite observations.
- \`results/stage59/verify_local_energy.py\`: independently checkable finite prime, wheel, four-prime and optimality tests.
- \`results/stage59/verify_mod210_pilot.py\`: finite centered-window comparison, spacing 2 versus 210.
- Draft Stage 58 review: https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/pull/3

Read \`docs/research_statement.md\`, \`docs/research_protocol.md\`, and \`results/stage59/research_note.md\` first. The user's three-case formulation and the set H are non-negotiable definitions.

## T1 — Exact pointwise inequality to investigate

For consecutive even targets n_j=n_0+2j, k>=2, write x_j=R(n_j)/A_210(n_j), where R counts **unordered distinct genuine prime pairs** and A_210 is the exact local wheel admissibility factor. Let mu=(sum_j x_j)/k and E=sum_{j=0}^{k-2}(x_{j+1}-x_j)^2.

Define A_(k,j)= [sum_{t=1}^j t²+sum_{t=1}^{k-1-j}t²]/k². The proved sharp inequality is

    (x_j - mu)^2 <= A_(k,j) E.

Hence **mu² > A_(k,j)*E** is a correct pointwise zero-exclusion criterion. The coefficient A_(k,j) cannot be improved for arbitrary nonnegative sequences, even with a zero at j.

This is a deterministic theorem, NOT the missing arithmetic bound.

## Stage 59 research and execution requirements

1. Inspect the existing working tree; fetch the Stage 59 branch through the dedicated SSH deploy key and check it out safely (no destructive overwrite).
2. Run both provided verification scripts and record exact outputs; independently verify at least some outputs with SageMath's primality functions. Write result JSON and a reproducibility manifest under \`results/stage59/\`.
3. Verify independently the **proof** of T1 and the sharpness counterexamples T2, and the cyclic zero-invisibility theorem T3 for m=1,2,3,4.
4. Derive and explain the complete decomposition of E into same-target and adjacent-target correlations of **four prime positions**, including all shared-prime categories, two wheel denominators, diagonal terms, and exceptions involving 2 and 3.
5. Compare **independently derived** lower bounds mu>=m_N and upper bounds E<=U_N against the strict condition m_N²>A_(k,j)U_N. Never use a hypothetical R(N)>0 to prove either bound, and never divide by R(N).
6. Investigate whether the k=3 or k=5 local criterion or spacing-210 residue-class paths admit a rigorous arithmetic upper bound based on published sieve or circle-method estimates. Cite precise theorems, hypotheses, uniformity, and constants.
7. Test whether residual N with extreme local singular-series factors defeat any proposed uniform inequality; distinguish finite counterexamples from speculative asymptotics. No unbounded brute-force sweep is necessary.
8. For fixed k and cyclic vectors, prove that any m-fold correlation average with fixed m can differ from the all-positive model by only m/k while still containing a zero. Explain why o(1) averaged accuracy does not exclude an isolated zero.
9. Review the September 2026 Bhowmik–Grimmelt published work on Goldbach exceptional sets and its major-arc formula (https://doi.org/10.1007/s10476-026-00191-z). Identify what quantitative estimate would be needed to bridge the gap to each individual target. This is **not** a claim that the published article closes the problem.
10. Save all new code, SageMath notebook (if useful), exact data, report, source/provenance and SHA-256 manifest in \`results/stage59/\`. Retain existing original files.
11. Commit and push **only** \`cocalc/stage59-sharp-local-energy\` after independent checks. Do not modify or merge \`main\` or prior research branches; propose a draft PR for review.
12. Report a precise statement of the **first missing analytic bound** and whether the local energy route remains plausible at the numerical scales examined.

## Scientific standard

Keep all repository files, comments, code and commit messages in English. Separate proved lemmas, assumptions, conditional conclusions, finite observations, counterexamples and open obligations. Seek an actual proof for *every* N in H, not a positive average. Do not claim Goldbach or the user's universal statement has been proved without a complete non-circular proof.

Do not install software, incur additional charges, delete files, or publish externally without approval.
