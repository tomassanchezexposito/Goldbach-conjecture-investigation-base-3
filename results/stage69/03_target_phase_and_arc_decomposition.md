# M3 — Target phase, rational cells, and the signed arc obstruction

## Exact partition and symmetry

Fix $X$, $P=X^\kappa$ with fixed $0<\kappa<1/2$, and the standard major arcs
\[
\mathfrak M(P)=\bigcup_{q\le P}\bigcup_{(a,q)=1}\{\alpha:\|\alpha-a/q\|\le P/(qX)\},\qquad
\mathfrak m=\mathbb T\setminus\mathfrak M(P).
\]
For sufficiently large $X$, $2P^2<X$ makes these intervals pairwise disjoint. Their union and complement are invariant under reflection $\alpha\mapsto-\alpha$. A finite measurable partition of $\mathfrak m$ can be made by listing its component intervals and assigning endpoints by a fixed half-open convention. More finely, any proposed measurable partition $\{E_s\}$ can be replaced by the Boolean refinement $E_s\cap(-E_t)$; this makes each reflected piece have an explicitly paired partner and leaves no unmatched set implicit.

For real coefficients $a_p$, $S(-\alpha)=\overline{S(\alpha)}$. Hence
\[
F_N(\alpha):=S(\alpha)^2e(-N\alpha),\qquad F_N(-\alpha)=\overline{F_N(\alpha)}.
\]
Integrals over reflected pieces are conjugates; only a reflection-invariant union has a real integral. The complete minor coefficient is real, but its individual non-symmetric cell contributions need not be. Pairing proves reality, not nonnegativity.

For each piece, the exact identities are
\[
I_E(N)=\int_E S(\alpha)^2e(-N\alpha)\,d\alpha,
\quad
\Delta_{E,j}(N)=I_E(N+j)-I_E(N)
=\int_E S(\alpha)^2e(-N\alpha)(e(-j\alpha)-1)\,d\alpha.
\]
No approximation is involved. Taking absolute values yields only
\[
|\Delta_{E,j}(N)|\le\int_E|S(\alpha)|^2|e(-j\alpha)-1|\,d\alpha,
\]
which discards the phase needed to prove a signed lower bound.

## Rational-center multiplier calculation

Let $\alpha=a/q+\beta$, $(a,q)=1$, and $j\in\mathbb Z$. The shift multiplier at the center is zero exactly when $q\mid j$. Indeed, $e(-ja/q)=1$ iff $q\mid ja$, and coprimality makes this equivalent to $q\mid j$. On $|\beta|\le\delta$:
\[
q\mid j\quad\Longrightarrow\quad |e(-j\alpha)-1|\le2\pi|j|\delta.
\]
If $q\nmid j$, the center multiplier is at least $2\sin(\pi/q)$, and the reverse triangle inequality gives
\[
|e(-j\alpha)-1|\ge2\sin(\pi/q)-2\pi|j|\delta.
\]
These are exact Lipschitz consequences of $|e(t)-1|\le2\pi|t|$. The latter lower bound can be negative and then says nothing. In particular, for the standard major radius $\delta=P/(qX)$ it is useful only when $|j|P/(qX)$ is smaller than $\sin(\pi/q)$. It is not a uniform nonresonance estimate as $q$ grows.

For a fixed nonzero shift $j$, every resonance $q\mid j$ has $q\le|j|$. Thus for fixed $j$ and sufficiently large $P$, those rational centers lie among the major arcs. On the minor arcs the relevant approximating denominator is larger than $P$, but the nonresonant center multiplier can itself be only of order $1/q$; the perturbation radius and the denominator must be compared quantitatively. None of these multiplier facts bounds the phase or size of $S(\alpha)^2$.

## Why a positive arc Gram bound does not imply signed cancellation

For a finite shift set $J$ and disjoint measurable cells $E_s$, define
\[
G_s(j,k)=\int_{E_s}|e(-j\alpha)-1|\,|e(-k\alpha)-1|\,d\alpha.
\]
Each $G_s$ is positive semidefinite since it is a Gram matrix in $L^2(E_s)$. An upper bound on the norm of the increment vector follows by Cauchy and depends only on the arc budgets $B_s=\int_{E_s}|S|^4$. But the signed increment contains $S^2$, while the Gram contains only absolute multiplier magnitudes. Replacing the complex function $S^2e(-N\alpha)$ by an arbitrary function in the same norm ball gives the sharp Hilbert-space bound, and that relaxation has the one-hole extremizer in M2. To improve it one needs a lower bound on a phase-sensitive functional restricted to the actual prime-square polynomial.

A possible sufficient new input is a uniform, target-independent cell density theorem $B_s\le C X^2|E_s|^2$ for a specified partition of the minor arcs, with $C$ small enough relative to the major coefficient constant if the partition does not refine. If the maximum cell measure tends to zero and $\sum_s|E_s|\le1$, this condition would imply
\[
\sum_s|I_{E_s}(N)|\le\sum_s\sqrt{|E_s|B_s}
\le\sqrt C X\sum_s|E_s|^{3/2}
\le\sqrt C X\sqrt{\max_s|E_s|}.
\]
This conditional implication is rigorous. No such cellwise estimate for genuine primes is proved in this stage, and the cited global minor fourth moment does not imply it. Moreover, for finitely many cells of fixed measure, this estimate is only $O(X)$ and must have a constant strictly below the independently proved major lower-bound constant.

## Half-period and base-position check

When $w(2/X)=0$, only odd primes occur, so $S(\alpha+1/2)=-S(\alpha)$ and $S^2$ is $1/2$-periodic. On a reflection- and half-period-invariant set, even $N$ gives equal translated contributions, not cancellation. The exact base-position map $p=3+2a$ gives $S(\alpha)=e(3\alpha)F(2\alpha)$ and target coefficient $[F^2]_{N/2-3}$. It conjugates the same target phase and introduces no sign or density saving. Prime $3$ remains the index $a=0$.

**Potential circularity and first missing arithmetic fact.** A bound on $|e(-j\alpha)-1|$ or on the positive Gram matrix is not a bound on the sign of $\Delta_{\mathfrak m,j}(N)$. Any claim that it is must identify a missing phase estimate for actual prime coefficients. The first unavailable statement is a uniform bound on the signed minor coefficient or on a phase-sensitive family of its increments, valid for every prescribed $N\in H$ without selecting a prime pair at $N$.

## M3 verdict

The rational-center resonance calculation and phase identities are proved. The cellwise fourth-moment condition is a conditional sufficient criterion only. No prime-specific cell-density or signed-cancellation estimate is obtained.
