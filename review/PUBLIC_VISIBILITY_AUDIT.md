# Public-visibility and provenance audit — 23 November 2026

**Classification:** Documented limited security/provenance audit. **NOT an exhaustive security review or assurance that every historical commit is free of private material.** The GitHub repository visibility was confirmed **public** using authenticated repository metadata on 23 November 2026. The owner already changed visibility before this audit.

## Scope and methods

- Enumerated 27 currently returned repository branches (one GitHub API page) and inspected their recursive HEAD trees, with no truncation observed.
- Searched all observed branch file **names** for conventional credential or private-key extensions, credential-oriented names and risky attached binaries. No obvious credential filename was observed. This **does not inspect the contents of all files** or earlier/deleted commit objects.
- Read 14 selected notebook/manifests/source-provenance files, across Stages 56–76, for common credential patterns, email addresses and local machine paths. No evident private key, API credential or access-token pattern was found in the sampled text. Some environment-local source paths and one GitHub-generated noreply-type address appeared; these are metadata rather than automatically confidential secrets.
- Compared all 39 source-hash rows (18 claim summaries and 21 historical stage references) in the proposed root LEDGER with the pinned Stage76 Git tree at `d9e0ac05247f2f220423c444d30561645c747c4c`; **39/39 Git blob SHA-1 values matched**. This checks provenance only, not the mathematical content.
- Independently checked locally available binary files using SHA-256:
  - English v1.2 PDF: `20b54eb88d5483978462ee07e41c57472a4935e962b9fb4266b7a30a37467547`.
  - Spanish v1.2 PDF: `af30540a6756ea668e4c5867a38659439bfc86e363544fca222311f1fb75653a`.
  - v1.2 reproducibility ZIP: `f884729f17fec5b367b27f842d3a64e44c5966a901b165dd5f280060960f594c`.
  - These binaries are **not** committed in governance PR #28 or publication PR #29.

## Explicit limitations and open tasks

1. A recursive branch-HEAD path inventory is **not a complete scan of Git commit history** (deleted files and orphaned objects may still be reachable through history).
2. The scan did **not** inspect the full contents of all 303+ research tree entries, and did **not** scan every PR discussion, issue comment, attachment, releases, GitHub Actions secret configuration, collaborator permission or downloaded third-party book.
3. **GitHub visibility is already public.** Any secret discovered in public history must be revoked and rotated immediately; deleting a current file is not enough to remove history exposure.
4. The historical reviewer handoff is an invitation for mathematical review; **no independent human mathematical referee verdict is recorded**. Three invitation emails were sent by the project owner through an authorized Gmail connection on 11 November 2026; this does not establish that reviews were accepted or completed.
5. SSRN was last observed at Step 7 (**Review and Submit**); neither a confirmed submission nor a posted SSRN DOI is evidenced by that screenshot.
6. Before public release of third-party documents, recheck license and redistribution rights. Existing research monographs and code are not automatically granted CC BY merely because the author's SSRN manuscript uses that license.

## Gate disposition

**Governance/documentation gate:** The root ledger matches pinned source hashes; Markdown table syntax was repaired. The public/private metadata has been reconciled. No new mathematical theorem is claimed.

**Security gate:** *Limited review complete; comprehensive historical/privacy review remains open.* This is a transparent risk record and not a claim of certified safe exposure.

**Scientific gate:** T73.5/T74.3/T75.1 still await independent human mathematical review. Strong Goldbach and the author's universal three-case assertion remain OPEN.

The preservation policy is append-only for theorem claim histories; metadata clarifications are dated rather than silently overwriting earlier scientific results.
