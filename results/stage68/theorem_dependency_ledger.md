# Stage 68 theorem and dependency ledger

| ID | Statement | Hypotheses | Proof location | Independent verification | Evidence/status |
|---|---|---|---|---|---|
| L1 | Fourier sum identity, signed increment, and Gram orientation | $e(t)=e^{2\pi it}$; finite prime polynomial; stated Fourier convention | `01_dependency_audit.md`; adversarial derivation in `08_adversarial_review.md` | SymPy/Sage finite matrix checks | PROVED identity |
| L2 | Exact arc-budget optimum | Finite $J$, measurable disjoint $E_r$, complex $L^2$ inputs, budgets $B_r\ge0$ | `02_exact_budget_optimization.md`, Theorem 1 | Two independent symbolic implementations verify examples only | PROVED abstract theorem |
| L3 | Triangle-bound equality criterion | Same as L2 | `02_exact_budget_optimization.md` | Matrix argument and exact interval example | PROVED |
| L4 | Nonaligned interval Grams exist | $J=\{1,2\}$, radius $1/8$, centers 0 and $1/2$ | `02_exact_budget_optimization.md` | `verify_stage68.py`, `verify_stage68_sage.py` | PROVED exactly; FINITE VERIFICATION |
| L5 | Allocation collapse with total budget | Same domains, only $\sum B_r\le B$ | `02_exact_budget_optimization.md` | Cauchy–Schwarz equality allocation | PROVED |
| L6 | Uniform complete-minor spectral estimate | Any finite distinct nonzero $J(X)$ and measurable major set of measure $\mu$ | `03_uniform_spectral_no_gain.md` | Exact full Gram on several finite sets | PROVED geometrically |
| L7 | Arcwise-energy implication to increment norm | Disjoint partition, independent upper budgets for each piece | `04_arc_budget_feasibility.md` | Exact optimization theorem L2 | PROVED conditional on budgets |
| L8 | Strict pointwise zero-exclusion criterion | Nonnegative weight; major lower bound, total energy and increment bounds independent of target representation | `04_arc_budget_feasibility.md` | Algebraic reduction and inherited Stage 66 variance theorem | CONDITIONAL implication PROVED |
| L9 | Sparse positive-coefficient minor-sign countermodel | $S=e(3\alpha)+e(5\alpha)$, target 28, symmetric interval radius $1/88$ | `05_prime_specific_structure.md` | SymPy and Sage polynomial/interval checks | PROVED model; FINITE VERIFICATION; not genuine-prime counterexample |
| L10 | Half-period relation | Odd frequency support; region invariance only when explicitly imposed | `05_prime_specific_structure.md` | Algebraic translation identity | PROVED |
| L11 | Base-3 reflection and local exclusions | $p=3+2a$, $q=3+2b$, separate $a=0$ prime 3 | `05_prime_specific_structure.md` | Direct modular derivation | PROVED coordinate identity; no prime lower bound |
| L12 | Shared/four-distinct decomposition limitation | Stage 63 representation-count conventions | `05_prime_specific_structure.md` and Stage 63 M1 | Exact count partition inherited | PROVED identity; lower bound OPEN |
| L13 | Li–Liu/global moment scaling | Smooth weight, rational cores, common Dirichlet zero hypothesis | `06_literature_and_theorem_strength.md`; inherited Stage 64 sources | Fresh Stage 68 statement-level check; PDF hash in `06_sources.json` | EXTERNAL THEOREM; CONDITIONAL; statement-level source check |
| L14 | Candidate signed increment theorem (P68) | Uniform $N\in H\cap[X/2,X]$, even shifts, exact major/moment scales | `07_primary_analytic_attempt.md` | No proof or prime computation claims it | OPEN |
| L15 | Original three-case universal coverage | Every even target under original formulation | User's formulation; summarized in `final_report.md` | Not established | OPEN |

## Dependency graph

The deterministic route is L1 + L2 + L5 + L6. The conditional pointwise route is L7 + L8 plus independent arithmetic inputs. The arithmetic bridge sought is L14; if true with stated constants it feeds L8. L9–L12 rule out several generic replacements for that bridge. L13 supplies a global conditional moment and major term but is insufficient quantitatively. None of L1–L13 implies L15.
