# Stage 68 M3 — arc budgets, pointwise threshold, and feasibility

## Exact allocation and its collapse under a global moment

For a disjoint partition $\mathfrak m=\bigsqcup_rE_r$, write $B_r=\int_{E_r}|S_w|^4$ and $G_r=G_{E_r}$. If independently proved upper bounds $B_r\le\bar B_r$ are available, Theorem 1 gives
\[
V(N)=\sum_{j\in J}|\Delta_j(N)|^2\le
\left(\max_{\|z\|=1}\sum_r\sqrt{\bar B_r}\sqrt{z^*G_rz}\right)^2=\bar V.
\]
The same partition must be used in the moment integrals and every increment. If only $\sum_rB_r\le B$ is known, optimize over allocations. For fixed unit $z$, set $q_r=z^*G_rz\ge0$. Then
\[
\max_{B_r\ge0,\,\sum B_r\le B}\sum_r\sqrt{B_rq_r}
=\sqrt{B\sum_rq_r},
\]
with equality at $B_r=Bq_r/\sum_sq_s$ when the denominator is positive. If all $q_r=0$ or $B=0$, both sides are zero. Maximizing over $z$ yields exactly $\sqrt{B\lambda_{\max}(\sum_rG_r)}$. Hence partitioning without a nontrivial independent allocation profile adds no information.

## Strict pointwise certificate

Let $r_w(N)=a_w(N)+m_w(N)$ be the full, major, and minor coefficients. Assume $w\ge0$, $N\in H$, an independent theorem gives $a_w(N)\ge A_X>0$, and independent estimates give total minor energy $\int_{\mathfrak m}|S_w|^4\le\bar B$ and increment energy $V(N)\le\bar V$. If $R(N)=0$, then the full weighted coefficient is zero, so $m_w(N)=-a_w(N)$ and $|m_w(N)|\ge A_X$. Parseval and the sharp Stage66 aggregate inequality then imply
\[
\bar B\ge\|m_w\|_{\ell^2}^2\ge A_X^2+m\left(A_X-\sqrt{\bar V/m}\right)_+^2.
\]
Therefore strict inequality of the right side over $\bar B$ implies $R(N)>0$. This is non-circular because the zero-representation hypothesis is used only to derive a contradiction; it is not used in either analytic input. If an arc piece is not reflection symmetric, its Fourier coefficient may be complex; the argument uses modulus at the center and only a real-part sign after symmetric pairing. A complex piece cannot separately be called positive. If $w$ changes sign, the full coefficient is not a nonnegative weighted representation count, so the implication to $R(N)$ fails.

## Quantitative scale ledger

The inherited conditional Li–Liu theorem supplies only $\bar B\ll C_BX^{5/2}(\log X)^{100}$ on the complete minor set. The major coefficient has scale $A_X\ge c_AX$ in its applicable target range. Even with $\bar V=0$, the best lower energy is $(m+1)A_X^2$, so a necessary possibility for (F) is
\[
m+1>\bar B/A_X^2\asymp (C_B/c_A^2)X^{1/2}(\log X)^{100}.
\]
For $\bar B>A_X^2$ and $m>(\bar B-A_X^2)/A_X^2$, (F) requires
\[
\bar V<m\left(A_X-\sqrt{(\bar B-A_X^2)/m}\right)^2.
\]
As $m/(\bar B/A_X^2)\to\infty$, this demands $\bar V/m\lesssim A_X^2\asymp X^2$, while the global Gram bound gives only $V/m\le(1+1/m)\bar B\asymp X^{5/2}(\log X)^{100}$. The missing saving is a factor of order $X^{1/2}(\log X)^{100}$. Thus the necessary shift count is already of square-root scale with the full logarithmic loss, and increasing it does not repair the available bound. For meaningful local variation choose distinct even shifts $j=2h$, with $N+j$ inside the coefficient support range (for the stated weight, pair sums lie below $2X$); the energy theorem itself allows all integer indices, but large shifts do not encode local behavior.

## Resolved budget candidate and phase alternative

One explicit disjoint candidate is the nearest-rational partition. For $P=X^\kappa$, take all reduced centers $a/q$ with $q\le P$; assign every minor point to its nearest center, breaking ties lexicographically, then put it in shell $s\ge0$ when
\[
2^sP/(qX)\le\|\alpha-a/q\|<2^{s+1}P/(qX).
\]
The sets $E_{a/q,s}$ are disjoint and cover the minor set; the last shell can be truncated at the largest possible distance. Define $B_{a/q,s}=\int_{E_{a/q,s}}|S_w|^4$. The global result bounds only $\sum_{a/q,s}B_{a/q,s}$, which collapses exactly as above. A profile useful for (F) must provide upper bounds whose resulting $\bar V$ is below the displayed threshold, uniformly in each target; merely proving $B_{a/q,s}=o(B)$ for each fixed bin is insufficient when the number of bins grows. No such profile was located or proved here.

A phase condition could in principle be less restrictive than tiny energy: if the complex arc coefficients $c_r(N)$ sum to a real number and one proves $\sum_r\Re c_r(N)>-a_w(N)$, then $r_w(N)>0$. But this is exactly the signed positivity condition in the decomposition, not a weaker independent sufficient condition. A verifiable stronger condition such as $|\sum_rc_r(N)|\le(1-\delta)A_X$ with $a_w(N)\ge A_X$ implies positivity, but is stronger in magnitude than what is logically needed and has no known independent proof. Rephrasing the desired sign as a phase hypothesis does not create new arithmetic information.

| Candidate input | What it proves | Status |
|---|---|---|
| Global fourth moment only | Exceptional-set energy; no prescribed target bound | EXTERNAL CONDITIONAL theorem; insufficient |
| Total energy redistributed among disjoint arcs | Same operator bound as one global piece | PROVED collapse |
| Uniform localized budget profile below (F) threshold | Would exclude a zero target | OPEN arithmetic estimate |
| Arc phase cancellation sufficient for positivity | Directly excludes a zero target | Logically equal/stronger reformulation; OPEN |

The exact unresolved premises are listed in `04_proof_obligations.json`.
