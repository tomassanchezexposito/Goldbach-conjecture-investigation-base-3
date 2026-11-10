# Stage 60 integration review

**Branch:** `cocalc/stage60-integrated-research`
**Evidence label:** source preservation and verification record; finite checks do not establish universal Goldbach coverage.

## Integration and provenance

The branch began at integration base `156c6acaa89825cd70dd3f3742bf98de8e90434c`. The Stage 58 supplement was cherry-picked from `cocalc/stage58-pointwise-second-moment`, source commit `689c3d696ce750610bed6ad69cdd476fdcaee464`, as commit `d847c3a88d441d2332585c72b468498612ba190e`. Its seven files are:

- `results/stage58/compute_second_moment.sage.py`
- `results/stage58/pointwise_second_moments.md`
- `results/stage58/second_moment_exact.json`
- `results/stage58/second_moment_manifest.json`
- `results/stage58/second_moment_verification.json`
- `results/stage58/summary.md`
- `results/stage58/verify_second_moment.py`

The `cocalc/stage59-local-second-moment` line, including commit `900cae804b76e09992aba555932bc0fd866737af`, was already an ancestor of the integration base. Its report, exact results, Python verifier, and native C verifier remain present. The distinct `cocalc/stage59-sharp-local-energy` line was merged in merge commit `4a4064734074357ef8ee5b34b9af857d1f14f4c4` with second parent `60fed50ca43342bd10384a05813202c79c57eab3`. The retained branch-specific Stage 59 files are:

- `results/stage59/report.md`, `research_note.md`
- `results/stage59/local_cert_native.c`
- `results/stage59/verify_stage59.py`, `verify_local_energy.py`, `verify_mod210_pilot.py`, `verify_graph_energy.py`
- `results/stage59/stage59_local_check.json`, `stage59_mod210_pilot.json`, `graph_energy_pilot.json`

The only merge conflict was `tasks/NEXT_TASK.md`. The Stage 60 parent task remained authoritative. The resolution cites both Stage 59 task protocols by source commit and points to the retained Stage 59 reports and verifiers. No Stage 59 research files were discarded.

## Research distinctions and theorem status

| Item | Status after integration |
|---|---|
| Wheel count and $X_N=R(N)/A_{210}(N)$ definitions | Exact definitions; wheel admissibility is not primality. |
| Same-target square decomposition | Exact identity $R(N)^2=R(N)+R(N)(R(N)-1)$; the second term consists of four distinct prime values. |
| Distinct-target shifted decomposition | Exact partition into four one-position-sharing classes and a four-distinct class. For ordered pairs $p<q$, $r<s$ and increasing target sums, the low/high shared class is empty; two shared positions are impossible. |
| Stage 58 weighted moment lemma and Stage 59 path/cycle/graph inequalities | Deterministic finite-dimensional inequalities, proved under their stated hypotheses. They do not bound prime correlations. |
| Stage 59 local-cycle criterion | Uses a cyclic triangle energy on $(X_{N-2},X_N,X_{N+2})$. |
| Stage 59 local path and graph criteria | Use adjacent-path or specified graph energies. These are distinct energies and their finite pilot results are not interchangeable. |
| Four-position arithmetic estimates | Stage 60 supplies only an elementary candidate-position upper bound, not a useful pointwise asymptotic. No independent positive lower bound for a target count or local mean is obtained. |
| Universal positivity for $N\in H$ | Open. No report or finite search here proves the author's universal three-case statement. |

## Independent verification record

The integrated Stage 57–59 programs were run with exact integer or rational arithmetic where supplied:

- `python3 results/stage57/compute_stage57.py && python3 results/stage57/verify_stage57.py`: all 5,616 correlation rows, 564 targets, 999 wheel values and five configuration categories passed their independent checks. The recorded search is finite.
- `python3 results/stage58/verify_stage58.py && sage results/stage58/compute_second_moment.sage.py && python3 results/stage58/verify_second_moment.py`: passed. Checks include 249 wheel targets, 149 same-target cases, 62 residual anchors, 620 shifted rows, and 320 weighted vectors; the bounded residual search found no zero.
- `python3 results/stage59/verify_stage59.py`: passed its 1,524 residual-target checks in the stated interval; the only failed local-cycle certificate among tested even centers was $N=8$, outside $H$.
- `python3 results/stage59/verify_local_energy.py`, `verify_mod210_pilot.py`, and `verify_graph_energy.py`: all exact local-energy, wheel pilot, and graph-energy assertions passed. The pilots are finite and use measured prime counts.
- Native C verification compiled with `cc -O3 -std=c11` and run through 1,000,000: 499,996 centers and 1,671,838,245 unordered pair configurations were checked; only $N=8$ failed, and no tested residual center failed.
- `python3 -m unittest discover -s tests -v`: all four repository tests passed.

Stage 60 adds an independent bounded audit. `compute_stage60.py` uses a sieve and exact `Fraction` values. `verify_stage60.py` does not import the compute script: it uses trial division, direct enumeration of the 210 residue classes, independent shared-position classification, and exact rational checks. On even centers $8\le N\le300$, it verifies 147 triples, 441 wheel values, and all same-target and shifted product decompositions. It checks the sharp zero-coordinate inequality on 256 nonnegative integer triples. All assertions pass. Among the 62 tested residual centers, the measured path certificate passes at all 62 and no center count is zero. These are bounded computational observations only.

## Issue #8 access

The handoff references coordination issue #8, but it could not be read in this environment: `gh` is not installed, and an unauthenticated read-only GitHub API request returned HTTP 404 for this private repository/issue. No software was installed and no credentials were requested or exposed. The branch integration and research follow the checked-in handoff; the issue's contents remain an explicit unavailable input.

## Working-tree and branch scope

The integration work was performed on `cocalc/stage60-integrated-research`; the base `main` branch was not checked out or modified. No branch was force-pushed, rebased, reset, or deleted. Generated Python cache directories from verification are incidental untracked files and are not part of this deliverable.
