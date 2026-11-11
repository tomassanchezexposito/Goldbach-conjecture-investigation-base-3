# Stage 72 — Genuine-prime, pointwise central-core theorem and sharpened prime-power correction

**Date:** 2026-11-11. **Method:** independent mathematical deductions, exact finite verification and GitHub publication, **no CoCalc/Codex**.  
**Evidence labels:** T72.1 and T72.2 **PROVED** (elementary lemmas with classical PNT for asymptotics); T72.3 **EXACT CONDITIONAL CERTIFICATE** (the needed hypothesis remains OPEN); no universal Goldbach theorem.  
**Scope:** the original author's three-case formulation is unchanged. Its residual domain is
\[
H=\{N\in2\mathbb Z:N\ge4,\ N-1\text{ composite},\ N/2\text{ composite}\}.
\]
For \(N\in H\), only distinct genuine-prime pairs remain unresolved. Prime \(2\) is not a summand at even \(N>4\), and the diagonal \(p=q=N/2\) is impossible. The genuine-prime positional map is \(p=3+2a\), not base-three digits. For odd-prime pairs the reflection condition is \(a+b=N/2-3\), a necessary algebraic equality, not an existence proof.

## 1. The genuine-prime polynomial and its exact target coefficient

Fix once for all a nonzero, nonnegative, real smooth \(w\in C_c^\infty((0,1))\). Write
\[
W=\int_0^1w(t)\,dt>0,\quad M=\|w\|_\infty,\quad e(t)=e^{2\pi it},
\]
\[
S_X(\alpha)=\sum_{p\text{ genuine prime}}(\log p)w(p/X)e(p\alpha),\quad
r_X(N)=\int_{\mathbb T}S_X(\alpha)^2e(-N\alpha)\,d\alpha.
\]
Orthogonality gives exactly
\[
r_X(N)=\sum_{\substack{p+q=N\\p,q\ {\rm genuine\ primes}}}
(\log p)(\log q)w(p/X)w(q/X)\ge0.
\tag{72.1}
\]
On H, distinct unordered pairs are counted twice. \(r_X(N)>0\) implies a genuine Goldbach pair **within the weight support**, but \(r_X(N)=0\) does not exclude pairs outside it. For \(N\in[X/2,X]\), to make the support permissive one can deliberately choose \(w>0\) on e.g. \([1/5,3/5]\), covering the midpoint \(N/(2X)\in[1/4,1/2]\); however this only ensures potential midpoint regions are admitted, not that any complementary prime pair exists.

The established PNT and partial summation give
\[
S_X(0)=\sum_p(\log p)w(p/X)=WX+o_w(X).
\tag{72.2}
\]

## 2. Theorem 72.1 — an unconditional positive POINTWISE central arc (PROVED)

For each \(X>1\) and integer \(N\), set \(J_X=[-1/(6X),1/(6X)]\subset\mathbb T\) (for X≥2), and define
\[
C_X(N)=\int_{J_X}S_X(\alpha)^2e(-N\alpha)\,d\alpha.
\tag{72.3}
\]
For EVERY \(N\in\mathbb Z\cap[X/2,X]\), whether or not a prime representation exists, \(C_X(N)\) is real and satisfies the **finite-X exact inequality**
\[
\boxed{\quad C_X(N)\ge\frac{2}{3\pi X}\,S_X(0)^2.\quad}
\tag{72.4}
\]
In particular, from (72.2), uniformly for all such N and sufficiently large X,
\[
\boxed{\quad C_X(N)\ge\frac{W^2}{6\pi}\,X>0.\quad}
\tag{72.5}
\]
**This is a lower bound on a signed restricted Fourier integral, NOT on its FULL-circle coefficient \(r_X(N)\).**

### Complete proof

Expand the square using the **actual fixed** nonnegative prime coefficients \(a_p=(\log p)w(p/X)\ge0\). Every contributing p satisfies \(0<p<X\). For \(N\in[X/2,X]\) and two contributing p,q,
\[
-X <p+q-N<\tfrac32X.
\]
For every real \(u\), with \(\operatorname{sinc}(v)=\sin(v)/v\) and sinc(0)=1,
\[
\int_{-1/(6X)}^{1/(6X)}e(u\alpha)d\alpha
=\frac{1}{3X}\operatorname{sinc}\!\left(\frac{\pi u}{3X}\right).
\]
Here \(|\pi u/(3X)|\le\pi/2\). Concavity of \(\sin t\) on \([0,\pi/2]\) gives \(\sin t\ge2t/\pi\), so \(\operatorname{sinc}(t)\ge2/\pi\) throughout \(|t|\le\pi/2\). Every summand in the expanded integral is thus nonnegative and at least \(2a_pa_q/(3\pi X)\). Summing p and q yields (72.4). Then \(S_X(0)\ge WX/2\) for all large X by (72.2), proving (72.5). Symmetry of J_X and real coefficients makes C_X(N) real. No single complementary prime pair at N is assumed.

The coefficient \(2/(3\pi X)\) is a simple sharp uniform bound given only the upper bound \(3X/2\) on \(|p+q-N|\) and the chosen sinc kernel; no claim is made that it is optimal among all possible arc widths or all compact supports.

### Corollary 72.1a — exact negative cancellation required by a missing target

Set
\[
E_X(N)=\int_{\mathbb T\setminus J_X}S_X(\alpha)^2e(-N\alpha)\,d\alpha.
\]
The complementary set is reflection-invariant, so E_X(N) is real. By exact Fourier inversion,
\[
\boxed{r_X(N)=C_X(N)+E_X(N).}\tag{72.6}
\]
Thus if \(r_X(N)=0\), necessarily
\[
\boxed{E_X(N)=-C_X(N)\le-\frac{W^2}{6\pi}X}\tag{72.7}
\]
uniformly for large X and \(N\in[X/2,X]\). Conversely, if one independently proves
\(E_X(N)>-W^2X/(6\pi)\), then \(r_X(N)>0\).

**MISSING:** there is NO such independently proven signed estimate for the complement for all residual N. It is essential that \(\mathbb T\setminus J_X\) contains other major arcs as well as conventional minor arcs; one must not label E_X simply 'minor arcs' or transfer a standard minor-only moment bound to it.

## 3. Theorem 72.2 — precise prime-power removal with one fewer logarithm (PROVED)

Define von Mangoldt \(\Lambda(n)=\log p\) if \(n=p^k\) for a genuine prime p and integer k≥1, and \(\Lambda(n)=0\) otherwise. Set
\[
T_X(\alpha)=\sum_{n\ge1}\Lambda(n)w(n/X)e(n\alpha),\quad
G_X(N)=\int_\mathbb T T_X(\alpha)^2 e(-N\alpha)\,d\alpha.
\]
For every \(X\ge4\) and integer N, the **deterministic, uniform** contamination inequality is
\[
\boxed{
0\le G_X(N)-r_X(N)
\le 2M^2\lfloor\sqrt X\rfloor(\log X)^2.}
\tag{72.8}
\]
In particular \(G_X(N)-r_X(N)=o_w(X)\) as \(X\to\infty\), without any unproved hypothesis about zeros of L-functions or twin/Goldbach primes. This sharpens the project Stage 69's earlier \(O_w(\sqrt X(\log X)^3)\) deterministic estimate by a factor of \(\log X\). The elementary idea is known in prime-power bookkeeping; no external novelty claim is made.

### Complete proof: group powers by the same prime base

Write \(Q_X=T_X-S_X\). Its coefficients are nonnegative, supported only on **proper** powers \(p^k,\ k\ge2\), with weights \((\log p)w(p^k/X)\). If such a power lies in the fixed support, then \(p^k<X\), hence \(p\le\lfloor\sqrt X\rfloor\). For each such p, letting \(K_p=\lfloor\log X/\log p\rfloor\),
\[
\sum_{\substack{k\ge2\\p^k\le X}}\log p
=(K_p-1)_+\log p\le \log X.
\]
Therefore
\[
\sum_{n\ge1}[Q_X]_n
\le M\sum_{p\le\sqrt X}\log X
\le M\lfloor\sqrt X\rfloor\log X.
\tag{72.9}
\]
Every coefficient of \(T_X\) is at most \(M\log X\). Expanding
\(T_X^2-S_X^2=2S_XQ_X+Q_X^2\), and counting the ordered pairs with at least one proper prime-power coordinate by a union bound (which may count both-proper pairs twice), gives
\[
0\le G_X(N)-r_X(N)
\le 2\sum_{\substack{n\ge1\\n=p^k,\ k\ge2}}
[Q_X]_n[T_X]_{N-n}
\le2M\log X\sum_{n\ge1}[Q_X]_n.
\]
Substitute (72.9) to obtain (72.8). All quantities are from genuine primes and their true proper powers. In particular, there is no assumption that \(r_X(N)\) is nonzero.

### Corollary 72.2b — a further logarithm saved by Chebyshev (PROVED with established theorem)

The classical **unconditional Chebyshev upper bound** \(\pi(y)\le C_{\rm Ch}y/\log y\) for all \(y\ge2\) gives, for \(X\ge16\),
\[
\sum_{n}[Q_X]_n
\le M\pi(\sqrt X)\log X
\le2C_{\rm Ch}M\sqrt X.
\tag{72.9b}
\]
Inserting this in the same precise pair union bound above yields
\[
\boxed{
0\le G_X(N)-r_X(N)
\le 4C_{\rm Ch}M^2\sqrt X\log X
=O_w(\sqrt X\log X)}
\tag{72.9c}
\]
**uniformly in every target N**, without assuming any Goldbach representation or any zero-free hypothesis. Here \(C_{\rm Ch}\) can be *any fixed rigorously admissible upper Chebyshev constant* for \(y\ge2\); we do not claim it to be numerically optimal. This improves the published Stage 69 \(O_w(\sqrt X\log^3X)\) accounting by **two logarithmic factors**. The simple explicit finite-X bound (72.8) remains valid independently of Chebyshev.

The underlying upper Chebyshev theorem is classical; consult Manuel Eberl's formalized elementary prime-bound treatment in the Isabelle AFP, https://isa-afp.org/browser_info/current/AFP/Prime_Distribution_Elementary/Elementary_Prime_Bounds.html . Its independent proof is an external input, not newly supplied here.

### Corollary 72.2a — a correct but unproved at-scale quantitative target certificate

For any N, if an independent theorem produces the strict lower bound
\[
G_X(N)>2M^2\lfloor\sqrt X\rfloor(\log X)^2,
\tag{72.10}
\]
then \(r_X(N)>0\) and a pair of genuine primes lies inside the chosen weight support. In particular, an independently proved uniform \(G_X(N)\ge cX\) with fixed c>0 would suffice for all sufficiently large residual targets in \([X/2,X]\).

**Not proved:** (72.10), nor \(G_X(N)\ge cX\), for each residual N. These are stronger quantitative arithmetic assertions than merely asserting Goldbach and cannot be imported from estimates valid only for *almost all* N.

## 4. A targeted adversarial test: positivity of the center is insensitive to sparse deletions

Stage 71 constructs, for each \(N\in H\cap[X/2,X]\), a polynomial \(S'_{X,N}\) from **a subset of genuine prime frequencies**, deleting only \(o(X)\) mass but removing all prime pairs for the target. Its retained mass satisfies \(S'_{X,N}(0)=WX+o_w(X)\) uniformly by the unconditional upper sieve of J. Wu and the classical PNT. The proof of T72.1 uses only nonnegative coefficients and support \((0,X)\), so it applies *verbatim* to \(S'_{X,N}\), showing
\[
\int_{J_X}(S'_{X,N})^2e(-N\alpha)d\alpha
\ge\frac{W^2}{6\pi}X,
\quad\text{even though}\quad
[(S'_{X,N})^2]_N=0.
\tag{72.11}
\]
The complementary integral for that modified model is necessarily **negative of this entire positive central contribution**. This is a concrete proof that **a large, target-uniform positive tiny major core, even for genuine-prime-supported coefficients, does not suffice when modified supports are permitted**. It is *not* a statement about failure of Goldbach for the **unmodified all-prime polynomial**.

## 5. Scientific assessment and what remains

- **PROVED (finite Fourier):** positivity C_X(N)≥(2/(3πX)) S_X(0)^2 for all N in range; exact missing-target cancellation.
- **PROVED (PNT input):** center C_X(N)≥(W²/(6π))X for all sufficiently large X, uniformly in N.
- **PROVED (elementary):** proper prime-power contamination is at most \(2M^2\lfloor\sqrt X\rfloor(\log X)^2=o(X)\), pointwise, and is in fact \(O_w(\sqrt X\log X)\) via the unconditional classical Chebyshev theorem.
- **CONDITIONAL certification only:** full binary von Mangoldt correlation above that error, or sufficiently weak negative signed complement E_X(N).
- **OPEN:** an unconditional, target-uniform estimate of E_X(N), G_X(N) or r_X(N) forcing a positive representation on H. **No solution to strong Goldbach.**

The genuinely difficult term is *the signed complementary prime interaction*, not the proper prime powers: the latter now have an explicit, negligible deterministic correction. These results do not repeat a global norm bound; they establish an exact **pointwise** central contribution, its possible complete cancellation and a strictly smaller pointwise \(\Lambda\)-to-prime correction.

### Sources

The classical prime number theorem and weighted partial summation are established inputs. For the parity barrier and necessity of signed/Type-II information, consult H. Iwaniec, *Prime Numbers and L-functions*, ICM 2006 plenary proceedings, pp. 279–306, https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM2006.1/ICM2006.1.ocr.pdf . For the distinction between exceptional-set and pointwise statements, see G. Bhowmik and L. Grimmelt, *The exceptional set of the Goldbach problem*, *Analysis Mathematica* 52 (2026), 767–808, https://doi.org/10.1007/s10476-026-00191-z . The latter's overview and explicit-major-arc discussion do **not** themselves establish a universal binary prime representation theorem. For related exact prime-power bound documentation, see https://prove2.me/theorems/f473c64c-a73e-4549-9a07-a81a0ec59082 (the claim was visible from external search; not independently verified in Lean here).

**Reproducibility:** finite exact surrogate-power convolutions and identity checks are stored in \`verify_stage72.js\` and \`exact_results.json\`. An exact integer check does not substitute for the universal analytic proof above.
