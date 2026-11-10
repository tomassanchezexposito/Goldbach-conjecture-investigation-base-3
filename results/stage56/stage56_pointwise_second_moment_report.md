# Stage 56: Pointwise second moments for residual even integers

**Date:** 2026-11-10  
**Environment:** SageMath 10.9, CoCalc SageMath Jupyter kernel  
**Notebook:** `stage56_pointwise_second_moment.ipynb`

## Scope and definitions

The residual set is

$$H=\{N\in\mathbb Z: N\ge4,\ N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\}.$$

For each even $N$, let

$$R(N)=\#\{(p,q):p<q,\ p,q\text{ prime},\ p+q=N\}.$$

The notebook enumerates each unordered distinct-prime pair exactly once and excludes the diagonal case $p=q$. The residual condition is checked with exact Sage primality tests.

The existing notebook `wheel210_baseline.ipynb.ipynb` was inspected before work began. It contains environment checks and a preliminary exact-rational experiment on blocks 50–100 and 50–200. That file was left unchanged. SageMath 10.9 and its SageMath Jupyter kernel were already installed; no software was installed.

## Exact wheel-210 factor

For each prime $\ell\in\{2,3,5,7\}$, the number $\nu_\ell(N)$ of forbidden residues for the two prime summands is 1 if $\ell\mid N$ and 2 otherwise. The Chinese remainder theorem gives the exact admissible residue-class count

$$A_{210}(N)=\prod_{\ell\in\{2,3,5,7\}}(\ell-\nu_\ell(N)).$$

This product was checked against a direct enumeration of all 210 residue classes. With $\varphi(210)=48$, the associated truncated singular factor is

$$\mathfrak S_{210}(N)=\frac{A_{210}(N)/210}{(48/210)^2}=\frac{210A_{210}(N)}{48^2}.$$

Some exact values are:

| $N$ | $A_{210}(N)$ | $\mathfrak S_{210}(N)$ |
|---:|---:|---:|
| 4 | 15 | $175/128$ |
| 6 | 30 | $175/64$ |
| 10 | 20 | $175/96$ |
| 30 | 40 | $175/48$ |
| 42 | 36 | $105/32$ |
| 50, 100, 200 | 20 | $175/96$ |

The moment experiment uses the finite-wheel normalized count

$$X_N=\frac{R(N)}{A_{210}(N)}.$$

This normalization is explicit and matches the preliminary notebook. It is not an asserted asymptotic approximation for $R(N)$.

## Exact finite-block moments

For each displayed block, $B=H\cap[L,U]$, the notebook computes in $\mathbb Q$

$$\mu_B=\frac1k\sum_{N\in B}X_N,\qquad
M_{2,B}=\frac1k\sum_{N\in B}X_N^2,$$

where $k=|B|$, and

$$V_B=\sum_{N\in B}(X_N-\mu_B)^2=k(M_{2,B}-\mu_B^2),\qquad
T_B=\frac{k}{k-1}\mu_B^2.$$

All entries below are exact rationals. “Pass” means the strict proposed criterion $V_B<T_B$ holds.

| Even-integer interval | $k$ | Zero $R(N)$ counts | Exact $\mu_B$ | Exact $M_{2,B}$ | Exact $V_B$ | Exact $T_B$ | Pass |
|---:|---:|---:|---:|---:|---:|---:|:---:|
| 50–100 | 12 | 0 | $353/1440$ | $2173/34560$ | $5771/172800$ | $124609/1900800$ | Yes |
| 50–200 | 33 | 0 | $3991/11880$ | $34559/285120$ | $18416/66825$ | $15928081/136857600$ | No |
| 202–500 | 78 | 0 | $7193/11232$ | $5746411/13478400$ | $51178949/40435200$ | $51739249/124540416$ | No |
| 502–1000 | 143 | 0 | $927/880$ | $84441553/74131200$ | $11991823/2851200$ | $11171277/9996800$ | No |
| 1002–2000 | 306 | 0 | $93707/55080$ | $235130029/79315200$ | $850887041/39657600$ | $8781001849/3023892000$ | No |

Across all 564 residual integers in $[4,2000]$, exact enumeration found zero cases with $R(N)=0$. This is a finite observation only.

### What the criterion does prove

If some $X_N=0$ in a block, Cauchy–Schwarz applied to at most $k-1$ remaining nonzero values gives

$$\sum_{N\in B}X_N^2\ge\frac{(k\mu_B)^2}{k-1},$$

so $V_B\ge T_B$. Therefore $V_B<T_B$ is a valid sufficient condition for every $R(N)>0$ in that finite block. Its failure is inconclusive.

An active scan of 426 sliding windows, each containing 51 even integers (window endpoints differ by 100), found three violations of the strict bound. The largest ratio $V_B/T_B$ was

$$\frac{1716160}{1568187}>1$$

on the window 50–150. This window contains 21 residual integers and has no zero representation counts. It is a concrete counterexample to treating the proposed variance inequality as a universal bound, while illustrating that the inequality is not necessary for coverage.

## Four-prime correlation expansion

Let $\mathcal P_N$ be the set of unordered representations $(p,q)$ with $p<q$. Squaring its size gives an ordered pair of representations:

$$R(N)^2=\sum_{(p,q)\in\mathcal P_N}\sum_{(r,s)\in\mathcal P_N}1
=D(N)+O(N),$$

where

$$D(N)=R(N),\qquad O(N)=R(N)(R(N)-1).$$

If two representations share a prime, their other summands are forced equal, so the representations are identical. Thus every off-diagonal term consists of four distinct primes. For normalized second moments, the pointwise identity is

$$X_N^2=\frac{R(N)}{A_{210}(N)^2}+\frac{R(N)(R(N)-1)}{A_{210}(N)^2}.$$

Two exact enumerations were compared for every one of the 33 residual integers in $[50,200]$: (1) the Cartesian square of the explicit prime-pair list, and (2) a direct nested scan over lower summands with four primality checks. They agree pointwise with $(R(N)^2,R(N),R(N)(R(N)-1))$.

Aggregate results on this block are:

- Total four-prime configurations: 1803.
- Diagonal contribution $\sum R(N)$: 229.
- Off-diagonal contribution $\sum R(N)(R(N)-1)$: 1574.
- Exact weighted diagonal contribution to $\sum X_N^2$: $76033/129600$.
- Exact weighted off-diagonal contribution: $27647/8100$.
- Exact total $\sum X_N^2$: $34559/8640$, equal to the sum of the two weighted contributions.

## Limitations and unresolved proof obligations

The wheel factor records local admissibility only at 2, 3, 5, and 7. It is not the full singular series and supplies no error term for approximating prime-pair counts. The exact four-prime expansion is an identity; the computation does not estimate its off-diagonal correlation for arbitrarily large $N$.

To establish universal coverage of $H$, one still needs a proof that $R(N)>0$ for every $N\in H$. A moment approach would need global, rigorously justified estimates for the first and second moments (including diagonal and off-diagonal terms), strong enough to force the finite-block criterion or another positivity result on every relevant block. Finite checks, even with exact arithmetic, cannot provide that infinite-range argument. No result here proves Goldbach's conjecture or universal coverage.

## Reproduction

Open and run all code cells in `stage56_pointwise_second_moment.ipynb` with the SageMath 10.9 kernel. The notebook contains the definitions, exact finite computations, assertions comparing both four-prime algorithms, and the printed output summarized above.
