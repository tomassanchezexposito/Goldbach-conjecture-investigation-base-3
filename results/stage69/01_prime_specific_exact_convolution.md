# M1 — Exact prime-specific convolution and dependency audit

## Scope and definitions

Fix $X>0$ and a real-valued smooth function $w$ of compact support in $(0,\infty)$ with $w\geq0$. Put
\[
 a_p=(\log p)w(p/X),\qquad S_w(\alpha)=\sum_{p\ \mathrm{prime}}a_p e(p\alpha),\qquad e(x)=e^{2\pi ix}.
\]
All sums are finite. A zero weight is allowed. Define
\[
 r_w(n)=\int_{\mathbb T}S_w(\alpha)^2e(-n\alpha)\,d\alpha,
 \qquad R(n)=\#\{p<q:p,q\text{ prime},\ p+q=n\}.
\]
The residual set remains
\[
 H=\{n\ge4:n\text{ even},\ n-1\text{ composite},\ n/2\text{ composite}\}.
\]

## Exact coefficient and edge cases

Expanding the finite polynomial and using $\int_{\mathbb T}e(k\alpha)d\alpha=1_{k=0}$ gives the identity
\[
 r_w(n)=\sum_{p+q=n}a_pa_q.
\]
This is an **ordered** sum. If $n\in H$, the diagonal $p=q=n/2$ is absent because $n/2$ is composite, so
\[
 r_w(n)=2\sum_{p<q,\ p+q=n}a_pa_q.
\]
It is not in general a fixed multiple of $R(n)$: the factor on an unordered pair is $2(\log p)(\log q)w(p/X)w(q/X)$ and varies with the pair. Moreover, a pair counted by $R(n)$ can contribute zero if either weight vanishes. If all possible summands lie in a region where $0<c\le w\le C$, then the displayed expression gives explicit pairwise bounds using $2c^2\log p\log q$ and $2C^2\log p\log q$; such a hypothesis is not automatic.

For even $n>4$, the prime 2 cannot occur: $n-2$ is an even integer greater than 2 and is composite. The prime 3 is not excluded; its possible contribution is the pair $(3,n-3)$ when $n-3$ is prime and the weight is nonzero. The endpoint $n=4$ is outside $H$ and has the diagonal representation $2+2$. These facts are independent of any Fourier approximation.

## Prime powers and the von Mangoldt replacement

Let $Y=\lfloor Xb\rfloor$, where $b=\sup\operatorname{supp}w$; if $Y<2$ all sums below are empty. Write
\[
 U_w(\alpha)=\sum_{m\ge1}\Lambda(m)w(m/X)e(m\alpha)=S_w(\alpha)+Q_w(\alpha),
\]
where $Q_w$ is supported on prime powers $m=p^k$, $k\ge2$, and has coefficient $(\log p)w(p^k/X)$. Prime factorization makes these power positions distinct. Set $M=\|w\|_\infty$ and
\[
 K(Z)=\#\{p^k\le Z:p\text{ prime},\ k\ge2\},\qquad K(Z)\le \lfloor\log_2 Z\rfloor\lfloor\sqrt Z\rfloor\quad(Z\ge2).
\]
The last inequality follows by summing the crude upper bound $Z^{1/k}\le\sqrt Z$ over $2\le k\le\lfloor\log_2 Z\rfloor$; it is intentionally elementary and may overcount.

For each integer $n$, coefficient extraction gives exactly
\[
 [U_w^2-S_w^2]_n=2(a* b)_n+(b*b)_n,
\]
where $a_m=(\log m)w(m/X)1_{m\text{ prime}}$ and $b_m=\Lambda(m)w(m/X)1_{m=p^k,\ k\ge2}$. For $Z=\min(Y,n-1)$ and $Z\ge2$, each prime-power position has at most one complementary summand. Hence
\[
 \big|[U_w^2-S_w^2]_n\big|\le 3K(Z)M^2(\log Z)^2.
\]
If $Z<2$ the correction is zero. The factor 2 is the two cross-convolution orders; the remaining factor 1 is the prime-power/prime-power convolution. This estimate includes every prime-power contribution, including diagonal terms, without assuming a representation. For fixed support endpoint and $n\asymp X$, its crude size is $O_w(\sqrt X(\log X)^3)$, which is $o(X)$, but only as an absolute deterministic coefficient error. It does not manufacture a positive major-arc main term at a target, and it does not justify transferring an unquantified major-arc asymptotic. Any claimed source main term must still dominate this explicit error uniformly in the relevant $n$.

The diagonal distinction is worth making explicit. In $S_w^2$, a diagonal term exists only if $n/2$ is prime and equals $a_{n/2}^2$. In $U_w^2$, the coefficient at $n/2$ can also be a prime power. The identity $U_w^2-S_w^2=2S_wQ_w+Q_w^2$ accounts for these differences exactly; no extra factor of two is attached to a diagonal term.

## Fourth moment and multiplicities

Parseval for the finite polynomial gives both exact forms
\[
 \int_{\mathbb T}|S_w(\alpha)|^4d\alpha=\sum_t r_w(t)^2
 =\sum_{p_1+p_2=p_3+p_4}a_{p_1}a_{p_2}a_{p_3}a_{p_4}.
\]
The quadruples are ordered in all four positions. To display the induced multiplicities, let $\mathcal U_t$ be unordered distinct prime pairs at target $t$, put $v_{\{p,q\}}=a_pa_q$, and let $d_t=a_{t/2}^2$ if $t/2$ is prime and zero otherwise. Then
\[
 r_w(t)^2=4\sum_{A\in\mathcal U_t}v_A^2
 +8\sum_{\{A,B\}\subset\mathcal U_t,\ A\ne B}v_Av_B
 +4d_t\sum_{A\in\mathcal U_t}v_A+d_t^2.
\]
Thus one unordered off-diagonal representation squared has four ordered realizations; two different unordered representations at the same target have eight cross realizations. A diagonal pair has one ordered realization, and its cross term with a distinct pair has multiplicity four.

Two different unordered representations at the **same** target cannot share exactly one prime: if both contain $p$, their other member must equal $t-p$. The eight-fold cross terms therefore use four distinct prime values. A diagonal representation $\{p,p\}$ and a different representation $\{r,s\}$ at $2p$ have three distinct values; neither $r$ nor $s$ can equal $p$ unless both do. This classifies the same-target coincidences. For two different targets $u\ne v$, however, representations can share exactly one prime: $\{p,u-p\}$ and $\{p,v-p\}$ share $p$ and generally have distinct complements. This is a different, shifted-target correlation and is recorded in the M4 ledger.

For any measurable $E\subset\mathbb T$, the restricted coefficient is
\[
 I_E(n)=\int_E S_w(\alpha)^2e(-n\alpha)d\alpha
 =\sum_t r_w(t)\widehat{1_E}(n-t),\quad \widehat{1_E}(k)=\int_Ee(-k\alpha)d\alpha.
\]
The Fourier coefficients $\widehat{1_E}$ are generally complex/signed. Therefore $\int_E|S_w|^4$ and $I_E(n)$ have different combinatorics: the former is a nonnegative additive energy only on the full circle, while the latter is a signed convolution with an arc indicator. A minor-arc fourth moment is a nonnegative integral of $|S_w|^4$ but is not the same as a nonnegative count of prime quadruples satisfying one integer equation.

## Exact shift identity

For integer $j$, define
\[
 \Delta_{E,j}(n)=I_E(n+j)-I_E(n)
 =\int_E S_w(\alpha)^2e(-n\alpha)(e(-j\alpha)-1)d\alpha.
\]
In frequency space this is exactly
\[
 \Delta_{E,j}(n)=\sum_t r_w(t)\{\widehat{1_E}(n+j-t)-\widehat{1_E}(n-t)\}.
\]
This identity preserves the target phase and the shift sign. It supplies no sign for either coefficient.

## Half-period and the exact support condition

The equality $S_w(\alpha+1/2)=-S_w(\alpha)$ holds exactly when the coefficient at the only even prime, 2, vanishes, that is, when $w(2/X)=0$. (If that coefficient is nonzero, the constant Fourier mode from $p=2$ breaks the equality.) In this case $S_w^2$ is $1/2$-periodic, so its full Fourier expansion has only even frequencies. For $I_E(n)$, if $E$ is invariant under translation by $1/2$, then changing variables shows $I_E(n)=(-1)^n I_E(n)$; thus odd $n$ coefficients vanish, as they must. For even $n$ this gives no cancellation.

For a set not invariant under this translation, put $\tau=1/2$, $C=E\cap(E+\tau)$, $W=E\setminus(E+\tau)$, and $W'= (E+\tau)\setminus E$. The translation formula is
\[
 I_{E+\tau}(n)=(-1)^n I_E(n).
\]
The symmetric hull $E\cup(E+\tau)$ has integral $I_C(n)+I_W(n)+I_{W'}(n)$; the unmatched-wing contribution is explicit and cannot be discarded. More directly, for even $n$, translation identifies the integrals over $W$ and $W'$, while for odd $n$ they have opposite signs. Thus reflected pairing gives a factor of two for even targets and cancellation for odd targets; on $H$ only the former applies. This symmetry does not provide a negative minor term cancellation at the target under study.

## Base-3 position coordinates: exact reparametrization

For $n\in H$, every summand is odd, so write $p=3+2a$, $q=3+2b$ with integers $a,b\ge0$. Define
\[
 P_X(a)=1_{3+2a\text{ prime}}(\log(3+2a))w((3+2a)/X).
\]
Then, exactly and with $p=3$ retained at $a=0$,
\[
 r_w(n)=\sum_{a+b=n/2-3}P_X(a)P_X(b),\qquad n\in H.
\]
The two ordered positions remain present; since $n/2-3>0$ on $H$, there is no equal-index prime diagonal. Define $F_X(\theta)=\sum_{a\ge0}P_X(a)e(a\theta)$. The odd-prime polynomial obeys
\[
 S_w(\alpha)=e(3\alpha)F_X(2\alpha),\qquad
 r_w(n)=[F_X^2]_{n/2-3}=\int_{\mathbb T}F_X(\theta)^2e(-(n/2-3)\theta)d\theta.
\]

This is a change of variables, not a new additive-energy theorem: Parseval in the $a$ coordinate reproduces the same energy after an affine reindexing and the frequency dilation $\alpha\mapsto2\alpha$, with phase $e(3\alpha)$. A cutoff in $p/X$ becomes the corresponding cutoff in $(3+2a)/X$; it is not a sharp interval in $a$ unless $w$ is chosen that way.

## Dependency graph and status

```mermaid
flowchart TD
  P[Actual weighted prime coefficients a_p] --> C[Exact convolution r_w(n)]
  C --> T[Target positivity r_w(N)>0]
  C --> E[Full-circle additive energy sum_t r_w(t)^2]
  C --> F[Restricted coefficient I_E(N), signed Fourier convolution]
  W[Wheel/CRT admissibility] --> C
  W -. necessary residues only .-> T
  G[Arc geometry / Gram or L2 bounds] --> F
  E --> G
  V[Von Mangoldt polynomial] --> Q[Explicit prime-power correction]
  Q --> C
```

The arbitrary-$L^2$ spike extremizer for a single Fourier coefficient need not be a square of a polynomial with nonnegative prime coefficients; this report proves no quantitative distance from that extremizer to the actual prime-square class. Conversely, the positivity of $a_p$ proves the exact full convolution and full energy are nonnegative, but it does not force a restricted coefficient $I_E(N)$ to be nonnegative. Modulus admissibility and arc-Gram estimates are inputs about the allowed geometry, not proof of simultaneous primality. The sole target-specific prime arithmetic content that would settle the issue is a lower bound for this coefficient (or an independent lower bound for the unweighted pair count) at each prescribed $N$.

**Potential circularity and first missing arithmetic fact.** Any use of a selected representation in the energy expansion to lower-bound $r_w(N)$ is circular. The first missing input is an independent, uniform target estimate for the genuine-prime pair convolution; none of the identities above supplies one.

## M1 verdict

The prime-only Fourier coefficient, the prime-power error, full additive energy, shifted coefficient identity, half-period rule, and base-coordinate convolution are exact. The base coordinate is a reparametrization, not new arithmetic control. No Goldbach positivity theorem follows.
