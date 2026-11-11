# Stage 71 — Integrated mathematical research report

**Date:** 2026-11-11. **Branch:** \`cocalc/stage71-sharp-deletion-sensitivity\`.  
**Method:** direct ChatGPT research, GitHub source audit and focused independent local exact tests. **No CoCalc/Codex usage.**  
**Universal conjecture:** the author's original three-case coverage on \(H=\{N\ge4:\ N\text{ even},\,N-1\text{ composite},\,N/2\text{ composite}\}\) is **OPEN**; no proof of \(R(N)>0\) for all N in H is claimed.

## 1. T71.1 — exact target erasure threshold and complete optimization curve (PROVED)

Fix a finite set P of genuine prime positions, nonnegative specified weights \(a_p\), and \(N\in H\). Active edges \(\{p,q\}\) satisfy p<q, p+q=N, a_pa_q>0. Because q=N−p is unique, the target incidence graph is a matching. Set \(A_i=\max(a_{p_i},a_{q_i})\), \(B_i=\min(a_{p_i},a_{q_i})\).

The exact least amount of coordinatewise downward \(\ell^1\) perturbation required to erase the target coefficient is
\[
\tau_N=\sum_i B_i.
\]
For every \(1\le s<\infty\), the exact \(\ell^s\) distance to the zero-target class is \((\sum_iB_i^s)^{1/s}\), and the \(\ell^\infty\) distance is \(\max_iB_i\). These formulas are obtained by hitting every disjoint edge at one endpoint.

A more detailed theorem solves the **entire partial-deletion problem**: sort the edges by decreasing A_i and allocate the allowed deleted mass greedily to the corresponding smaller endpoints, saturating B_i before proceeding. The ordered target coefficient decreases piecewise linearly with slopes \(-2A_i\); this is rigorously optimal by both concavity of the two-endpoint product and linear-programming duality. The exact algebra and endpoint quantifiers are in \`01_exact_target_robustness_and_lp.md\`.

**Precise limitation:** for all-prime unit weights, \(\tau_N=R(N)\). An independent theorem \(\tau_N>0\) for every target would be a Goldbach proof, so the exact formula is an optimization theorem, **not an independent prime-existence theorem**. For a compactly supported smooth weight, \(\tau_N=0\) can also occur when some actual prime pairs fall outside the support.

## 2. T71.1a — the exact target-sensitive perturbation identity (PROVED)

If \(d_p=a_p-b_p\ge0\) are removed weights, then
\[
r_a(N)-r_b(N)
=2\sum_{\{p,q\}\in\mathcal E_N}
(a_pd_q+a_qd_p-d_pd_q)
\le2\sum_pd_pa_{N-p}.
\]
The right side is a **reflected target interaction**: it depends on the complementary prime \(N-p\), not just on aggregate deleted weight. One loses this information upon passing to a generic global norm. The inequality is sharp to first order in a deletion from a small endpoint of an edge with a maximal-weight complement. The result is exact algebra, not a measured nonzero lower bound.

## 3. T71.2 — global Fourier near-invisibility of an erased target (PROVED using established PNT and Wu sieve)

Fix nonzero real \(w\ge0\) in \(C_c^\infty((0,1))\) and the actual complete weighted prime polynomial
\[
S_X(\alpha)=\sum_{p\ {\rm prime}}(\log p)w(p/X)e(p\alpha).
\]
For each sufficiently large X and every \(N\in H\cap[X/2,X]\), delete the smaller weighted endpoint of each target complement edge. The modified \(S'_{X,N}\) is supported on **a subset** of actual prime frequencies, has the **target coefficient zero** in its square, and deletes total weight at most \(O_w(X\log\log X/\log X)\). This last bound follows from the **unconditional upper** Goldbach sieve theorem of J. Wu (Acta Arith. 114(3), 2004, Theorem 1), plus \(N/\varphi(N)\ll\log\log N\).

The resulting polynomial is asymptotically close to the true full polynomial in every **fixed normalized global Fourier norm**:
\[
\frac{\|S_X-S'_{X,N}\|_q}{\|S_X\|_q}\to0
\qquad(2\le q\le\infty\text{ fixed}),
\]
and the **squares themselves** satisfy
\[
\boxed{
\frac{\|S_X^2-(S'_{X,N})^2\|_r}
{\|S_X^2\|_r}\to0
\quad\text{for every fixed }1\le r\le\infty,
\qquad [(S'_{X,N})^2]_N=0.}
\]
The convergence is **uniform in residual N in [X/2,X]**. For the important \(r=2\), the explicit relative rate is
\[
O_w\!\left(\frac{(\log\log X)^{3/4}}{\sqrt{\log X}}\right).
\]
The first-order polynomial has an \(L^2\) relative rate \(O_w(\sqrt{\log\log X/\log X})\) and a uniform norm relative rate \(O_w(\log\log X/\log X)\). Proof uses exact deleted \(\ell^1,\ell^2\) bounds, the classical weighted PNT, interpolation and Hölder. A second, independent \(L^4\) proof uses discrete convolution Young's inequality. None relies on an unverified 2026 zero-free claim.

**What this establishes:** even normalized global closeness of the *entire quadratic Fourier function* is insufficient, by itself, to force one prescribed coefficient to remain nonzero in the broadened class that permits sparse deletion of prime frequencies. It is **not** a counterexample to Goldbach: the actual full polynomial retains all real prime coefficients, whereas S' has been deliberately changed.

## 4. The precise still-missing estimate

The proof-relevant quantity at one target is the **absolute** coefficient \(r_w(N)\), naturally on an order-X scale when a Hardy–Littlewood main term is available. The full square polynomial has \(\|S_X^2\|_2\gg_wX^{3/2}\); thus a relative global \(o(1)\) bound does **not** imply an absolute \(o(X)\) coefficient error, and our explicit ratio is much weaker than the rough \(o(X^{-1/2})\) requirement for that route.

A **sufficient** perturbation bound \(\|S_X-S'\|_2=o(\sqrt{X/\log X})\) would imply \(r_w(N)-r'_w(N)=o(X)\) by Cauchy and weighted PNT; the adversarial construction only provides \(\|S_X-S'\|_2=O_w(\sqrt{X\log\log X})\). There is a logarithmically growing gap. These are sufficiency scales, not evidence that \(r_w(N)\asymp X\) has been proved for any particular residual N.

A future solution must establish **target-anchored** information not preserved by deletion: e.g. a genuinely independent uniform signed prime-only minor-arc estimate, a quantified bilinear dispersion theorem that forces a positive complementary pair, or a rigidity property for the **actual fixed** coefficient sequence. Such results are **OPEN** in this research.

## 5. Verification and independent criticism

An actually executed standard-library Python 3.13.5 program, \`verify_stage71.py\`, gave PASS. Its full stdout is stored exactly in \`exact_results.json\`; the script and output were byte-matched to the GitHub copies by Git object hashing, and their SHA-256 hashes are in \`verification_manifest.json\`. Checks were limited to:

- 15 deletion-budget integer levels for a three-edge nontrivial matching, compared between the greedy formula and an **independent dynamic program that allows deletions from both endpoints**;
- five finite residual targets N=50,100,120,256,300 in an odd-prime support up to 200, with exact nonconstant integer weights; exact minimum cost, target extinction, full-energy monotonicity and the Young L4 bound;
- explicit check that each N is in H and no p=q diagonal exists.

This is verification of finite algebra. It is neither a large Goldbach search nor proof of a prime asymptotic.

See \`02_adversarial_review.md\` for first-pitfall analysis and external-source limitations.

## 6. Source status, scope and next research choice

**Primary external theorem:** J. Wu, *Chen's double sieve, Goldbach's conjecture and the twin prime problem*, *Acta Arithmetica* 114 (2004), 215–273, DOI https://doi.org/10.4064/aa114-3-2. The paper's Theorem 1 is an **upper**, not lower, bound: \(D(N)\le7.8209\,\Theta(N)\) for sufficiently large even N. Its journal listing and original statement were retrieved, but the full published proof is not newly re-proved here. Classical PNT and \(N/\varphi(N)\ll\log\log N\) are likewise external established inputs.

**Project status:** T71.1 exact matching sensitivity **PROVED**; T71.1a reflected perturbation **PROVED**; T71.2 normalized global Fourier near-invisibility **PROVED deduction from established external theorems**; explicit countermodels **FINITE checks**; actual fixed-prime target-uniform positivity **OPEN**.

**Next Stage 72 (queued only):** work exclusively on a *target-level* true-prime quantity that is provably sensitive to the matching deletion while preserving the original fixed coefficients. One possible direction is an exact, signed prime-only minor-arc bilinear estimate or genuinely stronger growing-modulus distribution with a mathematical derivation that crosses the sieve parity barrier. Do not return to polishing global Lp norms, large finite prime scans or reformulations that already assume a complementary pair.

**Resource control:** no Codex, CoCalc Goal, scheduled automation, paid resource, GitHub permission change, \`main\` merge or history rewrite occurred. Keep this research branch and any PR in draft review status.
