# Stage 62 — An exact obstruction to wheel-210-only local smoothness

**Status:** proved elementary/standard-theorem consequence about the *arithmetic Goldbach singular series*, conditional interpretation for the conjectured prime-pair asymptotic, and finite exact examples. **NOT** a proof or disproof of the author's universal three-case conjecture.

## Research inheritance

Start from the Stage 61 signed local certificate, its exact verified true-prime correlations, and the Stage 60 integrated record. The original residual set remains
\[
H=\{N\ge4:\ N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\}.
\]
Let \(R(N)\) count unordered *distinct genuine-prime* pairs summing to \(N\), and \(A(N)=A_{210}(N)\) count admissible residues modulo \(210\). \(A(N)\) is NOT a prime count.

Stage 61 obtained an exact signed quadratic form \(D_N=\mu_N^2-\tfrac29E_N\), but no unconditional estimate proving \(D_N>0\) for every \(N\in H\). It also stated a **conditional** hypothesis that all three neighboring normalized true-prime counts lie within relative \(1/3\) of one common positive value.

## Definition — the arithmetic singular-series factor (not actual representations)

For even \(n\ge4\) define
\[
F(n)=\prod_{\substack{\ell\mid n\\ \ell>2\\\ell\ \mathrm{prime}}}
\frac{\ell-1}{\ell-2},\qquad
\mathfrak S(n)=2C_2F(n),\qquad
C_2=\prod_{\ell>2}\left(1-\frac1{(\ell-1)^2}\right)>0.
\]
The finite product \(F(n)\) is an exact, unconditional multiplicative function. \(\mathfrak S(n)\) is the conventional Hardy–Littlewood Goldbach singular-series arithmetic factor; it is **not** the proven asymptotic for \(R(n)\).

For even \(n\), the exact wheel factor satisfies \(15\le A_{210}(n)\le48\). The wheel captures only local primes \(2,3,5,7\), whereas \(F(n)\) contains **all** odd prime divisors of \(n\).

## Theorem 62.1 — unbounded normalized singular-series jumps on H (PROVED)

**Claim.** For every real \(T>0\), there exist infinitely many even integers \(N\in H\) such that
\[
\boxed{\frac{\mathfrak S(N)/A_{210}(N)}
{\mathfrak S(N+2)/A_{210}(N+2)}>T.}
\]
In particular, wheel-210 normalization alone does not make the arithmetic singular-series factor uniformly smooth between consecutive even integers, even on the author's residual set.

**Proof.** Let \(P\) be a finite set of primes \(\ell\ge11\), with \(M=\prod_{\ell\in P}\ell\). Choose a residue \(a\bmod 5M\) satisfying
\[
a\equiv1\pmod M,\qquad a\equiv4\pmod5.
\]
The Chinese remainder theorem gives a unique residue and \(\gcd(a,5M)=1\). Dirichlet's theorem on primes in arithmetic progressions supplies infinitely many primes \(q\equiv a\bmod 5M\). Choose \(q\) sufficiently large. Set \(N=2(q-1)\). Then \(N/2=q-1\) is even and greater than two, hence composite, and \(N-1=2q-3>5\) is divisible by five, hence composite. Thus \(N\in H\).

Every \(\ell\in P\) divides \(q-1\), hence divides \(N\), and therefore
\[
F(N)\ge\prod_{\ell\in P}\frac{\ell-1}{\ell-2}.
\]
But \(N+2=2q\) has exactly one odd prime divisor, \(q\), so
\[
F(N+2)=\frac{q-1}{q-2}<2.
\]
The common constant \(2C_2\) cancels. Since \(15\le A_{210}(\cdot)\le48\),
\[
\frac{\mathfrak S(N)/A(N)}{\mathfrak S(N+2)/A(N+2)}
\ \ge\ \frac{15}{96}
\prod_{\ell\in P}\frac{\ell-1}{\ell-2}.
\]
As \(P\) ranges over increasingly long initial segments of the primes at least 11, the product diverges, since
\[
\log\!\prod_{\ell\in P}\left(1+\frac1{\ell-2}\right)
\sim\sum_{\ell\in P}\frac1\ell\longrightarrow\infty
\]
by Euler's theorem on divergent prime reciprocals (or just lower-bound its logarithm by a fixed multiple of \(1/\ell\) for large \(\ell\)). For each sufficiently large \(P\) the lower bound exceeds \(T\), and Dirichlet gives infinitely many suitable \(q\), hence infinitely many such \(N\). QED.

**Logical scope:** This is a theorem about the *singular-series function*. It does **not** prove that actual \(R(N)\) has the same jump. That further claim requires a highly nontrivial, pointwise Goldbach asymptotic, which remains unproved.

## Corollary 62.2 — obstruction to a common 1/3 baseline for the singular-series model (PROVED)

For any two positive numbers \(u,v\) satisfying \(u,v\in[\tfrac23\Lambda,\tfrac43\Lambda]\) for one \(\Lambda>0\), we have \(u/v\le2\). But by Theorem 62.1, infinitely many \(N\in H\) satisfy
\[
\frac{\mathfrak S(N)/A(N)}{\mathfrak S(N+2)/A(N+2)}>2.
\]
Consequently, **there is no universally valid common-relative-error-\(1/3\) baseline for the wheel-normalized singular-series model** at all such adjacent target pairs.

If one additionally assumes the *unproved* Hardy–Littlewood pointwise asymptotic for genuine prime pairs,
\[
R(n)\sim\frac12\,\mathfrak S(n)\frac{n}{(\log n)^2}
\quad\text{uniformly at all sufficiently large even }n,
\]
then the same model-dependent incompatibility applies asymptotically to \(X_n=R(n)/A(n)\). This conditional implication is NOT an unconditional theorem about \(R(n)\).

## Proposition 62.3 — sharpened Stage 61 conditional constant (PROVED but logically insufficient)

Let \(a,b,c\in[\tfrac23\Lambda,\tfrac43\Lambda]\), \(\Lambda>0\), and
\[
D(a,b,c)=\frac{-a^2-3b^2-c^2+6ab+2ac+6bc}{9}.
\]
Then
\[
\boxed{D(a,b,c)\ge\frac49\Lambda^2,}
\]
and the constant \(4/9\) is sharp (equality at \(a=b=c=2\Lambda/3\)). Proof: \(\partial D/\partial a=(-2a+6b+2c)/9>0\) on the box; similarly \(\partial D/\partial c>0\); and \(\partial D/\partial b=\tfrac23(a+c-b)\ge0\). Thus the minimum occurs when all three coordinates take their smallest allowed value.

Stage 61's \((8/81)\Lambda^2\) bound was valid but weaker. **More important:** the hypothesis already gives \(b\ge2\Lambda/3>0\), exactly the target positivity. Thus this local-uniformity assumption cannot be presented as a non-circular route to Goldbach unless independent, genuinely arithmetic evidence proves it **without assuming b positive**. A stronger deterministic constant does not remove that logical dependence.

## Why this matters to the wheel-210 program

- The exact wheel factor \(A_{210}(N)\) removes only finitely many small-prime local biases.
- The infinite family in Theorem 62.1 demonstrates mathematically that **larger-prime arithmetic factors can create arbitrary local disparities** in the *expected singular-series contribution*.
- Consequently a proof strategy requiring uniformly similar raw \(X_N,X_{N\pm2}\) is poorly adapted to the conventional Goldbach heuristic; even its relative-error premise entails the desired positivity.
- A better research target is a **singular-series-adjusted, independently controlled prime-correlation error** which retains the exact target \(p+q=N\), handles small-prime exceptions, and does not assume the singular-series asymptotic. Such an estimate has not been obtained.

## Focused reproducible examples

\`results/stage62/verify_singular_series.py\` checks finite CRT constructions using trial-division primality, exact integer fractions, independent direct wheel enumeration, and full odd-divisor factorization for a few small sets \(P\). It tests the displayed lower bound without making any unproved statement about prime-pair counts.

Computational samples are supplementary; the unboundedness theorem depends on Dirichlet's theorem and divergence of the prime reciprocal sum, **not** finite experiments.

## Sources and status

- Hardy–Littlewood (1923), *Some problems of Partitio numerorum; III*, Acta Math. 44, 1–70: conventional singular-series prediction, **conjectural** for binary prime representations.
- Dirichlet's theorem: existence of infinitely many primes in a reduced residue class; **established**.
- Euler's divergence of \(\sum_{p\ \mathrm{prime}}1/p\); **established**.
- G. Bhowmik and L. Grimmelt, *The exceptional set of the Goldbach problem*, **Analysis Mathematica** 52 (2026), 767–808, DOI: 10.1007/s10476-026-00191-z: reviewed published survey/new major-arc contribution; does not establish zero exceptions.

**Next obligation:** derive or refute a *non-circular, target-anchored, uniform signed four-prime error estimate* after retaining the complete arithmetic local factors; distinguish a real prime correlation estimate from the formal singular-series model. Do not increase finite testing ranges merely to accumulate favorable observations.
