# Append-only publication ledger delta — 23 November 2026

This delta is **not** a revision of any previous theorem statement, and does not replace the root `LEDGER.md` proposed in PR #28.

| ID | Exact record | Label | Dependencies | Source |
|---|---|---|---|---|
| PUB-SSRN-V12-FORM | Author-supplied screenshot shows SSRN Step 7, Review and Submit, for English v1.2 preprint; no completed submission or SSRN DOI evidenced. | Submission preparation observation, NOT publication confirmation | SSRN author screenshot 2026-11-23; SHA-256 of local PDF in README | Publication branch `publication/ssrn-v1-2-submission-record`; this delta |
| PUB-SSRN-V12-STATUS | Goldbach strong and the author's universal three-case statement remain unproved; T73.5, T74.3, T75.1 await independent human analytical review. | Open obligations / internally derived analytic dependencies | PR #27, PR #28, first missing theorem O75.1 | PR27 head `d9e0ac05247f2f220423c444d30561645c747c4c` |
| PUB-SSRN-V12-FINITE | Exact finite witness audit reports distinct-prime coverage for all even N from 4 to 8,000,000 except 4 and 6; this is not a universal proof. | Computational observation reported in v1.2 supplement, not rerun here | `distinct_witness_audit.cpp`, `witness_8000000.txt`, v1.2 supplement SHA-256 | Publication README |

**No-GO/novelty gate:** The first missing actual-prime target-uniform signed Type II bound is unchanged. No new analytic proof is asserted; the present stage is documentation only (L0–L1). Deletion-stable coarse-data obstructions apply only to their enlarged models, not to genuine primes.

**Dated visibility note (23 November 2026):** The owner has already made the repository **public**. A limited 27-branch tree and selected manifest/metadata audit is recorded in governance PR #28; a full historical privacy/license scan remains open. This publication PR did not change visibility. At the time this delta was written no PR merge had been claimed.

## V1.2 artifact-deposit completion — 23 November 2026 (append only)

| ID | Statement | Label | Dependencies and reproducibility | Location |
|---|---|---|---|---|
| PUB-V12-BINARIES | The English and Spanish v1.2 preprint PDFs and the complete original supplement ZIP have been deposited byte-for-byte in the public GitHub publication directory. | Verified artifact deposit, not mathematical endorsement | Original SHA-256 digests and Git blob SHA-1 for all three matched; exact checksums in `README.md` | `publications/2026-11-23-ssrn-v1.2/` |
| PUB-V12-SOURCES | All 14 original text files from the ZIP have been deposited separately as source/code/evidence, with 14/14 Git blob identities verified against the originals. | Verified provenance and reproducible sources | `supplement/SHA256SUMS` and local `sha256sum -c` result PASS; tracked under distinct `supplement/` path, preserving original file names | `publications/2026-11-23-ssrn-v1.2/supplement/` |
| PUB-V12-RERUN | Exact finite prefix, reflected pairs, 8,000,000-bound witness and antidiagonal fixtures were executed successfully in a separate local environment. | Independent rerun of finite algorithms / computational observation only | Python standard library and C++17 compiler; exact comparison with archived results. No new exhaustive analytic proof follows. | `supplement/` |
| PUB-V12-SSRN | The author reports having published the v1.2 manuscript on SSRN, but the SSRN public article page and identifier were not independently obtained. | Author-reported administrative event; external verification OPEN | Last examined screenshot: SSRN Step 7. No SSRN DOI or date is invented. | `SUBMISSION_STATUS.md` |

**Review gate unchanged:** T73.5, T74.3 and T75.1 are not independently accepted analytical proofs; no actual-prime signed target-uniform Type II bound is established. Both universal conjectures remain OPEN. The source research PR #27 and prior historical branches remain unmerged, available through pinned SHA references.

## Corrective administrative delta — 23 November 2026 (append only)

| Registry ID | Corrected event | Evidence label | Source | Effect |
|---|---|---|---|---|
| PUB-V12-SSRN-CORRECTION | The author confirms that English v1.2 was **submitted to SSRN and remains under SSRN review/screening** as of 23 November 2026; it is **not yet published on SSRN**. | Author-confirmed administrative status; no public listing/DOI verified | Direct author clarification, 23 November 2026 | **Supersedes** the earlier `PUB-V12-SSRN` row and any statement that the paper had already been published. Preserves history; no mathematical label or PDF changes. |

The GitHub manuscript PDFs and reproducibility package remain publicly accessible. SSRN's administrative screening must not be described as independent mathematical peer review.
