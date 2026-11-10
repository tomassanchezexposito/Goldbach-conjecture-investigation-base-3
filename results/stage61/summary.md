# Stage 61 summary

## Established

- The exact signed three-target quantity is
  $$D_N=\frac{-X_{N-2}^2-3X_N^2-X_{N+2}^2+6X_{N-2}X_N+2X_{N-2}X_{N+2}+6X_NX_{N+2}}9.$$
- Its full arithmetic expansion separates same-target diagonals, same-target four-distinct terms, one-prime shared-position contractions, and cross-target four-distinct prime configurations, with exact wheel denominators.
- If $R(N)=0$, then $D_N=-(X_{N-2}-X_{N+2})^2/9\le0$.
- If all three normalized counts are within relative error $1/3$ of one common positive baseline, then $D_N\ge8/81$ times the baseline squared. A uniform $C/\log N$ version would have effective threshold $N\ge\max(N_0,\lceil e^{3C}\rceil)$.
- The PR #9 index ambiguity is resolved: $Q_4(N,M)>0$ implies representations at both indexed targets, while $Q_4(N-2,N+2)>0$ alone says nothing deductive about the center.

## Refuted or insufficient

- Wheel admissibility plus $0\le R(n)\le\lfloor(n-4)/4\rfloor$ cannot force signed positivity. The abstract $N=100$ vector $(1,0,1)$ obeys those caps and has $D=-1/18225$; it is not claimed to arise from primes.
- Averages, exceptional-set bounds, Chen-type prime-plus-almost-prime theorems, and outer-target correlations do not establish strict signed dominance at every residual target.

## Exact finite check

Eight focused triples with targets at most 502 were computed using a sieve and checked independently using trial division and direct modulo-210 enumeration. Both routines use exact rational arithmetic. Two centers lie in $H$; all eight signed configuration expansions agree exactly. The 27-point relative-error grid has exact minimum $4/9$. These are finite observations only.

## Unresolved

The missing input is a non-circular, explicit pointwise estimate for genuine-prime correlations that makes the signed off-diagonal terms dominate the same-target diagonal and four-distinct terms for each sufficiently large $N\in H$, with an effective cutoff. No universal three-case coverage is proved.
