# STAGE 69 — DEEP RESEARCH DIRECTIVE, PART II
## Source-level analytic research, two-pass proof attempts, a rigorous pointwise criterion, and a scientific closure process

**This is a continuation of \`tasks/STAGE69_DEEP_PROGRAM_I.md\`. Do NOT start here without completing the Stage 69 M0 mathematical erratum and reading the new Stage 68 dependency audit. The user's request is to double analytical depth, not computational volume.** Work through M5–M9 after M0–M4, recording actual theorem development and failed inferences. Do not mark this work as complete after producing only a plan, a bibliography, or a restatement of the existing pointwise gap.

## M5 — PRIMARY-SOURCE ANALYSIS: WHICH KNOWN ESTIMATE REALLY CONTROLS A SINGLE TARGET?

The primary mathematical question is the **quantifier mismatch** between an average over coefficients and a pointwise signed bound at a specified residual even N. This theme is a *source-to-implication audit*, not a list of prestigious citations. A deep result is an exact proof of what a published theorem actually yields in our notation, with the first missing inequality clearly exposed.

### M5a. Recheck the October/November 2026 source chain

Verify current accessible versions, revision dates, theorem statements, full hypotheses, notation, proof status (preprint versus reviewed) and URL for:

1. H. Li and Z. Liu, *Fourth moments of prime exponential sums and exceptional sets for sums and differences of primes*, arXiv:2610.26756, https://arxiv.org/abs/2610.26756 (submitted 2026-10-19). The abstract states a conditional square-root exceptional-set bound under a common Dirichlet \(L\)-function zero-real-part condition with fixed \(1/2\le\Theta<11/12\). Read the **actual** minor-arc fourth-moment theorem, its smoothing class, \(P=X^\kappa\), target ranges, implied constants, and any exceptional-zero dependencies; do not extrapolate from its abstract.
2. J. Pintz and I. Althöfer, *The Goldbach exceptional set: an exponent 7/12 and conditional refinement*, arXiv:2610.15559, https://arxiv.org/abs/2610.15559 (submitted 2026-10-11). Check the exact fixed zero-free hypothesis, the conditional exponent, and the external inputs. Distinguish the claim in the preprint from a fully checked proof.
3. I. Althöfer, D. Chen, A. Perelli and J. Pintz, *The exceptional set of Goldbach numbers among polynomial values*, arXiv:2611.09386, https://arxiv.org/abs/2611.09386 (submitted 2026-11-06). Verify degree restriction, normalization of polynomial index, theorem constants and why an almost-all result on a polynomial subsequence does not prove every N in H.
4. G. Bhowmik and L. Grimmelt, *The exceptional set of the Goldbach problem*, *Analysis Mathematica* 52 (2026), 767–808, DOI https://doi.org/10.1007/s10476-026-00191-z (published 2026-09-23). Read the exact fully explicit major-arc formula and its uniform target range, as well as the special hypotheses for its conditional results. Distinguish the journal theorem from the conjectured Hardy–Littlewood main term.
5. The alleged 2026 uniform zero-free half-plane for all primitive Dirichlet \(L\)-functions, as reported in OpenAI Math manuscripts/Lean notes. Audit the **exact mathematical hypotheses and any formally checked scope**, and separate this external input from the downstream Goldbach paper; do not treat reliance by a preprint as an independent validation. If source files/Lean proof are inaccessible or uncompiled, state that explicitly.
6. Established baseline results: Chen's prime+\(P_2\); Vinogradov's ternary Goldbach (distinct problem); Bombieri–Vinogradov in its precise modulus-average form; classical Montgomery–Vaughan/Pintz exceptional-set estimates; Vaughan's identity or Heath-Brown's identity for decomposing prime exponential sums; any applicable existing bilinear minor-arc bounds. Only cite exact theorems after verifying their statement.

Do not spend time on speculative full-Goldbach proof claims from unscreened repositories unless they contain a clear verifiable new theorem with a proof that survives immediate contradictions.

### M5b. Theorem translation protocol

For EACH potentially relevant theorem, produce a **translation record**:
- original notation and weights;
- original target variable (including whether it denotes N or X);
- actual quantified domain for N, and whether \(N\in H\) is supported;
- all \(\Theta,\kappa,q,h,w\) restrictions;
- theorem's implied-constant dependence and effective/ineffective cutoff;
- pointwise versus average over targets, moduli, or shifts;
- sign (upper bound for absolute value, signed lower bound, or number of exceptions);
- finite-support/diagonal/prime-power corrections;
- **a formal implication to one of our exact Stage 69 proof obligations**, or a proof of why that implication fails with named exponents.

A conditional external theorem may be carried as a hypothesis to prove a conditional result, but its condition must **not disappear** in a later corollary. An exceptional set bound \(\ll X^\delta\), \(\delta>0\), still permits one exception and cannot be cited as an empty exceptional set.

### M5c. Literature-driven search for the *first* prime-only estimate not supplied

Prioritize questions with a genuine mathematical fork:
- Does the source supply \(\sum_{N\in I}|m_w(N)|^2\) only, or a weighted **supremum** over prescribed N?
- Are short-shift increments bounded in a sum over N, or uniformly for each N, including the residual H?
- Are the estimates uniform over the full minor-arc partition, or only one rational shell?
- Do the bounds control \(\int_E|S_w|^4\) only, or \(\Re\int_E S_w^2e(-N\alpha)\) with meaningful sign?
- Do the estimates rely on the smoothing weight being 1 over a central interval, and is that interval guaranteed to cover *some* prime pair at each N? No support coverage may be assumed before proving existence.
- Could a source theorem improve the global \(X^{5/2}(\log X)^{100}\) error to \(o(X^2)\) for the *same exact quantity*? If not, locate the first mismatch of norms or quantifiers.
- Is an amplitude \(X^{5/4}\log^{50}X\) being compared with an \(X\)-scale main term, or is there an overlooked weight factor from \(\log p\)?

**Deliverable M5:** \`results/stage69/05_verified_primary_literature.md\` and \`05_source_ledger.json\`. Include original PDFs' version/URL and any hash if actually downloaded, separately label inherited source descriptions, and provide a theorem implication table. Commit/push a source-audited milestone.

---

## M6 — DEEP ANALYTIC BRIDGE: EXACT QUANTITATIVE TARGET-SPECIFIC LEMMAS

This milestone requires **new proof work** even if the genuinely arithmetic estimate remains open. Build the strongest logically sound theorem that would follow from available independent inputs and quantify the exact shortfall. Do not merely state "a uniform minor arc estimate would suffice": that is already known.

### M6a. Re-derive the local energy exclusion sharply

Suppose \(a_w(N)\ge A_X>0\) for a given residual target N from an external major-arc theorem. If \(R(N)=0\), then \(r_w(N)=0\), hence \(|m_w(N)|=|a_w(N)|\ge A_X\). For any \(m\) distinct even shifts \(j\in J\), with
\[
V_{N,J}=\sum_{j\in J}|m_w(N+j)-m_w(N)|^2,
\quad
B_X=\sum_{n\in\mathbb Z}|m_w(n)|^2,
\]
the sharp Stage 66 inequality gives
\[
B_X\ge A_X^2+m\left(A_X-\sqrt{V_{N,J}/m}\right)_+^2.
\]
Independently prove all needed inequalities from scratch in two ways (Jensen/convexity and direct projection on the center, or another genuinely distinct method). Show the result is sharp in the abstract coefficient class, and characterize equality including \(V/m\ge A_X^2\). Explain why sharp abstractness prevents improving the constant without new prime-specific hypotheses.

### M6b. Solve the exact **finite m tradeoff** before passing to asymptotics

Given actual certified bounds \(\overline B_X\) and \(\overline V_{N,J}\), solve the strict inequality
\[
A_X^2+m\left(A_X-\sqrt{\overline V_{N,J}/m}\right)_+^2>\overline B_X
\]
for the admissible triples \((m,A_X,\overline V)\), including boundary equality and zero cases. Determine the minimal useful m when \(A_X\) and \(\overline B_X\) are fixed. Give a closed expression for the maximum allowable \(\overline V\) when \(m\) is fixed. When there is a family of shift sets \(J\) with different geometries or weights, treat selection of m and J as an optimization under **realistic support constraints**, not "choose infinitely many neighbors" without an independent bound.

### M6c. Prove a **robustness lemma** for errors in the major term and prime-power correction

The inputs are not always the prime-only polynomial: sources may give a von Mangoldt weighted coefficient or major arc formula up to errors. Formulate and prove a robust version of the strict certificate with a major lower bound \(M_X\), a rigorously bounded diagonal/prime-power error \(D_X\ge0\), and a signed minor error. Determine whether the correct center threshold is \(A_X=M_X-D_X\), \(M_X-2D_X\), or another value, depending on the exact convolution and counting convention. No guessed factor of 2. Keep source weights and prime-power terms explicit. If \(M_X\le D_X\), the criterion cannot be used; say so.

### M6d. Develop a **target-localized Cauchy versus correlation** alternative

For a fixed N, compare:
\[
|m_w(N)|\le \sqrt{\int_{\mathfrak m}|S_w|^4}\,\sqrt{|\mathfrak m|},
\]
\[
\sum_{j\in J}|\Delta_j(N)|^2\le B_X\lambda_{\max}(G_{\mathfrak m}),
\]
and the exact fourth moment as a positive additive energy of the full polynomial. Can a signed or bilinear identity improve either bound by exploiting genuine-prime coefficients and target twist? Give the strongest candidate and a complete mathematical derivation. Reject any step invoking cancellation of an integrand after taking absolute values, or using \(\sum_N\) information to bound a designated N.

### M6e. Source-dependent optimization

Separate three regimes:
- the unconditional published prime distribution input actually available;
- the conditional 2026 zero-free input accepted as an explicit assumption;
- an idealized stronger hypothesis that would **in principle** close the gap.

For each, provide exact exponents/logs and logically separate status. If under one regime \(\overline B_X/A_X^2\) diverges as \(X^{1/2}\log^{100}X\), demonstrate which new saving in \(\overline V/m\) would overcome it and where the saving must originate. Do not claim the source supplies a target-signed estimate when it only supplies \(|S_w|^4\).

### M6f. New result acceptance standard

A genuinely **new mathematical advance** within the project may be:
- a provably sharper **prime-specific** inequality (not just unrestricted-L2 optimality) using an exact nonnegativity, support or shift correlation constraint;
- a clearly stated, strictly weaker *conditional* arithmetic hypothesis than "every N is represented", with a valid proof of implication and a plausible route to establish it independently;
- a rigorous **no-go theorem** showing a precisely specified family of published moment/Gram inputs is mathematically incapable of excluding one exception;
- or a fully developed target-preserving bilinear decomposition identifying a nontrivial intermediate prime distribution lemma with exact constants and a well-motivated proof attempt.

A project result is **not** an advance merely because it has new notation, a different kernel, a longer finite scan, or a proof of a known generic Cauchy–Schwarz inequality.

**Deliverables M6:** \`06_sharp_target_criterion_and_robust_errors.md\`, \`06_quantitative_gap_table.json\`, and a small independent exact check only for non-obvious boundary algebra. Commit/push with a clearly labeled verdict.

---

## M7 — TWO INDEPENDENT PROOF ATTEMPTS AGAINST ONE EXPLICIT PRIME-THEORETIC GAP

Choose the most promising candidate from M3–M6; write it as a **formal theorem candidate before attempting to prove it**. It must include:
\[
\forall X\ge X_0,\quad
\forall N\in H\cap[X/2,X],\quad
\forall h\in\mathcal H_X \text{ (if needed)},
\]
and explicit \(q,\Theta,\kappa,w\), zero-free hypotheses, modulus range, effectivity of \(X_0\) and source dependencies. Avoid reusing the letter H ambiguously for the residual set and shift horizon.

### M7 Route A — analytic signed Fourier estimate

1. Start with the actual prime-only \(S_w(\alpha)^2e(-N\alpha)\) and split \(\mathfrak m\) into a complete measurable partition.
2. Identify a phase-sensitive expression; do not take absolute values before deciding which cancellation is mathematically needed.
3. Derive an estimate using a published exponential-sum inequality, bilinear decomposition, or dispersion method. State every replacement or dyadic decomposition and its loss.
4. Identify precisely whether the bound is uniform in the prescribed N, and whether the source theorem itself assumes a distribution conjecture.
5. Work at least one nontrivial special case (fixed rational denominator, a finite admissible shift family, or a short range of N) **symbolically**. If the special case already requires the full missing theorem, identify that reduction; do not hide the difficulty.
6. Produce an adversarial "one-hole" model for any claim derived only from global norms. If it does not satisfy all premises of the actual proposed theorem, it is not a valid refutation of that theorem; articulate the gap.

### M7 Route B — arithmetic bilinear/correlation estimate

1. Start from the exact pair sum \(R(N)\) or its log-weighted prime analogue, with reflection \(p\mapsto N-p\).
2. Apply an independent decomposition: arithmetic progressions, a sieve/dispersion identity, or genuine four-position configurations, not the same arcwise Cauchy proof renamed.
3. Separate necessary congruence admissibility from simultaneous primality, including the sieve parity barrier.
4. Determine whether the proposed target anchored four-prime lower bound is circular. If it uses a selected prime pair at N, the derivation is invalid when testing R(N)=0.
5. Derive either a proved intermediate prime correlation lemma or the exact first unavailable theorem. Compare its strength with the Route A obstacle and decide whether one route is logically weaker.
6. Use a quantified comparison, not intuition, to choose the best continuation. If both routes reach a theorem essentially equivalent to binary Goldbach, state that rather than pretending the problem has been reduced.

### M7 cross-pollination: attempt to join the routes

If Route A yields a signed energy/covariance expression and Route B yields an additive four-prime correlation, write down an **exact bridge identity** (if one exists) that passes between them. Check multiplicity, diagonals, prime powers and signs. A bridge that simply says "these correlate" without a literal equality or valid bound does not count.

In the event of no genuine arithmetic advance, publish a **negative research result** identifying the smallest input missing from both routes and documenting the proof attempts with the *first false or unproved step*.

**Deliverable M7:** \`07_primary_analytic_route_A.md\`, \`07_primary_arithmetic_route_B.md\`, \`07_bridge_and_comparison.md\`, and one explicit candidate theorem statement \`07_candidate_theorem.json\` with status PROVED / CONDITIONAL / REFUTED / OPEN. Commit/push checkpoint.

---

## M8 — HOSTILE INDEPENDENT MATHEMATICAL REVIEW

This is a separate *critical pass*, not the same author's confidence assessment. Follow a structured adversarial protocol; if another model/agent is unavailable within the existing membership, simulate the pass as a new analysis with no reliance on prose conclusions in M0–M7, checking each displayed mathematical claim against its hypotheses from scratch.

### M8a. Verify the repaired PSD statement

Recompute both the false inherited two-projector "gap" and the true six-Pauli-projector gap with two independent techniques. Do not conflate them again. Check that any claimed **specific interval Gram matrix** has been derived from an actual integral and has the alleged optimum, not merely that abstract PSD matrices have the property.

### M8b. Audit all arithmetic and Fourier transformations

- Sign of \(e(-N\alpha)\) and \(e(-j\alpha)-1\);
- whether the **square** is \(S_w^2\), not \(|S_w|^2\);
- factor two between ordered and unordered prime pairs;
- \(p=q\) diagonal and \(N/2\) composite on H;
- impossibility of using prime 2 in a distinct representation for even N>4;
- prime 3 and base-index \(a=0\);
- correct treatment of nonnegative weight support and real-part conditions;
- whether a restricted arc integral is complex and cannot be called positive before symmetry pairing;
- absolute values moved through a sum/integral only by a valid inequality, with all losses recorded;
- any use of unproved pointwise Hardy–Littlewood asymptotics;
- the difference between a sieve survivor and an actual prime.

### M8c. Quantifier and asymptotic audit

For every \(\ll,o,O\) term:
- specify which parameters are fixed;
- which are allowed to grow (shift count \(m=m(X)\), denominator q, smooth weight w, \(\Theta\));
- whether the implied constant is uniform in the target N;
- whether the cutoff is effective and small target exceptions are checked by actual exact computation only when required;
- whether an averaged theorem was converted to a supremum through an unjustified step;
- whether a conditional Dirichlet zero-free assertion was inadvertently omitted when applying a derived 2026 theorem.

### M8d. Active search for countermodels

Choose the *strongest* newly proposed lemma and try to falsify it, rather than checking many weak examples. Construct a rational/complex coefficient-vector countermodel satisfying all of its hypotheses if it is false. For a claim about prime-only polynomials, a general coefficient countermodel cannot refute it; distinguish this explicitly and, when feasible, try a sparse positive-spectrum polynomial that genuinely meets its stated support restrictions. For a claim about actual primes, only rigorous number-theoretic counterexamples or logical proof defects can refute it.

When a proof is invalid, identify the **earliest invalid implication** with the exact equation and state the minimal changed assumption that would repair it. Do not silently rewrite source results or claim a failed argument is an independent theorem.

### M8e. Small exact code, only when mathematically decisive

If a nontrivial combinatorial identity or optimizer equality survives proof, write a small Python+SageMath or alternative exact pair of verifiers with a limited, declared finite domain. Use exact fractions, algebraic numbers, finite fields or symbolic expressions, not floating-point tests as proof. Test the inherited two-projector SDP error specifically; regression must fail if the erroneous "2" optimum is reintroduced. Include the six-projector objective and its exact Jensen bound. Do not produce millions of routine Goldbach checks.

### M8f. Source and novelty audit

Compare any allegedly new number-theoretic result against precise published source statements and preprints. Record known overlap and hypothesis differences. A general functional-analytic identity may be new *to the project's cumulative record* without being new to mathematical literature; state the distinction.

**Deliverable M8:** \`08_independent_proof_audit.md\`, \`08_countermodels_and_repairs.md\`, \`08_evidence_classification.json\`. Include a table of proposed lemmas, verdict, first failed step, repaired statement, and link to the exact proof. Commit/push checkpoint.

---

## M9 — SYNTHESIS, PROVENANCE, AND A SCIENTIFICALLY NARROW NEXT TARGET

Prepare a final report that communicates mathematical value without inflating claims. Do not write a long polished narrative as a substitute for actual proofs. Every reported new theorem must link to a derivation and a separate critic pass. Every experimentally checked observation must state its finite range.

### Deliverables

All under \`results/stage69/\`:
- \`00_erratum_psd_lifting.md\` (already committed; independently audited).
- \`01_prime_specific_exact_convolution.md\`.
- \`02_information_hierarchy_and_no_go.md\`.
- \`03_target_phase_and_arc_decomposition.md\`.
- \`03_signed_analytic_candidate.md\`.
- \`04_residual_arithmetic_and_sieve_barrier.md\`.
- \`04_anchor_correlation_ledger.md\`.
- \`05_verified_primary_literature.md\`, \`05_source_ledger.json\`.
- \`06_sharp_target_criterion_and_robust_errors.md\`, \`06_quantitative_gap_table.json\`.
- \`07_primary_analytic_route_A.md\`, \`07_primary_arithmetic_route_B.md\`, \`07_bridge_and_comparison.md\`, \`07_candidate_theorem.json\`.
- \`08_independent_proof_audit.md\`, \`08_countermodels_and_repairs.md\`, \`08_evidence_classification.json\`.
- \`final_report.md\`, \`theorem_dependency_ledger.md\`, \`failed_approaches.md\`, \`checkpoint_log.md\`, \`verification_manifest.json\`.
- A **short, rigorously chosen** next-stage instruction in \`tasks/NEXT_TASK.md\` stating one concrete analytic question for Stage 70, not an automatic repeat of Stages 63–69.
- Targeted verification programs only for mathematically nontrivial new identities or countermodels. No enormous primality sweeps, arbitrary expanded intervals or misleading performance benchmarks.

### Scientific outputs required

1. A **table of newly proved results** with exact hypotheses, domain, proof file and whether standard external results are used.
2. A list of *refuted or superseded* claims, explicitly including the Stage 68 false SDP-lifting example and any additional detected defects.
3. A detailed map of which operator results are **sharp for arbitrary L2** and which have any additional **proved** true-prime strength.
4. An exact quantitative bridge from a missing prime estimate to \(R(N)>0\) for each N in H, retaining all smoothing/arc/zero-free assumptions and effective constants if actually supplied.
5. A candid assessment of whether the strongest proposed lemma is effectively equivalent to a target-specific binary Goldbach proof. An exact reformulation is not proof progress by itself.
6. A narrow next theorem: either a genuinely weaker prime-correlation distribution lemma or a fully stated no-go theorem for an explicitly delimited class of inputs, with a proposed *proof strategy* and anticipated first obstruction.
7. Links or recorded IDs for source PDFs/preprints and current versions; distinguish current fresh source checks from inherited Stage 64/68 reports.
8. The original three-case formulation preserved verbatim, base-position coordinate treated correctly, and universal claim explicitly OPEN unless independently proved without circularity.

### Milestone quality scorecard (not numerical test volume)

Score each theme as:
- Did it state an exact mathematical problem with nontrivial quantified hypotheses?
- Did it develop at least one complete proof or locate the first unavailable lemma?
- Did it challenge a tempting but false implication or establish a sharp equality case?
- Did it make **new arithmetic use** of actual prime coefficients beyond finite congruence counts?
- Did it compare the strongest claimed bound quantitatively to the required pointwise threshold?
- Did it record source provenance and method limitations?
- Does it advance beyond a repetition of the Stage 68 Hilbert-space optimum?

Do **not** mark a theme successful merely because a report file exists. Use an honest verdict for each; a detailed negative finding can be valuable if it rules out a previously plausible line.

### Git, synchronization and exit discipline

- Git clone: \`/home/user/goldbach-research-github\`; branch: \`cocalc/stage69-deep-prime-specific-localization\`.
- Fetch/push using the already configured dedicated SSH identity, with \`IdentitiesOnly=yes\`. Never display private key content.
- Make a separate verified commit/push checkpoint after each substantial theme. If the local tree is not clean, inspect and preserve changes, do not overwrite.
- Preserve all original Stage 56–68 branches, logs and research papers. Do not merge into \`main\`, force push, reset, remove commits, or rewrite the original Stage 68 erratum-bearing text.
- \`gh\` is optional and known to be unavailable in CoCalc. **Do not install it, request API tokens, or treat a missing CLI as failed publication**. The authenticated GitHub integration in ChatGPT handles draft PR creation. Report the remote SHA and branch compare URL.
- At completion run the relevant existing test suite, \`git diff --check\`, syntax/JSON checks, source SHA-256 manifest generation and clean-tree/remote SHA check. If generated JSON uses changing run times, avoid editing historical files merely to rerun verification; save separate Stage 69 transcripts.
- If the session runs out of context, allowance or permitted time, finish by committing all *actually completed* findings, saying precisely what remains. Do not claim work has continued after stopping; do not invent a duration or indefinite execution.

### Strong scientific constraint

Even if every M0–M9 milestone is finished, this does not imply Goldbach is solved. A final "all milestones complete" means **the requested research process was executed and documented**, not that its hardest hypothesis was demonstrated. A proof claim would require the exact universal quantified theorem, a complete chain of valid independently checked estimates for genuine primes, all small exceptions and zero-free assumptions resolved, and external scholarly review before public declaration.

**End of extended Stage 69 deep-research program.**
