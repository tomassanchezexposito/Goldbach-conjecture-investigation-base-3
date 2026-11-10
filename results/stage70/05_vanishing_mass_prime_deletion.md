# Stage 70 — a stronger asymptotic density no-go from the published Goldbach upper-bound sieve

**Date:** 2026-11-10. **Proof class:** original deduction from established unconditional theorems of Wu (2004), the classical PNT and PNT in fixed arithmetic progressions. The deduction is **PROVED** given these already published theorems; it is not claimed as previously unpublished mathematics. No Goldbach existence theorem is established. **CoCalc/Codex not used.**

## 1. Established upper sieve input and exact quantifiers

Let
\[
D(N)=\#\{p\text{ prime}:N-p\text{ prime}\}
\]
be the *ordered* Goldbach representation count for even N. J. Wu, *Chen's double sieve, Goldbach's conjecture and the twin prime problem*, **Acta Arithmetica** 114.3 (2004), 215–273, Theorem 1, proved the **unconditional** uniform upper bound for all sufficiently large even N,
\[
D(N)\le 7.8209\,\Theta(N),\qquad
\Theta(N)=C_N\,\frac{N}{(\log N)^2},
\]
where
\[
C_N=\Bigl(\prod_{p>2}(1-(p-1)^{-2})\Bigr)
\prod_{\substack{p\mid N\\p>2}}\frac{p-1}{p-2}.
\]
Primary-source URL: https://www.impan.pl/shop/publication/transaction/download/product/82961 . The exact numeral 7.8209 is not important here; a universal finite multiplicative constant suffices. On the residual H, N/2 is composite, so **there is no diagonal**, and \(D(N)=2R(N)\). The result is an **upper**, not a lower, bound.

For all odd primes,
\[
\frac{p-1}{p-2}
=\frac p{p-1}\left(1+\frac1{p(p-2)}\right).
\]
The product of the second factors over all odd primes converges to a finite positive absolute constant. Thus
\[
\prod_{\substack{p\mid N\\p>2}}\frac{p-1}{p-2}
\ll \frac N{\varphi(N)}
\ll\log\log N,
\]
where the final uniform bound is classical (for all sufficiently large N); it follows e.g. from established Rosser–Schoenfeld estimates for \(N/\varphi(N)\). Therefore the **uniform established unconditional upper estimate**
\[
\boxed{R(N)\ll \frac{N\log\log N}{(\log N)^2},
\qquad N\in H,\ N\to\infty}
\tag{70.16}
\]
holds. Its proof uses no conjectured positivity of R(N).

## 2. Theorem 70.5 — a vanishing relative deletion preserving weighted prime mass (PROVED)

Let \(w\in C_c^\infty((0,1))\) be **fixed, nonzero and nonnegative**, \(W=\int_0^1w(t)dt>0\), and define the **actual full weighted prime support**
\[
P_X=\{p\text{ genuine prime}:w(p/X)>0\},\qquad
a_p=(\log p)w(p/X)>0,
\qquad S_X=\sum_{p\in P_X}a_p.
\]
By the classical prime number theorem and weighted partial summation,
\[
S_X\sim WX.
\]
For **every sufficiently large X** and **every residual even** \(N\in H\cap[X/2,X]\) there exists a subset \(P'_{X,N}\subseteq P_X\), constructed without assuming a representation, such that, with \(S'_{X,N}(\alpha)=\sum_{p\in P'_{X,N}}a_pe(p\alpha)\),
\[
\boxed{
\begin{aligned}
\sum_{p\in P'_{X,N}}a_p
&\ge
S_X-O_w\!\left(\frac{X\log\log X}{\log X}\right)
=S_X\left(1-O_w\left(\frac{\log\log X}{\log X}\right)\right),
\\
[S'_{X,N}(\alpha)^2]_N&=0,\\
0\le [S'_{X,N}{}^2]_k&\le[S_X(\alpha)^2]_k
\quad\text{for every integer }k,\\
\int_{\mathbb T}|S'_{X,N}(\alpha)|^4d\alpha
&\le\int_{\mathbb T}|S_X(\alpha)|^4d\alpha.
\end{aligned}}\tag{70.17}
\]
Here \([S^2]_k\) denotes the exact k-th Fourier coefficient and \(S_X(\alpha)=\sum_{p\in P_X}a_pe(p\alpha)\) denotes the full polynomial (while the unadorned \(S_X=\sum a_p\) is its mass at zero). The notation makes clear which object is a scalar and which is a function.

**Proof.** Form the graph on P_X with an undirected edge \(\{p,q\}\) whenever p+q=N and p≠q. Since q=N−p is uniquely determined, this graph is a matching plus isolated vertices. The diagonal is impossible on H. For each edge delete the endpoint of **smaller** weight, breaking ties deterministically; keep every isolated vertex. The retained set has no complementary pair at target N. The removed mass is at most
\[
(\#\text{edges})\max_{p\in P_X}a_p\le R(N)\,\|w\|_\infty\log X.
\]
The uniform sieve bound (70.16) and N∈[X/2,X] make the right side
\[
O_w(X\log\log X/\log X)=o(S_X)
\]
uniformly in N. Setting nonnegative input weights to zero cannot increase any squared-convolution coefficient. All coefficients are nonnegative; consequently Parseval implies the stated monotonicity of the full fourth moment. The construction and inequalities hold even if R(N)=0: then there are no edges and deletion is empty. No claim of existence is used. QED.

### Sharp logical interpretation

This is a much stronger **model-class counterexample** than the earlier general matching lemma retaining only half the mass. It proves that **even a \(1-o(1)\) proportion of the genuine-prime weighted mass**, support restricted to the actual allowed prime positions and a nonincreasing full-circle fourth moment, **does not logically force a prime-pair coefficient at a prescribed N if arbitrary deletions of a vanishing mass fraction are permitted**.

Crucially, the constructed polynomial is **not** the true fixed \(\sum_p(\log p)w(p/X)e(p\alpha)\): it deliberately deletes a small number of prime positions whose reflected complements are prime. Thus it is **NOT** a Goldbach counterexample and cannot refute a theorem using the original actual coefficients without deletions, or one controlling the signed major/minor contribution with a strict margin.

## 3. Corollary 70.5a — even prime distribution in every FIXED arithmetic progression is preserved

For each **fixed** modulus q≥1 and residue a coprime to q, the classical PNT in arithmetic progressions gives
\[
\sum_{\substack{p\in P_X\\p\equiv a\pmod q}}
(\log p)w(p/X)\sim\frac{W}{\varphi(q)}X.
\]
The deletion loses **at most its global total weighted mass** on *any* progression, and that total is \(o(X)\), uniformly for residual N∈[X/2,X]. Hence
\[
\boxed{
\sum_{\substack{p\in P'_{X,N}\\p\equiv a\pmod q}}a_p
=\frac{W}{\varphi(q)}X+o_q(X)
}
\tag{70.18}
\]
for every fixed q,a as \(X\to\infty\), even along **arbitrary varying** residual targets N=N(X). The error is not asserted uniform in moduli q growing with X, and the constructed subsets are not claimed to consist of **all** primes in a progression.

**Consequence:** global weighted prime mass, the first-order weighted PNT in each fixed progression, and an upper bound on full fourth-moment energy are still insufficient, by themselves, to certify a nonzero representation at a prescribed target **for the class of sparse deletions of actual primes**.

This distinguishes first-order equidistribution of *one prime variable* from the target-dependent simultaneous primality correlation \(p,N-p\). Any viable theorem must preserve the **full fixed coefficient structure** or exert quantitative control over the delicate target-pair dependency which the deletions destroy.

## 4. Adversarial limitations and source classification

- **External established theorem:** Wu's unconditional upper sieve theorem supplies the *upper* representation count bound. The classical PNT and PNT-AP are also external established theorems; their proofs are not newly supplied by this research.
- **Proved elementary deduction:** complement edges form a matching; deleting the lighter endpoint per edge preserves \(1-o(1)\) of original mass by the external upper bound and eliminates all representations in the **altered** model; monotonicity of nonnegative Fourier coefficients proves the energy inequality; fixed-q asymptotics survive because the total deletion has mass o(X).
- **Not proved:** that the fixed actual genuine-prime polynomial has zero at any target, or that the full fixed-prime coefficients can be changed without changing the arithmetic problem.
- **First invalid inference to avoid:** from \(\sum_{p\in P'}a_p=(1-o(1))\sum_{p\in P_X}a_p\) and fixed-AP equidistribution to \([S'^2]_N>0\). This is false, despite \([S_X^2]_N\) potentially being positive.
- **Quantifier discipline:** q is **fixed**, w is fixed, N can vary with X subject to N∈H∩[X/2,X]. All constants may depend on w; the upper sieve constant is absolute. No increasing-modulus level of distribution, parity breakthrough or target-signed cancellation is claimed.

## 5. How this changes the next research priority

There is now no reason to pursue a proof built only from *coarse first-order prime mass, positive wheel survivorship, finitely many fixed-modulus prime progressions, and a nonincreasing energy budget*. Such inputs are invariant under a carefully designed o(1)-mass deletion that destroys all pairs at one target.

The only useful next step is to seek information **not stable under this deletion**: actual fixed coefficients at every prime, or a target-uniform signed bilinear correlation / sufficiently strong growing-modulus distribution statement with an independently derived strict margin.

**Final status:** a rigorous conditional-on-established-theorems *model-class no-go*, not a new proof or refutation of Goldbach.
