# NEXT TASK — Stage 60: independent signed prime-correlation bounds for the sharp local energy certificate

**Evidence status:** analytic positivity obligation OPEN. Use the new Stage 59 theorem as an exact, sharp *conditional* certificate, never as an unconditional Goldbach proof.

## Continuity

- Read results/stage59/report.md and independently run:
  - \`python results/stage59/verify_stage59.py\`
  - \`cc -O3 -std=c11 results/stage59/local_cert_native.c -o /tmp/stage59_local_cert && /tmp/stage59_local_cert 1000000\`
- Note the source branch \`cocalc/stage59-local-second-moment\`. Stage 56–58 files and the author's original definition are preserved.
- The previous chat thread ended. Use this GitHub task as the sole durable handoff; CoCalc agent chats are not automatically synchronized with ChatGPT.

## Universal target

For even \(\,N\in H\,\) (\(N-1,N/2\) both composite), prove the existence of two distinct genuine primes summing to \(N\), using the original positional reflection formula \(p=3+2a,\ q=3+2b,\ a+b=N/2-3\). Do not assume Goldbach or any equivalent statement.

Let \(R(N)\) be the genuine unordered distinct prime pair count, \(A(N)\) the wheel-210 admissible residue count, and \(X_N=R(N)/A(N)\).

## Sharp proved Stage 59 certificate

For \(a=X_{N-2},\ b=X_N,\ c=X_{N+2}\),
\[
2(ab+bc+ca)>a^2+b^2+c^2
\quad\Longleftrightarrow\quad
(\sqrt a-\sqrt c)^2<b<(\sqrt a+\sqrt c)^2
\]
suffices for \(R(N)>0\), but is not known unconditionally for \(N\in H\). Exact finite testing through one million observed no failures among 384,263 residual centers. That is NOT a universal bound. Prove neither half by dividing by \(b\) or by calculating \(R(N)\) as a premise.

## Main analytic obligations

1. **Independent moment bounds:** specify explicit, non-circular estimates \(\mu_N\ge m_N>0\) and \(E_N\le e_N\) with \(m_N^2>(2/9)e_N\) for each sufficiently large residual \(N\), or prove such estimates cannot follow from the proposed input assumptions. All constants, uniformity and error terms must be quantified.
2. **Correlation decomposition:** expand \(E_N\) into exact products \(R(s)R(t)\), separate identical-pair diagonals, shared-prime contractions and four-distinct-prime terms for shifts 0, 2 and 4. Compute exact weighted factors \(A(s)A(t)\).
3. **Arithmetic estimate:** investigate whether currently established unconditional bounds for prime sums along these exact shifted planes yield upper bounds with signs, rather than merely absolute values/averages. Distinguish new conjectural estimates from known theorems.
4. **Sieve bridge:** express the original odd-position sieve \(p=3+2j\) and prime marker exclusion congruences exactly, and identify where survival under finite wheel/criba ceases to imply simultaneous primality.
5. **Counterexample search:** independently test any intermediate inequality. The exact 3-point criterion fails at N=8 (outside H), and no other failures were seen through 1,000,000: do not extrapolate.
6. **Alternative analytical certificate:** if moment estimates are impossible with present input, exhibit a rigorously proved conditional theorem with the narrowest precise missing prime-distribution hypothesis. Avoid restating the desired positivity as an assumption.
7. **Reproducibility:** save mathematical report, independent verifier, data and manifest with code hashes in \`results/stage60/\`. Do not run longer arbitrary Goldbach sweeps in place of proving lemmas.
8. **Review:** prepare a new branch derived from Stage 59, commit only reproducible audited files there, push it, and create a draft PR. Never merge to main without review.

## Acceptance

The result must either establish a uniform independent pointwise inequality with a positive margin and proof, or explicitly identify and quantify the first missing non-circular error estimate. Do not label any universal coverage statement proved merely because the sharp local certificate is satisfied in a long finite range.

## Stage 60 integration resolution

This parent-branch Stage 60 objective remains the governing task. The conflicting Stage 59 task protocols are cited in their source commits: `cocalc/stage59-local-second-moment` at `900cae804b76e09992aba555932bc0fd866737af` and `cocalc/stage59-sharp-local-energy` at `60fed50ca43342bd10384a05813202c79c57eab3`. Their distinct reports, experiments, proofs, and verifiers are retained under `results/stage59/`.
