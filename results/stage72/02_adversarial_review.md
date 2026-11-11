# Stage 72 — Adversarial mathematical review and failure-mode ledger

**Date:** 2026-11-11. **Scope:** \`01_pointwise_core_and_prime_power.md\` (T72.1–T72.2, improved Chebyshev corollary). **This is an internal independent argument audit, not external peer review or a formal Lean check.**

## A. Scope of the exact Fourier core

The input is the actual, nonnegative, *fixed* prime coefficient vector \(a_p=(\log p)w(p/X)\) with \(w\in C_c^\infty((0,1))\), \(w\ge0\), \(w\not\equiv0\). The compact support ensures \(0<p<X\), and classical PNT provides \(S_X(0)\sim WX\), \(W>0\). Neither of these statements asserts that \(N=p+q\) for a given N.

For \(X/2\le N\le X\), every pair of prime **frequencies**, whether or not its sum is N, has \(-X<p+q-N<3X/2\). On \(J_X=[-1/(6X),1/(6X)]\), the integrated phase is \((3X)^{-1}\mathrm{sinc}(\pi(p+q-N)/(3X))\ge 2/(3\pi X)\). Integrating the finite double sum term by term is exact. The lower bound \(C_X(N)\ge2S_X(0)^2/(3\pi X)\) is correct and universal for this class of nonnegative frequency weights. The final \(W^2X/(6\pi)\) constant follows by using the classical PNT-derived \(S_X(0)\ge WX/2\) at large X.

The crucial logical trap is visible immediately: the proof works just as well when **every** pair sum is different from N! The positivity of \(C_X(N)\) is a statement about a short signed Fourier integral, not about the N-th full-circle coefficient. A hypothetical zero therefore requires the complementary signed term to equal \(-C_X(N)\); this equality provides a quantitative *necessary* cancellation but does not rule out that cancellation.

**Countermodel:** Stage 71's true-prime-*subset* polynomial \(S'_{X,N}\), constructed by deleting at most one endpoint from each N-complementary matching edge, has \([S'^2]_N=0\), yet (from the unconditional Wu upper sieve theorem and weighted PNT) its mass remains \(WX+o_w(X)\). The same proof shows \(C'_X(N)\gg_wX\). Its complement is **exactly** \(-C'_X(N)\). This is a rigorous model-level counterexample to concluding Goldbach from a positive short core. It is not a counterexample for all true primes, because S' has altered coefficients.

**Support condition:** choosing \(w>0\) on \([1/5,3/5]\) covers the midpoint interval \(N/(2X)\in[1/4,1/2]\). This makes eligible potential central pairs but does not force a prime in either position. For arbitrary smooth w, \(r_X(N)\) may vanish because its support omits all prime pairs even if Goldbach holds at N.

## B. Audit the von Mangoldt / genuine-prime distinction

\(\Lambda(n)=\log p\) for \(n=p^k\), and 0 otherwise; its *proper* prime powers are k≥2. Thus \(T_X=S_X+Q_X\) with nonnegative Fourier coefficients. The ordered coefficient \(G_X(N)-r_X(N)\) is nonnegative and is bounded by counting ordered pairs with at least one coordinate from Q. Each such pair is counted at least once by the two symmetric terms of the union bound \(2\sum Q(n)T(N-n)\); there is no unaccounted diagonal exception.

The exact key inequality for each genuine prime p is
\[
\sum_{\substack{k\ge2\\p^k\le X}}\log p
\le\left\lfloor\frac{\log X}{\log p}\right\rfloor\log p
\le\log X.
\]
There are at most \(\lfloor\sqrt X\rfloor\) possible prime bases. Therefore \(\sum_n[Q_X]_n\le M\sqrt X\log X\) and \(G_X(N)-r_X(N)\le2M^2\sqrt X(\log X)^2\), pointwise for all N. This initial finite-X upper bound requires no external prime distribution theorem.

The **classical Chebyshev bound** \(\pi(y)\le C_{\rm Ch}y/\log y\) then improves the number of possible bases. Since \(\log\sqrt X=\frac12\log X\), for X≥16,
\[
\sum_n[Q_X]_n
\le M(\log X)\pi(\sqrt X)
\le2C_{\rm Ch}M\sqrt X,
\quad
G_X(N)-r_X(N)\le4C_{\rm Ch}M^2\sqrt X\log X.
\]
The stated improvement is thus **not** a conjecture or a numerical extrapolation. The Chebyshev bound is an established external theorem. All constants are independent of N, and the theorem is true even when N is not residual or N has no representation.

### Critical dimension and notation checks

- \(r_X(N)\) is the ordered genuine-prime *weighted* coefficient, not the unordered integer R(N). For N∈H every genuine unordered pair appears twice.
- \(G_X(N)\) is the **von Mangoldt** coefficient, not a count of genuine prime pairs. A positive G alone can arise exclusively from proper prime powers.
- For X≥16 the Chebyshev bound is asymptotic/with an unspecified proven constant \(C_{\rm Ch}\); do not present \(4C_{\rm Ch}\) as an optimized numerical constant.
- A condition \(G_X(N)>4C_{\rm Ch}M^2\sqrt X\log X\) would imply \(r_X(N)>0\); **no such target-uniform lower bound was proved**.
- The smaller \(O(\sqrt X\log X)\) contamination estimate does not by itself improve a missing lower bound for the full \(\Lambda*\Lambda\) coefficient.
- No assertion of special new zero-free L-function bounds, parity-violating sieve estimates or universal Goldbach follows.

## C. Exact computational audit

\`verify_stage72.py\` was actually run using Python 3.13.5 with exact \`fractions.Fraction\`. It checked **122 even target inputs** across X=90,150,240, comparing pair-list direct convolution with reflected dictionary convolution, nonnegativity and pointwise proper-power union bound, and exact removal of every N-edge in a finite prime-support matching. The outputs are in \`exact_results.json\`.

The regression deliberately uses a **rational polynomial surrogate** \(w_X(n)=(n/X)(1-n/X)\) and **unit coefficients** for prime and prime-power terms, rather than the smooth fixed w and logarithmic coefficients of the analytic theorem. Its purpose is to test the exact algebra/implementation, not the actual Chebyshev asymptotic, the sharp logarithmic correction nor the sinc analytic integral. The original theorem is proved by the analytic inequalities, not by these finite checks.

The local \`git hash-object\` of executed source and output matched the GitHub blob SHAs, and SHA-256 hashes were recorded separately. No SageMath/Codex kernel was used.

## D. Incomplete routes and precise next lemma

**Route A:** A complete *signed* estimate for the full genuine-prime complement integral \(E_X(N)=\int_{\mathbb T\setminus J_X}S_X^2e(-N\alpha)d\alpha\) with lower bound strictly above \(-W^2X/(6\pi)\), **uniformly for every prescribed N in H∩[X/2,X]**, would imply a pair. This is not supplied by unsigned L4 or average exceptional-set theorems. The complement includes other major arcs; calling it merely minor arcs is wrong.

**Route B:** An unconditional lower bound \(G_X(N)>4C_{\rm Ch}M^2\sqrt X\log X\) on the **actual von Mangoldt** convolution for each prescribed residual N would imply a genuine-prime pair. Existing average results may have sparse exceptional N. Proving this threshold uniformly remains unavailable and can be as difficult as the Goldbach problem.

**First unproved implication:** from \(C_X(N)\gg X\) and proper-power error \(o(X)\) to \(r_X(N)>0\). These facts alone leave \(E_X(N)\) uncontrolled in sign and allow full cancellation. Neither lemma bypasses the prime-correlation/parity obstruction.

### Evidence classification

- T72.1 central-core bound: **PROVED elementary Fourier**, plus **established PNT** for uniform asymptotic positive order.
- T72.2 finite-X prime-power correction: **PROVED elementary**.
- Improved \(\sqrt X\log X\) correction: **PROVED deduction from established Chebyshev prime-counting estimate**.
- 122 examples: **FINITE exact checks**, not arithmetic asymptotic.
- Signed remainder and a sufficient uniform binary \(\Lambda\)-correlation bound: **OPEN**.
- Universal coverage on H: **OPEN**.

**Outcome:** the deterministic prime-power error is now demonstrably negligible at scale X. The remaining issue is the sign of the fixed genuine-prime complementary correlation; extra positive core mass alone is not the missing step.
