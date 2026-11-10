# Stage 63 checkpoint and verification log

## Branch and scope

- Repository: `tomassanchezexposito/Goldbach-conjecture-investigation-base-3`.
- Research branch: `cocalc/stage63-extended-analytic-program`, based on the Stage 62 integration branch.
- Main was neither changed nor merged.
- Dedicated SSH identity was used for Git fetch/push. No private credential content was read, printed, or included in artifacts.
- No software was installed, no paid compute was started, and no files from earlier stages were deleted or overwritten.
- At Stage 63 entry three untracked Python bytecode cache directories were present (`results/stage61/__pycache__/`, `src/__pycache__/`, `tests/__pycache__/`). They have been preserved and are not part of Stage 63 commits.

## Checkpoint commits

| Milestone | Commit | Summary | Verification status |
|---|---|---|---|
| M0 | `9563a6d8986e396c44651ee9615232b5d9478639` | Provenance and critical audit of Stages 56–62. | Earlier focused Stage 57–62 verifiers, SageMath check, and four unit tests recorded in `00_provenance_and_audit.md` and `00_reproducibility_transcript.txt`; exact identities and quantifier limitations reviewed. |
| M1 | `002206c157256eb8080b2ca04cbd16df0a92ca76` | Exact shared-prime contraction and CRT wheel lemma. | `01_verify_modular.py`: 380 modular cases over moduli 210 and 330; 780 target pairs; 564 Stage 57 rows rechecked; assertions passed. |
| M2 | `c47b9361d193eedf08495779b9181033958e1896` | Target-anchored Fourier coefficient and missing-bound ledger. | `02_verify_fourier.py`: 42 targets, direct convolution vs exact finite DFT with $L=2N+1$; multiplicity and prime-power partition assertions passed. |
| M3 | `ef75955339adc7ef0226d03bc2270198fb9fbb8d` | Adversarial audit of adjusted graph/energy criteria. | `03_verify_energy_countermodels.py`: 2,197 exact rational triples, 169 zero-center cases, sharp path constant, eight Stage 61 rows; assertions passed. |
| M4 | `2d22791beffc2713fafacc0a05c5113d5d9846c1` | Full-source literature and implication review. | Peer-reviewed Bhowmik–Grimmelt PDF and Pintz v2 were inspected; cited hypotheses and quantifiers recorded. Chen primary-scan limitation disclosed. |
| M5 | `0b252d916b75c5b2c5755ee0714980b088ffeee5` | Conditional dyadic energy criterion and adversarial countermodel. | `05_countermodels.py`: exact rational threshold/countermodel and prime examples 28, 50, 56 passed. The analytic energy premise remains open. |
| M6 | Recorded by the final commit on this branch; see `git log` and the user return for the resulting full SHA. | Independent final audit, integrated report, dependency register, failed-approach record, Stage 64 objective, manifest, and task handoff. | Commands and results below passed before commit. |

## M6 environment and commands

Environment: Python `3.14.4`; SageMath `10.9 (2026-05-04)` available. M6 used Python 3.14.4. `-B` prevented creation of additional Python bytecode caches. No installation or network-fetched data was needed for M6 checks.

| Command | Result |
|---|---|
| `python3 -B results/stage63/01_verify_modular.py` | Passed; exact direct/product CRT comparisons and shared-prime checks. |
| `python3 -B results/stage63/02_verify_fourier.py` | Passed; 42 exact convolution/DFT coefficient comparisons. |
| `python3 -B results/stage63/03_verify_energy_countermodels.py` | Passed; exact rational certificate and graph countermodels. |
| `python3 -B results/stage63/05_countermodels.py` | Passed; exact rational energy threshold and selected genuine-prime examples. |
| `python3 -B results/stage63/06_final_audit.py` | Passed; 499 even targets and 258 residual targets through 1000, two independent primality algorithms; no finite-range residual zero found; 149 direct/product wheel targets and 1,225 shared-target pairs agreed. |
| `python3 -B -m unittest discover -s tests -v` | Passed: all four repository unit tests. |
| `git diff --check` | Passed before commit. |

The M6 audit is a bounded computational observation and validates definitions/implementations only. It does not prove the infinite assertion. Earlier Stage 56–62 test transcripts remain in the M0 audit and are not represented as M6 reruns.

## Mathematical outcome and unresolved obligations

- Exact CRT, shared-prime contraction, Fourier coefficient, diagonal multiplicity, and prime-power correction identities are proved in research at their linked reports.
- Several proposed covariance, variance, and local-smoothness criteria fail or remain unsupported; explicit counterexamples and first invalid steps are retained in `failed_approaches.md`.
- The M5 conditional implication is proved, but its $o(X^2)$ dyadic energy premise is not known from the reviewed sources.
- The reviewed unconditional literature gives average or exceptional-set information, not universal coverage of every residual target.
- The original three-case conjecture and universal residual coverage remain open. No Goldbach proof is claimed.

## Resource and file preservation record

The finite checks completed locally in under a second per M6 command in this execution. There were no long-running scans, software changes, paid services, destructive Git operations, or edits to prior Stage 56–62 research. Stage 63 commits contain only the explicitly named milestone artifacts. The prior untracked cache directories remain preserved locally and are excluded from Stage 63 content.

## Provenance and hashes

The Stage 63 commit chain is recorded above. M0 includes source commit hashes for Stages 57–62 and a SHA-256 audit of the inherited source files. M6's exact deliverable filenames and SHA-256 values are in `06_manifest.json`; the manifest omits its own digest to avoid a self-referential hash. The final M6 commit SHA cannot be embedded in its own tree, so it is identified by the resulting branch HEAD and user return.
