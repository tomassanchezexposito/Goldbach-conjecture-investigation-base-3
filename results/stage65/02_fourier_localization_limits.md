# Stage 65 — What linear Fourier localization cannot infer

**Classification:** deterministic no-go for the global coefficient norm alone; a separate conditional local-regularity criterion is proved below. The abstract obstruction is not an arithmetic counterexample.

## Global fourth moment and a single exceptional coefficient

Let $c_X(n)=m_w(n)$ and suppose the available input is only
\[
\sum_{n\in\mathbb Z}|c_X(n)|^2\leq B_X,
\qquad B_X=CX^{5/2}(\log X)^{100},
\]
for a fixed positive constant $C$. A missing representation at a target with independently established major arc $a_w(N)\geq cX$ forces $c_X(N)=-a_w(N)$, hence $|c_X(N)|\geq cX$. For all sufficiently large $X$, $c^2X^2\leq B_X$. The abstract vector
\[
c_X(n)=-cX\,\mathbf1_{n=N}
\]
therefore obeys the assumed global norm bound while containing exactly the size and sign that a missing target requires. This proves that the global $\ell^2$ inequality alone cannot exclude one exceptional coefficient.

More generally, the admissible abstract class is
\[
\mathcal C_X=\{c:\mathbb Z\to\mathbb C:\ c\text{ finitely supported},\ \sum_n|c(n)|^2\leq B_X\}.
\]
For any finitely supported linear statistic $L_\lambda(c)=\sum_h\lambda_hc(N+h)$, the singleton vector gives $L_\lambda(c)=-cX\lambda_0$. If $\lambda_0=0$, it is invisible; if $\lambda_0$ is small, it is attenuated; if $\lambda_0=1$, it remains at full size. Exact recovery of the central coordinate from an arbitrary sequence requires a coefficient vector whose central coefficient is one, and its $\ell^2$ norm is at least one. Cauchy–Schwarz then yields no improvement over the one-coordinate bound. This is a logical model of what follows from a global norm hypothesis, not evidence that the singleton can arise from a genuine prime exponential sum.

## Why normalized short-shift averages do not invert

Both shift-weight sequences in `01_localized_kernel_identities.md` sum to one, while their central weights tend to zero: $1/(2H+1)$ for Dirichlet and $1/(H+1)$ for Fejér. The associated trigonometric multipliers have those central weights as their circle integrals; coefficient-weight normalization is not unit circle-integral normalization. For the exact abstract spike $c(N)=-A$, $c(N+h)=0$ for $0<|h|\leq H$, their averages equal respectively
\[
-\frac{A}{2H+1}\quad\text{and}\quad-\frac{A}{H+1}.
\]
These tend to zero relative to $A$ as $H\to\infty$, even though the exceptional coordinate stays fixed. This countermodel respects a global energy budget whenever $A^2\leq B_X$. It refutes the inference “a small normalized average implies the center is small” absent a neighbor constraint.

The first missing true-prime input for this route is an additive shift-regularity theorem, valid without assuming any representation at the center, for the actual signed coefficients $m_w(N+h)$. A useful quantified form would be
\[
|m_w(N+h)-m_w(N)|\leq L_X|h|\quad (N\text{ in the required target range},\ |h|\leq H),
\]
with constants small enough after choosing $H$. The global fourth moment does not imply this bound. Indeed the exact difference is
\[
m_w(N+h)-m_w(N)=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)(e(-h\alpha)-1)\,d\alpha,
\]
and a direct Cauchy–Schwarz estimate sees the multiplier on the entire minor set; without additional arithmetic information it gives no required small shift modulus.

## Conditional Fejér criterion with sharp displayed constants

Assume, for a specified $H\geq0$, that the major-arc theorem applies to a residual target $N$ and gives $a_w(N)\geq cX>0$. Assume also the Li–Liu fourth-moment hypothesis in the form
\[
\int_{\mathfrak m}|S_w|^4\leq C_4X^{5/2}(\log X)^{100},
\]
and the independently proved additive regularity estimate above for every $|h|\leq H$. Let $B_H(N)$ be the normalized Fejér average. The exact first-moment identity and Cauchy–Schwarz give
\[
|m_w(N)-B_H(N)|\leq L_X\frac{H(H+2)}{3(H+1)},
\]
\[
|B_H(N)|\leq \sqrt{C_4}\,X^{5/4}(\log X)^{50}
\sqrt{\frac{2H^2+4H+3}{3(H+1)^3}}.
\]
Therefore the explicit sufficient inequality
\[
\sqrt{C_4}\,X^{5/4}(\log X)^{50}
\sqrt{\frac{2H^2+4H+3}{3(H+1)^3}}
+L_X\frac{H(H+2)}{3(H+1)}<cX
\]
implies $a_w(N)+m_w(N)>0$ and hence $R(N)>0$ for $N\in H$, provided $w\geq0$ and the support/diagonal conditions from the source theorem hold. This is a conditional theorem: neither this shift-regularity estimate nor constants making the inequality true are established. Its hypotheses do not assert $R(N)>0$ or assume all neighboring targets are represented, so the implication itself is non-circular.

## Scope of the no-go statement

The result is deliberately limited to arbitrary coefficient sequences controlled only by the stated global norm, and to linear functionals without extra coefficient constraints. It does not rule out nonlinear arithmetic localization, bilinear identities, additional local moments, sieve input, or a target-specific theorem for the true prime coefficients. To beat the obstruction one must add genuine arithmetic information that excludes or controls an isolated coefficient.
