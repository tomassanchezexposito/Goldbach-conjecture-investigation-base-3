# Stage 66 — Sharp local modulus-to-global-energy obstruction

**Classification:** a fully proved sharp deterministic theorem and a conditional arithmetic application. **No** unconditional pointwise prime-pair lower bound is asserted. The original three-case statement remains open.

## 1. Definitions and the pointwise challenge

Retain the Stage 65 **corrected** Fourier coefficient
\[
m_w(n)=\int_{\mathfrak m}S_w(\alpha)^2e(-n\alpha)\,d\alpha,
\quad S_w(\alpha)=\sum_p(\log p)w(p/X)e(p\alpha).
\]
Do **not** replace \(S_w^2\) by \(|S_w|^2\), which would encode differences of primes.

When a valid major-arc theorem independently guarantees \(a_w(N)\ge A>0\) and a target \(N\in H\) had no genuine prime pair, the exact ordered-prime sum would be zero, so
\(m_w(N)=-a_w(N)\), whence \(|m_w(N)|\ge A\).
The major-arc assertion may rely on an explicitly labeled external uniform zero-free hypothesis; it is not taken as unconditional.

The available conditional global fourth-moment input has the form
\[
\sum_{n\in\mathbb Z}|m_w(n)|^2\le B_X,\qquad
B_X=C_4X^{5/2}(\log X)^{100}.
\]
On its own, this is far larger than \(A^2\asymp X^2\) and allows a single bad coefficient.

## 2. Theorem 66.1 — optimal local modulus energy (PROVED)

Let \(I\subset\mathbb Z\setminus\{0\}\) be any finite set of distinct shifts, and let \(d_h\ge0\) be specified bounds for \(h\in I\). Consider an arbitrary complex coefficient sequence \(c:\mathbb Z\to\mathbb C\) of finite \(\ell^2\) norm satisfying, at some integer \(N\),
\[
|c(N)|\ge A>0,\qquad
|c(N+h)-c(N)|\le d_h \quad(h\in I).
\]
Then the **sharp inequality**
\[
\boxed{\sum_{n\in\mathbb Z}|c(n)|^2
\ge A^2+\sum_{h\in I}(A-d_h)_+^2},
\qquad (x)_+=\max(x,0),
\]
holds.

**Proof.** By the reverse triangle inequality,
\[
|c(N+h)|\ge \big(|c(N)|-|c(N+h)-c(N)|\big)_+
\ge (A-d_h)_+.
\]
The center and all \(N+h\) with \(h\in I\) are pairwise distinct. Sum their squared magnitudes, dropping all remaining nonnegative contributions.

**Sharpness in the stated arbitrary-sequence class.** Set
\[
c(N)=-A,\quad c(N+h)=-(A-d_h)_+\ (h\in I),
\quad c(n)=0\ \text{at all other indices}.
\]
Then every constraint is satisfied: for \(d_h\le A\) the difference has magnitude \(d_h\), and for \(d_h>A\) the difference has magnitude \(A\le d_h\). Equality holds. This exact construction is **not** a possible or proven coefficient sequence of primes; it establishes the best inference from the stated abstract input alone.

**Necessary and sufficient consistency criterion in this abstract class:** for \(B\ge0\), there exists an \(\ell^2\) sequence satisfying all the constraints and \(\sum|c(n)|^2\le B\) if and only if
\[
B\ge A^2+\sum_{h\in I}(A-d_h)_+^2.
\]
The forward implication is the inequality above; the reverse follows from its exact extremizer. Hence a strict inequality in the opposite direction rules out a center of magnitude \(A\) using only this global energy and the independently supplied modulus bounds.

## 3. Corollary 66.2 — even-step Lipschitz modulus (PROVED, conditional to apply)

For arbitrary complex \(\ell^2\) coefficients, suppose
\[
|c(N+2h)-c(N)|\le L|h|\quad (1\le|h|\le H),
\quad |c(N)|\ge A>0
\]
with \(H\ge0\), \(L\ge0\), integer. Then
\[
\boxed{B\ge A^2+2\sum_{h=1}^H(A-Lh)_+^2}
\]
is **necessary** if \(B\) is a global upper bound for the coefficient-square sum. It is also sharp for the *abstract* finite-shift constraints. The increments use **even shifts \(2h\)** to compare like-parity targets and avoid silently mixing even Goldbach targets with odd prime-sum targets.

If \(L>0\), set
\[
J=\min\big(H,\max(0,\lceil A/L\rceil-1)\big).
\]
Elementary sums give the exact bound
\[
B\ge A^2+
2\left[
JA^2-ALJ(J+1)
+\frac{L^2J(J+1)(2J+1)}6
\right].
\]
When \(L=0\), the right side is simply \((2H+1)A^2\). For \(H\ge\lceil A/L\rceil\) and \(A/L\to\infty\), the right side is
\[
\frac{2A^3}{3L}+O(A^2+AL)
\]
(with an absolute implied constant). This shows the scale: if \(A\asymp cX\) and \(B_X\asymp C_4X^{5/2}(\log X)^{100}\), one would need a **proved** even-step modulus around
\[
L\lesssim \frac{2c^3}{3C_4}\,
X^{1/2}(\log X)^{-100}
\]
with strictly sufficient numerical margin, provided the even-shift range has \(H\gtrsim A/L\). This is a **necessary scale for this abstract energy contradiction**, not an established bound on genuine prime correlations.

If \(L\) is defined per unit integer displacement rather than per even step, replace \(L\) above by \(2L\). The distinction matters.

## 4. Conditional arithmetic conclusion (NOT established universally)

Assume an independently valid major-arc lower bound \(a_w(N)\ge A_X>0\) for each relevant residual \(N\), the externally specified fourth-moment/global coefficient energy bound \(B_X\), and independently proven **genuine-prime** signed-minor coefficient increments
\[
|m_w(N+2h)-m_w(N)|\le d_{X,N}(h)
\quad(1\le|h|\le H).
\]
If for every such target the numerical inequality
\[
\boxed{
A_X^2+2\sum_{h=1}^H(A_X-d_{X,N}(h))_+^2>B_X
}
\]
is verified from independent quantitative estimates, then no target \(N\in H\) can have a missing genuine distinct-prime pair. The conclusion is non-circular *as a logical implication*: its premises never use \(R(N)>0\) as an assumption.

**Open arithmetic gap:** the required increment estimates for genuine prime-only minor-arc coefficients are NOT established by the global fourth moment, the wheel 210, the singular-series model, or prior Stage 56–65 local correlations. The inequality is a deterministic tool that exposes the missing arithmetic input; it does not prove that input.

## 5. Numerical checks and adversarial test plan

The independently executable exact Python verifier \`results/stage66/verify_stage66.py\` checks the formula at rational parameters, constructs the exact extremizer, tests both even and odd shift sets, and exercises small edge cases \(H=0\), \(L=0\), \(A\le L\), and \(A/L\in\mathbb Z\). It uses only integer and rational arithmetic. A second SageMath or standalone path should verify selected distinct parameter cases before accepting a CoCalc research report.

**Distinct from Stage 65:** the theorem proves the exact *minimum global energy* at a fixed-magnitude center under a chosen arbitrary local modulus, and thus a sharp necessary-and-sufficient abstract consistency criterion. It neither assumes nor derives a prime-pair representation. The proof does not imply the existence of a good prime-only shift modulus.

## 6. Highest-priority Stage 66 research obligation

Study whether the true-prime **even-step signed increments** \(m_w(N+2h)-m_w(N)\) admit an independently proved uniform bound sharp enough to force the theorem's energy contradiction. Investigate the arithmetic singular-series variation, the parity structure, and exact Fourier multiplier \(e(-2h\alpha)-1\). Check each attempted bound for missing signs, the use of \(S_w^2\) rather than \(|S_w|^2\), target uniformity and dependence on any assumed representation of \(N\).

If such a bound is inaccessible, document the **first missing estimate** precisely and compare with the Fejér conditional criterion from Stage 65. Do not extend finite Goldbach tests without a new falsifiable lemma. Prior reports remain untouched.
