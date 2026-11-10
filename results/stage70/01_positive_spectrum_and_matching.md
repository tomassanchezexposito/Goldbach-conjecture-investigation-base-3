# Stage 70 — Positive-spectrum Fourier cone and the prime-support matching obstruction

**Research date:** 2026-11-10.  
**Execution:** independent mathematical research and local Python verification **without CoCalc/Codex**, using the GitHub-connected branch \`cocalc/stage70-positive-spectrum-cone-audit\`.  
**Scientific status:** two **PROVED** finite-dimensional/finite-prime-support lemmas, one **PROVED** classical-PNT consequence, and an **OPEN** quantitative actual-prime problem. **No proof of Goldbach**.

## 0. Keep the target and the hierarchy of admissible inputs exact

The author's original cases remain \(N=p+1\), \(N=2p\), or \(N=p+q\) with \(p<q\) genuine primes, plus the tautologically equivalent reflection \(N-2p=2q-N\). On
\[
H=\{N\ge4:N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\}
\]
the first two cases fail, and the unresolved claim is \(R(N)>0\). For even N>4, prime 2 cannot occur in a prime-pair representation; prime 3 is retained. The odd-prime position map \(p=3+2a\) is a coordinate only.

Let \(e(t)=e^{2\pi it}\), and let \(\mathbb T=\mathbb R/\mathbb Z\). An actual weighted prime polynomial has
\[
S_w(\alpha)=\sum_{p\text{ genuine prime}}a_pe(p\alpha),\quad
a_p=(\log p)w(p/X)\ge0,\quad
F_w=S_w^2=\sum_k r_w(k)e(k\alpha),
\]
with \(r_w(k)=\sum_{p+q=k}a_pa_q\ge0\) and exact full energy
\(\int_{\mathbb T}|F_w|^2=\sum_kr_w(k)^2\).

**Three distinct mathematical classes (never conflate them):**
1. Unrestricted finite Fourier polynomials \(F=\sum_{k\in K}c_ke(k\alpha)\), complex \(c_k\).
2. Nonnegative-spectrum polynomials \(c_k\ge0\) on a chosen finite \(K\); not every such coefficient vector is \(S^2\).
3. Prime-square inputs \(F=S^2\) with \(S=\sum_{p\in P}s_pe(p\alpha)\) and \(s_p\ge0\); the fixed *actual* \(s_p=a_p\) is one point of this class, and allowing zeros in \(s_p\) enlarges the admissible class materially.

## 1. Theorem 70.1 — exact positive-spectrum dual-cone bound (PROVED)

Let \(K\subset\mathbb Z\) be finite, \(N\in\mathbb Z\), and \(M\subset\mathbb T\) measurable and invariant under reflection \(\alpha\mapsto-\alpha\) up to null sets. Define the **real** numbers
\[
\beta_k(N;M)=\int_Me((k-N)\alpha)\,d\alpha
=\int_M\cos(2\pi(k-N)\alpha)\,d\alpha,
\quad k\in K\setminus\{N\}.
\]
For \(F(\alpha)=\sum_{k\in K}c_ke(k\alpha)\) with **nonnegative real** \(c_k\), assume \(c_N=0\) (interpreted as automatic if \(N\notin K\)) and that its actual major coefficient is the **positive real** number
\[
a=\int_MF(\alpha)e(-N\alpha)\,d\alpha>0.
\]
Put \(D_+=\sum_{k\in K\setminus\{N\}}(\max\{\beta_k,0\})^2\). Then
\[
\boxed{\int_{\mathbb T}|F(\alpha)|^2\,d\alpha
=\sum_kc_k^2\ge\frac{a^2}{D_+}.}\tag{70.1}
\]
If \(D_+=0\), a positive a is impossible. If \(D_+>0\), equality in this **nonnegative coefficient cone** is attained by
\[
c_k=\frac{a\,(\beta_k)_+}{D_+},\quad k\ne N,\qquad c_N=0.
\tag{70.2}
\]
In contrast, allowing arbitrary **complex** \(c_k\) gives the weaker *sharp* bound
\[
\int|F|^2\ge\frac{a^2}{D_{\rm free}},\quad
D_{\rm free}=\sum_{k\in K\setminus\{N\}}|\beta_k|^2.
\tag{70.3}
\]
Thus whenever both signs of nonzero \(\beta_k\) occur on K, the nonnegative cone gives a strict improvement, quantified by \(D_{\rm free}/D_+>1\).

**Proof 1 (cone duality).** Because \(c_k\ge0\),
\[
a=\sum_{k\ne N}c_k\beta_k
\le\sum_{k\ne N}c_k(\beta_k)_+
\le\sqrt{\sum_kc_k^2}\sqrt{D_+}.
\]
The candidate (70.2) meets both inequalities with equality. Parseval gives the displayed full energy. If \(D_+=0\), the first sum cannot be positive.

**Proof 2 (KKT / constrained projection).** Minimize \(\tfrac12\sum c_k^2\) subject to \(\sum c_k\beta_k=a>0\), \(c_k\ge0\), \(c_N=0\). This is a strictly convex quadratic program on a closed convex feasible set. Its stationarity and complementary-slackness conditions give \(c_k=t(\beta_k)_+\) for \(t>0\), and the linear equality determines \(t=a/D_+\). Feasible and unique. For unrestricted complex coefficients, Hilbert-space projection onto the linear functional's representer \((\overline{\beta_k})_{k\ne N}\) gives (70.3).

**Exact finite cyclic example, not a Goldbach example.** On \(\mathbb Z/12\mathbb Z\), let the major set be \(M=\{0,1,5,6,7,11\}\), normalized counting measure, center N=0, and allowed Fourier frequencies K=\{2,6\}. It is reflection symmetric and half-period invariant. Direct character orthogonality gives \(\beta_2=1/3,\ \beta_6=-1/6\). Then \(D_{\rm free}=5/36\), \(D_+=1/9\), so for positive \(a=1\) the unrestricted minimum energy is \(36/5\) whereas the nonnegative-cone minimum energy is **9**. The first has coefficient vector \((12/5,-6/5)\), forbidden by positivity; the second \((3,0)\) is feasible. These exact values were checked independently by a finite cyclic DFT. This example illustrates the strict cone gain and is **not asserted to be a prime-square input or the actual continuous circle major arcs**.

**Corollary 70.1a (non-circular target criterion; CONDITIONAL for actual primes).** Choose any **explicitly predetermined** frequency superset
\[
K_X=\{k\in2\mathbb Z:6\le k\le2Y\}
\]
for a nonnegative real prime weight supported on odd genuine primes \(p\le Y\). Use \(K_X\setminus\{N\}\) in \(D_+\), without needing to know which even k are actually represented. If an independent major-arc theorem proves \(a_w(N)\ge A_X>0\), and an independent **full-circle** fourth-moment estimate proves \(\int_{\mathbb T}|S_w|^4\le B_X\), then
\[
\boxed{B_XD_+(N;M,K_X)<A_X^2\quad\Longrightarrow\quad r_w(N)>0.}\tag{70.4}
\]
**Proof by contradiction:** if \(r_w(N)=0\), then \(F_w=S_w^2\) lies in the nonnegative cone with \(c_N=0\), so (70.1) contradicts (70.4). This does **not** select a representation at N. For \(N\in H\), a positive coefficient certifies a distinct genuine-prime pair. The criterion is not currently known to hold with available arithmetic estimates; **no Goldbach proof is claimed**.

**Critical caveat:** K_X is a *permitted superset*, not the exactly known true prime-pair sumset; computing the exact sumset and omitting N because a prime pair was found would make an alleged proof circular. The sharpness extremizer in (70.2) need not factor as \(S^2\) and need not correspond to actual prime coefficients. Any further gain from nonnegative *factorization* is a separate problem.

## 2. Theorem 70.2 — half-mass prime-support deletion with a prescribed missing target (PROVED)

Let P be any finite set of **genuine primes**, let \(a_p\ge0\) be arbitrary weights, and let N be an integer with no prime diagonal within P (in particular every \(N\in H\)). Then there is a subset \(P'\subseteq P\) such that
\[
\boxed{\sum_{p\in P'}a_p\ge\frac12\sum_{p\in P}a_p,\qquad
\sum_{\substack{p,q\in P'\\p+q=N}}a_pa_q=0.}\tag{70.5}
\]
Writing \(S'=\sum_{p\in P'}a_pe(p\alpha)\), \(S=\sum_{p\in P}a_pe(p\alpha)\), the same construction ensures
\[
0\le [S'^2]_k\le[S^2]_k\quad(\forall k),\qquad
\boxed{\int_{\mathbb T}|S'|^4\le\int_{\mathbb T}|S|^4.}\tag{70.6}
\]

**Proof.** Form the complement graph with vertices P and an undirected edge between distinct p,q precisely when p+q=N. Each p has **at most one** neighbor q=N−p, so the graph is a matching plus isolated vertices; there are no loops by the diagonal hypothesis. From each edge keep its endpoint with the larger weight (break ties arbitrarily), and retain every isolated vertex. The retained weight is at least half that of each two-vertex component and all that of each isolated vertex, proving the first inequality. No edge has both endpoints retained, so \([S'^2]_N=0\). Every Fourier coefficient of S and S' squared is a sum of nonnegative ordered products, and setting some weights to zero can only decrease each coefficient. Squaring their nonnegative values and summing over k gives (70.6) by Parseval. No assumptions about distribution or primality beyond membership of P are needed.

**Sharpness scope.** The factor \(1/2\) cannot be increased **uniformly over all matching graphs with equal-weight complete edges**. It is not asserted that this worst case arises for the full set of genuine primes in every interval. In concrete prime sets, the retained mass may be much higher.

**Exactly what this refutes.** A hypothetical representation cannot be forced from only the following *coarse input data*: (i) support is a **subset** of genuine-prime positions, (ii) all prime-frequency coefficients are nonnegative and bounded above by specified original weights, (iii) total weight is at least half the original mass, and (iv) the *full-circle* fourth moment is bounded above by the original full-circle moment. The theorem supplies a countermodel inside that broad class with the target coefficient zero, even if the **original** actual prime polynomial has many representations.

**Exactly what this does NOT refute.** The actual \(S_w\) uses **every** genuine prime with its specified positive weight wherever \(w>0\); one is **not allowed** to delete half the coefficients in a proof about that fixed polynomial. The constructed S' does not preserve all fixed coefficients, a prescribed major-arc asymptotic, or the Li–Liu minor-arc moment bound without a separate argument. It is **not a counterexample** to strong Goldbach and does not exclude a strategy exploiting all actual prime coefficients or signed arc cancellation.

**Independent exact check.** A separate integer-only program took all odd genuine primes ≤200 with nonconstant positive integer weights \(a_p=p+(p\bmod7)^2\). At residual targets N=50,100,120,256,300 the original positive weighted target coefficient was nonzero; the pruned coefficient was exactly zero, while at least half the original mass remained and every squared-convolution coefficient, and hence the total fourth-moment energy, did not increase. The experiment validates an exact theorem implementation, not a universal computation.

## 3. A classical-PNT scale check for full-circle energy (PROVED conditional on an established theorem)

Suppose \(w\ge0\) is fixed, piecewise smooth, supported in (0,1), and \(\int_0^1w(t)dt>0\). The **known prime number theorem** (weighted partial summation) gives
\[
S_w(0)=\sum_p(\log p)w(p/X)\sim X\int_0^1w(t)\,dt,
\]
so \(S_w(0)\ge c_wX\) for sufficiently large X. For \(|\alpha|\le1/(12X)\), all contributing primes satisfy p≤X, so
\(\Re S_w(\alpha)\ge(\sqrt3/2)S_w(0)\). This interval has measure \(1/(6X)\), hence
\[
\boxed{\int_{\mathbb T}|S_w(\alpha)|^4d\alpha\ge
\frac{3}{32}c_w^4X^3.}\tag{70.7}
\]
This is an unconditional consequence of the standard PNT for fixed nontrivial nonnegative smooth weights, **not a new prime-distribution theorem**.

**Implication:** a minor-arc fourth-moment upper bound of scale \(X^{5/2}\log^{100}X\) may **never** be substituted into an inequality demanding an upper bound for the *full-circle* energy, whose actual lower bound is of scale \(X^3\). In particular, the M2/M9 full-circle one-hole criterion is a different theorem from a minor-only Cauchy estimate. The PNT lower bound does **not** rule out a stronger positivity-cone Fourier criterion that has a much smaller geometric constant \(D_+\); evaluating that constant on the actual major sets remains OPEN.

## 4. Adversarial issue: refining cells cannot manufacture a uniform quadratic local budget

A prior conditional Stage 69 idea imposed \(B_E:=\int_E|S_w|^4\le CX^2|E|^2\) for every cell E of a very fine partition. For a partition of the minor set with maximal cell size \(h\), this would force
\[
\int_{\mathfrak m}|S_w|^4=\sum_EB_E
\le CX^2\sum_E|E|^2\le CX^2 h|\mathfrak m|.
\]
For any fixed nonzero \(S_w\) and nonempty minor set of positive measure, its left side is positive. Thus one cannot assert such a uniform bound with fixed C and fixed X over **arbitrarily fine** refinements \(h\to0\); it would imply a contradiction. For a family of X-dependent partitions, the condition might instead require constants that grow with refinement and must be justified independently. This identifies the first invalid inference in any purported proof that splits arcs indefinitely while retaining the same \(CX^2|E|^2\) upper bound.

## 5. Literature comparison and first missing theorem

The recent Li–Liu 2026 arXiv preprint \`https://arxiv.org/abs/2610.26756\` reports a **conditional** fourth-moment bound on the **minor arcs** and an exceptional-set bound; it does not supply (70.4). The published Bhowmik–Grimmelt \`https://doi.org/10.1007/s10476-026-00191-z\` discusses explicit major-arc formulae and exceptional sets, not a uniform zero-exception theorem. See the source-status table already committed in Stage 69. Neither paper is claimed here to have been independently re-proved.

**Open Stage 70 arithmetic question:** For the actual fixed full-prime weight and the actual symmetric major arcs, determine whether the fully explicit geometry-only \(D_+(N;M,K_X)\), together with any rigorously established **full-circle** \(B_X\) and target major lower bound \(A_X\), ever satisfies (70.4) uniformly for all N in H. If not, identify whether the factorization \(F_w=S_w^2\), with **fixed nonzero coefficients on all appropriate primes**, admits a stronger, *quantitative and uniform* obstruction. A constructive theorem about the *true* prime coefficients is necessary; removing primes from support as in Theorem 70.2 is disallowed.

**Final status:** Stage 70's first theoretical cycle is complete; **PROVED:** Theorems 70.1, 70.2 and their finite examples, and classical-PNT consequence (70.7). **REFUTED for the stated broad classes:** prime-support + nonnegative upper-bounded weights + half total mass + full energy upper bound, without fixed coefficients, implies target existence. **OPEN:** a non-circular uniform prime-only signed saving or an effective true-prime support-separation threshold sufficient to establish \(R(N)>0\) on H. This work does not solve Goldbach.
