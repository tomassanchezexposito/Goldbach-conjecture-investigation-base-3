# Stage 63 final report: exact structure, analytic bottleneck, and open coverage

## Executive finding

**Verdict: universal coverage remains OPEN.** Stage 63 proves exact finite and algebraic statements, audits several proposed positivity criteria, and establishes a useful *conditional* mean-square criterion. It proves neither the author's three-case conjecture nor strong Goldbach. No unconditional estimate found in the sources reviewed supplies the missing pointwise control at every residual target.

The original statement is preserved: for every even integer $N>2$, at least one of (i) $N=p+1$ for prime $p$, (ii) $N=2p$ for prime $p$, or (iii) $N=p+q$ for distinct primes $p<q$ with $N-2p=2q-N$ holds. The last equality is algebraically automatic from $p+q=N$; it does not add a primality fact. For

$$H=\{N\ge4:N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\},$$

the first two cases are unavailable, so the actual remaining obligation is $R(N)>0$ for every $N\in H$, where $R(N)=\#\{p<q:p,q\text{ prime},p+q=N\}$. This is still unproved.

## What Stage 63 established

### Exact arithmetic identities

**Proved in this research — shared-prime contraction (M1).** For distinct even targets $n<m$, the common-prime count $S_{n,m}$ is the number of integers $x$ with $2\le x\le\min(n-2,m-2)$, all of $x,n-x,m-x$ prime, and both diagonals excluded. Sorting each pair turns each admissible $x$ into exactly one representation at each target. Conversely a shared prime determines $x$ uniquely. Thus

$$R(n)R(m)=S_{n,m}+Q_4(n,m),$$

where $Q_4$ counts pairs of representations using four distinct prime positions. The range and diagonal restrictions are essential; residue products alone do not encode them.

**Proved in this research — exact wheel CRT factor (M1).** For squarefree $W=\prod_{\ell\in P}\ell$,

$$T_W(n,m)=\#\{x\pmod W:\gcd(x(n-x)(m-x),W)=1\}
=\prod_{\ell\mid W}(\ell-\nu_\ell(0,n,m)),$$

where $\nu_\ell$ counts distinct residues. This is the Chinese remainder theorem, not a prime-tuple theorem. At $W=210$ and even $n,m$, $T_{210}=0$ exactly when $n,m$ are $1,2$ modulo $3$ in either order. Even when the sieve factor is zero, genuine triples can survive because prime values equal to $3,5,7$ are permitted. The four-position product without coupling constraints is just $A_W(n)A_W(m)$, the product of existing per-target factors.

**Proved in this research — target-anchored Fourier coefficient (M2).** With $S_N(\alpha)=\sum_{p\le N}(\log p)e(p\alpha)$, exact orthogonality gives

$$\int_0^1 S_N(\alpha)^2e(-N\alpha)\,d\alpha
=2\sum_{p<q,\ p+q=N}\log p\log q
+\mathbf1_{N/2\text{ prime}}(\log(N/2))^2.$$

On $H$ the diagonal is absent, so positivity of the full coefficient is equivalent to $R(N)>0$. The integral identity is exact, but no lower bound for this coefficient has been proved. Explicit measurable major/minor arc sets were defined; to use them universally still requires an independent major-arc lower bound and a signed, target-uniform minor-arc bound that leaves a positive margin.

**Proved in this research — prime-power correction bound (M2).** If $C_\Lambda(N)=\sum_{a+b=N}\Lambda(a)\Lambda(b)$ is the ordered von Mangoldt convolution and $P_\Lambda(N)=\sum_{p+q=N}(\log p)(\log q)$ is its ordered prime-only part, then

$$0\le C_\Lambda(N)-P_\Lambda(N)
\le2\lfloor\log_2N\rfloor\lfloor\sqrt N\rfloor(\log N)^2.$$

The prime-only sum itself counts each distinct unordered pair twice and the prime diagonal once. On $H$, that diagonal is absent. Higher prime powers are not absent from $C_\Lambda$.

### Positivity criteria under adversarial checks

**Proved in this research — deterministic criteria; arithmetic inputs remain open (M3).** The positive-weight graph inequality

$$(x_j-w^Tx)^2\le((e_j-w)^TL^+(e_j-w))(x^TLx)$$

is sharp for a connected weighted graph. It implies coordinate positivity only when independent arithmetic bounds place the mean and energy on the required sides of the threshold. This recovers the Stage 59 type of criterion; it adds no prime-distribution estimate. Rescaling by the full singular-series profile changes coordinates but does not prove the actual normalized counts are near a positive constant.

The exact Stage 61 three-point quadratic certificate is nonpositive whenever its center count is zero. Its positive off-center correlation term alone cannot force a positive center: the exact abstract triples $(1,0,1),(1,0,2),(2,0,5)$ have positive off-center products while the certificate is $0,-1,-9$, respectively. These are logical countermodels, not prime data.

**Proved conditionally (M5).** Let $\mathfrak S(N)=2C_2\prod_{p\mid N,p>2}(p-1)/(p-2)$, with $C_2=\prod_{p>2}(1-(p-1)^{-2})>0$. For integer $X$ and even $N\in[X/2,X]$, define

$$\mathcal E(X)=\sum_{N\text{ even},\ X/2\le N\le X}|C_\Lambda(N)-N\mathfrak S(N)|^2.$$

If $D(X)=2\lfloor\log_2X\rfloor\lfloor\sqrt X\rfloor(\log X)^2$, then the exact implication proved in M5 is: if $D(X)\le C_2X/2$ and $\mathcal E(X)<C_2^2X^2/4$, there is no residual zero in that block. In particular, the stronger asymptotic hypothesis $\mathcal E(X)=o(X^2)$ would imply that every sufficiently large $N\in H$ has $R(N)>0$. The proof uses $\mathfrak S(N)\ge2C_2$ and the prime-power correction bound. The hypothesis is not proved. An abstract block with one zero and target profile $cN$ incurs energy at least $c^2X^2/4$, so an unrestricted $O(X^2)$ bound alone does not suffice for this argument.

## Literature and what its quantifiers provide

The source review is in `04_literature_and_implications.md`, with metadata and access status in `04_bibliography.json`.

- The unconditional Chudakov–van der Corput–Estermann almost-all result, Montgomery–Vaughan exceptional-set result, and Pintz's $|E(X)|<X^{0.72}$ result leave exceptional targets. For any fixed $N_0$, a set containing just $N_0$ satisfies such growing power-saving upper bounds for sufficiently large $X$; that observation demonstrates the quantifier gap, not an arithmetic exception.
- Bhowmik–Grimmelt's 2026 peer-reviewed paper was read for its hypotheses and proofs. Its conditional exceptional-set estimates and sparse Hardy–Littlewood implication are not an unconditional all-target theorem. In particular, Theorem 8.2 assumes a near-asymptotic on all but an allowed number of even multiples of an exceptional conductor at a specified scale and concludes a zero-free statement.
- Chen's theorem gives a prime plus a number with at most two prime factors, not necessarily a prime plus a prime. The original 1973 scan could not be read in this environment; this limitation is disclosed in the bibliography ledger.
- The reviewed minor-arc $L^2/L^4$ and large-sieve/Bombieri–Vinogradov estimates control averages or exceptional sets, not the required signed coefficient at each specified $N$.
- The published conditional mean-square estimate recorded from Bhowmik–Grimmelt is $\ll X^{3/2+2\Theta+\epsilon}$ under its stated zero-real-part hypothesis. At $\Theta=1/2$ its exponent is $5/2+\epsilon$, not the M5 $o(X^2)$ threshold. The reviewed theorem therefore does not prove the candidate hypothesis.

No result in the reviewed sources establishes $R(N)>0$ for every $N\in H$.

## Finite exact verification and its limits

The new independent M6 verifier uses two different primality procedures: a Sieve of Eratosthenes and trial division. They agree on unordered distinct prime-pair counts for every even $N\le1000$ and on the residual-set classification. On this finite range it finds 258 residual targets and no uncovered one. It separately checks direct residue enumeration against product formulas for 149 wheel targets and 1,225 distinct even target pairs for the shared-prime wheel count. The boundary checks report no distinct pair at $N=4,6$, and the pair $(3,5)$ at $N=8$; the prime diagonal is correctly excluded at 4 and 6. These are finite computational observations only.

The M1, M2, M3, and M5 exact verifiers separately check the CRT identities, integer finite-DFT coefficients, exact rational certificates, and the conditional block threshold. The repository's four unit tests and all focused Stage 63 verifiers were rerun for M6; commands and results are in `checkpoint_log.md`. Earlier Stage 56–62 verifier commands and outcomes are preserved in the M0 transcript. No large prime scan, installation, paid compute, or external service was used.

## Remaining proof obligations

1. Prove an unconditional pointwise positive lower bound for the prime-only target coefficient at every residual $N$, or an alternative theorem that directly forces $R(N)>0$.
2. For the circle-method route, establish a real major-arc lower bound and a signed minor-arc estimate uniform over every residual target, with explicit constants and finite cutoff. A positive formal singular series does not supply either bound.
3. For the M5 route, prove the dyadic estimate $\mathcal E(X)=o(X^2)$ (or a sufficiently small explicit block bound after the explicit prime-power correction). Neither the reviewed external results nor the finite experiments prove this.
4. Preserve exact small-prime and diagonal cases when translating between candidate counts, wheel factors, the prime-only polynomial, and the von Mangoldt convolution.
5. Any final universal theorem must retain the user's residual quantifier and original three cases; an average result, an asymptotic for almost all targets, or a finite computation is insufficient.

The full dependency register is in `theorems_and_dependencies.md`; refuted strategies and their first invalid steps are in `failed_approaches.md`. The next research task is specified in `next_objective.md` and replaces the completed Stage 63 task only on this branch.

## Publication and status

All Stage 63 milestones M0–M6 are recorded as checkpointed commits on `cocalc/stage63-extended-analytic-program`; see `checkpoint_log.md` for SHAs and verification commands. The final M6 source list and SHA-256 values are in `06_manifest.json`. The branch is intended for a draft review against `cocalc/stage62-singular-series-local-variation`; `main` is not modified or merged.

**Final mathematical status: OPEN.** The three-case conjecture's universal residual coverage has not been proved. No proof of strong Goldbach is claimed.
