# Stage 73 — Signed prime correlations and the binary obstruction

**Status:** the authorized research cycle is completed with internally checked proofs, exact regressions and two developed analytic routes. Universal coverage of the original three-case conjecture remains **OPEN**. No new simultaneous-primality lower bound has been proved. Statements below are project deductions, not claims of mathematical-literature novelty or external peer review.

## Unchanged domain and continuity

$H=\{N\ge4:N\text{ even},N-1\text{ composite},N/2\text{ composite}\}$; $R(N)$ counts unordered distinct genuine-prime pairs. The original cases are $N=p+1$, $N=2p$, or $N=p+q$ with $p<q$. The coordinates $p=3+2a$, $q=3+2b$, $a+b=N/2-3$ preserve prime 3 at $a=0$ and provide no primality theorem.

The branch descends exactly from Stage 72 commit `0801eff2a1e8335539016360be4d1572a1d5ca50`. All Stage 72 proofs, its adversarial review, final report and manifest were read; Stages 70–71 deletion and Stage 69 signed-route dependencies were recovered. The old checkout contained uncommitted Stage 69 files, so they were preserved there and this branch uses `/home/user/goldbach-stage73`. The Stage 73 worktree started clean. Historical research and Stage 72 PR #21 were preserved; the PR was checked to be open, draft and unmerged. SSH fetch succeeded before research; no stale-ref assumption was made.

## A. Proven results

| Result | Mathematical content | Proof and critical pass |
|---|---|---|
| T73.1 | Exact $D$-microarc projector onto $p+q\equiv N\pmod D$ and finite nonnegative sinc lower bound, for $X>\max(2,D/3)$ | [01](01_fourier_signed_complement.md), two derivations; [04](04_adversarial_review.md) |
| T73.2 | For fixed $D,w$, signed local asymptotic $C_D=XF_D(N)K_w(N/X)+o(X)$; for even $N$, $F_{210}(N)\ge175/128$, equality at $(N,105)=1$ | Fixed-modulus PNT-AP/Ramanujan and CRT proofs in 01; exact independent residue checks |
| T73.3 | Correct Vaughan truncation including the small-$n$ boundary and hyperbolic Type II term | Two exact convolution proofs in [02](02_binary_von_mangoldt_decomposition.md); independent formal-log implementations |
| T73.4 | Sharp general bound $|\int_E(S_a^2-S_b^2)e(-N\alpha)|\le|E|\delta(2A-\delta)$ | Two proofs in 04; exact equality case and certified finite checks |
| T73.5 | At $U=V=\lfloor X^{1/5}\rfloor$, $G=\mathcal M_I+A_3+O_{A,w}(X\log^{-A}X+X^{2/5}\log^3X)$ uniformly in the target | Logarithmic grouped coefficient bound, AP partial summation, nonreduced prime-power bound, BV mesh reduction in 02; separate audit in 04 |

The fixed-wheel theorem uses established fixed-modulus PNT. T73.5 uses established Bombieri–Vinogradov and quantitative PNT; it closes the Type I error and retains the signed Type II main contribution. T73.4 plus the established Stage 70–71 deletion theorem shows a new limitation: **even leading signed profiles on every fixed rational-arc family, at $o(X)$ precision, survive target-erasing prime-subset deletion**. This result concerns the enlarged subset class, not the immutable actual-prime sequence.

Stage 72's $C_1\ge2S(0)^2/(3\pi X)$ and $0\le G-r\le4C_{\rm Ch}M^2\sqrt X\log X$ were independently rederived. They are not presented as new Stage 73 improvements. A conservative new wheel bound is $C_{210}\ge175W^2X/(768\pi)$ at sufficiently large $X$, and a sharper asymptotic lower coefficient is $175W^2/(192\pi)$. Neither controls the total coefficient without its signed complement.

## B. Conditional conclusions and exact remaining gap

Fix a broad smooth weight, for example $w>0$ on $[1/5,3/5]$. With actual fixed prime coefficients,
$$r_X(N)=C_{210}(N)+E_{210}(N).$$
An independent lower bound $E_{210}\ge-L_{210}+\eta_X$, $\eta_X>0$, for **every** $N\in H\cap[X/2,X]$, would imply $r_X(N)>0$. The convenient stricter bound $E_{210}>-175W^2X/(768\pi)$ would also suffice at large $X$. Both remain open.

In Path B the exact prime-power threshold is $D_X=4C_{\rm Ch}M^2\sqrt X\log X=o(X)$. A target-uniform lower bound $G_X(N)>D_X$ would imply a genuine prime pair. After T73.5, the first unestimated arithmetic quantity is $\mathcal M_I(N)+A_3(N)$ with a positive absolute margin. Section 6 of 02 states the centered Type II Hardy–Littlewood-strength hypothesis and its full quantified consequence, including $J_w\ge m_w^2/20$. That hypothesis retains the essential binary Goldbach difficulty and is not a proved weaker assumption. No 2026 zero-free assertion is needed or accepted in the unconditional reductions.

## C. Refuted approaches and corrections

- Positive central or finite-wheel signed cores alone do not force the target coefficient: the remaining complement may cancel them exactly. Matching deletion preserves these local profiles to $o(X)$.
- A universal statement for **every** smooth weight is false even for full actual-prime support: if $\operatorname{supp}w\subset(1/10,1/5)$ then $r_X(N)=0$ throughout $N\in[X/2,X]$. The residual sequence $N=X=12k+4$ supplies infinitely many explicit domain examples. This is a support error, not a Goldbach counterexample.
- A minor-only fourth moment cannot be applied to the whole complement of the tiny core, which contains other rational arcs. Taking absolute values loses the phase needed for a signed bound.
- Vaughan Type II cannot be discarded, assigned a positive sign, or estimated by a smooth one-variable exponential-sum theorem with the reflected prime weight silently omitted.
- Finite wheel survivors and prime+$P_2$ are not simultaneous primes; exceptional-set bounds permitting one exception do not remove a prescribed target.
- The freshly inspected Bhowmik–Grimmelt formula has $X/\sqrt T$ in (6.7); Stage 69's source ledger transcribed $X/T$. The historical file was preserved and the defect is recorded in [03](03_literature_and_hypothesis_audit.md).
- Stage 72's final reproducibility sentence names a `.js` verifier; its actual committed/rerun program is `.py`. Its historical rational surrogate remains explicitly distinguished from the smooth logarithmic weight.

## D. Computations actually run

Reproduce all declared runs with:

```sh
python3 -B results/stage73/run_verification.py
```

This runs the unchanged Stage 70, 71 and 72 regressions and the two new implementations, writing results only under Stage 73. Python 3.14.4 and SageMath 10.9 (Sage's Python 3.14.4) were used. No software was installed. Exact run times and per-process CPU/peak RSS from `wait4` are in [verification_runs.json](verification_runs.json); finite outputs, source fingerprints and limitations are in [verification_manifest.json](verification_manifest.json).

- Each new implementation checked 600 Vaughan identities and grouped Type I coefficient bounds: $1\le n\le120$, $(U,V)=(1,1),(2,3),(4,4),(5,2),(12,10)$.
- Six binary convolutions were checked as formal polynomials in prime logarithms at $N=16,28,40,64,100,120$. These formal identities imply the actual-log identities by substitution; no algebraic independence of products of logarithms is assumed.
- Python CRT/Möbius arithmetic and Sage cyclotomic arithmetic independently checked the wheel factor over all 105 even residues; Sage checked all 210 root-projector residues.
- Sage checked $X=600$, $N=300,400,540\in H$ with all supported genuine primes, actual logarithms and one fixed smooth bump supported on $[1/10,9/10]$. Certified 160-bit intervals verify core lower bounds, prime-power contamination and local deletion stability. Deleted coefficients are exactly zero by support erasure while their 210-core intervals remain strictly positive. This is three finite examples, not an asymptotic result. Approximate displayed core values are in the machine output; the computations used certified enclosures.
- Stage 72's rerun result byte-matches its historical output; its declared SHA-256 source and result hashes also match. Its 122 rational surrogate cases do not test logarithmic asymptotics. Deterministic factorization/trial division is used in Python; the Sage checks use exact integer factorization, proven small-prime enumeration and cyclotomic fields (prime inputs below 600).

## E. Primary sources and dependency limits

Actually read relevant original passages: Tao, arXiv:1201.6656v4 (2012; journal 2014), equation (4.18)/Lemma 4.11; Wu, *Acta Arith.* 114 (2004), DOI 10.4064/aa114-3-2, Theorems 1–2 via arXiv:0705.1652v1; Tao's author lecture notes (2015), BV Theorem 17 and discrepancy convention; Bhowmik–Grimmelt (2026), DOI 10.1007/s10476-026-00191-z, Theorems 3.1 and 6.3. Full URLs, exact qualifications, metadata discrepancy and downloaded-source hashes are in 03 and [source_manifest.json](source_manifest.json). External full proofs were not independently refereed. The Stage 69 preprint descriptions are inherited and are not accepted as newly checked premises.

## F. Stage 74 objective and scientific verdict

The next question is to **evaluate the explicit truncated Type I main kernel $\mathcal M_I(N)$ uniformly in the residual target**, including the interaction $\varphi(dm)$ when $d$ and prime-power $m$ share a prime, before proposing any Type II cancellation theorem. This is a multiplicative-function problem that does not select a target prime pair. It should determine the correct signed centering of $A_3$, or rigorously exhibit arithmetic variation that prevents a uniform proposed formula. See `tasks/NEXT_TASK.md` for the narrow task and acceptance gates.

Stage 73 gives a positive signed rational-core refinement, an extended deletion obstruction, and a rigorous Type I reduction. It does **not** give the missing positive binary correlation. Universal Goldbach coverage remains **OPEN**.
