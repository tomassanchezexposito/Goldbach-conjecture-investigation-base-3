# Stage 67 — Rational-arc Gram geometry and the pointwise prime gap

**Status:** exact geometric identities proved; no new prime-correlation saving obtained. The original residual set and three-case formulation are unchanged, and universal coverage remains open.

## 1. Conventions and exact Gram matrix

Write $e(t)=e^{2\pi i t}$ and take Fourier coefficients with $e(-n\alpha)$. Let $J=\{j_1,\ldots,j_m\}$ be distinct nonzero integers, let $E\subset\mathbb R/\mathbb Z$ be measurable, and put
$$g_j(\alpha)=e(-N\alpha)(e(-j\alpha)-1).$$
The target phase cancels in every Gram entry. If
$$\mu_E(n)=\int_E e(n\alpha)\,d\alpha,$$
then the exact Hermitian Gram matrix is
$$\boxed{G_E(j,k)=\mu_E(k-j)-\mu_E(-j)-\mu_E(k)+\mu_E(0).}$$
Indeed, the integrand is $(e(-j\alpha)-1)(e(k\alpha)-1)$. For every vector $z\in\mathbb C^J$,
$$z^*G_Ez=\int_E\left|\sum_{j\in J}\overline{z_j}g_j(\alpha)\right|^2d\alpha\ge0.$$
Thus $G_E$ is positive semidefinite and its operator norm is its largest eigenvalue. In general that eigenvalue is the largest root of the characteristic polynomial of the explicit matrix above; there is no arc-independent scalar formula beyond this finite matrix. The exact matrix, rather than a pointwise multiplier maximum, retains the interaction between the shifts.

If $E$ is a disjoint union of intervals $I_r=\{c_r+\beta:|\beta|\le\rho_r\}$, with lengths $2\rho_r$, then
$$\mu_E(0)=\sum_r2\rho_r,\qquad
\mu_E(n)=\sum_r e(nc_r)\frac{\sin(2\pi n\rho_r)}{\pi n}\quad(n\ne0).$$
These formulas also apply to intervals crossing the chosen coordinate origin by interpreting them on the circle. They give exact entries for any rational centers and rational widths.

For the full circle, orthogonality gives $G_{\mathbb T}=I_m+\mathbf1\mathbf1^*$. Its eigenvalues are $m+1$ once and $1$ with multiplicity $m-1$ (for $m=1$, just $2$). This recovers the Stage 66 sharp full-circle operator norm.

## 2. Rational centers, divisibility, and finite width

At a reduced center $c=a/q$, define the center vector
$$v_j(c)=e(-ja/q)-1.$$
Since $(a,q)=1$, $v_j(c)=0$ exactly when $q\mid j$. In the parity-preserving Stage 66 shifts $j=2h$, this condition is $q\mid2h$. If it fails, the center multiplier has size
$$|v_j(a/q)|=2|\sin(\pi ja/q)|>0,$$
which may be as large as $2$. Divisibility by the shift, rather than proximity to a rational number by itself, is the resonance condition.

For a single centered interval of radius $\rho$, the matrix has the exact decomposition
$$G_I=2\rho\,v(c)v(c)^*+E_I.$$
Let $L_J=2\pi(\sum_{j\in J}j^2)^{1/2}$. The componentwise derivative estimate implies
$$\|v(c+\beta)-v(c)\|_2\le L_J|\beta|.$$
Using $\|xx^*-yy^*\|_{op}\le\|x-y\|_2(\|x\|_2+\|y\|_2)$ and integrating over $-\rho\le\beta\le\rho$ proves
$$\boxed{\|E_I\|_{op}\le2L_J\|v(c)\|_2\rho^2+\frac23L_J^2\rho^3.}$$
For a disjoint union of centered intervals, the center matrices add and the errors obey the sum of these bounds. In particular,
$$\left|\lambda_{max}(G_E)-\lambda_{max}\!\left(\sum_r2\rho_rv(c_r)v(c_r)^*\right)\right|
\le\sum_r\left(2L_J\|v(c_r)\|_2\rho_r^2+\frac23L_J^2\rho_r^3\right).$$
This follows from Weyl's eigenvalue inequality. If $q\mid j$ for every $j\in J$ at one center, its center matrix vanishes and its interval Gram norm is at most $\frac23L_J^2\rho^3$. The cubic order is sharp: for a singleton $J=\{j\}$ at a resonant center,
$$G_I(j,j)=4\rho-\frac{2\sin(2\pi j\rho)}{\pi j}
=\frac83\pi^2j^2\rho^3+O(j^4\rho^5)$$
as $|j|\rho\to0$.

If $q\nmid j$, the exact singleton formula is
$$G_I(j,j)=4\rho-2\cos(2\pi ja/q)\frac{\sin(2\pi j\rho)}{\pi j}
=2\rho|v_j(a/q)|^2+O(j^2\rho^3).$$
For example, at $a/q=1/3$ and shift $j=2$, the center multiplier has squared size $3$, and
$$G_I(2,2)=4\rho+\frac{\sin(4\pi\rho)}{2\pi}=6\rho+O(\rho^3).$$
This refutes a uniform small-shift estimate of cubic order on arcs centered at arbitrary rationals. It is not a prime counterexample.

For finitely many shrinking arcs, the center matrix is the exact first-order asymptotic. More precisely, if the center and shifts are fixed and all radii scale by $\varepsilon$, then
$$G_E(\varepsilon)=\varepsilon C+O_{J,c}(\varepsilon^2),\quad
C=\sum_r2\rho_rv(c_r)v(c_r)^*,$$
in operator norm. When every center is resonant for every shift, the error improves to $O_J(\varepsilon^3)$.

## 3. What happens on the complete minor-arc set

The cited Li–Liu setup uses $P=X^\kappa$, reduced centers $a/q$ with $q\le P$, and major arcs of radius $P/(qX)$; the audited range has $\kappa<1/2$. Let $\mathfrak M$ be their union. Even allowing overlaps,
$$|\mathfrak M|\le\sum_{q\le P}\varphi(q)\frac{2P}{qX}
\le\frac{2P^2}{X}=2X^{2\kappa-1}=o(1).$$
The complete minor set is $\mathfrak m=\mathbb T\setminus\mathfrak M$. Since $|g_j\overline{g_k}|\le4$,
$$|G_{\mathfrak m}(j,k)-G_{\mathbb T}(j,k)|
=|G_{\mathfrak M}(j,k)|\le4|\mathfrak M|.$$
For fixed $m$, $\|G_{\mathfrak m}-G_{\mathbb T}\|_{op}\le4m|\mathfrak M|\le8mX^{2\kappa-1}$. Consequently
$$\lambda_{max}(G_{\mathfrak m})=m+1+O(mX^{2\kappa-1})$$
for fixed $J$ as $X\to\infty$. A useful gain on selected resonant subarcs does not survive as an unweighted Gram gain on the complete minor set. This conclusion is geometric and does not use a prime estimate.

The arcs at $a/q$ in this setup are the major-arc cores and are removed from $\mathfrak m$. Even if a local estimate were obtained on some selected part of the minor set, it would not control the signed increment over the omitted remainder. One must bound or exploit cancellation on every part of the minor set.

## 4. Application to genuine prime coefficients

Let
$$S_w(\alpha)=\sum_p(\log p)w(p/X)e(p\alpha),\quad
m_w(n)=\int_{\mathfrak m}S_w(\alpha)^2e(-n\alpha)\,d\alpha.$$
The square $S_w^2$ selects sums of two primes; replacing it by $|S_w|^2$ changes to prime differences. For each integer shift $j$ and target $N$,
$$\Delta_j(N):=m_w(N+j)-m_w(N)
=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)(e(-j\alpha)-1)\,d\alpha.$$
This is an unconditional identity and makes no assumption that $N$ has a prime representation.

For any measurable $E\subseteq\mathfrak m$, define $\Delta_j^E(N)$ by restricting this integral to $E$ and $B_E=\int_E|S_w|^4$. The exact Gram operator gives
$$\boxed{\sum_{j\in J}|\Delta_j^E(N)|^2\le B_E\,\lambda_{max}(G_E).}$$
Indeed, for every unit $z$, Cauchy–Schwarz bounds $|\sum_j\overline{z_j}\Delta_j^E|^2$ by $B_E z^*G_Ez$, and taking the supremum proves the claim. The bound is uniform in $N$ and is optimal for an unconstrained $L^2(E)$ input. Its application to $S_w^2e(-N\alpha)$ remains an upper bound only; no primality-specific gain follows from the Gram identity.

For the complete minor set and fixed shifts, the Stage 66 conditional global fourth moment gives only
$$\sum_{j\in J}|\Delta_j(N)|^2
\le B_X\bigl(m+1+O(mX^{2\kappa-1})\bigr),\quad
B_X\ll X^{5/2}(\log X)^{100}.$$
The major-arc main term at a residual target is of order $A_X\asymp X$, under the hypotheses recorded in the Stage 64 source audit. The exact Stage 66 criterion can be nonvacuous only when $mA_X^2>B_X-A_X^2$; in that range it requires
$$V<m\left(A_X-\sqrt{\frac{B_X-A_X^2}{m}}\right)^2.$$
For fixed $m$ this range eventually fails, so the criterion is vacuous. For $m$ large enough to enter the nonvacuous range, the Gram estimate still gives $V/m\le(1+1/m+o(1))B_X$, whereas the criterion requires the *mean squared increment* $V/m$ to be below $\left(A_X-\sqrt{(B_X-A_X^2)/m}\right)^2$, which approaches the $A_X^2$ scale when $m\gg B_X/A_X^2$. The available upper bound is larger by roughly $B_X/A_X^2\asymp X^{1/2}(\log X)^{100}$. Thus the global fourth moment plus this Gram inequality does not certify the required increment bound; it has not supplied the missing saving. The cited conditional input is unchanged and still allows an isolated exceptional target.

On a selected resonant arc, the geometric factor can be cubic in its width. But $B_E$ must also be bounded on that arc, and the contribution of the rest of $\mathfrak m$ must be controlled with its sign. Li–Liu's cited bound is for the complete minor arcs and does not provide the required target-specific signed estimate or the local fourth-moment profile needed for this decomposition.

## 5. Countermodels, hypotheses, and unresolved theorem

The nonresonant example $q=3,j=2$ refutes the claim that every rational arc gives a small multiplier for small shifts. The full-minor-set measure calculation refutes the claim that merely removing major-arc cores creates an asymptotic operator-norm saving for fixed shifts. Both are geometric counterexamples to proposed inferences, not counterexamples to Goldbach.

The fourth-moment input discussed here is H. Li and Z. Liu, *Fourth moments of prime exponential sums and exceptional sets for sums and differences of primes*, arXiv:2610.26756v1 (2026), Theorems 1–2 and Proposition 4.1, as recorded in the Stage 64 source audit. Its hypotheses include a fixed smooth real weight $w\in C_c^\infty((0,1))$, $0\le w\le1$, with $w=1$ on $[1/8,7/8]$ and the paper's specified logarithmic Gevrey regularity; arcs with $P=X^\kappa$, reduced centers $a/q$, $q\le P$, and radius $P/(qX)$; and a single uniform hypothesis that every nontrivial zero of every primitive Dirichlet $L$-function, including $\zeta$, has real part at most $\Theta$, uniformly in conductor and height. The fourth-moment theorem assumes a fixed $1/2\le\Theta<11/12$ and uses its corresponding $\kappa=\kappa(\Theta)\in(4/9,9/20)$; Proposition 4.1 has its own stated main-term hypotheses. The exceptional-set estimate allows a singleton. The Stage 64 literature audit was inherited, not refreshed in Stage 67, and no external claim is strengthened here.

The first missing analytic theorem is one of the following genuinely prime-only inputs, with explicit dependence on $X$, $N$, shifts, weight, arcs and zero-free hypotheses:

1. a target-uniform bound for the signed vector $\bigl(\Delta_j(N)\bigr)_{j\in J}$ whose squared norm is below the exact Stage 66 exclusion threshold; or
2. a localized fourth-moment profile on a partition of the full minor set, together with signed control of all nonresonant pieces, strong enough to yield the same bound.

An estimate only on resonant arcs, modular admissibility modulo $210$, or an average over targets does not imply either statement. The residual set remains $H=\{N\ge4:N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\}$. Its remaining distinct-prime case is not assumed in any identity or estimate in this report.

## 6. Exact verification and reproducibility

From the repository root run:

```text
python3 -B results/stage67/verify_rational_arc_gram.py
sage -python results/stage67/verify_rational_arc_gram_sage.py
```

The Python verifier uses exact rational coefficients in sparse cyclotomic group rings and checks the arc expansion, reduced-center criterion, rank-one center identities, full-circle Gram entries, and major-arc measure inequalities. The independent SageMath verifier uses cyclotomic number fields and a formal variable for $1/(2\pi i)$ to check exact interval matrices and Hermitian symmetry. The proofs above establish the all-parameter identities; the scripts are finite regression checks only. Ranges, run data, and SHA-256 hashes are recorded in `verification_manifest.json`.
