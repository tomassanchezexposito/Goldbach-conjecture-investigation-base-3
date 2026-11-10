# Stage 59 — Sharp local second-moment inequality for wheel-210 prime pairs

**Evidence status:** Proven elementary inequalities (T1–T3); finite observations (tables); **unproved** pointwise arithmetic energy estimates. The author's universal three-case statement remains open.

## Original representation target

The author's statement permits, for every even N>2: (i) N=1+p with p prime; (ii) N=2p with p prime; or (iii) N=p+q with two distinct primes p<q and equidistant doubles N-2p=2q-N. The reflection equation is equivalent to p+q=N and supplies no independent primality condition.

The residual set is H={even N>=4: N-1 composite and N/2 composite}. Let R(N) be the number of unordered genuine distinct-prime pairs p<q satisfying p+q=N. The remaining universal obligation is R(N)>0 for **each** N in H.

Let A_210(N) be the exact number of locally admissible residues modulo 210: the product, over ell=2,3,5,7, of ell-1 if ell divides N and ell-2 otherwise. For even N this is positive. Define x(N)=R(N)/A_210(N).

## E59-T1: pointwise path-energy inequality — PROVED

For any real sequence x_0,...,x_(k-1), k>=2, define the mean mu=(sum x_i)/k, the adjacent energy E=sum_{i=0}^{k-2}(x_(i+1)-x_i)^2, and

A_(k,j)=[sum_{t=1}^j t^2 + sum_{t=1}^{k-1-j} t^2]/k^2.

**Theorem:** (x_j-mu)^2 <= A_(k,j)*E for each 0<=j<k.

**Proof:** Put d_t=x_(t+1)-x_t. Telescoping the mean gives x_j-mu=sum_{t=0}^{k-2} c_(j,t)d_t, where c_(j,t)=(t+1)/k for t<j, and c_(j,t)=-(k-t-1)/k for t>=j. The squared norm of the coefficient vector equals A_(k,j). Apply Cauchy–Schwarz. QED.

**Pointwise corollary:** For nonnegative entries, mu^2>A_(k,j)*E implies x_j>0. Hence for consecutive even targets n_j=n_0+2j, if independently established estimates mu>=m>0 and E<=U satisfy m^2>A_(k,j)*U, then R(n_j)>0 **without assuming its existence**. No such uniform analytic estimates for genuine prime-pair counts have been established.

## E59-T2: sharp constant, including sequences with a zero — PROVED

For a fixed j take differences d_t=-c_(j,t) as in the proof and set x_j=0. Integrating the differences to both sides constructs x_i>=0 for all i. Equality in Cauchy–Schwarz holds, so mu^2=A_(k,j)*E. Thus the constant is optimal even for nonnegative sequences containing a zero at the inspected position. This optimality is relative to arbitrary nonnegative sequences; additional arithmetic structure could conceivably yield a stronger bound.

## Exact four-prime expansion

For k consecutive even targets, the adjacent energy is

E = 2 sum_j x_j^2 - x_0^2 - x_(k-1)^2 - 2 sum_{j=0}^{k-2} x_j*x_(j+1).

Each x_j^2 contains a same-target ordered pair of prime-pair representations, with an identical-pair diagonal and a four-distinct-prime off-diagonal. Each shifted product x_j*x_(j+1) partitions into **shared-prime** and **four-distinct-prime** configurations (as checked in Stage 57), divided by both exact wheel factors.

This is an identity, not an independent upper bound on E. A proof of universal positivity needs a new distribution estimate that bounds these terms with the needed signs and uniform constants.

## E59-T3: a single zero is invisible to low-precision averaged correlations — PROVED

Consider the **abstract** cyclic nonnegative vector (0,1,...,1) of length k. For any m distinct cyclic shifts h_1,...,h_m, the average of products of m shifted entries is exactly 1-m/k. Exactly m translated products include the unique zero.

Thus even all such fixed-order (including fourfold) correlations can approach their all-ones values to o(1) while one entry stays zero. An average estimate accurate only to o(1) is insufficient to exclude one zero: resolving this defect from an m-fold average requires precision on the scale m/k. This is a logical countermodel, NOT a prime-count counterexample.

The Stage 55 sharp variance threshold also follows: among nonnegative k-vectors of fixed mean mu with at least one zero, the smallest sum of centered squares is k*mu^2/(k-1), attained by a zero and k-1 identical positive values.

## Finite exact results (not theorems about all primes)

An independent local Python computation used exact sieve counts, trial division crosschecks, exact Fraction arithmetic, wheel residue enumeration and direct classification of adjacent four-prime configurations.

| Inclusive even block | Residual targets | Real zeros | Residual positions satisfying E59-T1 strict certificate | Shared-prime terms | Four-distinct-prime terms |
|---|---:|---:|---:|---:|---:|
| 50–54 | 2 | 0 | 2 | 5 | 22 |
| 50–60 | 3 | 0 | 3 | 13 | 56 |
| 50–100 | 12 | 0 | 0 | 80 | 451 |
| 50–200 | 33 | 0 | 0 | 328 | 2987 |
| 262–362 | 25 | 0 | 0 | 368 | 6712 |

Independent prime-pair tests: 249 even targets up to 500. Direct wheel checks: 249 targets. Sharpness equality checks: 22 cases. Cyclic m-fold moment checks: 12 cases. All passed.

A further finite pilot sampled exactly 295 residual centers in {10000,10020,...,17980}. Centered windows in progressions of spacing 2 and 210 gave:

| k | Spacing 2 certified | Spacing 210 certified |
|---|---:|---:|
| 3 | 295/295 | 295/295 |
| 5 | 295/295 | 295/295 |
| 9 | 295/295 | 295/295 |
| 21 | 295/295 | 295/295 |
| 51 | 10/295 | 72/295 |

All assertions used exact rational comparisons. Short windows look more feasible in this *finite sample*. Same-wheel-class spacing improves the 51-window success rate in this sample but does not supply uniform positivity.

## First missing step

For each N in H, select a short path of even targets containing N, with center index j, and prove independent unconditional bounds

  mean >= m_N>0, energy <= U_N, and m_N^2 > A_(k,j)*U_N,

or find a genuinely stronger pointwise analytic route. The mean bound and the energy bound must be derived from genuine prime distribution, **not** by assuming or using R(N)>0.

For the center of a path, A_(k,j) grows proportionally to k. Long blocks therefore demand unusually small total energy. The k=51 results show that a direct large-block extrapolation is untenable.

## External context

Bhowmik and Grimmelt (2026), "The exceptional set of the Goldbach problem", Analysis Mathematica 52, 767–808, DOI: https://doi.org/10.1007/s10476-026-00191-z, review major/minor arcs and introduce an explicit major-arc formula. Neither an exceptional-set bound nor an exact major-arc formula alone eliminates a hypothetical isolated zero.

Grimmelt and Teräväinen, "The Exceptional Set in Goldbach's Problem with two Chen Primes", arXiv:2508.16400 (2025, revised 2026), concerns Chen primes and exceptional sets; it is not a proof of the binary Goldbach conjecture.

**Status:** three combinatorial lemmas PROVED; computations finite; universal pointwise energy estimate OPEN; the author's universal coverage claim NOT PROVED.


## E59-T4: sharp *multi-shift graph-energy* certificate — PROVED (classical discrete Sobolev form)

The path inequality above is a special case of classical discrete Sobolev / graph-Laplacian inequalities, not a new graph-theoretic theorem. Relevant prior work: K. Takemura, A. Nagai and Y. Kametaka, "Two types of discrete Sobolev inequalities on a weighted Toeplitz graph", *Linear Algebra and its Applications* **507** (2016), 344–355, DOI https://doi.org/10.1016/j.laa.2016.06.029 . Here we apply the method to wheel-210-normalized prime-pair counts.

Let G=(V,E) be a connected undirected graph on k indexed even targets, with strictly positive edge conductances w_uv and graph Laplacian L. Define

- x in R^k with components x_i=R(n_i)/A_210(n_i).
- mu=(1/k) sum_i x_i.
- graph energy E_G=sum_{uv in E} w_uv (x_u-x_v)^2 = x^T L x.
- a_j=e_j-(1/k)1 and sharp constant C_(G,j)=a_j^T L^+ a_j, where L^+ is the Moore–Penrose pseudoinverse.

**Theorem:** (x_j-mu)^2 <= C_(G,j)*E_G. Consequently, mu^2>C_(G,j)*E_G implies the genuine target count R(n_j)>0.

**Proof:** L is positive semidefinite with kernel spanned by 1. Since a_j is orthogonal to 1, a_j=L L^+a_j. Hence a_j^Tx=(L^+a_j)^T Lx. Apply Cauchy–Schwarz in the L-seminorm to obtain the displayed inequality.

**Sharpness for nonnegative sequences with a zero:** Choose v=L^+a_j (mean zero). At every vertex i≠j, (Lv)_i=-1/k<0. If a maximum occurred at i≠j, the Laplacian maximum principle would force (Lv)_i>=0, a contradiction; hence v_j is maximal. Define x_i=v_j-v_i>=0. Then x_j=0, its mean equals v_j=C_(G,j), its energy equals C_(G,j), and equality holds. This proves optimality without assuming any genuine prime pair.

### Exact finite multi-shift feasibility experiment

Construct the unit-conductance graph on k=51 consecutive index positions, connecting every pair of indices with separation at most h, for h=1,2,5,10,50. Choose target position j=25. The sharp constant was computed by exact rational elimination of (k L + J)v=k e_j-1; its value for h=5 is

    C_(51,25,h=5) =
    38683159850948518167722 / 265567883438518147239561.

On the same 295 residual target centers in the finite grid {10000,10020,...,17980}, all comparisons used exact rational arithmetic:

| Maximum connected index lag h | Even-number spacing 2 | Even-number spacing 210 |
|---:|---:|---:|
| 1 (path only) | 10/295 | 72/295 |
| 2 | 287/295 | 294/295 |
| 5 | **295/295** | **295/295** |
| 10 | **295/295** | **295/295** |
| 50 (complete graph) | 295/295 | 10/295 |

The complete graph reproduces the classical variance criterion, while the path graph recovers E59-T1. An intermediate graph outperformed both endpoints on this finite sample. Its edge energies incorporate **multiple shifted four-prime correlations**: each (x_i-x_j)^2 contributes two same-target second moments and one shifted correlation, including the shared-prime and four-distinct terms classified in Stage 57.

**Critical limitation:** this is a finite experiment and the certificate uses measured genuine prime-pair counts. We have not established independent analytic estimates for mu or E_G, so no universal prime-pair positivity follows. There is no proof that h=5 is optimal outside this sample.

**Code:** \`results/stage59/verify_graph_energy.py\` uses exact Fraction elimination, verifies the sharp constant with a nonnegative zero-coordinate equality witness, and checks every finite window. It writes \`results/stage59/graph_energy_pilot.json\` when run.

### Next analytical obligation

Study whether a weighted multi-shift graph G_N, chosen **without knowing whether R(N)>0**, admits unconditional lower/upper bounds mu_N>=m_N>0 and E_(G_N)<=U_N for every sufficiently large N in H, with m_N²>C_(G_N,j)U_N. Determine whether published major/minor-arc or sieve correlation bounds can control the **signed sum of several four-prime correlations** with this required precision. If only average-in-N bounds are available, state that the isolated-zero exclusion remains unproved.
