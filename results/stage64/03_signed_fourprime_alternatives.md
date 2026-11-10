# Stage 64 — Signed four-prime correlations and residual arithmetic

## 1. Exact unweighted expansion

For an even integer $t$, define the finite set
\[
\mathcal R(t)=\{\{p,q\}:p<q,\ p,q\text{ prime},\ p+q=t\},
\qquad R(t)=|\mathcal R(t)|.
\]
This is the repository's distinct, unordered count. For distinct even targets $n<m$, partition $\mathcal R(n)\times\mathcal R(m)$ according to whether the two representations share a prime position. They can share at most one prime: sharing both would force their sums equal. Thus the exact identity is
\[
R(n)R(m)=S(n,m)+Q_4(n,m),
\]
where
\[
S(n,m)=\sum_{\substack{x\text{ prime}\\n-x,m-x\text{ prime}}}
\mathbf 1_{x\ne n-x}\mathbf 1_{x\ne m-x}
\]
counts the shared-prime configurations once by their unique shared prime, and $Q_4(n,m)$ counts ordered pairs of representations with four distinct prime positions. If a shared prime is $x$, the other two positions are forced to be $n-x$ and $m-x$; hence this formula includes no extra orientation factor. For $n=m$, two distinct unordered representations cannot share exactly one prime, since their other prime must also agree. The same-target decomposition is instead
\[
R(n)^2=R(n)+Q_4(n,n),
\]
where the first term is the diagonal of identical unordered representations and $Q_4(n,n)$ counts ordered pairs of disjoint representations.

With weights $W_t(\{p,q\})=\log p\log q$, multiplication and the same partition give an exact weighted identity. The shared term is
\[
S_{\log}(n,m)=\sum_{\substack{x\text{ prime}\\n-x,m-x\text{ prime}}}
\mathbf1_{x\ne n-x}\mathbf1_{x\ne m-x}(\log x)^2\log(n-x)\log(m-x).
\]
The four-distinct term is the sum of $W_nW_m$ over the disjoint pairs. For $n=m$, the diagonal contributes $\sum_{\{p,q\}\in\mathcal R(n)}(\log p\log q)^2$. These are exact algebraic partition identities; they are not estimates for either term.

The exclusions have a concrete role. The set $\mathcal R(t)$ excludes the equal-prime diagonal. If instead one uses all unordered representations including $p=q$, the shared formula and same-target diagonal must be changed. On the residual set $H$, $N/2$ is composite, so the equal-prime prime diagonal is absent. Small primes are not otherwise discarded. For every even $N>4$, no prime-pair representation can contain 2: the complementary integer $N-2>2$ is even and therefore composite. At $N=4$, the sum $2+2$ is a prime diagonal and is excluded by the requirement $p<q$. Thus the prime 2 never occurs in the distinct unordered representations counted by $R(N)$. The open prime variables in all formulas mean genuine primes, not merely residues surviving a wheel.

## 2. What the signed identity does not imply

After centering by any independently fixed real model $\mu_t$, the exact algebra is
\[
(R(n)-\mu_n)(R(m)-\mu_m)
=S(n,m)+Q_4(n,m)-\mu_mR(n)-\mu_nR(m)+\mu_n\mu_m.
\]
This rearrangement supplies no sign for the centered expression. If $R(n)=0$, the left side is $-\mu_n(R(m)-\mu_m)$, and the positive raw terms $S,Q_4$ are constrained by the product identity to sum to zero. Since they count nonnegative configurations, both are then zero. They do not produce a contradiction unless one has independently proved a positive lower bound for a target-anchored shared or disjoint correlation that does not assume a representation of $n$. Any estimate whose proof selects or normalizes by an element of $\mathcal R(n)$ is circular under the zero case.

This identifies the first failed use of “four-prime positivity”: positivity of a combinatorial count is not a positive lower bound. Four distinct prime positions are a simultaneous primality event, and modular admissibility alone cannot guarantee it.

## 3. Local wheel and singular-series data do not encode membership in $H$

Take $N=210$ and $M=420$. Both are even and congruent to zero modulo 210. Define
\[
A_{210}(t)=\#\{a\pmod {210}:(a,210)=1,\ (t-a,210)=1\}.
\]
At $t\equiv0\pmod{210}$, the second coprimality condition is identical to the first, so $A_{210}(210)=A_{210}(420)=\varphi(210)=48$. Equivalently, the local product is $(2-1)(3-1)(5-1)(7-1)=48$.

The conventional even Goldbach singular series is
\[
\mathfrak S(t)=2C_2\prod_{\substack{p\mid t\\p>2}}\frac{p-1}{p-2}.
\]
The distinct prime divisors of 210 and 420 above 2 are both exactly $3,5,7$, hence $\mathfrak S(210)=\mathfrak S(420)$ exactly, including the common infinite Euler product $2C_2$. Yet $210\in H$: $210-1=209=11\cdot19$ and $210/2=105=3\cdot5\cdot7$ are composite. But $420\notin H$, because $420-1=419$ is prime (trial division by primes at most $\sqrt{419}<21$ suffices), although $420/2$ is composite.

Therefore neither the wheel factor nor the full singular-series value determines the residual-set predicate, even for these two explicit targets. This refutes the implication “identical wheel/singular-series data force identical residual status.” It does **not** refute a stronger theorem that uses additional arithmetic information about $N-1$ or $N/2$.

## 4. Position coordinates and local sieves

For odd prime positions $p>3$, writing $p=3+2a$ is a bijection between odd integers $p>3$ and integers $a\geq1$. Primality of $p$ remains an extra condition; the coordinate change is not a distribution theorem. The even prime $p=2$ must be split off as described above. Modulo 210, the necessary conditions that both $p$ and $N-p$ avoid $2,3,5,7$ can be counted exactly, but they are only necessary local conditions. The Stage 62 arithmetic model already shows that singular-series profiles can vary without representing actual prime-pair counts; Stage 64's 210/420 pair adds that the residual predicate itself is not a function of these local factors.

No new sieve inequality was found that transforms the residue conditions plus compositeness of $N-1,N/2$ into a lower bound for simultaneous primality. A sieve upper bound on candidates is in the wrong direction for this purpose. A lower-bound sieve for two prime variables would face the parity obstruction; nothing in the reviewed results removes it in a target-specific way.

## 5. Pointwise alternatives and precise obligations

| Proposed route | Exact useful statement required | First missing step / circularity audit | Status |
|---|---|---|---|
| Signed minor arc | $m_w(N)>-a_w(N)$ for every sufficiently large $N\in H$, with explicit fixed arcs and independently proven $a_w(N)\geq cX$. | Li–Liu's global fourth moment only yields a count $O(X^{1/2}\log^{100}X)$ of potential failures. No per-target signed estimate is supplied. | **Open**; see `02_fourth_moment_to_pointwise_gap.md`. |
| Local covariance/PSD | A positive lower bound for an anchored quadratic form for all admissible target data, with constants independent of $R(N)$. | Positive semidefiniteness gives Cauchy–Schwarz constraints among correlations but does not make an individual coordinate positive. If the anchor is normalized by a prime representation at $N$, the premise assumes the conclusion. | **No new estimate**; deterministic linear algebra alone is insufficient. |
| Weighted graph or block energy | An independently established mean and an upper bound on all relevant energy below the zero-coordinate threshold. | Stage 58–63 exact optimizations refine constants but do not produce arithmetic means/energies. Stage 63's $o(X^2)$ von Mangoldt energy remains open. | **Conditional only**. |
| Congruence/sieve restriction | A theorem that the simultaneous prime-position set for every $N\in H$ has positive cardinality. | Congruence admissibility does not imply prime values; no target-uniform lower sieve estimate is proved. | **Open**. |
| Singular-series lower bound | A lower bound for the formal main term. | $\mathfrak S(N)\geq2C_2$ controls the expected main term, not the signed error. Example 210/420 shows the factors do not encode $H$. | Main-term fact **proved**; positivity inference **refuted** absent an error estimate. |

## Classification

- **Proved in this report:** the exact combinatorial identities and the explicit arithmetic distinction between 210 and 420.
- **Finite computational verification:** identity multiplicities checked in Python and SageMath in `tests/`; this is supplementary to the direct proofs.
- **Refuted:** inferring residual membership from wheel/singular-series data alone, and inferring pointwise positivity from the stated global fourth-moment bound alone.
- **Open:** every signed, target-specific estimate that would force $R(N)>0$ for all $N\in H$.
