# External referee package — verification notes

## State and review protocol

Pinned source branch: `cocalc/dependency-audit-stages73-75`.
Pinned source commit: `512a20cac32623ad4d150a8e15a92d311476fe05`.
Dedicated-identity SSH fetch succeeded; local and remote heads matched; initial worktree was clean. The authorized GitHub connector confirmed PR #25: open, draft, not merged, targeting `cocalc/stage75-novelty-gate-prime-input`. The optional `gh` executable remains unavailable; it was neither installed nor needed. No second PR is created.

The canonical referee document is `referee_package.pdf`: two body pages plus one appendix page. Its editable LaTeX source contains the same material. The appendix reproduces all cells of six selected historical ledger rows without changing their text. The manifest fingerprints those source rows and earlier evidence. Line references in the eight questions refer to unchanged files at the pinned source commit. The appendix and questions are review pointers, not a substitute for the full earlier proofs.

## Exact checks actually executed

Command from the repository root:

```sh
sage -python results/external_referee_package/verify_algebra_sage.py
```

Result: PASS, SageMath 10.9; three groups of free multivariate polynomial identities over the rational field QQ. This new implementation imports no project verifier and does not inspect earlier Python algorithms.

1. **Error elimination:** two residuals vanish identically for independent formal variables, checking both rearrangements in T75.1. This does not test whether its analytic error bounds hold.
2. **Proper-power union algebra:** the product difference is `t*q + s*u + q*u`; the union majorant exceeds it by `q*u`. Nonnegative coefficient variables are an explicit assumption for the inequality. This checks the algebra behind double-counting, not a prime-counting estimate.
3. **Midpoint/base-3 algebra:** five equalities check the midpoint sum, position sum, position difference and the two reconstruction formulas. Division is exact in QQ. These tests assert no primality or integrality domain; those remain mathematical hypotheses in the document.

There are no sampled targets, sieve ranges or primality methods: no primes were computed. No old Type I kernel, wheel-210, deletion, moment or Goldbach experiment was rerun. No finite check verifies an analytic theorem or a universal quantifier. The execution was a short local Sage invocation; separate peak-memory/CPU timing was not instrumented and no such measurement is claimed. Exact software versions and outputs are embedded in the manifest.

## Independent human referee required

- T73.5: reflected Stieltjes weights, coefficient grouping, nonreduced powers and BV mesh/centering, with uniform target errors.
- T74.3: boundary convergence of the differentiated Mobius series, the Euler convolution and absolute moment for varying target divisors, and uniform local-factor removal.
- T75.1: dependence on those analytic bounds, proper-power correction, precise asymptotic quantifiers and conditional positivity threshold.
- Logical scope: distinguish the original three-case assertion from strong Goldbach; verify all prime-2, midpoint, weight-support and distinctness conditions.
- Overall: check no unproved signed actual-prime margin is used as a premise for a claimed unconditional conclusion. The package makes no claim of outside certification yet.

## Optional later Lean scope — not started

At most one four-hour exploratory formalization session, only after human approval of definitions: one hour for the three-case predicates and their actual logical implications; one hour for the integer/half-integer bookkeeping in `a+b=N/2-3`; one hour for the midpoint reflection identity; one hour for the exact finite wheel-210 admissibility factor, including exceptional small-prime conventions. If required library infrastructure exceeds the time box, stop with an explicit dependency list. This is a proposed scope, not an estimate or promise of completed formal proofs.

Do not propose Lean certification of BV, quantitative PNT, the uniform Type I asymptotic, simultaneous primality or the missing signed Type II theorem within this scope. The wheel item is a future finite modular identity only; no wheel computation or formalization is performed now. Three-case equivalence means equivalence with residual coverage and the stated pointwise disjunction, not an unproved converse to strong Goldbach.

## Reproduction and limitations

Use the installed CoCalc document pipeline:

```sh
"/opt/cocalc/bin/node" "/opt/cocalc/bin2/cocalc-cli.js" project build /home/user/goldbach-dependency-audit/results/external_referee_package/referee_package.tex --build-timeout 60s
pdfinfo results/external_referee_package/referee_package.pdf
```

Check that PDF pages 1–2 are the body and page 3 is the single appendix, all content is legible, and no compilation error is present. Build-generated PDF metadata can vary on another run; hashes pin the delivered bytes, not a promise of bitwise-identical PDF regeneration. Compare the manifest's text/script and historical-evidence hashes before reproducing. Re-run `git diff --check` and inspect that changes from the pinned source are restricted to this package directory. The manifest excludes its own hash; the final pushed Git commit identifies its exact bytes. Final local/remote SHA equality is reported in chat and the existing review PR, without a self-referential commit field.

## Five-line novelty/parity disposition

1. Existing reductions retain a signed pointwise Type II remainder.
2. A Type I main term does not control that sign.
3. Coarse deletion-stable data fail to force target positivity in the modified-subset class.
4. This package supplies no new independent actual-prime arithmetic input.
5. Preserve NO-GO; stop after publication, with no Stage 76 and no universal Goldbach claim.
