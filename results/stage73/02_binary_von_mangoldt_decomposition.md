# Stage 73 — Exact binary von Mangoldt decomposition

All weights and support conventions are those in 01. Extend $\Lambda(n)=0$ for integers $n\le0$ and write $\Lambda(p^k)=\log p$, $k\ge1$. No target prime pair is assumed.

## 1. Audited prime-power correction

Let $T(\alpha)=\sum_{n\ge1}\Lambda(n)w(n/X)e(n\alpha)$ and
$$G_X(N)=\int T(\alpha)^2e(-N\alpha)d\alpha
=\sum_{n\in\mathbb Z}\Lambda(n)\Lambda(N-n)w(n/X)w((N-n)/X).$$
Set $Q=T-S$; its coefficients $q_n$ are nonnegative proper powers. For each base $p\le\sqrt X$, the sum of its proper-power logarithmic weights is at most $M\log X$. Hence $\sum q_n\le M\pi(\sqrt X)\log X$ and $\max_n[T]_n\le M\log X$. The ordered union bound gives
$$0\le G_X(N)-r_X(N)\le2\sum_n q_n[T]_{N-n}
\le2M^2\pi(\sqrt X)(\log X)^2.$$
This proves the Stage 72 elementary bound $2M^2\lfloor\sqrt X\rfloor\log^2X$. Any rigorously valid Chebyshev constant $C_{\rm Ch}$ with $\pi(y)\le C_{\rm Ch}y/\log y$ for $y\ge2$ yields
$$D_X:=4C_{\rm Ch}M^2\sqrt X\log X,\qquad0\le G-r\le D_X\quad(X\ge16).$$
There is no missing factor of two: the right side double-counts terms with two proper-power entries, which is allowed in an upper bound. An exact alternative is $G-r=2(s*q)(N)+(q*q)(N)$. We reproduce the proof; no new improvement over Stage 72 is claimed. It is uniform in all integer $N$, including outside $H$.

## 2. T73.3 — correctly truncated Vaughan identity, including boundary term

Dirichlet convolution is denoted by $*$, the constant arithmetic function by $\mathbf1$ and the convolution identity by $\varepsilon=1_{n=1}$. Put $\mu_1=\mu1_{n\le U}$, $\mu_2=\mu1_{n>U}$, $\Lambda_1=\Lambda1_{n\le V}$, $\Lambda_2=\Lambda1_{n>V}$, for real $U,V\ge1$. Then for EVERY $n\ge1$,
$$\boxed{\Lambda=\Lambda_1+\mu_1*\log-\mu_1*\mathbf1*\Lambda_1+\mu_2*\mathbf1*\Lambda_2.}$$
**Proof 1:** $\log=\mathbf1*\Lambda$ and $\mu*\mathbf1=\varepsilon$. Expand $\mu*\mathbf1*\Lambda$, split $\mu$ and $\Lambda$, and combine $\mu_2*\mathbf1*\Lambda_1=\Lambda_1-\mu_1*\mathbf1*\Lambda_1$. This proves the identity including $n=1$, primes, powers, and $n=U,V$ when integral.

**Independent proof 2:** the two Type I terms combine to $\mu_1*\mathbf1*\Lambda_2$. Adding the Type II term gives $\mu*\mathbf1*\Lambda_2=\Lambda_2$, and adding the boundary term returns $\Lambda$. This checks the sign of the subtracted term without relying on a numerical fit. These are algebraic proofs of the standard identity, not a new literature theorem.

For definiteness take $U=V=\max(1,\lfloor X^{1/5}\rfloor)$. Retain all exact products below; no rectangular approximation is made. Define
$$F_N(n)=\Lambda(N-n)w(n/X)w((N-n)/X),\qquad
b_U(k)=\sum_{d\mid k,\ d>U}\mu(d)=\varepsilon(k)-\sum_{d\mid k,\ d\le U}\mu(d).$$
In particular $b_U(k)=0$ for $k\le U$ (including 1), and $|b_U(k)|\le\tau(k)$. Exact substitution gives
$$G_X(N)=A_0(N)+A_1(N)-A_2(N)+A_3(N),$$
$$A_0=\sum_{n\le V}\Lambda(n)F_N(n),$$
$$A_1=\sum_{d\le U}\mu(d)\sum_{k\ge1}\log k\,F_N(dk),$$
$$A_2=\sum_{d\le U,m\le V}\mu(d)\Lambda(m)\sum_{k\ge1}F_N(dmk),$$
$$A_3=\sum_{k>U,m>V}b_U(k)\Lambda(m)F_N(km).$$
Every inner sum has $\sigma X\le n\le\rho X$, $\sigma X\le N-n\le\rho X$ inherited from $F_N$, hence $n<N$ and $n<X$. The sums are finite. $A_0$ vanishes only once $V<\sigma X$; it is retained at finite scales. All $\Lambda(m)$ and $\Lambda(N-km)$ retain proper powers until the full correction is applied. The support in $A_3$ is hyperbolic, not an unrestricted rectangle.

## 3. Concrete Type I error and the Type II obstruction

Write $h_N(t)=w(t/X)w((N-t)/X)$, smooth and compactly supported with $\|h_N\|_\infty\le M^2$ and total variation bounded independently of $X,N$. The Type I inner sums use moduli $d\le U$ or $l=dm\le UV\le X^{2/5}$. For $(N,l)=1$, define
$$\mathcal E_l(N;h)=\sum_{k\ge1}\Lambda(N-lk)h(lk)-\frac1{\varphi(l)}\int_\mathbb R h(t)dt.$$
This definition is exact: it states the expected AP main term and its unknown error. For $A_1$ use $h(t)=h_N(t)\log(t/d)$ on its compact positive support; for $A_2$ use $h_N$. Summation by parts bounds $\mathcal E_l$ by a fixed (or $O_w(\log X)$) total-variation factor times the maximum AP $\psi$ error over endpoints at most $X$. No boundary term is omitted: extend $h$ by zero, integrate the step function against $h'$, and its endpoint contributions vanish. For $(N,l)>1$, a nonzero $\Lambda(N-lk)$ must be a power of a prime dividing $(N,l)$. These finitely supported terms must be kept separately; the reduced-class main term cannot be applied there.

### T73.5 — close the Type I error before naming the remaining gap

Group $A_2$ by $l=dm$ and put $c_l=\sum_{dm=l,d\le U,m\le V}\mu(d)\Lambda(m)$. The coefficient loss is only logarithmic:
$$|c_l|\le\sum_{m\mid l}\Lambda(m)=\log l.$$
This elementary bound removes the need to assume an additional divisor-weighted distribution theorem here. Define
$$\mathcal D(X,Q)=\sum_{l\le Q}\max_{(a,l)=1}\sup_{0\le y\le X}|\psi(y;l,a)-y/\varphi(l)|,\quad Q=UV,$$
and the explicit Type I main term
$$\mathcal M_I(N)=\int h_N(t)\left[\sum_{d\le U,(d,N)=1}\frac{\mu(d)}{\varphi(d)}\log(t/d)
-\sum_{l\le UV,(l,N)=1}\frac{c_l}{\varphi(l)}\right]dt.$$
For sufficiently large $X$ with $U=V=\lfloor X^{1/5}\rfloor$,
$$\boxed{|A_1-A_2-\mathcal M_I|\ll_w\log(2X)\mathcal D(X,Q)+Q\log^3(2X).}$$
**Proof:** reduced-class inner errors are bounded by summation by parts as above. For $A_1$, the variation of $h_N(t)\log(t/d)$ is $O_w(\log X)$ uniformly in $d\le U$. For grouped $A_2$, the variation of $h_N$ is $O_w(1)$ and $|c_l|\le\log l$. Sum those errors over moduli. For $(N,l)>1$, every surviving $N-lk$ is a power of a prime dividing $N$. For each such prime its total $\Lambda$ mass up to $X$ is at most $\log X$. Thus the nonreduced inner sum is $O_w(\omega(N)\log X)=O_w(\log^2 X)$; the extra logarithm in $A_1$ or $c_l$ costs at most $O(\log X)$. There are at most $Q$ moduli. This proves the displayed bound; all constants are uniform in $N\in[X/2,X]$. $A_0=0$ once $V<\sigma X$.

Classical maximal-endpoint Bombieri–Vinogradov implies $\mathcal D(X,X^{2/5})\ll_A X\log^{-A}X$ for every fixed $A$. To keep the inspected source honest, its nonmaximal Theorem 17 also suffices here after the following elementary reduction. Choose a mesh of spacing at most $X/\log^C X$, with its first positive endpoint comparable to that spacing. Apply the endpoint theorem at each of $O(\log^C X)$ endpoints; $X^{2/5}<\sqrt y/\log^B y$ at every positive mesh endpoint for all sufficiently large $X$. The source centers at $\varphi(l)^{-1}\sum_{n\le y,(n,l)=1}\Lambda(n)$. Removing the coprimality condition changes its numerator by at most $\omega(l)\log X=O(\log^2X)$, since only powers of primes dividing $l$ contribute. Summing this divided by $\varphi(l)$ costs $O(\log^4X)$ per mesh endpoint, negligible after any fixed polylogarithmic number of endpoints. Classical quantitative PNT then replaces the complete mass by $y$ with any desired logarithmic saving. Monotonicity of $\psi(y;l,a)$ between successive mesh endpoints bounds its discrepancy by the larger endpoint error plus the spacing divided by $\varphi(l)$. The sum of those interpolation terms is $O(X\log^{2-C}X)$, since $1/\varphi(l)\le\tau(l)/l$ and $\sum_{l\le Q}\tau(l)/l\ll\log^2(2Q)$. The region below the first endpoint uses the same monotonicity and zero value at 0. Choose $C>A+3$ and the source saving exponent larger than $A+C+3$. This proves the required maximal form in this restricted polynomial range, using established BV and quantitative PNT only. No effective numerical cutoff is computed.

Therefore for every fixed $A>0$ the Type I reduction is unconditionally
$$G_X(N)=\mathcal M_I(N)+A_3(N)+O_{A,w}(X\log^{-A}X+X^{2/5}\log^3X),$$
uniformly in integer $N\in[X/2,X]$, for sufficiently large $X$. This is an error reduction, not a lower bound: $\mathcal M_I$ is signed and $A_3$ may contain main contribution. Choosing $U=V=X^{1/3}$ would produce Type I moduli $X^{2/3}$, outside this argument.

The surviving Type II term is explicitly
$$A_3(N)=\sum_{k>U,m>V\atop km<N}b_U(k)\Lambda(m)\Lambda(N-km)h_N(km).$$
Dyadic splitting $k\in[2^i,2^{i+1})$, $m\in[2^j,2^{j+1})$ gives $O(\log^2X)$ nonempty boxes; keep $km$ in the exact support on each. An $o(X/\log^2X)$ bound per box for a justified *centered remainder* would sum to $o(X)$; an uncentered bound on each $A_3$ block is not supplied and need not be the right assertion. $b_U$ changes sign. Taking absolute values or replacing it by $\tau(k)$ destroys cancellation, and there is no theorem here permitting $A_3\ge0$ or $A_3=o(X)$. It may carry part of the main term.

For the explicit AP main term $\mathcal M_I$ above, put exactly
$$\mathcal R_I=A_0+A_1-A_2-\mathcal M_I,\quad G=\mathcal M_I+\mathcal R_I+A_3.$$
With T73.5 controlling $\mathcal R_I=o(X)$, the first missing estimate is a lower bound for the **signed Type II/main-term combination**, or equivalently the **signed combined remainder** $\mathcal R_I+A_3$ with enough main term to make
$$\mathcal M_I(N)+\mathcal R_I(N)+A_3(N)>D_X$$
for EACH prescribed $N\in H$. Writing this condition is an exact reduction; it proves no independent arithmetic estimate. A strong target-uniform Hardy–Littlewood asymptotic for $G$ would imply it for weights with a uniformly positive continuum convolution, but is a major strengthening of Goldbach, not an accepted premise.

## 4. Target-specific Cauchy reveals four-position information

For one Type II block set $B_k(N)=\sum_{m\in I_k}\Lambda(m)\Lambda(N-km)h_N(km)$ with the exact hyperbolic cutoff. Cauchy gives
$$|\sum_k b_U(k)B_k(N)|^2\le\sum_k|b_U(k)|^2\sum_k|B_k(N)|^2.$$
Expanding the last factor yields $\sum_{k,m_1,m_2}\Lambda(m_1)\Lambda(m_2)\Lambda(N-km_1)\Lambda(N-km_2)h_N(km_1)h_N(km_2)$. This is a target-preserving four-position expression. Separate $m_1=m_2$ explicitly; off-diagonal terms enforce simultaneous primality/powers at reflected positions. It is neither an average over $N$ nor the unshifted full fourth moment. Bounding its unsigned total by Cauchy is only an upper bound on $|A_3|$; it gives no positive lower bound for $G$. An independent centered dispersion theorem with absolute error $o(X)$ at this target is the missing arithmetic information. Applying a one-variable exponential-sum theorem to this reflected product without checking its test-function hypotheses is the first invalid step.

## 5. Sieve and conditional status

A sieve can count integers avoiding small divisors in both reflected positions; CRT permits them for even $N$, but prime plus semiprime remains possible. Wu's published lower bound concerns prime+$P_2$, whereas his prime-pair theorem is an upper bound. Neither provides $G>D_X$. No external uniform zero-free hypothesis is assumed in the exact decomposition or the new fixed-wheel theorem. If a conditional circle-method estimate is used later, all zero, weight, arc and target quantifiers must remain in its conclusion. An almost-all theorem, even with a power-saving exceptional set, can leave the prescribed target exceptional.

## 6. Quantified ideal hypothesis, with support checked

For a fixed $w>0$ on $[1/5,3/5]$, let $m_w=\min_{[9/40,21/40]}w>0$. For $\tau\in[1/2,1]$, integrate over $u\in[\tau/2-1/40,\tau/2+1/40]$ to get
$$J_w(\tau):=\int w(u)w(\tau-u)du\ge m_w^2/20.$$
Both arguments lie in $[9/40,21/40]$, so this is a continuum support statement with a proved constant, not an assumption about primes. Let $C_2=\prod_{p>2}(1-1/(p-1)^2)>0$ and $\mathfrak S(N)=2C_2\prod_{p\mid N,p>2}(p-1)/(p-2)\ge2C_2$ for even $N$.

An ideal missing estimate is
$$A_3(N)-\left[X\mathfrak S(N)J_w(N/X)-\mathcal M_I(N)\right]=o_w(X)$$
uniformly for every $N\in H\cap[X/2,X]$. Together with T73.5 it would give $G=X\mathfrak S(N)J_w+o(X)\ge C_2m_w^2X/20$ for sufficiently large $X$, and then $r\ge G-D_X>0$. This is a quantitative weighted Hardy–Littlewood-strength hypothesis, **not** a newly proved estimate or a known weaker substitute for Goldbach. It identifies the main term that the centered Type II problem must include; claiming the uncentered Type II term is small would discard this term without justification. No numerical effectiveness is claimed for any cutoff.
