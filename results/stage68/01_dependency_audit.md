# Stage 68 M0 — dependency and hostile proof audit

## Verdict

The abstract formulas in the starting note survive, with two qualifications made explicit here: the exact budget identity is an unrestricted complex $L^2$ optimum, and the simple eigenvalue-sum bound is an equality only when all active top eigenspaces have a common unit vector. A concrete pair of rational-centered interval Grams verifies that the latter condition can fail for the actual multipliers. None of these statements is a prime-arithmetic estimate.

## Conventions re-derived

Set $e(t)=\exp(2\pi i t)$ and $\widehat F(n)=\int_{\mathbb T}F(\alpha)e(-n\alpha)\,d\alpha$. For $S_w(\alpha)=\sum_p a_p e(p\alpha)$ with $a_p=(\log p)w(p/X)$,
\[
S_w^2=\sum_{p,q}a_pa_qe((p+q)\alpha),\qquad |S_w|^2=\sum_{p,q}a_pa_qe((p-q)\alpha).
\]
Thus the first is the ordered prime-sum polynomial; the second is a prime-difference polynomial. The identity for $\Delta_j(N)$ must use $S_w^2$ and the multiplier $e(-j\alpha)-1$.

With $g_j=e(-N\alpha)(e(-j\alpha)-1)$, $G_E(j,k)=\int_Eg_j\overline{g_k}$. Its entry formula is $\mu_E(k-j)-\mu_E(-j)-\mu_E(k)+\mu_E(0)$, and $z^*G_Ez=\int_E|\sum_j\overline z_jg_j|^2$. This orientation is consistent with the bilinear map $f\mapsto(\int fg_j)_j$: in the inner product linear in the first slot its adjoint is $z\mapsto\sum_jz_j\overline{g_j}$, so $DD^*=G_E$.

For real coefficients the full Fourier coefficient is real. A restricted coefficient is real if its region is reflection invariant; otherwise only its real part may be used in a sign argument. The equality $r_w(N)=a_w(N)+m_w(N)$ is exact for a disjoint major/minor partition.

## Dependency table

| Claim used | Exact hypotheses/dependency | Arithmetic input | Adversarial check | Status |
|---|---|---|---|---|
| $\Delta_j(N)=\int_{\mathfrak m}S_w^2e(-N\alpha)(e(-j\alpha)-1)$ | Fourier coefficient convention above | None | Expansion fixes the minus sign; $|S|^2$ gives differences | PROVED identity |
| $G_E$ formula and PSD | Measurable $E$, finite distinct nonzero shifts | None | Direct expansion and integral of a square | PROVED |
| Exact allocation (A) | Pairwise disjoint $E_r$; independent complex $L^2$ balls | None | Both proofs and interval example in 02 | PROVED, abstract |
| Uniform Gram bound (C) | Finite $J$, arbitrary size depending on $X$ | Major set has measure $\mu$ | Loewner order and all-ones Rayleigh quotient | PROVED, geometric |
| Parseval energy | $F=1_{\mathfrak m}S_w^2\in L^2$ | Prime polynomial only in identifying coefficients | $\sum_n|m_w(n)|^2=\int_{\mathfrak m}|S_w|^4$ | PROVED identity |
| Missing target forces $m_w(N)=-a_w(N)$ | $w\ge0$, and full coefficient is the weighted ordered pair count | Genuine primes; $a_w(N)>0$ supplied by major-arc theorem | If $w$ vanishes at every pair, converse need not hold; only missing implies zero | PROVED implication |
| Stage66 aggregate energy obstruction | $m$ distinct shifts, central modulus at least $A$, increment energy at most $V$ | None | Sharp finite vector extremizer is documented in Stage66 | PROVED |
| Certificate (F) implies representation | Prior rows, independently valid $\bar B_r,\bar V$ | Pointwise major term and minor bounds | Strict inequality contradicts Parseval energy | CONDITIONAL |
| Universal $R(N)>0$ on $H$ | Would need all preceding hypotheses and a strict criterion for all sufficiently large targets | New genuine-prime pointwise estimate missing | Exceptional-set bounds permit singleton | OPEN |

## Endpoint and weight audit

The residual set remains $H=\{N\ge4:N$ even, $N-1$ composite, $N/2$ composite$\}$. The original three alternatives remain $N=p+1$, $N=2p$, and $N=p+q$ with $p<q$; the equality $N-2p=2q-N$ is algebraic once $p+q=N$ and is no primality fact. On $H$, $N/2$ composite excludes the diagonal. For even $N>4$, if one summand is 2 the other is the even number $N-2>2$, not prime. $N=4$ has only the excluded diagonal $2+2$ and lies outside $H$; $N=6,8$ lie outside $H$ because $N-1$ is prime.

For $w\in C_c^\infty((0,1))$, put $\alpha_w=\inf\operatorname{supp}w>0$. The weight excludes 2 when $2/X<\alpha_w$ (equivalently $X>2/\alpha_w$); no numeric endpoint is assumed. Nonnegative weights make the full coefficient nonnegative, and a positive coefficient supplies a genuine prime pair with positive weights. A zero weighted coefficient does not in general imply absence of an unweighted pair.

## First invalid implications found in inherited approaches

1. Replacing $S_w^2$ by $|S_w|^2$ in a target sum coefficient changes $p+q=N$ into $p-q=N$ (Stage65 erratum; exact counterexample there).
2. Inferring a useful complete-minor Gram saving from a small selected resonant arc ignores the complementary minor set. Its first failure is the unproved passage from a local arc bound to the full signed increment.
3. Inferring target positivity from an exceptional-set estimate $O(X^\delta)$ with $\delta>0$ fails because such a set may contain one target.

No defect was found in the formulas (68.1)–(68.7) after the scope and equality qualifications above.
