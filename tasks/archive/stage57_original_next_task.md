# Archived Stage 57 task (unaltered source)

Source was the former `tasks/NEXT_TASK.md` at Git blob `a8f56ad80658f0ff64a75f79cdc1638b55fbd370` on main before the v1.2 publication migration.

# NEXT TASK — Stage 57: shifted four-prime correlations and pointwise obstruction

**Status: open research task.** No universal coverage proof is claimed.

## Inputs

- `experiments/stage56_variance_probe.py` — independent small reference.
- `results/stage56_variance_diagnostic.md` — independently checked variance example.
- The CoCalc-generated Stage 56 notebook and report must be imported and reviewed before being treated as the authoritative experimental record.

## Mathematical target

For even N in the residual set H, define R(N) as the number of unordered distinct-prime representations p+q=N. Let A_210(N) be the number of wheel-compatible residues and X_N=R(N)/A_210(N).

1. Derive an **exact** expansion for the shifted correlation X_N X_{N+2h} for fixed h. Identify coincident prime positions and genuinely distinct four-prime configurations. Explicitly handle shared summands, diagonal cases, and wheel factors for both targets.
2. Evaluate the shifted correlations exactly for a reproducible range (e.g., even N<=2000, h=1..10), with independent primality-based algorithms and assertions. Do not infer asymptotics from this finite test.
3. Investigate whether an **independent analytic bound**, rather than an identity involving R(N), could exclude an isolated zero of R(N) on H. Specify all hypotheses and error terms.
4. Audit the known limitation: the strict global variance criterion can fail on blocks with zero missing representations. A new criterion must be logically sufficient and potentially feasible.
5. Save `results/stage57/` containing a Markdown report, machine-readable data, reproducible code, and a manifest of exact parameters. All repository content and agent instructions in English.
6. Search for counterexamples to each proposed intermediate inequality. Do not assert a solution to Goldbach.

## Completion criterion

A valid output includes exact finite verification and a clearly separated *open* analytic proof obligation. Only mark a pointwise theorem proved if a complete non-circular argument is supplied.
