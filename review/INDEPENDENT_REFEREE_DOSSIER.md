# Independent mathematical referee dossier — Stages 73–76

**Purpose:** Request three distinct, independently authored mathematical assessments of the analytical dependency chain. This is a **review request**, not a certificate, endorsement, or claim of universal Goldbach.

**Canonical research version:** [Stage 76 selected PR #27](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/pull/27), head `d9e0ac05247f2f220423c444d30561645c747c4c` (a draft and unmerged when this dossier was prepared). The inherited [external referee handoff in PR #25](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/pull/25), head `3a5581dd93b7c50bbc55062d032a6ad2acab1fb4c`, contains a two-page body, an appendix, and eight source-linked questions. PR #26 is the retained alternative, not the primary review target. The proposed root [LEDGER.md](../LEDGER.md) becomes the canonical governance registry only when PR #28 is merged to `main`.

## Unaltered problem and what the project does *not* prove

The author's three cases are `N=p+1`, `N=2p`, and `N=p+q` for distinct genuine primes `p<q`. For even `N>=4`, let `R(N)` count unordered distinct pairs and `H` consist of even `N` with `N-1` and `N/2` composite. The universal three-case assertion is equivalent to `R(N)>0` for every `N in H`.

Define the additional boundary `H1={N even>=8: N-1 prime, N/2 composite}`. Strong Goldbach is equivalent to `R(N)>0` on `H union H1`. The two universal statements must not be conflated.

The analytical chain uses the actual primes, not an arbitrary model:
```latex
S_X(alpha) = sum_{p prime} (log p) w(p/X) exp(2 pi i p alpha),
r_X(N) = integral_0^1 S_X(alpha)^2 exp(-2 pi i N alpha) d alpha,
G_X(N) = sum_n Lambda(n)Lambda(N-n) w(n/X)w((N-n)/X).
```
The coefficient `r_X` counts **ordered weighted** genuine-prime pairs, not `R(N)`. With the defined signed Type II term `A_3`, the existing chain proposes the identity `A_3(N)=r_X(N)-F_X(N)+e_X(N)` and a uniform `sup |e_X|=o_w(X)` on the stated even target range. The unresolved arithmetic input is a sufficiently strong signed bound for genuine primes. No such bound, effective finite cutoff, universal three-case proof, or strong Goldbach proof has been established.

## Referee assignments (three independent mathematical reviews)

Reviewers should not merely rerun project tests or copy another reviewer. Each receives the pinned sources, may inspect the full ancestor history, and supplies an original proof-level report with citations to precise source lines, independent derivations or counterexamples wherever feasible.

| Review | Core question | Required technical checkpoints | Evidence to consult |
|---|---|---|---|
| **R1 — Analytic Type I / T73.5** | Is the reduction `G_X=M_I+A_3+E_I` justified uniformly in every stated target and every fixed power-of-log saving? | Vaughan truncation and `l=1`; support and endpoint terms; reflected Stieltjes integration; non-coprime residue and prime-power contributions; Bombieri–Vinogradov centering, endpoint mesh, parameter ordering, uniformity in `N`; error and quantifiers | PR25 referee PDF Questions 2–4; `results/stage73/02_binary_von_mangoldt_decomposition.md`; `results/stage74/01_gate_and_kernel.md` |
| **R2 — Arithmetic kernel / T74.3** | Does the truncated kernel approach the binary singular series uniformly with the claimed absolute error? | `phi(dm)` when `gcd(d,m)>1`, correction sign; `N=16,U=V=3` counterexample; Möbius derivative convergence at `s=0`; absolute Euler moment uniform in varying `N`; shared prime and removed-`p` correction, even `N>0`, local-factor product, dependence on `w` | PR25 Questions 5–7; `results/stage74/01_gate_and_kernel.md`; independent exact scripts and manifest |
| **R3 — Error transport, logic and scope / T75.1 + Stage 76** | Are the rearrangements, prime-power error and positivity threshold justified with exact domains, without circular hypotheses? | `P_X=G_X-r_X>=0` and its upper bound; error signs; uniform `o_w(X)` and epsilon slack; `H/H1` partition, 2 and diagonals, actual-prime weighted support; `F_X>=c_w X`; conditional threshold only; matching deletion scope and counterexample on shared-endpoint graphs; no inappropriate universal inference | PR25 Questions 1 and 8; `results/stage75/01_duplication_gate.md`; `results/stage76_closure/01_audit_report.md`, monograph and manifest |

**Cross-review requirement:** R2 states whether its theorem supports R3's use of `F_X`; R1 specifies exactly what R2/R3 may treat as established; R3 must list every remaining input independently. Each review remains provisional until all cross-dependencies and corrections are reconciled. A critique by one author under three headings is **one** reviewer, not three.

## Full reference links pinned to the chosen source tree

- [R1 decomposition](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/blob/d9e0ac05247f2f220423c444d30561645c747c4c/results/stage73/02_binary_von_mangoldt_decomposition.md)
- [R2 kernel](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/blob/d9e0ac05247f2f220423c444d30561645c747c4c/results/stage74/01_gate_and_kernel.md)
- [R3 Stage 75 dependency](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/blob/d9e0ac05247f2f220423c444d30561645c747c4c/results/stage75/01_duplication_gate.md)
- [Stage 76 audit](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/blob/d9e0ac05247f2f220423c444d30561645c747c4c/results/stage76_closure/01_audit_report.md)
- [Stage 76 12-page monograph](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/blob/d9e0ac05247f2f220423c444d30561645c747c4c/results/stage76_closure/03_monograph.pdf)
- [Stage 76 script](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/blob/d9e0ac05247f2f220423c444d30561645c747c4c/results/stage76_closure/02_verify_exact.py)
- [Stage 76 execution and hashes](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/blob/d9e0ac05247f2f220423c444d30561645c747c4c/results/stage76_closure/04_verification_manifest.json)
- [Original three-theorem referee package](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/blob/3a5581dd93b7c50bbc55062d032a6ad2acab1fb4c/results/external_referee_package/referee_package.pdf)

**Named external dependencies, for reviewers to verify against original statements:** T. Tao, *254A Notes 3*, Bombieri–Vinogradov Theorem 17 ([source](https://terrytao.wordpress.com/2015/01/10/254a-notes-3-the-large-sieve-and-the-bombieri-vinogradov-theorem/)); H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I*, Chapter 6, Theorem 6.9 and equations (6.17)–(6.19) ([chapter](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/10.0_pp_168_198_The_Prime_Number_Theorem.pdf)); and J. Wu, upper-sieve theorem ([DOI](https://doi.org/10.4064/aa114-3-2)) only for the separately qualified deletion-model asymptotic. Referees must check hypothesis matches and uniformity; citing a title does not establish applicability.

## Required referee report

Use [REFEREE_REPORT_TEMPLATE.md](REFEREE_REPORT_TEMPLATE.md) as an independent report (one report per referee). Record each theorem's **PASS / PASS WITH CORRECTIONS / MAJOR GAP / FAIL / NOT REVIEWED** verdict, exact quantified statement, independent check method, precise line citations, source dependencies, and the first unjustified inference if applicable. Explicitly classify (i) proofs in the mathematical sense, (ii) finite rational or symbolic checks, and (iii) results assumed from literature.

A conditional theorem must not be marked unconditionally proved simply because its implication is valid. An accepted logical bridge does not establish the existence claim. State openly whether a uniform signed actual-prime bound or an effective finite cutoff was produced; expected answer on the current record is **NO**.

## Handling reports and corrections

Do not merge PRs or modify historical source claims on receipt. Store reviewer-authored reports (with permission) under a new review-only directory on a separate branch, record version, author consent/attribution, timestamp, hash, and precise scope. Keep an append-only delta in the canonical ledger for accepted conclusions or errata. If reviewers disagree, register the conflict and refrain from promoting either assertion until reconciled.

**Dated administrative update (23 November 2026):** Three individualized invitations were sent on 11 November 2026 using the author's Gmail connection, for the R1/R2/R3 review topics. Delivery by the mail provider is not acceptance of an assignment. No signed acceptance, completed review or independent analytical certification is recorded. Contact details and correspondence remain outside this repository.
