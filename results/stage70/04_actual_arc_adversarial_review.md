# Stage 70 second-cycle adversarial review — independent scrutiny of the Fejér no-go

**Date:** 2026-11-10. **Scope:** Theorems 70.3–70.4 in \`03_actual_arc_cone_nogo.md\`. This is a separate conceptual audit using elementary Fourier algebra and classical PNT, not CoCalc Codex, Lean, or external mathematical refereeing.

## 1. Verify the spectral geometry without assuming any Goldbach case

- The major arcs are exactly the union of neighborhoods of **all** reduced q≤P rational centers with widths P/(qX). Their union contains the q=1 interval |alpha|≤P/X. **No disjointness assumption is required** for the measure upper bound.
- Reflection symmetry of the union ensures every \(\beta_{N+2j}(N)=\int_{\mathfrak M} e(2j\alpha)d\alpha\) is real. Without this symmetry the positive-part operation would be undefined, so this hypothesis cannot be omitted.
- With \(L=\lfloor X/(4P)\rfloor\), the q=1 interval contains \([-1/(4(L+1)),1/(4(L+1))]\). On that interval Fejér's kernel \(\mathcal F_L(2\alpha)\ge4(L+1)/\pi^2\) follows exactly from the sine bound; its mass is ≥2/π²>1/5. This statement is valid irrespective of all other rational arcs and of any prime coefficients.
- The central frequency contributes \(\beta_N=\nu\le1/10\), leaving a **positive weighted sum** of off-central coefficients greater than 1/10. The required \((\cdot)_+\) cannot be replaced by \(|\cdot|\) without changing the conclusion; Cauchy's use of \((\cdot)_+\) is correct and loses no sign information in the stated direction.
- The off-center \(N+2j\) are all inside the **predetermined** even band \(\{6,8,\ldots,2\lfloor X\rfloor\}\) for large X and N∈[X/2,X]. Importantly, this inclusion uses only arithmetic of the interval, **not any assumption that these even targets have prime representations**.
- Sum of triangular weights squared is \(Q_L=L(2L+1)/(3(L+1))\le2L\), so \(D_+>1/(100Q_L)\ge P/(50X)\). The looser 50 constant is unconditional for all sufficiently large X under \(\nu\le1/10\); no hidden \(N\)-dependent constants exist.

An equivalent proof in operator language uses the normalized vector \(L+1\) consecutive **even frequencies** and its squared Dirichlet polynomial as a positive test kernel. This yields the same spectral obstruction. It is a different interpretation of the same Fejér identity, **not** a claim of a materially independent new theorem.

## 2. Audit the prime-specific full-energy input

The weight \(w\in C_c^\infty((0,1))\) is fixed nonnegative with positive integral \(W\). Compact support away from zero implies \(w(2/X)=0\) eventually, so odd-prime contributions make the square spectrum even. The *classical PNT* plus weighted partial summation gives \(\sum_p(\log p)w(p/X)\sim WX\), hence \(S_w(0)\ge WX/2\) for large X.

For \(|\alpha|\le 1/(12X)\), all relevant p≤X have argument at most π/6, so \(\Re S_w(\alpha)\ge(\sqrt3/2)S_w(0)\). Integrating its fourth power over an interval of length 1/(6X) gives \(\int_{\mathbb T}|S_w|^4\ge3W^4X^3/512\). This is a **FULL-circle lower bound**. It cannot be replaced by or compared as if it were the Li–Liu conditional **MINOR-arc** upper bound.

The *actual major coefficient* satisfies
\[
|a_w(N)|\le\int_{\mathfrak M}|S_w|^2
\le\int_{\mathbb T}|S_w|^2
=\sum_p(\log p)^2w(p/X)^2
\le M_w^2X(\log X)^2.
\]
This does not presume its sign or that a representation exists. If the coefficient is nonpositive, the earlier positive-major hypothesis is unavailable; if positive, any certified \(A_X\le a_w(N)\) is bounded by this upper limit.

Combining \(B_{\rm true}\gg_wX^3\), \(D_+\gg P/X\) and \(|a|\ll_w X(\log X)^2\) yields
\[
\frac{B_{\rm true}D_+}{a^2}
\gg_w \frac{P}{(\log X)^4}\to\infty.
\]
This **cannot** establish or disprove \(r_w(N)>0\); it establishes that the sufficient inequality \(B_XD_+<A_X^2\) is not satisfiable even with optimal true budgets.

## 3. Attack the logical scope

**Would this remain true for the EXACT prime sumset rather than its broad even superset?** Not proved. Replacing K_X by the smaller exact \(\{p+q:a_pa_q>0\}\) may decrease \(D_+\), but determining whether N belongs to that set is itself the target existence question. A noncircular narrower predetermined band requires a theorem that excludes frequencies without using a representation of N as an input.

**What about factorization \(F=S_w^2\)?** Theorem 70.1 relaxes the coefficients \(r_w(k)\) to *independent* nonnegative variables; the Fejér extremal test says nothing about the nonlinear convolution constraints among r_w(k). The no-go is a proof-method obstruction for this relaxed criterion, not for factorized prime inputs.

**Could a conditional positive major theorem repair this?** No: the failure of the test is unconditional and compares its left side with the *actual* major coefficient upper bound, which is already larger than every valid positive lower budget. A stronger asymptotic for \(a_w(N)\) cannot reverse this specific inequality.

**Could the PNT input be removed?** The geometric D+ theorem is entirely elementary. The full fourth-moment lower bound uses the established PNT for fixed nonzero smooth weights; one may replace it with any independent \(\sum_pa_p\gg X\) estimate. The proof does **not** rely on the 2026 unverified external common zero-free theorem.

**Does 70.4 rule out all positive coefficient strategies?** Absolutely not. It rules out only the full-band, full-circle-energy **sufficient condition (70.4)** and direct attempts to improve its constants without new prime structure.

**Does the earlier half-mass pruning imply Goldbach can fail?** No: pruning deletes selected prime coefficients and is not the actual all-prime polynomial. The present theorem makes no such deletion; it uses only known positivity and PNT to show a relaxation is quantitatively too weak.

## 4. Exact independent parameter regression

The focused script \`verify_stage70_arc_nogo.py\` was independently executed with exact Python fractions for four increasing (X,P) pairs with \(2P^2/X=1/50\). It verifies the Fejér core inclusion, triangular-weight squared sum, even-band endpoint inclusion and \(1/(100Q_L)\ge P/(50X)\). This test **does not numerically integrate actual major arcs** and is not presented as numerical evidence for Goldbach. The all-X proof is Sections 1–2 of the theorem document.

## 5. Classification and next step

- **PROVED:** uniform \(D_+\ge P/(50X)\) via Fejér, for the standard major arcs and broad even band.
- **PROVED FROM ESTABLISHED EXTERNAL PNT:** true full-circle \(L^4\) energy \(\gg_w X^3\); unconditional comparison of the *actual* energy, geometry and major coefficient.
- **PROVED NO-GO FOR SPECIFIC TEST:** strict positive-cone energy certificate impossible eventually, even for exact true energy and actual major coefficient.
- **OPEN:** a target-uniform noncircular bound exploiting the exact *fixed-coefficient* factorization \(S_w^2\) or direct signed minor-arc cancellation; prime-pair existence on every residual target.
- **REFUTED UNSAFE INFERENCE:** using Li–Liu's conditional **minor-only** \(L^4\) upper bound as a full-circle energy upper bound, or claiming the cone is the full prime-square class.

**Decision:** stop trying to optimize the numerical constants of the full-band \(D_+\) cone certificate. Formulate a different prime-factorization-specific theorem whose hypotheses do not already assert a complementary prime pair.
