# Stage 65 — Exact target-localized kernel identities

**Status:** proved Fourier identities and a conditional implication; no new prime-correlation estimate is asserted.

## Convention and fixed target

Write $e(t)=e^{2\pi i t}$ and use
\[
\widehat f(n)=\int_0^1 f(\alpha)e(-n\alpha)\,d\alpha.
\]
For the finite smooth prime polynomial
\[
S_w(\alpha)=\sum_p a_p e(p\alpha),\qquad a_p=(\log p)w(p/X),
\]
let $\mathfrak m\subset\mathbb R/\mathbb Z$ be the fixed measurable minor-arc set and set
\[
f_X(\alpha)=\mathbf1_{\mathfrak m}(\alpha)S_w(\alpha)^2,
\qquad m_w(n)=\widehat f_X(n).
\]
Then $m_w(n)=\int_{\mathfrak m}S_w(\alpha)^2e(-n\alpha)\,d\alpha$. The square is essential: it selects prime sums. Replacing it by $|S_w|^2$ selects prime differences, as the Stage 65 erratum records. If the arcs are symmetric and the coefficients are real, $m_w(n)$ is real.

## Arbitrary finite shift identity

Let $\lambda=(\lambda_h)_{h\in\mathbb Z}$ be any finitely supported complex sequence and define
\[
K_\lambda(\alpha)=\sum_{h\in\mathbb Z}\lambda_h e(-h\alpha).
\]
For every integer $N$, finite linearity of integration gives the exact identity
\[
\begin{aligned}
\sum_h\lambda_hm_w(N+h)
&=\sum_h\lambda_h\int_{\mathfrak m}S_w(\alpha)^2e(-(N+h)\alpha)\,d\alpha\\
&=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)K_\lambda(\alpha)\,d\alpha.
\end{aligned}
\]
The minus sign in $e(-h\alpha)$ follows from the coefficient convention. Orthogonality of the characters gives
\[
\|K_\lambda\|_{L^2(\mathbb R/\mathbb Z)}^2
=\int_0^1\sum_{h,k}\lambda_h\overline{\lambda_k}e((k-h)\alpha)\,d\alpha
=\sum_h|\lambda_h|^2.
\]
The same derivation works with integration restricted to any measurable $E\subseteq\mathfrak m$; then the second Cauchy–Schwarz factor is $\|K_\lambda\|_{L^2(E)}\leq\|\lambda\|_2$. Parseval's equality is for the full circle; restriction gives only this inequality. Restricting the target index set to a finite $B$ gives $\sum_{n\in B}|m_w(n)|^2\leq\int_{\mathfrak m}|S_w|^4$ and no smaller bound for a specified coordinate without further information.

By Cauchy–Schwarz,
\[
\left|\sum_h\lambda_hm_w(N+h)\right|
\leq \left(\int_{\mathfrak m}|S_w(\alpha)|^4\,d\alpha\right)^{1/2}\|\lambda\|_2.
\]
Thus the conditional Li–Liu estimate cited in `04_primary_literature.md` gives
\[
\left|\sum_h\lambda_hm_w(N+h)\right|
\ll X^{5/4}(\log X)^{50}\|\lambda\|_2.
\]
For $\lambda_0=1$, $\|\lambda\|_2\geq1$. Taking only $\lambda_0=1$ recovers the ordinary pointwise bound at scale $X^{5/4}(\log X)^{50}$, larger than the major-arc scale $X$. Adding coefficients cannot improve this direct Cauchy–Schwarz bound. This limitation concerns this norm argument; it is not a no-go theorem for all arithmetic localization.

## Exact Dirichlet and Fejér normalization

For an integer $H\geq0$, the centered Dirichlet kernel and its coefficient-sum-one normalization are
\[
D_H(\alpha)=\sum_{|h|\leq H}e(-h\alpha),\qquad
\widetilde D_H(\alpha)=\frac{D_H(\alpha)}{2H+1}.
\]
The Fourier coefficient weights sum to $1$, the polynomial is normalized by $\widetilde D_H(0)=1$, and its circle integral is its central Fourier coefficient, $1/(2H+1)$. Its central shift weight is also $1/(2H+1)$, and $\|\widetilde D_H\|_2^2=1/(2H+1)$. This kernel is not pointwise nonnegative.

The standard Fejér kernel and its coefficient-normalized shift averaging multiplier are
\[
F_H(\alpha)=\frac1{H+1}\left|\sum_{j=0}^H e(-j\alpha)\right|^2
=\sum_{|h|\leq H}\left(1-\frac{|h|}{H+1}\right)e(-h\alpha),
\]
\[
\widetilde F_H(\alpha)=\frac{F_H(\alpha)}{H+1}
=\sum_{|h|\leq H}\omega_h e(-h\alpha),\qquad
\omega_h=\frac{H+1-|h|}{(H+1)^2}.
\]
Here $F_H\geq0$ and $\int_0^1F_H=1$. The shift weights obey $\sum_h\omega_h=1$ and have central weight $\omega_0=1/(H+1)$. The multiplier satisfies $\widetilde F_H(0)=1$, but its circle integral is $\omega_0=1/(H+1)$, not $1$. Exact finite sums give
\[
\sum_h\omega_h^2=\frac{2H^2+4H+3}{3(H+1)^3},\qquad
\sum_h|h|\omega_h=\frac{H(H+2)}{3(H+1)}.
\]
The Fourier support is exactly $[-H,H]$ (except the trivial $H=0$ case, where it is $\{0\}$). The effective width is order $H$; no assertion of arithmetic regularity is encoded by this support.

Consequently the Fejér average
\[
B_H(N)=\sum_{|h|\leq H}\omega_hm_w(N+h)
=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)\widetilde F_H(\alpha)\,d\alpha
\]
satisfies, under the same conditional fourth-moment input,
\[
|B_H(N)|\ll X^{5/4}(\log X)^{50}
\sqrt{\frac{2H^2+4H+3}{3(H+1)^3}}.
\]
For large $H$ the multiplier is about $\sqrt{2/(3H)}$, so this controls an average more sharply than the single coefficient. The center is simultaneously diluted by $1/(H+1)$; the estimate does not control $m_w(N)$ by itself.

## Independent finite checks

`tests/verify_localized_kernel.py` checks the exact rational weights, norms, first moment, and shift identity for $0\leq H\leq16$. `tests/verify_localized_kernel_sage.py` checks the product-coefficient identity and Parseval for an independent finite-field DFT of length 32 modulo 97, and independently checks the Fejér norm numerator. Their machine-readable outputs are adjacent JSON files. These finite checks audit the algebra; the displayed proofs establish the identities for all finite $H$.
