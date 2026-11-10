# M4 — Exact shifted representation correlation ledger

Let $a_p\ge 0$ be any finitely supported weights on genuine primes and put
\[
r(N)=\sum_{p+q=N}a_pa_q.
\]
For $N\in H$, every representation is off diagonal, so if $\mathcal P_N$ denotes the unordered prime pairs $\{p,q\}$ with $p<q$ and $p+q=N$, then
\[
r(N)=2\sum_{A\in\mathcal P_N}v_A,\qquad v_{\{p,q\}}=a_pa_q.
\]
This notation separates the exact combinatorics from any heuristic for prime correlations.

## Distinct targets

Take $N,N+j\in H$ with $j\ne0$. Expanding the product and sorting unordered pair configurations gives
\[
\boxed{r(N)r(N+j)=4\sum_{\substack{A\in\mathcal P_N,\ B\in\mathcal P_{N+j}\\A\cap B=\varnothing}}v_Av_B
+4\sum_{x\in\mathbb P}a_x^2a_{N-x}a_{N+j-x}.}
\]
In the second sum, both complementary entries must be primes with positive weights and both unordered pairs must be off diagonal. The shared prime is exactly $x$. Two shared primes would force the unordered pairs to be identical and hence their sums equal, contrary to $j\ne0$. Conversely, every pair of representations sharing one prime has a unique shared prime, so the sum counts it once. Each unordered representation has two orientations at each target, producing multiplicity $2\cdot2=4$ in both terms. There is no configuration sharing exactly two prime positions for distinct targets.

An entirely independent ordered-position derivation starts with the four ordered variables $(p,q,r,s)$ subject to $p+q=N$ and $r+s=N+j$. For a shared value, one of $p,q$ equals one of $r,s$: there are four possible position equalities. The four equality sums are equal after swapping the two coordinates within either pair; since $j\ne0$, their intersections are empty. Their total is therefore the displayed factor $4$ times the one-variable sum. The remaining quadruples have four distinct prime values and give the disjoint-pair term. This independently confirms the multiplicity.

The shared term is a genuine three-prime-position correlation with a square weight on the anchor. Its nonnegativity is exact, but an upper bound or asymptotic for its average does not imply a positive value at a specified $N$. Using an anchor $x$ for which both complementary entries are prime at the target already assumes that target has the representation under investigation.

## Coincident target

For $j=0$, classify two unordered representations at the same target. A diagonal-in-pair configuration $A=B$ contributes $4v_A^2$. Distinct unordered pairs cannot share exactly one prime: a common prime $x$ forces both complements to equal $N-x$, and hence forces the pairs to be identical. Thus
\[
r(N)^2=4\sum_{A\in\mathcal P_N}v_A^2
+8\sum_{\substack{A,B\in\mathcal P_N\\A<B}}v_Av_B.
\]
The coefficient $8$ is the two ordered choices of the distinct unordered pairs times four orientations. On $H$ there is no prime diagonal $p=q=N/2$; outside $H$ its ordered contribution must be added separately.

## Scope

These identities remain valid for zero weights and do not infer the existence of any prime pair. They are finite exact identities. To turn them into a target-specific lower bound one still needs arithmetic information on the disjoint four-prime term or on the signed Fourier coefficient; the decomposition alone is not such information.
