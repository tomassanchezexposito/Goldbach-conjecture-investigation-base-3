# Stage 66 — Independent review and sharp modulus proofs

## Scope and inherited definitions

The original three-case statement says every even $N>2$ has at least one of $N=p+1$, $N=2p$, or $N=p+q$ for distinct primes $p<q$. The equidistance condition in the third case is algebraically equivalent to $p+q=N$. The residual set is
$$H=\{N\ge4:N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\}.$$
For $N\in H$ the first two alternatives fail, so the open obligation is a distinct genuine-prime pair. The wheel count $A_{210}(N)$ counts residue pairs modulo $210$ that are locally admissible; it does not count prime pairs.

The Fourier convention inherited from Stage 65 is $e(t)=e^{2\pi i t}$ and
$$r_w(n)=\int_0^1 S_w(\alpha)^2e(-n\alpha)\,d\alpha,
\qquad m_w(n)=\int_{\mathfrak m}S_w(\alpha)^2e(-n\alpha)\,d\alpha.$$
The square $S_w^2$ selects sums $p+q=n$. Replacing it with $|S_w|^2$ selects differences $p-q=n$ and is invalid for this problem. Parseval still uses $|S_w^2|^2=|S_w|^4$.

## Independent proof of the arbitrary-modulus theorem

Let $I$ be a finite set of distinct nonzero integer shifts. Suppose $|c(N)|\ge A>0$ and $|c(N+h)-c(N)|\le d_h$ for each $h\in I$. The reverse triangle inequality gives
$$|c(N+h)|\ge \bigl(|c(N)|-|c(N+h)-c(N)|\bigr)_+\ge(A-d_h)_+.$$
The indices $N$ and $N+h$ are pairwise distinct, so summing only these terms proves
$$\|c\|_2^2\ge A^2+\sum_{h\in I}(A-d_h)_+^2.$$

This is sharp over the stated class of arbitrary complex sequences: assign $c(N)=-A$, assign $c(N+h)=-(A-d_h)_+$, and set all other entries to zero. If $d_h\le A$, the corresponding increment has magnitude $d_h$; if $d_h>A$, it has magnitude $A\le d_h$. Thus equality holds. In particular, for a budget $B$, existence of a sequence satisfying the constraints and $\|c\|_2^2\le B$ is equivalent to $B$ being at least the displayed minimum. This extremizer is a logical countermodel for deductions from the abstract hypotheses; it is not asserted to arise from primes.

## Exact even-step Lipschitz threshold

For distinct shifts $\pm2,\ldots,\pm2H$ and bounds $d_{\pm2h}=Lh$, the preceding result gives
$$B\ge A^2+2\sum_{h=1}^H(A-Lh)_+^2.$$
For $L>0$, the positive summands are exactly $1\le h\le J$, where
$$J=\min\bigl(H,\max(0,\lceil A/L\rceil-1)\bigr).$$
The endpoint is written this way deliberately: if $A/L$ is an integer, the term at $h=A/L$ is zero and need not be included. Expanding the finite sums of $1,h,h^2$ gives
$$B\ge A^2+2\left[JA^2-ALJ(J+1)+\frac{L^2J(J+1)(2J+1)}6\right].$$
For $L=0$ all $2H$ neighbors have magnitude at least $A$, giving $(2H+1)A^2$. For $H\ge\lceil A/L\rceil$ and $A/L\to\infty$, comparison with the integral of $(A-Lx)^2$ gives $A^2+2A^3/(3L)+O(A^2+AL)$.

An independently verified necessary scale follows when $A\sim cX$ and $B\sim C_4X^{5/2}(\log X)^{100}$: a contradiction by this test requires $L$ on the order of, or smaller than,
$$\frac{2c^3}{3C_4}X^{1/2}(\log X)^{-100},$$
with a strict margin and a shift span at least comparable to $A/L$. This is a scale calculation for the abstract criterion, not an estimate for primes.

## Verification evidence

The pre-existing exact Python regression checks 300 rational parameter combinations and nonuniform examples. The new independent SageMath verifier reconstructs the finite sums using `QQ`, checks the closed formula against direct summation on a separate parameter grid, and checks true-prime representation partitions independently. These checks validate algebra and finite bookkeeping; the displayed arguments prove the infinite parameter statements. See `verification_manifest.json` for commands and hashes.
