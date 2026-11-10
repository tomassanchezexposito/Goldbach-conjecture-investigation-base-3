# M2 — Information hierarchy and the exact one-target norm obstruction

## Four nested information classes

Fix a target scale $X$, a finite allowed frequency set $\Lambda_X\subset\mathbb Z$ (the prime positions where the chosen weight may be nonzero), a measurable partition $\mathbb T=\mathfrak M\sqcup\mathfrak m$, and an energy budget $B$. Write $\mu=|\mathfrak m|$, $\nu=|\mathfrak M|=1-\mu$. For a function $G$ define $\widehat G(n)=\int_{\mathbb T}G(\alpha)e(-n\alpha)d\alpha$.

Use the following classes, all with the same $B,\Lambda_X,\mathfrak m$:

* $\mathcal C_0$: sequences $c\in\ell^2(\mathbb Z)$ with $\|c\|_2^2\le B$.
* $\mathcal C_1$: sequences $c(n)=\widehat{1_{\mathfrak m}G}(n)$ for $G\in L^2(\mathbb T)$ with $\int_{\mathfrak m}|G|^2\le B$.
* $\mathcal C_2$: as in $\mathcal C_1$, but $G=S^2$, where $S(\alpha)=\sum_{a\in\Lambda_X}s_a e(a\alpha)$ is a finite polynomial with $s_a\ge0$, and $\int_{\mathfrak m}|S|^4\le B$.
* $\mathcal C_3$: the single sequence from the actual weighted prime polynomial $S_w(\alpha)=\sum_{p\in\Lambda_X} (\log p)w(p/X)e(p\alpha)$, with its actual energy at most $B$.

Parseval gives $\mathcal C_3\subseteq\mathcal C_2\subseteq\mathcal C_1\subseteq\mathcal C_0$. Here $\mathcal C_2$ inherits the exact same allowed support and energy constraint; it is not a class with arbitrary changing frequencies. If $0<\mu<1$, $\mathcal C_1\subsetneq\mathcal C_0$: the Fourier coefficient sequence of a suitably scaled nonzero constant function belongs to $\mathcal C_0$, but uniqueness of Fourier coefficients means it cannot equal the sequence of a function supported on $\mathfrak m$, whose inverse Fourier function vanishes on $\mathfrak M$. Also $\mathcal C_2\subsetneq\mathcal C_1$ (for a positive energy budget): choose $A\subset\mathfrak m$ with both $A$ and $\mathfrak m\setminus A$ of positive measure and let $1_{\mathfrak m}G=\epsilon1_A$ for sufficiently small $\epsilon>0$. If this equaled $1_{\mathfrak m}S^2$, the trigonometric polynomial $S^2$ would vanish on a positive-measure set and be nonzero on another, impossible for a nonzero analytic polynomial. In the nonzero case $\mathcal C_3\subsetneq\mathcal C_2$ by scaling the finite polynomial $S$ by $\sqrt t$ for $t\in(0,1)$; the resulting square remains nonnegative-spectrum and obeys the upper energy budget, but is not the specified actual-prime sequence. These strictness statements are not numerical separations from actual prime data.

## Sharp one-coefficient and major/minor bounds

For any $c\in\mathcal C_0$, $|c(N)|\le\sqrt B$, sharply, with the spike $c(n)=\sqrt B\,e^{i\theta}1_{n=N}$. For $\mathcal C_1$, direct Cauchy and Parseval give
\[
 |c(N)|=\left|\int_{\mathfrak m}G(\alpha)e(-N\alpha)d\alpha\right|
 \le \sqrt{\mu B}.
\]
The operator is the restriction of the Fourier coefficient functional to $L^2(\mathfrak m)$; its norm is exactly $\sqrt\mu$. Equality occurs for $G(\alpha)=\sqrt{B/\mu}\,e(N\alpha+i\theta)$ on $\mathfrak m$. The same result follows by duality: the normalized representer of the functional is $1_{\mathfrak m}e(N\alpha)/\sqrt\mu$. This is the reproducing-kernel calculation; no larger universal bound follows from the same data.

Now include the full-circle energy, not just the minor energy. For any $F\in L^2(\mathbb T)$ set
\[
 a=\int_{\mathfrak M}F(\alpha)e(-N\alpha)d\alpha,\qquad
 b=\int_{\mathfrak m}F(\alpha)e(-N\alpha)d\alpha,
 \qquad \int_{\mathbb T}|F|^2\le B.
\]
Separate Cauchy inequalities on the disjoint sets yield the exact necessary condition
\[
 \frac{|a|^2}{\nu}+\frac{|b|^2}{\mu}\le B. \tag{2.1}
\]
It is also sufficient in the unrestricted $L^2$ class: take $F=(a/\nu)e(N\alpha)$ on $\mathfrak M$ and $F=(b/\mu)e(N\alpha)$ on $\mathfrak m$. Thus the least energy needed to have full coefficient $a+b=0$ with prescribed major coefficient $a$ is
\[
 B_{\rm hole}^{L^2}=|a|^2\left(\frac1\nu+\frac1\mu\right)=\frac{|a|^2}{\mu\nu}. \tag{2.2}
\]
This is a sharp finite-measure obstruction, stronger than treating the two arcs separately and then forgetting the fixed major coefficient. In particular, if a rigorously established full energy bound satisfies $B<|a|^2/(\mu\nu)$, a zero total coefficient is impossible for every function in this class. Equality is possible with the piecewise representer just displayed.

The extremizers obey the conjugate symmetry $F(-\alpha)=\overline{F(\alpha)}$ when the arcs are symmetric, $N$ is an integer, and $a,b$ are real. They generally do not belong to the finite trigonometric-polynomial class: the minor representer vanishes on the major set and is nonzero on the minor set, whereas a nonzero trigonometric polynomial cannot vanish on a positive-measure arc. The exact extremizer is therefore excluded from $\mathcal C_2$ when both sets have positive measure. No explicit lower bound on its distance to the actual prime-square class $\mathcal C_3$ is known here. Qualitative exclusion from a fixed finite-dimensional polynomial subspace does not give a useful uniform quantitative separation as $X$, support, or the prime coefficients vary.

For the minor-only moment input often appearing in applications, $|b|\le\sqrt{\mu B_{\mathfrak m}}$. If the only available information is the *full* energy plus a fixed exact major coefficient, (2.1) is sharper. An asymptotic lower bound for $|a|$ alone can be inserted into (2.2) only if the full $a$ is known to be at least that large; the bound decreases as $|a|$ increases, so the weakest allowed $|a|$ gives the conservative test.

## Positive prime-frequency spectrum does not sign a restricted coefficient

Take the explicit polynomial
\[
 S(\alpha)=e(11\alpha)+e(13\alpha),\qquad S(\alpha)^2=e(22\alpha)+2e(24\alpha)+e(26\alpha).
\]
All frequencies are odd primes greater than 7, with positive coefficients. At the target $N=36$, the full coefficient is zero because 36 is outside the sumset $\{22,24,26\}$. Here $36\in H$, and $13+23=36$ is a locally admissible residue pair modulo 210. Let $\mathfrak M=\{\alpha:\|\alpha\|_{\mathbb T}<\delta\}$ with $0<\delta<1/56$. The real part of the target integrand is
\[
 \cos(28\pi\alpha)+2\cos(24\pi\alpha)+\cos(20\pi\alpha)>0
\]
throughout this symmetric interval. Hence $a=\Re I_{\mathfrak M}(36)>0$ and $\Re I_{\mathfrak m}(36)=-a<0$. This refutes the inference “nonnegative coefficients of $S$ imply a nonnegative restricted coefficient of $S^2$.” It is an abstract finite positive-spectrum example, not a counterexample to Goldbach: it does not contain every prime in a growing weighted support. The local pair 13 and 23 also demonstrates that positive wheel admissibility and singular-series local factors do not repair the sign inference.

## Arithmetic restrictions and the spike model

For an even target $N$, a candidate prime position must avoid residue zero modulo each odd prime $\ell$, both for $p$ and $N-p$, except for the finite endpoint exceptions $p=\ell$ or $N-p=\ell$. When $\ell\nmid N$, two residue classes are forbidden; when $\ell\mid N$, only one residue class is forbidden. These local conditions constrain the support of candidate coefficients, but they do not force two supported positions to sum to the designated $N$. A one-spike coefficient vector supported at an admissible position has positive total energy and a zero coefficient at any target outside its self-sum. Such a model can respect parity and any fixed finite list of CRT exclusions. It is not a true-prime polynomial containing all primes in the prescribed interval, so it cannot refute a theorem using that stronger hypothesis.

Likewise $A_{210}(N)>0$ and the formal positivity of the Hardy–Littlewood singular series are local admissibility statements. Stage 62 shows that the finite wheel factor does not control the full singular-series factor uniformly: infinitely many residual targets can share a wheel profile while the remaining product varies without bound. Neither local fact forces the target coefficient. The “all primes in the support” restriction in $\mathcal C_3$ is precisely where a new theorem would have to enter; this report has no proof that the spike is close to, or separated from, that class.

## Scale comparison: energy versus an individual target

The inherited conditional fourth-moment scale is the **minor-only** bound $B_{\mathfrak m,X}=\int_{\mathfrak m}|S_w|^4\ll X^{5/2}(\log X)^{100}$, with constants and hypotheses as recorded for source re-audit in M5. Applied directly to the minor coefficient, Cauchy gives the pointwise *amplitude* bound
\[
 |m_w(N)|\ll X^{5/4}(\log X)^{50},
 \qquad \frac{|m_w(N)|}{X}\ll X^{1/4}(\log X)^{50}.
\]
At the squared-energy level the excess over an $X^2$ target threshold is $B_{\mathfrak m,X}/X^2\ll X^{1/2}(\log X)^{100}$. These are distinct exponents. The amplitude bound is larger than the required $X$ scale, not $o(X)$; an unspecified $\ll$ constant cannot reverse the power. Even an average over $\asymp X$ targets gives at most an RMS scale $X^{3/4}(\log X)^{50}$, while a Chebyshev exceptional-set estimate of order $X^{1/2}(\log X)^{100}$ still allows individual exceptions. This comparison uses only the minor set and the one-set inequality $|m_w(N)|\le\sqrt{\mu B_{\mathfrak m,X}}$; it does not assert that the minor-only bound is a bound for the full-circle energy.

## Precisely delimited localization no-go

Here is a no-go statement, not a claim that “Fourier methods cannot work.” Fix a measurable two-set partition with $0<\mu,\nu<1$. Suppose the only information about an arbitrary $F\in L^2(\mathbb T)$ is $\|F\|_2^2\le B$ and its exact major coefficient $a$. If
\[
 B\ge |a|^2/(\mu\nu),
\]
the constraints permit a one-hole profile $b=-a$, by the equality construction for (2.2). Therefore these norm data alone cannot force $a+b\ne0$. If the inequality is reversed, they do force nonvanishing. This is sharp within the named class and includes any proof using only those two linear observations and the total $L^2$ budget. It does **not** apply to arguments that exploit further algebraic/arithmetic information about $F=S_w^2$.

For the two-set theorem (2.1), $B$ must bound the **full** energy $\int_{\mathbb T}|F|^2$; the cited minor-arc estimate alone cannot be substituted for that $B$. Its comparison with a full-circle budget therefore remains unmade here. Separately, the direct minor-only criterion is $B_{\mathfrak m,X}<|a|^2/\mu$, which would force $a+b\ne0$ when $b$ is the minor coefficient. For $|a|\asymp X$, fixed $\mu>0$, and the cited $B_{\mathfrak m,X}\ll X^{5/2}(\log X)^{100}$, the available upper bound is larger than the $X^2$ threshold by a factor $X^{1/2}$ up to logarithms, so this input does not certify the criterion. Reallocating only the same total minor budget among rational arcs cannot improve it; a new prime-specific phase/correlation constraint is required. These statements neither refute nor prove such an extra constraint.

## Candidate additional hypotheses and their exact force

The following quantified conditions would suffice, but they are deliberately distinguished by strength:

1. **Signed minor hypothesis:** if $a_w(N)\ge cX$ and, uniformly for $N\in H\cap[X/2,X]$, $\Re m_w(N)\ge -(c-\varepsilon)X$ for some fixed $\varepsilon>0$, then $r_w(N)=a_w(N)+m_w(N)>0$. This directly supplies the missing signed inequality and is essentially the desired target positivity in weighted form.
2. **Short-shift/local-energy condition:** for a block of $m$ neighboring target coefficients centered at $r_w(N)$, a certified total energy upper bound $B_X$ and shift energy $V_{N,J}$ imply positivity if the strict Stage 66 inequality in M6 holds. This can be weaker than naming $r_w(N)>0$, but only if $V_{N,J}$ is independently bounded below the explicit threshold; no such true-prime bound is proved here.
3. **Bilinear pair lower bound:** $\sum_{p}1_{\mathbb P}(p)1_{\mathbb P}(N-p)\ge1$ is exactly the desired representation (up to diagonal convention); a lower bound $\gg N/(\log N)^2$ is much stronger. It is sufficient but circular as an assumed “new lemma” unless independently established by a different proof.
4. **Signed rational-arc cancellation:** bounds for separate arc magnitudes are insufficient. A condition on the signed sum of arc integrals is sufficient only when it yields $\Re\sum_E I_E(N)>-a_w(N)$ uniformly, and thus is another formulation of the pointwise missing estimate unless its phase property is derived from primes.

Formal one-hole coefficient vectors and the positive-spectrum example above defeat weaker conditions that specify only global energy, local residues, or nonnegative frequencies. They do not meet $\mathcal C_3$ and hence are not arithmetic counterexamples.

**Potential circularity and first missing arithmetic fact.** Assuming a favorable signed minor bound or a target-anchored positive four-prime count without an independent derivation simply renames the conclusion. The first missing arithmetic fact is a uniform, target-specific signed correlation estimate for the actual prime coefficients (or an independent nonzero lower bound for their reflected pair convolution).

## M2 verdict

The hierarchy, sharp norm bounds, equality profiles, positive-spectrum sign counterexample, and localized one-hole threshold are proved for their stated function classes. The published global fourth moment is too large relative to $X^2$ to exclude a single zero in those classes. The unresolved question is whether the full-prime positive-spectrum structure supplies a quantitatively useful separation from the unrestricted extremizer; no such separation is established.
