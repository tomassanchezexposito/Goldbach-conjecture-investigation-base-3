# Prime Progressions and Reflected Even-Number Representations

**Private mathematical research workspace** for the author's prime-position study and three-case representation statement. All repository materials are written in English.

> **Mathematical status: OPEN.** Universal coverage of every even integer is not proved. This repository distinguishes algebraic identities, established results, computational observations, and open proof obligations.

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

Evaluate whether wheel-normalized prime-pair representation counts can satisfy a **pointwise second-moment bound** strong enough to exclude an isolated zero. This requires control of four-prime correlations and off-diagonal terms for the exact even target; positive averages are not enough.

The variance condition under investigation is sufficient but may be unrealistically strong; its feasibility must be audited before claiming it as a universal route.

## Provenance and caution

Earlier research stages (1–55), spreadsheet/video source materials, and supporting manuscripts have **not** been automatically imported or revalidated by this initialization. Each source should be brought in with provenance, independently checked, and classified before being treated as a proved result.

All mathematical writing and commit messages within this repository are in English.
