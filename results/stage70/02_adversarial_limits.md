# Stage 70 — adversarial audit: what the cone and pruning lemmas do NOT establish

**Date:** 2026-11-10. **Research state:** first mathematical cycle complete without Codex. **Goldbach: OPEN.**

## A. Claim T70.1: exact positivity-cone optimization

**Audit of both proofs.** On a reflection-symmetric major set \(M\), the Fourier coefficients \(\beta_k=\widehat{1_M}(N-k)\) are real. A nonnegative sequence \(c_k\ge0\) has major coefficient \(a=\sum c_k\beta_k\). For **a>0**, ignoring negative \(\beta_k\) yields \(a\le\langle c,\beta_+\rangle\le\|c\|_2\|\beta_+\|_2\). The equality vector is \(\beta_+\), so the cone extremizer and sharpness are rigorous. The independent KKT projection proof handles zero coordinates. If \(M\) is not reflection symmetric, the full major coefficient can be complex, and neither \(\beta_+\) nor the sign argument is defined: first pair reflected arcs and use the real part. If \(a<0\), instead use the *negative* part; a formula using the positive part for arbitrary sign would be false.

**Support and factorization caveat.** We fixed a frequency **superset** K consisting of possible even target sums; the precise actual prime sumset must not be presumed known by a Goldbach proof. The optimal cone coefficients \(c_k\) need not factor as \(\sum_{p+q=k}s_ps_q\) with \(s_p\ge0\). Thus the theorem is mathematically stronger than free complex Fourier energy bounds but strictly weaker as arithmetic input than controlling the actual \(S_w^2\). The finite \(\mathbb Z/12\mathbb Z\) example has exactly verified values \(D_+=1/9\) and \(D_{\rm free}=5/36\), but does **not** assert a Goldbach representation or a realizable continuous rational-arc model.

**Quantitative gap.** The criterion \(\bar B_X D_+<A_X^2\) is the exact hypothesis needed for this method. The previous Li–Liu conditional minor-arc fourth moment is **not** a full-circle \(\bar B_X\). Indeed, by the established prime number theorem, a genuine nontrivial nonnegative smooth weighted prime sum has full-circle fourth moment \(\gg_w X^3\). Any attempt to insert \(O(X^{5/2}\log^{100}X)\) as that full energy would be invalid. Nothing here establishes that the actual \(D_+\) on the published major arcs decays enough to make the criterion true.

## B. Claim T70.2: half-weight pruning of genuine prime frequencies

**Audit.** The complement graph has degree at most one, even if P includes primes outside the target range: an edge exists only when both endpoints are in P and sum to N. H rules out a self-edge because N/2 is composite. Selecting the heavier endpoint of each component and all isolated vertices preserves at least half the weight and deletes every edge. Monotonicity of coefficients of S² under nonnegative weight deletion implies its full fourth moment cannot increase. This proof is exact for *every finite* P and all N in H.

**The essential limitation:** P' is a subset of actual primes with coefficients that have been intentionally set to zero. It is **not** the fixed actual weighted polynomial, and there is no claim it still obeys the positive major-arc main term of Li–Liu (or any source theorem assuming all prime coefficients). A person who calls the pruned S' a counterexample to Goldbach commits a category error. Nevertheless, it rigorously rules out any claimed general theorem whose only premises are support contained in genuine primes, nonnegative bounded weights, total mass at least half of the full weight, and an upper bound on the *full-circle* fourth moment.

**Why a 50% mass floor alone cannot help:** the deletion operation is possible on any matching graph of reflected pairs, without knowing whether one pair exists. If the original prime set represents N, the modified coefficients can be chosen to destroy all its representations. Therefore any useful existence argument must exploit mandatory *nonzero* weights on specific complementary genuine-prime positions or a separate arithmetical uniformity property unavailable to the pruned class.

## C. Independent finite regression and provenance

The standard-library Python script \`results/stage70/verify_stage70.py\` was executed in a separate local runtime (not CoCalc); it and its exact output are byte-for-byte identified with the committed GitHub blobs:

- Script SHA-256: \`4de02e7b7ec374956702141693d751899569b5826e9a8b7374198250a03b561e\`; Git blob \`aa6be24d6bf6968e28c1dac3187c849c7f2ab7ed\`.
- JSON SHA-256: \`20521ee2123873cd5caaf9def67c0d29f943186577c0a70a17fe0b1a66acc691\`; Git blob \`87b16d30200907e039f8910019111367614b3991\`.

The script confirms the cyclic \(36/5\) vs \(9\) energy difference and, on P = odd primes ≤200, exact pruning at N=50,100,120,256,300. Each target belongs to H, all five **actual** full-support weighted coefficients are positive, and all five pruned coefficients are exactly zero while retained mass is at least half. All arithmetic in this script is integer or rational.

A finite test validates the implementation and formula edge cases; the universal proof is the matching argument above, not the test.

## D. Further optional checks and open obligations

1. Derive an **actual-arc** \(D_+(N;M,K_X)\) estimate for the fixed major-arc definition, correctly handling reflection, half-period, rational denominators and target-dependent Fourier phases. If its scale cannot make (70.4) strict, register a quantified no-go for this cone relaxation rather than optimizing it endlessly.
2. Investigate the nonlinear factorization cone \(c_k=\sum_{p+q=k}s_ps_q\), keeping fixed actual coefficients \(s_p=(\log p)w(p/X)\) separate from permitted variable deletions. A proof exploiting a positive lower bound on *all* fixed weights must avoid assuming there exists a complementary prime pair.
3. Compare any resulting quantitative condition to the exact and conditional external major-arc/fourth-moment theorems. Keep source hypotheses, norms and supports attached to every estimate.

**Verdict:** T70.1 and T70.2 are proved in their stated mathematical classes; they reveal a nontrivial cone saving and a complementary support/density obstruction. **Neither solves Goldbach.** The key open information is still the fixed-target simultaneous primality of \(p,N-p\) or an independently established signed prime-only Fourier estimate with a strict margin.
