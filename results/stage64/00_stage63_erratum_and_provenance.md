# Stage 63 M1 erratum and provenance

## Erratum

The Stage 63 M1 text in `results/stage63/01_shared_prime_modular_lemma.md` incorrectly said that the shared primes for targets $(n,m)=(12,18)$ are $x=7$ and $x=11$. The correct values are $x=5$ and $x=7$:

| $x$ | $n-x$ | $m-x$ | Result |
|---:|---:|---:|---|
| 5 | 7 | 13 | All three are prime |
| 7 | 5 | 11 | All three are prime |
| 11 | 1 | 7 | Rejected because 1 is not prime |

The prime test was checked in two independent ways. First, the inherited `results/stage63/01_verify_modular.py` uses trial division to enumerate prime pairs at each target and intersects their position sets; its exact output `01_exact_cases.json` records two shared positions at $(12,18)$. Second, an independent direct trial-division calculation checks the three explicit triples above. The shared-prime contraction lemma itself is unchanged; only the illustrative example was wrong.

## Provenance fingerprints

- Stage 63 source branch: `cocalc/stage63-extended-analytic-program`, audited at commit `cd8dbfd0fd8f3f3a0a1d42f334ebe29e114665b0`.
- Original M1 source commit: `002206c157256eb8080b2ca04cbd16df0a92ca76`.
- Stage 64 starting commit before this correction: `6d53777d70ff25132c02689428ffe491c2296069`.
- SHA-256 of the inherited M1 Markdown at the source commit: `4a540b4f7304c7d5f79457310a039048d716572ede02f4e9c6fd061aff8f63c7`.
- SHA-256 of the inherited M1 verifier: `093f74dd1294778c64e28ff7a9e42a87357cc9fd85d51ef2d0e5a9d2e2c69e62`.

The original commits are preserved. This Stage 64 commit transparently corrects the source example and records the independent checks.

## Classification

**Proved / exact finite verification:** the listed triples and primality statuses are exact. This correction does not change the proof of the general shared-prime identity and makes no universal Goldbach claim.
