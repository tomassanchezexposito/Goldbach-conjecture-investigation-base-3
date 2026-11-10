# STAGE 63 — EXTENDED UNATTENDED MATHEMATICAL RESEARCH PROGRAM

**Project:** Prime-Correlations-210 / author's independent three-case representation conjecture  
**Execution environment:** the existing CoCalc SageMath/Codex project and its already cloned private GitHub repository  
**Authoritative integration base:** \`cocalc/stage62-singular-series-local-variation\`  
**Work branch:** \`cocalc/stage63-extended-analytic-program\`  
**Evidence status at handoff:** universal coverage is OPEN. No proof of strong Goldbach is claimed.

## 0. Mission, execution contract, and boundaries

The researcher will be away for several hours and cannot answer routine follow-up questions. Treat this as an authorization to **complete the full multi-milestone plan**, continuing from one subproblem to the next without needing a new user message, **as long as the existing project, selected model allowance and resource limits permit**. Do not interpret it as permission for spending money, changing subscriptions or project permissions, expanding access to secrets, installing software, deleting work, or force-pushing. CoCalc Goals may permit automatic continuations, but cannot guarantee uninterrupted running or unlimited allowance.

Work only inside the existing clone \`/home/user/goldbach-research-github\` (or confirm its actual location before proceeding). Preserve all prior source branches and experiments. Use the previously configured dedicated GitHub deploy key, explicitly selecting its identity if needed; never display secret content. Do not let a missing GitHub CLI or private issue API 404 block research: read checked-in handoffs and task files, and use SSH Git to push.

**A milestone counts as completed only with a written proof/analysis, a test or independent audit, and a committed GitHub checkpoint.** Proceed to the next milestone after recording a successful checkpoint. If a line of argument fails, document the first invalid implication and redirect, instead of producing repetitive unfalsifiable narrative or ever-larger finite intervals. Focus on mathematical progress, not wall-clock duration.

**Suggested workflow order:** M0 (state and audit), M1 (new exact CRT local factors), M2 (direct target-anchored Fourier formulation), M3 (evaluate singular-series-adjusted graph certificates), M4 (external analytic results and bottleneck), M5 (challenge one genuinely independent estimate), M6 (independent adversarial review, publication and long-form synthesis). Complete all feasible milestones within the current agent session/goal and stop cleanly only upon a real limit or after the full plan.

Set the directory for all research artifacts to \`results/stage63/\` with meaningful subdirectories. Use English for **all** GitHub repository code, comments, reports, notebooks, commit messages, and PR text. The ChatGPT conversational answer to the user may be in Spanish when requested.

### User's original formulation: do not silently replace it

For every even integer \(N>2\), at least one of these holds:

1. \(N=p+1\) for a prime \(p\);
2. \(N=2p\) for a prime \(p\);
3. \(N=p+q\) for **distinct primes** \(p<q\), such that \(N-2p=2q-N\).

The reflection equality follows algebraically from \(p+q=N\): **it does not assert simultaneous primality**. Cases need not be disjoint.

The remaining domain is
\[
H=\{N\ge4:\ N\ {\rm even},\ N-1\ {\rm composite},\ N/2\ {\rm composite}\}.
\]
For \(N\in H\), the first two clauses fail, and we must prove \(R(N)>0\), where
\[
R(N)=\#\{p<q:\ p,q\ {\rm genuine\ primes},\ p+q=N\}.
\]
Do not assume \(R(N)>0\), normalize by \(R(N)\) before proving it positive, use averages as a pointwise estimate, or call wheel-210 survivors prime pairs.

The user's base-3 *position* notation for odd primes is \(p=3+2a\), \(q=3+2b\), \(a<b\), \(a+b=N/2-3\). Keep the exact interpretation; **do not equate it with ternary digits or congruences modulo 3**. Handle p=3 as a=0, p=q as an excluded diagonal, and the even-prime exception separately.

## M0 — Recover and independently audit the existing Stage 56–62 record

**Read:** \`README.md\`, \`docs/research_protocol.md\`, \`docs/stage60_integration_handoff.md\`, the current \`tasks/NEXT_TASK.md\`, reports \`results/stage57/report.md\`, \`results/stage58/pointwise_second_moments.md\`, \`results/stage59/report.md\`, \`results/stage59/research_note.md\`, \`results/stage60/report.md\`, \`results/stage61/report.md\`, \`results/stage62/report.md\`, and their manifests/tests. Locate any additional original base-3 definitions rather than inventing them. Record exact source paths and commit hashes.

**Verify and label:**

- Stage 56: strict block variance threshold has known counterexamples even without zero representations.
- Stage 57: signed covariance can be negative; exact four-prime partition identities are not a positivity estimate.
- Stage 58: sharp finite-block one-zero/multi-zero and weighted moment inequalities; the best unknown-zero two-moment threshold does not improve merely by unequal weights.
- Stage 59: exact path/cycle/graph Laplacian certificates; positive mean and sufficiently small **independently controlled** energy would imply positivity, but real-prime bounds are absent.
- Stage 60: \(0\le R(N)\le\lfloor(N-4)/4\rfloor\) (even N), and four-prime candidate upper bounds are too weak to exclude zeros.
- Stage 61: exact signed expression
  \[
  9D_N=-a^2-3b^2-c^2+6ab+2ac+6bc,\quad
  a=X_{N-2},\,b=X_N,\,c=X_{N+2}.
  \]
  When \(b=0\), \(9D_N=-(a-c)^2\le0\). Its common-relative-error hypothesis over **all three genuine-prime counts** already gives \(b>0\), hence is not an independent proof input.
- Stage 62: \(\mathfrak S(n)=2C_2\prod_{p\mid n,p>2}(p-1)/(p-2)\) is the **arithmetically defined conventional singular series**, not an established pointwise asymptotic for the actual representation count. The CRT + Dirichlet/Euler construction yields infinitely many N in H with \(A_{210}(N)=A_{210}(N+2)=15\) but unbounded adjacent *singular-series* ratios. The later Stage 62.4 uses Linnik's least-prime theorem to construct N in H with the center singular-series profile asymptotically dominating both neighbors and the signed path certificate **negative for the model**. Check the full proof, not just the summary; verify the Linnik dependency, coprime CRT residue, growth of q_y, bounded factors for q_y−2, and constants.

**Independence test:** re-run focused previous verifiers where practical and inspect source/manifest hashes; cross-check at least one important algebraic identity by a distinct routine. If a claim is wrong, issue a revision document preserving the original wording and identify the first incorrect inference before moving on.

**Deliverables:** \`results/stage63/00_provenance_and_audit.md\`, \`00_manifest.json\`, and a reproducibility transcript. Commit/push checkpoint \`stage63: provenance and critical audit\`. If progress cannot be pushed, preserve local commits and record the exact transport error.

## M1 — Derive new exact modular arithmetic for SHARED-prime triple positions

For two distinct even targets \(n\ne m\), a shared prime \(x\) forces the three numbers \(x,n-x,m-x\) to be prime (with diagonal exclusions). The exact contraction count is
\[
S_{n,m}=\sum_{\substack{x\ {\rm prime}\\
n-x,\ m-x\ {\rm prime}\\
x\ne n/2,\ x\ne m/2}}
1
\]
with the inherent positivity/range requirements, and the off-diagonal four-distinct count is \(Q_4(n,m)=R(n)R(m)-S_{n,m}\). Check that no configuration is double-counted and that the constraints \(p<q\) are treated correctly: common \(x\) is not always the *lower* summand, so \(S_{n,m}\) needs an explicit range convention and must enforce \(n-x>1,m-x>1\). If the displayed triple sum counts a shared x more than once or misses endpoint restrictions, correct it explicitly rather than repeating the formula.

**Candidate local factor (exact CRT identity):** for squarefree \(W=\prod_{\ell\in P}\ell\), derive
\[
T_W(n,m)=\#\{x\bmod W:\gcd(x(n-x)(m-x),W)=1\}
=\prod_{\ell\mid W}(\ell-\nu_\ell(0,n,m)),
\]
where \(\nu_\ell(0,n,m)\) counts the *distinct* residues in \(\{0,n,m\}\bmod\ell\). The formula is exact by CRT. For \(W=210\), analyze when \(T_W=0\), classify local obstructions, and show small-prime exceptions (especially x equal to 3, 5, 7, and p=2 when relevant) may survive a zero factor if a prime term itself equals a factor of W. **Do not** infer that \(T_W>0\) implies genuine prime triples.

Use actual Stage 57/61 shared-prime correlations for \(m=n+2\), \(n+4\), \(n+2h\) as a cross-check. Also formulate an analogous four-position wheel count for \((p,n-p,r,m-r)\) with distinctness conditions; determine carefully whether its straightforward CRT product is genuinely new or just a restatement of existing per-target factors. Explicitly distinguish:
- exact modular identity;
- a trivial candidate upper bound;
- probabilistic prime-tuple heuristic;
- actual proven lower/upper bound for genuine primes.

**Independent proof and tests:** provide a direct enumerator on all residues modulo 210 and an independent product-based Sage/Python checker; test small n,m, boundary primes, and a locally obstructed case. Include precise statements, quantified domains, and proof. Produce \`01_shared_prime_modular_lemma.md\`, \`01_verify_modular.py\`, \`01_exact_cases.json\`. Commit/push checkpoint.

## M2 — Build and audit the direct TARGET-ANCHORED prime-only Fourier identity

Let \(e(t)=e^{2\pi it}\). For a fixed even N define
\[
S_N(\alpha)=\sum_{\substack{p\le N\\p\ {\rm prime}}}(\log p)e(p\alpha).
\]
Prove exact orthogonality (no asymptotics):
\[
\int_0^1 S_N(\alpha)^2 e(-N\alpha)\,d\alpha
=2\sum_{\substack{p<q\\p+q=N}}(\log p)(\log q)
+\mathbf1_{\{N/2\ {\rm prime}\}}(\log(N/2))^2.
\]
For \(N\in H\), the diagonal vanishes by definition, so positivity of the *full integral* is exactly equivalent to the genuine-prime distinct-pair existence. No division by \(R(N)\) is used. Distinguish weighted prime representation count \(\sum_{p<q}\log p\log q\) from \(R(N)\).

Partition the exact integral into major and minor arcs **with explicit measurable sets that cover [0,1]**. Express a precise unconditional *sufficient* statement:
- an independently justified lower bound \(M_N\) on the **real** major-arc integral;
- an independently justified upper bound \(E_N\) on the magnitude of the **real** minor-arc integral;
- \(M_N>E_N\) on each residual N, or a weighted diagonal-adjusted equivalent for all even N.

Do **not** assert either estimate merely because the singular series is positive; pointwise binary Goldbach is the missing issue. Propose the narrowest analytical lemma about a signed minor-arc term that would suffice, with constants/ranges and an effective finite cutoff if the external result supplies it.

Compare exact prime-only Fourier coefficients with the von Mangoldt-weighted coefficient \(\sum_{m+m'=N}\Lambda(m)\Lambda(m')\). Identify prime powers \(\Lambda(p^k)\) for k>=2, evaluate rigorous error upper bounds with explicit/logarithmic factors, and separate the p=q diagonal. Check the positive sign and every multiplicity exactly. Determine whether any already established theorem supplies the needed target-uniform minor-arc error, and quote exact hypotheses.

**Verification:** two independent computations of Fourier coefficients for selected small N (one exact algebraic convolution, one symbolic roots of unity / finite DFT over an integer modulus >2N, **not** floating quadrature as a purported proof). Test all diagonal and prime-power cases. Keep these focused to test *identities*, not vast Goldbach ranges.

**Deliverables:** \`02_fourier_pointwise_framework.md\`, exact verifier, explicit missing-bound ledger. Commit/push checkpoint.

## M3 — Adversarial test of singular-series-adjusted graph/energy positivity

Motivation: Stage 62.4 establishes that the existing signed *path certificate* is negative along an infinite sequence for the **full singular-series arithmetic profile**, even when both neighboring targets and the center belong to the relevant even range. The arithmetic model is **not** the actual prime-pair count.

Analyze at least three distinct mathematical approaches:

**Track A: model-adjusted normalization.** Define a positive arithmetic profile
\[
\Phi(N)=\frac{F(N)N}{A_{210}(N)(\log N)^2}
\]
for even N sufficiently large (and define a harmless exact lower-end convention). Consider \(Y_N=X_N/\Phi(N)\). This is a purely algebraic normalization by known N-dependent factors, so Y_N is well-defined even if R(N)=0. Re-derive the exact three-point signed certificate using Y in place of X and expand it explicitly in true-prime correlations, including the \(\Phi\) denominators. ***Crucial:*** neither Y_N≈constant nor Y_N>0 is assumed. Explain exactly which independent prime-only bounds would make a Y-certificate positive and which are simply alternative ways of assuming the conclusion.

**Track B: target-anchored weighted graph energies.** Recover Stage 59's path/cycle/graph estimates (do not silently recycle them as new). For a graph with vertices representing even targets and positive preassigned arithmetic weights depending on N, derive a sharp coordinate-vs-energy inequality using a pseudoinverse/Green kernel when it actually strengthens the prior argument. Test the hypothetical one-zero profile in the exact inequality and make clear whether the proposed graph lower mean is independent of the central count. Distinguish changing the deterministic constant from new prime-distribution content.

**Track C: direct anchored mixed-prime-correlation positivity.** Re-express the Stage 61 signed four-prime combination
\[
9D_N=-\frac{R_-^2}{A_-^2}-3\frac{R_0^2}{A_0^2}-\frac{R_+^2}{A_+^2}
+6\frac{R_-R_0}{A_-A_0}+2\frac{R_-R_+}{A_-A_+}+6\frac{R_0R_+}{A_0A_+}
\]
through exact shared-prime triple counts and four-distinct configurations. Identify which positive terms are anchored at N and which are off-center. Give abstract countermodels demonstrating why lower bounds on exclusively off-center correlations cannot imply center positivity.

For every proposed improved criterion, build a **logical-strength table**:
1. Is its hypothesis directly implying \(R(N)>0\) without other reasoning?
2. Is the hypothesis independently proved from arithmetic (or merely assumed/empirical)?
3. Is it consistent with the explicit singular-series profile of Stage 62?
4. Can its needed constant be obtained from published unconditional theory?
5. Does it genuinely improve the prior criterion, or merely change coordinates?

If the model refutes uniform certificate feasibility, state it rigorously and pivot; do not repeat the same failed local-smoothness strategy.

**Deliverables:** \`03_adjusted_energy_comparison.md\`, proof scripts/finite exact countermodels, status table. Commit/push checkpoint.

## M4 — External literature review, exact implications, and the parity barrier

Consult primary or peer-reviewed sources wherever network access permits. At minimum, verify citation details and **read the mathematical hypotheses** (not just abstracts) for:

- G. Bhowmik & L. Grimmelt, *The exceptional set of the Goldbach problem*, Analysis Mathematica 52 (2026), 767–808, DOI \`10.1007/s10476-026-00191-z\`, https://link.springer.com/article/10.1007/s10476-026-00191-z — explicit major-arc formula, exceptional-set estimates, and the stated conditions involving a sparse Hardy–Littlewood conjecture. The paper does **not** claim unconditional zero exceptions.
- J. R. Chen (1973), theorem on representation of all sufficiently large evens as a prime plus a product of at most two primes: near-prime is not genuine prime.
- Montgomery–Vaughan (1975) and Pintz (2018) exceptional-set results: reconcile strength (density vs power-saving) with what would be required at *every* N.
- Relevant rigorous results on exponential sums over primes, large sieve/Bombieri–Vinogradov, minor-arc L² or L⁴ estimates; check whether the precise one-target weighted signed correlation sought in M2/M3 is available or not.
- Linnik's least-prime theorem and the precise way Stage 62.4 uses it; distinguish a non-effective generic Dirichlet existence statement from a polynomial least-prime bound.
- Recent arXiv/MathSciNet/zbMATH results only when independently verifiable and actually about the required binary, pointwise, target-specific problem.

Build a **formal implication matrix**: theorem, exact quoted/rederived hypothesis, quantifier structure, range, excluded primes, effective constants, averaged vs pointwise nature, and whether it genuinely supplies the target inequality. Never replace a sum over almost all even N by a statement about all \(N\in H\). No unsupported claim of a new published Goldbach solution.

**Deliverables:** \`04_literature_and_implications.md\` and a JSON bibliography ledger with DOI/URL/publication dates/preprint-vs-reviewed status. Commit/push checkpoint.

## M5 — Attempt ONE genuinely new independent analytic inequality, adversarially

Select the strongest non-circular candidate from M1–M4. Prefer an *intermediate lemma not equivalent to the target conclusion*; write the proposed lemma before searching for evidence. Exact domains, all signs, constants and uniformity must be explicit.

Possible candidates, only if logically useful:
- A signed comparison of the target-anchored shared-prime triple correlations and four-distinct terms with an independently controlled major-arc integral;
- A novel admissible-local-factor decomposition plus a **proved** gain over candidate-count upper bounds that survives the sieve parity barrier, not a wheel count alone;
- A target-specific error bound under a *genuinely weaker and independently verified* distribution hypothesis (possibly conditional), with a precise implication to R(N)>0;
- A rigorous incompatibility theorem for a family of deterministic moment certificates on the full singular-series model (clear as model-only, not as actual R).

For the selected attempt:
1. Prove basic lemmas exactly.
2. Search for hidden circularity and false equivalences, especially any assumed lower bound proportional to \(R(N)\) or an anchored correlation whose positivity already implies R(N)>0.
3. Try at least one distinct derivation (not merely a rewritten identity).
4. Challenge every inequality with integer/rational abstract countermodels and targeted genuine-prime examples where meaningful.
5. Compare constants and hypotheses against published estimates.
6. If blocked, identify the *first missing theorem*, its precise statement and smallest nontrivial special case; do not claim it was proved.
7. If unexpectedly solved, require a completely written universal proof, a separate critic-audit attempting to disprove it, complete small-prime exceptions, and no public “Goldbach proved” headline without independent scholarly review.

**Deliverables:** \`05_primary_analytic_attempt.md\`, \`05_countermodels.py\`, \`05_proof_obligation.json\`, and an unambiguous verdict of PROVED / CONDITIONAL / REFUTED / OPEN. Commit/push checkpoint.

## M6 — Independent final audit and publication for user return

Produce one integrated, readable mathematical report and ensure all prior hypotheses and results retain their correct labels.

Required artifacts:
- \`results/stage63/final_report.md\` — research narrative organized by the real proof obligations, not by speculative milestones.
- \`results/stage63/theorems_and_dependencies.md\` — numbered lemmas with hypotheses and proof links, including exactly what is external literature.
- \`results/stage63/failed_approaches.md\` — counterexamples, first invalid implications, and lessons learned; never delete failed work.
- \`results/stage63/next_objective.md\` — best precise unsolved estimate and an executable Stage 64 research task, if appropriate.
- Exact test programs, reference datasets, independent verifier, manifest of parameters, versions and SHA-256 of saved deliverables.
- \`results/stage63/checkpoint_log.md\` — each milestone's commit SHA, results, verified scripts, remaining work and resource usage.
- A short \`results/stage63/return_brief_es.md\` written in **Spanish only if the repository's English-only convention is explicitly waived**; by default instead write \`return_brief.md\` **in English**, explaining in simple prose what was genuinely proved and what remains open.
- The repository's authoritative \`tasks/NEXT_TASK.md\` updated to the *new and verified* next objective **on this branch only**, not \`main\`.

Final review:
- Independent proof pass by a distinct algorithmic path and adversarial check of any nontrivial analytic novelty;
- Exact arithmetic for deterministic tests and congruences (not floating-point primality);
- Include boundary \(N=4,6,8\), p=q diagonal, 2,3,5,7; verify every finite range and quantifier;
- Re-run the full relevant test suite and record commands/output;
- \`git diff --check\`, clean tree, intended file list, provenance graph and source hashes;
- Push the Stage 63 branch and open a **draft PR** against Stage 62 if possible. If private PR API is inaccessible, give the GitHub comparison URL and do not treat PR creation as mandatory for publication.

### Execution continuity and safety

- Do not pause after M0/M1/M2 unless a real blocker makes safe progress impossible; continue sequentially through the remaining milestones.
- Do not ask for permission for normal writing, running existing tools, checking literature or creating ordinary commits on the Stage 63 branch: those are authorized. Do request approval (and stop only the relevant action) for **any** paid resource, software installation, credential change, destructive Git operation, privacy exposure, public disclosure, or merge into main.
- Checkpoints are essential: commit and push distinct milestones while the agent is active so progress survives context compaction/session loss or a CoCalc idle stop.
- If SSH fails, use the dedicated identity explicitly with \`IdentitiesOnly=yes\`, do not output private key material, and continue locally if read-only sources remain sufficient; record the block.
- No \`git push --force\`, no reset/rebase on existing work, no silent edits of Stage 56–62. No new parallel worker agents without a clear reason; do not multiply usage expense merely to look busy.
- Avoid lengthy unfocused brute force. Use focused tests for a theorem, with a recorded purpose and explicit bound; if the proposed statement fails, stop that experiment promptly and document it.
- Respect the project's resource and subscription limits. Before a heavier computation, estimate time/memory and arrange checkpointed chunks; never assume a process survives logout or a runtime idle timeout.
- If a CoCalc Goal is active, continue automatically through the milestones while authorization/allowance is available; at the end, report deliverables and **finish** the goal rather than restarting an infinite loop.
- Preserve the original statement as the investigation target but do not claim an independent conjecture equivalent to Goldbach has been proved by checking only N<=some finite bound.

## Completion acceptance criteria

Success is **not** a required Goldbach proof. A substantive outcome can be:
- a new fully proved modular/shared-prime lemma with precise exceptional cases;
- a demonstrably new independent analytic bound for genuine primes;
- a rigorous model-level no-go theorem that eliminates an unproductive local-certificate strategy;
- a precise audited conditional theorem with independent external assumptions and quantified error, plus a proof-gap matrix;
- a reproducible negative result that rules out a tempting but false universal inequality.

A report that merely reprints the already known moment identity, increases finite prime-count ranges, or labels an unproved uniform estimate “established” **does not satisfy this task**.

**End of extended unattended program.**
