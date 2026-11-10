# M3 addendum — explicit signed analytic candidate

**Status: OPEN; conditional major-arc premise, unproved prime-only minor estimate.** This file supplies the formal candidate required by M3 and used as the common target for M7. It is not a Goldbach proof.

Fix a weight $w$ from Li–Liu's Theorem 1: a specified nonnegative Gevrey function in $C_c^\infty((0,1))$, bounded by one and equal to one on $[1/8,7/8]$. Fix a zero boundary $1/2\leq\Theta<11/12$ and the theorem's fixed $\kappa=\kappa(\Theta)\in(4/9,9/20)$; set $P=X^\kappa$ and use their arcs $q\leq P$, $|\alpha-a/q|\leq P/(qX)$. The conditional hypothesis $Q_\Theta$ is that every nontrivial zero of every primitive Dirichlet $L$-function, including $\zeta$, has real part at most this fixed $\Theta$.

Write $r_w(N)=a_w(N)+m_w(N)$ with the exact coefficients defined in `01_prime_specific_exact_convolution.md`. On the source's uniform even range $N\in[X/2,X]$, Proposition 4.1 supplies a major-arc asymptotic with a positive singular-series main term and a power-saving error, under its stated fixed parameters. Since the even singular series has a positive lower bound and the fixed weight's main integral is positive, this yields some source-dependent constants $c_0=c_0(w,\Theta,\kappa)>0$, $\eta>0$, and threshold $X_0$ with $a_w(N)\geq c_0X$ for $X\geq X_0$, provided those source statements are applied with exactly their hypotheses. We do not assign numerical values or claim an effective $X_0$; the checked paper's big-O constants do not provide them.

The missing estimate is:

> **Candidate A.** Under the fixed $Q_\Theta$ hypothesis and the fixed $w,\Theta,\kappa$ above, there are $\delta>0$ and $X_1$ such that, for every $X\geq X_1$ and every even $N\in H\cap[X/2,X]$,
> $$\left|\int_{\mathfrak m(X^\kappa)} S_w(\alpha)^2e(-N\alpha)\,d\alpha\right|\leq(c_0-\delta)X.$$

The constants may depend only on the fixed source parameters, not on $N$ or $X$; effectivity of $X_1$ is OPEN and not supplied by this research. The integration is over the genuine-prime polynomial, not a von Mangoldt replacement. If Candidate A and the cited major-arc lower bound both hold, then $r_w(N)\geq\delta X>0$. Because $w=1$ on a central interval, any such positive coefficient is an actual prime-pair representation; and $N\in H$ removes the diagonal, so it yields $R(N)>0$. This implication does not assume a representation in advance.

The missing estimate is itself very strong: combined with the conditional major-arc theorem it implies binary Goldbach for every sufficiently large even $N$ in the target range under $Q_\Theta$. It may be stronger quantitatively than needed, but no argument here makes it a strictly weaker route. The Li–Liu fourth moment $\int_{\mathfrak m}|S_w|^4\ll X^{5/2}(\log X)^{100}$ gives only $|m_w(N)|\leq (\int_{\mathfrak m}|S_w|^4)^{1/2}\ll X^{5/4}(\log X)^{50}$ by Cauchy, which is larger than the required $O(X)$ threshold by a factor $X^{1/4}$ up to logarithms. Its exceptional-set theorem permits isolated targets. Neither result proves Candidate A.

**Potential circularity and first missing arithmetic fact.** Replacing the missing signed estimate by a lower bound on $r_w(N)$ is the desired conclusion in weighted form. No target pair may be selected to anchor a four-prime correlation. The first missing fact is a uniform, phase-sensitive bound for the true-prime minor coefficient (or another independent positive lower bound for the true-prime pair correlation). All assumptions are explicit above; Candidate A is OPEN, not an established conditional theorem.
