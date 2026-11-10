# Stage 58 supplement: sharp moments and shifted four-prime positions

**Status:** elementary moment and correlation identities are proved below. The finite calculations are exact observations on the stated ranges. Universal positivity on the residual set remains open.

This supplement extends [`report.md`](report.md), which records the prime-only Fourier coefficient, the conditional circle-method certificate, and the analytic obstruction. It preserves that report and the earlier Stage 56 and Stage 57 files.

## Definitions and normalization

The residual set and distinct-pair count are

$$H=\{N\ge4:N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\},\qquad
R(N)=\#\{(p,q):p<q,\ p,q\text{ prime},\ p+q=N\}.$$

For $\ell\in\{2,3,5,7\}$, put $\nu_\ell(N)=1$ if $\ell\mid N$ and $2$ otherwise. The exact number of compatible residue classes with neither summand divisible by $\ell$ is $\ell-\nu_\ell(N)$. The Chinese remainder theorem gives

$$A_{210}(N)=\prod_{\ell\in\{2,3,5,7\}}(\ell-\nu_\ell(N)),\qquad
X_N=\frac{R(N)}{A_{210}(N)}.$$

For even $N$, the factor at $2$ is $1$. At $3$, the factor is $2$ when $3\mid N$ and $1$ otherwise; at $5$ and $7$ it is respectively $4$ or $3$, and $6$ or $5$. In particular, $A_{210}(4)=15$, $A_{210}(6)=30$, $A_{210}(10)=20$, $A_{210}(30)=40$, and $A_{210}(42)=36$. This is a residue count, not a primality estimate or the full singular series.

Every distinct-prime representation of an even target consists of two odd primes: a summand $2$ would leave an odd other summand, while $2+2$ is excluded by $p<q$. The primes $3,5,7$ can still occur. Thus a four-position configuration with all four primes greater than $7$ lies in reduced residue classes modulo $210$ and obeys

$$p+q\equiv N\pmod{210},\qquad r+s\equiv N+2h\pmod{210}.$$

Configurations containing $3,5,$ or $7$ are exact exceptional terms and are recorded separately. The normalization by $A_{210}$ does not remove these terms from $R(N)$.

## Sharp finite-dimensional second-moment obstruction

Let $x_1,\ldots,x_k\ge0$, with $k\ge2$, and set

$$\mu=\frac1k\sum_{i=1}^k x_i,\qquad M_2=\frac1k\sum_{i=1}^k x_i^2,
\qquad V=\sum_{i=1}^k(x_i-\mu)^2=k(M_2-\mu^2).$$

If a specified set $Z$ of $m<k$ coordinates is zero, Cauchy--Schwarz on the other $k-m$ entries gives the sharp bound

$$\sum_i x_i^2\ge \frac{(\sum_i x_i)^2}{k-m},\qquad
M_2\ge\frac{k}{k-m}\mu^2,\qquad
V\ge\frac{km}{k-m}\mu^2.$$

Equality is attained when all $k-m$ remaining coordinates are equal. In particular, one zero forces $M_2\ge k\mu^2/(k-1)$ and $V\ge k\mu^2/(k-1)$. Therefore $\mu>0$ and $V<k\mu^2/(k-1)$ imply that every coordinate is positive. Applied to $x_N=R(N)/A_{210}(N)$ on a finite block $B\subset H$, this is a valid sufficient certificate if its moment hypotheses are established independently of the target representation counts.

There is a sharp weighted version. Let $w_i>0$, $\sum_iw_i=1$, and define $\mu_w=\sum_iw_ix_i$, $M_{2,w}=\sum_iw_ix_i^2$. If $x_j=0$, then

$$\mu_w^2=\left(\sum_{i\ne j}w_ix_i\right)^2
\le (1-w_j)\sum_{i\ne j}w_ix_i^2=(1-w_j)M_{2,w},$$

so $M_{2,w}\ge\mu_w^2/(1-w_j)$. Equality holds when all $x_i$ for $i\ne j$ are equal. To exclude a zero at any coordinate using only these two weighted moments, the sharp uniform condition is

$$M_{2,w}<\frac{\mu_w^2}{1-w_{\min}},\qquad w_{\min}=\min_iw_i.$$

Since $w_{\min}\le1/k$, this worst-coordinate threshold is at most $k\mu_w^2/(k-1)$; equal weights maximize it. Thus reweighting alone cannot strengthen the two-moment obstruction for an unknown zero coordinate. Extra arithmetic information could still support a different estimate.

**Proof.** The unweighted claims are Cauchy--Schwarz applied to the $k-m$ potentially nonzero terms, followed by $V=\sum x_i^2-k\mu^2$. The weighted inequality is Cauchy--Schwarz with factors $\sqrt{w_i}$ and $\sqrt{w_i}x_i$ over $i\ne j$. The equality conditions follow from equality in Cauchy--Schwarz. For an unknown zero coordinate, the smallest of the lower bounds $\mu_w^2/(1-w_j)$ occurs when $w_j=w_{\min}$; the arithmetic mean of the weights gives $w_{\min}\le1/k$. This proves sharpness and the comparison with uniform weights. $\square$

The Stage 56 proposed strict variance condition is not a universal property of these prime counts. On $B=H\cap[50,150]$, the exact computation gives $k=21$, no zero count, $\mu=241/840$, and

$$V=\frac{5363}{56700},\qquad \frac{k}{k-1}\mu^2=\frac{58081}{672000},\qquad
\frac{V}{k\mu^2/(k-1)}=\frac{1716160}{1568187}>1.$$

This refutes the proposal that the strict condition holds automatically on every block. It does not refute the proved implication from the condition to positivity.

## Shifted four-prime expansion

Write $M=N+2h$ with $h>0$, and

$$\mathcal P_N=\{(p,q):p<q,\ p,q\text{ prime},\ p+q=N\},\qquad
\mathcal P_M=\{(r,s):r<s,\ r,s\text{ prime},\ r+s=M\}.$$

Then $R(N)R(M)$ counts ordered choices in $\mathcal P_N\times\mathcal P_M$. Partition these choices by the position equalities $p=r$, $p=s$, $q=r$, $q=s$, or by no equality. Let their counts be $S_{LL},S_{LH},S_{HL},S_{HH},Q_4$, respectively. Two equalities would force both prime values, hence equal target sums, impossible for $h>0$. The classes are disjoint and exhaustive, and

$$R(N)R(N+2h)=S_{LL}+S_{LH}+S_{HL}+S_{HH}+Q_4.$$

The four shared-position counts have these exact descriptions:

$$\begin{aligned}
S_{LL}&=\#\{(p,q)\in\mathcal P_N:q+2h\text{ prime}\},\\
S_{LH}&=0,\\
S_{HL}&=\#\{p<q<p+2h:p,q,p+2h\text{ prime},\ p+q=N\},\\
S_{HH}&=\#\{(p,q)\in\mathcal P_N:p+2h\text{ prime},\ p+2h<q\}.
\end{aligned}$$

For $S_{LL}$, the second pair is $(p,q+2h)$. For $S_{HL}$ it is $(q,p+2h)$, which requires $q<p+2h$. For $S_{HH}$ it is $(p+2h,q)$, which requires $p+2h<q$. In the remaining nominal case $p=s$, the inequalities imply $p<N/2$ from $p<q=N-p$ and $p>M/2$ from $r=M-p<p$, a contradiction because $M>N$. Hence $S_{LH}=0$.

The four-distinct term $Q_4$ is an ordered prime quadruple count with $p+q=N$, $r+s=N+2h$, low/high ordering in each pair, and pairwise distinct prime values. Its reduced-residue subcount (all positions $>7$) satisfies the two displayed congruences modulo $210$; the complementary subcount contains at least one of $3,5,7$. Neither a congruence-compatible residue quadruple nor a four-prime identity estimates the number of such prime quadruples at an individual target.

At zero shift the position pattern changes. In $\mathcal P_N^2$, identical representations contribute the diagonal $R(N)$. If two representations share one prime, their other summands are forced equal, so they are identical; there is no exactly-one-shared-prime class. All other ordered pairs have four distinct primes, giving the exact identity

$$R(N)^2=R(N)+R(N)(R(N)-1).$$

For the ordered Fourier sum which includes $p=q$, the count is $2R(N)+\mathbf1_{N/2\text{ prime}}$. The diagonal therefore vanishes on $H$, but is retained in the general identity.

## Exact finite computation and independent checks

`compute_second_moment.sage.py` uses SageMath 10.9 primality and `QQ` rational arithmetic. It builds explicit low/high representation lists, forms their Cartesian products, and separately scans candidate low positions $p,r$ for each shifted target pair. `verify_second_moment.py` independently uses a standard-library Eratosthenes sieve and `fractions.Fraction`; it checks the saved rows by both a pair-list product and a direct nested candidate scan. The comparison checks every category row by row. The scripts also check the wheel formula by enumerating all 210 residues and recompute the exact block moments.

Parameters were $N\le300$ for same-target checks, $N\in H$ with $4\le N\le300$ for shifted anchors, $h=1,\ldots,10$, and $M\le320$. The wheel check covered all 249 even targets from 4 through 500. The finite residual search found 62 targets and no zero representation count. This is a bounded observation only.

| $h$ | $S_{LL}$ | $S_{LH}$ | $S_{HL}$ | $S_{HH}$ | $Q_4$ | $Q_4$ with a prime $\le7$ | $Q_4$ all primes $>7$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 171 | 0 | 0 | 213 | 4,186 | 867 | 3,319 |
| 2 | 108 | 0 | 0 | 171 | 4,054 | 876 | 3,178 |
| 3 | 270 | 0 | 5 | 329 | 4,376 | 897 | 3,479 |
| 4 | 147 | 0 | 10 | 209 | 4,503 | 1,077 | 3,426 |
| 5 | 142 | 0 | 3 | 181 | 4,090 | 1,031 | 3,059 |
| 6 | 253 | 0 | 17 | 287 | 4,432 | 993 | 3,439 |
| 7 | 198 | 0 | 18 | 229 | 4,856 | 1,123 | 3,733 |
| 8 | 107 | 0 | 6 | 138 | 3,989 | 975 | 3,014 |
| 9 | 265 | 0 | 22 | 256 | 4,499 | 1,025 | 3,474 |
| 10 | 179 | 0 | 28 | 216 | 4,939 | 1,119 | 3,820 |

Each row aggregates the same 62 residual anchors and sums raw configuration counts, not normalized correlations. Across all positive shifts there are 620 checked rows. The scripts record every row, the wheel denominators, normalized shifted products, and exact moment values in `second_moment_exact.json`; the independent verification summary is `second_moment_verification.json`.

For $B=H\cap[50,200]$, the new calculation reproduces $k=33$, $\mu=3991/11880$, $M_2=34559/285120$, and $V=18416/66825$. The ratio of $V$ to the one-zero threshold is $37715968/15928081>1$, while the block has no zero. For $H\cap[202,300]$, the computed ratio is $58749984/84695209<1$ and no zero occurs in this finite block. These exact outputs verify data and illustrate that a passing finite criterion certifies this block only; they do not provide a theorem for later blocks.

## What is established and what remains open

**Proved here:** the unweighted and weighted sharp zero-coordinate inequalities; the optimality of uniform weights for a worst-coordinate certificate using only the first two moments; the same-target diagonal/off-diagonal identities; the shifted five-class decomposition and its shared-position formulas; the wheel residue count and the small-prime exceptions.

**Refuted:** the blanket assertion that the Stage 56 variance threshold holds on every finite residual block, by the exact block $[50,150]$. The general inference that positive shifted averages or positive-semidefinite covariance constraints alone force all coordinates positive also fails: the length-10 cyclic vector $(0,1,\ldots,1)$ has mean $9/10$, every nonzero shifted product mean $4/5$, and covariance matrix with diagonal $9/100$ and off-diagonal $-1/100$. Its eigenvalues are $0$ and $1/10$ (the latter with multiplicity 9), so the covariance matrix is positive semidefinite despite the zero coordinate. This vector is a logical countermodel, not a prime-count model.

**Open:** no bound for the four-distinct prime quadruple contribution or for the pointwise second moment has been proved uniformly in $N$. A universal proof would require, for example, independent lower and upper block-moment estimates meeting the strict certificate on a covering family, or a non-circular pointwise estimate $R(N)\ge L(N)-E(N)>0$ for every sufficiently large $N\in H$, plus exact verification below an effective cutoff. The full singular series, minor-arc error, four-prime correlations, and exceptional terms must be controlled at the individual target. The finite wheel, exact identities, and favorable finite averages do not supply these estimates. The project does not prove Goldbach or universal coverage of $H$.

## Reproduction

From the repository root:

```bash
sage -python results/stage58/compute_second_moment.sage.py
python results/stage58/verify_second_moment.py
python results/stage58/verify_stage58.py
python results/stage57/verify_stage57.py
python -m unittest discover -s tests -v
```

The first script rewrites only `second_moment_exact.json`; the independent verifier rewrites only `second_moment_verification.json`. The additional existing checks validate earlier Stage 57/58 results. All observed data are finite; the proofs above do not depend on the computations.
