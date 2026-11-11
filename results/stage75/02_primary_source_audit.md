# Stage 75 — Primary-source applicability audit

Audit: 11 November 2026. Only the passages named below were read; external proofs were not independently refereed in full. The targeted search is not an exhaustive claim about all literature. A correct theorem can fail this project's applicability test.

## A. Exceptional-zero input

Kaisa Matomäki and Jori Merikoski, *Siegel zeros, twin primes, Goldbach's conjecture, and primes in short intervals*, [arXiv:2112.11412v2](https://arxiv.org/pdf/2112.11412v2), revised 5 February 2022; IMRN 2023, 20337–20384 ([publisher](https://academic.oup.com/imrn/article/2023/23/20337/7111993)). Read Corollary 1.2 and Theorems 1.3–1.4, pp. 2–3; publisher metadata confirmed.

Theorem 1.4 assumes primitive quadratic $\chi\pmod q$, $q=2^rq'$ with $q'$ odd, and a real zero $\beta_0=1-(\eta\log q)^{-1}$, $\eta\ge10$. For integer $h\ge q^{10}$ and $V=\log h/\log q$, the unweighted ordered $\Lambda$ convolution is
$$h\mathfrak S(h)\left[1+\chi(-1)\mathbf1_{\varphi(2^r)\mid h}(-1)^{h/\varphi(2^r)}\prod_{p\mid q',p\nmid h}\frac{-1}{p-2}\right]+O_{C,\epsilon}\left(\frac{h^2}{\varphi(h)}\left[e^{-C\sqrt{V\log\eta}}+e^{-C(\log h)^{3/5-\epsilon}}+\frac{V\log^6\eta}{\eta}\right]\right),$$
for fixed $C\ge1$, $\epsilon>0$. There is no modulus averaging: conductor, zero and scale restrictions remain. Corollary 1.2 deduces zero exclusion from a Goldbach-count band, not the converse.

**Our independent applicability check:** if $q\mid h$, $h$ even and $\chi(-1)=-1$, the bracket is zero. The product is empty; $h/\varphi(2^r)$ is even (use even $h$ for $r=0$, and $2^r\mid h$ otherwise). This is a conditional degeneracy, not an exhibited exceptional character or a Goldbach counterexample. Omitting this correction cannot produce a positive uniform main term. Also, for fixed $q,\eta$, $V\log^6\eta/\eta$ does not tend to zero as $h\to\infty$. The unweighted total is not our prescribed smooth correlation without an additional transfer. Reject the unconditional application at the zero hypothesis before smoothing. This source genuinely addresses reflected correlations; it is not rejected by confusing them with plus shifts.

## B. Almost twin primes: actual summands but exceptions

Lasse Grimmelt and Joni Teräväinen, *The Exceptional Set in Goldbach's Problem with Almost Twin Primes*, [arXiv:2207.08805v1](https://arxiv.org/pdf/2207.08805v1), 6 July 2022. Read Theorems 1.1–1.2, p. 2, and the transfer discussion, pp. 4–5.

With $P_k$ denoting integers having at most $k$ prime factors, $E(Y,k_1,k_2)$ counts $m\le Y$, $m\equiv4\pmod6$, lacking $m=p_1+p_2$ with genuine primes $p_i$ and $p_i+2\in P_{k_i}$. Theorem 1.1 gives $E(Y,2,3)\ll Y^{1-\delta}$ for some effective $\delta>0$, effectively. Theorem 1.2 gives $E(Y,2,2)\ll_A Y\log^{-A}Y$ for each fixed $A>0$, ineffectively. These statements have no free modulus parameter. The transfer discussion retains exceptional targets; improved sieve levels do not remove them.

**Our independent check:** a bound on exceptional-set size permits a prescribed member; one residue family also does not cover all $H$. The first invalid step is “power-saving exceptions, therefore no exception at this target.” The summands ARE primes: rejecting this as only prime-plus-almost-prime would be incorrect. The additional almost-prime restrictions concern $p_i+2$. No signed smooth every-target lower margin follows from the inspected conclusions.

## C. Linear equations in primes: excluded reflected system

Benjamin Green and Terence Tao, *Linear equations in primes*, Annals of Mathematics 171 (2010), 1753–1850, [original journal PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p08-p.pdf). Read Definition 1.5, Examples 1, Lemma 1.6, Main Theorem and Corollary 1.7, pp. 1759–1763.

The main theorem as printed assumes GI$(s)$ and MN$(s)$ and treats fixed finite complexity at most $s$; the printed Corollary 1.7 is unconditional for complexity at most 2. Lemma 1.6 excludes affinely dependent pairs; Examples 1 explicitly identifies $(n,N-n)$ as infinite complexity. No error estimate for that excluded system, or growing-modulus uniformity for it, is provided. This records the original paper, not a claim that its finite-complexity dependencies remain unresolved today.

**Our independent check:** the linear parts $1,-1$ are proportional. In base-3 coordinates the pair becomes $3+2a,N-3-2a$ and remains reflected and dependent. Adding the target as a free variable may yield an average; restricting it back to every prescribed slice requires a new theorem. Resolving finite-complexity dependencies cannot remove this domain exclusion. Importing the conclusion to the binary slice is the first invalid implication.

## D. November 2026 polynomial exceptional sets

Ingo Althöfer, Dijia Chen, Alberto Perelli and János Pintz, *The exceptional set of Goldbach numbers among polynomial values*, [arXiv:2611.09386v1](https://arxiv.org/pdf/2611.09386v1), 6 November 2026. Read Theorem 1 and Section 2, pp. 2–5. This preprint is not independently certified here.

For a fixed integer polynomial $\phi$ of degree $k\ge2$ with positive leading coefficient, Theorem 1 bounds exceptional indices by $O_{\phi,\epsilon}(Y^{\alpha_k+\epsilon})$, for fixed $\epsilon>0$, $Y\ge2$: $\alpha_2=1/2$, $\alpha_3=5/8$, $\alpha_4=3/4$, and $\alpha_k=1-1/(k+1)$ otherwise. Here $\theta$ is the supremum of real parts of nontrivial zeros of all primitive Dirichlet L-functions, including zeta. Section 2 invokes the external assertion $\theta\le7/8$. Its route uses $\theta<11/12$, a fourth moment with $\kappa\in(4/9,9/20)$ and a major coefficient estimate for $\kappa<9/20$. That external zero-free claim is not verified or adopted here. Theorem 1 has no free AP modulus.

**Our independent check:** granting all external premises still leaves possible singleton exceptions. A new polynomial cannot be chosen for each target while silently retaining fixed-polynomial constants. Structured averaging does not supply the signed pointwise margin. The external dependency is recorded, not silently promoted to an unconditional input.

## E. Contemporary leads screened with explicit reading limits

Pham Van Khanh, *Uniformity, Local Structure and Boundary Correlations in Goldbach Representations*, [Preprints.org v1](https://www.preprints.org/manuscript/202610.3061), posted 30 October 2026, not peer reviewed. Read the abstract/status discussion, Proposition D.5 and Theorem G.2. D.5 expressly assumes its covariance estimate. G.2 assumes an actual-convolution band on a positive proportion of conductor multiples at $X=f^A$, fixed $A>5/2$, before excluding a real zero. Neither supplies the premise for this project. Other uninspected proofs are not certified.

Borros Arneth, *A Cubic Prime Minorant and the Remaining Correlation in Binary Goldbach*, [Zenodo v1](https://doi.org/10.5281/zenodo.23477014), 19 October 2026. Read the creator's description, not the PDF proof. It explicitly retains an unresolved long signed operator and gives conditional closure. This is a rejected lead at its advertised scope, not an independently audited theorem. Conditional closure is not established correlation input.

## Separate critical pass: acceptance matrix

A second logical pass by the same agent grants the named source result and checks whether it entails the required margin. This is not a proof-blind external review.

| Route | Actual primes or exact Lambda? | Every residual target and scale? | Signed sufficient margin supplied? | First failed application |
|---|---|---|---|---|
| A | Yes | No unconditional all-scale result | No | Zero premise, correction and error restrictions |
| B | Yes, genuine summands | No | No | Almost all replaced by every |
| C | Yes within its domain | Binary reflected system excluded | No | Infinite-complexity slice imported |
| D | Yes in a polynomial family | Exceptions remain | No | Exceptions and external zero dependency omitted |
| E | Actual-prime quantities appear | Required premise retained | No | Covariance/count band assumed |

These fail before any deletion-stability test could establish applicability. Failure to extend a theorem to modified prime subsets does not refute an actual-prime theorem. **No applicable independent input was found among the inspected results.** This is not an impossibility theorem about all literature or future arithmetic methods.
