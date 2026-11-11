# L76.1 — Exact logical bridge and extension to the boundary targets

## Status and preserved definitions

This is logical closure and a domain extension of already established error estimates, not an arithmetic lower bound. Strong Goldbach and the author's universal three-case assertion remain OPEN. Historical ledgers are unchanged.

For even integers $N\ge4$ let $R(N)=\#\{p<q:p,q\text{ genuine primes},p+q=N\}$. Define
$$C(N)=[N-1\text{ prime}]\lor[N/2\text{ prime}]\lor[R(N)>0],$$
$$H=\{N\ge4:N\text{ even},N-1,N/2\text{ composite}\},\quad H_1=\{N\ge8:N\text{ even},N-1\text{ prime},N/2\text{ composite}\}.$$
Composite means an integer greater than one that is not prime. In particular, 1 is never prime or composite here. The predicates $N-1$ prime and $N/2$ prime mean exactly the author's existential cases $N=p+1$ and $N=2p$.

## Set identities and logical equivalences

Let $D=\{N\ge4:N\text{ even},N/2\text{ composite}\}$. Then $D=H\mathbin{\dot\cup}H_1$. Indeed for $N\in D$, $N/2\ge4$, so $N\ge8$ and $N-1>1$ is either prime or composite, exclusively. Conversely both named sets lie in $D$. No target representation is needed for this partition.

For such $N$, binary Goldbach is exactly
$$B(N)\iff[N/2\text{ prime}]\lor[R(N)>0].$$
Every unordered two-prime representation either has equal endpoints, necessarily $N/2$, or has distinct endpoints counted by $R$. Thus
$$C(N)\iff[N-1\text{ prime}]\lor B(N),$$
$$[\forall N\ge4\text{ even},C(N)]\iff[\forall N\in H,R(N)>0],$$
$$[\forall N\ge4\text{ even},B(N)]\iff[\forall N\in H\cup H_1,R(N)>0].$$
For the middle equivalence, outside $H$ one of the first two cases already holds; inside $H$ neither does. For the last equivalence, outside $D$ the midpoint is prime, and inside $D$ only distinct prime pairs can supply Goldbach. Consequently the three-case assertion together with coverage of $H_1$ is equivalent to binary Goldbach. The three-case assertion alone is not proved equivalent to binary Goldbach. Case I does not make 1 prime and does not itself supply a binary representation. L76.1 resolves the logical discrepancy; it does not solve its arithmetic boundary obligation.

## Positions, midpoint and symmetry

For odd $p\ge3$ there is exactly one nonnegative integer $a=(p-3)/2$ with $p=C_a=3+2a$. The map $a\mapsto C_a$ is a bijection between nonnegative integers and odd integers at least 3; it does not map all indices to primes. For odd $p,q$ and even $N=2m$,
$$p+q=N\iff a+b=m-3,\qquad p=m-h,\ q=m+h,\quad h=(q-p)/2=b-a,$$
$$N-2p=2q-N=q-p.$$
For distinct ordered endpoints $p<q$, $h$ is a positive integer; the midpoint need not be prime. Prime 3 has index zero. Prime 2 contributes to an even two-prime sum only at $N=4$; the odd-position bijection is not applied there. The equal-prime case is absent on $D$.

## Uniform extension of the actual-prime identity

Fix nonnegative $w\in C_c^\infty((0,1))$ and immutable $S_X(\alpha)=\sum_{p\ge2}(\log p)w(p/X)e(p\alpha)$. Its coefficient at 1 is exactly zero. Let $r_X$ be its ordered binary coefficient, and retain the exact Stage 73 definitions of $G_X,A_3,\mathcal M_I$, $U=V=\max(1,\lfloor X^{1/5}\rfloor)$, and the Stage 74 $F_X=X\mathfrak S(N)J_w(N/X)$. Set
$$E_I=G_X-\mathcal M_I-A_3,\quad E_K=\mathcal M_I-F_X,\quad P_X=G_X-r_X.$$
T73.5 is uniform in all integer targets in $[X/2,X]$, T74.3 in all positive even $N\le X$, and the proper-power bound in every target. None requires $N-1$ composite. For each fixed $A>0$ these established deductions give
$$|E_I|\ll_{A,w}X\log^{-A}X+X^{2/5}\log^3X,\quad |E_K|\ll_w Xe^{-c\sqrt{\log X}},\quad0\le P_X\le4C_{\rm Ch}\|w\|_\infty^2\sqrt X\log X\quad(X\ge16).$$
Rearrange the same actual-prime identities, without new terms:
$$\boxed{A_3(N)=r_X(N)-F_X(N)+e_X(N),\quad e_X=P_X-E_K-E_I.}$$
Their errors are $o_w(X)$ uniformly on $D\cap[X/2,X]$, hence on $(H\cup H_1)\cap[X/2,X]$. Empty suprema are zero. This follows from the domains of the estimates, not merely from the zero coefficient at 1. That zero coefficient explains why $N=(N-1)+1$ introduces no prime-pair contribution and no extra Case I term. Neither $r_X>0$ nor a Type II sign is assumed. Weights are fixed, not allowed to shrink with $X$.

## Verification boundary

The companion certificate checks finite rational identities, modular admissibility and abstract matching covers. Those tests do not prove analytic uniformity. Lean was not found on PATH or in the four standard locations checked; the supplied Mathlib-dependent Lean source is UNCOMPILED, not machine-certified. No software is installed. Exact source/verification statuses are in the manifest.
