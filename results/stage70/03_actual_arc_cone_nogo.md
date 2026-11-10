# Stage 70 second cycle — Fejér lower bound and an unconditional no-go for the full-energy positive-spectrum certificate

**Date:** 2026-11-10. **Provenance:** separate ChatGPT mathematical derivation, without CoCalc/Codex execution.  
**Status:** theorems **PROVED** using elementary Fourier analysis and the classical prime number theorem (PNT, external established input); independent reproducibility check pending/recorded separately. **Goldbach on the author's residual H remains OPEN.**

## 0. The actual Stage 70 criterion to evaluate

For an even target N in the residual set H, a prime-only polynomial
\[
S_w(\alpha)=\sum_{p\ {\rm genuine\ prime}}(\log p)w(p/X)e(p\alpha),\quad e(t)=e^{2\pi it},
\]
has square \(F_w(\alpha)=S_w(\alpha)^2=\sum_k r_w(k)e(k\alpha)\), \(r_w(k)\ge0\). The original case and position definitions are unchanged.

Fix a standard real, nonnegative, nonzero \(w\in C_c^\infty((0,1))\), and \(0<\kappa<1/2\), \(P=X^\kappa\). Define the standard Hardy–Littlewood major set (mod 1)
\[
\mathfrak M(X)=\bigcup_{1\le q\le \lfloor P\rfloor}\ 
\bigcup_{\substack{0\le a<q\\(a,q)=1}}
\left\{\alpha\in\mathbb T:\|\alpha-a/q\|_{\mathbb T}\le P/(qX)\right\}.
\]
It is measurable, invariant under \(\alpha\mapsto-\alpha\), and contains the \(q=1\) core \(\{|\alpha|\le P/X\}\) for X sufficiently large. Its measure \(\nu\) satisfies
\[
\nu=|\mathfrak M|\le\frac{2P}{X}\sum_{q\le P}\frac{\varphi(q)}q
\le\frac{2P^2}{X}=o(1).
\tag{70.8}
\]
There is no need to assume intervals are disjoint; the union bound suffices.

Because the fixed weight has compact support away from zero, there is an X_0(w) such that \(w(2/X)=0\) for every X≥X_0(w). Thus only **odd** genuine primes contribute to \(S_w\) on the asymptotic range of this theorem, and every nonzero square coefficient has even frequency. This is an exact support fact, not an assumption that any particular even target has a representation.\n\nUse a **predetermined entire even-frequency superset**
\[
K_X=\{k\in2\mathbb Z:6\le k\le2\lfloor X\rfloor\}
\]
of all possible odd-prime sums with both primes \(\le X\). This does **not** infer which even k actually have a prime-pair representation. For each even \(N\in[X/2,X]\), define
\[
\beta_k(N)=\int_{\mathfrak M}e((k-N)\alpha)d\alpha\in\mathbb R,\quad
D_+(N)=\sum_{k\in K_X\setminus\{N\}}(\beta_k(N))_+^2,\quad
t_+=\max(t,0).
\]
The earlier proved Theorem 70.1 says that if a positive **actual** major coefficient \(a_w(N)>0\) is known, a full-circle fourth-moment **upper** budget \(B_X\ge\int_{\mathbb T}|S_w|^4\), and a positive major **lower** budget \(0<A_X\le a_w(N)\), then \(B_XD_+(N)<A_X^2\) would imply a genuine prime pair at N. The present theorem shows that this strict inequality can **never** hold eventually under this broad superset and major-arc setup, whatever valid upper/lower budgets one chooses.

## 1. Theorem 70.3 — a universal uniform lower bound on the cone geometric constant (PROVED)

Assume
\[
X\text{ sufficiently large},\qquad L=\left\lfloor\frac{X}{4P}\right\rfloor\ge1,\qquad
N\in2\mathbb Z\cap[X/2,X],\qquad 2P^2/X\le 1/10.
\]
Then \(\{N+2j:-L\le j\le L\}\subset K_X\), and
\[
\boxed{D_+(N)\ge\frac{P}{50X}.}\tag{70.9}
\]
The constant is intentionally conservative, and the lower bound is uniform in N, even without assuming N belongs to H.

### Complete proof using a positivity kernel

Define the normalized Fejér kernel
\[
\mathcal F_L(t)=\frac1{L+1}\left|\sum_{r=0}^{L}e(rt)\right|^2
=\sum_{j=-L}^{L}\left(1-\frac{|j|}{L+1}\right)e(jt)
=\frac1{L+1}\left(\frac{\sin\pi(L+1)t}{\sin\pi t}\right)^2.
\]
It is nonnegative everywhere. For \(|t|\le1/(2(L+1))\), the inequalities
\(\sin u\ge2u/\pi\) for \(0\le u\le\pi/2\) and \(|\sin\pi t|\le\pi|t|\) imply
\[
\mathcal F_L(t)\ge\frac{4(L+1)}{\pi^2}.
\tag{70.10}
\]
This remains valid at t=0 by continuity.

Since \(L+1>X/(4P)\), the interval
\(I=[-1/(4(L+1)),1/(4(L+1))]\) lies inside the \(q=1\) major core \(|\alpha|\le P/X\). Applying (70.10) to \(t=2\alpha\) and integrating only over I,
\[
\int_{\mathfrak M}\mathcal F_L(2\alpha)\,d\alpha
\ge\int_I\mathcal F_L(2\alpha)\,d\alpha
\ge\frac1{2(L+1)}\,\frac{4(L+1)}{\pi^2}
=\frac2{\pi^2}>\frac15.
\tag{70.11}
\]
By Fourier expansion, reflection symmetry and the definition of \(\beta\),
\[
\int_{\mathfrak M}\mathcal F_L(2\alpha)d\alpha
=\nu+\sum_{1\le|j|\le L}
\left(1-\frac{|j|}{L+1}\right)\beta_{N+2j}(N).
\]
Write \(\omega_j=1-|j|/(L+1)\in[0,1]\). Because \(\nu\le1/10\), the sum of the noncentral terms is greater than \(1/10\); dropping their negative parts only increases it:
\[
\sum_{1\le|j|\le L}\omega_j(\beta_{N+2j})_+>\frac1{10}.
\tag{70.12}
\]
Cauchy–Schwarz and the fact that all these frequency indices belong to \(K_X\setminus\{N\}\) give
\[
\frac1{100}<
\left(\sum_{1\le|j|\le L}\omega_j^2\right)
\left(\sum_{1\le|j|\le L}(\beta_{N+2j})_+^2\right)
\le 2L\,D_+(N).
\]
Since \(L\le X/(4P)\), we conclude
\[
D_+(N)>\frac1{200L}\ge\frac{P}{50X}.
\]
The weaker nonstrict displayed form (70.9) follows. The proof requires only a **single q=1 major core**, reflection symmetry and a broad predetermined even frequency band. No theorem about simultaneous primality is used.

### Independent interpretation

The Fejér kernel is the square of a short geometric sum,
\(\mathcal F_L(2\alpha)=\frac1{L+1}|\sum_{r=0}^Le(2r\alpha)|^2\).
Its integral over the q=1 core stays bounded away from zero. Therefore it forces positive Fourier mass across **approximately X/P nearby even frequencies**. Cauchy turns that nonzero positive mass into the \(P/X\) lower bound for the squared positive-part sum. A Fourier-set refinement, not a prime-distribution claim.

## 2. Theorem 70.4 — the positive-spectrum FULL-circle certificate is asymptotically impossible (PROVED using classical PNT)

Let \(w\in C_c^\infty((0,1))\) be a fixed real nonnegative function not identically zero, put \(W=\int_0^1w(t)dt>0\) and \(M_w=\|w\|_\infty>0\), and keep the major arcs and K_X from Section 0 with fixed \(0<\kappa<1/2\).

For all sufficiently large X and **every even** \(N\in[X/2,X]\), the following unconditional estimates hold:
\[
\boxed{
\begin{aligned}
D_+(N)&\ge P/(50X),\\
B_{\rm true}(X):=\int_\mathbb T|S_w(\alpha)|^4d\alpha
 &\ge (3W^4/512)\,X^3,\\
|a_w(N)|:=\left|\int_{\mathfrak M}S_w(\alpha)^2e(-N\alpha)d\alpha\right|
 &\le M_w^2 X(\log X)^2.
\end{aligned}}
\tag{70.13}
\]
Consequently
\[
\boxed{
\frac{B_{\rm true}(X)\,D_+(N)}{|a_w(N)|^2}
\ge \frac{3W^4}{25600M_w^4}\,
\frac{P}{(\log X)^4}
\longrightarrow+\infty
}
\tag{70.14}
\]
whenever \(a_w(N)\ne0\); if \(a_w(N)=0\), no positive major lower budget is available in the first place. The divergence is uniform in even N in the range. In particular, for **every** valid global-energy upper bound \(B_X\ge B_{\rm true}\) and **every** valid positive major lower bound \(A_X\le a_w(N)\), eventually
\[
\boxed{B_X D_+(N)>A_X^2,}\tag{70.15}
\]
which is the exact *opposite* of the earlier sufficient cone certificate (70.4). This proves that **no improvement in how accurately one estimates the same full-circle B_X, and no optimization of its constants, can make (70.4) certify a single target at large X** for these particular arcs and predetermined full even band.

### Proof: lower bound for the true full-circle energy

The **classical prime number theorem** for \(\vartheta(x)=\sum_{p\le x}\log p\sim x\), followed by weighted partial summation for fixed continuous compactly supported w, yields
\[
S_w(0)=\sum_p(\log p)w(p/X)\sim WX.
\]
For large enough X, \(S_w(0)\ge WX/2\).

Because w is supported on \((0,1)\), all contributing primes satisfy p≤X. For \(|\alpha|\le1/(12X)\), the angles satisfy \(|2\pi p\alpha|\le\pi/6\); since every weight is nonnegative,
\[
\Re S_w(\alpha)\ge(\sqrt3/2)S_w(0).
\]
The interval length is \(1/(6X)\), so
\[
\int_{\mathbb T}|S_w|^4d\alpha
\ge\frac1{6X}\left(\frac{\sqrt3}{2}S_w(0)\right)^4
=\frac{3S_w(0)^4}{32X}
\ge \frac{3W^4}{512}X^3.
\]
This is standard PNT-based full-circle energy concentration at \(\alpha=0\); it is **not** the conditional fourth-moment theorem about the *minor arcs* quoted by Li–Liu.

### Proof: unconditional upper bound on the major coefficient

By triangle inequality, \(|S_w^2|=|S_w|^2\), and Parseval for \(S_w\),
\[
|a_w(N)|\le\int_{\mathfrak M}|S_w|^2
\le\int_{\mathbb T}|S_w|^2
=\sum_p(\log p)^2w(p/X)^2
\le M_w^2\,\lfloor X\rfloor(\log X)^2
\le M_w^2 X(\log X)^2.
\]
Combine this with (70.9) and the preceding lower bound. Since \(P=X^\kappa\) dominates \((\log X)^4\) for every fixed \(\kappa>0\), (70.14) and (70.15) follow.

### Logical strength and sharp scope

- **PROVED NO-GO:** the *specific sufficient test* \(B_XD_+(N)<A_X^2\), based on full-circle fourth moment and positivity of **arbitrary nonnegative square-spectrum coefficients in the predetermined full even band**, is uniformly impossible asymptotically. This is stronger than merely failing to prove the test using currently available estimates: it fails even with **the exact actual** full-circle B and major a.
- **NOT REFUTED:** the existence of a strictly better inequality exploiting \(F_w=S_w^2\) with **all its fixed actual prime coefficients**, local signed cancellation, or a norm constrained to a narrower support using independently proved information. Our geometric cone is a relaxation, and its sharpness extremizer need not factor as a prime-square polynomial.
- **NOT A COUNTEREXAMPLE TO GOLDBACH:** N may in fact have many genuine prime representations. We have shown only a particular Fourier proof certificate is too coarse to detect them.
- **No circular sumset:** K_X contains all possible sums, regardless of whether a given N is represented; no target pair was chosen.

## 3. What is genuinely missing after this no-go

The broad nonnegative spectrum already yields an exact cone improvement over unrestricted complex Fourier coefficients (Theorem 70.1), but the Fejér lower bound forces its geometric denominator D_+ to be too large by a factor at least \(P/(\log X)^4\) against the **true** full-circle fourth moment.

A useful next lemma must use information absent from the relaxed cone, for example:

1. **Fixed true-prime factorization:** the coefficients \(r_w(k)\) satisfy \(r_w(k)=\sum_{p+q=k}a_pa_q\) with **fixed positive \(a_p=(\log p)w(p/X)\)** for every genuine prime p in the prescribed support, not arbitrary nonnegative \(r_w(k)\). Stage 70's matching-pruning countermodel shows why being *allowed* at prime frequencies, while permitted to delete up to half the total weight, cannot be enough.
2. **Target-signed cancellation:** a new independently proved estimate of the actual \(\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)d\alpha\), with sign and uniformity in each residual N, or a comparably strong true-prime shift-correlation estimate.
3. **Source-level precise comparison:** any future claim must compare to major-arc and exceptional-set theorems with their actual zero-free assumptions. An \(L^4\) minor moment or a positive-power exceptional-set bound alone cannot prevent one zero target.

**Recommended next research question:** derive a nonlinear, *prime-factorization-specific* variational inequality, instead of further optimizing or repeating the full-even-band positive-spectrum denominator. The latter is now rigorously ruled out as a path to universal coverage via certificate (70.4).

## 4. Reproducibility and literature provenance

The elementary Fejér identity used in (70.10) follows from a finite geometric sum and also appears in Gressman's UPenn Fourier notes at https://www2.math.upenn.edu/~gressman/analysis/08b-summability.html and NIST DLMF https://dlmf.nist.gov/1.15. The PNT input \(\sum_{p\le x}\log p\sim x\) is an established classical theorem; see https://alexkontorovich.github.io/PrimeNumberTheoremAnd/blueprint/corollaries-chapter.html for a documented PNT-related source. These are **external background theorems**, not original claimed prime-distribution results.

Focused independent exact parameter checks in \`verify_stage70_arc_nogo.py\` test the algebraic window/measure and frequency-band conditions. They do not replace the all-X analytic proof. No Codex process was launched, no full Goldbach sweeps were executed, and previous research branches remain unmodified.

**Final evidence classification:** T70.3 **PROVED elemental Fourier**; T70.4 **PROVED from classical PNT and elementary Fourier**; novel status only *within this research program* pending an external mathematical novelty audit; Goldbach coverage **OPEN**.
