# Stage 58: audit of a non-circular pointwise positivity certificate

**Status:** open analytic proof obligation; no universal coverage theorem is proved.
**Branch:** `cocalc/stage58-pointwise-analytic-certificate`
**Target:** for every residual even integer $N$, prove $R(N)>0$ without assuming a prime pair at $N$.
**Reproduction:** `python results/stage58/verify_stage58.py` (Python 3 standard library only).

## 1. Scope, provenance, and evidence labels

The task follows the Stage 56 exact moment experiment and the Stage 57 exact shifted four-prime correlations. The Stage 56/57 files are retained unchanged. Stage 58 tests the logical and analytic requirements of pointwise certificates; it deliberately does not run another large Goldbach enumeration.

The original three-case statement and residual set are unchanged. For even $N>2$, the first two cases are $N=p+1$ and $N=2p$. Define

$$H=\{N\in\mathbb Z:N\ge4,\ N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\}.$$

For $N\in H$, those first two cases are unavailable, and the remaining obligation is

$$R(N)=\#\{(p,q):p<q,\ p,q\text{ prime},\ p+q=N\}>0.$$

The equidistant-doubles condition in the original third case is algebraically equivalent to $p+q=N$; it supplies no primality information. The labels in this report follow `docs/research_protocol.md`:

- **Proved in this research:** the Fourier coefficient identity, diagonal removal, wheel residue formula, and deterministic moment implication below.
- **Computational observation:** the exact outputs of the targeted checks listed in Section 7.
- **Refuted:** inference of pointwise positivity from positive means or positive shifted mean products alone; a universal application of the Stage 56 variance threshold to every block is also refuted by a finite block with no zero.
- **Open proof obligation:** supply explicit uniform analytic estimates with strict pointwise dominance, or another independent pointwise certificate, for every $N\in H$ above an effective cutoff and verify the remaining finite set.
- **Established theorem (background):** Chen's theorem gives a prime plus an almost-prime with at most two prime factors for every sufficiently large even integer. It does not assert that the second summand is prime; see Section 6.

No result here proves Goldbach's conjecture or the project's universal coverage statement.

## 2. Vacuity and the average-to-pointwise obstruction

Let $x_N=R(N)/A_{210}(N)$, where $A_{210}(N)>0$ is defined in Section 5. All $x_N$ are nonnegative, and $x_N>0$ is equivalent to $R(N)>0$.

A theorem giving $x_Nx_{N+2h}\ge c_N>0$ independently for a target $N$ would be a valid, stronger route: nonnegativity implies both factors are positive. Such a theorem is not inherently circular. It becomes circular if its derivation assumes $x_N>0$, divides by $x_N$, or imports the existence of a target representation to establish the product bound. In that case the purported certificate already uses the conclusion it is meant to prove.

Even exact positive averages of shifted products do not give pointwise positivity. A concrete countermodel is the cyclic length-10 vector

$$x=(0,1,1,1,1,1,1,1,1,1).$$

Its mean is $9/10$. For every nonzero cyclic shift $h\pmod {10}$, its mean shifted product is $4/5>0$, while the product of the means is $81/100$ and the covariance is $-1/100$. Thus all these averages are positive although $x_0=0$. This is a countermodel to the logical inference from averaged positivity; it is not a model of prime counts. The verifier records every shift exactly.

Consequently, Stage 57's shifted correlation identity cannot establish coverage by itself. A uniform positive *pointwise* lower bound on a product could establish it, but obtaining that bound without already knowing the target factor is positive is precisely the missing work.

## 3. Exact prime-only Fourier coefficient

Write $e(t)=\exp(2\pi i t)$ and, for each integer $N\ge4$, define on $\mathbb R/\mathbb Z$

$$S_N(\alpha)=\sum_{\substack{p\le N\\p\text{ prime}}}(\log p)e(p\alpha).$$

Orthogonality of the integer characters gives the exact identity

$$T(N):=\int_0^1 S_N(\alpha)^2e(-N\alpha)\,d\alpha
=\sum_{\substack{p,q\le N\\p,q\text{ prime}\\p+q=N}}\log p\log q.$$

The sum on the right is ordered and includes the diagonal. Let

$$D(N)=\mathbf 1_{N/2\text{ prime}}\bigl(\log(N/2)\bigr)^2.$$

Pairing the two orders for each distinct-prime pair yields

$$T(N)-D(N)=2\sum_{\substack{p<q\\p+q=N\\p,q\text{ prime}}}\log p\log q.$$

Every weight is strictly positive. Hence $T(N)-D(N)>0$ if and only if $R(N)>0$. Also

$$R(N)\ge \frac{T(N)-D(N)}{2(\log N)^2}$$

whenever the numerator is positive, since each $\log p\log q\le(\log N)^2$. On $H$, $N/2$ is composite, so $D(N)=0$. This removes the diagonal exactly for the target set; for general even $N$, it must be subtracted. The identity is a reformulation, not an estimate.

## 4. Explicit circle-method certificate and the missing estimates

Here is one precise major/minor arc formulation. Fix an integer $B\ge1$. For sufficiently large $N$, put $Q_N=\lfloor(\log N)^B\rfloor$ and define

$$\mathfrak M_B(N)=\bigcup_{1\le q\le Q_N}\ \bigcup_{\substack{0\le a<q\\(a,q)=1}}
\left\{\alpha\in\mathbb R/\mathbb Z:
\left\|\alpha-\frac aq\right\|\le\frac{(\log N)^B}{N}\right\},\qquad
\mathfrak m_B(N)=(\mathbb R/\mathbb Z)\setminus\mathfrak M_B(N),$$

where $a=0,q=1$ is included and $\|\cdot\|$ is distance to the nearest integer. Overlaps, if any, are interpreted as a union. Let

$$J_E(N)=\operatorname{Re}\int_E S_N(\alpha)^2e(-N\alpha)\,d\alpha.$$

The complete major and minor integrals sum to the exact real coefficient: $T(N)=J_{\mathfrak M_B}(N)+J_{\mathfrak m_B}(N)$.

The expected full local main term for the logarithmically weighted ordered coefficient is $N\mathfrak S(N)$, where for even $N$

$$\mathfrak S(N)=2C_2\prod_{\substack{\ell\mid N\\\ell>2}}\frac{\ell-1}{\ell-2},\qquad
C_2=\prod_{\ell>2\text{ prime}}\left(1-\frac1{(\ell-1)^2}\right).$$

A sufficient, fully quantified analytic input would be explicit constants $N_0\ge4$, $C_M,C_m>0$, exponents $A_M,A_m\ge0$, and $0<\delta_M,\delta_m\le1$, such that for every even $N\ge N_0$ the following hold:

$$J_{\mathfrak M_B}(N)\ge N\mathfrak S(N)-C_MN^{1-\delta_M}(\log N)^{A_M},$$

$$|J_{\mathfrak m_B}(N)|\le C_mN^{1-\delta_m}(\log N)^{A_m}.$$

These error terms must include all truncation and approximation errors, and all constants and hypotheses must be explicit. Because $\mathfrak S(N)\ge 2C_2>0$ for even $N$, strict dominance

$$2C_2N>C_MN^{1-\delta_M}(\log N)^{A_M}
+C_mN^{1-\delta_m}(\log N)^{A_m}+D(N)$$

would imply $T(N)-D(N)>0$, hence $R(N)>0$. On $H$, $D(N)=0$. If such estimates and constants were established, an effective cutoff could be chosen and the finite residual range below it checked separately.

**Open:** this project has not proved these major-arc and minor-arc inequalities, supplied their constants, or shown that a chosen $B$ and arc family give them. In particular, a uniform minor-arc bound of power-saving size strong enough to be dominated by the positive main term is not available in this research. An asymptotic prediction, a heuristic singular series, a mean estimate, or a major-arc computation alone is not a substitute. The proposed pair of inequalities would settle the binary prime-pair positivity for every sufficiently large even target, so the missing estimate is of Goldbach-level strength. It is not made easier by restricting to $H$ in any argument presently established here.

## 5. Wheel congruences and exceptional primes

For $\ell\in\{2,3,5,7\}$, count residues $a\pmod\ell$ for which neither $a$ nor $N-a$ is divisible by $\ell$. There is one forbidden residue when $\ell\mid N$ (the two forbidden residues coincide), and two distinct forbidden residues otherwise. The Chinese remainder theorem proves

$$A_{210}(N)=\prod_{\ell\in\{2,3,5,7\}}(\ell-\nu_\ell(N)),\qquad
\nu_\ell(N)=\begin{cases}1,&\ell\mid N,\\2,&\ell\nmid N.\end{cases}$$

For even $N$, the modulo-2 factor is exactly $1$. There are $\varphi(210)=48$ reduced residues, so the exact wheel-truncated normalized factor is

$$\mathfrak S_{210}(N)=\frac{A_{210}(N)/210}{(48/210)^2}=\frac{210A_{210}(N)}{48^2}.$$

In older project notes the integer residue count is sometimes named $C_{210}(N)$; in Stages 56/57 and this report it is $A_{210}(N)$. These names denote the same finite integer count, not the normalized factor $\mathfrak S_{210}(N)$ and not the full singular series.

The local normalized factor at a prime $\ell$ is the allowed residue density divided by the square of the one-prime reduced-residue density. For even $N$, the factor at $2$ is $2$, and for odd primes it is

$$\begin{cases}\ell/(\ell-1),&\ell\mid N,\\
\ell(\ell-2)/(\ell-1)^2,&\ell\nmid N.\end{cases}$$

The factor at $3$ is therefore $3/2$ if $3\mid N$ and $3/4$ otherwise; modulo 210 its allowed-residue count is respectively 2 or 1. The full product over odd primes, with the modulo-2 factor, yields $\mathfrak S(N)$ above. The finite wheel gives no control over the omitted primes $\ell>7$, the minor arcs, or the pointwise error. The actual primes $2$ and $3$ also occur as exceptional individual summands not represented by an asymptotic reduced-residue model; the exact Fourier coefficient includes them, and the diagonal at $2$ is handled by $D(N)$. On $H$, $N/2$ is not prime, so this diagonal is absent.

## 6. Sieve comparison and parity limitation

Chen's theorem states that every sufficiently large even integer is a sum of a prime and an integer with at most two prime factors (with the usual almost-prime convention, including multiplicity). This is a major theorem, but its second summand need not be prime. It therefore does not prove $R(N)>0$ for a given residual $N$. A semiprime survivor cannot silently be relabelled as a prime.

The sieve parity problem describes a limitation of broad classes of sieve weights: such weights generally cannot distinguish prime numbers from integers with the wrong parity of the number of prime factors at the strength needed to isolate primes. This explains why sieve lower bounds for a prime plus an almost-prime do not automatically become prime plus prime. It is a methodological barrier, not a theorem that no analytic approach can prove Goldbach, and no impossibility claim is made here. The residual conditions $N-1$ composite and $N/2$ composite do not remove that parity issue in any proof established in this project.

## 7. Alternative non-circular criterion, audit, and exact checks

### Independent block-moment certificate

For a finite block $B\subset H$ of size $k\ge2$, set

$$x_N=\frac{R(N)}{A_{210}(N)},\qquad
\mu_B=\frac1k\sum_{N\in B}x_N,\qquad
M_{2,B}=\frac1k\sum_{N\in B}x_N^2.$$

If one $x_N$ is zero, Cauchy--Schwarz on the other at most $k-1$ entries gives

$$\sum_{N\in B}x_N^2\ge\frac{(\sum_{N\in B}x_N)^2}{k-1}
=\frac{k^2\mu_B^2}{k-1},\quad\text{so}\quad
M_{2,B}\ge\frac{k}{k-1}\mu_B^2.$$

Thus independently proved bounds $\mu_B\ge m_B>0$ and $M_{2,B}\le u_B<\frac{k}{k-1}m_B^2$ imply every $R(N)>0$ in $B$. This is a genuinely non-circular conditional criterion only when both moment estimates are proved without assuming any target representation. The audit found no such uniform bounds. Computing the moments from the exact $R(N)$ values is a verification after the fact, not an analytic certificate; the second moment contains the unresolved four-prime correlation.

### Approaches that fail to give a universal certificate

1. **Positive means or shifted means:** refuted as a pointwise inference by the length-10 vector in Section 2.
2. **Assuming a universal strict Stage 56 variance threshold:** refuted as a universal bound by the exact block $[50,150]$ below. The deterministic implication remains valid whenever its strict hypothesis is independently established; failure of the threshold is inconclusive.
3. **Assuming nonnegative covariance/factorization for shifted products:** refuted by the Stage 57 window $[262,362]$, $h=1$, rechecked below.
4. **Taking the Fourier identity or wheel factor as an estimate:** invalid; neither bounds the minor arcs or proves a positive pointwise margin.
5. **Promoting Chen's almost-prime summand:** invalid without an additional argument forcing that summand to be prime.

### Reproducible targeted computations

`verify_stage58.py` uses only Python's standard library and exact integers / `fractions.Fraction`. It independently checks the wheel formula against all 210 residue classes for 249 even targets from 4 through 500; checks ordered-pair diagonal bookkeeping using trial division versus a sieve for 149 even targets from 4 through 300; exhaustively checks the finite-vector moment implication on 5,456 vectors of lengths 2 through 6 with entries in $\{0,1,2,3\}$; and recomputes two specific finite counterexamples with a fresh sieve and direct pair scans. These are lemma checks and counterexample audits, not universal prime-pair searches.

Exact results:

- The Stage 56 block $B=H\cap[50,150]$ has $k=21$, no zero representation counts, $V_B=5363/56700$, threshold $T_B=58081/672000$, and

  $$V_B/T_B=1716160/1568187>1.$$

  This refutes the proposal that the strict threshold automatically holds on every block; it does not refute the valid sufficient implication.
- For residual anchors in $[262,362]$ and shift $h=1$, there are 25 anchors. The independently recomputed mean shifted product is $4859/15000$ and the product of means is $971927/3000000$, so the covariance is

  $$-127/3000000<0.$$

  This refutes universal nonnegative covariance for these shifted normalized counts.
- The cyclic toy vector has mean $9/10$ and mean shifted product $4/5$ for every nonzero shift, while containing a zero coordinate.
- Every targeted assertion passes. The exact output is saved in `verification.json`.

The source and output do not establish any assertion outside their stated finite domains. The integer pair checks validate the diagonal convention in the coefficient identity; the proof for all $N$ is the character-orthogonality argument in Section 3.

## 8. Proof obligations and next objective

The following remain open in this project:

1. Prove a major-arc lower estimate with explicit constants that captures the full singular-series main term, including truncation errors.
2. Prove a uniform minor-arc upper bound strong enough for strict pointwise dominance for every sufficiently large even $N$ (or at least every sufficiently large $N\in H$).
3. Supply an explicit effective threshold and verify all residual targets below it exactly.
4. Alternatively, produce independent lower and upper block-moment estimates meeting the strict criterion for a covering family of blocks, with no use of target-pair existence.
5. Audit any new argument for diagonal terms, local factors at 2 and 3, singular-series tails, and hidden pointwise assumptions.

The next mathematically meaningful objective is to specify and prove the strongest available unconditional minor-arc estimate for the prime-only coefficient under an explicit arc decomposition, then compare its error scale against $N\mathfrak S(N)$ and the exact diagonal. If it does not give strict dominance, record the first term that fails and seek a genuinely stronger pointwise input; do not replace the target by an average theorem.

## 9. References

1. G. H. Hardy and J. E. Littlewood, “Some problems of ‘Partitio numerorum’; III: On the expression of a number as a sum of primes,” *Acta Mathematica* **44** (1923), 1–70. The Goldbach singular series is a conjectural main-term framework in this work, not an unconditional binary Goldbach theorem.
2. J. R. Chen, “On the representation of a large even integer as the sum of a prime and the product of at most two primes,” *Scientia Sinica* **16** (1973), 157–176. Cited for the prime-plus-almost-prime theorem, not for a prime-plus-prime conclusion.
3. H. Halberstam and H.-E. Richert, *Sieve Methods*, London Mathematical Society Monographs, no. 4, Academic Press, 1974. Background on sieve methods and their limitations.
4. H. Iwaniec and E. Kowalski, *Analytic Number Theory*, American Mathematical Society Colloquium Publications, vol. 53, 2004. Background on the circle method, exponential sums, and sieve methods.

These works are background references. No external theorem beyond the specific Chen statement above is invoked to claim universal positivity.
