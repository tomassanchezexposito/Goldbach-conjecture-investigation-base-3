# Stage 56 — pointwise variance feasibility diagnostic

**Status:** finite computational observation, checked with exact Python integers and rational fractions; not a universal theorem.

Run from a SageMath Jupyter code cell using the script content, or from the repository root:

```bash
python experiments/stage56_variance_probe.py
```

This small diagnostic uses only Python standard-library arithmetic, so it also runs in SageMath's Python 3 (Sage) kernel without importing symbolic packages.

For an even number N, R(N) counts unordered pairs of distinct primes p<q with p+q=N, and C_210(N) counts compatible reduced residue pairs modulo 210. In the residual set H, x_N=R(N)/C_210(N).

For K values x_N, the proposed sufficient test is:

- mean mu > 0
- centered sum V = sum (x_N - mu)^2 < K * mu^2 / (K-1).

If this bound holds, no x_N can be zero. This is a proved elementary implication, not an established bound for all prime-representation blocks.

## Independently reproduced results

| Inclusive interval | K in H | Zero counts | mean (exact) | centered sum V | threshold | test passes |
|---|---:|---:|---|---:|---:|---|
| [50,100] | 12 | 0 | 353/1440 | 0.033397 | 0.065556 | Yes |
| [50,200] | 33 | 0 | 3991/11880 | 0.275585 | 0.116384 | **No** |

The calculations were run locally using exact fractions. Displayed decimals are rounded; the comparisons use exact rational arithmetic.

For N=100 the ordered four-prime indicator sum over p,r<N/2 counts 36 configurations, equal to R(100)^2 because R(100)=6.

## Mathematical consequence

The proposed global variance criterion is **not necessary** for the absence of isolated zeros: a block with no zeros can fail it. Applying it indiscriminately to increasingly large intervals is therefore potentially counterproductive.

This finding does **not** refute a hypothetical universal upper bound for a different, carefully chosen family of blocks. Any such proposal must be tested independently, without assuming Goldbach or the author's three-case coverage.

## Next task

Study fluctuations after removing local biases and seek a non-circular lower bound for an individual N in H. Consider local weights, positivity certificates, and four-prime off-diagonal control, but do not confuse exact expansion of R(N)^2 with an independent analytic estimate.
