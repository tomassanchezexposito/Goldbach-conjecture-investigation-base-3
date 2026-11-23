# Reflected prime pairs on 3 + 2a — SSRN preprint v1.2

**Author:** Tomás Sánchez Expósito (Independent Researcher)  
**Manuscript date:** 22 November 2026 (PDF title page); **SSRN form date:** 23 November 2026  
**Submission type:** Preprint; **license selected in SSRN form:** Creative Commons Attribution (CC BY)  
**Status as of the latest author-supplied screenshot:** SSRN submission form reached **Step 7, Review and Submit**. **No confirmation of pressing Submit, SSRN paper ID, DOI, public posting, or editorial screening result has been supplied.** This GitHub record must NOT be cited as proof of SSRN acceptance or public availability.

## Title

*Reflected prime pairs on 3 + 2a: exact sieving, a three-case conjecture and a Type II obstruction*

## Abstract

We connect an additive prime sieve and a batch-residue test for twin-prime candidates to the exact counting of distinct prime pairs with a prescribed even sum. The author's three-case conjecture is equivalent to distinct-prime coverage on the set where both the predecessor and the midpoint are composite. Strong Goldbach additionally requires coverage where the predecessor is prime and the midpoint is composite. We derive a square-start reflected sieve and an equivalent complete-batch GCD test with explicit small-prime exceptions. Three deterministic computations agree on every even target from 4 to 7930, transferring the published 1000-prime prefix to a two-prime counting experiment. A separate exact witness audit through 8,000,000 finds a distinct-prime pair at every even target except 4 and 6. We consolidate the project's variance, Fourier and deletion obstructions and give the details of the Vaughan Type I reduction, the singular-series evaluation of its kernel and the centering of the Type II term. A target-uniform signed lower bound for that term would suffice for eventual coverage, but is not established. We also derive, from an external exceptional-zero formula, a conditional restriction on real Dirichlet zeros from an uncut two-sided estimate on the residual set. An exact counterexample tests an antidiagonal symmetry asserted in a recent preprint. The inherited analytic derivations await independent human review. Neither universal conjecture is proved.

## Precise mathematical scope

For every even integer `N >= 4`, the author's three cases are `N = p+1`, `N = 2p`, or `N = p+q` for genuine primes `p < q`. In the third case `q=N-p` must be prime. The reflected identity `N-2p = 2q-N = q-p` follows algebraically from the sum and does not prove primality.

Define `H={N even >=4: N-1 and N/2 composite}` and `H1={N even >=8: N-1 prime and N/2 composite}`. The universal three-case statement is equivalent to distinct-prime coverage on `H`; strong Goldbach requires coverage on `H union H1` (plus the prime midpoint cases). The former is not a proven equivalent of the latter.

**Status:** elementary logical reductions and exact finite computations are distinguished from internally derived analytical identities and conditional implications. The missing result is an independent target-uniform signed Type II bound for actual primes, followed by an effective cutoff and finite connection. The deletion-stable model no-go does not apply to actual primes without additional hypotheses. Goldbach remains open.

## Scientific record and verification

- Source analytic chain: [PR #27](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/pull/27), pinned commit `d9e0ac05247f2f220423c444d30561645c747c4c`.
- Canonical ledger proposal and independent-referee dossier: [PR #28](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/pull/28). The research PR #27 is not represented as externally accepted; governance PR #28 is tracked separately for the canonical ledger.
- **PDF in English** (`Goldbach_v1.2_EN_SSRN.pdf`, 11 pages), SHA-256: `20b54eb88d5483978462ee07e41c57472a4935e962b9fb4266b7a30a37467547`.
- **PDF in Spanish** (`Goldbach_v1.2_ES.pdf`), SHA-256: `af30540a6756ea668e4c5867a38659439bfc86e363544fca222311f1fb75653a`.
- **Reproducibility supplement** (`Goldbach_v1.2_suplemento.zip`), SHA-256: `f884729f17fec5b367b27f842d3a64e44c5966a901b165dd5f280060960f594c`.
- These three binary files were checked locally but **are not uploaded to GitHub by this publication-record change**. They must not be presented as GitHub-hosted assets. A verified SSRN paper URL and a public supplementary archive URL may be added later, after upload and confirmation.
- The manuscript includes an explicit disclosure that ChatGPT assisted with comparison, derivation, exposition and code. No independent human analytical acceptance is claimed.

## Copyright and publication safeguards

The author's SSRN form shows a proposed CC BY license, but the record does not independently confirm completed submission. The repository is **public** as of 23 November 2026; a limited branch/manifest privacy inspection is documented by governance PR #28, and a complete historical/privacy review remains open. CC BY selected for the SSRN paper does not automatically license code, prior commits or third-party materials. Public GitHub visibility is distinct from making the manuscript publicly available on SSRN. No peer-review endorsement is implied.
