# Stage 66 — Sharp local energy and the genuine-prime pointwise gap

**Research status:** completed as a rigorous obstruction study. The original three-case conjecture remains open. No universal Goldbach claim is made.

## A. Proven mathematical results

Let $c\in\ell^2(\mathbb Z)$, $|c(N)|\ge A>0$, and let $I$ be any finite set of distinct nonzero shifts with $|c(N+h)-c(N)|\le d_h$. Then
$$\|c\|_2^2\ge A^2+\sum_{h\in I}(A-d_h)_+^2.$$
This is sharp for arbitrary complex sequences, with an explicit finite-support extremizer. Thus for a global budget $B$, the displayed lower bound is the exact minimum compatible energy. Its sharpness is abstract and says nothing about which sequences arise from primes.

For the parity-preserving shifts $\pm2h$, $1\le h\le H$, and $d_{\pm2h}=Lh$, the exact necessary budget is
$$B\ge A^2+2\sum_{h=1}^H(A-Lh)_+^2.$$
For $L>0$, put $J=\min(H,\max(0,\lceil A/L\rceil-1))$. Then the sum is
$$A^2+2\left(JA^2-ALJ(J+1)+\frac{L^2J(J+1)(2J+1)}6\right);$$
for $L=0$ it is $(2H+1)A^2$. When $H\ge\lceil A/L\rceil$ and $A/L\to\infty$, this is $2A^3/(3L)+O(A^2+AL)$.

A sharp aggregate variant follows from convexity. If $J$ contains $m$ distinct nonzero shifts and $\sum_{j\in J}|c(N+j)-c(N)|^2\le V$, then
$$\|c\|_2^2\ge A^2+m\left(A-\sqrt{V/m}\right)_+^2.$$
Equal increments attain equality. For $B>A^2$ and $0<B-A^2<mA^2$, this lower bound excludes a center under budget $B$ precisely when
$$V<m\left(A-\sqrt{(B-A^2)/m}\right)^2.$$
This optimizes the inference from this aggregate input; it is not an arithmetic variation estimate.

## B. Exact identities and computational observations

For $m_w(n)=\int_{\mathfrak m}S_w(\alpha)^2e(-n\alpha)\,d\alpha$,
$$m_w(N+2h)-m_w(N)=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)(e(-2h\alpha)-1)\,d\alpha.$$
The sum square $S_w^2$ selects prime sums; replacing it by $|S_w|^2$ changes the problem to prime differences. Full-circle Cauchy–Schwarz gives only $\sqrt{2B_X}$ for each nonzero increment. For $m$ distinct shifts the fixed-target increment-vector bound is $(m+1)B_X$. Summing over all targets gives an average bound $4B_X$ per nonzero shift, not a bound for a prescribed target.

For unordered distinct-prime representation sets, at one target $R(n)^2=R(n)+Q(n)$, where $Q(n)=R(n)(R(n)-1)$ consists solely of four-distinct-position terms. At distinct targets $u,v$, $R(u)R(v)=S(u,v)+T(u,v)$, partitioned into exactly-one-shared-prime and four-distinct configurations. The exact normalized difference identity and multiplicities are in `03_fourprime_signed_energy.md`.

Finite checks: the original verifier passed 300 rational Lipschitz cases. The new Python verifier passed 22,140 rational aggregate vectors and 3,422 ordered distinct-target partitions (even targets 4–120). The independent SageMath verifier passed 260 Lipschitz cases, 8,400 aggregate vectors, 8 Gram-matrix sizes and 2,352 ordered distinct-target partitions (even targets 4–100). Stage 65’s corrected sum/difference and localized-kernel Python/Sage tests, plus selected Stage 61/62/64 checks, also passed. See the manifest for exact commands, versions, runtimes and hashes. These are finite computations only.

## C. Refuted approaches

- A global fourth moment does not imply pointwise control: a sequence supported at one index is an abstract countermodel whenever its single squared value is within the global budget. The first invalid implication is converting an average $\ell^2$ budget into a pointwise small bound.
- The full-circle multiplier norm is exactly $2$ for every nonzero integer shift. The unsupported step in a proposed $O(h/X)$ bound is discarding rational arcs where the multiplier is not small.
- A wheel-210 count, even with an equal wheel factor or equal singular-series normalization, does not encode primality of reflected endpoints or membership in the residual set. Stage 62’s unbounded singular-series variation is a model theorem, not a prime-count theorem.
- A pair anchored at the target cannot be selected in the zero-representation case. This invalidates representation-anchored proofs of the missing case.
- Nonnegative four-prime counts do not determine the sign of the normalized difference identity; the relative self/cross-correlation magnitudes remain uncontrolled.

## D. Conditional result

If an independently justified major-arc estimate gives $a_w(N)\ge A_X>0$, and independent genuine-prime estimates give even-shift increment bounds $d_{X,N}(h)$, then a zero representation at $N$ is excluded whenever
$$A_X^2+2\sum_{h=1}^H(A_X-d_{X,N}(h))_+^2>B_X.$$
Under the cited conditional scale $A_X\asymp X$, $B_X\ll X^{5/2}(\log X)^{100}$, the Lipschitz route requires roughly $L\lesssim X^{1/2}(\log X)^{-100}$ and shift span $H\gtrsim A_X/L$, with sufficient constants. This is a conditional implication, not a proved prime modulus.

## E. Remaining analytic obstruction

No source in the inherited literature audit gives a target-uniform signed minor-arc increment or block-variation estimate at the required scale. The first missing theorem is a quantitative bound for the prime-weighted, target-twisted minor-arc integral with multiplier $e(-2h\alpha)-1$, or a strong enough target-specific aggregate bound for a finite block of even shifts. It must state all uniformities and its dependence on the common zero-free hypothesis. Existing exceptional-set and global moment estimates allow an isolated target and do not fill this gap.

The residual set remains $H=\{N\ge4:N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\}$. Its base-3 *position coordinate* (prime positions $3+2a$ and $3+2b$ with $a+b=N/2-3$) is an algebraic reflection, not evidence that both endpoints are prime. The cases $N=p+1$ and $N=2p$ are excluded on $H$; the outstanding case is still an unproved distinct-prime pair.

## F. Next objective

Stage 67 should prove or refute a **rational-arc resolved increment inequality**: decompose the exact multiplier by reduced denominator $q$, separate $q\mid 2h$ from $q\nmid2h$, and determine whether any available prime-only fourth-moment input yields a target-specific saving after summing those arc contributions. First establish the sharp algebraic upper bound and its extremizers for the arc-weighted Gram matrix; then compare it with all unconditional/conditional source hypotheses. If no saving follows from the available norms, give an explicit abstract countermodel and state the first needed prime-correlation estimate. No finite-range extension is needed unless it tests a new inequality.

## Reproducibility

Run `python3 -B results/stage66/verify_stage66.py`, `python3 -B results/stage66/verify_stage66_aggregate.py`, and `sage -python results/stage66/verify_stage66_sage.py` from the repository root. Machine-readable results and SHA-256 provenance are in this directory.
