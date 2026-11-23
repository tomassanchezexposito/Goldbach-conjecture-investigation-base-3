# Reflected prime pairs on 3 + 2a — SSRN preprint v1.2

**Author:** Tomás Sánchez Expósito (Independent Researcher)  
**Manuscript date:** 22 November 2026 (PDF title page); **SSRN form date:** 23 November 2026  
**Submission type:** Preprint; **license selected in SSRN form:** Creative Commons Attribution (CC BY)  
**Status (23 November 2026):** the author confirms that this manuscript **has been submitted to SSRN and is currently under SSRN's review/screening process; it has NOT been published on SSRN**. Earlier documentary evidence shows SSRN **Step 7, Review and Submit**. No public SSRN paper URL, manuscript/abstract ID, DOI or confirmation email has been supplied or independently verified. SSRN screening is not independent mathematical peer review.

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
- Canonical root ledger and independent-referee dossier, merged into main through [PR #28](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/pull/28). The research PR #27 remains unmerged and is not represented as externally accepted; PR #28 is a merged documentation/governance record, not an analytic proof endorsement.
- **PDF in English** (`Goldbach_v1.2_EN_SSRN.pdf`, 11 pages), SHA-256: `20b54eb88d5483978462ee07e41c57472a4935e962b9fb4266b7a30a37467547`.
- **PDF in Spanish** (`Goldbach_v1.2_ES.pdf`), SHA-256: `af30540a6756ea668e4c5867a38659439bfc86e363544fca222311f1fb75653a`.
- **Reproducibility supplement** (`Goldbach_v1.2_suplemento.zip`), SHA-256: `f884729f17fec5b367b27f842d3a64e44c5966a901b165dd5f280060960f594c`.
- **All three original files are now uploaded as GitHub binary blobs:** [English PDF](Goldbach_v1.2_EN_SSRN.pdf), [Spanish PDF](Goldbach_v1.2_ES.pdf) and [complete supplement ZIP](Goldbach_v1.2_suplemento.zip). The [supplement/](supplement/) subdirectory contains all 14 extracted original text files for readability and reproduction.
- Every one of the 17 deposited files matches its local Git blob SHA-1 (17/17); the three binary SHA-256 digests above match the originals. The included `SHA256SUMS` checklist passes.
- **Independent local rerun:** Python `goldbach_reflected_audit.py 7930` passed; C++ `distinct_witness_audit.cpp` compiled and reproduced all recorded results through 8,000,000 with two exact sieve implementations; `check_printed_prefix.py` verified all 1000 published primes; `antidiagonal_audit.py` reproduced the documented counts. These are finite checks only, not proof of analytic asymptotics.
- The exact public SSRN landing-page URL/DOI is still **unverified**; add it only when supplied or independently checked.
- The manuscript includes an explicit disclosure that ChatGPT assisted with comparison, derivation, exposition and code. No independent human analytical acceptance is claimed.

## Copyright and publication safeguards

The author's SSRN form shows CC BY selected; the submission is pending SSRN review and not yet publicly published on SSRN; no public landing page or DOI has been verified. The repository is **public** as of 23 November 2026; a limited branch/manifest privacy inspection is documented by governance PR #28, and a complete historical/privacy review remains open. CC BY selected for the SSRN paper does not automatically license code, prior commits or third-party materials. Public GitHub visibility is distinct from making the manuscript publicly available on SSRN. No peer-review endorsement is implied.
