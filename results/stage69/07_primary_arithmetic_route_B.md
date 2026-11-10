# M7 Route B — reflected prime correlation and sieve limitation

**Verdict: no independent target-uniform prime lower bound obtained.** This route starts with the arithmetic pair count and does not use the minor-arc Cauchy argument.

## 1. Exact reflected count

For even $N\in H$, define $1_{\mathbb P}(n)$ to be one for positive primes and zero otherwise. The ordered convolution is
$$G(N)=\sum_{1\leq n<N}1_{\mathbb P}(n)1_{\mathbb P}(N-n)=2R(N).$$
The factor two is valid because $N/2$ is composite by the definition of $H$, so there is no diagonal; for $N>4$, neither summand is 2. The prime 3 is retained. The map $n\mapsto N-n$ is an involution of the summation interval and accounts for the two orders. This identity does not presuppose $G(N)>0$.

With logarithmic weights, $G_\Lambda(N)=\sum_{n<N}\Lambda(n)\Lambda(N-n)$ is a different object: it includes prime powers. The exact correction to the genuine-prime sum is the convolution correction in M1, not a harmless identity. For $N\asymp X$ and the fixed compact support there, the deterministic correction bound $O_w(\sqrt X(\log X)^3)=o(X)$ is smaller than a positive $cX$ main term, but it cannot create one when none has independently been proved.

## 2. Local congruence count, with endpoint convention

For an odd prime $\ell$ and a residue $r\pmod\ell$, the simultaneous conditions that neither summand be divisible by $\ell$ are $r\not\equiv0$ and $N-r\not\equiv0$. The number of forbidden residues is
$$\nu_\ell(N)=\begin{cases}1,&\ell\mid N,\\2,&\ell\nmid N.\end{cases}$$
For $\ell=2$ and even $N$, only $r=0$ is forbidden; $r=1$ survives. Thus for a squarefree modulus $d$ with primes at least 2, CRT gives the exact density of admissible residue classes
$$\prod_{\ell\mid d}\left(1-\frac{\nu_\ell(N)}{\ell}\right),
\quad \nu_2(N)=1.$$
Every factor is positive (for odd $\ell$, $\nu_\ell\leq2<\ell$). For $d=210$, this is precisely a wheel admissibility statement. It counts integers $n$ for which no prime factor from the selected wheel divides either member; it does not count prime pairs.

For a finite interval of integers in a fixed residue class modulo $d$, the count differs from its length times the CRT density by at most the number of residue classes, hence at most $d$. This elementary discrepancy is useful for the finite wheel, but after requiring avoidance of all primes up to a growing sieve level $z$, the modulus and remainder terms grow and must be controlled by a sieve theorem. Even a successful upper/lower sieve bracket counts survivors with both members having no small prime factor. It cannot distinguish a prime from a composite with two or more prime factors above $z$; this is the parity obstruction. Chen-type conclusions allow a number with at most two prime factors and do not imply both factors are prime.

## 3. First unavailable arithmetic estimate

The exact target-level theorem that would settle this route is, for some fixed $c>0$ and all sufficiently large even $N\in H$,
$$\sum_{p+q=N\atop p,q\ \mathrm{prime}}\log p\log q\geq cN.$$
The weaker assertion that the sum is positive is exactly binary Goldbach on $H$ (with a positive weight), while this displayed bound is a quantitative strengthening. Sieving residue classes supplies only a positive density of wheel survivors, not this lower bound for simultaneous primality. Bombieri–Vinogradov-type average distribution for one prime variable does not furnish the reflected two-prime correlation at a prescribed $N$; a dispersion argument still needs a remainder estimate that distinguishes primes from the parity-compatible composite survivors.

An anchored four-prime estimate such as a lower bound on
$$\sum_{p+q=N}\sum_{r+s=N+j}W(p,q,r,s)$$
is circular if the proof first selects a pair $(p,q)$ at target $N$. If $R(N)=0$, the outer sum is empty. By contrast, the unrestricted global energy $\sum_t r_w(t)^2$ sums over all targets and is not circular, but its nonnegative average has no supplied mechanism forcing one specified target coefficient to be nonzero.

**Potential circularity and first missing arithmetic fact.** Wheel and CRT admissibility have been proved exactly; simultaneous primality has not. The first missing lemma is a lower bound for the reflected prime correlation itself, or a dispersion estimate with a rigorously positive target-specific main term and an error smaller than that term. Inserting a prime pair at $N$ as an anchor assumes precisely what is being tested.
