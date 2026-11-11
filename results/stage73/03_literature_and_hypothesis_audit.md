# Stage 73 — Primary-source and hypothesis audit

Checked on 2026-11-11. Relevant theorem statements and proof passages were read in the original author/publisher sources below; complete external proofs were not independently refereed. Download hashes, sizes and exact URLs are in `source_manifest.json`. PDFs are cached outside the repository under `/tmp/stage73-source-cache/`; that cache is temporary and may not persist. No quotation or citation is treated as a proof of an additional target estimate.

## Sources actually checked

1. **Terence Tao**, *Every odd number greater than 1 is the sum of at most five primes*, arXiv [1201.6656v4](https://arxiv.org/abs/1201.6656v4), version 2012-07-03; published *Mathematics of Computation* 83 (2014), 997–1038. Read [Lemma 4.11 and its proof, equation (4.18)](https://arxiv.org/html/1201.6656), and the adjacent parameter hypotheses. The algebraic identity in (4.18) is the identity rederived in 02. The lemma's optimized inequality assumes the test function is supported in $(V,UV^2)$. Our $U=V=X^{1/5}$ does **not** place the full binary support there; we use the unrestricted exact identity, not that inequality. Its exponential-sum applications have specified smoothing and approximation conditions, and are no theorem for the reflected $\Lambda(N-n)$ test function. The five-prime conclusion is a different additive problem.

2. **Jie Wu**, *Chen's double sieve, Goldbach's conjecture and the twin prime problem*, *Acta Arithmetica* 114(3) (2004), 215–273, [DOI 10.4064/aa114-3-2](https://doi.org/10.4064/aa114-3-2); original manuscript [arXiv:0705.1652v1](https://arxiv.org/pdf/0705.1652v1), uploaded 2007-05-11. Read definitions and Theorems 1–2. Theorem 1 is an unconditional upper bound $D(N)\le7.8209\Theta(N)$ for large even $N$, with $D$ ordered prime-pair count. Theorem 2 lower-bounds prime+$P_2$, not two primes. Only the upper-bound order and its displayed singular factor are used through Stages 70–71 to bound deletion mass. It does not establish a lower binary correlation. The manuscript's introductory parity discussion is context, not a proof of impossibility for all analytic methods.

3. **Terence Tao**, [*254A, Notes 3: The large sieve and the Bombieri–Vinogradov theorem*](https://terrytao.wordpress.com/2015/01/10/254a-notes-3-the-large-sieve-and-the-bombieri-vinogradov-theorem/), author exposition, 2015-01-10. Read Theorem 17 and the Vaughan proof discussion. This is an established-theorem exposition, not the original 1965 publication. It bounds a sum over moduli of maximal reduced-residue progression discrepancies by $O_A(x\log^{-A}x)$ when $Q\le x^{1/2}\log^{-B(A)}x$. It controls one prime variable averaged over moduli. It does not directly control the target-dependent Type II correlation in 02. Its printed discrepancy convention uses the mass coprime to the modulus divided by $\varphi(q)$; T73.5 bounds the omitted prime powers and the PNT centering error explicitly. The mesh argument in T73.5 derives the needed maximal-endpoint version in the restricted polynomial range from this statement and classical quantitative PNT. The coefficient bound there handles the logarithmic weights explicitly.

4. **Gautami Bhowmik and Lasse Grimmelt**, *The exceptional set of the Goldbach problem*, [DOI 10.1007/s10476-026-00191-z](https://doi.org/10.1007/s10476-026-00191-z), publisher online date 2026-09-23. The publisher record lists *Analysis Mathematica* 52, 767–808 (2026); the served PDF running header instead says 53. This metadata discrepancy is preserved here. Read PDF Theorem 3.1, Theorem 6.3 and surrounding definitions. Theorem 3.1 assumes a fixed all-Dirichlet zero bound $\Re\rho\le\Theta<3/4$ and gives $O_\epsilon(X^{2\Theta-1/2+\epsilon})$ exceptions. Theorem 6.3 is a major-arc **error** formula for even $N\in[X/2,X]$, $0<\epsilon<\vartheta<4/9-\epsilon$; it does not estimate the complete signed complement below the required threshold. The zero-pair sum remains to be controlled. No such zero hypothesis is adopted for T73.1–4.

**Concrete inherited transcription correction:** Theorem 6.3 equation (6.7), PDF page 30 (zero-index page 29), has an error term $O(Xe^{-cH}+X/\sqrt T+X^{1-\epsilon})$. Stage 69's `05_source_ledger.json` writes $X/T$. This is a source-transcription defect; the historical file is preserved and its stronger term is not used. The letter $H$ in that external error term is a zero-window parameter, unrelated to our residual set. The zero sum is never assumed small merely because it is explicit.

## External baseline and dependency discipline

Classical fixed-modulus PNT-AP, weighted partial summation, PNT and the Chebyshev prime-counting upper bound are established external theorems. Their proofs are not newly supplied here. Fixed-modulus PNT suffices for the new wheel asymptotic; no zero-free-half-plane conjecture, growing-modulus bound or 2026 preprint is needed. The project Stage 69 October/November preprint descriptions are inherited, not newly source-audited in this stage, and supply no accepted premise here. In particular no alleged external formal zero-free result is assumed or claimed compiled.

| Source/input | Exact role here | Missing implication |
|---|---|---|
| Fixed-modulus PNT-AP | Signed fixed-wheel main coefficient in 01 | Does not bound its full complement |
| Vaughan identity | Exact binary decomposition including boundaries | No target-uniform sign of Type II |
| Bombieri–Vinogradov | Locates a feasible Type I modulus scale | Type I errors closed in T73.5; reflected Type II remains |
| Wu upper sieve | Uniformly small deletion mass | Upper bound gives no positive pair |
| Prime+$P_2$ theorem | Identifies the sieve distinction | Almost prime may be composite |
| Conditional exceptional set | Quantifier comparison only | An allowed isolated target may remain |
| Explicit major-arc zero formula | Source audit only | Neither zero sum nor minor complement is controlled |

No freshly checked source supplies the required absolute signed remainder margin for every prescribed residual target. This is a scope conclusion about the statements inspected, not an exhaustive claim about every publication.
