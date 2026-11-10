# Stage 63 M3: adversarial comparison of adjusted certificates

Let `t_-=N-2`, `t_0=N`, `t_+=N+2`, and write `R_i=R(t_i)`, `A_i=A_210(t_i)`. The exact Stage 61 variables are `X_i=R_i/A_i`. This note tests changes of normalization and graph weights as certificates; it does not assert a prime-pair asymptotic.

## Track A — singular-series-adjusted variables

Let `F(t)=prod_{p|t,p>2}(p-1)/(p-2)` and

$$\Phi(t)=\frac{F(t)t}{A_{210}(t)(\log t)^2},\qquad Y_i=\frac{X_i}{\Phi(t_i)}=\frac{R_i}{B_i},\qquad B_i=A_i\Phi(t_i)=\frac{F(t_i)t_i}{(\log t_i)^2}.$$

All denominators are positive for even `t>=4`; the lower endpoint is thus already defined. The exact signed form, with no smoothness or positivity assumption on `R_i`, becomes

$$9D_Y=-Y_-^2-3Y_0^2-Y_+^2+6Y_-Y_0+2Y_-Y_++6Y_0Y_+.$$

In genuine-prime counts this is exactly

$$\begin{aligned}
9D_Y={}&-\frac{R_-+Q_{--}}{B_-^2}-3\frac{R_0+Q_{00}}{B_0^2}-\frac{R_++Q_{++}}{B_+^2}\\
&+6\frac{S_{-0}+Q_{-0}}{B_-B_0}
+2\frac{S_{-+}+Q_{-+}}{B_-B_+}
+6\frac{S_{0+}+Q_{0+}}{B_0B_+}.
\end{aligned}$$

Here `Q_ii=R_i(R_i-1)` counts ordered pairs of distinct representations at one target; these necessarily use four distinct prime values. For `i<j`, `S_ij` is the exact shared-prime contraction from M1 and `Q_ij` is the four-distinct count, so `R_iR_j=S_ij+Q_ij`. The identity is obtained by substitution, not an estimate. The denominators `B_i` retain the complete arithmetic factors and the logarithmic main scale.

A strict inequality `D_Y>0` would imply `R_0>0` because if `R_0=0`, then `Y_0=0` and

$$9D_Y=-(Y_--Y_+)^2\le0.$$

But proving `D_Y>0` from the expanded correlations is precisely a genuine-prime pointwise problem. A lower bound on `Y_0` itself, or a uniform relative approximation `Y_i=c+o(1)` with a proved `c>0`, already entails center positivity and is not an independent route unless proved from separate noncircular input. Stage 62 proves that the *unadjusted* singular-series profile `X=Phi` makes the Stage 61 path form negative infinitely often. Under the new scaling that formal profile becomes `Y=1`, so this particular model obstruction disappears; this algebraic repair does not show that actual `Y` is close to 1. The needed pointwise Hardy–Littlewood estimate remains unproved.

## Track B — weighted graph energy and pseudoinverse

Let `G` be a fixed connected finite graph on the target set, with positive edge conductances and Laplacian `L`. Choose preassigned arithmetic weights `w_i>0` with `sum_i w_i=1`, and a target vertex `j`. For any real vector `x`, put `mu_w=w^T x`, `c=e_j-w`, and `tau=c^T L^+c`. Since `c^T 1=0`, the Moore–Penrose pseudoinverse gives

$$x_j-\mu_w=c^Tx=(L^+c)^TLx,$$

and Cauchy–Schwarz in the Laplacian seminorm yields the sharp inequality

$$(x_j-\mu_w)^2\le(c^TL^+c)(x^TLx)=\tau E_G.$$

Sharpness follows by taking `x=L^+c` up to an additive constant. If `x_j=0`, then `mu_w^2<=tau E_G`. Thus independently proved bounds `mu_w>=m>0` and `E_G<=U` with `m^2>tau U` imply `x_j>0`. This is the same mean/energy proof obligation in weighted coordinates. If a weight choice or lower mean depends on `R_j>0`, it is circular; changing `tau` alone contributes no prime-distribution estimate.

For the three-vertex path with equal weights and the center selected, solving `Lu=e_j-(1/3)1` with `sum u_i=0` gives `tau=2/9`. The sharp zero-center vector `(1,0,1)` has `mu^2=(2/3)^2=4/9` and `tau E=(2/9)2=4/9`. Hence no smaller deterministic constant can exclude the one-zero profile. Stage 59 already proved and tested the general pseudoinverse inequality, its sharpness, and finite path/graph cases; this stage recovers it as an adversarial check, not as a new graph theorem.

## Track C — anchored and off-center correlations

The exact Stage 61 expansion is recovered by splitting `R_i^2=R_i+Q_ii` and `R_iR_j=S_ij+Q_ij`. Its off-center-only positive term is `2(S_-+ + Q_-+)/A_-A_+`. The terms involving the center are `6(S_-0+Q_-0)/A_-A_0` and `6(S_0+Q_0+)/A_0A_+`; each vanishes when `R_0=0`. The negative same-target terms remain. For a zero center the entire certificate reduces exactly to

$$9D_N=-\left(\frac{R_-}{A_-}-\frac{R_+}{A_+}\right)^2.$$

Therefore a positive off-center correlation alone cannot force the center positive. Exact abstract countermodels in `03_exact_checks.json` take wheel scales equal to one and `(R_-,R_0,R_+)=(1,0,1),(1,0,2),(2,0,5)`: the off-center product is positive in every case, but `9D` is respectively `0,-1,-9`. These are logical countermodels, not prime data. The exact identities and finite prime-position classifiers (M1 and Stage 57) already distinguish the shared-prime and four-distinct pieces.

## Logical-strength table

| Proposed condition | Directly implies center positivity? | Independently established arithmetically? | Consistent with Stage 62 full singular-series profile? | Published unconditional target constants available? | Assessment |
|---|---|---|---|---|---|
| `D_Y>0` | Yes, since `R_0=0` forces `D_Y<=0` | No | The profile `Y=1` passes; actual counts unknown | No | Same strict certificate under positive coordinate scaling, not new input |
| Weighted graph `mu_w^2>tau E_G` | Yes, if `R_i>=0` and target assumptions hold | Deterministic inequality is proved; arithmetic bounds are absent | Depends on weights/profile; no actual-count conclusion | No | Generalizes Stage 59; constant change only |
| Positive lower bound on off-center `Q_-+` alone | No | No such bound used | Abstractly compatible with a zero center | No | Refuted as a sufficient logical condition |
| Uniform `Y_i` relative approximation to `c>0` | Yes, if error is small enough to force `Y_0>0` | No | It fits the adjusted formal model, not a proved estimate | No | Equivalent in strength to a pointwise positive lower bound at the center when imposed there |

## Verification and status

`03_verify_energy_countermodels.py` uses exact fractions to check the signed quadratic identity on 2,197 rational triples, the zero-center reduction on 169 cases, the sharp three-path constant on 169 endpoint pairs, and reconstructs all eight saved Stage 61 center rows from `R` and `A_210`. Stage 59's exact pseudoinverse verifier and Stage 61's original verifier remain the independent source audits. Output: `03_exact_checks.json`.

**Proved:** algebraic rescaling, correlation decomposition, graph pseudoinverse inequality, and countermodels to off-center-only sufficiency.

**Open:** every arithmetic input that would give a positive margin for the actual prime counts. No new genuine-prime estimate was found.
