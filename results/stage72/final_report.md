# Stage 72 — Final mathematical report: pointwise central Fourier positivity and true-prime-power separation

**Research date:** 2026-11-11. **Branch:** \`cocalc/stage72-pointwise-prime-power-core\` derived from Stage 71, PR #20.  
**Execution:** direct ChatGPT mathematical proofs, literature comparison and 122 focused exact local Python checks. **No CoCalc, Codex, paid runtime, or scheduled process.**  
**Scientific status:** new internally verified *elementary deductions*, no assertion of mathematical novelty in the literature, no peer review or Lean formal proof. **Strong Goldbach on the residual domain is OPEN.**

## 1. The unchanged target

For each even integer N define
\[
H=\{N\ge4:N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\},\qquad
R(N)=\#\{p<q:p,q\text{ genuine primes},\,p+q=N\}.
\]
The original three alternatives are prime-plus-one, twice a prime, or two **distinct** primes. For N∈H only the third remains. The positional relation \(p=3+2a\), \(q=3+2b\), \(a+b=N/2-3\), is an exact reparametrization of the sum, **not** an arithmetic theorem forcing two prime positions.

## 2. Theorems closed in this cycle

### T72.1 (PROVED: target-uniform strictly positive central Fourier core)

For a fixed nonzero \(w\ge0\) in \(C_c^\infty((0,1))\), define
\[
S_X(\alpha)=\sum_{p\ {\rm genuine\ prime}}(\log p)w(p/X)e(p\alpha),
\qquad W=\int_0^1w(t)\,dt>0,\quad J_X=[-1/(6X),1/(6X)].
\]
The elementary sinc identity and \(|p+q-N|<3X/2\) prove **exactly**
\[
C_X(N):=\int_{J_X}S_X(\alpha)^2e(-N\alpha)d\alpha
\ge\frac2{3\pi X}S_X(0)^2.
\]
Using the **classical PNT** \(S_X(0)\sim WX\), for every sufficiently large X and every integer N∈[X/2,X], in particular residual even N,
\[
\boxed{C_X(N)\ge W^2 X/(6\pi)>0.}
\]
No Goldbach pair is selected or assumed. This is a **positive restricted integral**, not a bound on its full Fourier coefficient. If \(r_X(N)=\sum_{p+q=N}(\log p)(\log q)w(p/X)w(q/X)=0\), then the exact complementary signed integral \(E_X(N)=\int_{\mathbb T\setminus J_X}S_X^2e(-N\alpha)\) must be \(-C_X(N)\le-W^2X/(6\pi)\). Its sign has **not** been bounded for the actual complete prime polynomial.

Stage 71's deliberate target-specific sparse deletion preserves total mass \(WX+o(X)\) and thus this positive core **but eliminates the target coefficient** in the *modified* model. This furnishes an exact method-level counterexample to mistaking positive tiny-core mass for Goldbach. It is not a Goldbach counterexample.

### T72.2 (PROVED: unconditional power removal, two logarithmic factors improvement)

Let \(T_X(\alpha)=\sum_n\Lambda(n)w(n/X)e(n\alpha)\), \(G_X(N)=\int_{\mathbb T}T_X(\alpha)^2e(-N\alpha)d\alpha\), and \(M=\|w\|_\infty\). The total weighted mass of proper powers \(n=p^k,\ k\ge2\), is at most
\[
\sum_{k\ge2,p^k<X}(\log p)w(p^k/X)
\le M\pi(\sqrt X)\log X.
\]
Every \(\Lambda(n)w(n/X)\) coefficient is at most \(M\log X\), and the ordered convolution contamination is bounded by twice the proper-power mass times that maximum. Therefore **for all X≥4 and every integer N**, an explicitly deterministic bound holds:
\[
\boxed{0\le G_X(N)-r_X(N)\le2M^2\lfloor\sqrt X\rfloor(\log X)^2.}
\]
Using additionally the established *unconditional Chebyshev prime-counting upper estimate* \(\pi(y)\le C_{\rm Ch}y/\log y\), we prove for X≥16
\[
\boxed{0\le G_X(N)-r_X(N)\le4C_{\rm Ch}M^2\sqrt X\log X.}
\]
The second estimate improves the Stage 69 project \(O_w(\sqrt X\log^3X)\) prime-power bookkeeping by **two logarithms**; this is a refinement of an elementary known argument, not a new Goldbach theorem. No special zero-free assumption is needed.

### T72.3 (CONDITIONAL exact target certificate; arithmetic hypothesis OPEN)

Either one of the following **independently proven** target-pointwise inequalities would guarantee a genuine-prime pair in the support:

- **Signed complement:** \(E_X(N)>-W^2X/(6\pi)\), for sufficiently large X and all residual N∈[X/2,X].
- **Full von Mangoldt coefficient:** \(G_X(N)>4C_{\rm Ch}M^2\sqrt X\log X\) for the same targets and X≥16.

Neither has been established for every residual N. The full target positivity is not inferred. Standard published average/exceptional-set theorems do not prohibit a particular isolated failure. These conditions may be far stronger than the conjecture itself, and must never be silently assumed.

## 3. Exact finite validation and its boundaries

Run \`python3 -B results/stage72/verify_stage72.py\` to reproduce \`exact_results.json\`. The test executed with **Python 3.13.5**, using \`fractions.Fraction\` and deterministic trial-division primality checking. It checked **122 even target inputs** across X=90,150,240. For each case, it independently computed the weighted convolution by direct pair enumeration and by reflected dictionary lookup, verified the proper-power contamination union bound, and erased the target coefficient by deleting one endpoint per complementary prime edge. All checks passed. **Crucial caveat:** this finite regression uses a rational surrogate weight \((n/X)(1-n/X)\) and *unit* coefficients rather than true \(\log p\) weights, and tests only the exact combinatorial and Fourier-algebraic statements. It does NOT test Chebyshev/PNT asymptotics, numerical Fourier integrations, or universal Goldbach.

The executed local source and output were compared against their exact GitHub blob SHA-1 identities. Their SHA-256 values and tool versions are in \`verification_manifest.json\`.

## 4. Historical and external context

- Classical weighted PNT and elementary Fourier inversion: **ESTABLISHED external facts**, applied directly in T72.1.
- Chebyshev \(\pi(y)\ll y/\log y\): **ESTABLISHED external theorem**, independently formalized in Isabelle AFP by Manuel Eberl, https://isa-afp.org/browser_info/current/AFP/Prime_Distribution_Elementary/Elementary_Prime_Bounds.html .
- The sieve parity barrier and complexity of a full *binary* prime correlation are discussed in H. Iwaniec, *Prime Numbers and L-functions* (ICM 2006), https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM2006.1/ICM2006.1.ocr.pdf .
- Goldbach exceptional-set theorems (e.g. Bhowmik–Grimmelt, *The exceptional set of the Goldbach problem*, *Analysis Mathematica* 52 (2026)) do not supply a **pointwise theorem** with no exceptions. DOI https://doi.org/10.1007/s10476-026-00191-z .
- Wu's established unconditional upper sieve (2004) was used in Stages 70–71 to construct the vanishing-mass deletion countermodel, not to claim Goldbach positivity: https://doi.org/10.4064/aa114-3-2 .

## 5. Audited limitations and the next mathematical bottleneck

- The **positive short core is arithmetic-neutral**: it applies to any dense enough nonnegative prime-frequency subset, even one constructed to lack the target.
- The **prime-power error is small and unconditional**, but a positive lower bound for the full binary \(\Lambda*\Lambda\) coefficient remains the essential unresolved arithmetic statement.
- \(\mathbb T\setminus J_X\) contains other major arcs as well as minor arcs. It is **incorrect** to use a minor-only fourth moment as an upper bound on that whole complement.
- The bound \(G_X(N)>O(\sqrt X\log X)\), uniform for *each* N, cannot be obtained from the first-order PNT, the 210-wheel density, a finite higher moment or an exceptional-set power saving alone.
- The full Fourier identity is \(r_X(N)=C_X(N)+E_X(N)\). Claiming the sign of E from positivity of C would be the **first invalid implication**.

**Next task, Stage 73 (queued only):** find a mathematically noncircular **true-prime signed correlation estimate** for the complementary region that is *not* preserved by Stage 71's matching deletion, or prove an explicit obstacle for a narrowly defined attempted estimate. Do not revisit general norms or increase finite verification ranges.

**Final verdict:** Stage 72 closed as a rigorous *internal mathematical step* and sharpened arithmetic error analysis; **no universal binary Goldbach positivity theorem proved**. \`main\` and prior branches untouched, PR remains draft pending external mathematical review. No Codex usage.
