# Stage 68 M6 — target-uniform signed increment attempt

## Candidate theorem, stated before assessment

Fix the Li–Liu smooth weight $w$ and its major/minor partition at $P=X^\kappa$, with the common zero hypothesis $\Theta<11/12$ required by that source. Let $N\in H\cap[X/2,X]$, and let $J_X=\{2,4,\ldots,2m\}$ with
\[
m\ge 2(C_B/c_A^2)X^{1/2}(\log X)^{100},
\]
where $A_X\ge c_AX$ is the major-arc lower bound and $B_X\le C_BX^{5/2}(\log X)^{100}$ is the full minor fourth-moment upper bound, uniformly over the indicated $N$. Here $a/q$ denotes reduced rational arc centers with $q\le X^\kappa$, when the optional frequency partition below is used, and $2h$ are the even shifts. The candidate prime-specific estimate is
\[
\tag{P68}
\sup_{N\in H\cap[X/2,X]}\sum_{h=1}^{m}
|m_w(N+2h)-m_w(N)|^2
<mA_X^2\left(1-\sqrt{\frac{B_X-A_X^2}{mA_X^2}}\right)^2.
\]
Assume $m>(B_X-A_X^2)/A_X^2$, so the right side is positive. For fixed constants one can take $m\ge2B_X/A_X^2$, which makes the right side at least $mA_X^2(1-1/\sqrt2)^2$. The shifts are even and their maximal size $2m=O(X^{1/2}(\log X)^{100})$ is $o(X)$, so they are local on the scale $X$. The variance argument uses the minor coefficient sequence at shifted integer indices; it does not assume representations at those indices or require them to lie in the major-arc theorem's target range. The candidate is an estimate about genuine prime sums and does not assume a representation at $N$.

If proved, (P68) makes the Stage 66/68 criterion strict and excludes every zero representation in the specified target interval. The constants, weight dependence, target uniformity and zero hypothesis are part of the statement; an averaged version is not sufficient.

## Proof pass 1: deterministic reduction and exact threshold

Let $a_w(N)$ and $m_w(N)$ be the major and minor coefficients. If $R(N)=0$, nonnegativity of $w$ and the prime coefficient identity imply $a_w(N)+m_w(N)=0$. If the independent major theorem gives $a_w(N)\ge A_X$, then $|m_w(N)|\ge A_X$. Parseval gives
\[
\sum_n|m_w(n)|^2=\int_{\mathfrak m}|S_w|^4\le B_X.
\]
For $V_N=\sum_{j\in J_X}|m_w(N+j)-m_w(N)|^2$, the sharp finite-dimensional variance inequality yields
\[
\sum_n|m_w(n)|^2\ge A_X^2+m\left(A_X-\sqrt{V_N/m}\right)_+^2.
\]
When $B_X>A_X^2$ and $m>(B_X-A_X^2)/A_X^2$, rearrangement shows that strict contradiction follows exactly from
\[
V_N<m\left(A_X-\sqrt{(B_X-A_X^2)/m}\right)^2.
\]
This is the right side of (P68). This reduction is rigorous and non-circular, conditional on its independent analytic inputs.

At $m\ge2B_X/A_X^2$, the needed saving is on the order of $mX^2$. With $m\asymp X^{1/2}(\log X)^{100}$, this permits an increment energy of order $X^{5/2}(\log X)^{100}$ but with a specific constant below the threshold. The generic complete-minor operator estimate is $V_N\le(m+1)B_X$, of order $X^3(\log X)^{200}$, and misses a factor of order $X^{1/2}(\log X)^{100}$. The available Li–Liu theorem states a global fourth moment, not (P68).

## Proof pass 2: rational-arc allocation and why it does not close

Partition the complete minor set into disjoint nearest-rational shells $E_{a/q,s}$ as in `04_arc_budget_feasibility.md`. Write $G_{a/q,s}$ for the exact increment Gram matrix and suppose, hypothetically, one proves genuine-prime bounds
\[
\int_{E_{a/q,s}}|S_w|^4\le B_{q,s}(X;w,\Theta)
\]
with a disjoint total and a phase-independent allocation satisfying
\[
\left(\max_{\|z\|_2=1}\sum_{q,s}\sqrt{B_{q,s}(X;w,\Theta)}
\sqrt{z^*G_{q,s}z}\right)^2
<m\left(A_X-\sqrt{(B_X-A_X^2)/m}\right)^2.
\]
Then (P68) follows by the exact support-function theorem. This is a materially different route through frequency localization, but it still requires a localized prime fourth-moment profile strong enough for the target threshold and leaves no room for unbounded signed remainder. If only $\sum_{q,s}B_{q,s}\le B_X$ is established, the allocation collapses to $B_X\lambda_{\max}(G_{\mathfrak m})$ and is far too large. If one estimates only selected resonant denominators, the complement remains uncontrolled.

The second proof route therefore identifies a precise missing theorem; it does not establish it. We have no theorem in the audited source chain giving these $B_{q,s}$ uniformly with the needed constant, and no independent estimate for signed cancellation over the entire minor set.

## Independent critic: strongest countermodels and first invalid steps

1. **Variance bound sharpness.** For arbitrary vectors, fix center value of modulus $A$ and increments with prescribed squared norm $V$. The minimizing configuration distributes the increment equally in the direction that reduces each shifted coordinate toward zero, producing the $(A-\sqrt{V/m})_+$ term. Thus no stronger conclusion follows from the center and $V$ alone. This is an abstract finite-dimensional extremizer, not a prime realization.
2. **Arc partition.** Assigning a total budget to many bins cannot improve the bound: optimizing over all allocations gives exactly $\sqrt{B\lambda_{\max}(\sum G_r)}$. The first invalid step in a proposed gain from mere disjointization is treating labels $B_r$ as independently small without proving those bounds for primes.
3. **Phase cancellation.** If $c_r(N)$ are restricted arc coefficients, the condition $\sum_r\Re c_r(N)>-a_w(N)$ is exactly the positivity condition for their sum. A strict margin $\sum_r\Re c_r(N)\ge -a_w(N)+\delta X$ is a stronger sufficient condition, not a consequence of energy. This route simply restates the pointwise obstacle unless an independent theorem proves the margin.
4. **Averaging.** An exceptional-set bound $|E(X)|\ll X^\eta$ with $\eta>0$, or a target average of $V_N$, does not prove (P68) for every $N$: one exceptional target remains logically possible. The first invalid step is replacing a mean estimate by a supremum.

## Quantitative verdict and remaining theorem

| Quantity | Best inherited input | Required by the certificate | Gap |
|---|---:|---:|---:|
| Major coefficient | $A_X\ge c_AX$ under the cited major-arc hypotheses | Same | No gap in scale, but conditional on the external theorem |
| Total minor energy | $B_X\le C_BX^{5/2}(\log X)^{100}$ | Also appears in the necessary shift count | No pointwise bound follows |
| Shift count | $m> B_X/A_X^2-1$; take $m\ge2B_X/A_X^2$ | $m\asymp X^{1/2}(\log X)^{100}$ even shifts | Feasible geometrically; growing dimension alone is no gain |
| Signed increment energy | Generic $\le(m+1)B_X$ | $<m(A_X-\sqrt{(B_X-A_X^2)/m})^2\asymp mX^2$ | Generic estimate is larger by $B_X/A_X^2\asymp X^{1/2}(\log X)^{100}$ |
| Arc budgets | Only their sum is known in the inherited theorem | A profile yielding the strict allocation inequality | OPEN; the total alone collapses |

The precise missing result is a target-uniform, genuine-prime estimate of the signed increment vector (P68), or an independently proved localized fourth-moment profile plus full-complement phase control that implies it. No wheel condition, singular-series heuristic, half-period identity, or four-distinct nonnegativity supplies that estimate. Universal coverage remains OPEN.
