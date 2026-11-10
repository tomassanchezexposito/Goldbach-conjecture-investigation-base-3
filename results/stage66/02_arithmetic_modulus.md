# Stage 66 — Aggregate variation and the arithmetic gap

## A sharp aggregate theorem

Let $c:\mathbb Z\to\mathbb C$ have finite $\ell^2$ norm, let $J$ be a set of $m$ distinct nonzero shifts, and suppose
$$|c(N)|\ge A>0,\qquad \sum_{j\in J}|c(N+j)-c(N)|^2\le V.$$
Write $\delta_j=|c(N+j)-c(N)|$. Reverse triangle and convexity of $f(t)=(A-t)_+^2$ on $t\ge0$ give
$$\sum_{j\in J}|c(N+j)|^2\ge\sum_j f(\delta_j)
\ge m f\!\left(\frac1m\sum_j\delta_j\right)
\ge m\left(A-\sqrt{V/m}\right)_+^2.$$
The last step uses Cauchy–Schwarz and that $f$ is decreasing. Therefore
$$\boxed{\|c\|_2^2\ge A^2+m\left(A-\sqrt{V/m}\right)_+^2.}$$
This is sharp for every $V\ge0$: take all $\delta_j=s=\min(A,\sqrt{V/m})$, set $c(N)=-A$, $c(N+j)=-(A-s)$, and set other coordinates to zero. The increments consume at most $V$ and attain equality. It is an aggregate version of the deterministic local theorem, not an arithmetic input.

When $B>A^2$, this aggregate condition excludes a center of size $A$ from a global energy budget $B$ only if the sharp lower bound exceeds $B$. If $0<B-A^2<mA^2$, a sufficient and sharp budget threshold is
$$V<m\left(A-\sqrt{(B-A^2)/m}\right)^2.$$
If $B-A^2\ge mA^2$, no value of $V$ can make this particular lower bound exceed $B$. These are exact finite-dimensional thresholds.

## What the available Fourier norm gives

For the Stage 65 minor-arc coefficient, put $F(\alpha)=\mathbf1_{\mathfrak m}(\alpha)S_w(\alpha)^2$. For a nonzero integer shift $j$,
$$m_w(N+j)-m_w(N)=\int_0^1F(\alpha)e(-N\alpha)(e(-j\alpha)-1)\,d\alpha.$$
In particular the parity-preserving increment is exactly
$$m_w(N+2h)-m_w(N)=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)(e(-2h\alpha)-1)\,d\alpha.$$
The sign in the multiplier follows from the convention $e(-n\alpha)$ for coefficients. This identity does not assume any prime representation.

For a fixed nonzero $j$, Cauchy–Schwarz gives
$$|m_w(N+j)-m_w(N)|\le \left(\int_{\mathfrak m}|S_w|^4\right)^{1/2}
\left(\int_{\mathfrak m}|e(-j\alpha)-1|^2\,d\alpha\right)^{1/2}
\le \sqrt{2B_X},$$
where $B_X$ is the global fourth-moment bound. The full-circle multiplier integral is exactly $2$ for every nonzero integer $j$, not $O(j^2/X^2)$; thus the full-circle Cauchy estimate has no small-shift gain. The pointwise bound is $O(X^{5/4}(\log X)^{50})$ under the conditional Li–Liu input, larger than the needed $O(X^{1/2}(\log X)^{-100})$ modulus by a power of $X$.

There is a sharper simultaneous Hilbert-space estimate for any $m$ distinct nonzero shifts $j_1,\ldots,j_m$. The full-circle Gram matrix of $g_k(\alpha)=e(-N\alpha)(e(-j_k\alpha)-1)$ is $G=I_m+\mathbf1\mathbf1^*$. Its eigenvalues are $m+1$ once and $1$ with multiplicity $m-1$. Restricting the integrals to $\mathfrak m$ can only decrease the quadratic form. The analysis-operator bound therefore yields
$$\sum_{k=1}^m|m_w(N+j_k)-m_w(N)|^2\le(m+1)\int_{\mathfrak m}|S_w|^4\le(m+1)B_X.$$
Substituting $V=(m+1)B_X$ into the sharp aggregate theorem is ineffective: $B_X\gg A_X^2$, so the variation budget is already much larger than $mA_X^2$ for the relevant $A_X\asymp X$. The bound cannot force any neighbor to remain near the center. A target-specific estimate for this weighted increment energy is still missing.

For comparison, summing over all target indices first gives the exact identity
$$\sum_{n\in\mathbb Z}|m_w(n+j)-m_w(n)|^2
=\int_{\mathfrak m}|S_w(\alpha)|^4|e(-j\alpha)-1|^2\,d\alpha\le4B_X.$$
This global shift identity is an average over targets and does not bound a prescribed target. It cannot be substituted for the fixed-$N$ inequality.

## Conditional pointwise criterion and remaining input

If a valid major-arc theorem gives $a_w(N)\ge A_X>0$, absence of a target representation forces the full weighted sum coefficient $r_w(N)=a_w(N)+m_w(N)$ to vanish, and hence $m_w(N)=-a_w(N)$. Therefore any independently proved target-uniform bounds $|m_w(N+2h)-m_w(N)|\le d_{X,N}(h)$ imply a contradiction whenever
$$A_X^2+2\sum_{h=1}^H(A_X-d_{X,N}(h))_+^2>B_X.$$
The logical implication is non-circular, but no available result supplies these signed prime-only increments with adequate constants. The Li–Liu fourth moment is conditional on the common zero-free hypothesis recorded in `results/stage64/01_2026_primary_sources.md`; even accepting that input supplies only global energy and exceptional-set information.

The first missing estimate is precise: one needs a uniform-in-target upper bound for the minor-arc quadratic form with multiplier $e(-2h\alpha)-1$, or a comparably strong aggregate bound for a block of even shifts. Bounding the multiplier by $2\pi |h|\|2\alpha\|$ does not help without a prime-weighted fourth-moment estimate localized near the relevant rational arcs. The full minor set is not a neighborhood of zero, and the global fourth moment gives no such localization. Even-step shifts must remain distinct from one-step shifts because they preserve target parity.
