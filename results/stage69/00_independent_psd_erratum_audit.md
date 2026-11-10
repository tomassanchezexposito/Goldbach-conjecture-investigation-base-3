# Stage 69 M0 — independent audit of the Stage 68 PSD-lifting claim

**Verdict: PROVED correction.** This audit preserves the Stage 68 files and records the exact false step. The result is an abstract matrix-optimization correction; it says nothing about Goldbach representations.

## 1. The inherited two-projector example

For $G_1=\operatorname{diag}(1,0)$, $G_2=\operatorname{diag}(0,1)$, and unit budget on both terms, the rank-one objective is
\[
F(z)=\sqrt{z^*G_1z}+\sqrt{z^*G_2z}=|z_1|+|z_2|,
\qquad |z_1|^2+|z_2|^2=1.
\]
Cauchy--Schwarz gives $F(z)\le\sqrt2$, with equality at $|z_1|=|z_2|=1/\sqrt2$. For the lifted problem, every feasible $X$ has $X_{11}=t$, $X_{22}=1-t$ for some $t\in[0,1]$, so
\[
F_{\rm PSD}(X)=\sqrt t+\sqrt{1-t}\le\sqrt2,
\]
again with equality at $X=I/2$. The off-diagonal entry is irrelevant to this objective. Thus both optima are $\sqrt2$. The separate termwise spectral estimate is
\[
F_{\rm PSD}(X)\le\sqrt{\lambda_{\max}(G_1)}+\sqrt{\lambda_{\max}(G_2)}=2.
\]
It is generally only an upper bound. Here it is strict at every optimizer. Its value $2$ is not attained by a trace-one $X$.

There is a second direct check of the lifted value: concavity of $t\mapsto\sqrt t$ gives $\sqrt t+\sqrt{1-t}\le2\sqrt{1/2}=\sqrt2$, with equality only at $t=1/2$. This confirms the lift calculation independently of the vector Cauchy equality argument.

### Exact predecessor error and provenance

The first invalid inference in `results/stage68/02_exact_budget_optimization.md`, final paragraph of “Certified relaxations,” is the equation-level identification of
\[
\max_{X\succeq0,\,\operatorname{tr}X=1}(\sqrt{X_{11}}+\sqrt{X_{22}})
\]
with $2$. The expression was replaced by the sum of separate spectral maxima, which is the triangle certificate, not the relaxed optimum. `results/stage68/08_adversarial_review.md` repeats this same substitution in section 2 and then calls it a valid PSD gap; its section 8 also says both verifiers reproduce that gap. `results/stage68/00_operator_allocation_and_uniform_gram.md` says the diagonal example proves a density-matrix relaxation can be wasteful. `results/stage68/final_report.md` repeats “rank-one PSD relaxation gap” and attributes that claim to the verifiers. Those four claims are superseded by this correction.

The machine-readable `results/stage68/stage68_exact_results.json` already records the correct value `orthogonal_PSD_true_optimum: sqrt(2)` and triangle value `2`; it does not encode a strict lifting gap. The Stage 68 Python verifier's assertion
\[
\bigl(\sqrt{1/2}+\sqrt{1/2}\bigr)-2=\sqrt2-2
\]
is a true arithmetic identity, but tests no optimization and therefore cannot certify the claimed gap. The Stage 68 Sage output has no independently optimized lifted problem either. Historical files and their hashes remain untouched.

## 2. The six-Pauli family: independent proof of a real abstract gap

Let $P_{a,\varepsilon}=(I+\varepsilon\sigma_a)/2$ for $a\in\{x,y,z\}$ and $\varepsilon\in\{+1,-1\}$, with the Pauli matrices as defined in `00_erratum_psd_lifting.md`. Each $\sigma_a$ is Hermitian, squares to $I$, and has trace zero. Hence each $P$ is Hermitian and idempotent, with trace one; its eigenvalues are $0,1$, so it is PSD and rank one.

For every PSD trace-one $X$, $\operatorname{tr}(P_{a,+}X)+\operatorname{tr}(P_{a,-}X)=1$. Cauchy--Schwarz bounds each axis pair by $\sqrt2$. The state $I/2$ makes all six expectations $1/2$, attaining all three bounds simultaneously. Therefore the lifted optimum is exactly $3\sqrt2$.

For a unit vector $z=(z_1,z_2)$, define
\[
r_x=2\Re(\overline z_1z_2),\quad r_y=2\Im(\overline z_1z_2),\quad r_z=|z_1|^2-|z_2|^2.
\]
Then
\[
r_x^2+r_y^2+r_z^2=4|z_1|^2|z_2|^2+(|z_1|^2-|z_2|^2)^2=(|z_1|^2+|z_2|^2)^2=1.
\]
Conversely, if $r$ is a real unit vector with $r_z>-1$, take
\[
z_1=\sqrt{(1+r_z)/2},\qquad z_2=(r_x+i r_y)/(2z_1).
\]
The sphere relation gives $|z_2|^2=(1-r_z)/2$, so $z$ is unit and has the specified $r_x,r_y,r_z$. For $r_z=-1$, use $z=(0,1)$. Thus every unit $r$ is represented.

The rank-one objective is $\sum_a f(r_a^2)$, where $f(t)=\sqrt{1+\sqrt{1-t}}$. For $u=\sqrt{1-t}$ and $0\le t<1$,
\[
f''(t)=-\frac{2+3u}{16u^3(1+u)^{3/2}}<0.
\]
By continuity at $t=1$, $f$ is strictly concave on $[0,1]$. Jensen and $\sum_a r_a^2=1$ imply
\[
\sum_a f(r_a^2)\le3f(1/3)=3\sqrt{1+\sqrt{2/3}}.
\]
Equality requires $r_x^2=r_y^2=r_z^2=1/3$; such unit Bloch vectors exist, including $(1,1,1)/\sqrt3$. So this is the pure optimum.

An independent bound reaches the same value without Jensen. Two applications of Cauchy--Schwarz give
\[
\left(\sum_a\sqrt{1+\sqrt{1-r_a^2}}\right)^2
\le3\left(3+\sum_a\sqrt{1-r_a^2}\right)
\le3(3+\sqrt6)=9\left(1+\sqrt{2/3}\right).
\]
Equality in both steps holds when $r_a^2=1/3$ for all axes. The pure optimum is strictly below $3\sqrt2$ because $\sqrt{2/3}<1$. This is a genuine PSD-lifting gap for this abstract six-projector family.

## 3. The interval-Gram example remains a triangle-bound result

For the two Stage 68 interval Grams and $J=\{1,2\}$, the shared off-diagonal is $b=1/4-1/(2\pi)>0$. A real symmetric $2\times2$ matrix with a nonzero off-diagonal has distinct eigenvalues, so each top eigenspace is one-dimensional. Their commutator has off-diagonal entry $-2\sqrt2 b/\pi\ne0$. If two Hermitian matrices in dimension two with simple spectra shared an eigenvector, its orthogonal complement would also be invariant, and they would commute. Thus their top directions do not coincide. The exact allocation theorem's triangle bound is therefore strictly larger than the true rank-one allocation for these genuine interval Grams.

That argument proves strictness of the triangle bound, **not** strictness of a trace-one PSD lifting. The available Stage 68 calculations did not optimize that lifted objective for the interval pair. Whether this particular interval-Gram family has a lifting gap remains OPEN here.

## 4. Corrected audit rule and exact regression

For each nonlinear optimization, report separately: the rank-one maximum $\sup_{\|z\|=1}$; the lifted maximum $\sup_{X\succeq0,\operatorname{tr}X=1}$; the termwise triangle certificate $\sum_r\sqrt{B_r\lambda_{\max}(G_r)}$; and any Cauchy/dual upper certificate. A list of matrix eigenvalues is not an optimization of a sum of square roots.

The required command `python3 -B results/stage69/verify_psd_lifting.py` passed. It uses exact SymPy algebra to check the three old-example values separately, projectors, the mixed value, an explicit pure extremizer, and the strict comparison. The all-parameter optima are proved above; the script is a regression, not the proof. Its machine-readable result is `psd_lifting_exact_results.json`. No interval-lifting claim is made.

## Potential circularity and first missing arithmetic fact

Nothing in either PSD example concerns primes. To use this geometry for Goldbach would require a new inequality connecting the actual prime-square input to an operator optimum, plus a signed target-specific saving. The first missing arithmetic fact is still a non-circular estimate for the genuine-prime convolution at a prescribed target; the operator correction does not supply it.
