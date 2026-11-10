# Stage 69 M5 — Source-to-implication audit of recent Goldbach estimates

**Status:** source statements below were checked against the cited v1 arXiv PDFs and the Springer publisher record on 2026-11-10. The three arXiv items are preprints, not represented here as peer-reviewed. No conclusion below is unconditional pointwise binary Goldbach.

## 1. Li–Liu: fourth moment and exceptional sets

H. Li and Z. Liu, *Fourth moments of prime exponential sums and exceptional sets for sums and differences of primes*, arXiv:2610.26756v1 (submitted 2026-10-19), [abstract and version record](https://arxiv.org/abs/2610.26756v1), [PDF](https://arxiv.org/pdf/2610.26756v1).

Their hypothesis $Q_\Theta$ places every nontrivial zero of every primitive Dirichlet $L$-function, including the zeta function, in $\Re s\leq\Theta$, for one fixed $1/2\leq\Theta<1$. Their Theorem 1 assumes $\Theta<11/12$ and chooses a fixed $\kappa=\kappa(\Theta)$ in $(4/9,9/20)$. For the paper's specified smooth Gevrey weight $w\in C_c^\infty((0,1))$, $0\leq w\leq1$, equal to one on $[1/8,7/8]$, and $P=X^\kappa$, it proves

$$\int_{\mathfrak m(X^\kappa)}|S_w(\alpha)|^4\,d\alpha\ll_{w,\Theta} X^{5/2}(\log X)^{100}.$$

This is a minor-arc fourth moment, under the common zero hypothesis; its implied constant is not an explicit numerical constant. Their Theorem 2 gives exceptional-set bounds of order $O_\Theta(N^{1/2}(\log N)^{100})$ for the sum and difference problems. A set of this size can contain an isolated target. The moment is not a uniform signed estimate for $\int_{\mathfrak m}S_w^2e(-N\alpha)d\alpha$.

In Proposition 4.1, under $Q_\Theta$ for a fixed $\Theta<1$ and a fixed $\kappa<9/20$, their major-arc coefficient is uniformly asymptotic for even $n\in[X/2,X]$ to the singular-series main term, with an $O(X^{1-c})$ error for a positive $c$ depending on the fixed parameters. This is separate from the minor fourth moment and does not make its target coefficient pointwise positive.

## 2. Pintz–Althöfer: exceptional-set exponents

J. Pintz and I. Althöfer, *The Goldbach exceptional set: an exponent 7/12 and conditional refinement*, arXiv:2610.15559v1 (submitted 2026-10-11), [version record](https://arxiv.org/abs/2610.15559v1), [PDF](https://arxiv.org/pdf/2610.15559v1).

Their fixed hypothesis $H_{\theta_0}$ places zeros of all primitive Dirichlet $L$-functions, including zeta, in $\Re s\leq\theta_0$. Theorem 1 gives an exceptional-set estimate $\ll_{\theta_0,\epsilon}X^{7/12+\epsilon}$ for fixed $\theta_0<1$. Theorem 3 gives, under $H_\theta$ with fixed $\theta\leq2/3$, the exponent

$$g(\theta)+\epsilon,\qquad g(\theta)=2\theta-\frac32+\frac{3(1-\theta)}{2-\theta}=\frac{\theta(5-4\theta)}{2(2-\theta)}.$$

At $\theta=5/8$, this is $25/44+\epsilon$. These are still exceptional-set estimates, not the assertion that every even target is represented. The paper cites the 2026 OpenAI/Lean result at zero boundary $7/8$ as an external input; it does not supply an independent verification of that source. The paper itself states that its proof has not been formally verified in Lean. We therefore record its claims as preprint theorems conditional on their stated assumptions and proof, not as a separately machine-checked result.

## 3. Althöfer–Chen–Perelli–Pintz: polynomial-indexed targets

I. Althöfer, D. Chen, A. Perelli and J. Pintz, *The exceptional set of Goldbach numbers among polynomial values*, arXiv:2611.09386v1 (submitted 2026-11-06), [version record](https://arxiv.org/abs/2611.09386v1), [PDF](https://arxiv.org/pdf/2611.09386v1).

Theorem 1 treats a fixed polynomial $\phi\in\mathbb Z[x]$ with positive leading coefficient and degree $k\geq2$. For its polynomial-indexed exceptional count $E_{k,\phi}(N)$, it states $E_{k,\phi}(N)\ll_{\phi,\epsilon}N^{\alpha_k+\epsilon}$, where $\alpha_2=1/2$, $\alpha_3=5/8$, $\alpha_4=3/4$, and $\alpha_k=1-1/(k+1)$ for $k>4$. The theorem excludes degree one and leaves a positive-power exceptional set on each covered polynomial sequence. A bound on the number of exceptions does not show that a particular $N\in H$ is not an exception. Its proof uses the Li–Liu estimates and the paper's cited external zero-free input; those dependencies remain dependencies, not additional unconditional results.

## 4. Bhowmik–Grimmelt: journal survey and conditional result

G. Bhowmik and L. Grimmelt, *The exceptional set of the Goldbach problem*, *Analysis Mathematica* 52(3) (2026), 767–808, DOI [10.1007/s10476-026-00191-z](https://doi.org/10.1007/s10476-026-00191-z), first published online 2026-09-23. The metadata and publication status were checked at the [Springer article record](https://link.springer.com/article/10.1007/s10476-026-00191-z); publisher PDF: [link](https://link.springer.com/content/pdf/10.1007/s10476-026-00191-z.pdf).

The new explicit formula is Theorem 6.3, which reproduces Pintz's major-arc-error formula from the cited works [20, Theorem A] and [21, Theorem 1]. For $0<\epsilon<\vartheta<4/9-\epsilon$ and $R=X^\vartheta$, and every even $N\in[X/2,X]$, it expresses the major-arc error $E_M(N)$ as a sum over pairs $(\rho_1,\chi_1),(\rho_2,\chi_2)$ in the paper's exceptional set $\mathcal E$:

$$E_M(N)=\sum_{(\rho_1,\chi_1),(\rho_2,\chi_2)\in\mathcal E}S(\chi_1,\chi_2,N)\frac{\Gamma(\rho_1)\Gamma(\rho_2)}{\Gamma(\rho_1+\rho_2)}N^{\rho_1+\rho_2-1}+O\!\left(Xe^{-cH}+\frac XT+X^{1-\epsilon}\right).$$

The generalized singular series satisfies $|S(\chi_1,\chi_2,N)|\leq\mathfrak S(N)$ and is small unless the two conductors divide a bounded multiple of $N$ and the product character has small conductor, as specified in (6.4)–(6.6). This is a zero-explicit formula, not a Hardy–Littlewood asymptotic for the complete representation count. Its target range is uniform, but the zero sum is not shown uniformly small for every target; the paper uses it in an exceptional-set argument. Theorem 3.1 assumes every zero of every Dirichlet $L$-function satisfies $\Re\rho\leq\Theta$ for a fixed $\Theta<3/4$, and concludes, for every $\epsilon>0$, $|E(X)|\ll_\epsilon X^{2\Theta-1/2+\epsilon}$. This is a strong, fixed zero-free hypothesis and still permits exceptions. The Hardy–Littlewood full main term is not asserted as an unconditional pointwise theorem.

## 5. Alleged common zero-free half-plane and formal verification scope

The cited downstream papers refer to a 2026 OpenAI Math manuscript/Lean development giving a common zero-free boundary $7/8$ for primitive Dirichlet $L$-functions. We did not locate a directly identified, independently retrievable source file and compiled Lean project from the exact citations available in the checked papers. One cited commit identifier is not enough to establish repository identity, theorem statement, hypotheses, or successful compilation. Accordingly, this project does **not** claim to have verified that external formal result. Any downstream theorem using it retains it as an explicit external premise. In particular, formal verification of a cited zero-free theorem would not by itself formally verify the downstream analytic argument.

## 6. Classical baselines and what they do not provide here

The classical results have different quantifiers and objects: Vinogradov's ternary theorem concerns three prime summands; Chen's theorem gives sufficiently large even integers as a prime plus an integer with at most two prime factors (with the usual theorem's technical conventions), not two primes; Bombieri–Vinogradov controls an average of prime-distribution errors over moduli up to a sub-square-root range, not the correlation $\sum_p1_{\mathbb P}(p)1_{\mathbb P}(N-p)$ at a prescribed $N$. Vaughan's and Heath-Brown's identities are decompositions of a von Mangoldt sum into Type I/II (and related) sums; they do not alone establish a target-uniform binary correlation. These standard statements are included only to delimit scope and are not used as a substitute for a fully specified source-level derivation in this project.

## 7. Translation to the Stage 69 coefficient

For $S_w(\alpha)=\sum_p(\log p)w(p/X)e(p\alpha)$, the coefficient of $S_w^2$ is the ordered weighted prime-pair count

$$r_w(n)=\sum_{p+q=n}(\log p)(\log q)w(p/X)w(q/X).$$

Writing $S_w^2$ (not $|S_w|^2$) preserves the sum constraint. For even $n>4$, a prime 2 cannot occur in a two-prime representation; prime 3 remains a possible endpoint contribution. On $H$, $n/2$ is composite, so the diagonal $p=q=n/2$ is absent. The circle-method decomposition $r_w(n)=a_w(n)+m_w(n)$ is exact for the selected major/minor partition. If $r_w(n)=0$, then $m_w(n)=-a_w(n)$, but the source fourth moment only bounds an average square of such coefficients and allows a single exceptional target. None of the source theorems supplies the signed, pointwise, genuine-prime estimate needed to exclude that possibility.

## 8. Local source integrity

The source PDFs used for this audit were saved outside the repository under `/tmp/stage69_sources`; SHA-256 values and retrieval metadata are in `05_source_ledger.json`. This avoids adding source binaries to the research branch. The downloaded versions, theorem numbers and status are recorded there. The source audit is a translation and scope check, not an independent proof of the papers' analytic theorems.
