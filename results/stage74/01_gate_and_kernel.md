# Stage 74 — Parity gate and evaluation of the truncated Type I kernel

## Gate 0 — novelty and parity decision (one-page gate)

**Classification:** standard external inputs plus proofs assembled here; no claim of mathematical-literature novelty. A repository search of Stages 69–73 and tasks found this exact kernel in Stage 73 and its next-task instruction, but no earlier evaluation. Targeted literature searches for truncated Vaughan/Goldbach Type I main terms and coprime Möbius/totient sums found the classical mechanisms below, not a verified new binary positivity theorem. This is a limited search, not proof of absence from the literature.

The strongest inherited missing statement is, for every residual $N\in[X/2,X]$ and fixed broad weight,
$$A_3(N)-[X\mathfrak S(N)J_w(N/X)-\mathcal M_I(N)]=o_w(X).$$
It is a Hardy–Littlewood-strength signed target theorem, not an established consequence of Type I or first-order distribution. Its positive full-correlation conclusion does **not survive** target-erasing prime deletion: retain the proper-power coefficients but delete a hitting endpoint from every target prime-pair edge. Then the genuine-prime target coefficient is zero and the retained binary von Mangoldt coefficient is at most the unchanged $O_w(\sqrt X\log X)=o(X)$ power correction, whereas the proposed positive main term has order $X$ for the broad weight. The altered sequence is not the immutable actual $\Lambda$ sequence. Neither the exact Vaughan identity with unchanged Möbius coefficients nor maximal BV accuracy is asserted to survive deletion. Thus this is a no-go for deducing positive correlation from deletion-stable premises, not a counterexample satisfying the actual-prime theorem hypotheses. **Decision:** record that no-go, drop Type II proof development, and continue only the self-contained Type I evaluation. No parity-breaking estimate is claimed.

**Sources actually inspected on 2026-11-11:** H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I: Classical Theory* (Cambridge, 2007), Ch. 6, [author-hosted PDF](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/10.0_pp_168_198_The_Prime_Number_Theorem.pdf), (6.17)–(6.19), Exercises 16–18; DOI printed in PDF [10.1017/CBO9780511618314.008](https://doi.org/10.1017/CBO9780511618314.008). These already contain the quantitative Möbius baseline and closely related coprime and totient sums. T. Tao, [*254A Notes 3*](https://terrytao.wordpress.com/2015/01/10/254a-notes-3-the-large-sieve-and-the-bombieri-vinogradov-theorem/), 2015-01-10, discrepancy definition and Theorem 17, supplies the checked BV convention for the audit. Classical methods are reused; no unscreened preprint is a premise. Exact downloaded hashes are in the manifest.

## Domain and definitions

The original cases $N=p+1$, $N=2p$, $N=p+q$ with $p<q$ remain unchanged. Set $H=\{N\ge4:N\text{ even},N-1,N/2\text{ composite}\}$ and let $R(N)$ count unordered distinct genuine-prime pairs. The positions $p=3+2a$, $q=3+2b$, $a+b=N/2-3$ include prime 3 at $a=0$ and assert no simultaneous primality. Prime 2 cannot occur in an even target above 4; $H$ removes the diagonal.

Fix nonnegative $w\in C_c^\infty((0,1))$, supported in $[\sigma,\rho]$ with $0<\sigma<\rho<1$, and use the immutable full genuine-prime polynomial of Stage 73. The kernel evaluation below is arithmetic and does not require $R(N)>0$. Put $h_N(t)=w(t/X)w((N-t)/X)$, $J_w(\tau)=\int w(u)w(\tau-u)du$, $U=V=\lfloor X^{1/5}\rfloor$ and
$$a_N(d)=\frac{\mu(d)1_{(d,N)=1}}{\varphi(d)},\quad A_N(y)=\sum_{d\le y}a_N(d),\quad B_N(y)=\sum_{d\le y}a_N(d)\log d,$$
$$c_l=\sum_{dm=l,d\le U,m\le V}\mu(d)\Lambda(m),\quad
C_N(U,V)=\sum_{l\le UV,(l,N)=1}\frac{c_l}{\varphi(l)},$$
$$\mathcal K_{U,V,N}(t)=A_N(U)\log t-B_N(U)-C_N(U,V),\quad
\mathcal M_I(N)=\int h_N(t)\mathcal K_{U,V,N}(t)dt.$$
All cutoffs are inclusive. The formula below holds for all **positive even** $N\le X$, and therefore on the required residual range; $N=0$ is excluded.

## Gate 1 — independent audit of T73.5

Regroup the exact Vaughan term as $A_2=\sum_{l\le UV}c_l\sum_k\Lambda(N-lk)h_N(lk)$. Independently of any totient factorization,
$$|c_l|\le\sum_{m\mid l}\Lambda(m)=\log l.$$
For reduced $(N,l)=1$ change variable $x=N-lk$ and integrate the compactly supported weight $f(x)=h_N(N-x)$ against the Stieltjes measure $d\psi(x;l,N)$. Subtract $dx/\varphi(l)$. The discrepancy error is at most $\operatorname{Var}(f)\sup_{y\le X}|\psi(y;l,N)-y/\varphi(l)|$. In $A_1$, replace $f$ by $h_N(N-x)\log((N-x)/d)$; its variation is $O_w(\log X)$ because $N-x\ge\sigma X$. There is no endpoint contribution since the weight vanishes off a compact subinterval of $(0,X)$. This gives the same main kernel directly in the reflected variable, independently of the original arrangement.

If $(N,l)>1$, only $x=p^j$ with $p\mid(N,l)$ can have nonzero $\Lambda(x)$. Each prime base contributes at most $\log X$, so the nonreduced total per modulus is at most $O_w(\omega(N)\log X)=O_w(\log^2X)$; the additional logarithm from $c_l$ or $A_1$ yields $O_w(UV\log^3X)$.

The inspected BV theorem centers at the mass coprime to $l$, not at $X$. Replacing this center by total $\psi(y)$ costs at most $\omega(l)\log X/\varphi(l)$; its modulus sum is $O(\log^4X)$. Quantitative PNT handles the total-mass replacement. On a mesh of spacing $\Delta\asymp X/\log^C X$, endpoint BV at every positive grid point applies to $Q=UV\le X^{2/5}$, including the first grid point. Monotonicity bounds between-point discrepancies by endpoint errors plus $\Delta/\varphi(l)$, including the interval starting at zero. Since $\sum_{l\le Q}1/\varphi(l)\ll\log^2(2Q)$, the interpolation error is $O(X\log^{2-C}X)$. Choose $C$ and the BV saving exponent large in terms of the desired fixed $A$. The small-$n$ Vaughan boundary vanishes once $V<\sigma X$.

**Audit verdict: passes.** For each fixed $A>0$, uniformly for $N\in[X/2,X]$,
$$G_X(N)=\mathcal M_I(N)+A_3(N)+O_{A,w}(X\log^{-A}X+X^{2/5}\log^3X).$$
The exact checks below audit grouped coefficients, shared-prime factors, inclusive endpoints and nonreduced prime-power bookkeeping; finite tests do not verify BV or an asymptotic cutoff.

## Gate 2a — exact kernel evaluation; first derivation

Let
$$H_N(V)=\sum_{p^j\le V,p\nmid N}\frac{\log p}{\varphi(p^j)},\qquad J_p=\max\{j\ge1:p^j\le V\}.$$
Splitting each nonzero $m=p^j$ term according to $p\mid d$ or $p\nmid d$ gives the exact identity
$$\boxed{C_N(U,V)=H_N(V)A_N(U)+\sum_{p\le\min(U,V),p\nmid N}
\frac{\log p(1-p^{-J_p})}{(p-1)^3}A_{Np}(U/p).}\tag{74.1}$$
Indeed, for squarefree $d$,
$$\frac1{\varphi(dp^j)}=\frac1{\varphi(d)}\begin{cases}
1/\varphi(p^j),&p\nmid d,\\1/p^j,&p\mid d.
\end{cases}$$
Their correction is $-1/[\varphi(d)(p-1)p^j]$. Moreover
$$\sum_{d\le U,p\mid d,(d,N)=1}\frac{\mu(d)}{\varphi(d)}=-\frac1{p-1}A_{Np}(U/p).$$
Sum the geometric powers $p^{-j}$ to obtain (74.1), including its **positive** correction sign. Thus a finite, fully coprime-preserving evaluation is
$$\mathcal K=A_N(U)[\log t-H_N(V)]-B_N(U)-\sum_p\frac{\log p(1-p^{-J_p})}{(p-1)^3}A_{Np}(U/p).$$

**Exact boundary obstruction to the tempting factorization:** $N=16\in H$, $U=V=3$ has $A_{16}(3)=1/2$ and $C_{16}(3,3)=(\log3)/3$. Replacing $\varphi(dm)$ by $\varphi(d)\varphi(m)$ incorrectly gives $(\log3)/4$. The missing correction is $(\log3)/12$, since $\varphi(9)=6\ne4=\varphi(3)^2$. Consequently the correct kernel is $(\log t)/2+(\log3)/6$, whereas that naive formula gives $(\log t)/2+(\log3)/4$. At $U=V=1$ the exact kernel is $\log t$, so the asymptotic below is never asserted at a fixed small cutoff.

## Gate 2b — uniform asymptotic, including targets with many small divisors

**External established baseline:** quantitative PNT for Möbius gives $\sum_{n\le y}\mu(n)\ll y\exp(-c_0\sqrt{\log y})$. Partial summation, ordinary convergence and $1/\zeta(1+s)=s+O(s^2)$ imply, after reducing a positive constant,
$$A_\mu(y):=\sum_{n\le y}\frac{\mu(n)}n=O(e^{-c_0'\sqrt{\log y}}),\quad
B_\mu(y):=\sum_{n\le y}\frac{\mu(n)\log n}n=-1+O(e^{-c_0'\sqrt{\log y}}).$$
For completeness the tails follow by integrating the Möbius summatory bound against $1/t$ and $\log t/t$; powers of $\log y$ are absorbed by reducing $c_0'$. Uniform convergence of those tail integrals for real $s\ge0$ justifies the limits of $1/\zeta(1+s)$ and its derivative. No unproved zero-free half-plane is used.

Define a multiplicative $g_N$ by $g_N(1)=1$ and
$$g_N(p^j)=\begin{cases}p^{-j},&p\mid N,\\-1/[p^j(p-1)],&p\nmid N,\end{cases}\qquad j\ge1.$$
Euler factors give the exact convolution
$$a_N=(\mu(n)/n)*g_N.$$
For each fixed even $N$, $\sum|g_N(k)|k^{1/4}<\infty$ with a constant depending on $N$. The convolution immediately yields $A_N(U)=O_N(e^{-c\sqrt{\log U}})$, $B_N(U)=-\sum g_N+O_N(e^{-c\sqrt{\log U}})$. This fixed-parameter statement alone is insufficient when $N\asymp X$.

**Uniform transfer lemma (proved here).** For any fixed $B,\alpha,\beta>0$ with $\alpha\le\beta$, uniformly for positive even $N\le X^B$ and $X^\alpha\le y\le X^\beta$,
$$A_N(y)=O_{B,\alpha,\beta}(e^{-c\sqrt{\log X}}),\qquad
B_N(y)=-\mathfrak S(N)+O_{B,\alpha,\beta}(e^{-c\sqrt{\log X}}).\tag{74.2}$$
Here $c>0$ may depend on the displayed fixed parameters. A proof that explicitly treats large collections of small prime divisors follows.

Put $L=\log X$ and $T_N=\sum|g_N(k)|k^{1/4}$. The local factors for $p\nmid N$ are $1+[p^{-3/4}/((p-1)(1-p^{-3/4}))]$, whose logarithms sum absolutely. For $p\mid N$ the factor is $(1-p^{-3/4})^{-1}$. Split those prime divisors at $L$: the small part has $\sum_{p\le L}p^{-3/4}\le\sum_{n\le L}n^{-3/4}\ll L^{1/4}$. There are at most $B L/\log L$ prime divisors above $L$, each contributing at most $L^{-3/4}$ before an absolute constant. Therefore
$$T_N\le C\exp(C_B L^{1/4})$$
uniformly, even when $N$ has many small prime divisors. No fixed-$N$ implied constant is imported.

Write $A_N(y)=\sum_{k\le y}g_N(k)A_\mu(y/k)$ and split at $k=\sqrt y$. The lower part is bounded by $T_Ne^{-c_1\sqrt{\log y}}$; the upper part is at most $T_Ny^{-1/8}(1+\log y)$. Similarly
$$B_N(y)=\sum_{k\le y}g_N(k)[B_\mu(y/k)+(\log k)A_\mu(y/k)].$$
Its difference from $-\sum_k g_N(k)$ is bounded by
$$O\!\left(T_N(1+\log y)^2[e^{-c_1\sqrt{\log y}}+y^{-1/8}]\right).$$
This is $O(e^{-c\sqrt L})$ in the stated polynomial range. The absolutely convergent Euler product evaluates the constant independently of the estimates:
$$\sum_k g_N(k)=\prod_{p\mid N}\frac p{p-1}\prod_{p\nmid N}\left(1-\frac1{(p-1)^2}\right)
=2C_2\prod_{p\mid N,p>2}\frac{p-1}{p-2}=\mathfrak S(N),$$
where $C_2=\prod_{p>2}(1-1/(p-1)^2)>0$. Evenness removes the zero factor at 2; it is an essential hypothesis, not a cosmetic parity condition. This proves (74.2).

Apply (74.2) at $y=U\asymp X^{1/5}$. The elementary bound $H_N(V)\ll\log^2(2V)$ handles the first term in (74.1). In its correction sum, $p\le\sqrt U$ gives $U/p\ge\sqrt U$ and $Np\le X^{6/5}$, so (74.2) again applies uniformly. For larger p use $|A_{Np}(U/p)|\ll\log^2(2U)$ and
$$\sum_{p>\sqrt U}\frac{\log p}{(p-1)^3}\ll\frac{\log(2U)}U.$$
Thus the correction is exponentially small after including its $O(\log^3(2U)/U)$ tail, and $C_N(U,V)=O(e^{-c\sqrt{\log X}})$ uniformly. Since $\log t=O_{\sigma,\rho}(\log X)$,
$$\boxed{\mathcal K_{U,V,N}(t)=\mathfrak S(N)+O_{\sigma,\rho}(e^{-c\sqrt{\log X}})}\tag{74.3}$$
for all positive even $N\le X$, $t\in[\sigma X,\rho X]$, sufficiently large $X$. It follows that
$$\boxed{\mathcal M_I(N)=X\mathfrak S(N)J_w(N/X)+O_w(Xe^{-c\sqrt{\log X}})}\tag{74.4}$$
uniformly for the required residual targets. The bounds are absolute errors, not merely relative to a possibly growing singular series. Floors are absorbed using $\lfloor X^{1/5}\rfloor\ge X^{1/5}/2$ at large $X$. No numerical cutoff or optimized constant is supplied.

## Gate 2c — second derivation, using a different treatment of the shared-prime term

The following derivation was also obtained by the proof-blind review without access to the preceding argument. Let $b(n)=\mu(n)/n$ and remove the entire p-local factor of $g_N$ to obtain $g_{N,p}$, so $g_{N,p}(n)=0$ if $p\mid n$ and equals $g_N(n)$ otherwise. For $p\nmid N$ and $j\ge1$, compare the two possible squarefree exponents of p in d. The p-local series of $\mu(d)1_{(d,N)=1}/\varphi(dp^j)$ is
$$\frac1{\varphi(p^j)}\left(1-\frac{p^{-s}}p\right).$$
All other factors are unchanged. Thus exactly
$$\sum_{d\le U,(d,N)=1}\frac{\mu(d)}{\varphi(dp^j)}
=\frac1{\varphi(p^j)}\sum_{d\le U}(b*g_{N,p})(d).\tag{74.5}$$
This cancels the p-local factor through $1/\zeta(1+s)$ rather than explicitly summing the correction in (74.1). Its absolute $1/4$ moment is no larger than $T_N$ because an absolute Euler factor of size at least one is removed. The transfer proof therefore bounds the last sum by $O(e^{-c\sqrt{\log X}})$ **uniformly in p and j**. Summing (74.5) against $\log p$ over $p^j\le V$, $p\nmid N$, gives the same small $C_N(U,V)$, since $\sum_{p^j\le V}\log p/\varphi(p^j)\ll\log^2(2V)$. Combined with (74.2) this independently recovers (74.3)–(74.4), avoiding the prime-tail split. The derivations share the stated classical Möbius input, but differ in their exact arithmetic treatment of $\varphi(dp^j)$.

## Gate 3 — finite validation and result labels

`verify_stage74.py` uses exact fractions, trial factorization and sparse formal logarithms; `verify_stage74_sage.py` independently groups polynomial coefficients over Sage QQ and constructs multiplicative convolution factors. Neither imports the other. The declared parameter grid is $U,V=1,\ldots,12$, $N=2,6,16,28,210,2310,30030,510510$; it tests the two exact kernel representations and grouped coefficient bound. Convolution coefficients are checked for $n\le64$; removed-local identities use $p=3,5,7,11$, $j=1,2,3$ when $p\nmid N$. These are finite algebra checks, not evaluations of an asymptotic error or a Goldbach sweep. Full counts, exact counterexample, executed commands, runtime and source hashes are embedded in the manifest.

- **Established external:** BV, quantitative Möbius/PNT, classical singular-series Euler product.
- **Proved here:** (74.1), uniform transfer proof, (74.3)–(74.5), and the quantified fixed-versus-varying target distinction; these are classical-method project deductions, without a literature-novelty claim.
- **Computational observations:** the declared finite exact identities and counterexample pass independently.
- **Refuted:** the naive totient separation at the displayed boundary; extending target positivity to deletion-stable model data.
- **Conditional/open obligation:** the Type II estimate named in Gate 0 is unproved and dropped from research under the parity gate. Combining the kernel evaluation with T73.5 only recenters that missing term; it does not control its sign or prove $R(N)>0$.
