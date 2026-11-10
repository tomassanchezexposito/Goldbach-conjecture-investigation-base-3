# Stage 69 M8 — Independent adversarial audit and erratum register

**Review date:** 2026-11-10. **Review origin:** ChatGPT's connected GitHub review and separate local exact-arithmetic runtime, **not a resumed CoCalc Codex job**.  
**Scope:** the actual committed M0–M7 files in \`results/stage69/\`, with selected inherited dependencies in Stages 63–68.  
**Final verdict:** deterministic and Fourier identities verified within their stated domains; **no independently proved, target-uniform genuine-prime lower bound**. Goldbach on the author's residual set H is **OPEN**.

## 1. Precise target and quantifiers

The user's formulation retains the three cases \(N=p+1\), \(N=2p\), and \(N=p+q\) for distinct genuine primes \(p<q\). The reflection equality \(N-2p=2q-N\) follows from their sum; it supplies no primality condition. The residual domain is
\[
H=\{N\in2\mathbb Z:N\ge4,\ N-1\text{ composite},\ N/2\text{ composite}\}.
\]
On H the first two cases fail, and the third is equivalent to \(R(N)>0\) for unordered distinct genuine-prime pairs. For even N>4, no pair includes 2; a possible endpoint 3 remains. \(N=4\) is outside H.

The M8 classification is **PROVED / ESTABLISHED EXTERNAL RESULT / CONDITIONAL / FINITE CHECK / REFUTED / OPEN**. A hypothetical one-hole sequence is not a Goldbach counterexample, and checking finitely many values of H never proves all of H.

## 2. Audit table: exact proof obligations

| Dependency | Audit verdict | First requirement for use on real primes |
|---|---|---|
| M0: two diagonal-projector PSD lift | **PROVED correction**: pure and lift optima both \(\sqrt2\), triangle bound is 2 | Not an arithmetic theorem |
| M0: six Pauli-projector PSD lift | **PROVED abstract**: mixed \(3\sqrt2\), pure \(3\sqrt{1+\sqrt{2/3}}\) | Cannot identify these abstract matrices with actual rational-arc prime Grams without a new realization proof |
| M1: prime-only \(S_w^2\) convolution | **PROVED exact**, with ordered pairs, diagonal and prime-3 exceptions | A positive coefficient needs **simultaneous genuine primality**, not just an admissible residue |
| M1: replacing primes by \(\Lambda\) | **PROVED algebraic correction** \(U_w^2-S_w^2=2S_wQ_w+Q_w^2\); crude uniform error under fixed smooth bounded support | A source's main-term bound must dominate the correction with matching normalization |
| M1/M7: \(\int_{\mathbb T}|S_w|^4e(-j\alpha)\) | **PROVED exact** global shifted correlation of weighted representation counts | Global nonnegative average does not prove \(r_w(N)>0\) at a prescribed N |
| M2: classes \(\mathcal C_0\supset\mathcal C_1\supset\mathcal C_2\supset\mathcal C_3\) | **PROVED under stated nondegeneracy conditions**, abstract classes only | No quantitative separation of the actual \(\mathcal C_3\) input from the unrestricted extremizer |
| M2: two-piece norm obstruction | **PROVED sharp in arbitrary \(L^2\)**, with exact major+minor energy threshold \(|a|^2/(\mu\nu)\) | Requires a **full-circle** fourth-moment budget; a bound on the minor arcs alone cannot replace it |
| M3: rational-arc Fourier identities and reflected pieces | **PROVED** for the explicitly defined arc sets and signs | A geometric multiplier estimate does not control phase of \(S_w^2e(-N\alpha)\) |
| M3: unqualified minor-arc denominator assertion | **REQUIRES CORRECTION**; see Section 4 | State the specific approximation theorem/selection and its error window |
| M4: wheel/CRT admissible classes | **PROVED finite modular count** | Survivors may be composite; sieve parity obstruction remains |
| M6: exact-energy minimum vs energy-upper-budget certificate | **PROVED** with corrected branch breakpoint; independently checked as below | Need an independently proved target-uniform increment energy \(\bar V\) below the strict exclusion threshold |
| M7: two proof routes | **OPEN** at specific signed prime-only Fourier estimate and reflected two-prime correlation lower bound | Neither line supplies the necessary estimate from inherited theorems |

## 3. Independent algebraic regression executed in this review

The independent script \`results/stage69/verify_m8_independent.py\` was **actually executed in a separate local Python runtime**, with machine-readable output \`results/stage69/m8_independent_exact_results.json\`. It is not the prior CoCalc source or a claim about any unexecuted Sage run. It uses only the Python standard library and exact integers/\`Fraction\`:

- Seven explicitly selected residual targets in the range 28–120: ordered weighted prime-pair convolution independently matched unordered-pair counts and same-target four-prime multiplicities, using weights \(a_p=p\) rather than reproducing the previous \(\log p\) numerical route.
- All 21 unordered pairings of those seven targets: the four-distinct/shared-one-prime partition equals the directly computed weighted convolution products; shared anchor sums match independently.
- 252 exact rational cases for the M6 energy minimum and its upper-budget inequality, including the transition \(V=mA^2\), the exact-energy breakpoint \(A^2(m+1)^2/m\), and fixed center magnitude.
- The earlier independent extended audit (not yet mirrored as a repo script) also checked nine global weighted fourth-moment shift coefficients and verified 62 residual targets through 300. These are **FINITE checks** only.
- The inherited two-projector and six-Pauli optimal-value proofs were examined algebraically: the first is \(\sqrt2\) in both the vector and PSD formulations, and the second has a strict lift gap. The executable script committed here focuses on the separate prime-correlation and energy tests; it does not claim a fresh independent formal derivation of every external result.

A successful finite script does not establish a large-N analytic estimate or eliminate a singleton.

## 4. New M8 correction: minor-arc membership does not imply low-denominator approximants are absent

In \`results/stage69/03_target_phase_and_arc_decomposition.md\`, Section "Rational-center multiplier calculation", the sentence

> "On the minor arcs the relevant approximating denominator is larger than P"

is **unqualified**. A specific Diophantine approximation scheme might select a rational with denominator \(q>P\), but merely being outside the major-arc neighborhoods does **not** mean there is no nearby rational center with \(q\le P\).

**Exact counterexample to that broader reading:** take \(P=13\), \(X=2000\), and
\[
\alpha=\frac{1013}{3000}=\frac13+\frac{13}{3000}.
\]
The \(q=3\) major-arc radius is \(P/(3X)=13/6000\), strictly smaller than \(|\alpha-1/3|=13/3000\). For every other reduced rational \(a/q\) with \(q\le13\), we have \(|a/q-1/3|\ge1/(3q)\); this gives a separation larger than its major-arc radius, as the exact enumerator independently confirms. Thus \(\alpha\) lies on the **minor arcs** but its **nearest** reduced center with \(q\le P\) remains \(1/3\).

**Required repair:** replace the unqualified sentence by: "Being outside the major-arc cores only means \(|\alpha-a/q|>P/(qX)\) for all reduced \(q\le P\). A denominator \(q>P\) may be produced by a *separately stated* Dirichlet approximation with its own accuracy bound; nearby low-denominator centers can still exist." The original center-resonance identity \(q\mid j\iff e(-ja/q)=1\) and signed increment identity remain valid. No Goldbach result is affected.

**Status:** the original M3 file is preserved to maintain traceability; this explicit review correction supersedes its ambiguous prose. It should be carried into the next consolidated edition, not silently edited in the historical Stage 69 M3 source.

## 5. Sharpness, errors and logical circularity

### M6 exact-vs-upper-budget precision

Let \(c\in\ell^2(\mathbb Z)\), \(|c(N)|\ge A>0\), \(m\) distinct nonzero shifts, \(V=\sum_{j\in J}|c(N+j)-c(N)|^2\), \(B=\sum_n|c(n)|^2\). The universally valid inequality is
\[
B\ge A^2+m\left(A-\sqrt{V/m}\right)_+^2.
\]
For **known exact** \(V\), the sharp minimum equals
\[
\min_{x\ge A}\{x^2+(\sqrt{V}-\sqrt m\,x)^2\}
=\begin{cases}
A^2+(\sqrt V-\sqrt m A)^2,& V\le A^2(m+1)^2/m,\\
V/(m+1),& V\ge A^2(m+1)^2/m.
\end{cases}
\]
For **only** \(V\le\bar V\), the sharp minimum is \(A^2+m(A-\sqrt{\bar V/m})_+^2\). Stage 69 correctly distinguishes these claims. Equality of a proposed energy upper bound with the exclusion threshold gives **no contradiction**.

### Phase and support

The total weighted prime convolution is nonnegative when \(w\ge0\), but the separate minor coefficient may be negative. For a reflection-invariant arc partition, the complete major/minor coefficients are real; nonpaired arc pieces can be complex. For \(N\in H\), a strictly positive weighted coefficient implies an actual **distinct** genuine-prime pair; conversely an actual pair might have zero weight and thus no weighted contribution.

An "anchored" lower bound on four-prime configurations involving target N cannot be asserted after selecting a representation at N: selecting it assumes exactly the unresolved existence claim. No such assumption was needed in the audited identities, but neither route yields an independent lower bound.

### Source-level hypotheses

The 2026 Li–Liu arXiv record states a conditional exceptional-set bound under a **single common Dirichlet-L zero real-part hypothesis** with fixed \(\Theta<11/12\). Pintz–Althöfer and the polynomial-values preprint also have distinct scopes; the latter treats degree \(k\ge2\) polynomial targets. Their arXiv abstracts were checked in this ChatGPT review on 2026-11-10; full mathematical assumptions in the GitHub M5 source report were **recorded by the preceding CoCalc review** and have not been independently re-proved here. The Bhowmik–Grimmelt journal paper supplies an explicit major-arc formula but no zero-exception theorem. None of these results has been demonstrated in this project to yield the missing target-uniform signed estimate. The status of any cited 2026 7/8 zero-free Lean manuscript is inherited and **not** newly certified by this review.

## 6. First missing theorem and corrected conclusion

The source fourth-moment statement is on the scale \(B_{\mathfrak m}(X)\ll X^{5/2}(\log X)^{100}\) **under its stated external hypotheses**, so Cauchy yields only \(|m_w(N)|\ll X^{5/4}(\log X)^{50}\), exceeding the \(X\)-scale positive major term by \(X^{1/4}(\log X)^{50}\). An exceptional-set bound with positive power of \(X\) still permits a singleton.

The **open** arithmetic task is a **uniform signed estimate at every prescribed residual target N** or a provably independent increment-energy estimate that makes the strict exclusion inequality work. The standalone assertion \(|m_w(N)|<(c_0-\delta)X\) under a positive major input is already very strong and implies a quantitative binary Goldbach theorem: do not relabel it as a proven reduction from current estimates.

**M8 disposition:** the main exact formulas survive this review, the SDP correction is sustained, the denominator wording needs the explicit qualification above, and the target-specific prime-distribution estimate is still missing. This is a completed adversarial *document review* with selected executed exact regression, **not** independent journal peer review, Lean proof certification or a proof of Goldbach.
