# Dependency validation of T73.5, T74.3 and T75.1

Date: 11 November 2026. Base: Stage 75 commit `983c9d91bd0ac036c1c75d0afa10b0809fe0728a`. This is a validation gate, **not Stage 76**, a repeated Type I evaluation, or a reopened Type II proof attempt.

## Verdict and scope

The three deductions pass the mathematical dependency audit with the fixed-weight, target and polynomial-range hypotheses already stated in the repository. No circular prime-pair premise, invalid sign, missing target-uniformity condition or necessary theorem correction was found within this chain. The parameter schedule and convergence justifications below make the validation checkable. No new arithmetic saving is established. The Stage 75 **NO-GO remains in force**.

The audit reconstructed the implication steps from the external input statements and checked their potentially failing cases. It is a fresh critical pass by the same agent, not external peer review, a proof-blind reviewer, or formal verification. Earlier finite tests were not rerun. Historical reports and theorem ledgers are preserved; an additive audit ledger records the verdict.

## 1. External inputs, separated from project deductions

**E1 — established Bombieri–Vinogradov theorem.** The source actually read is Terence Tao, *254A Notes 3: The large sieve and the Bombieri–Vinogradov theorem*, 10 January 2015, [discrepancy definition and Theorem 17](https://terrytao.wordpress.com/2015/01/10/254a-notes-3-the-large-sieve-and-the-bombieri-vinogradov-theorem/). For every fixed saving exponent $D>0$, endpoint discrepancy summed over reduced-class maxima is $O_D(y\log^{-D}y)$ when $Q\le\sqrt y\log^{-B(D)}y$. Its center is $\varphi(q)^{-1}\sum_{n\le y,(n,q)=1}\Lambda(n)$. Exercise 20 also states an endpoint-maximal strengthening, but the audit does not assume that exercise as an additional proved premise.

**E2 — established quantitative PNT/Möbius cancellation.** H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I: Classical Theory* (Cambridge, 2007), Chapter 6, [author-hosted chapter](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/10.0_pp_168_198_The_Prime_Number_Theorem.pdf), especially (6.17)–(6.19), gives $M(y)=\sum_{n\le y}\mu(n)\ll y\exp(-c\sqrt{\log y})$ and the corresponding sum of $\mu(n)/n$, with total sum zero. The same chapter supplies quantitative PNT. These are unconditional classical inputs; no fixed zero-free half-plane for all Dirichlet L-functions is a premise here.

Only these named passages were read anew, not the complete external proofs. Their current byte receipts are in the manifest. A changed HTML hash is a current-page receipt, not evidence that its theorem has changed.

## 2. T73.5: endpoint, centering and target uniformity audit

Fix $w\in C_c^\infty((0,1))$ once and for all, with support inside $[\sigma,\rho]$, $0<\sigma<\rho<1$. Constants may depend on this fixed weight and a fixed desired logarithmic saving, never on $N\in[X/2,X]$. This conclusion cannot automatically be applied to weights or support endpoints varying with $X$.

### 2.1 Grouping and reflected measure

For the inherited grouped coefficient,
$$|c_l|\le\sum_{m\mid l}\Lambda(m)=\log l,$$
including $l=1$, where both sides vanish. Thus no divisor-weighted BV extension is being assumed. The $A_1$ coefficient is bounded by one; the two contributions to a shared modulus are combined with a fixed constant loss only.

For a reduced class, put $x=N-lk$ and $f_N(x)=h_N(N-x)$. On its support $x\in[\sigma X,\rho X]$ and $N-x\in[\sigma X,\rho X]$. Therefore $\int|f_N'|\ll_w1$. The corresponding logarithmic weight has variation $O_w(\log X)$: differentiating $\log((N-x)/d)$ costs $O_\sigma(X^{-1})$, and the other factor costs $O_w(X^{-1}\log X)$. The integration interval has length $O(X)$. No singularity at $N-x=0$ is present. Compact support removes boundary terms in the Stieltjes integration. The source residue maximum allows $a=N\pmod l$ to vary with both target and modulus.

If $(N,l)>1$, every nonzero $\Lambda(N-lk)$ is a power of a prime dividing $(N,l)$. Summing its logarithmic weight for each base up to $X$ costs at most $\log X$. Since $N\le X$, there are $O(\log X)$ such bases. Including the outer coefficient/logarithm yields $O_w(\log^3X)$ per modulus, and hence $O_w(Q\log^3X)$ altogether. These terms cannot be inserted into a reduced-class main term. The small-variable Vaughan boundary vanishes only once $V<\sigma X$; the asymptotic statement has exactly that large-$X$ regime.

### 2.2 Explicit mesh schedule, avoiding circular parameter choices

Let $A>0$ be the desired final saving in T73.5 and set $R=A+2$. First choose an integer $C>R+3$, then $D>R+C+4$, then the source's $B=B(D)$. Choose a grid with mesh $\Delta\asymp X/(\log X)^C$, first positive endpoint comparable to $\Delta$, last endpoint $X$, and $O((\log X)^C)$ points. With $Q\le X^{2/5}$ and any positive grid point $y$,
$$\frac{Q(\log y)^B}{\sqrt y}\ll X^{-1/10}(\log X)^{B+C/2}\longrightarrow0.$$
Thus E1 applies even at the first positive endpoint. This ordering fixes all logarithmic powers before taking $X$ large; no forbidden modulus is obtained by allowing parameters to depend on $X$.

At each endpoint, replacing the coprime center by $y/\varphi(l)$ costs, after summing over moduli,
$$\ll (\log X)^4+\Big|\sum_{n\le y}\Lambda(n)-y\Big|(\log X)^2.$$
Here $\sum_{l\le Q}1/\varphi(l)\ll\log^2(2Q)$ follows from $1/\varphi(l)\le\tau(l)/l$. Summing these losses over the grid is negligible compared with $X(\log X)^{-R}$ by E2 and $\log y\asymp\log X$ at positive endpoints. The endpoint BV losses total $O(X(\log X)^{C-D})$.

For $y$ between endpoints $y_j,y_{j+1}$, monotonicity gives the discrepancy bound by the larger endpoint discrepancy plus $\Delta/\varphi(l)$. At $y_0=0$ the discrepancy is exactly zero, so the initial interval causes no gap. The summed interpolation term is $O(X(\log X)^{2-C})$. It follows that the modulus sum of the endpoint supremum is $O_R(X(\log X)^{-R})$. The extra $O_w(\log X)$ from the weight variation is absorbed in the requested T73.5 saving.

**Verdict V73:** the uniform T73.5 error reduction follows from E1/E2, coefficient grouping and explicit treatment of nonreduced powers. It does not apply BV to a reflected two-prime test function: the prime factor outside Type I is not hidden inside an inadmissible weight. The uncontrolled Type II term remains present. No target representation is used. Neither this argument nor the source provides the effective numerical cutoff needed for a universal finite connection.

## 3. T74.3: audit of analytic transfer, not another kernel evaluation

The previously established exact finite kernel identities are left in place. The audit checks the dependence of their estimates on a varying $N$, and their local-factor normalization; it does not repeat the finite sums or their experiments.

### 3.1 Convergence, derivative and sign

E2 and partial summation give convergent tails for both $\sum\mu(n)/n$ and $\sum\mu(n)\log n/n$, bounded by a polynomial in $\log y$ times $\exp(-c\sqrt{\log y})$. For example the latter tail is controlled by a constant times
$$|M(y)|\frac{\log y}{y}+\int_y^\infty\frac{|M(t)|(1+\log t)}{t^2}\,dt.$$
After $v=\sqrt{\log t}$ this is a polynomial tail times $e^{-cv}$. Decreasing $c$ absorbs that polynomial. These bounds are uniform when an extra factor $n^{-s}$ is inserted, $0\le s\le1$, using the same partial summation. Therefore passage to $s\downarrow0$ in the differentiated series is legitimate. Since $1/\zeta(1+s)=s+O(s^2)$ and differentiation introduces a minus sign,
$$\sum_{n\ge1}\frac{\mu(n)\log n}{n}=-1.$$
The sign is not a conjectured prime correlation. Without convergence justification, formal differentiation at the boundary would have been a gap; here the stated Möbius input supplies it.

### 3.2 Uniformity certificate for the auxiliary convolution

For $a_N(n)=\mu(n)\mathbf1_{(n,N)=1}/\varphi(n)$ and the inherited $g_N$, audit the local series in $z$:
$$g_{N,p}(z)=\begin{cases}(1-z/p)^{-1},&p\mid N,\\(1-z/(p-1))/(1-z/p),&p\nmid N.\end{cases}$$
Multiplication by the $\mu/n$ factor $1-z/p$ gives respectively $1$ and $1-z/(p-1)$, exactly the local factors of $a_N$. Thus the convolution uses $\mu/n$, not $\mu$ or an assumed prime-pair function.

The critical absolute moment is $T_N=\sum_k|g_N(k)|k^{1/4}$. Its factors away from divisors of $N$ have summable logarithms of size $O(p^{-7/4})$; at divisors they are $(1-p^{-3/4})^{-1}$. With $L=\log X$ and positive $N\le X^B$, split those divisors at $L$. Their small-prime logarithms total $O(L^{1/4})$ by comparison with all integers; their number above $L$ is at most $B L/\log L$, each costing $O(L^{-3/4})$. Hence
$$\log T_N=O_B(1+L^{1/4}),$$
without a fixed-$N$ constant. For $X^\alpha\le y\le X^\beta$, fixed $0<\alpha\le\beta$, the convolution errors after splitting at $k=\sqrt y$ are bounded by
$$T_N(1+\log y)^2\{e^{-c_1\sqrt{\log y}}+y^{-1/8}\}.$$
Indeed $A_\mu(z)\ll1+\log z$ and $B_\mu(z)\ll(1+\log z)^2$ suffice for the tail; $\sum_{k>\sqrt y}|g_N(k)|\le T_Ny^{-1/8}$. The logarithmic factors in the lower part have degree at most two. Because $L^{1/4}=o(\sqrt L)$, the display is $O_{B,\alpha,\beta}(e^{-c\sqrt L})$. This confirms that many small target divisors cannot overwhelm the saving.

At $z=1$, absolute convergence yields the constant
$$\sum_k g_N(k)=\prod_{p\mid N}\frac p{p-1}\prod_{p\nmid N}\left(1-\frac1{(p-1)^2}\right)=\mathfrak S(N)$$
for positive even $N$. Evenness is essential at prime 2. The audit does not extend this expression to $N=0$ or import the even-target main term to odd targets.

For the inherited correction-term estimate, the small-prime auxiliary target satisfies $Np\le X^{6/5}$ and the argument $U/p$ is at least $\sqrt U$ when $p\le\sqrt U$. Fixed polynomial transfer ranges therefore suffice, after harmless weakening of a fixed exponent to absorb floors. For the alternative removed-factor argument, removal makes the absolute Euler moment no larger and is uniform in the prime and prime-power exponent. Neither treatment introduces a growing unspecified parameter in $B,\alpha,\beta$. The larger-prime tail has the inherited elementary decaying bound. The final integration uses $\|h_N\|_1\le X\|w\|_\infty^2$, uniformly in $N$.

**Verdict V74:** the analytic dependencies of the absolute, target-uniform error in T74.3 are justified by E2 and the stated polynomial ranges. No extra Dirichlet zero-free hypothesis or simultaneous-primality premise is present. This validates the known Type I evaluation; it supplies no new Type II sign control. No numerical kernel evaluation was repeated.

## 4. T75.1: dependency and quantitative implication audit

Let $E_I=G-\mathcal M_I-A_3$, $E_K=\mathcal M_I-F_X$, and $P=G-r_X\ge0$. The exact sign check is
$$r_X=F_X+A_3+E_K+E_I-P,\qquad A_3=r_X-F_X+(P-E_K-E_I).$$
The audited bounds imply $\sup_{N\in H\cap[X/2,X]}|P-E_K-E_I|/X\to0$ for fixed $w$. The power bound uses only nonnegative proper-power coefficients, a union bound and the established Chebyshev bound; it assumes no target pair. All estimates refer to the same $X,N,w$ and truncations.

Thus uniform $A_3=o_w(X)$ and uniform $r_X=F_X+o_w(X)$ are equivalent quantitative assertions. The reverse direction is as valid as the forward one. For a lower bound, the epsilon-half argument in T75.1 correctly preserves asymptotic inequalities with slack, not an exact finite boundary. With $F_X\ge c_wX$, the unproved $A_3\ge-c_wX/2$ gives $r_X\ge c_wX/4$ once the error is at most $c_wX/4$.

**Verdict V75:** correct, with no hidden circular premise in the identity or equivalence. Circularity would arise only if its unproved signed premise were then cited as an established input. Positivity applies to the ordered weighted coefficient; on $H$, the absent equal-prime diagonal converts a positive coefficient to an unordered distinct prime pair. The base-3 coordinates have no role in proving positivity. Eventual positivity alone does not certify the remaining finite targets.

## 5. Final classification and stopping decision

| Class | Assessment |
|---|---|
| Established external theorems | E1 Bombieri–Vinogradov; E2 classical PNT/Möbius and Chebyshev bounds |
| Verified project deductions | T73.5 with explicit mesh schedule; T74.3 analytic uniformity and normalization; T75.1 exact signs and quantitative equivalences |
| Conditional claim | The signed Type II margin would force eventual true-prime positivity |
| Unresolved obligation | An independently proved uniform signed actual-prime correlation margin, and any effective finite connection needed for universality |
| New applicable arithmetic theorem | None established by this audit |

No invalid implication or missing hypothesis requiring correction was found in the three stated deductions. Their existing fixed-weight, positive-even-target and fixed-polynomial-parameter restrictions must remain explicit. Extending any of these domains without a new proof would be unjustified. This is validation of a restricted dependency chain, not a certification of every result in Stages 69–75 or an exhaustive literature search.

There is no new independent input to compare favorably with the first missing theorem of Stage 75. The external results used here already underlie the Type I reduction and contain no signed target-pair lower margin. **Retain NO-GO and stop. No Stage 76 is proposed or begun.** The original three cases and universal Goldbach coverage remain OPEN. No numerical sweep, established Type I finite calculation, or old verification script was rerun.
