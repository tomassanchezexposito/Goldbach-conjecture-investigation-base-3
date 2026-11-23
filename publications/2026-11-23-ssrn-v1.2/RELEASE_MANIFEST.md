# SSRN v1.2 — artifact and reproducibility completion manifest

**Date:** 23 November 2026 (UTC). **Scope:** scholarly document preservation and deterministic finite verification. **This is not a mathematical referee report or Goldbach proof.**

## Release bundle

| Item | Path | Original SHA-256 | Git blob SHA-1 | Verified |
|---|---|---|---|---|
| English SSRN-submitted manuscript (11 pages) | `Goldbach_v1.2_EN_SSRN.pdf` | `20b54eb88d5483978462ee07e41c57472a4935e962b9fb4266b7a30a37467547` | `92036b22f47ebc1f3345beddaf2becfd0b6d3cc3` | PASS |
| Spanish companion manuscript | `Goldbach_v1.2_ES.pdf` | `af30540a6756ea668e4c5867a38659439bfc86e363544fca222311f1fb75653a` | `f3b6e1c105ba8b3b61f7d52a612cb066dcb656d5` | PASS |
| Full reproducibility ZIP | `Goldbach_v1.2_suplemento.zip` | `f884729f17fec5b367b27f842d3a64e44c5966a901b165dd5f280060960f594c` | `6e7bea60e974912973a627bf99761df480bd3f4f` | PASS |

All **14 supplementary text files** were extracted unchanged to `supplement/`. Their full byte-level Git blob SHA-1 identities were independently matched to the original extracted files (14/14 PASS). The three binary blobs were also matched to local Git hashes (3/3 PASS). No PDF regeneration or normalization was performed, preserving the exact originally supplied bytes.

## Reproduction in an independent local execution environment

| Command / action | Outcome |
|---|---|
| `sha256sum -c SHA256SUMS`, in extracted ZIP | PASS: 14/14 original supplementary files |
| `python3 goldbach_reflected_audit.py 7930` | PASS: exact reflected-sieve checks, 3964 even targets |
| `g++ -std=c++17 -O3 -Wall -Wextra -pedantic distinct_witness_audit.cpp -o witness` | PASS: compile without reported errors |
| `./witness 8000000 > witness-rerun.txt` and exact `diff -u` | PASS: output identical to supplied `witness_8000000.txt` |
| `python3 check_printed_prefix.py 'ssrn-5705571 (1).pdf'` | PASS: all 1000 prime entries, endpoints 3 and 7927 |
| `python3 antidiagonal_audit.py` | PASS: `R1=0, R2=2, R3=7, R4=5`, matching the supplied output |

In the 8,000,000-bound check, there are 3,202,369 targets in H and 514,484 in H1, all with distinct-prime witnesses; among 283,146 targets with prime midpoint, 283,144 have distinct-prime witnesses, and 4 and 6 do not. **These are finite exact outcomes, not statements about larger ranges.**

## The mathematical limit

The author's three cases are N=p+1, N=2p, and N=p+q for distinct genuine primes p<q. The reflected equality follows from N=p+q but is not a prime-pair criterion. The original assertion is equivalent to R(N)>0 for N in H; strong Goldbach requires the additional H1 boundary. The analytic derivations T73.5, T74.3 and T75.1 are pending independent mathematical review. The critical target-uniform signed actual-prime Type II bound and an effective finite link remain unproved. **Neither universal statement is proved.**

## Version and public status

- GitHub archive: deposited and verified in the public repository.
- SSRN: the author reports that the English manuscript was published; a public SSRN page, DOI or abstract ID has not been supplied or independently located. [The separate status file](SUBMISSION_STATUS.md) records the distinction.
- The original source ZIP's `supplement/README.md` is preserved unchanged as a historical snapshot, and its sentence describing an earlier pre-submission stage is not the current administrative state. This manifest and `SUBMISSION_STATUS.md` are the dated updates.
- The manuscript's AI disclosure is retained. Public GitHub access does not imply permission to republish third-party source materials. No independent human peer review or formal certification is claimed.

This folder is an archived **working-paper version**, not a GitHub Release created in the platform's Releases UI. Do not rename it a peer-reviewed accepted article without documentary evidence.
