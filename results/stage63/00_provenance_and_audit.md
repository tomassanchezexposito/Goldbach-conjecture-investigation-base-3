# Stage 63 M0 — provenance and critical audit

**Evidence status:** this document records source provenance, independently rerun finite checks, and mathematical audits. It establishes no new universal prime-pair theorem. The original three-case statement and the open residual coverage obligation are retained.

## Repository state and provenance

- Repository: `tomassanchezexposito/Goldbach-conjecture-investigation-base-3`.
- Work branch: `cocalc/stage63-extended-analytic-program`.
- Stage 63 starting commit: `4aa65d9ea7e735e81e40672b672ebaae76174e6d`.
- The branch was fetched and checked out from `origin` using the dedicated SSH identity selected with `IdentitiesOnly=yes`; no credential contents were read or emitted.
- At entry, tracked files were clean. Three untracked `__pycache__` directories were already present in `results/stage61/`, `src/`, and `tests/`. They were preserved and excluded from all Stage 63 commits.
- The exact original coordinate convention is recorded in `docs/research_statement.md`: an odd candidate is `3+2a`, with complementary indices satisfying `a+b=N/2-3`. It is a position parameterization, not ternary digits or a mod-3 assertion.

The report and source provenance commits checked in the current branch history are:

| Stage | Primary report/source | Origin commit |
|---|---|---|
| 57 | `results/stage57/report.md` | `e77e3d0e3c4c3bb005c37e3d30396131598003a2` |
| 58 | `results/stage58/pointwise_second_moments.md` | `d847c3a88d441d2332585c72b468498612ba190e` |
| 59 | `results/stage59/report.md` | `a35142ae4c83f0edfa2e89ef2aa4000c1b6389ae` |
| 60 | `results/stage60/report.md` | `e33e4103ad97686be7f9c21cad2fe8636f2bb7e2` |
| 61 | `results/stage61/report.md` | `fcafa07f7601e41608e1e71c54d661869f759028` |
| 62 | `results/stage62/report.md` | `262264f9d6a2fee6a849cc11645647074578e9c6` |

The source files and all prior result directories remain in place. SHA-256 values for the audited reports, task/protocol definitions, manifests, and independent verifier outputs are recorded in `00_manifest.json`.

## Definitions retained

The three clauses remain: (i) `N=p+1` for prime `p`; (ii) `N=2p` for prime `p`; or (iii) `N=p+q` for distinct primes `p<q`, with `N-2p=2q-N`. The reflection equality follows from the sum equation and is not a primality condition. For

`H={N>=4: N even, N-1 composite, N/2 composite}`,

the first two clauses fail and the required conclusion is `R(N)>0`, where `R(N)` counts unordered genuine-prime pairs `p<q` with sum `N`. No Stage 63 audit or finite calculation assumes this conclusion.

`A_210(N)` is the exact number of residues `x mod 210` for which both `x` and `N-x` are coprime to 210. Stage 56 called the same integer `C_210(N)`. This relabeling does not change the residue count, but neither symbol denotes the complete Hardy–Littlewood singular series or a count of prime pairs.

## Independent verification transcript

All commands below were run from the repository root with the already installed Python 3.14.4 and SageMath 10.9. No software was installed and no broad new Goldbach scan was run.

| Command | Result | Evidence classification |
|---|---|---|
| `python3 -B results/stage57/verify_stage57.py` | Passed: 5,616 rows, 564 residual targets, 999 wheel values, all five correlation classes and aggregates. | Finite exact verification |
| `python3 -B results/stage58/verify_second_moment.py` | Passed: 620 shifted rows, 62 residual anchors, 149 same-target values, 249 wheel targets, exact rational moment and weighted-vector checks. | Finite exact verification |
| `python3 -B results/stage58/verify_stage58.py` | Passed: 5,456 finite vector checks, diagonal identity through 300, cyclic zero countermodel, and Stage 56/57 counterexamples. | Finite exact verification |
| `python3 -B results/stage59/verify_stage59.py` | Passed: even centers 8 through 4,998, 1,524 residual targets, 250 shared-prime configurations; only finite observations. | Finite exact verification |
| `python3 -B results/stage59/verify_local_energy.py` | Passed: exact wheel/pair checks, five recorded blocks, sharpness and cyclic cases. | Finite exact verification |
| `python3 -B results/stage60/verify_stage60.py` | Passed: 147 rows, 62 residual centers, 441 wheel checks and 256 zero-center abstract triples. | Finite exact verification |
| `python3 -B results/stage61/verify_stage61.py` | Passed: 8 triples, 24 target counts, 8 signed decompositions and 27 rational-grid cases. | Finite exact verification |
| `python3 -B results/stage62/verify_singular_series.py` | Passed: six exact CRT examples and the 27-point conditional grid. | Finite exact verification |
| `sage -python results/stage62/verify_singular_series_sage.py` | Passed: six examples, 49 independently recomputed center identities, 27 rational-grid cases; SageMath 10.9. | Independent finite exact verification |
| `python3 -B -m unittest discover -s tests -v` | All four repository unit tests passed. | Finite software verification |

The Sage verifier rewrote only a runtime-timing field in the existing Stage 62 output during this audit. That incidental generated difference was restored byte-for-byte from the Stage 63 starting commit before this milestone was staged. No prior Stage 56–62 source or result is included in the Stage 63 changes.

## Critical mathematical audit

### Stage 56 — variance criterion

**Proved in research:** for `k` nonnegative values with mean `mu`, a zero coordinate forces centered sum of squares `V >= k*mu^2/(k-1)`. Strictly smaller variance is therefore sufficient for positivity. **Refuted:** the claim that this strict condition holds on every block. The finite residual block `[50,150]` has 21 entries, no zero, and exact variance-to-threshold ratio `1716160/1568187 > 1`. Failure of a sufficient criterion does not imply a zero.

### Stage 57 — shifted correlations

**Proved in research:** the ordered Cartesian product of two distinct-target representation sets partitions into four shared-position classes and a four-distinct class; local wheel counts are exact by CRT. The signed covariance expression can be negative. **Refuted:** the blanket positive-covariance block inequality, by the exact interval `[262,362]`, shift 1, covariance `-127/3000000`. The partition identity does not supply independent bounds on its terms.

### Stage 58 — moments

**Proved in research:** the sharp `m`-zero unweighted moment lower bound `V >= km*mu^2/(k-m)` and the weighted one-zero inequality. Equal weights maximize the worst-coordinate two-moment threshold when the zero is unknown. The identical-pair diagonal and four-distinct terms at one target, and shared-position/four-distinct terms across distinct targets, have exact combinatorial partitions. **Refuted:** reweighting alone improves the unknown-zero threshold, and positive shifted means force coordinatewise positivity; the exact cyclic vector `(0,1,...,1)` is a countermodel.

### Stage 59 — graph energies

**Proved in research:** path/cycle/graph Laplacian inequalities are deterministic implications from independently supplied mean and energy estimates. Their equality cases establish sharp constants in the specified finite-dimensional settings. **Open:** no independent true-prime arithmetic estimate supplies the needed means and energies uniformly. The graph inequality is not itself a prime distribution theorem.

### Stage 60 — candidate caps

**Proved in research:** the stated elementary candidate-position cap is an upper bound for `R(N)`, and exact wheel/correlation bookkeeping holds. **Refuted:** upper caps and wheel factors alone force positivity; an abstract profile with a zero center satisfies these restrictions. Finite counts are observations only.

### Stage 61 — signed three-point certificate

**Proved in research:** the exact identity is

`9D_N=-a^2-3b^2-c^2+6ab+2ac+6bc`,

where `a=X_{N-2}`, `b=X_N`, `c=X_{N+2}`. If `b=0`, it reduces to `-(a-c)^2<=0`. The common-relative-error condition `|epsilon_i|<=1/3` implies positive center, but its premise includes a positive common baseline and already forces `b>0`; it is not an independent proof input.

### Stage 62 — singular-series variation

**Proved in research, as model arithmetic:** the exact singular-series factor `F(n)=prod_{ell|n, ell>2}(ell-1)/(ell-2)` can vary without bound relative to `A_210` across adjacent residual targets, even with equal wheel factors. Using Dirichlet gives the unbounded adjacent ratio. Using Linnik's least-prime theorem gives a sequence where the singular-series profile `Phi(n)=F(n)n/(A_210(n)(log n)^2)` has a negative Stage 61 signed certificate for all sufficiently large sequence members. The proof checks the reduced CRT class, `q_y>y`, the fixed factors 3 and 7 and exclusion of 5 and all prescribed primes in `q_y-2`, the divisor-count bound, and the polynomial-in-modulus upper bound from Linnik. Euler's divergence of prime reciprocals yields `F(N_y)->infinity`.

This is not a theorem about `R(n)`: no pointwise Goldbach asymptotic for every even target has been proved. Nor does a negative value of a sufficient certificate refute positivity of the actual representations; it only invalidates a proposed universal model-smoothness route.

## M0 conclusion and next milestone

The checked record is internally coherent on its stated evidence classes. The strongest audit finding is that finite-wheel normalization does not capture higher-prime singular factors, while importing the full singular-series profile into the Stage 61 local certificate still makes that certificate negative infinitely often. This rules out that particular universal local-smoothness strategy at the model level. The next milestone proves an exact shared-prime CRT lemma and identifies its precise limits; it does not treat admissible residues as prime triples.

**Universal coverage of the original three-case statement remains open.**
