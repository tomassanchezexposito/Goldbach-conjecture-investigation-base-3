# STAGE 68 — EXTENDED DEEP RESEARCH: EXACT ARC-ENERGY ALLOCATION, LARGE-SHIFT SPECTRAL OBSTRUCTION, AND GENUINE-PRIME SIGNED LOCALIZATION

**Execution branch:** \`cocalc/stage68-optimal-arc-allocation-and-pointwise-obstruction\`  
**Parent:** published \`cocalc/stage67-rational-arc-increment-gram\`  
**Repository:** \`tomassanchezexposito/Goldbach-conjecture-investigation-base-3\`  
**CoCalc clone:** \`/home/user/goldbach-research-github\`  
**Evidence status:** the author's original three-case universal coverage remains OPEN.  
**Document language:** English for all GitHub commits, reports, scripts, PR descriptions and research artifacts.

## A. Why this assignment is deeper — and what would count as real progress

This is deliberately **substantially deeper than the Stage 67 assignment**, but **not a request to double the number of computational trials, append thousands of routine cases, or write an artificially longer narrative**. Concentrate the available mathematical effort on the precise **mechanism by which a globally controlled prime exponential-sum fourth moment might or might not yield a signed estimate at one prescribed even integer**.

Every major claim must pass three separate standards:
- **Abstract theorem:** a valid, quantified mathematical statement for exactly specified spaces, indices, operators and budgets; constants optimized or rigorously bounded, and equality/attainability examined.
- **Arithmetic realization:** the exact extra hypothesis needed to apply the abstract theorem to \`S_w(\alpha)^2\` (never \`|S_w(\alpha)|^2\` for prime sums), including its provenance from a theorem about genuine primes, not guessed from a wheel or singular-series heuristic.
- **Logical strength:** the resulting implication must have a carefully diagnosed relation to \`R(N)>0\` in the actual target. Never make a hypothesis that has silently assumed a representation, normalize by \`R(N)\`, or treat a claimed \`o(X^2)\` pointwise energy input as an established fact.

The **deep mathematical questions** are:
1. Can an exact *arcwise constrained* Hilbert-space optimization genuinely sharpen the Stage 67 operator inequality, and when is the sharpening strict?
2. Does an independently proved distribution of fourth-moment mass over rational arcs exist at a scale that would make the corrected Stage 66 sharp energy certificate nonvacuous?
3. Can arithmetic structure of the genuine-prime polynomial give a **signed** saving at a fixed target that the arbitrary-\(L^2\) extremizer cannot realize?
4. If not, which **first missing arithmetic theorem**, with quantifiers, exponents, constants, and support assumptions, is genuinely necessary?

Do not equate a conditional theorem with its verification for primes, do not repackage a Fourier identity as a lower bound, and do not claim to have proved Goldbach without a complete universal, independently reviewed argument.

### Original conjecture to preserve exactly

For even \(N>2\), at least one of
\[
N=p+1,\qquad N=2p,\qquad N=p+q\quad(p<q,\ p,q\text{ genuine primes})
\]
holds; in the third case \(N-2p=2q-N\), which **follows algebraically from \(p+q=N\)** and does not imply primality.

The remaining domain after the first two alternatives fail is
\[
H=\{N\ge4:\ N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\}.
\]
Let \(R(N)=\#\{p<q:\ p,q\text{ genuine primes},\ p+q=N\}\). The unresolved objective is \(\forall N\in H:R(N)>0\). Treat each exception, diagonal and lower endpoint precisely: \(p=q\) is excluded, and for even \(N>4\) the prime 2 cannot occur in a representation because \(N-2>2\) is even. At \(N=4\) the pair \(2+2\) is excluded, and this N is outside H because \(N-1=3\) is prime. For odd primes write \(p=3+2a\) with \(a\ge0\); **do not** confuse this position coordinate with ternary expansions, congruence classes or a progression of difference 3. Prime 3 corresponds to \(a=0\). The exact reflected-index condition is \(a+b=N/2-3\).

## B. Execution protocol for a longer unattended research session

1. Verify a clean working tree and confirm the intended remote branch. Fetch using the already configured dedicated GitHub SSH deploy key with \`IdentitiesOnly=yes\`. Do not display private-key material; do not create new keys, tokens, subscriptions, or private-issue API workarounds.
2. Check out the **existing** Stage 68 branch \`cocalc/stage68-optimal-arc-allocation-and-pointwise-obstruction\`. It already contains a mathematical starting paper \`results/stage68/00_operator_allocation_and_uniform_gram.md\` and this task file. These are proposed/proved-by-draft statements to **audit independently**, not immutable truth.
3. Read \`docs/cocalc_github_pr_workflow.md\` and follow it. The \`gh\` CLI is not installed and **is not required**. Push verified commits through SSH Git. ChatGPT's connected GitHub app creates and updates PRs; give a branch URL and commit SHA instead of calling lack of \`gh\` a publication failure.
4. Read and cite the actual earlier dependencies: Stage 63's prime-only Fourier identity and moment criterion, Stage 64's corrected fourth-moment quantifier audit, Stage 65's exact Fejér kernel and sum-vs-difference erratum, Stage 66's sharp pointwise-energy/aggregate-variation inequalities and Stage 67's rational-arc Gram report. Avoid repeating those proofs except to verify an exact dependency.
5. Work successively through the research themes **M0–M6** below. Each theme requires a mathematical argument, an independent critic check, an explicit verdict, and a short commit/push checkpoint. Proceed to the next theme when a line is blocked: document the *first invalid implication*, not merely "inconclusive".
6. If CoCalc Goal continuation is available, continue automatically through all feasible themes within the already authorized membership/runtime allowance. This is **not** authorization to consume additional paid resources, run indefinitely, install software, reveal private data, create public releases, or force-push. Keep checkpoints so a stopped session does not lose the mathematical work.
7. Spend more effort on proof analysis and falsification than on computation. A small exact check suffices for an exact identity when an all-parameter proof is written. Do not scale finite prime scans for their own sake, do not repeat millions of uninformative configurations, and do not multiply agents merely for activity.

## M0 — Dependency graph and hostile proof audit: do not inherit a subtle algebraic defect

**Primary read:** \`results/stage68/00_operator_allocation_and_uniform_gram.md\`, \`results/stage67/report.md\`, \`results/stage67/adversarial_review.md\`, \`results/stage66/02_arithmetic_modulus.md\`, \`results/stage65/00_erratum.md\`, and \`results/stage64/01_2026_primary_sources.md\`.

Re-derive, from first principles, all of the following *before* relying on them:
- Fourier convention \(e(t)=e^{2\pi it}\), \(\hat f(N)=\int f(\alpha)e(-N\alpha)\,d\alpha\). The polynomial \(S_w^2\) represents ordered **prime sums**. \(|S_w|^2\) represents **prime differences** and must not be substituted into either major- or minor-arc coefficient.
- Exact signed increment
  \[
  \Delta_j(N)=m_w(N+j)-m_w(N)
  =\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)(e(-j\alpha)-1)d\alpha.
  \]
  Distinguish even shifts \(j=2h\), which preserve the parity of the target.
- Hermitian orientation of \(G_E(j,k)=\int_E g_j\bar g_k\), including how the dual variational formula interacts with the complex bilinear coefficient \(\int_E f g_j\) instead of \(\int_E f\bar g_j\). The exact Fourier sign is more important than a convenient matrix notation.
- Stage 66's strict energy-exclusion threshold for a single missing target:
  \(\|m_w\|_{\ell^2}^2\ge A_X^2+m(A_X-\sqrt{V/m})_+^2\),
  provided \(|m_w(N)|\ge A_X\) and \(V=\sum_{j\in J}|\Delta_j(N)|^2\) is independently bounded.
- Stage 67's measure estimate for Li–Liu major arcs \(P=X^\kappa,\ \kappa<1/2\). Count overlapping rational intervals only once; justify using the crude upper bound \(|\mathfrak M|\le2P^2/X\), independently of overlap. Do not assume a complement measure estimate on *selected* minor arcs without specifying their actual partition.
- Reality: with real weights, the **full** sum coefficient is real. A separately restricted major/minor or arcwise coefficient is real only when the corresponding region is reflection symmetric (or paired with its reflected region). If not, the required sign condition concerns its **real part**, not an unjustified real-valued individual piece.
- Small primes, \(N=4,6,8\), the prime diagonal, and support of the smooth weight. A positive smoothed prime coefficient is a genuine prime-pair witness; a missing pair forces the coefficient zero. The converse "coefficient zero implies no representation" is not true when the weight has limited support and may vanish on all available pairs.

**Deliverable:** \`results/stage68/01_dependency_audit.md\`, with a table of theorem → exact dependencies → arithmetic assumptions → known counterexamples → status. If the prewritten theorem or source report contains a false mathematical step, preserve the original history, write a transparent correction in this branch, and identify the *first* invalid implication.

## M1 — Prove the genuinely sharper arc-budget operator allocation theorem

Read Section 2 of the initial Stage 68 note. Treat the note as a conjectured statement to independently prove or refute.

Let \(E_1,\dots,E_R\) be pairwise disjoint measurable pieces of the full minor set, \(J=\{j_1,\ldots,j_m\}\) distinct nonzero integer shifts, and
\[
g_j(\alpha)=e(-N\alpha)(e(-j\alpha)-1),\quad
G_r(j,k)=\int_{E_r}g_j\bar g_k.
\]
For arbitrary \(f_r\in L^2(E_r)\) with \(\|f_r\|_2^2\le B_r\), analyze **exactly** the optimum
\[
\mathcal U(B_1,\dots,B_R;G_1,\dots,G_R)
=\sup_{\|f_r\|_2^2\le B_r}
\left(\sum_{j\in J}\left|\sum_r\int_{E_r}f_r g_j\right|^2\right)^{1/2}.
\]
The target identity is
\[
\mathcal U
=\max_{\|z\|_2=1}\sum_r\sqrt{B_r}\sqrt{z^*G_rz}.
\tag{A}
\]
Develop **two distinct proofs**: (i) support functions / Hilbert-space duality with an explicit saturating function, and (ii) direct operator-sum analysis using adjoints/singular vectors. Be precise about complex conjugation, zero eigenvalues, zero budgets and infinite-dimensional domains. State the equality condition for the simpler triangle bound
\[
\mathcal U\le\sum_r\sqrt{B_r\lambda_{\max}(G_r)}.
\tag{B}
\]
Is a **common top eigendirection** for all active \(G_r\) necessary and sufficient for (B) to be attained? Account for nonunique largest eigenspaces and \(\lambda_{\max}(G_r)=0\). If the answer requires an extra qualification, give its exact form.

Analyze strict improvement over (B) by an example with nonaligned eigenspaces. Distinguish an abstract PSD-matrix example from matrices that can arise from the **particular rational-arc multipliers**. Attempt to realize at least one strict-improvement example with genuine interval Gram matrices or rigorously prove why a proposed realization fails. This is a deep geometry question, not a request for many numerical tests.

Examine whether there is a useful **dual or convex formulation** to optimize the expression in (A) with computable certified bounds (e.g. a semidefinite relaxation, a second-order cone reformulation, or a minimax over positive weights). Prove the inequalities and qualification conditions; do not assert global convexity in the wrong variables. Investigate the difference between a statement for unrestricted complex \(L^2\) inputs and the actual real-symmetric prime-square input.

**Deliverable:** \`02_exact_budget_optimization.md\`, with precise theorem and sharpness/equality statements, one independent proof, a second argument attempted and audited, and a clear description of what this adds beyond Stage 67.

## M2 — Uniform-in-shift-count spectral obstruction; no premature conclusion about arithmetic

Stage 67 proved that for **fixed** shift count \(m\), the complete minor-set Gram approaches \(I+\mathbf1\mathbf1^*\) because only \(o(1)\) circle measure is removed. The initial Stage 68 note claims the following *stronger statement uniformly in m*:
\[
m+1-4m|\mathfrak M|
\le\lambda_{\max}(G_{\mathfrak m})\le m+1,
\quad\mathfrak m=\mathbb T\setminus\mathfrak M.
\tag{C}
\]
Prove it via the Loewner order and the Rayleigh quotient of the all-ones unit vector. Independently seek a counterexample when shifts depend on X, and decide exactly whether the relative bound
\[
\lambda_{\max}(G_{\mathfrak m})/(m+1)=1+O(|\mathfrak M|)
\]
holds for **every finite** \(J(X)\). Quantify what happens if \(m\) grows as \(X^{1/2}(\log X)^{100}\), the order demanded by the earlier local-energy scale. Distinguish absolute additive errors \(O(m|\mathfrak M|)\) from relative errors \(O(|\mathfrak M|)\).

A genuine research extension is to consider **subspaces** or weighted directions rather than only the top operator norm:
- Determine whether a known family of vectors \(z\) orthogonal to the constant direction could enjoy a stronger Gram bound on the complete minor set, and whether the true-prime increment vector is known to belong to that subspace. Do not assume orthogonality from averaging.
- Study the smaller eigenvalues/condition number of \(G_{\mathfrak m}\), especially for an \(m\)-dependent shift set, and whether the geometry alone produces a **signed** target estimate. Spectral improvement in irrelevant directions has no value unless an independent prime theorem selects those directions.
- Quantify resonance across denominators: \(q\mid j\) for reduced rational centers \(a/q\); for even shifts \(j=2h\). Show that a single nonzero shift of bounded size cannot resonate at all denominators \(\le P\) as \(P\to\infty\) without a rapidly growing least common multiple. You may cite established estimates for \(\operatorname{lcm}(1,\ldots,P)\) after verifying their exact hypotheses; a weaker elementary divisor argument is acceptable. Investigate whether restricting to specially chosen moduli has any **proved** advantage once the complementary minor arcs and shift range are accounted for.

**Deliverable:** \`03_uniform_spectral_no_gain.md\`, including the strongest **correctly quantified** geometric no-go theorem, proof of its scope, possible subspace loopholes and their required arithmetic assumptions.

## M3 — Exact allocation of fourth-moment mass across rational arcs: necessary and sufficient budgets

For an actual prime-only polynomial
\[
S_w(\alpha)=\sum_{p\ {\rm prime}}(\log p)w(p/X)e(p\alpha)
\]
and a **disjoint** full-minor partition \(\mathfrak m=\bigsqcup_r E_r\), let
\[
B_r=\int_{E_r}|S_w(\alpha)|^4\,d\alpha,\qquad
B=\sum_rB_r.
\]
Use M1 to get the exact unrestricted worst-case increment-vector bound for any verified upper budgets \(\bar B_r\):
\[
V(N)=\sum_{j\in J}|\Delta_j(N)|^2
\le\left(\max_{\|z\|=1}
\sum_r\sqrt{\bar B_r}\sqrt{z^*G_rz}\right)^2
=:\bar V.
\tag{D}
\]
Check carefully that the same arc partition is used for all terms and that only the *total* fourth moment is known from the cited Li–Liu result.

**Prove the collapse theorem:** if the only input is \(\sum_r B_r\le B\), optimally assigning nonnegative budgets to pieces recovers exactly
\[
\sup_{\sum_r B_r\le B}\mathcal U=\sqrt{B\lambda_{\max}(\sum_rG_r)}.
\tag{E}
\]
This means disjointizing the circle and replacing one norm by many symbols does not create mathematical information. Derive equality by optimizing over \((B_r)_r\), with all zero cases and full-support constraints.

**State a correctly quantified sufficient criterion** to rule out a zero at a *prescribed* residual target \(N\):
if a valid independent major-arc theorem gives \(a_w(N)\ge A_X>0\), then
\[
A_X^2+m(A_X-\sqrt{\bar V/m})_+^2>\sum_r\bar B_r
\tag{F}
\]
would contradict \(R(N)=0\) via the sharp Stage 66 aggregate theorem and Parseval. Prove this implication without presuming the existence of a representation and without mixing \(\bar B\) with an exact \(B\). State what happens if some arc contributions are complex, if the major/minor partition is not symmetric, or if weights are not nonnegative.

**Sharpness and feasibility study — this is the substantive heart of M3:**
- With only Li–Liu's (conditional) **global** \(B\ll X^{5/2}(\log X)^{100}\) and \(A_X\asymp X\), derive the optimal exponent and logarithmic gain that (F) would require, uniformly at each \(N\in H\).
- Analyze the range \(m\lesssim B/A_X^2\) where the certificate is intrinsically vacuous, and the larger \(m\) range where \(\bar V/m\) must be at most the \(A_X^2\) scale. Explain any additional restriction that shift indices must lie in a meaningful target range and preserve even parity.
- Introduce a **meaningful** denominator- or dyadic-frequency-resolved candidate hypothesis \(B_{q,r}\) with explicitly defined disjoint pieces and all \(q,X,\kappa\) dependencies. Derive the *minimum strength* of independent estimates on these \(B_{q,r}\) that would make (F) strict, or prove that a proposed allocation cannot help even under optimistic estimates.
- The signed nature matters: ordinary energy bounds control absolute values, not signs. Test whether a **phase/cancellation** condition between arc pieces offers a logically weaker and analytically more plausible target-anchored input than extremely small arcwise energies. Formulate it without simply requiring \(m_w(N)>-a_w(N)\) by name; explicitly test whether your new assumption is quantitatively **stronger or weaker** than direct positivity.

**Deliverables:** \`04_arc_budget_feasibility.md\` with a theorem/countermodel/conditional matrix and a formula-level threshold ledger; \`04_proof_obligations.json\` listing each missing arithmetic estimate with exact quantified form.

## M4 — Recover genuine-prime structure beyond arbitrary Hilbert-space functions

The preceding theorems are optimal over **all complex \(L^2\)** functions. The real problem concerns highly structured
\[
f_X(\alpha)=\mathbf1_{\mathfrak m}(\alpha)S_w(\alpha)^2
\]
with \(S_w\) supported on **prime integers**, real nonnegative coefficients, and finite Fourier support. Search for a strictly stronger inequality that exploits this structure **without merely assuming the desired representation**.

Investigate several distinct, logically testable mechanisms:

**(a) Autoconvolution positivity and support.**
The coefficient of \(S_w^2\) is
\[
r_w(N)=\sum_{p+q=N}a_pa_q\ge0,
\]
but the *minor-arc component* may be signed. Determine what the nonnegative coefficient cone implies about the possible isolated negative value \(m_w(N)\) after removing major arcs. Construct small analytic-polynomial countermodels with nonnegative coefficients and omitted target frequencies, clearly marking whether their support consists of genuine *all* primes in the relevant range or an artificial sparse subset. A countermodel for arbitrary positive coefficients does **not** refute a theorem for all genuine primes.

**(b) Parity and half-period symmetry.**
When the smooth weight vanishes at 2 and the polynomial includes only odd primes, \(S_w(\alpha+\tfrac12)=-S_w(\alpha)\), so \(S_w^2\) is half-periodic. Check exactly when the cited major/minor arc sets are or are not invariant under translation by \(\tfrac12\). If not invariant, odd-index Fourier coefficients of the *restricted minor-arc* function need not vanish even though the full coefficient has even support. Determine whether pairing arcs related by half-shifts yields an exact usable improvement or merely moves mass between major and minor sets. State the \(X\) threshold for the weight to exclude 2, using the actual compact support \(w\), not an invented support endpoint.

**(c) Base-3 reflected positions and wheel constraints.**
Retain \(p=3+2a\), \(q=3+2b\), \(a+b=N/2-3\). Derive exactly how reflection affects the finite Fourier polynomial, parity and congruence restrictions modulo \(3,5,7,210\); separate \(a=0\) for prime 3 and small prime exceptions. Test whether the conditions \(N-1\) composite and \(N/2\) composite imply any new **necessary arithmetic congruence** on prime-pair positions that is not already encoded by the ordinary target sum \(p+q=N\). If such a congruence exists, prove it and show why it helps; otherwise explain why local survivorship does not produce an independent positive signed correlation estimate. Do not confuse a coordinate reparametrization with a distribution theorem.

**(d) True-prime shared/four-distinct correlations.**
Use the Stage 63 exact shared-prime \(S(u,v)\) and four-distinct \(Q_4(u,v)\) decompositions. Seek *signed* relationships for short shifts that are not consequences of nonnegativity alone. If you formulate a lower bound on \(Q_4(N,N+j)\), test whether it already implies \(R(N)>0\) and whether its proposed proof is circular. Compare the exact four-prime structure with the four-fold Fourier moment \(|S_w|^4\); identify any term-by-term connection and whether arc restriction destroys simple positivity.

At least one of these mechanisms should receive a serious, proof-driven attempt, **not four superficial paragraphs**. Classify each candidate as a proved theorem, conditional result, failed inference, computational observation, or unresolved problem.

**Deliverable:** \`05_prime_specific_structure.md\`, with original lemmas only if their proofs survive independent criticism, plus a logical-strength table comparing candidate hypotheses to \(\forall N\in H:R(N)>0\).

## M5 — External mathematical literature: source-level comparison, not a citation list

Audit the most relevant original theorems on binary Goldbach, the Hardy–Littlewood circle method, the parity problem for sieves, prime exponential sums, bilinear/minor-arc moment estimates, distribution in arithmetic progressions and any genuinely **localized** fourth-moment/correlation bound.

Start with the already checked 2026 source chain, but re-verify date, version, exact hypotheses and scope when fresh network access is available:
- H. Li and Z. Liu, *Fourth moments of prime exponential sums and exceptional sets for sums and differences of primes*, arXiv:2610.26756v1 (October 2026).
- J. Pintz and I. Althöfer, *The Goldbach exceptional set: an exponent 7/12 and conditional refinement*, arXiv:2610.15559v1 (October 2026).
- I. Althöfer, D. Chen, A. Perelli and J. Pintz, *The exceptional set of Goldbach numbers among polynomial values*, arXiv:2611.09386v1 (November 2026).
- G. Bhowmik and L. Grimmelt, *The exceptional set of the Goldbach problem*, *Analysis Mathematica* 52 (2026), 767–808, DOI \`10.1007/s10476-026-00191-z\`.
- Classical results of Chen, Bombieri–Vinogradov, Montgomery–Vaughan, Vaughan's identity, and the exact minor-arc or exceptional-set inputs cited in the sources above.
- If a new result depends on OpenAI's 2026 \(7/8\) zero-free manuscript or Lean repo, distinguish **the manuscript's claim**, its formalized exact scope, a completed Lean build, preprint status, and downstream applications; do not promote the whole chain to a peer-reviewed unconditional Goldbach theorem merely because another paper cites it.

For EACH claimed theorem that might help our allocation estimate:
1. Write its literal quantifiers and the correct normalization of \(S_w\), \(C_\Lambda\), \(r_w\) or \(\mathfrak S(N)\).
2. State whether it is unconditional, conditional on common Dirichlet-L zero bounds, dependent on an ineffective constant, or only for *almost all* targets.
3. Compare its scaling directly to (F), **including logarithms, denominator/shift range, signs and dependence on N**.
4. Identify any loss of target localization in applying Parseval, a large sieve, a Hölder inequality or an exceptional-set threshold. Name the *first* step where a theorem about an average is improperly used at a prescribed residual target.
5. Make an honest source/provenance table: paper, authors, date, version, theorem label, proof status, URL/DOI, key assumptions, and what it does *not* prove. If a source cannot be retrieved, say so and do not fabricate content.

Do not equate \(\#E(X)\ll X^\delta\) for \(\delta>0\) with an empty exceptional set; it permits a singleton. Be especially skeptical of new online manuscripts claiming full Goldbach without independently checkable proof.

**Deliverable:** \`06_literature_and_theorem_strength.md\` with an implication matrix and a provenance JSON ledger. Distinguish researched external facts from statements inherited from Stage 64.

## M6 — Primary analytic attempt, independent critic, synthesis and next-stage handoff

Choose the **single strongest genuinely non-circular research avenue** identified by M1–M5. Write its exact candidate theorem *before* analyzing data or claiming evidence. The candidate must include all variables and uniformities:
\[
X,\ N\in H\cap[X/2,X],\ q,\ a,\ h,\ J,\ w,\ \mathfrak M,\ \mathfrak m,\ \Theta,
\]
where applicable, as well as effective constants and the allowed dependence of implied constants on the smooth weight.

Develop the attempt through a full proof cycle:

**Proof pass 1:** derive every deterministic reduction and operator identity; isolate where a genuine-prime distribution theorem is required. If an extra hypothesis is proposed, prove it from published results or mark it as **OPEN** explicitly.

**Proof pass 2:** attempt a materially distinct derivation. Examples: (a) dual variational optimization versus direct operator factorization; (b) a conditional signed minor-arc decomposition versus covariance/energy; (c) frequency localization in rational arcs versus target localization in additive shifts. These must not be the same argument with variables renamed.

**Adversarial critic pass:** construct the strongest relevant countermodel, with all hypotheses satisfied, for any abstract inequality being rejected; test impossible residues, equality/sharpness cases, complex conjugates, endpoint effects, major/minor overlaps, odd/even parity and the zero-target model. If a candidate statement fails, name the first false inference and stop refining the same failed proof.

**Quantitative implication pass:** show whether the attempted estimate actually makes (F) strict for all sufficiently large N, with an explicit cutoff if one has proved all constants. If it only yields a positive proportion of represented targets, an exceptional-set bound, or a conditional theorem with an unproved premise, classify accordingly. Do not silently replace a target-specific estimate with an averaged version.

**Literature consistency pass:** compare the strongest surviving lemma with established literature, including the recent 2026 conditional preprints. A standard Hilbert-space theorem may be useful inside the project without being represented as a novel external mathematical breakthrough.

### Required final deliverables

Save under \`results/stage68/\`:
- \`00_operator_allocation_and_uniform_gram.md\` (already present; audit and correct in this branch if needed).
- \`01_dependency_audit.md\`.
- \`02_exact_budget_optimization.md\`.
- \`03_uniform_spectral_no_gain.md\`.
- \`04_arc_budget_feasibility.md\` and \`04_proof_obligations.json\`.
- \`05_prime_specific_structure.md\`.
- \`06_literature_and_theorem_strength.md\` and \`06_sources.json\`.
- \`07_primary_analytic_attempt.md\`.
- \`08_adversarial_review.md\`.
- \`final_report.md\`, \`theorem_dependency_ledger.md\`, \`checkpoint_log.md\`, and \`verification_manifest.json\`.
- **Only targeted** exact Python/SageMath verifiers and their machine-readable outputs where they distinguish a nontrivial equality case, conjugation orientation, a nonaligned Gram example, an arcwise budget allocation, or a countermodel. Do **not** manufacture thousands of repetitive numerical trials or large prime-count sweeps.
- An updated \`tasks/NEXT_TASK.md\` with the *narrowest analytically meaningful Stage 69* question, including the exact missing estimate and why the predecessor stages cannot supply it.

Final review must include:
- Explicit evidence labels **PROVED**, **EXTERNAL THEOREM**, **CONDITIONAL**, **REFUTED**, **FINITE VERIFICATION**, and **OPEN**.
- Exact equations and numbered lemmas with full hypotheses, proof locations and dependencies.
- Two independent mathematical derivations of the most important new statement, and one independent computational check if informative.
- A specific table of the strongest new constants versus the required prime-arithmetic saving.
- Clear audit of every use of primes 2 and 3, exclusion of \(p=q\), positivity of smooth weights, and target-evenness.
- At least one **credible failed approach** with its first mathematically invalid step, if any was encountered.
- Source versions/URLs and disclosure of anything inaccessible or not independently checked.
- A concise but scientifically candid summary for the user: what was **newly proved**, what was **only sharpened conditionally**, which hypotheses were **refuted**, and what exact theorem is still unavailable.

### How to checkpoint, publish, and stop correctly

Commit/push each completed mathematical theme M0–M6 to the Stage 68 branch with unambiguous commit messages and exact source hashes in a manifest. Preserve the original history of Stages 56–67; never rewrite, reset, force-push or merge into \`main\`. Before reporting success, confirm \`git status\` is clean and \`git ls-remote\` shows that the remote branch head matches the local final commit.

**Do not stop the research merely because \`gh\` CLI is unavailable.** GitHub PRs can be created and reviewed by ChatGPT's authenticated GitHub integration. Report the remote branch link/compare link and commit SHA; a new PR is optional and handled outside CoCalc.

Do not install tools or spend money without approval. Work deeply within the available runtime and allowance; if a limit ends the run, report the latest committed milestone and exact remaining obligations rather than implying unattended future completion.

**Acceptance standard:** a thorough, original mathematical investigation that either establishes a non-circular, quantitatively useful new prime-specific bound, or proves a sharp operator/allocation obstruction and identifies the smallest genuinely missing prime-theoretic lemma with quantified constants. Merely doubling the number of examples or adding generic prose does not count as deeper research.

**End of Stage 68 deep assignment.**
