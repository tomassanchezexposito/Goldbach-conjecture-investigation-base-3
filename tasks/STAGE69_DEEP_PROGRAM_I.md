# STAGE 69 — DEEP RESEARCH DIRECTIVE, PART I
## Mathematical audit, source-to-claim discipline, and the first genuinely prime-specific reductions

**Research mandate:** substantially deepen mathematical inference, not numerical workload or prose volume. This program consists of **Part I** (this document) and **Part II** (\`tasks/STAGE69_DEEP_PROGRAM_II.md\`), with a pre-audited mandatory erratum in \`results/stage69/00_erratum_psd_lifting.md\`. Both parts are binding, sequential work instructions. Read \`tasks/NEXT_TASK.md\` for startup and publication requirements.

**Status:** no proof of \(\forall N\in H:R(N)>0\) or binary Goldbach is known in the project. Every mathematical result must be separately labeled PROVED HERE, ESTABLISHED EXTERNAL THEOREM, CONDITIONAL PROPOSITION, FINITE EXACT CHECK, REFUTED, or OPEN.

### General evidence contract

A lemma is not complete merely when its algebra looks plausible. Record all domains and quantifiers. Distinguish:
1. a purely formal identity, true for any coefficient sequence;
2. a sharp extremal theorem in an unrestricted Hilbert/PSD space;
3. an identity true because coefficients are supported on **genuine primes**;
4. a statement true only if a cited external theorem with its full assumptions is accepted;
5. a heuristic derived from a singular series or sieve survivors;
6. a proved statement that *actually* implies positive representation for every target.

A result that is a true reparametrization, an abstract no-go lemma, or a conditional implication is worth retaining **when** it eliminates an invalid inference or identifies the smallest missing theorem. It is never to be reported as a breakthrough in the Goldbach conjecture unless a new prime-specific existence estimate is proved. In every section include a section **"Potential circularity and first missing arithmetic fact"**.

Do not ask the absent user to approve ordinary research, documentation, running preinstalled tools, or checkpoint commits. Continue as long as the CoCalc active Goal and membership allow, without promising uninterrupted operation. No extra fees, package installs, privilege changes, secret exposure, force push, destructive Git, merge to main, or public preprint submission are authorized.

### Common notation (immutable for this stage)

Let
\[
H=\{N\ge4:N\equiv0\pmod 2,\ N-1\text{ composite},\ N/2\text{ composite}\},
\quad
R(N)=\#\{p<q:\ p,q\text{ genuine primes},\ p+q=N\}.
\]
Original cases for every even \(N>2\): \(N=p+1\), \(N=2p\), or \(N=p+q\) for distinct primes \(p<q\). The claimed equidistance \(N-2p=2q-N\) follows algebraically from \(p+q=N\) and is **not** a primality theorem. When using odd-prime base-position variables \(p=3+2a,\ q=3+2b\), the exact target condition is \(a+b=N/2-3\); the prime 3 is \(a=0\). Do not confuse these with base-3 digits, residue class modulo 3, or progression difference 3.

For a smooth real nonnegative compactly supported weight \(w\), define
\[
S_w(\alpha)=\sum_{p\ {\rm prime}}(\log p)w(p/X)e(p\alpha),
\quad e(t)=e^{2\pi it},
\]
\[
r_w(N)=\int_{\mathbb T}S_w(\alpha)^2 e(-N\alpha)d\alpha,\quad
a_w(N)=\int_{\mathfrak M}S_w(\alpha)^2 e(-N\alpha)d\alpha,\quad
m_w(N)=\int_{\mathfrak m}S_w(\alpha)^2 e(-N\alpha)d\alpha.
\]
The full sum coefficient \(r_w(N)\) is a nonnegative weighted *ordered* count of prime pairs when \(w\ge0\). It is positive only if there is a prime-pair representation within the weight support; on H the pair must be distinct. If \(R(N)=0\), then \(r_w(N)=0\) for all such weights; the reverse implication need not hold due to the support restriction.

For \(j\in\mathbb Z\) set
\[
\Delta_j(N)=m_w(N+j)-m_w(N)
=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)(e(-j\alpha)-1)d\alpha.
\]
Use even \(j=2h\) for parity-preserving target shifts. **Never substitute \(|S_w|^2\) for \(S_w^2\)**: that changes sums into differences. Parseval still involves \(|S_w|^4\).

The inherited conditional 2026 scale (subject to the exact smooth-weight/zero-free hypotheses of the source theorem) is
\[
B_X=\int_{\mathfrak m}|S_w|^4\ll X^{5/2}(\log X)^{100},
\]
while \(a_w(N)\ge A_X\asymp X\) on the applicable interval only if the independently justified major-arc estimate and its full conditions hold. Do not assume \(B_X\) and \(A_X\) have known numerical values from big-O statements.

---

## M0 — HIGH-PRIORITY ERRATUM AND INDEPENDENT CERTIFICATION

**Problem:** The Stage 68 paper repeatedly claimed the two-projector example
\[
G_1=\operatorname{diag}(1,0),\ G_2=\operatorname{diag}(0,1),\ B_1=B_2=1
\]
gave rank-one optimum \(\sqrt2\) and semidefinite relaxed optimum \(2\). This is **false**. Both optima are \(\sqrt2\). The value \(2\) is only the separate triangle spectral bound. The inherited symbolic regression did not optimize the lifted variable; it tested a tautological arithmetic statement.

**Required proof work:**

M0a. Independently re-derive all three quantities: exact rank-one optimum, exact trace-one positive-semidefinite optimum, and exact triangle upper bound. State the first invalid equation in the predecessor, not merely "the example should change". Check all inherited reports that mistakenly repeat the claim: \`02_exact_budget_optimization.md\`, \`08_adversarial_review.md\`, \`final_report.md\`, their machine-readable proof labels and any verification log. Preserve predecessor history and write a Stage 69 erratum referring explicitly to the old paths.

M0b. Independently verify or refute the six-Pauli-projector strict gap in \`results/stage69/00_erratum_psd_lifting.md\`. Prove each projector PSD and rank one, the mixed optimum \(3\sqrt2\), and pure optimum \(3\sqrt{1+\sqrt{2/3}}\). Do not cite a qubit Bloch-sphere formula without deriving it from a unit \(z=(z_1,z_2)\): \(r_x=2\Re(\bar z_1z_2)\), \(r_y=2\Im(\bar z_1z_2)\), \(r_z=|z_1|^2-|z_2|^2\), then \(r_x^2+r_y^2+r_z^2=1\). Show every unit \(r\) arises from such \(z\). Prove \(f(t)=\sqrt{1+\sqrt{1-t}}\) is concave; give the equality case. A tiny exact symbolic check is appropriate but is not the proof.

M0c. Audit the second "two interval" Gram matrices in Stage 68 independently. Noncommutativity of real symmetric \(2\times2\) matrices with simple spectra rules out a common eigenvector, proving **strictness of the triangle bound**, but not automatically an SDP-lifting gap. Record that the strict triangle example is valid while the SDP example was false. Test if special interval Gram families could actually exhibit rank-one/PSD gaps; if not proved, leave the statement OPEN.

M0d. Update the independent audit philosophy: any optimization example must distinguish \(\sup_{\|z\|=1}\), \(\sup_{X\succeq0,\operatorname{tr}X=1}\), \(\sum_r\sqrt{B_r\lambda_{\max}(G_r)}\), and the best valid Cauchy/dual upper certificate. Numerical matrix eigenvalues alone cannot show which nonlinear optimization was solved.

**Acceptance M0:** a formal correction with all statements and original source locations; two logically distinct proofs; a tiny exact reproducible regression testing **three** quantities; no unverified use of the flawed predecessor result. Commit/push this checkpoint before M1.

---

## M1 — RECONSTRUCT THE PRIME-SPECIFIC PROBLEM FROM SCRATCH

The previous work is strongest in unrestricted functional analysis. Now examine whether the **special convolution** \(S_w^2\) affords strictly stronger information. Start not with a new inequality, but with exact integral and integer identities.

M1a. Define the ordered prime-pair coefficient \(r_w(N)\) and distinct unordered count \(R(N)\); write precise conversions, noting the nonuniform factors \((\log p)(\log q)w(p/X)w(q/X)\). For even \(N\in H\), \(N/2\) composite makes the prime diagonal vanish. For even \(N>4\), 2 is never a summand, and \(p=3\) must be treated, not discarded. Do **not** replace \(r_w(N)\) by a fixed multiple of \(R(N)\) without explicit lower/upper bounds on nonzero weights.

M1b. Prove an exact prime-only Fourier relation with a compactly supported smooth weight; then derive the correction when replacing the genuine-prime polynomial by the von Mangoldt polynomial \(\sum_{n\le X}\Lambda(n)e(n\alpha)\). Count prime powers, diagonal p=q and order multiplicities separately. State an explicit deterministic upper bound on the prime-power correction with all constants (or derive a meaningful improved bound), using only rigorous elementary estimates. Check whether the correction is small *relative to the claimed major term uniformly at N* under the actual hypotheses. Do not claim a pointwise power-saving because the total correction is small on average.

M1c. Write the exact fourth-moment identity in two ways:
\[
\int_{\mathbb T}|S_w(\alpha)|^4\,d\alpha
=\sum_t\left|\sum_{p+q=t}a_pa_q\right|^2
=\sum_{\substack{p_1+p_2=p_3+p_4}}a_{p_1}a_{p_2}a_{p_3}a_{p_4},
\]
where \(a_p=(\log p)w(p/X)\ge0\). Give the correct ordering and diagonal/multiplicity classification for unordered distinct representations, same target, and cross targets. Identify precisely which terms are truly 4-distinct, which share one prime, and why two distinct same-target unordered pairs **cannot** share exactly one prime. Clarify that fourth moment on the **minor arcs** is **not** a simple nonnegative sum of these integer configurations because the indicator \(1_{\mathfrak m}\) introduces signed Fourier coefficients.

M1d. Build an exact dependency graph separating:
- global nonnegative additive energy;
- smoothed prime representation coefficients;
- restricted, generally signed minor-arc coefficients;
- local modulus and Gram geometric inputs;
- actual Goldbach representations at the prescribed N.

Mark every point where arbitrary-L2 extremizers fail to have the prime-square form. Derive whether any prime polynomial constraint has *known proven content* strong enough to exclude the exceptional "spike" abstract model. Avoid saying "the prime coefficients cannot spike" without a proof.

M1e. Investigate the half-period odd-prime symmetry \(S_w(\alpha+1/2)=-S_w(\alpha)\) only when 2 is absent from support. Determine the *exact* condition on X and w that excludes p=2; do not assume \(\operatorname{supp}w\subset[1/8,7/8]\) unless the source actually specifies that. Show the full square has only even Fourier frequencies; for restricted major/minor sets that fail translation invariance by 1/2, identify the defect term explicitly. If a symmetry cancellation survives after pairing reflected pieces, prove it and quantify what it buys at a fixed target.

M1f. Independently derive the base-position convolution \(p=3+2a\), \(q=3+2b\), \(a+b=N/2-3\). Express it as an *exact weighted convolution of the primality indicator along a one-dimensional position index*, with p=3 retained. Does this reveal a new nontrivial additive energy identity, or merely a change of variables? Compare convolution autocorrelation and Fourier transforms in this index with the usual odd-supported prime polynomial; identify all phase and cutoff changes.

**Acceptance M1:** at least two independently derived exact prime-only structural formulae, complete edge-case accounting, a proof-dependency diagram and explicit separation of what is *new arithmetic control* versus mere reparametrization. Deliver \`results/stage69/01_prime_specific_exact_convolution.md\`. Do not award a "prime-theoretic advance" solely for rewriting a known convolution.

---

## M2 — HARD LOGICAL NO-GO STUDY: WHAT DOES GLOBAL FOURTH MOMENT REALLY EXCLUDE?

Formalize an *information hierarchy* instead of repeating one abstract singleton.

Define a family of increasingly restricted coefficient classes:
\[
\mathcal C_0=\{c\in\ell^2:\ \|c\|_2^2\le B\},
\]
\[
\mathcal C_1=\{c=\widehat{\mathbf1_{\mathfrak m}F}:\ \|F\|_2^2\le B\},
\]
\[
\mathcal C_2=\{c=\widehat{\mathbf1_{\mathfrak m}S^2}:\ S\text{ finite trigonometric polynomial with }a_n\ge0\},
\]
\[
\mathcal C_3=\{c=\widehat{\mathbf1_{\mathfrak m}S_w^2}:\ S_w\text{ uses all actual primes in the specified weighted support}\}.
\]
Define these sets carefully (as written \(\mathcal C_2,\mathcal C_3\) must **also** inherit the energy bound and the same frequency/weight parameters to be nested). Investigate which containments hold, which require a fixed support interval, and which differ due to the minor-arc indicator. Do not assert strictness without a witness.

M2a. Find the **sharpest universal coefficient bound** obtainable solely from the global fourth moment and the full-circle major/minor decomposition. Derive it via direct Cauchy, reproducing kernels, Parseval, duality and an exact phase extremizer. State whether the extremizer obeys the Fourier support, reality and conjugate symmetry of the actual coefficient. If the exact extremizer is impossible for a prime polynomial, **identify a proved quantitative distance** or admit that no such distance is known.

M2b. Analyze whether restricting \(F=S^2\), with S having **nonnegative Fourier coefficients**, rules out a strongly negative fixed minor coefficient. Construct a small analytic trigonometric polynomial with positive coefficients and a target outside its sumset, then choose a symmetric measurable major set where the restricted coefficient is positive, forcing a negative minor coefficient. Clarify why this is an abstract positive-spectrum counterexample rather than a statement about the set of all primes.

M2c. Test whether global additive-energy information together with exact parity/CRT residues and \(\mathfrak S(N)>0\) can force a target coefficient. Attempt a countermodel meeting **all actually stated** abstract constraints. If the proposed model is not realizable as a true-prime polynomial, make that limitation explicit; if it violates a necessary Fourier positivity or support constraint, reject it rather than counting it as a counterexample.

M2d. Prove or refute a **localization impossibility lemma for a specified class of multipliers**. Delimit the class by operator norms, sign symmetry, support and permitted target dependence. An unrestricted "no Fourier method can work" is unacceptable: only prove an information-theoretic no-go under a precisely named set of estimates. Show why a result from the 2026 literature adds or fails to add independent information beyond that class.

M2e. Quantify the distinction between:
\[
\sum_{N\in[X/2,X]}|m_w(N)|^2\ll X^{5/2}(\log X)^{100}
\quad\text{and}\quad
\sup_{N\in H\cap[X/2,X]}|m_w(N)|=o(X).
\]
Spell out the exact loss \(X^{1/4}(\log X)^{50}\) in the ordinary pointwise *amplitude* bound relative to an \(X\)-scale major term, and the \(X^{1/2}(\log X)^{100}\) loss in **squared energies**. Do not mix amplitude and squared energy exponents. A numerical big-O constant is not supplied by a scale exponent.

M2f. Propose the smallest **additional prime-only distribution hypothesis** that excludes the abstract extremizer without already asserting \(r_w(N)>0\). Compare candidates: normalized short-shift regularity, local block energy, signed rational-arc phase cancellation, and a bilinear prime-correlation inequality. For each condition write a logically sufficient quantified theorem and a formal countermodel showing why strictly weaker prior conditions fail.

**Acceptance M2:** a carefully quantified information-poset/no-go theorem, explicit strengths and weaknesses, at least one serious attempted strengthening of the abstract model, and the first missing prime-specific input. Deliver \`02_information_hierarchy_and_no_go.md\`, with proofs or precisely marked open cases. Use small symbolic examples, **not** growing prime sweeps.

---

## M3 — CORE ANALYTIC ATTEMPT I: MAJOR/MINOR ARCS WITH THE FIXED TARGET PHASE RETAINED

The Stage 68 arc-allocation formulas were sharp for **unrestricted \(L^2\)** functions and intentionally discarded the arithmetic phase. This task is to retain the phase \(e(-N\alpha)\) wherever possible and prove at least one nontrivial result or identify a genuinely narrower obstruction.

M3a. Define a measurable disjoint partition of the complete minor set \(\mathfrak m\) with target-compatible symmetry. Every piece must have explicit endpoints or a measurable allocation rule, including ties, overlapping rational cores, reflected \(\alpha\mapsto-\alpha\) images, and every unassigned remainder. Distinguish denominator-resolved and dyadic-distance-resolved partitions. If a partition depends on N or h, disclose that dependence; don't silently invoke a source theorem for an N-dependent partition when only an N-independent one was proved.

M3b. For each piece derive
\[
I_E(N)=\int_E S_w(\alpha)^2e(-N\alpha)d\alpha,\qquad
\Delta_{E,j}(N)=\int_E S_w(\alpha)^2e(-N\alpha)(e(-j\alpha)-1)d\alpha.
\]
Provide two calculations: one in frequency space using a convolution of the Fourier transform of \(1_E\) with the nonnegative prime-pair coefficient sequence; one directly via the circle-method exponential integral. Locate the *signed* information that is destroyed by replacing every \(I_E\) with \(|I_E|\) and then using Cauchy–Schwarz.

M3c. Derive a **dual phase-alignment certificate** with explicit admissible test functions \(\psi_E\). State the theorem: if independently established signed bounds on \(\Re I_E(N)\) (or correlations among pieces) guarantee \(\sum_E\Re I_E(N)>-a_w(N)\), then positivity follows. Decide whether the hypothesis is merely a dressed-up restatement of the desired positivity. To count as useful it must have a structural property **proven from true-prime distribution**, not introduced as an assumption naming the negative coefficient.

M3d. Revisit \(\mathfrak M\) as in Li–Liu with denominator \(q\le P=X^\kappa\) and radius \(P/(qX)\), where actual paper conditions include \(\Theta\), \(w\), and \(\kappa\). Analyze rational resonance \(q\mid2h\) and the off-resonant arcs, and prove why controlling just the resonant pieces cannot establish the full signed sum. If a complete dyadic partition produces a nontrivial inequality, record the exact \(X,q,h,N\)-dependent operator constants; compare them directly to the Stage 66 strict threshold.

M3e. Work out how a **localized prime fourth moment** would have to scale on each region to close the gap. Do not merely label \(B_{q,s}\): choose a proposed dependence on \(X,q,s,\Theta,w\), derive its sum, and prove the target signed bound implied (or show it is still inadequate). Explicitly compare the hypothesis to the inherited global fourth-moment theorem. Distinguish "individually bounded arcs" from the possibility that the available moment may concentrate on a small number of bad arcs.

M3f. Investigate **bilinear rather than absolute-value estimates**. Can signed products of Type I and Type II sums, or a dispersion identity, retain enough cancellation at one N? Write the exact form before estimating it. Cite Vaughan/Heath-Brown identity or other classical prime decompositions only when the relevant equality is actually checked. If the first step applies absolute values and loses the target twist, identify that loss quantitatively and test an alternative.

M3g. At the end of this theme, choose one serious analytic candidate with a written theorem statement:
\[
\forall X\ge X_0\ \forall N\in H\cap[X/2,X],\quad
\text{signed prime-weight integral}\ \le\ \text{explicit bound}.
\]
Write all parameters: \(w,\Theta,\kappa,q,j\), effective or ineffective constants, residue exceptions, and smooth support. Prove everything *up to* the first missing prime-specific lemma, or complete the proof if genuinely possible. Under no circumstances label that lemma "known" without a direct exact citation.

**Acceptance M3:** a complete phase-preserving analytic reduction with two independent viewpoints, an explicit threshold inequality, and at least one deeply attempted prime-only bound. Deliver \`03_target_phase_and_arc_decomposition.md\` and \`03_signed_analytic_candidate.md\`.

---

## M4 — CORE ANALYTIC ATTEMPT II: ARITHMETIC PROGRESSIONS, SIEVES, AND TARGET-ANCHORED CORRELATIONS

This is a separate mathematical route, **not** a rewording of M3. It must use the arithmetic of the reflection \(p\mapsto N-p\) and the constraints on N in H.

M4a. Starting from exact \(R(N)\) and the positional variables \(a+b=N/2-3\), derive local necessary residue conditions for a candidate pair \(p,N-p\) to avoid each small prime \(\ell\), with exact exceptional case \(p=\ell\) or \(N-p=\ell\). Build the general CRT local-factor formula for any squarefree modulus \(W\). Explain rigorously why a positive local factor does not give a prime pair. Recover wheel 210 as a special case without modifying earlier definitions. If the factorization \(N-1\) or \(N/2\) composite adds a **new proven restriction**, state it; do not assert one based only on experimental patterns.

M4b. Compare the **full** Hardy–Littlewood Goldbach singular series to finite wheel normalization. Use the actual Stage 62 theorem that on infinitely many N in H one may have \(A_{210}(N)=A_{210}(N+2)=15\) yet arbitrarily different singular-series arithmetic factors. Audit whether a proposed local-smoothness hypothesis contradicts this **arithmetic model**; do not claim the same divergence for actual R(N) without a proven pointwise asymptotic. This prevents rebuilding a refuted universal baseline.

M4c. Analyze the parity barrier for a sieve that tests both \(p\) and \(N-p\). What does a two-dimensional elementary/linear/large sieve actually upper-bound? Explicitly determine whether a lower bound for surviving numbers after a sieve is enough to force simultaneous primality, or whether large composite survivors remain. Compare with Chen's prime + \(P_2\) theorem, stating why it is not identical to two primes. Use exact sieve dimension and remainder estimates where source proofs are accessible; do not invent a primality conclusion from an admissible sieve tuple.

M4d. Study prime distribution in arithmetic progressions in a *target-anchored* manner. For a fixed modulus q, Dirichlet guarantees infinitely many primes in a reduced class **over unbounded values**. Bombieri–Vinogradov averages errors over moduli but does not supply simultaneous primality at a prescribed complementary pair. Distinguish \(\sum_{q\le Q}\max_{(a,q)=1}|\pi(x;q,a)-\mathrm{Li}(x)/\varphi(q)|\) from a correlation \(\sum_p1_{\mathbb P}(p)1_{\mathbb P}(N-p)\). Formulate one exact correlation/distribution statement that would bridge the gap, and investigate whether it is strictly weaker than the full assertion of Goldbach.

M4e. Recover the exact shared-prime and four-distinct correlations \(S(u,v),Q_4(u,v)\) for shifted targets. Establish their relationship, if any, to prime AP distributions and four-fold additive energies, but **never** choose a representation at the target whose existence is under test. A positive anchored \(Q_4(N,M)\) already implies \(R(N)>0\); that is a valid criterion only if its lower bound is proved **independently** of the desired pair. Challenge any such proposed lower bound against abstract one-hole count vectors.

M4f. Investigate whether the structural condition \(N-1\) composite, \(N/2\) composite could exclude some exceptional Goldbach target by a genuine theorem, rather than by density heuristics. Produce a rigorous comparison of exceptional sets: the original three-case failure set is a subset of the binary Goldbach exceptional set, but known upper bounds of the form \(O(X^\delta)\) for \(\delta>0\) may still contain any given isolated member of H. If there is a source-level theorem specifically excluding exceptions under those two compositeness conditions, identify precisely its hypotheses; otherwise state the unproved necessity of such a result.

**Acceptance M4:** a separate genuine arithmetic investigation, at least one candidate nontrivial statement with actual proof progress, a source-accurate sieve parity barrier analysis, and a quantified bridge lemma or proved obstruction. Deliver \`04_residual_arithmetic_and_sieve_barrier.md\` and \`04_anchor_correlation_ledger.md\`.

**PART I STOP CONDITION:** This document alone is NOT the entire assignment. After completing and committing M0–M4, **continue automatically to \`tasks/STAGE69_DEEP_PROGRAM_II.md\`** through the remaining milestones and final synthesis. Do not report the task finished after Part I.
