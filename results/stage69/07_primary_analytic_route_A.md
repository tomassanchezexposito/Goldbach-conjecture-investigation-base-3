# M7 Route A — signed rational-arc analysis

**Verdict: OPEN at one target-uniform prime estimate.** The calculations below are exact reductions and scale tests, not a proof of Candidate A.

## 1. Complete partition with target phase retained

Use the finite Farey set of reduced centers $\mathcal F_P=\{a/q\in\mathbb T:1\le q\le\lfloor P\rfloor,(a,q)=1\}$, with the usual single center for $q=1$. Order its elements lexicographically by $(q,a)$ and assign each point of $\mathbb T$ to a nearest center; at equidistant points choose the first in this fixed order. The resulting half-open Voronoi cells $V_{a/q}$ form a measurable, disjoint, exhaustive partition of the circle. The minor arcs are exactly the disjoint union $E_{a/q}=V_{a/q}\cap\mathfrak m$; cells of zero measure can be ignored. This definition resolves overlapping cores, ties and the remainder without assuming a rational approximation theorem. Reflection maps each cell to the cell at $-a/q$, up to endpoints; split any paired cell along endpoints if a reflection-invariant partition is desired.

For further resolution, intersect $E_{a/q}$ with shells $2^sP/(qX)\leq\|\alpha-a/q\|<2^{s+1}P/(qX)$, $s=0,1,\ldots,s_{a/q}$, and a final endpoint shell, where $s_{a/q}$ is the least integer with $2^{s_{a/q}+1}P/(qX)$ at least the cell's maximum distance. Since $E_{a/q}$ excludes the source major core, no point at distance below $P/(qX)$ remains in this cell when that center is the nearest center. Empty shells are allowed. With endpoints assigned to the later shell, these intersections form a complete partition. It is fixed independently of $N$ and of the target shift.

For every piece $E$ the exact phase-bearing coefficient and increment are
$$I_E(N)=\int_E S_w(\alpha)^2e(-N\alpha)d\alpha,$$
$$\Delta_{E,j}(N)=I_E(N+j)-I_E(N)=\int_E S_w(\alpha)^2e(-N\alpha)(e(-j\alpha)-1)d\alpha.$$
Frequency expansion gives the independent exact identity
$$I_E(N)=\sum_t r_w(t)\widehat{1_E}(N-t),\qquad \widehat{1_E}(k)=\int_Ee(-k\alpha)d\alpha.$$
The $r_w(t)$ are nonnegative, but the cell Fourier coefficients are generally complex and signed. Thus the sign is carried by the oscillatory transform, not by the positivity of the prime-pair coefficients.

## 2. Exact rational-center calculation

For $(a,q)=1$, put $C_r(\beta)=\sum_{p\equiv r\pmod q}a_p e(p\beta)$. The exact expansion at $a/q+\beta$ is
$$S_w(a/q+\beta)^2e(-N(a/q+\beta))
=e(-Na/q)e(-N\beta)\sum_{r,s\bmod q}C_r(\beta)C_s(\beta)e(a(r+s)/q).$$
Summing over reduced numerators $a$ weights $r+s-N$ by the Ramanujan sum $c_q(r+s-N)=\sum_{(a,q)=1}e(a(r+s-N)/q)$, which can have either sign. No positivity follows from residue admissibility.

The shift multiplier at the center is $e(-ja/q)-1$, zero exactly when $q\mid j$. On the full arc radius $P/(qX)$ its magnitude varies by at most $2\pi|j|P/(qX)$. If $q\nmid j$, the center magnitude is at least $2\sin(\pi/q)$; this gives a useful lower bound only when $2\sin(\pi/q)>2\pi|j|P/(qX)$. These multiplier facts are not estimates for the phase-weighted prime sum. In particular, removing the resonant cells does not control the aggregate signed contribution of the nonresonant cells.

## 3. What the available moment proves, and its exact loss

For any measurable cell $E$, Cauchy gives
$$|I_E(N)|\leq |E|^{1/2}\left(\int_E|S_w|^4\right)^{1/2}.$$
Summing over a complete partition and applying Cauchy once more yields only
$$|m_w(N)|\leq\sum_E|I_E(N)|\leq\left(\int_{\mathfrak m}|S_w|^4\right)^{1/2}
\ll X^{5/4}(\log X)^{50}.$$
There is no gain from subdividing if only the sum of the cell moments is known. With $K$ cells and only the global budget, a careless independent bound loses as much as $\sqrt K$ before the second Cauchy restores this same global estimate. The needed threshold is $O(X)$ with a leading constant below $c_0$ in Candidate A, whereas the known bound is larger by $X^{1/4}(\log X)^{50}$.

For a fixed denominator $q$ (a genuine special case), the numerator sum produces Ramanujan weights and still contains the unknown sums $C_rC_s$. Even at $q=1$, the target coefficient remains a signed integral of $S_w(\beta)^2e(-N\beta)$ over its minor portion. Thus fixed $q$ does not bypass the target correlation. A finite family of shifts changes the multiplier Gram matrix but not the absence of a pointwise phase estimate.

## 4. Adversarial one-hole model and exact limitation

The global fourth moment is an $\ell^2$ bound on the coefficient sequence of $1_{\mathfrak m}S_w^2$. For arbitrary coefficients with $\sum_n|c(n)|^2\leq B$, one may set $c(N)=-A$, $c(n)=0$ elsewhere, and separately prescribe a positive major coefficient $A$ at that target. This saturates the global energy and leaves the full coefficient zero. It disproves an inference from those abstract norm data alone. It is **not** a counterexample to Candidate A: no claim is made that this vector is the Fourier coefficient sequence of $1_{\mathfrak m}S_w^2$ for the actual primes. The first unproved step in any argument using the norm alone is the passage from a global $\ell^2$ budget to a strict pointwise bound below $c_0X$.

**Potential circularity and first missing arithmetic fact.** The complete partition and all phase identities hold for actual primes, but the only proven bound above takes absolute values and is too large. The missing result is the signed estimate in Candidate A, uniformly for each prescribed $N$, under its fixed zero-free and weight parameters. No target pair is used or assumed. The Li–Liu fourth moment is conditional on $Q_\Theta$ and cannot by itself supply the missing cancellation.
