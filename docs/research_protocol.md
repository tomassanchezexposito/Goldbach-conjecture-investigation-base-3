# Mathematical verification protocol

## Evidence classifications

Every mathematical claim must carry one of these labels:

- **Established theorem:** proven in recognized mathematical literature with an accurate reference.
- **Proved in this research:** a complete checkable proof is included.
- **Conditional:** true under stated additional hypotheses, without implying those hypotheses.
- **Conjecture:** not proved.
- **Computational observation:** checked on a specified finite domain by specified code.
- **Refuted:** an explicit counterexample or proof of failure exists.
- **Open proof obligation:** a missing estimate or logical step required by a larger claim.

Do not relabel a proof obligation as a theorem.

## Reproducibility requirements

Record definitions, hypotheses, quantified ranges, exceptional cases, and the exact normalization. For each experiment, include parameters, the primality-testing method, hardware/software details where significant, reproducible code, and at least one independent check for important results.

Finite checks are not universal theorems. Prime or semiprime counts from a sieve must not be silently treated as confirmed prime representations.

## Research workflow

1. Retrieve and preserve source materials and their provenance.
2. Formalize the target lemma with exact domains.
3. Research prior results and citation validity.
4. Derive a proof with every step justified.
5. Actively search for small counterexamples and degenerate cases.
6. Check with exact arithmetic where feasible.
7. Audit the proof independently.
8. Only then tag the result as proved and update the research status.

## Publication and attribution

The repository documents the author's three-case statement. Algebraic symmetry is a reformulation, not a proof of universal prime-pair existence. Classical techniques (Vaughan identities, Selberg sieve, Rosser-Iwaniec, circle method, large sieve, etc.) should be accurately attributed.

Do not publish a claimed solution to Goldbach or the three-case coverage conjecture unless a complete universal proof exists.

## Language and privacy

All repository content, source-code comments, commit messages, and associated documentation are written in English. The repository is private; do not commit personal information, access tokens, unreleased private materials, or third-party copyrighted books.
