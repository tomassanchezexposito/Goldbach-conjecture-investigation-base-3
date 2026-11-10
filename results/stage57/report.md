# Stage 57: shifted four-prime correlations and the pointwise obstruction

**Status:** finite computational observations and proved counting identities; universal coverage remains open.
**Research branch:** `cocalc/stage57-shifted-four-prime-correlations`
**Finite target limit:** 2000
**Shifts:** $h=1,\ldots,10$, with $M=N+2h$

## 1. Research question and evidence labels

The repository's original three-case statement is preserved: each even $N>2$ is to have a prime-plus-one representation, a doubled-prime representation, or a representation by two distinct primes. On

$$H=\{N\ge4:N\text{ is even},\ N-1\text{ is composite},\ N/2\text{ is composite}\},$$

the first two cases are unavailable, so the pointwise obligation is to prove $R(N)>0$, where

$$R(N)=\#\{(p,q):p<q,\ p,q\text{ prime},\ p+q=N\}.$$

Claims in this report are classified as follows:

- **Proved in this research:** the finite combinatorial identities and exact wheel count below.
- **Computational observation:** the exact outputs on the stated finite range, checked by the supplied independent implementations.
- **Refuted:** the named blanket finite-block covariance inequality, and the previously proposed universal strict variance bound, have explicit finite counterexamples.
- **Open proof obligation:** obtain a non-circular analytic estimate strong enough to prove $R(N)>0$ for every $N\in H$.

No asymptotic inference is drawn from the finite computations. No proof of Goldbach's conjecture or universal coverage is claimed.

## 2. Provenance and handoff

The Stage 56 notebook and its companion report were copied byte-for-byte from the completed CoCalc files into `results/stage56/`. Their original copies in the project root remain untouched. The existing `results/stage56_variance_diagnostic.md` and `experiments/stage56_variance_probe.py` were preserved. SHA-256 hashes of the Stage 56 source and imported copies are recorded in `manifest.json`.

Stage 56 used SageMath 10.9 and exact rational arithmetic. Stage 57 is independently reproducible using Python's standard library only; its code uses exact integer and `fractions.Fraction` arithmetic. The parameter and provenance record is `manifest.json`; full per-row exact data is `shifted_correlations.json`.

The earlier notation $C_{210}(N)$ in the diagnostic refers to the number of compatible reduced-residue pairs modulo 210. This report uses $A_{210}(N)$ for that same integer count, following the Stage 56 notebook. The integer normalization is unchanged; the names are made explicit here to avoid conflating a residue-class count with an analytic singular series.

## 3. Exact identities

### 3.1 Wheel factor

For a prime $\ell\in\{2,3,5,7\}$, the number of allowed residues $a\pmod\ell$ for which neither $a$ nor $N-a$ is divisible by $\ell$ is $\ell-1$ if $\ell\mid N$, and $\ell-2$ otherwise. The Chinese remainder theorem therefore gives the exact count

$$A_{210}(N)=\prod_{\ell\in\{2,3,5,7\}}\left(\ell-\nu_\ell(N)\right),\qquad
\nu_\ell(N)=\begin{cases}1,&\ell\mid N,\\2,&\ell\nmid N.\end{cases}$$

This is a finite local admissibility count, not a prime-pair estimate. The implementation checks the product against direct enumeration of all 210 residues for every even target from 4 through 2000 (999 targets). For even $N$, the factor at $\ell=2$ is 1. Define $X_N=R(N)/A_{210}(N)$.

### 3.2 Shifted pair expansion and position classes

Let $M=N+2h$ with $h>0$. Write the two distinct-prime representation sets as

$$\mathcal P_N=\{(p,q):p<q,\ p+q=N\},\qquad
\mathcal P_M=\{(r,s):r<s,\ r+s=M\}.$$

The product $R(N)R(M)$ counts ordered choices of one representation from each target. Its exact partition is

$$R(N)R(M)=S_{LL}^{(h)}(N)+S_{LH}^{(h)}(N)+S_{HL}^{(h)}(N)+S_{HH}^{(h)}(N)+Q_4^{(h)}(N),$$

where

$$S_{LL}=\sum_{(p,q)\in\mathcal P_N}\sum_{(r,s)\in\mathcal P_M}\mathbf1_{p=r},\quad
S_{LH}=\sum\mathbf1_{p=s},\quad
S_{HL}=\sum\mathbf1_{q=r},\quad
S_{HH}=\sum\mathbf1_{q=s},$$

and $Q_4$ counts those terms with $p,q,r,s$ pairwise distinct. The sums in the middle definitions run over $\mathcal P_N\times\mathcal P_M$. For $h>0$, two shared prime values would force the same unordered pair and hence equal target sums, which is impossible. Thus these five classes are disjoint and exhaustive. In the order convention $p<q$, $r<s$ and $M>N$, the $LH$ class is always empty; it is retained as a named position class so the expansion is explicit and the code checks it. The $HL$ class can occur when the target halves are sufficiently separated.

After normalization this becomes the identity

$$X_NX_M=\frac{S_{LL}^{(h)}(N)+S_{LH}^{(h)}(N)+S_{HL}^{(h)}(N)+S_{HH}^{(h)}(N)+Q_4^{(h)}(N)}{A_{210}(N)A_{210}(M)}.$$

These shared-position terms are sometimes called contraction or shared-summand terms. There is no identical-representation diagonal across distinct target sums. For comparison, at zero shift the identical-pair diagonal has size $R(N)$, and the off-diagonal has size $R(N)(R(N)-1)$; any two representations at the same target sharing a prime must be identical. This zero-shift identity is not used to infer shifted estimates.

## 4. Computation and independent verification

The anchor domain is every $N\in H$ with $4\le N\le2000$ and $N+2h\le2000$. The shifted target $M$ is not required to lie in $H; counts with both targets in $H$ are separately tabulated. There are 564 residual anchors through 2000 and no zero $R(N)$ values on that finite set. The experiment contains 5,616 anchor-shift rows.

Two methods were compared pointwise:

1. **Trial-division pair-list method.** For each target, enumerate all $p<q$ and test both candidates by exact trial division. Form the Cartesian product of the two explicit representation lists and classify each ordered pair by the four possible shared positions or by four distinct primes.
2. **Sieve/direct-scan method.** Build a Sieve of Eratosthenes prime table, then use direct nested scans over lower summands $p$ and $r$; derive $q=N-p$ and $s=M-r$, check prime flags, and classify equality positions without calling the pair-list correlation routine.

Every per-row category count and total agrees between the methods. A separate `verify_stage57.py` pass independently reads the saved JSON, rebuilds the sieve and direct residue enumeration, and rechecks all 5,616 rows, all category totals and all shift aggregates. All arithmetic and stored normalized values are exact rational values.

| $h$ | Anchors $N\in H$ | Both $N,M\in H$ | $S_{LL}$ total | $S_{LH}$ | $S_{HL}$ | $S_{HH}$ | $Q_4$ | $\sum_N X_NX_{N+2h}$ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 564 | 285 | 3,123 | 0 | 0 | 4,417 | 489,185 | $1273687/1200$ |
| 2 | 564 | 318 | 2,815 | 0 | 0 | 3,761 | 462,300 | $11582399/10800$ |
| 3 | 563 | 313 | 6,307 | 0 | 15 | 7,812 | 550,151 | $1556143/1440$ |
| 4 | 563 | 317 | 3,647 | 0 | 22 | 4,385 | 495,302 | $3887947/3600$ |
| 5 | 562 | 312 | 3,603 | 0 | 15 | 4,576 | 455,723 | $23105873/21600$ |
| 6 | 561 | 353 | 5,914 | 0 | 49 | 7,283 | 539,656 | $23263231/21600$ |
| 7 | 561 | 314 | 4,232 | 0 | 52 | 5,507 | 508,286 | $13863479/12960$ |
| 8 | 560 | 318 | 2,349 | 0 | 35 | 3,410 | 440,580 | $5735659/5400$ |
| 9 | 559 | 301 | 5,777 | 0 | 88 | 7,191 | 535,536 | $11581633/10800$ |
| 10 | 559 | 338 | 4,964 | 0 | 91 | 5,516 | 512,203 | $23076053/21600$ |

Across all shifts, the ordered representation-pair total is 5,085,878: 4,988,922 four-distinct terms and 96,956 shared-prime terms. The exact row-level data include each $R(N)$, $R(M)$, both wheel denominators, the five category counts, each normalized category, and the normalized shifted product. The shift sums are over anchors; they are not averages or asymptotic constants. Divide by the anchor count to obtain the corresponding finite mean; those exact means are also in the JSON file.

## 5. Counterexample search for stronger inequalities

### 5.1 Shifted covariance factorization heuristic

We tested the proposed stronger block inequality

$$\frac1k\sum_{N\in B}X_NX_{N+2h}\ \ge\
\left(\frac1k\sum_{N\in B}X_N\right)
\left(\frac1k\sum_{N\in B}X_{N+2h}\right),$$

where $B$ consists of residual anchors in an inclusive even-integer interval $[L,L+100]$ and every shifted target is at most 2000. This is a positive-covariance heuristic, not a consequence of the correlation identity. We checked all 9,490 such windows with at least two anchors for $h=1,\ldots,10$. The inequality fails in 3,762 windows and is therefore **refuted as a universal block inequality**. For example, at $h=1$, $[262,362]$ has 25 anchors and

$$\operatorname{Cov}(X_N,X_{N+2})=-\frac{127}{3000000},\qquad
\frac1k\sum X_NX_{N+2}=\frac{4859}{15000}
<\frac{971927}{3000000}=\left(\frac1k\sum X_N\right)\left(\frac1k\sum X_{N+2}\right).$$

On the full anchor set through 2000, this covariance inequality happens to pass for each of the ten shifts. That finite observation is not a theorem and cannot be substituted for a pointwise lower bound. Even a positive average shifted correlation does not rule out an isolated zero; the left side contains $R(N)$ itself and is not independent analytic information about it.

### 5.2 Stage 56 variance criterion

The Stage 56 elementary implication remains valid: for $k$ nonnegative values, if one is zero then the centered sum of squares obeys $V\ge k\mu^2/(k-1)$. Thus $V<k\mu^2/(k-1)$ suffices to exclude a zero in that finite block. The bound is not necessary for coverage and fails in blocks that have no zero. The prior exact scan's explicit counterexample is the 51-even-integer interval $[50,150]$, with $k=21$, no zero counts, and exact ratio

$$\frac{V}{k\mu^2/(k-1)}=\frac{1716160}{1568187}>1.$$

It is therefore refuted as a universal bound one could simply assume on all blocks. The original Stage 56 report retains the five block moments and scan details.

## 6. Analytic limitation and unresolved proof obligation

No independent analytic bound for an individual $R(N)$ was obtained. In particular, the wheel factor is only local admissibility, while the shifted expansion is an identity whose terms are built from the same prime-pair counts; neither supplies a non-circular positive lower bound.

A sufficient missing result would be an explicit theorem giving, for every even $N\ge N_0$ in $H$, a lower estimate

$$R(N)\ge L(N)-E(N)>0,$$

with $L(N)$, $E(N)$, all hypotheses, and the inequality verified uniformly on that domain, plus an exact finite verification for residual $N<N_0$. This project has not established such functions, constants, or hypotheses. Any proposed circle-method, sieve, or correlation estimate must supply an error term strong enough to keep this lower bound positive at every target; a mean estimate or an identity involving $R(N)$ does not meet that requirement. Consequently, the all-$N$ pointwise assertion on $H$ remains an **open proof obligation** in this research, and no claim about proving Goldbach is made.

## 7. Reproduction

From the repository root, using Python 3 and no additional packages:

```bash
python results/stage57/compute_stage57.py
python results/stage57/verify_stage57.py
```

The first command regenerates `shifted_correlations.json`; the second independently checks the saved data. Exact parameters, runtime version, input file hashes, and generated file hashes are in `manifest.json`.
