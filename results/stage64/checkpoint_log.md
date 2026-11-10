# Stage 64 checkpoint log

## Checkpoint 1 — inherited erratum

- Base: Stage 63 branch at cd8dbfd0fd8f3f3a0a1d42f334ebe29e114665b0.
- Commit: 6d9d067, correcting the shared-prime example for (12,18).
- The Stage 64 branch was pushed with this transparent correction before the main analytic work.

## Checkpoint 2 — research and independent checks

- Added primary-source audit, fourth-moment localization analysis, exact signed-correlation report, focused pointwise estimate attempt, adversarial review, and final synthesis.
- Python 3.14.4 verifier uses exact integer/rational arithmetic and trial division.
- SageMath 10.9 verifier uses independent primality and factorization routines.
- Both corrected verifiers pass. Initial versions had erroneous assertions about 419; 419 is prime, and the test fixtures were corrected. This was a verifier defect, not a mathematical counterexample.
- Tested finite arithmetic: targets (50, 68, 100, 112); local pair counts for (210,420); cyclic Fourier identity of length 16 modulo 97 and 193.
- No large search or software installation was performed.

## Final pre-push verification

- Both verification programs passed on the final source state: Python in about 0.065 seconds and SageMath in about 3.418 seconds.
- JSON outputs and the provenance manifest parse successfully; the Stage 64 source tree passed the control-byte scan and staged diff passed git diff --cached --check.
- SSH authentication and fetch were performed with the dedicated identity and IdentitiesOnly=yes. The Stage 64 remote branch was at 6d9d06797daf250649acfc5113ca07bf83a6d3fa before the final research commit.
- The GitHub CLI command is unavailable in this environment. No authenticated PR-creation endpoint was used, and no software was installed; the branch comparison URL is provided in the completion message.
