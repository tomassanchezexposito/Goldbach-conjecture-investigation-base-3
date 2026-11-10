# Stage 68 — Foundational operator-allocation theorem and uniform Gram obstruction

**Evidence class:** proved functional-analytic statements for arbitrary \(L^2\) inputs; **no arithmetic estimate for genuine primes**, and **no Goldbach proof**. This note is an initial research scaffold for an independent CoCalc proof audit, not the Stage 68 final report.

## 1. Exact scope inherited from Stage 67

Let \(E_1,\ldots,E_R\subset\mathbb T=\mathbb R/\mathbb Z\) be **pairwise disjoint** measurable sets, \(J=\{j_1,\dots,j_m\}\subset\mathbb Z\setminus\{0\}\) a set of **distinct** shifts and \(N\in\mathbb Z\). Define
\[
g_j(\alpha)=e(-N\alpha)(e(-j\alpha)-1),\quad
G_r(j,k)=\int_{E_r}g_j(\alpha)\overline{g_k(\alpha)}\,d\alpha,
\quad e(t)=e^{2\pi it}.
\]
These are the Stage 67 restricted Hermitian positive-semidefinite Gram matrices. For each \(f_r\in L^2(E_r)\), let its signed increment vector be
\[
D_r(f_r)_j=\int_{E_r} f_r(\alpha)g_j(\alpha)\,d\alpha,\qquad
D(f_1,\ldots,f_R)=\sum_{r=1}^R D_r(f_r).
\]
Here **\(f_r=S_w(\alpha)^2\)** in the true-prime application; these first theorems allow arbitrary \(f_r\) and therefore cannot be asserted sharp *among prime exponential polynomials*. The target phase in \(g_j\) is essential to the genuine-prime coefficient convention.

## 2. Theorem 68.1 — exact optimization over independent arc energy budgets (PROVED)

Suppose \(\|f_r\|_{L^2(E_r)}^2\le B_r\), with specified real \(B_r\ge0\). Then the **exact** maximum possible Euclidean norm of the signed increment vector, over all admissible arbitrary complex \(f_r\), is
\[
\boxed{
\sup_{\|f_r\|_2^2\le B_r}\Big\|\sum_{r=1}^R D_r(f_r)\Big\|_{\ell^2(J)}
=\max_{\|z\|_2=1}\sum_{r=1}^R\sqrt{B_r}\,\sqrt{z^*G_rz}.
}
\tag{68.1}
\]
This is more precise than the usually quoted, potentially strict bound
\[
\Big\|\sum_rD_r(f_r)\Big\|_2\le\sum_r\sqrt{B_r\lambda_{\max}(G_r)}.
\tag{68.2}
\]

**Proof.** In finite-dimensional complex space \(\|v\|=\max_{\|z\|=1}|\sum_j\overline{z_j}v_j|\). For a fixed \(z\), the relevant functional of \(f_r\) equals
\[
\sum_j\overline{z_j}D_r(f_r)_j
=\int_{E_r}f_r(\alpha)\left(\sum_j\overline{z_j}g_j(\alpha)\right)d\alpha.
\]
By Cauchy–Schwarz its optimal absolute value is \(\sqrt{B_r}\left\|\sum_j\overline{z_j}g_j\right\|_{L^2(E_r)}
=\sqrt{B_r}\sqrt{z^*G_rz}\).
Independence of the \(f_r\) on disjoint sets allows simultaneous equality with the same overall complex phase: choose each \(f_r\) proportional to the complex conjugate of the displayed multiplier (or zero when its norm vanishes). Hence for fixed \(z\), the optimal real projection is the **sum** of the individual optimal support functions. Both maxima can be interchanged because they are suprema over a Cartesian product, and the unit sphere for \(z\) is compact. This proves (68.1), including zero budgets and singular Gram matrices. Equation (68.2) follows from \(z^*G_rz\le\lambda_{\max}(G_r)\).

**Nonaligned example.** In an abstract two-dimensional observation space, \(B_1=B_2=1\) and \(G_1=\operatorname{diag}(1,0),\ G_2=\operatorname{diag}(0,1)\) give an exact maximum \(\sqrt2\) by (68.1), while (68.2) gives \(2\). This example illustrates a general operator-theoretic phenomenon and is **not claimed to arise from the specific rational-arc Gram matrices**. When the top eigenspaces align, equality in (68.2) may hold.

**Caveat.** The objective in (68.1) is the **worst-case upper bound** over arbitrary complex functions with the stated piecewise energies. It is not itself an estimate proving that the genuine prime input exhibits such worst-case alignment, nor a pointwise *lower* bound for prime-pair representations.

## 3. Corollary 68.2 — allocation to arcs adds no information if only total energy is known (PROVED)

Let \(E=\bigsqcup_rE_r\), \(G_E=\sum_rG_r\), and suppose only
\[
\sum_r\|f_r\|_2^2\le B
\]
is independently known. Then
\[
\boxed{
\sup_{\sum_r\|f_r\|_2^2\le B}
\Big\|\sum_rD_r(f_r)\Big\|_2
=\sqrt{B\,\lambda_{\max}(G_E)}.}
\tag{68.3}
\]
**Proof.** Treat the disjoint union as a single Hilbert-space domain \(L^2(E)=\bigoplus_r L^2(E_r)\). The coefficient map \(D:L^2(E)\to\mathbb C^m\) has \(DD^*=G_E\) (up to the harmless bilinear-versus-sesquilinear convention, giving the same Hermitian Gram); its operator norm is \(\sqrt{\lambda_{\max}(G_E)}\). The exact extremizer is a top singular vector. Equivalently, for fixed unit \(z\), maximize
\(\sum_r \sqrt{B_r}\sqrt{z^*G_rz}\) subject to \(B_r\ge0\), \(\sum_rB_r\le B\). Cauchy–Schwarz yields \(\sqrt{B\sum_r z^*G_rz}=\sqrt{Bz^*G_Ez}\), and the optimal allocation \(B_r\propto z^*G_rz\) attains it. Maximizing over \(z\) gives (68.3).

**Interpretation.** Merely *naming* rational subarcs does not upgrade an unallocated global fourth-moment bound. To gain anything in an operator argument one needs independently established nontrivial budgets \(B_r\) (or additional constraints on their phases and arithmetic structure), not just \(\sum B_r\le B\).

## 4. Theorem 68.3 — no global minor-set Gram gain, uniformly in shift-block dimension (PROVED)

Let \(\mathfrak M\subset\mathbb T\) be the major-arc set, \(\mathfrak m=\mathbb T\setminus\mathfrak M\), and \(J\) any finite set of \(m\ge1\) **distinct nonzero integer shifts**, allowed to depend arbitrarily on \(X\). Then
\[
\boxed{
m+1-4m|\mathfrak M|
\ \le\ \lambda_{\max}(G_{\mathfrak m})
\ \le\ m+1.}
\tag{68.4}
\]
The lower bound may be negative and then is merely trivial; it is informative when \(|\mathfrak M|=o(1)\).

**Proof.** Stage 67 gives \(G_{\mathbb T}=I_m+\mathbf1\mathbf1^*\) exactly, hence \(\lambda_{\max}(G_{\mathbb T})=m+1\). Since \(G_{\mathfrak M}\succeq0\) and \(G_{\mathfrak m}=G_{\mathbb T}-G_{\mathfrak M}\preceq G_{\mathbb T}\), the upper bound follows. Let \(z=m^{-1/2}(1,\dots,1)\), a unit top eigenvector of \(G_{\mathbb T}\). By the Rayleigh principle
\[
\lambda_{\max}(G_{\mathfrak m})
\ge z^*G_{\mathfrak m}z
=m+1-\int_{\mathfrak M}\left|\sum_{j\in J}\overline{z_j}g_j(\alpha)\right|^2d\alpha.
\]
Since \(|g_j|\le2\), the integrand is at most \((2\sqrt m)^2=4m\), yielding the lower bound. All estimates are uniform in the shift values and in \(m\).

For the Li–Liu-style major cores with \(P=X^\kappa\), \(\kappa<1/2\), the union estimate \(|\mathfrak M|\le2P^2/X=o(1)\) yields
\[
\frac{\lambda_{\max}(G_{\mathfrak m})}{m+1}=1+O(|\mathfrak M|)=1+o(1)
\quad\text{**uniformly for any finite** }J=J(X).
\tag{68.5}
\]
In particular, increasing the number of shifts to the growing scale demanded by Stage 66 **does not** by itself create a nontrivial *relative* operator-norm saving on the complete minor set. This strengthens Stage 67's stated fixed-\(m\) conclusion. The theorem is still a geometric statement for arbitrary \(L^2\) inputs.

## 5. Target-anchored scalar budget and the exact missing information

For a prescribed target \(N\), the minor coefficient
\[
m_w(N)=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)\,d\alpha
\]
is a single linear functional whose multiplier has unit modulus. If piecewise budgets \(B_r\) on the full minor partition \(E_r\) are available, its exact unrestricted worst-case bound is
\[
\boxed{
|m_w(N)|\le\sum_r\sqrt{B_r|E_r|}.}
\tag{68.6}
\]
This is achieved by suitably phase-aligned arbitrary \(L^2\) functions on each arc. It is an upper bound, not the signed *lower* bound \(m_w(N)>-a_w(N)\) required to exclude a missing representation.

If only \(\sum_r B_r\le B\) is known, maximizing (68.6) gives at most \(\sqrt{B|\mathfrak m|}\) by Cauchy–Schwarz, recovering ordinary global Cauchy–Schwarz without a pointwise arithmetic saving. The same allocation barrier persists for increment vectors by (68.3).

For the genuine prime input, let \(\overline B_r\) be **independently proved** bounds satisfying \(\int_{E_r}|S_w|^4\le\overline B_r\). Let
\[
\overline B=\sum_r\overline B_r,\qquad
\overline V=\left(\max_{\|z\|=1}
\sum_r\sqrt{\overline B_r}\sqrt{z^*G_rz}\right)^2.
\]
If an external (fully quantified and actually proved) major-arc estimate gives \(a_w(N)\ge A_X>0\) for the selected residual target, then the sharp Stage 66 aggregate local-energy argument yields the valid **conditional** implication
\[
\boxed{
A_X^2+m\left(A_X-\sqrt{\overline V/m}\right)_+^2
>\overline B
\ \Longrightarrow\ 
R(N)>0.}
\tag{68.7}
\]
Indeed, if \(R(N)=0\), the full nonnegative prime-only coefficient vanishes, so \(m_w(N)=-a_w(N)\) and \(|m_w(N)|\ge A_X\). Parseval gives
\(\|m_w\|_{\ell^2(\mathbb Z)}^2=\int_{\mathfrak m}|S_w|^4\le\overline B\).
For distinct shifts, the actual aggregate increment vector has squared norm \(\le\overline V\) by (68.1). The Stage 66 sharp aggregate theorem then implies
\(\|m_w\|_2^2\ge A_X^2+m(A_X-\sqrt{\overline V/m})_+^2>\overline B\), contradiction.

**Critical open obligation:** Neither the required arcwise budgets \(\overline B_r\) nor a signed cancellation estimate that makes (68.7) strict for every residual \(N\) has been proved from true-prime distribution in this research. If all that is known is the inherited global fourth moment \(\overline B\ll X^{5/2}(\log X)^{100}\), Corollary 68.2 and Theorem 68.3 explain why arbitrary arc partition and growing shift dimension alone cannot supply the missing pointwise control.

Also test whether an operator estimate on *increments* is logically any weaker than a direct signed estimate for the center: if its proof selects a representation of \(N\), divides by \(R(N)\), presumes all nearby coefficients are positive, or silently equates local wheel survival with primality, it is not an independent proof.

## 6. Evidence classification, adversarial issues and next tasks

- **Proved from basic Hilbert-space facts:** (68.1)–(68.4), their extremizers and (68.5)–(68.6), subject to careful audit of all conjugation conventions.
- **Conditional logical implication:** (68.7), depending on an independently justified major-arc bound and independent genuine-prime arc energy estimates.
- **NOT PROVED:** any strong arcwise \(\overline B_r\), genuine-prime signed cancellation, target-uniform \(R(N)>0\), or full strong Goldbach.
- **Potential pitfalls to audit:** \(S_w^2\) versus \(|S_w|^2\); Hermitian orientation in \(G_E\); disjointness versus overlapping arc sets; the difference between full-circle and arc-restricted norms; complex phase alignment versus real-symmetric prime inputs; the nonnegative representation coefficient versus signed minor-arc contribution; large \(m\) versus bounded shift-size; the \(2+2\) diagonal and prime 3 base-position exception.
- **No raw numerical Goldbach sweep needed.** A small exact operator example may test minimax constants, but a proof of the optimization for all finite \(R,m\) is the real deliverable.

Stage 68 should independently prove or refute these statements first, sharpen the *arithmetic* research question by exploring the true-prime tensor structure and the possibility of independently proving nontrivial arcwise allocations or signed cancellation, and identify the first currently unavailable theorem with exact variables, quantifiers, constants and citation provenance.
