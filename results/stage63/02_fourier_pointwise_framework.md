# Stage 63 M2: target-anchored prime Fourier coefficient

## Exact coefficient identity

Let `e(t)=exp(2 pi i t)` and define the finite prime polynomial

$$S_N(\alpha)=\sum_{p\le N,\ p\text{ prime}}(\log p)e(p\alpha).$$

Expanding the square gives a finite sum. Since

$$\int_0^1 e(k\alpha)\,d\alpha=\begin{cases}1&k=0,\\0&k\in\mathbb Z\setminus\{0\},\end{cases}$$

only ordered prime pairs with `p+q=N` remain. Each distinct unordered pair occurs in both orders, while `p=q=N/2` occurs once. Therefore, exactly,

$$\int_0^1 S_N(\alpha)^2e(-N\alpha)\,d\alpha
=2\sum_{p<q,\ p+q=N}\log p\log q
+\mathbf 1_{N/2\text{ prime}}(\log(N/2))^2.$$

The integral is real because it equals the real coefficient on the right. For residual `N` in the project's set `H`, `N/2` is composite, so the diagonal vanishes. Since each prime logarithm is positive, the full integral is positive if and only if `R(N)>0`. This is a restatement as an exact coefficient, not an estimate or a proof of positivity. The weighted sum is not `R(N)`.

## Explicit measurable arc partition and sufficient estimate

Fix integers `N>=4` and `1<=Q<N/2`. Regard `[0,1)` as the circle, with circular distance `||x||=min_{k in Z}|x-k|`. Define the measurable set

$$\mathfrak M(N,Q)=\bigcup_{1\le q\le Q}\ \bigcup_{0\le a<q,\ (a,q)=1}\{\alpha\in[0,1):\|\alpha-a/q\|\le Q/N\},$$

and let `m(N,Q)=[0,1)\\mathfrak M(N,Q)`. This union convention handles overlap and the endpoints on the circle. Let

$$g_N(\alpha)=\operatorname{Re}(S_N(\alpha)^2e(-N\alpha)),\quad I_M(N,Q)=\int_{\mathfrak M}g_N,\quad I_m(N,Q)=\int_m g_N.$$

Then `I_M+I_m` equals the full coefficient exactly. A sufficient route to universal coverage is to prove, for each `N in H` beyond an explicit `N_0`, independently justified bounds `I_M(N,Q)>=M_N` and `|I_m(N,Q)|<=E_N` with explicit constants and `M_N>E_N`, and to verify the finitely many residual targets `N<=N_0` exactly. Equivalently, the narrow signed minor-arc obligation is `I_m(N,Q)>-M_N`, when an independently established major-arc lower bound `M_N` is available. Neither the major lower bound nor this target-uniform minor-arc inequality is established here. A positive formal singular series alone is not either estimate.

For this explicit partition, the narrowest missing analytic statement has to hold for every residual target in the claimed range, not merely on average: given fixed explicit `Q(N)`, `N_0`, and an independently proved lower bound `M_N>0`, show `I_m(N,Q(N))>-M_N` for every `N in H, N>N_0`. No source checked in this stage supplies such constants/cutoff. Stating this conditional sufficient criterion does not make the missing inequality unconditional.

## Comparison with von Mangoldt weights

Let `Lambda(n)=log p` if `n=p^k` for a prime `p` and integer `k>=1`, and zero otherwise. The coefficient

$$C_\Lambda(N)=\sum_{a+b=N,\ a,b\ge1}\Lambda(a)\Lambda(b)$$

contains the prime-only ordered coefficient as its `a,b` prime sub-sum. The difference is nonnegative and consists exactly of ordered pairs with at least one prime power of exponent at least 2. Let

$$H_N=\{p^k\le N:p\text{ prime},\ k\ge2\},\quad K_N=|H_N|.$$

Each integer in this set has a unique prime-power representation, and the elementary bound

$$K_N\le \lfloor\log_2 N\rfloor\lfloor\sqrt N\rfloor$$

follows by bounding, for each exponent `k>=2`, the number of possible prime bases by `sqrt(N)`; exponents exceed `log_2 N` only when the power exceeds N. For each choice of a higher power in either ordered position, there is at most one complementary integer, and both von Mangoldt factors are at most `log N`. Thus the explicit, deliberately crude bound

$$0\le C_\Lambda(N)-\sum_{p+q=N}(\log p)(\log q)
\le 2K_N(\log N)^2$$

holds. The overlap where both terms are higher powers is counted twice only in the upper bound, which is harmless. Here the prime-only sum is ordered and includes the diagonal. Separately,

$$\sum_{p+q=N}(\log p)(\log q)=2\sum_{p<q,\ p+q=N}\log p\log q+\mathbf 1_{N/2\text{ prime}}(\log(N/2))^2.$$

The correction is not a signed error: it is nonnegative, and the `p=q` diagonal has multiplicity one. On `H` that prime diagonal is absent, but higher prime powers remain in `C_Lambda`.

## Verification and evidence status

`02_verify_fourier.py` checks 42 selected even targets, including 4, 6, 8 and targets with and without a prime diagonal, using two exact paths: direct ordered convolution and integer finite-DFT orthogonality with `L=2N+1>2N`. It separately partitions unit-weight prime-power convolutions into prime-prime and at-least-one-higher-power ordered terms. The output is `02_fourier_cases.json`. These checks use exact integer test weights; the proof above is for arbitrary real weights and therefore for `log p`. No floating-point quadrature is used.

**Proved:** the orthogonality identity, multiplicities, diagonal term, and stated elementary prime-power bound.

**Not proved:** any positive target-uniform lower bound for the prime-only coefficient, or the required signed minor-arc estimate. Existing average or exceptional-set information is not a substitute for that per-target inequality.
