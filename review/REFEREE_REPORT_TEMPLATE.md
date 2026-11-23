# Independent referee report template (complete one per reviewer)

**This template is not a completed mathematical review.** It is intended for an independent referee who has read the pinned proofs and original external theorems. Remove this instruction line from the submitted report.

## Identity, provenance and independence

- Reviewer name or agreed anonymous identifier:
- Affiliation/expertise (optional):
- Contact method (held privately; do **not** commit personal contact data without permission):
- Review date (UTC):
- Source repository / pinned commit(s):
- Scope: [ ] R1 T73.5 [ ] R2 T74.3 [ ] R3 T75.1 / Stage76
- Independent derivation performed (describe):
- Tools and versions used (if any):
- Any assistance/collaboration/conflicts of interest:
- Consent to publish this report and attribution: [ ] yes [ ] no [ ] restricted

## Exactly reviewed statement

Copy the exact quantified formulation **as a quotation from the submitted project source**, with source path, line range, version and hash. Include domain of X, N, all fixed constants, weight support, truncation parameters, implied-constant dependence and exceptions. If a statement cannot be located or its hypotheses are ambiguous, record that before analysis.

## Dependency table

| Dependency or theorem | Primary original source / exact theorem | Hypotheses verified? | Mathematical role | Missing/unclear detail |
|---|---|---|---|---|
| | | | | |

## Verification of each contested step

| Step / source lines | Verdict | Independent derivation, counterexample, or precise concern | Changes required |
|---|---|---|---|
| | PASS / PASS WITH CORRECTIONS / MAJOR GAP / FAIL / NOT REVIEWED | | |

Treat finite algebra/computational agreement as verification of the specified exact identities only. It does not establish asymptotic uniformity, target positivity or Goldbach.

## Mandatory targeted questions

- **R1:** Are truncation endpoints, reflected Stieltjes integration, nonreduced powers, Bombieri–Vinogradov centering, first positive mesh point, arbitrary logarithmic saving and uniformity in the varying target all justified?
- **R2:** Are the shared-prime correction and its sign valid, is `phi(dm)` never factored without coprimality, does the differentiated Möbius series converge at the relevant boundary, and is the Euler absolute moment uniform as N varies?
- **R3:** Are `P_X=G_X-r_X`, the error rearrangement and `o_w(X)` genuinely uniform; is H/H1 coverage logically exact; does the broad support imply F_X>=c_w X; is the A3 threshold **conditional**; and does the deletion NO-GO remain limited to its stated class?

Each reviewer should also comment on any dependency in the other two scopes that their own verdict relies upon.

## First invalid or unresolved step

- First theorem or implication that cannot currently be justified:
- Exact source lines and mathematical reason:
- Counterexample or independent calculation (if any):
- Most conservative corrected formulation:
- Does the issue change the scientific status of the project?

## Final verdict

- T73.5: PASS / PASS WITH CORRECTIONS / MAJOR GAP / FAIL / NOT REVIEWED
- T74.3: PASS / PASS WITH CORRECTIONS / MAJOR GAP / FAIL / NOT REVIEWED
- T75.1: PASS / PASS WITH CORRECTIONS / MAJOR GAP / FAIL / NOT REVIEWED
- Stage76 inherited logical and conditional conclusions: PASS / PASS WITH CORRECTIONS / MAJOR GAP / FAIL / NOT REVIEWED
- Has a new independently justified signed genuine-prime margin for each required target been proved? YES / NO (attach full proof if YES)
- Has a rigorous effective cutoff plus finite connection been proved? YES / NO
- Has strong Goldbach or the universal original three-case statement been proved in the reviewed package? YES / NO
- Specific corrections recommended and priority:
- Signature / report date:
- SHA-256 of finalized report (optional; computed after completion):

**A signed report must be evaluated for mathematical merit and cross-dependencies. Three independent reports are not equivalent to a machine-checked proof or to a published peer-reviewed acceptance, and disagreement must be recorded.**
