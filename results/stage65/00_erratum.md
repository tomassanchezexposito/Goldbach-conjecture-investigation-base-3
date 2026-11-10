# Stage 65 erratum: prime-sum versus prime-difference Fourier coefficients

**Classification:** rigorous algebraic correction of the inherited Stage 64 report. No new Goldbach positivity theorem is claimed.

## First invalid step in the earlier Stage 64 text

The previous report correctly defined
\[
S_w(\alpha)=\sum_{p}(\log p)w(p/X)e(p\alpha),\qquad
r_w(N)=\int_0^1 S_w(\alpha)^2e(-N\alpha)\,d\alpha,
\]
but **incorrectly** defined the major- and minor-arc integrals of \(|S_w(\alpha)|^2\) and asserted their sum was \(r_w(N)\).

For arbitrary real coefficients \(a_p\), set \(S(\alpha)=\sum_pa_pe(p\alpha)\). Multiplication gives
\[
S(\alpha)^2=\sum_{p,q}a_pa_qe((p+q)\alpha),\qquad
|S(\alpha)|^2=\sum_{p,q}a_pa_qe((p-q)\alpha).
\]
Therefore their \(N\)-th Fourier coefficients count weighted **sums** and weighted **differences**, respectively. They are not interchangeable.

Concrete exact counterexample:
\[
S=e(3\alpha)+e(5\alpha),\qquad
\widehat{S^2}(8)=2,\quad
\widehat{|S|^2}(8)=0.
\]
Indeed \(S^2=e(6\alpha)+2e(8\alpha)+e(10\alpha)\), whereas
\(|S|^2=2+e(2\alpha)+e(-2\alpha)\).

## Correct Fourier and Parseval framework

For a measurable disjoint major/minor partition \(\mathfrak M\cup\mathfrak m=[0,1)\), define
\[
a_w(N)=\int_{\mathfrak M}S_w(\alpha)^2e(-N\alpha)\,d\alpha,\qquad
m_w(N)=\int_{\mathfrak m}S_w(\alpha)^2e(-N\alpha)\,d\alpha.
\]
Then **exactly**
\[
r_w(N)=a_w(N)+m_w(N).
\]
For real prime weights and a partition symmetric under \(\alpha\mapsto-\alpha\), each coefficient is real; if the arc sets are not reflection symmetric, use real parts when formulating signed lower bounds.

The fourth-moment identity remains unchanged:
\[
\sum_{N\in\mathbb Z}|m_w(N)|^2
=\int_{\mathfrak m}|S_w(\alpha)^2|^2\,d\alpha
=\int_{\mathfrak m}|S_w(\alpha)|^4\,d\alpha.
\]
Thus the general conclusion that a bound \(\ll X^{5/2}(\log X)^{100}\) cannot by itself rule out a single coefficient of size \(\asymp X\) **survives the correction**. The earlier uncorrected definitions, however, cannot be cited as a valid proof.

For even \(N>4\), no distinct prime representation contains 2: \(N-2>2\) is even. At \(N=4\), the diagonal 2+2 is excluded from the representation count. On the residual set \(\mathcal H\), the equal-prime diagonal is excluded because \(N/2\) is composite.

## Implementation test and provenance

- \`results/stage65/tests/verify_sum_difference.py\` verifies all cyclic Fourier coefficients by **two exact methods**: direct sum/difference convolution and a finite-field DFT with a primitive 16th root modulo 97.
- The regression explicitly checks the frequency \(N=8\) and the \(S^2\) versus \(|S|^2\) distinction.
- The inherited Stage 64 source is corrected only in **the new Stage 65 branch**; historical Stage 64 commits and PR #13 are preserved.
- Re-run Stage 64 and Stage 63 verifiers before adopting the revised analysis. Record exact output and hash values.

**Remaining open mathematics:** establish an independent target-uniform bound on the *signed genuine-prime minor-arc coefficient*, or another non-circular arithmetical result implying a positive prime-pair count at every residual target.
