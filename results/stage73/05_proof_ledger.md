# Stage 73 — Proof and dependency ledger

| ID | Statement and exact domain | Evidence / independent check | Dependency and limitation |
|---|---|---|---|
| A72 | $C_1\ge2S(0)^2/(3\pi X)$, $X\ge2$, integer $N\in[X/2,X]$, nonnegative support in $(0,X)$ | Reproved in 01 by integrated sinc, checked on finite interval examples | Elementary; $\asymp X$ mass uses classical PNT; not new over Stage 72 |
| T73.1 | Disjoint full-$D$ microarc projector and lower bound $L_D$, $X>\max(2,D/3)$ | Two finite Fourier/residue derivations in 01; independent roots-of-unity check | Any nonnegative finite coefficients; includes small primes |
| T73.2 | $C_D=XF_DK_w+o_{w,D}(X)$, fixed $D,w$, uniform integer $N\in[X/2,X]$; even-wheel minimum $175/128$ for 210 | PNT-AP/Ramanujan derivation and independent CRT projection; all 105 residues exact | Established fixed-modulus PNT-AP; no growing $D$ claim or effective cutoff |
| T73.3 | Exact Vaughan identity for every $n\ge1$, $U,V\ge1$; exact binary sum | Two convolution proofs in 02; independent sparse formal-log and Sage polynomial verifiers | Standard identity, project specialization; no signed arithmetic saving |
| T73.5 | Uniform Type I reduction with error $O_{A,w}(X\log^{-A}X+X^{2/5}\log^3X)$ for $U=V=\lfloor X^{1/5}\rfloor$ | Coefficient bound, partial summation, nonreduced prime-power bound and mesh proof in 02; formal coefficient tests | Established BV and quantitative PNT; main term plus Type II sign remains open |
| A72-power | $0\le G-r\le2M^2\lfloor\sqrt X\rfloor\log^2X$; Chebyshev $4C_{\rm Ch}M^2\sqrt X\log X$ | Independent union-bound audit in 02 and inherited regression, actual-log finite checks | Improved bound inherited from Stage 72; valid for every integer target |
| T73.4 | Local signed-profile change $\le|E|\delta(2A-\delta)$, all integer targets and nonnegative attenuations | Factorization and independent coefficient-mass proofs in 04; interval checks | Elementary exact bound, sharp in full general class; asymptotic deletion uses Wu/PNT |
| N73.1 | Leading fixed rational-core signed profiles do not force target positivity in prime-subset class | T73.4 applied to Stage 70–71 matching deletion; exact target erasure | Depends on established Wu/PNT through inherited deletion theorem; no refutation for immutable primes |
| N73.2 | All-smooth-weight positivity claim is false for actual primes | Explicit support $(1/10,1/5)$ and residual sequence $N=X=12k+4$ | Exact support counterexample, no Goldbach counterexample |
| C73.A | $E_{210}\ge-L_{210}+\eta_X$, $\eta_X>0$, would imply $R(N)>0$ | Exact $r=C+E$ and T73.1 | CONDITIONAL implication; signed premise OPEN; fix broad support first |
| C73.B | $G_X(N)>D_X$ would imply $R(N)>0$ on $H$ | Nonnegative prime-power correction | CONDITIONAL implication; uniform lower bound OPEN |
| C73.C | Centered Type II weighted Hardy–Littlewood hypothesis, uniform on $H$ | Exact reduction in 02 section 6 and explicit $J_w\ge m_w^2/20$ support argument; reviewed in 04 section 6 | OPEN arithmetic hypothesis, quantitatively stronger than bare existence |

Theorems T73.1–5 are elementary/standard mechanisms assembled for the project; no mathematical-literature novelty is asserted. T73.2 uses fixed-modulus prime distribution; T73.5 uses established modulus-average distribution to control Type I errors. Neither supplies a new two-prime lower correlation. No theorem here improves simultaneous-primality lower bounds. Each proof is challenged in `04_adversarial_review.md`.


## Exact quantitative stopping point

For a fixed broad weight and every residual $N\in[X/2,X]$, the missing input is an **absolute** signed complement lower margin above $-L_{210}(N)$, or an independently proved binary $\Lambda$ lower bound above $D_X=O_w(\sqrt X\log X)$. A fixed $c_wX$ lower bound would suffice since $D_X=o(X)$. Type I/II expansion, extra positive rational cores and global moment bounds do not supply this input. A weighted Hardy–Littlewood asymptotic with a positive continuum convolution would be stronger than bare Goldbach; treating it as an established lemma would assume the essential difficulty.

## Provenance corrections and finite scope

Stage 72 report's last reproducibility sentence names `verify_stage72.js`; the committed and actually rerun program is `verify_stage72.py`. Its finite rational surrogate is not the smooth logarithmic theorem weight. Stage 73 preserves the historical report and records the actual executable, SHA-256, results and limitation in its own manifest. The Stage 69 $X/T$ source transcription is separately corrected in 03.

The exact tests check 600 integer Vaughan inputs per implementation ($1\le n\le120$, five truncation pairs), six binary polynomial targets, 105 even wheel residues, and 210 root-projector residues. Three further $X=600$ target examples ($N=300,400,540$, all in $H$) use immutable genuine-prime logarithms with certified 160-bit intervals. Their deliberately deleted models have zero target coefficient and positive 210-core integral. No finite result is promoted to a theorem about all targets.
