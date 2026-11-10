# Stage 69 M6 — Sharp target criterion, exact-energy correction, and source-scale gaps

**Verdict:** The advertised Stage 66 inequality is valid and sharp when the input is an upper bound on total shift energy. If the shift energy is fixed exactly, the same lower bound remains valid but ceases to be sharp above $V=mA^2$. The exact fixed-energy extremal value is derived below. This distinction repairs the M6a equality request; it does not supply a prime-specific estimate.

## 1. Setup and the exact pointwise statement

Let $c\in\ell^2(\mathbb Z;\mathbb C)$, fix a center $N$ and $m$ distinct nonzero shifts $j_1,\ldots,j_m$. Put

$$z=c(N),\quad d_i=c(N+j_i)-z,\quad V=\sum_{i=1}^m|d_i|^2,\quad B=\sum_n|c(n)|^2,$$

and assume $|z|\ge A>0$. Since all $m+1$ indices are distinct,

$$B\ge |z|^2+\sum_i|z+d_i|^2. \tag{6.1}$$

### The valid Stage 66 lower bound

For every actual value $V\ge0$,

$$\boxed{B\ge A^2+(\sqrt m A-\sqrt V)_+^2
=A^2+m\left(A-\sqrt{V/m}\right)_+^2.} \tag{6.2}$$

For $V\le mA^2$, this lower bound is the **exact minimum** over all admissible sequences with that exact $V$. For $V>mA^2$, (6.2) remains valid but is not the exact minimum.

### Proof 1: scalar convexity/Jensen

Write $x=|z|$ and $t_i=|d_i|^2$. Reverse triangle gives $|z+d_i|\ge(x-\sqrt{t_i})_+$. The function $f_x(t)=(x-\sqrt t)_+^2$ is convex on $[0,\infty)$: on $0<t<x^2$ its second derivative is $x/(2t^{3/2})>0$, and at $x^2$ its derivative joins continuously to zero. Hence

$$\sum_i|z+d_i|^2\ge\sum_i f_x(t_i)\ge m f_x(V/m).$$

The function $x\mapsto x^2+m(x-\sqrt{V/m})_+^2$ is increasing for $x\ge0$. Since $x\ge A$, this proves (6.2).

### Proof 2: projection in the shift space

In $\mathbb C^m$, let $u=z(1,\ldots,1)$ and $d=(d_1,\ldots,d_m)$. Then $\|u\|=\sqrt m|z|$, $\|d\|=\sqrt V$, and (6.1) gives

$$B\ge |z|^2+\|u+d\|^2\ge |z|^2+(\sqrt m|z|-\sqrt V)_+^2.
$$

The final expression is increasing in $|z|$, proving (6.2). This derivation is independent of Jensen.

## 2. Sharpness and equality: exact energy versus an upper bound

### Exact $V$ fixed

For fixed center magnitude $x\ge A$ and fixed $\|d\|=\sqrt V$, the exact minimum of $\|x\mathbf1+d\|$ is $|\sqrt{m}x-\sqrt V|$, attained when $d$ is collinear with $-x\mathbf1$. Thus minimizing (6.1) over $x\ge A$ reduces exactly to

$$\min_{x\ge A}\left[x^2+(\sqrt V-\sqrt m x)^2\right].$$

The unconstrained minimizer is $x_0=\sqrt{mV}/(m+1)$. Therefore the exact minimum is

$$\boxed{\mathcal E_m(A,V)=
\begin{cases}
A^2+(\sqrt V-\sqrt m A)^2,&0\le V\le A^2(m+1)^2/m,\\
V/(m+1),&V\ge A^2(m+1)^2/m.
\end{cases}} \tag{6.3}$$

This is attained by a sequence supported only at the center and the $m$ neighbors. If $V\le mA^2$, (6.3) is precisely (6.2); equality requires $|z|=A$, all $d_i$ equal in magnitude $\sqrt{V/m}$ and directed opposite to $z$, and all coefficients outside the block zero. At $V=mA^2$, the neighbors are all zero. If $mA^2<V<A^2(m+1)^2/m$, equality in the sharper exact-energy minimum still has $|z|=A$ and common $d_i=-\sqrt{V/m}\,z/A$; (6.2) is then strictly weaker. At and above the upper breakpoint, the exact minimizer has $|z|=x_0>A$ and collinear increments; again (6.2) is strict.

In particular, for exact $V>mA^2$, (6.2) reduces to $B\ge A^2$ and cannot be an equality: equality would force every neighbor and all other coefficients to vanish, which forces $V=m|z|^2\ge mA^2$; equality with $B=A^2$ further forces $|z|=A$ and hence $V=mA^2$, a contradiction.

### Only $V\le\overline V$ known

The exact minimum over the larger class $0\le V\le\overline V$ is

$$\min_{0\le V\le\overline V}\mathcal E_m(A,V)=
\begin{cases}
A^2+(\sqrt{m}A-\sqrt{\overline V})^2,&\overline V\le mA^2,\\
A^2,&\overline V\ge mA^2.
\end{cases} \tag{6.4}$$

Thus the Stage 66 formula with $V$ replaced by an **upper bound** $\overline V$ is sharp for every $\overline V$, including $\overline V\ge mA^2$: the extremizer uses actual energy $V=mA^2$, not $V=\overline V$, and has a nonzero center with all listed neighbors zero. The phrase “sharp with exact energy $V$” above this boundary would be false. Equation (6.4), which is the version relevant to certified upper bounds, is sharp in the unrestricted $\ell^2$ class. No prime-specific separation from its extremizer is known here.

## 3. Exact finite tradeoff and strict boundary cases

Suppose certified data give $B\le\overline B$ and $V\le\overline V$. A center with $|c(N)|\ge A$ is impossible if

$$F_m(A,\overline V):=A^2+m\left(A-\sqrt{\overline V/m}\right)_+^2>\overline B. \tag{6.5}$$

Equality in (6.5) is **not** enough for contradiction. The full finite classification is:

* If $\overline B<A^2$, the center is already impossible, independent of $V$ and shifts.
* If $\overline B=A^2$, (6.5) holds exactly when $\overline V<mA^2$.
* If $\overline B>A^2$, put $K=\overline B-A^2$. A useful $m$ exists only if $K<mA^2$; for such $m$, (6.5) is equivalent to
  $$\overline V<m\left(A-\sqrt{K/m}\right)^2.$$
  At equality, no contradiction follows. If $K\ge mA^2$, even the maximum value $(m+1)A^2$ at $\overline V=0$ does not strictly exceed $\overline B$.

For fixed $A,\overline B,\overline V$ with $K>0$, the least positive integer $m$ satisfying (6.5) is

$$m_{\min}=\left\lfloor\frac{(\sqrt{\overline V}+\sqrt K)^2}{A^2}\right\rfloor+1.$$

For $K=0$, it is $m_{\min}=\lfloor\overline V/A^2\rfloor+1$. For $K<0$, no shift is needed. These expressions incorporate strictness when the threshold is an integer. For an arithmetic application, $m$ cannot be made arbitrarily large without regard to parity, target interval, distinctness, and uniformity of the estimates; a block inside $[X/2,X]$ contains only $O(X)$ even targets.

## 4. Robust main-term and prime-power errors

Let $C_N$ be a nonnegative von Mangoldt convolution coefficient and let $P_N$ be the genuine-prime coefficient using the same weight. Write the exact decomposition

$$C_N=P_N+D_N,\qquad D_N\ge0,$$

where $D_N$ consists of pairs for which at least one coordinate is a higher prime power (and, if the target is not in $H$, any excluded diagonal convention is included explicitly). Suppose the analytic decomposition is

$$C_N=M_N+\eta_N+\mu_N,$$

where $M_N$ is a known complex main term, $|M_N|\ge M_X$, $|\eta_N|\le E_X$, $\mu_N$ is the signed minor coefficient, and $D_N\le D_X$. If $P_N=0$, then

$$|\mu_N|=|D_N-M_N-\eta_N|\ge M_X-E_X-D_X.$$

So the correct threshold is

$$A_X=M_X-E_X-D_X,$$

provided it is positive. It is **not** $M_X-E_X-2D_X$: the nonprime-power correction occurs once in $P=C-D$. A second copy would be justified only if the source's stated major term had itself already subtracted a correction of size $D_X$ and one then subtracted another distinct correction; that is a different convention and must be written as a separate identity.

For $0\le w\le1$ supported on $(0,X]$, uniformly for $N\le2X$, the elementary count of higher prime powers in $(0,X]$ is $O(\sqrt X)$; each product weight is at most $(\log X)^2$. By a union bound over the two coordinates,

$$0\le D_N\ll \sqrt X(\log X)^2.$$

This bound is deliberately crude but sufficient to show the correction is lower order than a major term of size $\asymp X$. It does not improve the minor moment and is not needed if the exponential sum is defined directly over genuine primes. If $M_X\le E_X+D_X$, this robust certificate gives no positive center threshold.

## 5. Target-localized Cauchy, Gram, and additive-energy alternatives

For the genuine-prime polynomial $S_w$ and minor set $\mathfrak m$, put

$$m_w(n)=\int_{\mathfrak m}S_w(\alpha)^2e(-n\alpha)\,d\alpha.$$

Cauchy and Parseval give, respectively,

$$|m_w(N)|\le |\mathfrak m|^{1/2}\left(\int_{\mathfrak m}|S_w|^4\right)^{1/2},\qquad
\sum_{n\in\mathbb Z}|m_w(n)|^2=\int_{\mathfrak m}|S_w|^4. \tag{6.6}$$

The second equality is a positive additive-energy identity. It is a global coefficient norm and has no target label.

For $m$ shifts let $g_j(\alpha)=e(-j\alpha)-1$ and

$$\Delta_j(N)=m_w(N+j)-m_w(N)=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)g_j(\alpha)\,d\alpha.$$

The exact Gram operator bound is

$$\sum_{j\in J}|\Delta_j(N)|^2\le B_X\lambda_{\max}(G),\quad
G_{ij}=\int_{\mathfrak m}\overline{g_i(\alpha)}g_j(\alpha)\,d\alpha,
\quad B_X=\int_{\mathfrak m}|S_w|^4. \tag{6.7}$$

Since $\operatorname{tr}G\le4m$, this only yields $V/m\le4B_X$. Under the Li–Liu conditional bound $B_X\ll X^{5/2}(\log X)^{100}$, it is larger than the natural $A_X^2\asymp X^2$ scale by $X^{1/2}(\log X)^{100}$. It cannot meet (6.5). This is a valid estimate, not a cancellation argument: the phase $e(-N\alpha)$ disappears in the operator norm. A signed/bilinear improvement must keep it before taking absolute values and must exploit a proved prime-specific correlation; no such saving is obtained here.

The pointwise Cauchy bound from the same moment is $O(X^{5/4}(\log X)^{50})$, while the major coefficient is $\gg_w X$. The ratio is $O(X^{1/4}(\log X)^{50})$, so it also fails by a power of $X$. A generic coefficient one-hole model is sharp for the moment-only input, but it is not a counterexample made from actual primes.

## 6. Quantitative regimes and what would close the criterion

Let $A_X\asymp c_wX$ and $B_X\le C_4X^{5/2}(\log X)^{100}$. Then

$$\frac{B_X}{A_X^2}\le \frac{C_4}{c_w^2}X^{1/2}(\log X)^{100}. \tag{6.8}$$

For $V=0$, one needs $m+1>B_X/A_X^2$. For positive $\overline V$, the exact requirement is the one in (6.5); if $K=B_X-A_X^2>0$, it requires

$$\frac{\overline V}{m}<A_X^2\left(1-\sqrt{\frac{K}{mA_X^2}}\right)^2,
\quad m>K/A_X^2. \tag{6.9}$$

The unconditional minor-moment baseline quoted in Li–Liu is $X^{31/12+\epsilon}$ (from the cited Maynard–Pandey–Radziwiłł result); its ratio to $A_X^2$ is $X^{7/12+\epsilon}$, also divergent. We have not independently re-proved that external moment theorem. The Li–Liu $X^{5/2}$ saving is conditional on the fixed common zero hypothesis $Q_\Theta$, $\Theta<11/12$, with their fixed smooth weight and $\kappa(\Theta)\in(4/9,9/20)$. Neither estimate is target-signed.

An idealized sufficient input is a uniform genuine-prime estimate for $V_{N,J}$ strong enough to satisfy (6.9) for each residual target, for a shift set of admissible size and with all constants uniform in $N$. This is strictly weaker in formal statement than $R(N)>0$ only if proved independently; asserted as a hypothesis it merely packages a new arithmetic burden. A still more direct sufficient input is $|m_w(N)|<a_w(N)$ at each residual target, but that is essentially the pointwise obstruction itself. No published source audited in M5 supplies (6.9).

## 7. Exact verification and verdict

`verify_stage69_m6.py` uses exact SymPy algebra and rational substitutions to check the identity of the two forms of (6.2), the piecewise exact-energy envelope (6.3), the upper-bound sharpness boundary at $\overline V=mA^2$, and the strict finite-$m$ threshold. The independent `verify_stage69_m6.sage` repeats the fixed-energy branch and upper-bound equality checks in Sage's exact real algebraic field. These checks validate displayed algebra, not a prime-correlation estimate.

**M6 conclusion:** The deterministic certificate is fully derived and its two notions of sharpness are now separated. The power/log gap remains: available moment information is too large by $X^{1/2}(\log X)^{100}$ in squared energy, while the target Cauchy amplitude loses $X^{1/4}(\log X)^{50}$. The missing theorem is a target-uniform signed estimate or shift-energy saving for the genuine-prime minor coefficient, proved without selecting any representation of the target.
