# Stage 69 M9 — Mathematical synthesis, dependency closure, and next objective

**Review date:** 2026-11-10.  
**Research base:** \`cocalc/stage69-deep-prime-specific-localization\`, descending from Stages 63–68.  
**Research status:** COMPLETE *as a documented internal M0–M9 review*, **not** a universal number-theory proof, independently refereed publication, completed Lean verification, or validation of all cited external papers. The CoCalc source produced M0–M7; M8 and M9 were completed by ChatGPT's separate GitHub-connected review, with their provenance explicitly identified.

## I. Exact problem preserved

The original three-case claim is: every even \(N>2\) is either \(p+1\) for a genuine prime \(p\), or \(2p\) for a genuine prime \(p\), or \(p+q\) for distinct genuine primes \(p<q\). In the third case the reflection equality \(N-2p=2q-N\) is algebraically equivalent to the sum. On
\[
H=\{N\ge4:\ N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\}
\]
the first two alternatives fail; the open claim is
\[
\forall N\in H,\qquad R(N)=\#\{p<q:\ p,q\text{ prime},\ p+q=N\}>0.
\]
The odd-prime position parameterization \(p=3+2a\) is a *position coordinate*, not ternary digits or an independent primality test. For even \(N>4\), prime 2 cannot occur as a summand, and \(p=q\) is excluded on H.

## II. Theorems demonstrated in the local mathematical program

**T69.1 (abstract PSD correction).** The vectors \(\operatorname{diag}(1,0),\operatorname{diag}(0,1)\) have both pure and trace-one positive-semidefinite lifted optimum \(\sqrt2\); 2 is merely a termwise spectral/triangle upper bound. An abstract six-Pauli-projector family **does** have a strict lift gap between \(3\sqrt{1+\sqrt{2/3}}\) and \(3\sqrt2\). The mathematical correction is independently written and audited in \`00_erratum_psd_lifting.md\` and \`00_independent_psd_erratum_audit.md\`. These matrix statements imply nothing about actual prime-pair counts.

**T69.2 (exact prime convolution).** For any finitely supported real nonnegative prime weights \(a_p\) and \(S(\alpha)=\sum_pa_pe(p\alpha)\),
\[
r(n)=\int_0^1S(\alpha)^2e(-n\alpha)d\alpha=\sum_{p+q=n}a_pa_q.
\]
The weighted count is ordered, distinct prime pairs contribute twice, and the diagonal must be handled separately outside H. For \(p=3+2a\), the same coefficient is an exact affine re-indexing. The full-circle fourth moment is
\[
\int_0^1|S|^4=\sum_n r(n)^2;
\]
the shifted fourth moment at frequency j is \(\sum_n r(n+j)r(n)\). These identities were independently cross-checked for exact integer test weights in M8. **They do not prove any \(r(N)>0\).**

**T69.3 (sharp information-class obstruction).** The M2 inclusions from unrestricted \(\ell^2\) coefficient vectors to restricted \(L^2\), nonnegative-frequency polynomial squares and the single actual prime polynomial hold with the specified nondegeneracy conditions. For a major/minor partition of measures \(\nu,\mu>0\), arbitrary \(F\in L^2(\mathbb T)\) with prescribed major coefficient a and missing full coefficient requires full-circle energy at least
\[
\|F\|_2^2\ge |a|^2\left(\frac1\mu+\frac1\nu\right)=\frac{|a|^2}{\mu\nu}.
\]
The arbitrary \(L^2\) extremizer is generally outside the finite prime-polynomial class. This is a sharp *functional-analytic* no-go theorem for proofs using only the specified norm/coefficient inputs. Its full-circle energy \(B\) cannot be replaced by a **minor-only** fourth-moment estimate.

**T69.4 (exact energy-vs-budget theorem).** For any \(c\in\ell^2(\mathbb Z;\mathbb C)\), a center amplitude \(|c(N)|\ge A>0\), and \(m\) distinct nonzero shifts with exact squared increment energy V,
\[
\|c\|_2^2\ge A^2+m\left(A-\sqrt{V/m}\right)_+^2.
\]
The exact fixed-V extremal energy is
\[
\begin{cases}
 A^2+(\sqrt V-\sqrt mA)^2,&0\le V\le A^2(m+1)^2/m,\\
 V/(m+1),&V\ge A^2(m+1)^2/m.
\end{cases}
\]
If only an upper bound \(V\le\bar V\) is known, the weaker displayed lower bound with \(V=\bar V\) is **sharp for every \(\bar V\)**, because the extremizer may use actual V smaller than its budget. Boundary equality does **not** exclude the hypothetical missing target. M6 proves both regimes; M8 independently checked 252 exact rational cases.

**T69.5 (exact target-vs-global correlation classification).** On distinct even residual targets, products \(r(N)r(N+j)\) decompose into four-distinct prime configurations and shared-one-prime configurations, with the proper fourfold orientation multiplicity. Same-target distinct representations cannot share exactly one prime. Global shifted fourth-moment Fourier coefficients average over *all* targets, not a prescribed N. A positive anchored four-prime correlation at N cannot be proved by choosing an existing representation at N; that would assume the conclusion.

## III. Refuted claims and corrected source language

1. **Stage 68 false numerical SDP-lift claim:** definitively corrected in M0. The separate strict *triangle* inequality for two genuine interval Grams was not refuted.
2. **Stage 69 M3 "minor arcs imply relevant denominator \(q>P\)" phrasing:** requires a stated approximation convention. The counterexample \(P=13,X=2000,\alpha=1013/3000\) lies outside all the q≤13 major cores while its nearest reduced small-denominator center is \(1/3\). Corrected precisely in \`08_adversarial_review.md\`. The Fourier resonance identity remains valid.
3. **Nonnegative Fourier coefficients force nonnegative restricted-minor coefficients:** false. A sparse positive prime-frequency polynomial can have a negative complementary signed integral for a target outside its support. This is an abstract positive-spectrum countermodel, **not** one built from all primes of the prescribed weight support.
4. **A bounded sum of CRT/wheel survivors guarantees a genuine prime pair:** false as a logical implication. The local factors give necessary modular compatibility, not simultaneous primality.
5. **A global fourth moment or exceptional-set upper bound forbids one isolated exception:** false. Even an \(O(X^{1/2}\log^{100}X)\) exceptional-set bound permits a singleton.
6. **An exact Fourier identity or a positive abstract Gram norm implies a signed saving:** false unless an independent prime-specific phase estimate is established.

## IV. Two independent but still incomplete routes

**Route A (circle method, signed coefficient).** For a fixed positive smooth prime weight, \(\mathfrak M\sqcup\mathfrak m=\mathbb T\), and \(r_w(N)=a_w(N)+m_w(N)\), an independently justified major lower bound \(a_w(N)\ge c_0X>0\) plus a **uniform** signed minor estimate
\[
|m_w(N)|\le(c_0-\delta)X,\qquad \delta>0,
\]
would imply \(r_w(N)\ge\delta X>0\) on every residual N in the specified interval. **The required signed estimate is OPEN**, and its conclusion is already a strong uniform binary-Goldbach statement under the source's zero-free assumptions.

**Route B (arithmetic reflected indicators).** An independent strictly positive bound for
\[
\sum_{p+q=N}1_{\mathbb P}(p)1_{\mathbb P}(q)
\]
would establish R(N)>0 on H, while a uniform \(\gg N/(\log N)^2\) bound is a much stronger quantitative statement. Current modular compatibility and parity-limited sieve information do not yield it. A four-prime bound anchored by first selecting a pair at N is circular.

These two routes have distinct hypotheses and techniques; neither was proved in M7, and the status must not be promoted by an audit document.

## V. Quantitative source-to-target gap

Under the *specific externally assumed* common Dirichlet-L zero-real-part hypothesis and the fixed smooth weight/arc construction recorded in the Li–Liu preprint, the inherited major-arc scale is \(A_X\asymp X\) and the **upper bound** on the minor fourth moment is
\[
B_X\ll X^{5/2}(\log X)^{100}.
\]
Cauchy–Schwarz gives only
\[
|m_w(N)|\ll X^{5/4}(\log X)^{50},
\]
a factor of order \(X^{1/4}(\log X)^{50}\) larger than the required \(X\)-scale. In squared energy the ratio of the **available bound** to an \(X^2\) target threshold grows like \(X^{1/2}(\log X)^{100}\). These statements describe the sufficiency gap of the *known upper bounds*, not the actual unknown size of B or any lower bound on \(|m_w(N)|\).

The Stage 66/69 increment certificate can be strict only if \(\bar B<A_X^2+m(A_X-\sqrt{\bar V/m})_+^2\), with independently proved \(\bar B\) and \(\bar V\). The known Gram+global-moment upper bound for \(\bar V\) is too large. Merely splitting the minor arcs into pieces does not create new arithmetic information; Stage 68's operator allocation collapses to the original total bound when only a total budget is known.

**External-source status:** Li–Liu, Pintz–Althöfer and Althöfer–Chen–Perelli–Pintz are 2026 arXiv preprints and must retain their exact hypotheses, including any common zero-free assumption. Bhowmik–Grimmelt's *Analysis Mathematica* paper is published, but its explicit major-arc identity is not a pointwise proof of Goldbach. The 2026 7/8 zero-free formalization was **not independently built or certified in this review**. A source's claimed formal status is not a substitute for verifying the theorem and dependencies.

## VI. Review and computational provenance

The prior CoCalc run published M0–M7 and individual tests; the branch **did not contain M8/M9 or a final manifest** before this separate review. This GitHub-connected review added:

- \`08_adversarial_review.md\` — independent proof/dependency audit with explicit M3 erratum.
- \`09_final_synthesis.md\` — this stage-level synthesis.
- \`verify_m8_independent.py\` — focused standard-library exact regression, actually executed in a separate local Python 3.13.5 runtime (not through CoCalc).
- \`m8_independent_exact_results.json\` — results: seven selected residual targets, 21 shifted target pairings, 252 exact-energy cases, and the exact minor-arc approximation counterexample.
- The earlier \`weekly_pause_handoff.md\` remains as a **historical checkpoint** explaining why the first Stage 69 PR was incomplete. It is not the authoritative current completion status.

The reviewer independently checked the **arXiv abstract/version records** for the three October/November 2026 preprints. This is not a fresh line-by-line verification of their analytical proofs, and it does not make any claim of journal-level independent refereeing.

## VII. Research handoff: the narrow Stage 70 target

Do **not** start a fresh long Codex run just to repeat stages 63–69. The next worthwhile investigation should examine, at the one-target level, how much the exact **nonnegative prime-support polynomial-square** constraint can improve the unrestricted two-arc \(L^2\) extremizer (M2), or directly produce a *uniform phase-sensitive* minor-arc bound. More precisely:

1. Define the finite-frequency cone \(\mathcal P_X=\{S(\alpha)^2:S=\sum_{p\in\mathcal P_X^\mathrm{prime}}s_p e(p\alpha),\,s_p\ge0\}\) with a fixed, actual prime support set and a fixed positive smooth weight for the target theorem. Separate the variable-coefficient cone from the **single actual weighted prime polynomial**.
2. Derive a quantitative support-constrained one-target extremal problem for \(r_w(N)\), major coefficient a and the minor-energy budget. Do **not** assume positive \(r_w(N)\), and investigate whether a uniform strict improvement over arbitrary \(L^2\) is feasible for each N. Exact Fourier orthogonality is the starting point; positivity on the support must be exploited only where justified.
3. Seek an explicit **arithmetic** separation estimate for the *true fixed prime coefficients* from any one-hole extremizer with a nonvanishing margin \(cX\), or demonstrate a rigorous countermodel for an overly broad coefficient class. Proving only abstract finite-bandwidth strictness with a constant shrinking to zero as X grows is not enough.
4. Audit all source-conditioned constants and strictness conditions, with a fallback to the signed target-coefficient route if no useful gap survives.

**Next stage status: QUEUED, NOT STARTED.** No Codex process or automation is created by this document.

## VIII. Final decision

The M0–M9 *internal documentary review* is now closed and independently recorded. The valid theorems are exact algebraic and functional-analytic statements; computations are finite checks; imported moment bounds retain their conditions; the two main prime-specific analytic/arithmetic proof routes remain OPEN. The universal claim \(\forall N\in H:R(N)>0\) has **not** been proved or disproved.

There is no justified reason to declare the draft pull request ready for merger into \`main\` merely because this review is complete: scientific acceptance, further CoCalc replay and independent external peer review remain separate decisions.
