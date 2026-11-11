# Stage 71 — Independent adversarial review and first missing arithmetic input

**Date:** 2026-11-11. **Provenance:** separate mathematical scrutiny by ChatGPT with independently executed exact Python calculations, not CoCalc/Codex and not external peer review.  
**Core review:** \`01_exact_target_robustness_and_lp.md\` and \`verify_stage71.py\`.  
**Verdict:** exact combinatorial and global Fourier statements are valid for their specified model classes; neither gives universal prime-pair positivity.

## A. Attack the exact matching optimization

**First possible pitfall — shared endpoint.** Could a prime p occur in two N-complementary edges? No: its only possible neighbor is N-p. On H the diagonal p=N/2 cannot be prime. Thus all edges are vertex-disjoint. Without the diagonal exclusion the graph contains a possible loop and the one-endpoint-per-edge formulation would need modification.

**Second pitfall — fractional deletion on both endpoints.** For one edge of initial weights A≥B, total cost t≤B and deletion x from A, t−x from B, the residual product is concave in x. Its minimum is attained at an endpoint, and deleting t from B yields no larger product than deleting t from A. For t>B the product can already be zero at lower cost B. Therefore it is not legitimate to assume every split is optimal; the proof explicitly rules out interior splits. With several edges the benefit per unit cost is exactly the complementary *larger* weight A_i, so an exchange proof or linear-programming duality certifies the descending-A greedy solution.

**Third pitfall — budget meaning.** T71.1(b) minimizes the remaining coefficient over *all* nonnegative attenuations \(0\le b_p\le a_p\) with cost ≤η. If the support is fixed and coefficient values are not allowed to change (actual prime weights), the feasible perturbation set is a singleton. This optimization gives a robustness threshold for **modified models**, not a new lower bound for actual R(N).

**Fourth pitfall — zero versus tiny weights.** The missing-target condition \(r_b(N)=0\) is exact. Since all terms are nonnegative, each edge must have a zeroed endpoint. A small positive endpoint does not erase its edge. For smooth weights w supported on (0,1), the fixed-weight matching can be empty even when N possesses prime representations outside the weight support; conversely \(r_w(N)>0\) is a genuine prime-pair witness. Any unconditional assertion that the matching is nonempty for each N is precisely the unresolved arithmetic content.

**Equality and exact norm tests.** The \(\ell^s\)-distance formula follows from the matching hitting-set property for every \(1\le s<\infty\); \(\ell^\infty\) is the maximum lighter endpoint. An independent integer dynamic program allowing arbitrary splits on both endpoints agrees with the greedy formula at all 15 integer budgets for three unequal edges (including the zero case), and provides a genuinely different check from the exchange proof. The universal theorem is the proof, not these 15 finite cases.

## B. Attack the global \(L^q\) near-invisibility result

**External input status.** Wu's Theorem 1, published in *Acta Arithmetica* 114(3), 215–273 (2004), DOI 10.4064/aa114-3-2, is an **unconditional UPPER sieve** for the ordered Goldbach representation count \(D(N)\); it provides no existence lower bound. The theorem text \(D(N)\le7.8209\,\Theta(N)\) was confirmed from the accessible original manuscript text and publisher listing. The proof of Wu's article is NOT newly reproduced or independently refereed here. Classical PNT yields \(S(0)\sim WX\) and \(\|S\|_2^2\sim X\log X\int w^2\), and classical \(N/\varphi(N)\ll\log\log N\) supplies the worst-case uniform singular-factor estimate.

**Deleted norms and exact Fourier support.** On H, no p=q diagonal exists and p=2 cannot contribute for even N>4. For sufficiently large X the fixed compact support of w excludes p=2 anyway. The deleted coefficient vector has \(\ell^1=O_w(X\log\log X/\log X)\) and squared \(\ell^2=O_w(X\log\log X)\), uniformly in N. Consequently \(\|\Delta\|_\infty\) is bounded by its coefficient \(\ell^1\), while \(\|\Delta\|_2^2\) is exactly its squared coefficient \(\ell^2\), **not** the same norm.

**Interpolation proof audit.** For q≥2,
\[
\|\Delta\|_q\le\|\Delta\|_\infty^{1-2/q}\|\Delta\|_2^{2/q}.
\]
For fixed 2<q<∞, this is \(O_{q,w}(X^{1-1/q}(\log\log X)^{1-1/q}/(\log X)^{1-2/q})\). The positive real part of the full weighted prime polynomial on a q=1 neighborhood of length 1/(6X) proves \(\|S\|_q\gg_{q,w}X^{1-1/q}\). For q=2, this latter bound is too weak: the stronger weighted PNT \(\|S\|_2^2\sim X\log X\int w^2\) is correctly used instead. The resulting ratios really tend to zero for every **fixed** q, including infinity. No uniformity in q depending on X has been claimed.

**Square-polynomial proof audit.** The identity \(S^2-(S')^2=(S-S')(S+S')\) and Hölder give the asserted relative \(L^r\) convergence for each fixed r≥1. The r=2 case is separately confirmed by discrete convolution Young's inequality
\[
\sum_k(d*d)_k^2\le(\sum_p d_p)^2\sum_p d_p^2.
\]
The exact regression checked the nonnegativity of all coefficient differences and the monotonicity of the full fourth moment after deletion. This is consistent with the theoretical factorization.

## C. Crucial absolute-versus-relative counterargument

Although
\[
\frac{\|S^2-(S')^2\|_2}{\|S^2\|_2}=o(1),
\]
the actual full square has \(\|S^2\|_2\gg_wX^{3/2}\). The relative error is only bounded by \(O_w((\log\log X)^{3/4}/\sqrt{\log X})\), **not** \(o(X^{-1/2})\), which is the rough relative scale needed to force an \(o(X)\) bound from this inequality at a specified Fourier coefficient. The loss of a single coefficient of expected scale X is therefore compatible with excellent global relative approximation. This does not claim that the actual coefficient is always ∼X: that would need the very Goldbach asymptotic under investigation.

An even simpler sufficient but currently unmet perturbation condition would be
\[
\|\Delta\|_2=o\left(\sqrt{X/\log X}\right),
\]
because \(|r_a(N)-r_b(N)|\le\|\Delta\|_2(\|S\|_2+\|S'\|_2)\) by Cauchy, and \(\|S\|_2\asymp_w\sqrt{X\log X}\). The actual deletion construction only guarantees \(\|\Delta\|_2=O_w(\sqrt{X\log\log X})\), weaker by a growing factor of \(\sqrt{\log X\log\log X}\) at the upper-bound level. This is a **sufficient stability threshold**, not a theorem about the actual size of any one Goldbach coefficient.

**Exact target sensitivity** is \((r_a-r_b)(N)=2\sum_{\{p,q\}\in\mathcal E_N}(a_pd_q+a_qd_p-d_pd_q)\). It depends on the **reflection interaction** \(a_{N-p}\), not merely on the total deleted mass. A hypothesis on this interaction that already assumes some complementary prime is circular unless its arithmetic proof is independent.

## D. Independent exact run and strict provenance

A separate local Python 3.13.5 environment ran \`results/stage71/verify_stage71.py\` (verified byte-for-byte against the committed GitHub blob), including 15 integer budgets on the independent three-edge dynamic-programming example and five actual *finite prime support* target calculations, with N=50,100,120,256,300 all explicitly checked to lie in H. Weighted exact convolution confirms zero target coefficient after deletion, the exact minimum mass cost, and the Young L4 inequality. Output \`results/stage71/exact_results.json\` is also byte-matched to the actual executed output by Git SHA-1 and SHA-256. **No large prime scans were performed** and these finite tests are not the theorem's universal proof.

## E. Next mathematical direction: what can defeat a targeted deletion?

- A statistic requiring the **exact fixed genuine-prime coefficients** at all supported primes, with a signed **target-local** estimate strong enough to distinguish S from S', might work.
- First-order PNT-AP and global Fourier \(L^q\) relative closeness are not sufficient for the broadened modified-support model; the Stage 70 logarithmic modulus caveat remains.
- Growing-modulus estimates, dispersion, or Type I/II bilinear decompositions must be shown to yield an **absolute** error smaller than the target's positive main term for every residual N, not merely a global mean or exceptional count. The sieve parity barrier must be treated, not renamed.
- An estimate that directly asserts \(\tau_N>0\) for the complete all-prime support is equivalent to Goldbach on H and needs an independent argument. Current bounds in this project do not provide it.

**Adversarial verdict:** T71.1–T71.2 are correct and precise for the stated classes; their norm obstruction is not an arithmetic counterexample; the exact missing theorem remains a target-uniform, non-circular signed prime-correlation input. This review is not peer-reviewed publication.
