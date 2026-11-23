# Prime Progressions and Reflected Even-Number Representations

**Public mathematical research repository** for the author's prime-position study and three-case representation statement. All repository materials are written in English.

> **Mathematical status: OPEN.** Universal coverage of every even integer is not proved. This repository distinguishes algebraic identities, established results, computational observations, and open proof obligations.

## Latest paper and reproducibility archive

**SSRN preprint v1.2:** *Reflected prime pairs on 3 + 2a: exact sieving, a three-case conjecture and a Type II obstruction* (Tomás Sánchez Expósito; manuscript dated 22 November 2026). The author reports publication on SSRN, but the exact public SSRN URL, DOI and screening status have **not been independently verified** in this repository.

- [English preprint PDF](publications/2026-11-23-ssrn-v1.2/Goldbach_v1.2_EN_SSRN.pdf) (11 pages; byte-identical to the file supplied for SSRN).
- [Spanish PDF](publications/2026-11-23-ssrn-v1.2/Goldbach_v1.2_ES.pdf) (parallel translation).
- [Complete reproducibility ZIP](publications/2026-11-23-ssrn-v1.2/Goldbach_v1.2_suplemento.zip), also extracted under [supplement/](publications/2026-11-23-ssrn-v1.2/supplement/).
- [Publication record and source hashes](publications/2026-11-23-ssrn-v1.2/README.md).
- [Canonical research ledger](LEDGER.md) and [independent mathematical referee dossier](review/INDEPENDENT_REFEREE_DOSSIER.md).

All 17 deposited artifacts were matched to their exact Git object IDs. The ZIP's SHA-256 checklist passes, and the deterministic finite tests were run. **Reproducibility does not establish a proof of universal Goldbach.** Internal analytic derivations T73.5, T74.3 and T75.1 still await independent human scrutiny; [Stage 76 PR #27](https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/pull/27) remains open, draft and unmerged.

## The author's three-case statement

The proposed statement is: **Every even integer N > 2 can be represented in at least one of these ways:**

1. **Prime plus one:** N = p + 1 for some prime p.
2. **Double of a prime:** N = p + p for some prime p.
3. **Two distinct primes with reflected doubles:** N = p + q, for primes p < q, such that N - 2p = 2q - N.

The reflection equation follows automatically from p + q = N. It explains the arrows in the original spreadsheet, but **does not** prove that the endpoints are prime.

### Open residual obligation

Let H contain the even integers N >= 4 such that both N - 1 and N/2 are composite. The first two representation types are unavailable on H; the unresolved task is to prove:

**For every N in H, there exist distinct primes p < q with p + q = N.**

This is not known to be true from a complete universal proof. The project studies this three-case formulation as its primary statement, without claiming its coverage has been demonstrated.

## Original coordinate system

Odd candidates are written 3 + 2a. For any even N >= 6, reflected positions satisfy:

    a + b = N/2 - 3

The wheel modulo 210 is used to encode local congruence compatibility. Such compatibility does not imply primality.

## Repository organization

| Path | Purpose |
| --- | --- |
| [docs/research_statement.md](docs/research_statement.md) | Exact statement, notation, residual set and relation to reflected arrows |
| [docs/research_roadmap.md](docs/research_roadmap.md) | Proof obligations, pointwise second-moment audit and success criteria |
| [docs/research_protocol.md](docs/research_protocol.md) | Rigorous evidence labels and reproducibility protocol |
| [docs/prior_research_register.md](docs/prior_research_register.md) | Staged intake of earlier research and source provenance |
| [src/](src/) | Reference algorithms and future computational implementations |
| [tests/](tests/) | Small deterministic regression tests |
| [experiments/](experiments/) | Reproducible experiments and parameter records |
| [lean/](lean/) | Lean 4 / mathlib formalizations, pending implementation |
| [results/](results/) | Audited results and verified certificates |

## Run the reference checks

Python 3.9+ is sufficient for the initial reference code:

~~~bash
python -m unittest discover -s tests -v
~~~

These tests check exact calculations on finite examples. **Passing them does not establish universal coverage.**

## Current research focus

The Stages 56-76 historical branch program has progressed beyond the original Stage 56 second-moment exploratory target. The remaining **first missing theorem** is an independently established target-uniform signed Type II lower bound for the full genuine-prime correlation; then a rigorously effective cutoff and a finite bridge would still be needed. The modeled-subset deletion no-go has a restricted domain and does not refute the actual-prime problem. See [current task status](tasks/NEXT_TASK.md).

## Provenance and caution

Earlier research stages (1–55), spreadsheet/video source materials, and supporting manuscripts have **not** been automatically imported or revalidated by the initial repository setup. Stages 56–76 are indexed by the canonical ledger using pinned commit references on historical research branches. Each source should be brought in with provenance, independently checked, and classified before being treated as a proved result.

All mathematical writing and commit messages within this repository are in English.
