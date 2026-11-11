# Stage 73 — Signed rational cores and the remaining complement

Evidence: internally proved identities and deductions from classical fixed-modulus PNT; no claim of literature novelty or universal Goldbach coverage.

## 1. Fixed object and Stage 72 audit

Throughout $w\in C_c^\infty((0,1))$ is fixed, real, nonnegative and nonzero. Choose fixed $0<\sigma<\rho<1$ with $\operatorname{supp}w\subset[\sigma,\rho]$, and put $W=\int w>0$, $M=\|w\|_\infty$, $a_p=(\log p)w(p/X)$ and $S(\alpha)=\sum_p a_pe(p\alpha)$, $e(t)=\exp(2\pi it)$. This is the immutable full actual-prime polynomial. All changes of coefficients below are explicitly adversarial models.

$H=\{N\ge4:N\text{ even},N-1\text{ composite},N/2\text{ composite}\}$ and $R(N)=\#\{p<q:p,q\text{ primes},p+q=N\}$. The three cases are $N=p+1$, $N=2p$, or $N=p+q$ with $p<q$. For odd primes $p=3+2a$, $q=3+2b$, $a+b=N/2-3$; $a=0$ retains prime 3. Prime 2 cannot occur for even $N>4$ and $p=q$ is impossible on $H$. Orthogonality gives the ordered coefficient $r(N)=\int S^2e(-N\alpha)=\sum_{p+q=N}a_pa_q$; on $H$ each weighted unordered pair contributes twice.

For $N\in[X/2,X]$, $-X<p+q-N<3X/2$. With $J=[-1/(6X),1/(6X)]$ and
$$k_X(u)=\int_J e(u\beta)d\beta=\frac1{3X}\operatorname{sinc}\frac{\pi u}{3X},$$
concavity of sine on $[0,\pi/2]$ proves $k_X(p+q-N)\ge2/(3\pi X)$. Thus
$$C_1(N)=\int_J S^2e(-N\alpha)\ge\frac{2}{3\pi X}S(0)^2.$$
This independently proves Stage 72's finite bound. Weighted PNT gives $S(0)=WX+o_w(X)$ and its conservative $C_1\ge W^2X/(6\pi)$ for sufficiently large $X$. The sharper asymptotic lower estimate is $C_1\ge 2W^2X/(3\pi)+o_w(X)$. Reflection makes these integrals real. Positivity of a restricted integral does not imply positivity of its full coefficient.

**Support limitation:** $w$ need not admit a pair for every $N$. Even $w>0$ around every possible midpoint merely admits candidate positions; it proves no simultaneous primality. We claim only weighted positivity implies a representation, never the converse for arbitrary $w$.

## 2. T73.1 — exact wheel projector, two independent derivations

Let an integer $D\ge1$ be fixed and $X>\max(2,D/3)$. The $D$ intervals
$$\mathcal A_D=\bigsqcup_{a=0}^{D-1}(a/D+J)\subset\mathbb T$$
are disjoint up to null endpoints. Define $C_D(N)=\int_{\mathcal A_D}S^2e(-N\alpha)$. For residue masses $M_r=\sum_{p\equiv r\pmod D}a_p$, the following exact identity and finite bound hold for every integer $N\in[X/2,X]$:
$$C_D(N)=D\sum_{p+q\equiv N\ (D)}a_pa_q k_X(p+q-N)
\ge L_D(N):=\frac{2D}{3\pi X}\sum_{r\ (D)}M_rM_{N-r}.$$

**Proof A (frequency projector).** Translate each arc by $a/D$ and expand the finite square. The center sum is $\sum_{a=0}^{D-1}e(a(p+q-N)/D)=D1_{D\mid p+q-N}$. Apply the nonnegative sinc lower bound termwise. This also proves reality and includes small primes automatically.

**Proof B (residue Fourier transform).** Set $S_r(\beta)=\sum_{p\equiv r(D)}a_pe(p\beta)$. Substituting $S(a/D+\beta)=\sum_r e(ar/D)S_r(\beta)$ and summing the resulting finite discrete transform gives $D\sum_r S_r(\beta)S_{N-r}(\beta)e(-N\beta)$. Integration and expansion of each $S_rS_{N-r}$ yields the same formula. In particular the mass term at $\beta=0$ is exactly $D\sum_r M_rM_{N-r}$, not a prime-pair count.

For $D=1$ this recovers Stage 72; for $D=2$ and $\sigma X>2$, odd-prime support gives exactly $C_2(N)=2C_1(N)$ for even $N$. These are boundary consistency checks.

## 3. T73.2 — fixed-wheel signed asymptotic and exact minimum for 210

For fixed $D$, let $A_D(N)=\#\{r\pmod D:(r,D)=(N-r,D)=1\}$ and
$$F_D(N)=\frac{D A_D(N)}{\varphi(D)^2}.$$
Classical PNT in each of the finitely many reduced progressions, followed by partial summation, gives uniformly in bounded $t$,
$$S(a/q+t/X)=\frac{\mu(q)}{\varphi(q)}X V(t)+o_{w,D}(X),\quad V(t)=\int_0^1w(u)e(tu)du,$$
for reduced $a/q$ with $q\mid D$. To justify uniformity, partial summation applies to the family $w(u)e(tu)$ with derivatives uniformly bounded for $|t|\le1/6$. Primes dividing $D$ are absent once $\sigma X$ exceeds the largest such prime. The principal residue sum is $c_q(a)=\mu(q)$; no replacement is asserted for growing $D$.

Put $\tau=N/X$ and
$$K_w(\tau)=\int_{-1/6}^{1/6}V(t)^2e(-\tau t)dt
=\iint w(u)w(v)\frac13\operatorname{sinc}\frac{\pi(u+v-\tau)}3\,du\,dv
\ge\frac{2W^2}{3\pi},\quad\tau\in[1/2,1].$$
Grouping the centers by reduced denominator gives the unconditional, target-uniform fixed-$D$ asymptotic
$$C_D(N)=XF_D(N)K_w(N/X)+o_{w,D}(X),\qquad
F_D(N)=\sum_{q\mid D}\frac{\mu(q)^2 c_q(N)}{\varphi(q)^2}.$$
The error follows by squaring $O(X)$ terms with uniform $o(X)$ errors, integrating arcs of length $1/(3X)$ and summing finitely many centers. The coefficient identity also follows independently from the CRT count in T73.1. For squarefree $D$ the local factor is
$$F_D(N)=\prod_{\ell\mid D}\frac{\ell(\ell-\nu_\ell(N))}{(\ell-1)^2},\quad
\nu_\ell(N)=\begin{cases}1&\ell\mid N,\\2&\ell\nmid N.\end{cases}$$
For even $N$, the factor at 2 is 2. For an odd $\ell$ it is $\ell/(\ell-1)$ if $\ell\mid N$, otherwise $\ell(\ell-2)/(\ell-1)^2$. Hence for every even $N$,
$$\boxed{F_{210}(N)\ge2\frac34\frac{15}{16}\frac{35}{36}=\frac{175}{128},}$$
with equality exactly when $(N,105)=1$. Consequently $C_{210}(N)\ge175W^2X/(192\pi)+o_w(X)$ uniformly over the stated even range. A convenient conservative finite-threshold corollary is
$$C_{210}(N)\ge\frac{175W^2}{768\pi}X$$
for all sufficiently large $X$: use $M_r\ge WX/(2\varphi(210))$ for every reduced class in T73.1. No numerical cutoff is supplied. The factor $175/128$ improves the fixed-core guarantee through additional rational arcs; it is only finite-wheel arithmetic.

## 4. Disjoint complete complement, exact phases and missing lemma

Write $\mathcal B_D=\mathbb T\setminus\mathcal A_D$ and $E_D(N)=\int_{\mathcal B_D}S^2e(-N\alpha)$. Always $r(N)=C_D(N)+E_D(N)$. To resolve the remainder, fix $Q\ge D$, $L>0$, enumerate all reduced $a/q$, $q\le Q$, and their radius $L/(qX)$ neighborhoods. Intersect them with $\mathcal B_D$ and assign any overlaps to the first center in a fixed order. These disjoint measurable pieces $E_{a/q}$, together with $\mathcal M=\mathcal B_D\setminus\bigcup E_{a/q}$, form an exhaustive partition. Thus
$$E_D(N)=\sum_{a/q}\int_{E_{a/q}}S^2e(-N\alpha)+\int_{\mathcal M}S^2e(-N\alpha).$$
Reflection pairing restores real values if individual pieces are complex. A numerator sum gives a Ramanujan sum only for identical translated beta domains; overlap-trimmed cells generally do not have that property. No such replacement is made here.

**Open signed candidate:** now additionally require the fixed $w$ to be positive on $[1/5,3/5]$, and fix $D=210$. The desired unproved input is that there exist $X_0$ and a nonnegative margin $\eta_X>0$ such that for all $X\ge X_0$ and every $N\in H\cap[X/2,X]$,
$$E_{210}(N)\ge-L_{210}(N)+\eta_X.$$
This would imply $r(N)\ge\eta_X>0$. The stronger convenient constant version $E_{210}(N)>-175W^2X/(768\pi)$ suffices at large $X$. Neither is proved. An arbitrary narrow $w$ may make either false; any universal candidate must first fix an admissible broad support, and proving it still requires new arithmetic. With $w>0$ on $[1/5,3/5]$, the expected continuum convolution is uniformly positive, but this remains no theorem about the prime convolution.

A minor-region fourth-moment upper bound $\int_{\mathcal M}|S|^4\le B$ gives only $|\int_{\mathcal M}S^2e(-N\alpha)|\le|\mathcal M|^{1/2}\sqrt B$. It says nothing about the omitted rational pieces. For the inherited conditional $B\ll X^{5/2}\log^{100}X$, even this partial bound is $O(X^{5/4}\log^{50}X)$, exceeding the required $X$ scale. That source claim is not used as an established theorem here. An exceptional-set bound allowing one target also fails to give the displayed quantifier. The first missing estimate is the signed total remainder with an absolute margin, not another positive core.
