# Stage 71 — Exact complement-matching sensitivity and Fourier-near-invisibility of one missing target

**Research date:** 2026-11-11. **Provenance:** direct independent ChatGPT mathematical research on a new branch descended from completed Stage 70, **no CoCalc/Codex usage**.  
**Result classifications:** T71.1 **PROVED finite combinatorial optimization**; T71.2 **PROVED from classical PNT and published unconditional sieve**; corollaries **PROVED for explicitly modified prime supports**; genuine full-Goldbach statement **OPEN**.

## 0. Unchanged mathematical target, necessary distinction

Let
\[
H=\{N\in2\mathbb Z:N\ge4,\ N-1\ {\rm composite},\ N/2\ {\rm composite}\},
\qquad R(N)=\#\{p<q:p,q\ {\rm actual\ primes},\ p+q=N\}.
\]
The original three cases remain \(N=p+1\), \(N=2p\), \(N=p+q\) with \(p<q\). On H only the third is unresolved, and the reflection \(N-2p=2q-N\) is algebraic. The odd-prime position coordinate \(p=3+2a\) retains \(p=3\) at a=0; it is not ternary notation or an independent primality theorem. For even N>4, prime 2 cannot contribute; on H there is no same-prime diagonal.

Stage 70 constructed a **modified** prime-supported polynomial by removing a few prime frequencies. All the theorems below distinguish that modified object from the immutable weighted polynomial containing **every actual prime in its support**.

## 1. Theorem 71.1 — exact deletion threshold, sharp continuous tradeoff (PROVED)

Let P be a finite set of actual primes, let positive real weights \(a_p>0\) be specified on P, and let \(N\in H\). Set
\[
\mathcal E_N=\{\{p,q\}\subseteq P:p<q,\ p+q=N\}.
\]
These edges are disjoint: since the complement of a given p is uniquely N-p, the graph of complementary representations is a matching (plus isolated vertices).

For \(0\le b_p\le a_p\), define the deleted-mass cost
\[
\delta_1(a,b)=\sum_{p\in P}(a_p-b_p)
\]
and the remaining ordered weighted coefficient
\[
r_b(N)=\sum_{p+q=N}b_pb_q=2\sum_{\{p,q\}\in\mathcal E_N}b_pb_q.
\]
For each edge i write \(A_i=\max(a_{p_i},a_{q_i})\), \(B_i=\min(a_{p_i},a_{q_i})\), both positive. Enumerate edges in **nonincreasing order of \(A_i\)** and put \(C_j=\sum_{i=1}^j B_i,\ C_0=0,\ C_m=\sum_i B_i\).

**(a) Exact distance from the prescribed original weights to the nonnegative-weight one-hole class:**
\[
\boxed{
\tau_N:=\min_{0\le b\le a,\ r_b(N)=0}\delta_1(a,b)
=\sum_{\{p,q\}\in\mathcal E_N}\min(a_p,a_q)=C_m.}
\tag{71.1}
\]
The minimum is zero if and only if \(\mathcal E_N=\varnothing\). For the whole genuine-prime set with unit weights, this identity reduces to \(\tau_N=R(N)\), **which is a reformulation, not an independent Goldbach theorem**. With a compactly supported smooth w the matching can be empty even when N has prime pairs outside the weight support.

For \(1\le s<\infty\), the exact weighted \(\ell^s\)-distance is
\[
\min_{0\le b\le a,\ r_b(N)=0}\Big(\sum_p|a_p-b_p|^s\Big)^{1/s}
=\Big(\sum_i B_i^s\Big)^{1/s},
\tag{71.2}
\]
and in \(\ell^\infty\) it is \(\max_iB_i\), with value 0 for an empty matching.

**(b) Exact optimal remaining coefficient for an arbitrary allowed deletion budget \(0\le\eta\le C_m\):**
\[
\boxed{
\min_{\substack{0\le b\le a\\\delta_1(a,b)\le\eta}}r_b(N)
=2\left(\sum_{i=1}^m A_iB_i
-\sum_{i<k}A_iB_i-A_k(\eta-C_{k-1})\right),
}
\tag{71.3}
\]
where k is an index satisfying \(C_{k-1}\le\eta\le C_k\). The formula is independent of the chosen k at tied breakpoints. At \(\eta\ge C_m\) the exact minimum is 0. Thus the optimal value is a continuous, piecewise-linear, nonincreasing function, with slopes \(-2A_i\) in decreasing A-order. In particular, a guaranteed strictly positive target count under arbitrary allowed deletion is possible exactly when \(\eta<\tau_N\), assuming the **original prescribed edge set is known and has positive weights**.

### Proof 1: local concavity and fractional knapsack

For one edge with weights \(A\ge B>0\), delete nonnegative amounts x from A and y from B. At total cost t=x+y≤B, the remaining product is
\[
(A-x)(B-y)=(A-x)(B-t+x).
\]
As a function of x∈[0,t], the second derivative is -2, so its minimum is attained at x=0 or x=t. The two endpoint products are \(A(B-t)\) and \((A-t)B\), and \(A(B-t)\le(A-t)B\) because A≥B. Hence the optimum always removes t from the **smaller endpoint**, obtaining \(A(B-t)\). If t≥B, deleting B from that endpoint makes the product zero at cost B. Different edges have disjoint vertices, so total target reduction is \(\sum_i2A_it_i\) with \(0\le t_i\le B_i\) and \(\sum t_i\le\eta\). A standard exchange argument (moving mass from a smaller A_i to a larger A_j whenever the latter is not saturated) proves the greedy order in (71.3). To make **all** edges vanish one must erase at least one endpoint per edge, at cost ≥B_i per edge; choosing the lighter endpoint attains their sum, proving (71.1). The same argument with s-th power costs proves (71.2).

### Proof 2: exact hitting set and linear-programming duality

The family of complementary edges is a matching. Any set of zeroed coordinates hitting every edge has separable minimum weighted cost \(\sum B_i\), and a zero product on each edge is equivalent to hitting every edge. This proves the distance formulas without using the local-concavity calculation.

For a partial budget, after the local concavity reduction each edge has a linear target-reduction segment of slope \(2A_i\), of length B_i. The dual to the fractional-knapsack maximization is
\[
\max_{\substack{0\le t_i\le B_i\\\sum_i t_i\le\eta}}\sum_iA_it_i
=
\min_{\lambda\ge0}\left(\lambda\eta+\sum_iB_i(A_i-\lambda)_+\right).
\tag{71.4}
\]
Weak duality follows from \(A_it_i\le\lambda t_i+(A_i-\lambda)_+B_i\). Choosing \(\lambda=A_k\) at the greedy breakpoint and its associated t_i gives equality, including repeated A values. This independently recovers (71.3).

### Limitation

The exact radius \(\tau_N\) depends on the *actual target representations*. Any proposed independently proved uniform \(\tau_N>0\) would already establish the Goldbach claim on the chosen full support. The theorem is an exact sensitivity characterization, **not** a number-theoretic lower bound for \(\tau_N\).

### Corollary 71.1a — exact target-specific perturbation identity and sharp first-order sensitivity

Extend a_p by zero outside P and put \(d_p=a_p-b_p\), \(0\le d_p\le a_p\). The *ordered* N-th convolution coefficients obey the exact algebraic identity
\[
\boxed{
r_a(N)-r_b(N)=
2\sum_{\{p,q\}\in\mathcal E_N}
\bigl(a_pd_q+a_qd_p-d_pd_q\bigr).
}
\tag{71.5a}
\]
Consequently, for \(a_{\max}=\max_{p\in P}a_p\),
\[
0\le r_a(N)-r_b(N)
\le 2\sum_{p\in P}d_p a_{N-p}
\le 2a_{\max}\delta_1(a,b).
\tag{71.5b}
\]
The first inequality holds because the weights are decreased coordinatewise, and the second because \(d_pd_q\ge0\). The final bound is *locally sharp*: deleting an infinitesimal amount from the lighter endpoint of an edge whose other weight equals \(a_{\max}\) changes r(N) at rate exactly \(2a_{\max}\).

The middle sum is a **target-reflected prime-weight interaction**, unlike the total deleted mass. Knowing only \(\delta_1\) loses its location on the complement graph. It is not an independently estimated arithmetic statistic, however: \(a_{N-p}\) records the primality and support status of the complementary entry. Assuming a lower bound for that interaction without proving it would repackage the original target question. The exact greedy tradeoff (71.3) records precisely how much this loss of location matters.

## 2. Theorem 71.2 — the erased-target polynomial is close in every normalized global Fourier Lp scale (PROVED)

Fix any nonzero nonnegative \(w\in C_c^\infty((0,1))\) and let
\[
S_X(\alpha)=\sum_{p\ {\rm prime}}a_pe(p\alpha),
\quad a_p=(\log p)w(p/X),\quad
W=\int_0^1w(t)dt>0.
\]
For every sufficiently large X and every even \(N\in H\cap[X/2,X]\), use the matching construction of T71.1 to remove the smaller weighted endpoint of **every** target edge, and call the resulting prime-supported polynomial \(S'_{X,N}\). Put \(\Delta_{X,N}=S_X-S'_{X,N}\) and \(F_X=S_X^2,\ F'_{X,N}=(S'_{X,N})^2\).

By the **published unconditional** J. Wu upper sieve result (Acta Arith. 114.3, 2004, Theorem 1), together with \(N/\varphi(N)\ll\log\log N\), uniformly for N∈H∩[X/2,X],
\[
\#\mathcal E_N=O(X\log\log X/(\log X)^2).
\]
Theorem 70.5 already deduced, for the deleted coefficient vector \(d_p=a_p-a'_p\ge0\),
\[
D_1:=\sum_pd_p=O_w(X\log\log X/\log X),\qquad
D_2:=\sum_pd_p^2\le\|w\|_\infty(\log X)D_1=O_w(X\log\log X).
\tag{71.5}
\]

**The new conclusion is much stronger than mere retained first-order mass:** for every **fixed** real \(q\in[2,\infty]\),
\[
\boxed{\frac{\|S_X-S'_{X,N}\|_{L^q(\mathbb T)}}{\|S_X\|_{L^q(\mathbb T)}}\longrightarrow0}
\quad\text{uniformly in }N\in H\cap[X/2,X],
\tag{71.6}
\]
and for every fixed \(r\in[1,\infty]\),
\[
\boxed{
\frac{\|S_X^2-(S'_{X,N})^2\|_{L^r(\mathbb T)}}
{\|S_X^2\|_{L^r(\mathbb T)}}\longrightarrow0,
\qquad [F'_{X,N}]_N=0.
}
\tag{71.7}
\]
The rates below make the statements quantitative:

- q=2: \(O_w(\sqrt{\log\log X/\log X})\).
- each fixed 2<q<∞: \(O_{q,w}((\log\log X)^{1-1/q}/(\log X)^{1-2/q})\).
- q=∞: \(O_w(\log\log X/\log X)\).
- For r≥1, (71.7) inherits the q=2r rates, with an additional factor \(2+o(1)\). In particular the \(r=2\) (full-square-polynomial L²) relative rate is \(O_w((\log\log X)^{3/4}/\sqrt{\log X})\).

### Proof: weighted PNT, interpolation and factorization

The classical PNT and fixed-weight partial summation give
\[
S_X(0)=\sum_pa_p\sim WX,\qquad
\|S_X\|_2^2=\sum_pa_p^2\sim X\log X\int_0^1w(t)^2dt.
\tag{71.8}
\]
For the second relation, \(w\) is supported away from 0, so \(\log p=\log X+O_w(1)\) on the support, and the weighted PNT applies to \(w^2\).

From coefficient nonnegativity and (71.5),
\[
\|\Delta\|_\infty\le D_1,\qquad
\|\Delta\|_2^2=D_2.
\tag{71.9}
\]
For q=2, divide D_2 by (71.8). For q=∞, use \(\|S_X\|_\infty=S_X(0)\sim WX\). For any q>2, the exact interpolation inequality
\[
\|\Delta\|_q^q
=\int|\Delta|^{q-2}|\Delta|^2
\le\|\Delta\|_\infty^{q-2}\|\Delta\|_2^2
\]
gives
\[
\|\Delta\|_q
\ll_{q,w}X^{1-1/q}
\frac{(\log\log X)^{1-1/q}}{(\log X)^{1-2/q}}.
\tag{71.10}
\]
On the interval \(|\alpha|\le1/(12X)\), the nonnegative weights and p≤X give
\[
|S_X(\alpha)|\ge\Re S_X(\alpha)
\ge(\sqrt3/2)S_X(0)\gg_wX,
\]
so \(\|S_X\|_q\gg_{q,w}X^{1-1/q}\), proving the q>2 ratio. The constants are uniform in target N.

For the squares, use the exact factorization
\[
F_X-F'_{X,N}=(S_X-S'_{X,N})(S_X+S'_{X,N}).
\]
For every 1≤r<∞, Hölder and the triangle inequality give
\[
\|F_X-F'_{X,N}\|_r
\le\|\Delta\|_{2r}(\|S_X\|_{2r}+\|S'_{X,N}\|_{2r})
\le\|\Delta\|_{2r}(2\|S_X\|_{2r}+\|\Delta\|_{2r}).
\]
Since \(\|F_X\|_r=\|S_X\|_{2r}^2\), (71.6) implies (71.7) with the stated rates. The r=∞ case follows from \(|F-F'|\le|\Delta|(|S|+|S'|)\) and the corresponding uniform bounds.

Finally, the target coefficient vanishes **exactly**, by the complement-matching selection. No existence of a prime pair at N is assumed: when none exists, the original coefficient is already zero and the deletion may be empty.

### Independent exact additive-energy strengthening

For any finitely supported nonnegative deletion vector d, integer-convolution Young's inequality yields
\[
\|\Delta\|_4^4
=\sum_k\left(\sum_{p+q=k}d_pd_q\right)^2
=\|d*d\|_{\ell^2}^2
\le\|d\|_{\ell^1}^2\|d\|_{\ell^2}^2
=D_1^2D_2.
\tag{71.11}
\]
Together with \(\|S_X\|_4^4\gg_wX^3\) (classical PNT concentration at 0), this again gives
\[
\frac{\|\Delta\|_4}{\|S_X\|_4}
\ll_w\frac{(\log\log X)^{3/4}}{\sqrt{\log X}}.
\tag{71.12}
\]
This independently verifies the central r=2 square-polynomial claim using an exact four-variable additive-energy inequality rather than interpolating by \(\|\Delta\|_\infty\).

## 3. What this no-go does and does not show

**Sharp information distinction.** All the modified polynomials \(S'_{X,N}\) are supported on genuine prime frequencies and retain the original nonnegative weights at their retained positions. They preserve (from Stage 70) 1-o(1) of total prime mass, first-order PNT in fixed/small polylog progressions, nonincreasing full-circle fourth moment, and now **relative closeness in every fixed global Fourier Lp scale of the prime polynomial and its square**. Nevertheless each prescribed target has zero coefficient in the modified polynomial.

**No paradox with Fourier continuity.** Global relative \(L^2\)-closeness of the square does not force an individual coefficient to remain positive. A target coefficient is an absolute linear functional of norm 1 in L², and the permitted absolute error \(\|F-F'\|_2=o(\|F\|_2)\) may still be much larger than the expected \(\asymp X\) target main term because \(\|F\|_2\gg_wX^{3/2}\). A *target-specific* Fourier error \(o(X)\) would be a materially stronger input, not supplied by relative global closeness.

**Not a proof or refutation of Goldbach.** The actual polynomial S_X includes **all** weighted genuine prime coefficients and is immutable. S' deliberately deletes target-sensitive frequencies, so it is an adversarial model, **not the true prime distribution**. The theorem proves a no-go only for arguments whose claimed inputs are stable under this o(1)-relative perturbation. A method exploiting every fixed coefficient or genuine prime-specific signed cancellation is not ruled out.

**Open arithmetic obligation.** Prove a target-uniform absolute lower bound for \(\tau_N\) with full support, or prove target-level correlation/signed Fourier control not stable under the deletion. Any \(\tau_N>0\) result for the complete prime support is already equivalent to existence of a Goldbach representation: do not repackage the sought conclusion as an independent input.

## 4. Source provenance and check plan

- J. Wu, *Chen's double sieve, Goldbach's conjecture and the twin prime problem*, **Acta Arithmetica** 114(3) (2004), 215–273, DOI https://doi.org/10.4064/aa114-3-2, Theorem 1 \(D(N)\le7.8209\,\Theta(N)\) for sufficiently large even N. **Unconditional upper bound only**, confirmed from publisher and original manuscript. \(\Theta(N)=C_NN/(\log N)^2\).
- Classical established PNT for \(\vartheta\) and weighted smooth functions is used for (71.8), and classical \(N/\varphi(N)\ll\log\log N\) is used to simplify Wu's singular factor.
- The exact optimization proof does not need any external arithmetic theorem; the asymptotic Fourier-closeness theorem uses those established unconditional results. No 2026 unverified zero-free claim is needed.
- An exact small matching/greedy regression with **two independent finite algorithms** will be committed separately, without large prime sweeps. Numerical tests check the formulas, **not** the universal Goldbach assertion.

**Verdict:** T71.1 and T71.2 are rigorous within their explicitly stated domains. Their original value is to sharpen the information-theoretic obstruction: even global norms of the entire *prime-square polynomial* can be asymptotically preserved by a targeted sparse deletion. The missing input is a **non-deletion-invariant, genuine-prime target estimate**, and remains OPEN.
