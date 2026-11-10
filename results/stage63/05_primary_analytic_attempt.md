# Stage 63 M5 — Dyadic energy criterion for eliminating every exception

## Proposed lemma, stated before the literature comparison

For even $N\ge4$, let
\[
C_\Lambda(N)=\sum_{a+b=N}\Lambda(a)\Lambda(b),\qquad
P_\Lambda(N)=\sum_{\substack{p+q=N\\p,q\text{ prime}}}(\log p)(\log q),
\]
where both sums are ordered and $a,b\ge1$. Let
\[
\mathfrak S(N)=2C_2\prod_{\substack{p\mid N\\p>2}}\frac{p-1}{p-2},\qquad
C_2=\prod_{p>2}\left(1-\frac1{(p-1)^2}\right)>0.
\]
For dyadic $X$, define
\[
\mathcal E(X)=\sum_{\substack{X/2\le N\le X\\N\text{ even}}}
  |C_\Lambda(N)-N\mathfrak S(N)|^2.
\]
Candidate lemma: if $\mathcal E(X)=o(X^2)$ as $X\to\infty$, then every sufficiently large residual $N\in H$ has $R(N)>0$.

This is an intermediate, global distribution estimate on a weighted convolution. It does not assume a prime pair at the target. It is strictly stronger than the desired coverage conclusion as an analytic assertion: coverage alone says nothing about the size of the discrepancy at representable targets. No proof of this energy hypothesis is claimed.

## Proof of the conditional implication

Put $c_*=2C_2$. Since every factor $(p-1)/(p-2)>1$, $\mathfrak S(N)\ge c_*$ for every even $N$. Let
\[
K_N=\#\{p^k\le N:p\text{ prime},\ k\ge2\}.
\]
There are at most $\lfloor\log_2N\rfloor$ possible exponents and at most $\lfloor\sqrt N\rfloor$ bases for each, so
\[
0\le C_\Lambda(N)-P_\Lambda(N)
 \le 2K_N(\log N)^2
 \le D(X):=2\lfloor\log_2X\rfloor\lfloor\sqrt X\rfloor(\log X)^2
\]
for $4\le N\le X$. The difference is nonnegative: it consists of ordered pairs with at least one non-prime prime power. The upper bound counts a pair twice if both entries are higher powers, which is harmless.

If $N\in H$ and $R(N)=0$, then the prime-only convolution vanishes, $P_\Lambda(N)=0$. Hence $C_\Lambda(N)\le D(X)$. For $X/2\le N\le X$,
\[
N\mathfrak S(N)-C_\Lambda(N)\ge c_*X/2-D(X).
\]
Because $D(X)=o(X)$, this is at least $c_*X/4$ for all sufficiently large $X$. One such residual exception would therefore contribute at least $c_*^2X^2/16$ to $\mathcal E(X)$. The assumption $\mathcal E(X)=o(X^2)$ eventually makes that impossible. This proves the candidate implication with explicit threshold form: whenever $D(X)\le c_*X/4$ and $\mathcal E(X)<c_*^2X^2/16$, the dyadic block contains no residual exception.

## Independent derivation from the block maximum

For every coefficient in the block, $|C_\Lambda(N)-N\mathfrak S(N)|\le\sqrt{\mathcal E(X)}$. Thus the energy hypothesis gives a uniform error $o(X)$ across the block. If $R(N)=0$ for a residual target, the prime-power correction is at most $D(X)=o(X)$, while the conjectural main term is at least $c_*X/2$. These facts contradict one another. This maximum-from-energy derivation reaches the same criterion without counting exceptional targets by a threshold argument.

## Adversarial checks and constants

An abstract one-exception model shows why the little-oh scale matters. Set the target profile to $W_N=cN$, put the observed coefficient equal to $0$ at one $N_0\in[X/2,X]$, and equal to $W_N$ elsewhere. Then the block energy is $c^2N_0^2\ge c^2X^2/4$. Thus a generic bound $\mathcal E(X)=O(X^2)$ with a large unspecified constant does not rule out one exception. An $o(X^2)$ bound, or a sufficiently small explicit constant below the derived threshold, is needed for this route.

The logarithm-bearing prime-power correction is $o(X)$, so it cannot mask the linear main term if $R(N)=0$. The diagonal $p=q=N/2$ contributes only when $N/2$ is prime and is absent on $H$ by definition. All signs are favorable for this implication: $C_\Lambda\ge P_\Lambda\ge0$.

Focused exact prime checks in `05_countermodels.py` use residual targets $28,50,56$ and list their genuine unordered prime pairs. These are sanity checks on the definitions and the residual filter, not evidence for the infinite energy hypothesis. The abstract energy model is exact rational arithmetic. No finite prime computation is used to support an asymptotic conclusion.

## Comparison with established estimates and first missing theorem

Bhowmik–Grimmelt, Section 3, gives under a zero-real-part hypothesis $\operatorname{Re}\rho\le\Theta<3/4$ the mean-square estimate
\[
\sum_{N\le X}|r_2(N)-N\mathfrak S(N)|^2\ll X^{3/2+2\Theta+\epsilon}.
\]
At the GRH value $\Theta=1/2$, this is $O(X^{5/2+\epsilon})$, not $o(X^2)$. In fact, the zeta function has infinitely many zeros on $\operatorname{Re}s=1/2$, so the displayed uniform zero hypothesis cannot have $\Theta<1/2$; this particular bound cannot reach the needed exponent by choosing a stronger true value of $\Theta$. The unconditional minor-arc fourth-moment estimate reviewed in M4 yields an exceptional-set bound, not the required dyadic $o(X^2)$ energy estimate for the full discrepancy.

The first missing theorem for this route is therefore the unconditional, target-independent dyadic estimate
\[
\sum_{\substack{X/2\le N\le X\\N\text{ even}}}
 |C_\Lambda(N)-N\mathfrak S(N)|^2=o(X^2),
\]
or a comparably strong explicit bound below $c_*^2X^2/16$ after the prime-power correction. Even its simplest unweighted analogue is a binary additive mean-square estimate beyond the bounds verified here. This report does not prove it. Since the requisite energy theorem itself would exclude all large residual exceptions, it may be a difficult sufficient theorem, not a shortcut around the central problem.

## Verdict: OPEN

The conditional lemma is proved. The needed energy hypothesis is neither proved nor supplied by the sources reviewed. No universal coverage conclusion follows. The original three-case conjecture remains open, and no proof of Goldbach is claimed.
