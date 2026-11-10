# Stage 65 — Adversarial analysis of localized signed correlations

## Attempt: Fejér localization plus additive regularity

For $H\geq0$, let
\[
\omega_h=\frac{H+1-|h|}{(H+1)^2}\quad(|h|\leq H),\qquad
B_H(N)=\sum_{|h|\leq H}\omega_hm_w(N+h).
\]
The exact identities and norms are proved in `01_localized_kernel_identities.md`. If the target is missing but the major-arc estimate gives $a_w(N)\geq cX$, then $m_w(N)=-a_w(N)\leq-cX$. Suppose, independently and without a representation assumption, one had
\[
|m_w(N+h)-m_w(N)|\leq L_X|h|\qquad(|h|\leq H).
\]
Then
\[
|m_w(N)-B_H(N)|\leq L_X\frac{H(H+2)}{3(H+1)},
\]
while the Li–Liu moment yields
\[
|B_H(N)|\leq \sqrt{C_4}X^{5/4}(\log X)^{50}
\sqrt{\frac{2H^2+4H+3}{3(H+1)^3}}.
\]
If the sum of these right-hand sides is strictly less than $cX$, then $m_w(N)>-cX$ and the missing-target equation is impossible. The argument does not assume $R(N)>0$ or positivity at neighboring targets. It is therefore a valid conditional criterion, not a proof of its new hypothesis.

For large $H$, the two terms are asymptotic to
\[
\sqrt{\frac{2C_4}{3H}}X^{5/4}(\log X)^{50},\qquad \frac{L_XH}{3}.
\]
Ignoring lower-order terms, a feasible $H$ must satisfy both
\[
H>\frac{2C_4}{3c^2}X^{1/2}(\log X)^{100},\qquad
H<\frac{3cX}{L_X}.
\]
Thus even this criterion requires roughly $L_X<(9c^2/(2C_4))X^{1/2}(\log X)^{-100}$, with strict margins and constants. This scale calculation is an asymptotic diagnostic, not an extra theorem. The source literature audited in `04_primary_literature.md` provides no such $L_X$.

## Attempts to remove the missing hypothesis

### Direct integral estimate

The exact increment has a multiplier $e(-h\alpha)-1$. The universal inequality $|e(-h\alpha)-1|\leq2\pi|h|\|\alpha\|_{\mathbb R/\mathbb Z}$ is not enough: the minor arcs include neighborhoods of many rational points, and the available global fourth moment does not give a target-specific small integral after inserting this multiplier. Cauchy–Schwarz merely gives the global scale times a multiplier norm; it does not yield the required uniform modulus in $h$.

### Global energy and optimized linear weights

For any finite weights with $λ_0=1$, Parseval gives $\|K_\lambda\|_2=\|\lambda\|_2\geq1$. Hence direct Cauchy–Schwarz cannot improve the one-coordinate $X^{5/4}(\log X)^{50}$ scale. If one instead chooses $λ_0\ll1$, a singleton coefficient is attenuated by that same central weight. The exact isolated-spike model in `02_fourier_localization_limits.md` shows why this linear average cannot be inverted from a global norm alone. This refutes an inference about the information content of the norm bound, not an arithmetic statement about actual primes.

### Anchored shared-prime and four-prime counts

The exact M1 identity partitions two-target representation products into shared-position and four-distinct terms. It is useful for avoiding multiplicity mistakes, but an anchor on a representation of $N$ is empty when $R(N)=0$. Consequently, a lower bound derived by selecting a prime pair at $N$ is circular for the target under investigation. Modularly admissible quadruples or singular-series densities have no signed primality lower bound at a prescribed target. No sign-preserving inequality independent of $R(N)$ was found.

### Wheel, singular series, and residual factorization

The inherited pair $N=210,420$ has identical wheel and full singular-series factors, while only 210 belongs to the residual set. Thus those factors alone do not encode residual membership. The factors from $N-1$ and $N/2$ constrain those integers but do not, by an established identity, force simultaneous primality at a reflected position. This is an exact counterexample to factor-only recovery, not to stronger estimates using additional arithmetic.

## Verdict

No new unconditional arithmetic estimate for genuine prime correlations was obtained. The strongest justified progress is (i) the corrected exact Fourier distinction between sums and differences, (ii) exact all-$H$ localization formulas, (iii) a sharp deterministic limitation for deriving pointwise control from the global fourth moment by linear functionals alone, and (iv) a non-circular conditional criterion whose missing input is explicit. The original three-case conjecture remains open.

## Next narrow target

Prove or disprove a uniform estimate for the **true-prime signed increment** $m_w(N+h)-m_w(N)$, for $N$ in the prescribed even target range and shifts $|h|\leq H(X)$ at least of order $X^{1/2}(\log X)^{100}$, with a constant strong enough to satisfy the displayed compatibility condition. The estimate must be derived without conditioning on any representation of $N$ or $N+h$. If that scale is inaccessible, identify the weakest weighted shift norm that still lets the Fejér argument exclude an isolated negative coefficient. This is a research objective, not a presumed theorem.
