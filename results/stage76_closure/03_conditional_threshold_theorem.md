# T76.1 — Conditional critical threshold and precise parity obstruction

## Quantified conditional theorem

Fix $w\ge0$ smooth and compactly supported in $(0,1)$, positive on $[1/5,3/5]$. Put $D=H\cup H_1$, $m_w=\min_{[9/40,21/40]}w>0$, $c_w=C_2m_w^2/10$, and retain the actual-prime definitions of L76.1. Suppose, independently of target positivity,
$$\exists X_0\ \forall X\ge X_0\ \forall N\in D\cap[X/2,X]:\quad A_3(N)\ge-\tfrac12c_wX.\tag{U}$$
Then there exists $X_1\ge X_0$ such that for all $X\ge X_1$ and every such target, $r_X(N)\ge c_wX/4>0$, hence $R(N)>0$. There is no conclusion at every $X\ge X_0$ unless $X_0$ also dominates the analytic error cutoffs. No effective $X_1$ or finite connection is proved.

**Proof.** For $\tau\in[1/2,1]$, the interval $[\tau/2-1/40,\tau/2+1/40]$ has length $1/20$ and both arguments $u,\tau-u$ lie in $[9/40,21/40]$. Therefore $J_w(\tau)\ge m_w^2/20$. For positive even $N$, $\mathfrak S(N)\ge2C_2$, so $F_X(N)\ge c_wX$. By L76.1 choose one $X_1\ge X_0$ so that $\sup_{D\cap[X/2,X]}|e_X|\le c_wX/4$ for all $X\ge X_1$. Then
$$r_X=F_X+A_3-e_X\ge c_wX-\tfrac12c_wX-\tfrac14c_wX=\tfrac14c_wX.$$
Both endpoints are genuine primes by definition of $r_X$. Since $N/2$ is composite throughout $D$, they are distinct. This proves the conditional implication only; (U) remains OPEN.

## Necessary and sufficient asymptotic equivalence

Uniformly on the same combined target domain,
$$\sup_N|A_3(N)|=o_w(X)\iff\sup_N|r_X(N)-F_X(N)|=o_w(X).$$
The exact relation $A_3=r_X-F_X+e_X$ proves each direction by the triangle inequality. Necessity is for the weighted Hardy–Littlewood asymptotic, not for mere existence of a prime representation. The error is absolute, not relative to a growing singular series. A sufficiently broad fixed weight is essential to the positive threshold, though the algebraic error identity itself does not require the extra positivity interval.

## L76.2 — finite matching deletion cost

Let a finite matching have disjoint edges $(p_i,q_i)$, $p_i+q_i=N$, $p_i<q_i$, with nonnegative real weights $a_n$. Set $r_a(N)=2\sum_i a_{p_i}a_{q_i}$; isolated vertices contribute no target product. Among coordinatewise attenuations $0\le b\le a$ with $r_b(N)=0$,
$$\min\sum_n(a_n-b_n)=\tau_N:=\sum_i\min(a_{p_i},a_{q_i}).$$
**Lower bound:** all products are nonnegative, so each must be zero. At least one endpoint of every edge is zeroed; its cost is at least that edge's smaller original weight. Disjointness lets these costs be summed without double counting. **Attainment:** zero a smaller endpoint on every edge, keep the other and all isolated vertices unchanged. This has exactly the asserted cost. Ties and zero original weights cause no difficulty. For nonnegative weights, $\tau_N=0$ does not imply the edge set is empty; the stronger historical iff uses strictly positive edge weights. An arbitrary nonnegative perturbation, even if increases are permitted, cannot have smaller L1 cost: every zero product still forces deletion of one original endpoint, and increases only add cost.

The vanishing relative-norm consequence is NOT a finite matching theorem for arbitrary weights. For example, one abstract edge with endpoint weights 1 and 1 has deletion cost 1 and total mass 2, a ratio of 1/2; repeating that weighted model at each scale does not make the ratio vanish. For actual coefficients $a_p=(\log p)w(p/X)$ it uses the established unconditional prime-pair upper sieve and weighted PNT, as in Stages 70–71. The sieve applies to all sufficiently large even targets, not just those with $N-1$ composite; no diagonal exists on $D$. Thus uniformly on $D\cap[X/2,X]$,
$$\tau_N\ll_w X\log\log X/\log X=o_w(X),\quad \sum_p a_p\asymp_w X.$$
If $d=a-b$, then $\sum d_p^2\le\|w\|_\infty\log X\,\tau_N\ll_w X\log\log X$. PNT gives $\|S_X\|_2^2\asymp_w X\log X$, so $\|S_X-S'_X\|_2/\|S_X\|_2\to0$, while $r_b(N)=0$. The fixed-q interpolation and square-polynomial factorization in Stage 71 give the inherited global-norm versions; no estimate is asserted for q growing with X. These asymptotic deductions are not Lean-certified or proved by finite endpoint-cover tests.

## Exact scope of the adversarial no-go

Let $\mathcal C_X$ be a class of nonnegative prime-supported coefficient sequences containing both the full sequence $a$ and its target-erasing attenuation $b$. Let data $\mathcal I$ and a proposed certificate depend only on information unchanged (or retained to the exact stated tolerance) under this attenuation. If a sound implication from those data claims $r_c(N)>0$ for every admissible $c\in\mathcal C_X$, then applying it to $b$ contradicts $r_b(N)=0$. Hence those data cannot certify a strict target-positive margin in that enlarged class.

To phrase the contradiction on the threshold scale define the model remainder $T_c=r_c-F_X$, keeping the external target main term fixed. Then $T_b=-F_X\le-c_wX$, which fails $T_b\ge-c_wX/2$. With a model reduction error uniformly $o(X)$, the same contradiction persists for large $X$. The tolerance itself must preserve the certificate's hypotheses; coarse relative norm closeness is not equality of every statistic.

**Crucial distinction:** $T_b$ is not asserted to equal the actual Vaughan $A_3$ computed with unchanged Mobius coefficients. Exact Vaughan structure and maximal BV precision were never claimed deletion-stable. Thus the no-go rules out an enlarged-class argument using ONLY deletion-stable premises. It does not prove that every identity about immutable primes fails, refute (U) for actual primes, or rule out an independent arithmetic mechanism not stable under deletion. The threshold remains NO-GO under the named premises, and OPEN for immutable actual primes.

## Scientific closure

No new signed arithmetic estimate is established. L76.1 repairs a logical domain boundary without proving its arithmetic coverage; L76.2 records finite sensitivity and explicitly separates its external asymptotic inputs; T76.1 is conditional. The direct deletion-stable Type II line stays closed. Strong Goldbach remains OPEN.
