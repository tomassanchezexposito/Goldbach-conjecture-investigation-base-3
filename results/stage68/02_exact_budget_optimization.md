# Stage 68 M1 — exact arc-budget optimization

## Theorem 1: exact optimum and first proof

Let $E_1,\ldots,E_R$ be pairwise disjoint measurable subsets of $\mathbb T$, let $J$ be a finite set of $m$ distinct nonzero integers, and set
\[
g_j(\alpha)=e(-N\alpha)(e(-j\alpha)-1),\qquad
(G_r)_{jk}=\int_{E_r}g_j\overline{g_k}.
\]
For specified $B_r\ge0$, define $D_r(f_r)_j=\int_{E_r}f_rg_j$ on the complex Hilbert ball $\|f_r\|_2^2\le B_r$. Then
\[
U:=\sup_{\|f_r\|^2\le B_r}\left\|\sum_rD_r(f_r)\right\|_2
=\max_{\|z\|_2=1}\sum_r\sqrt{B_r}\sqrt{z^*G_rz}.\tag{1}
\]

For any vector $v\in\mathbb C^m$, $\|v\|=\max_{\|z\|=1}|\sum_j\overline z_jv_j|$. Fix $z$. The functional on piece $r$ is $\int f_r h_z$ with $h_z=\sum_j\overline z_jg_j$, and
\[
\|h_z\|_{L^2(E_r)}^2=z^*G_rz.
\]
Cauchy–Schwarz is exact: if the norm is nonzero take $f_r=\sqrt{B_r}\,\overline{h_z}/\|h_z\|_2$; if it is zero, any admissible $f_r$, including zero, contributes zero. Every piece can attain the same phase, so the support function of the product of balls is the sum in (1). Taking the maximum over compact unit sphere gives (1). Zero budgets and singular Grams are covered by the same convention.

## Second derivation: ellipsoid images and Minkowski support

Use $\langle u,v\rangle=\int u\bar v$ (linear in the first slot). The map $D_r:L^2(E_r)\to\mathbb C^m$ is bounded, with
\[
D_r^*z=\sum_jz_j\overline{g_j},\qquad D_rD_r^*=G_r.
\]
Therefore the image of the radius-$\sqrt{B_r}$ ball is a compact, centered, possibly degenerate ellipsoid $K_r$ in finite-dimensional $\mathbb C^m$, whose support function in direction $z$ is $\sqrt{B_r}\sqrt{z^*G_rz}$. The image of the product domain is the Minkowski sum $K_1+\cdots+K_R$. For a compact convex set $K$, $\max_{x\in K}\|x\|=\max_{\|z\|=1}h_K(z)$: one inequality follows from $\|x\|=\max_{\|z\|=1}|\langle x,z\rangle|$, and the reverse follows by selecting a norm-maximizer $x$ and $z=x/\|x\|$. Support functions add under Minkowski sums, yielding (1). Singular-vector extremizers in each $D_r$ realize the support value; the displayed $f_r$ gives them explicitly. This proof factors through finite-dimensional output ellipsoids rather than optimizing the input functionals one at a time.

## Triangle bound and exact equality condition

Since $z^*G_rz\le\lambda_r:=\lambda_{\max}(G_r)$,
\[
U\le\sum_r\sqrt{B_r\lambda_r}.\tag{2}
\]
Equality holds iff there exists a unit $z$ belonging to every top eigenspace $\ker(G_r-\lambda_rI)$ for which $B_r>0$ and $\lambda_r>0$. No condition is imposed by a zero budget or a zero matrix. Necessity follows because a maximizing $z$ exists and equality in a sum of nonnegative termwise upper bounds forces each active Rayleigh quotient to be maximal; sufficiency is immediate. This includes nonunique top eigenspaces exactly: their intersection must contain a unit vector.

## Strictness for the actual interval multipliers

An abstract illustration is $G_1=\operatorname{diag}(1,0)$, $G_2=\operatorname{diag}(0,1)$, $B_1=B_2=1$. Formula (1) gives $\max_{|z_1|^2+|z_2|^2=1}(|z_1|+|z_2|)=\sqrt2$, whereas (2) is 2.

There is also an actual interval-Gram example. Let $J=\{1,2\}$ and take the disjoint arcs $E_0=[-1/8,1/8]$ and $E_{1/2}=[3/8,5/8]$ on $\mathbb T$. Direct integration of $\mu_E(n)=e(nc)\sin(\pi n/4)/(\pi n)$ gives
\[
G_0=\begin{pmatrix}\frac12-\frac{\sqrt2}{\pi}&b\\b&\frac12-\frac1\pi\end{pmatrix},\quad
G_{1/2}=\begin{pmatrix}\frac12+\frac{\sqrt2}{\pi}&b\\b&\frac12-\frac1\pi\end{pmatrix},\quad b=\frac14-\frac1{2\pi}>0.
\]
Each top eigenvalue is simple since its off-diagonal is nonzero. Their commutator has $(1,2)$ entry $-2\sqrt2 b/\pi\ne0$, so the matrices cannot share an eigenvector. Thus (2) is strictly larger than (1) for $B_0=B_{1/2}=1$. The Python/SymPy and independent Sage verifiers check these exact matrices and commutator; $b>0$ follows from $\pi>3$.

## Certified relaxations, and a relaxation that is not exact

For any $t_r>0$ with $\sum_rt_r=1$, Cauchy–Schwarz gives
\[
\left(\sum_r\sqrt{B_rq_r}\right)^2\le\sum_r\frac{B_r}{t_r}q_r,
\quad q_r=z^*G_rz.
\]
Consequently
\[
U^2\le\inf_{t_r>0,\,\sum t_r=1}\lambda_{\max}\left(\sum_r\frac{B_r}{t_r}G_r\right).\tag{3}
\]
This is a valid computable upper certificate; zero terms are handled by deleting zero $B_rG_r$ terms and taking boundary limits. It is not asserted to be sharp in general. Nor is the maximization in (1) generally an SDP obtained by lifting $zz^*$: replacing rank-one $X=zz^*$ by all $X\succeq0$, $\operatorname{tr}X=1$ can increase the objective. In the orthogonal rank-one example, this relaxation gives $\max_X(\sqrt{X_{11}}+\sqrt{X_{22}})=2$, while the true value is $\sqrt2$. That is an exact relaxation gap.

## Arithmetic scope

For the prime input $f=1_E S_w^2e(-N\alpha)$, (1) remains a valid upper bound on increments. The unrestricted extremizers need not equal a prime-square input, and the theorem supplies no signed lower bound on its target coefficient. The improvement over Stage 67 is an exact allocation formula, an equality criterion, and proof that matrix nonalignment can occur for genuine interval multipliers—not a Goldbach estimate.
