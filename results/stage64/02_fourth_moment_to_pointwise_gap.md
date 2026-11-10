# Stage 64 — From the fourth moment to one target: exact gap

## Definitions and the positive major term

Let $e(t)=e^{2\pi it}$ and let
\[
S_w(\alpha)=\sum_p(\log p)w(p/X)e(p\alpha),
\]
with the smooth weight and major/minor arcs specified in `01_2026_primary_sources.md`. Define
\[
r_w(N)=\int_{\mathbb R/\mathbb Z}S_w(\alpha)^2e(-N\alpha)\,d\alpha,
\quad
m_w(N)=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)\,d\alpha,
\quad
a_w(N)=\int_{\mathfrak M}S_w(\alpha)^2e(-N\alpha)\,d\alpha.
\]
These are exact complex Fourier coefficients and $r_w(N)=a_w(N)+m_w(N)$. The prime sum is finite because $w$ is compactly supported in $(0,1)$. Conjugate symmetry makes these coefficients real for integer $N$.

Li–Liu Proposition 4.1, under their common zero hypothesis with $\Theta<1$, gives for even $N\in[X/2,X]$
\[
a_w(N)=\mathfrak S(N)I_w^+(N)+O_{w,\Theta,\kappa}(X^{1-c}),
\quad I_w^+(N)=\sum_mw(m/X)w((N-m)/X).
\]
They establish $I_w^+(N)\geq X/4+O(1)$ and $\mathfrak S(N)\geq 2C_2>0$, where $C_2=\prod_{p>2}(1-(p-1)^{-2})$. Hence $a_w(N)\geq c_wX$ for sufficiently large $X$, uniformly in the displayed interval. If there is no prime pair, then $r_w(N)=0$; consequently $m_w(N)=-a_w(N)$ and $|m_w(N)|\geq c_wX$. This implication is non-circular: it uses absence only to infer vanishing of the exact prime coefficient, then compares with the independently established major arc.

The issue is how to prove the contrary pointwise estimate on $m_w(N)$.


**Stage 65 mathematical erratum (2026-11-10).** A previous revision incorrectly wrote \(|S_w(\alpha)|^2\) in both the major- and minor-arc coefficient definitions while using \(S_w(\alpha)^2\) for the full coefficient. The wrong integrals are coefficients of *prime differences*, not sums, and therefore do not partition \(r_w(N)\). Both definitions above have been corrected to \(S_w^2\), without altering the valid fourth-moment integrand \(|S_w|^4\) in Parseval. Explicit counterexample: \(S=e(3\alpha)+e(5\alpha)\) has the \(N=8\) Fourier coefficient of \(S^2\) equal to 2, while the \(N=8\) coefficient of \(|S|^2\) equals 0. See \`results/stage65/00_erratum.md\` and the independently exact regression script in that directory. The original Stage 64 Git history remains preserved.

## Exact Parseval calculation and exponents

Write $f(\alpha)=\mathbf 1_{\mathfrak m}(\alpha)S_w(\alpha)^2$. Its $N$th Fourier coefficient is $m_w(N)$ (up to the harmless sign convention). Parseval on the circle gives
\[
\sum_{N\in\mathbb Z}|m_w(N)|^2
=\int_{\mathbb R/\mathbb Z}|f(\alpha)|^2\,d\alpha
=\int_{\mathfrak m}|S_w(\alpha)|^4\,d\alpha.
\]
There is no missing factor of 2: this is the full integer Fourier series of the indicator-restricted function. If one sums only a subset of targets, its square sum is no larger.

The Li–Liu theorem therefore implies, with $L=\log X$,
\[
\sum_N|m_w(N)|^2\ll X^{5/2}L^{100},\qquad
|m_w(N)|\ll X^{5/4}L^{50}.
\]
The pointwise major term is $\asymp X$; the available Cauchy–Schwarz bound exceeds it by $X^{1/4}L^{50}$. A one-exception target contributes at least $c_w^2X^2$ to the global minor-arc coefficient energy. The theorem's upper bound is $X^{5/2}L^{100}$, so it permits that contribution with substantial room. Equivalently, the exceptional-set estimate obtained by thresholding is
\[
\#\{N:|m_w(N)|\geq c_wX\}\ll X^{1/2}L^{100};
\]
the right-hand side diverges.

For Stage 63 M5, the relevant discrepancy is instead
\[
\mathcal E_\Lambda(X)=\sum_{X/2\leq N\leq X,\ 2\mid N}|C_\Lambda(N)-N\mathfrak S(N)|^2,
\quad C_\Lambda(N)=\sum_{a+b=N}\Lambda(a)\Lambda(b).
\]
M5 proves that $\mathcal E_\Lambda(X)=o(X^2)$ suffices for eventual coverage of residual targets, after the explicit higher-prime-power correction. Li–Liu's $X^{5/2}L^{100}$ estimate is for a smoothed prime-only minor-arc Fourier coefficient. It is not an upper bound for $\mathcal E_\Lambda(X)$. Even if one informally identified the coefficient sequences, the exponent would be too large by a factor $X^{1/2}$, and the smoothing, arc split, main-term normalization, and higher prime powers would still need to be handled. No such identification is made here.

## First invalid derivation step

The tempting argument is:

1. a missing target forces $|m_w(N)|\geq c_wX$;
2. sum this square over targets and apply the $X^{5/2}L^{100}$ fourth moment;
3. conclude there are fewer than one missing target.

The first two steps give only $\#\text{exceptions}\ll X^{1/2}L^{100}$. The invalid step is replacing this diverging upper bound by zero. A bound $A(X)\ll X^{1/2}L^{100}$ does not imply $A(X)=0$; the model $A(X)=1$ satisfies it for all sufficiently large $X$. This is a quantifier failure, not an error in Parseval or the circle-method theorem.

The same mismatch blocks a direct M5 derivation: the proved M5 threshold is $\mathcal E_\Lambda(X)<C_2^2X^2/4$ once the prime-power correction is small enough, while the fourth moment is of order $X^{5/2}L^{100}$ for a different sequence. Neither the normalization nor the exponent supplies the required bound.

## Sharpness of what follows from a global norm alone

For $M_X=CX^{5/2}L^{100}$, the abstract vector $v$ indexed by targets with a single nonzero coordinate $v_{N_0}=cX$ has $\|v\|_2^2=c^2X^2\leq M_X$ for all sufficiently large $X$. Thus the inequality $\|m\|_2^2\leq M_X$ by itself cannot rule out one coordinate of the size forced by a missing target. This is a sharp logical obstruction for an inference from that norm bound alone. It is **not** a constructed minor-arc coefficient vector arising from primes and is not an arithmetic counterexample.

## What would close the argument

Any one of the following would be a new, non-circular input; none is supplied by the sources audited here.

1. For every residual $N\in[X/2,X]$, an estimate on the **real signed** coefficient $m_w(N)>-a_w(N)$ with constants uniform in $N$ and the chosen $X$.
2. A target-localized energy estimate on a family containing each target that makes the total energy strictly smaller than $c_w^2X^2$ whenever that target is missing. A global bound of $o(X^{5/2})$ is not enough by itself unless its constant and exponent make the one-coordinate threshold impossible; the direct sufficient global scale is $o(X^2)$.
3. The Stage 63 M5 estimate $\mathcal E_\Lambda(X)=o(X^2)$ (or its exact explicit threshold) for the unsmoothed von Mangoldt sequence, with a separate rigorous transfer to the prime-only count.

An average over shifts, moduli, or polynomial values is insufficient unless an additional theorem shows that a given residual target belongs to a family whose exceptional count is zero. A condition on an anchored correlation that already presupposes $R(N)>0$ is circular and cannot be used.

## Classification

- **Proved in this report:** the coefficient decomposition, Parseval identity, exponents of the consequence of the stated fourth moment, and the abstract one-coordinate obstruction.
- **External conditional input:** Li–Liu's fourth-moment and major-arc theorems under their stated common zero hypothesis.
- **Not proved:** the M5 energy bound, any target-uniform signed minor-arc estimate, or positivity for every residual target.
