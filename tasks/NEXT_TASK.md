# NEXT TASK — Stage 74: evaluate the truncated Type I main kernel

Queued research objective only; do not begin until requested. Universal coverage of the original three cases remains OPEN.

## Single concrete question

Starting from the completed Stage 73 branch, evaluate uniformly for $N\in H\cap[X/2,X]$ and $t$ in the fixed weight support the explicit signed kernel
$$\mathcal K_{U,V,N}(t)=\sum_{d\le U,(d,N)=1}\frac{\mu(d)}{\varphi(d)}\log(t/d)-\sum_{l\le UV,(l,N)=1}\frac{c_l}{\varphi(l)},\quad
c_l=\sum_{dm=l,d\le U,m\le V}\mu(d)\Lambda(m),$$
with $U=V=\lfloor X^{1/5}\rfloor$ and $\mathcal M_I(N)=\int h_N(t)\mathcal K_{U,V,N}(t)dt$. Prove a uniform asymptotic with a quantified error, or refute a proposed formula by an exact arithmetic obstruction. This asks for the correct Type II centering, not for an assumed prime-pair lower bound.

## Required method and gates

1. Read Stage 73's complete report, proofs, audit and manifest. Independently audit T73.5, including the grouped bound $|c_l|\le\log l$, nonreduced classes, BV centering and mesh endpoints. Preserve Stage 72 PR #21 and all prior evidence.
2. Expand the second term as the actual $d,m$ sum. Separate $m=p^j$ with $p\mid d$ from $p\nmid d$; never assume $\varphi(dm)=\varphi(d)\varphi(m)$ without coprimality. Track $(dm,N)=1$ exactly.
3. Compare fixed targets and targets with many small prime divisors. Constants must be uniform as $N$ varies with $X$; do not silently use a fixed-$N$ Möbius estimate in that regime. Source-check any required multiplicative-function/zero-free estimate.
4. Establish at least two independent derivations for the kernel simplification and use a few exact boundary counterexamples. Avoid expanding finite Goldbach sweeps.
5. State the resulting signed main term of $A_3$ and the precise first remaining target-uniform correlation estimate. Do not claim $A_3=o(X)$ before proving that its main contribution vanishes. Test any proposed enlarged-class certificate against Stage 70–71 deletion and T73.4.
6. Preserve $H=\{N\ge4:N\text{ even},N-1,N/2\text{ composite}\}$, unordered distinct genuine-prime $R(N)$ and $p=3+2a$, $q=3+2b$, $a+b=N/2-3$. The immutable full prime coefficients are unchanged.
7. Save English proofs, source/status ledger, independent verification and exact manifests under `results/stage74/` on a new dedicated branch. Fetch first using the configured dedicated SSH identity and `IdentitiesOnly=yes`; preserve uncommitted work. Do not modify main, install software, change credentials, force-push, incur costs or merge PRs. Publication and execution require the user's Stage 74 request.

Success is a proved target-uniform multiplicative-kernel evaluation or a rigorous refutation with its first missing input. It is not automatically a simultaneous-primality theorem.
