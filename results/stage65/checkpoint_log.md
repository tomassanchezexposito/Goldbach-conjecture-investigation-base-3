# Stage 65 — Checkpoint and reproducibility log

## Repository and authentication

- Repository: `tomassanchezexposito/Goldbach-conjecture-investigation-base-3`.
- Working branch: `cocalc/stage65-corrected-fourier-localization`, based on initial head `ecdb8e8` (`research: launch Stage 65 corrected Fourier localization with proof obligations`).
- Initial worktree was clean before branch checkout; Stage 65 began on its existing remote-tracking branch without overwriting prior commits.
- Latest fetch command, using the existing dedicated deploy identity: `GIT_SSH_COMMAND='ssh -o IdentitiesOnly=yes -i /home/user/.ssh/id_ed25519_goldbach-investigacion-base-3' git fetch origin --prune` — exit 0.
- Public fingerprint: `SHA256:1tt9g8Q3RZLv3B9HFSKihQp6YteXn7aYYy659+b1Zyg`. No private key data was read or recorded.

## Exact regression gate and new checks

All commands ran from the repository root. Python results use exact integers or `fractions.Fraction`; SageMath is 10.9. No additional software was installed.

| Command | Result and scope | Observed process wall time |
|---|---|---:|
| `python3 -B results/stage65/tests/verify_sum_difference.py` | PASS: N=8 prime sum coefficient 2, prime difference coefficient 0; all 16 frequencies agree with independent exact DFT modulo 97. | 0.11 s |
| `python3 -B results/stage65/tests/verify_localized_kernel.py` | PASS: normalized Dirichlet/Fejér coefficient-weight sums and norms for H=0..16; exact signed shift identity; negative isolated-spike countermodel. | 0.09 s |
| `sage -python results/stage65/tests/verify_localized_kernel_sage.py` | PASS: length-32 DFT modulo 97, product coefficient 200 mod 97 = 6, Parseval 208 mod 97 = 14, and Fejér norm numerators for H=0..16. | 3.29 s |

The Stage 65 scripts record machine-readable outputs beside each verifier. The DFT checks verify finite coefficient identities modulo the stated prime; they do not estimate prime correlations.

## Inherited independent regression suite

| Command | Result and scope | Observed process wall time |
|---|---|---:|
| `python3 -B results/stage64/tests/verify_stage64_exact.py` | PASS: exact CRT/wheel and singular-series checks, finite-field Parseval at moduli 97 and 193, four-prime partitions, and the 210/420 residual-status example. | 0.08 s |
| `sage -python results/stage64/tests/verify_stage64_sage.py` | PASS: independent Sage factorization, wheel count, singular factor, and shared/four-distinct partitions. | 3.30 s |
| `python3 -B results/stage63/01_verify_modular.py` | PASS: 380 modular cases, 780 target pairs, and 564 Stage 57 rows. | 0.72 s |
| `python3 -B results/stage63/02_verify_fourier.py` | PASS: 42 target checks by direct convolution and finite DFT. | 0.13 s |
| `python3 -B results/stage63/03_verify_energy_countermodels.py` | PASS: 2,197 rational vectors and 169 zero-center cases, plus reconstructed Stage 61 rows. | 0.17 s |

The concurrent test batch took approximately 3.5 seconds wall time. Individual process times are environment observations, not complexity claims. Peak memory was not measured. All listed tests exited 0.

## Source audit and finalization

The Stage 64 source manifest is a historical snapshot. In the current branch, four listed paths have different content: `tasks/NEXT_TASK.md`, `results/stage64/02_fourth_moment_to_pointwise_gap.md`, `results/stage64/03_signed_fourprime_alternatives.md`, and `results/stage64/04_research_attempt.md`. The exact current hashes are recorded in `source_manifest.json`; all other repository files listed by that prior manifest match its size and SHA-256. The Stage 64 coefficient report now uses $S_w^2$ for sum coefficients, and its $|S_w|^4$ Parseval expression remains correct.

The SSH fetch completed successfully after the verifiers. Final diff review is completed before commit. The commit SHA, push confirmation, and remote ref verification are reported in the research completion message.
