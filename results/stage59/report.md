# Stage 59 — Sharp pointwise local second-moment certificate on wheel-210-normalized prime correlations

**Status:** an elementary sharp local Sobolev theorem is proved below; all prime-representation inequalities are **finite computational observations**. No unconditional universal pointwise positivity estimate has been established. This stage follows Stages 56–58.

## Definitions and relation to the author's formulation

For even integers \(N\ge4\), let
\[
H=\{N:\ N-1\text{ composite},\ N/2\text{ composite}\},
\quad
R(N)=\#\{p<q:\ p,q\text{ prime},\ p+q=N\}.
\]
Let
\[
A(N)=A_{210}(N)=\prod_{\ell\in\{2,3,5,7\}}(\ell-\nu_\ell(N)),\quad
\nu_\ell(N)=1\ \text{if}\ \ell\mid N,\ \text{and}\ 2\ \text{otherwise},
\quad X_N=R(N)/A(N).
\]
The 210-wheel count records congruence admissibility, not prime-pair existence. On \(H\), the author's unresolved third case is equivalent to \(X_N>0\).

## Theorem 59.1 — sharp pointwise energy bound (proved, all real vectors)

Let \(m\ge3\), \(v_0,\ldots,v_{m-1}\in\mathbb R\), with cyclic convention \(v_m=v_0\). Set
\[
\mu=\frac1m\sum_{j=0}^{m-1}v_j,\qquad
E=\sum_{j=0}^{m-1}(v_{j+1}-v_j)^2,\qquad
K_m=\frac{m^2-1}{12m}.
\]
For every coordinate \(i\), the **sharp inequality**
\[
\boxed{|v_i-\mu|^2\le K_m E}
\]
holds. Hence if \(\mu>\sqrt{K_m E}\), then **every coordinate is positive**, without any nonnegativity assumption.

**Proof.** Put \(u=v-\mu{\bf1}\), so \(\sum u_j=0\). Write \(L\) for the Laplacian of the cycle graph of length \(m\), including the multigraph interpretation for \(m=2\) (which is not needed here). Then \(u^TLu=E\). Fourier diagonalization gives nonzero eigenvalues \(\lambda_k=4\sin^2(\pi k/m)\), \(k=1,\ldots,m-1\). Cauchy–Schwarz on the nonconstant Fourier coefficients yields
\[
u_i^2\le\left(\frac1m\sum_{k=1}^{m-1}\frac1{\lambda_k}\right) E
=\frac{m^2-1}{12m}\,E.
\]
The last identity follows from \(\sum_{k=1}^{m-1}\csc^2(\pi k/m)=(m^2-1)/3\). It can also be checked via the electrical network resistance formula on the cycle. Equality is attained by vectors proportional to the \(i\)-th column of the cycle's Laplacian pseudoinverse plus an arbitrary constant: \(u=c L^+(e_i-\mathbf1/m)\). Thus the constant cannot be reduced. Alternatively, an elementary extremizer with \(v_0=0\) is
\[
v_j=\frac{d_j(m-d_j)}{2m},\quad d_j=\min(j,m-j),
\]
for which \(\mu^2=K_mE\) and all other entries are positive. QED.

**Independent note:** For the displayed extremizer, \(E=K_m\) and \(\mu=K_m\) (indeed \(\mu^2=K_mE\)). This was checked exactly for \(m=3,5,7,11\); the Fourier proof covers all \(m\ge3\).

## Corollary 59.2 — local normalized three-even-integer criterion (proved implication)

For even \(N\ge6\), put \(a=X_{N-2}\), \(b=X_N\), \(c=X_{N+2}\). Then
\[
\frac{(a+b+c)^2}{9}>\frac29\big((a-b)^2+(b-c)^2+(c-a)^2\big)
\quad\Longleftrightarrow\quad
\boxed{2(ab+bc+ca)>a^2+b^2+c^2}.
\]
When this inequality holds, \(b>0\), hence \(R(N)>0\). It is a **sufficient** condition, not necessary.

If \(b=0\) and \(a,c\ge0\), the difference between the right and left sides is \(a^2+c^2-2ac=(a-c)^2\ge0\); therefore the criterion cannot hold. This is the sharpness/necessity barrier for a local-zero profile.

### Exact four-prime expansion

Let \(T=\{N-2,N,N+2\}\) and \(A_t=A(t)\). Then
\[
E=\sum_{t\in T}\left(\frac{R(t+2)}{A_{t+2}}-\frac{R(t)}{A_t}\right)^2
\]
with cyclic \(t+2\) interpreted as \(N-2\) after \(N+2\). Expanding yields
\[
E=2\sum_{t\in T}\frac{R(t)^2}{A_t^2}
-2\left(\frac{R(N-2)R(N)}{A_{N-2}A_N}
+\frac{R(N)R(N+2)}{A_NA_{N+2}}
+\frac{R(N-2)R(N+2)}{A_{N-2}A_{N+2}}\right).
\]
Every \(R(t)^2\) and \(R(s)R(t)\) is an exact ordered correlation of two prime-pair representations, hence a four-position-prime count including diagonal/shared-prime contractions. For \(s\ne t\), use Stage 57's exact decomposition into \(S_{LL},S_{LH},S_{HL},S_{HH},Q_4\). For \(s=t\), the identical pair diagonal is \(R(t)\) and the off-diagonal is \(R(t)(R(t)-1)\). The formulas are identities, not analytic estimates.

## Finite exact computation and counterexample search

Two independent programs were run locally:

1. Python 3 exact sieve and \`fractions.Fraction\`, included as \`results/stage59/verify_stage59.py\`: all \(1,524\) residual \(N\in[8,4998]\) pass; the only failed certificate among all even centers in that interval is \(N=8\), which is **not** in \(H\). Includes exact trial division cross-checks, wheel residue enumeration, direct shared-prime count checks, and sharpness vectors.
2. An independently written and executed native C program with an exact sieve and integer-scaled rational comparisons, supplied as \`results/stage59/local_cert_native.c\`, checked **all even centers \(8\le N\le999998\)** with both neighbors in range. It found one failure, at \(N=8\), and **no failures for its 384,263 residual centers**. In that version the test is computed exactly after scaling all \(R(t)/A(t)\) to a common integer denominator and checking \(2(ab+bc+ca)>a^2+b^2+c^2\).

The independent C program, compiled with \`cc -O3\`, reported 1,671,838,245 enumerated unordered distinct-prime pairs with sums \(\le10^6\), 499,996 even centers checked, and one failure \(N=8\). The exact finite test is suggestive but **does not** prove the inequality beyond \(10^6\).

The diagnostic \`N=8\` uses values \(X_6=0\), \(X_8=1/15\), \(X_{10}=1/20\); the original three-case representation includes the doubled-prime mechanism for \(6\), so this failure is not relevant to \(H\).

## What is actually missing

**Open pointwise prime-correlation estimate.** Find an independent lower bound \(m_N>0\) on the *local mean* and an independent upper bound \(e_N\) on the *three-edge energy* that satisfy
\[
\mu_N\ge m_N>0,\quad E_N\le e_N,\quad m_N^2>\frac29e_N,
\qquad (N\in H)
\]
without assuming \(R(N)>0\), dividing by \(R(N)\), or computing \(R(N)\) as a premise. The proven local inequality would then imply \(R(N)>0\) at every target.

**Crucial logical limitation:** direct measurement of \(\mu_N\) and \(E_N\) requires \(R(N)\), and their positivity condition is an alternative characterization of a strong local regularity, not a new analytic bound. The arithmetic gap remains: genuine non-circular control of simultaneous prime positions and their off-diagonal correlations. Finite testing of more even targets is not a substitute.

One may use a weighted discrete graph and other shifts (e.g. 210), but any such bound must be proved independently for genuine prime counts, not inferred from wheel-admissible candidates. The optimum cycle constant shows merely sharpening the graph inequality cannot close this gap.

## Classification and next objective

- **Proved in this research:** sharp cycle graph inequality and three-position positivity implication; exact four-prime energy expansion.
- **Computational observation:** the local criterion holds in the stated finite ranges.
- **Refuted universal suggestion:** claiming the three-position criterion holds for every even center \(N\ge8\) fails at \(N=8\). No refutation on \(H\) was found in the tested range.
- **Conditional open hypothesis:** the strict local criterion holds for all \(N\in H\); this would imply the author's universal third-case coverage.
- **Next step:** bound the *signed off-diagonal* four-prime terms and the first two local moments independently of \(R(N)\), and compare the required error margin with the best known circle/sieve estimates.

This stage neither proves nor refutes Goldbach; universal coverage remains open.
