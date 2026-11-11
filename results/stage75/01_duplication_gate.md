# Stage 75 — Mandatory novelty and parity gate

**G75.0: NO-GO for another direct Type II proof attempt.** The gate precedes any new correlation estimate. The source audit seeks independent input; it does not continue the closed proof line.

## Definitions and inherited results

Keep $H=\{N\ge4:N\text{ even},N-1,N/2\text{ composite}\}$, $R(N)=\#\{p<q:p+q=N,\ p,q\text{ prime}\}$. The original cases remain prime-plus-one, twice a prime, and two distinct primes. The odd-prime coordinates remain $p=3+2a,q=3+2b,a+b=N/2-3$, including prime 3 at position zero. They do not imply simultaneous primality.

Fix the Stage 73 broad nonnegative $w\in C_c^\infty((0,1))$, positive on $[1/5,3/5]$. With $e(t)=\exp(2\pi it)$, retain exactly
$$S_X(\alpha)=\sum_p(\log p)w(p/X)e(p\alpha),\qquad r_X(N)=\int_0^1S_X(\alpha)^2e(-N\alpha)\,d\alpha.$$
The ordered weighted count $r_X$ differs from $R$. On $H$, $r_X>0$ implies $R>0$: $N/2$ is composite, so no equal-prime diagonal occurs. No actual prime coefficient is altered.

Put $h_N(t)=w(t/X)w((N-t)/X)$, $U=V=\max(1,\lfloor X^{1/5}\rfloor)$, $b_U(k)=\sum_{d\mid k,d>U}\mu(d)$, and extend $\Lambda(n)=0$ for $n\le0$. Define
$$G_X(N)=\sum_n\Lambda(n)\Lambda(N-n)h_N(n),\quad A_3(N)=\sum_{k>U,m>V\atop km<N}b_U(k)\Lambda(m)\Lambda(N-km)h_N(km).$$
The hyperbolic support, signed coefficient and genuine reflected factor remain intact. Let
$$F_X(N)=X\mathfrak S(N)J_w(N/X),\quad J_w(\tau)=\int w(u)w(\tau-u)\,du,$$
$$\mathfrak S(N)=2C_2\prod_{p\mid N,p>2}\frac{p-1}{p-2},\quad C_2=\prod_{p>2}\left(1-\frac1{(p-1)^2}\right)>0.$$
The following are **inherited project deductions**, not new arithmetic estimates:

1. T73.5: $G=\mathcal M_I+A_3+E_I$, where $E_I=O_{A,w}(X\log^{-A}X+X^{2/5}\log^3X)$ uniformly in $N\in[X/2,X]$, for each fixed $A>0$.
2. T74.3: $\mathcal M_I=F_X+E_K$, $E_K=O_w(X\exp(-c\sqrt{\log X}))$, uniformly for positive even $N\le X$.
3. Stage 72–73: $P_X:=G_X-r_X$ satisfies $0\le P_X\le D_X=4C_{\rm Ch}\|w\|_\infty^2\sqrt X\log X$ for $X\ge16$, with any valid fixed Chebyshev constant.

The complete Stage 74 report, adversarial review, manifest and ledger were read, alongside the earlier obligation passages. All hashes listed in its manifest are checked unchanged. No Type I computation is repeated.

## T75.1 — exact duplication after centering

**PROVED HERE, algebraic dependency check.** Uniformly on $\mathcal H_X=H\cap[X/2,X]$,
$$\boxed{A_3(N)=r_X(N)-F_X(N)+e_X(N),\quad e_X=P_X-E_K-E_I,\quad \sup_{N\in\mathcal H_X}|e_X(N)|=o_w(X).}$$
**Proof:** substitute the first two inherited identities into $r_X=G_X-P_X$ and rearrange. Each error divided by $X$ tends to zero uniformly. The sign of $P_X$ in $e_X$ is positive. For an empty target set use error supremum zero. This assumes no representation exists.

Hence uniform $A_3=o_w(X)$ is equivalent to uniform $r_X=F_X+o_w(X)$. It is exactly the Stage 73 centered obligation C73.C, since $F_X-\mathcal M_I=o_w(X)$. This is a quantitative Hardy–Littlewood-strength assertion, stronger than bare existence, not new independent input.

For precise lower bounds fix $\lambda\ge0$. The assertion
$$\forall\epsilon>0\ \exists X_\epsilon\ \forall X\ge X_\epsilon\ \forall N\in\mathcal H_X:\quad A_3(N)\ge-(\lambda+\epsilon)X$$
is equivalent to the same quantified assertion with $r_X(N)\ge F_X(N)-(\lambda+\epsilon)X$. In either direction apply the premise with $\epsilon/2$ and use $|e_X|\le\epsilon X/2$. This independently checks both implications. An exact finite boundary without slack does not follow merely from an $o(X)$ relation.

With $m_w=\min_{[9/40,21/40]}w>0$ and $c_w=C_2m_w^2/10$, the inherited continuum argument gives $F_X\ge c_wX$. The missing uniform inequality $A_3\ge-c_wX/2$ would give $r_X\ge c_wX/4$ once $|e_X|\le c_wX/4$. This is **conditional only**: no premise, effective cutoff or finite connection is supplied.

## Reconciliation with Stages 69–74

| Prior obligation | Relation to this gate |
|---|---|
| Stage 69 signed prime-only coefficient with strict margin | Same fixed-target difficulty; no numerical equivalence of every certificate is asserted |
| Stage 70 deletion and Stage 71 matching sensitivity | Need information beyond deletion-stable mass, fixed AP profiles and relative global norms |
| Stage 72 complement margin or $G_X>D_X$ | Sufficient threshold; not equivalent to an $X$-sized lower bound |
| Stage 73 C73.C: $A_3-[F_X-\mathcal M_I]=o_w(X)$ | Precisely equivalent to the strong proposal, by T74.3 |
| Stage 74 O74.1: actual-prime signed Type II lower margin | The same remaining lower-bound obligation with centering evaluated |

T73.4/N73.1 preserve leading fixed rational-core profiles under target-erasing deletion, not positivity. The desired positive correlation fails in the enlarged class of modified prime subsets. This rules out its deduction from the named deletion-stable premises for that class. It does **not** refute an actual-prime theorem. Exact Vaughan structure with unchanged $\mu$ and maximal Bombieri–Vinogradov precision are not claimed to survive deletion. Full-prime hypotheses must be checked separately; naming the immutable sequence supplies no signed estimate by itself.

**Disposition:** close the duplicated direct Type II line. Continue only the authorized primary-source applicability audit. No direct proof attempt, Type I reevaluation, wheel calculation or finite Goldbach search is undertaken.
