# Stage 62 — An exact obstruction to wheel-210-only local smoothness

**Status:** proved elementary/standard-theorem consequence about the *arithmetic Goldbach singular series*, conditional interpretation for the conjectured prime-pair asymptotic, and finite exact examples. **NOT** a proof or disproof of the author's universal three-case conjecture.

## Research inheritance

Start from the Stage 61 signed local certificate, its exact verified true-prime correlations, and the Stage 60 integrated record. The original residual set remains
$$
H=\{N\ge4:\ N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\}.
$$
Let $R(N)$ count unordered *distinct genuine-prime* pairs summing to $N$, and $A(N)=A_{210}(N)$ count admissible residues modulo $210$. $A(N)$ is NOT a prime count.

Stage 61 obtained an exact signed quadratic form $D_N=\mu_N^2-\tfrac29E_N$, but no unconditional estimate proving $D_N>0$ for every $N\in H$. It also stated a **conditional** hypothesis that all three neighboring normalized true-prime counts lie within relative $1/3$ of one common positive value.

## Definition — the arithmetic singular-series factor (not actual representations)

For even $n\ge4$ define
$$
F(n)=\prod_{\substack{\ell\mid n\\ \ell>2\\\ell\ \mathrm{prime}}}
\frac{\ell-1}{\ell-2},\qquad
\mathfrak S(n)=2C_2F(n),\qquad
C_2=\prod_{\ell>2}\left(1-\frac1{(\ell-1)^2}\right)>0.
$$
The finite product $F(n)$ is an exact, unconditional multiplicative function. $\mathfrak S(n)$ is the conventional Hardy–Littlewood Goldbach singular-series arithmetic factor; it is **not** the proven asymptotic for $R(n)$.

For even $n$, the exact wheel factor satisfies $15\le A_{210}(n)\le48$. The wheel captures only local primes $2,3,5,7$, whereas $F(n)$ contains **all** odd prime divisors of $n$.

## Theorem 62.1 — unbounded normalized singular-series jumps on H (PROVED)

**Claim.** For every real $T>0$, there exist infinitely many even integers $N\in H$ such that
$$
\boxed{\frac{\mathfrak S(N)/A_{210}(N)}
{\mathfrak S(N+2)/A_{210}(N+2)}>T.}
$$
In particular, wheel-210 normalization alone does not make the arithmetic singular-series factor uniformly smooth between consecutive even integers, even on the author's residual set.

**Proof.** Let $P$ be a finite set of primes $\ell\ge11$, with $M=\prod_{\ell\in P}\ell$. Choose a residue $a\bmod 5M$ satisfying
$$
a\equiv1\pmod M,\qquad a\equiv4\pmod5.
$$
The Chinese remainder theorem gives a unique residue and $\gcd(a,5M)=1$. Dirichlet's theorem on primes in arithmetic progressions supplies infinitely many primes $q\equiv a\bmod 5M$. Choose $q$ sufficiently large. Set $N=2(q-1)$. Then $N/2=q-1$ is even and greater than two, hence composite, and $N-1=2q-3>5$ is divisible by five, hence composite. Thus $N\in H$.

Every $\ell\in P$ divides $q-1$, hence divides $N$, and therefore
$$
F(N)\ge\prod_{\ell\in P}\frac{\ell-1}{\ell-2}.
$$
But $N+2=2q$ has exactly one odd prime divisor, $q$, so
$$
F(N+2)=\frac{q-1}{q-2}<2.
$$
The common constant $2C_2$ cancels. Since $15\le A_{210}(\cdot)\le48$,
$$
\frac{\mathfrak S(N)/A(N)}{\mathfrak S(N+2)/A(N+2)}
\ \ge\ \frac{15}{96}
\prod_{\ell\in P}\frac{\ell-1}{\ell-2}.
$$
As $P$ ranges over increasingly long initial segments of the primes at least 11, the product diverges, since
$$
\log\!\prod_{\ell\in P}\left(1+\frac1{\ell-2}\right)
\sim\sum_{\ell\in P}\frac1\ell\longrightarrow\infty
$$
by Euler's theorem on divergent prime reciprocals (or just lower-bound its logarithm by a fixed multiple of $1/\ell$ for large $\ell$). For each sufficiently large $P$ the lower bound exceeds $T$, and Dirichlet gives infinitely many suitable $q$, hence infinitely many such $N$. QED.

**Logical scope:** This is a theorem about the *singular-series function*. It does **not** prove that actual $R(N)$ has the same jump. That further claim requires a highly nontrivial, pointwise Goldbach asymptotic, which remains unproved.

## Strengthening 62.1A — exactly identical wheel-210 factors (PROVED)

The preceding theorem holds **even if one insists on**
$$
\boxed{A_{210}(N)=A_{210}(N+2)=15.}
$$
Indeed, keep the same finite set of primes $P\ge11$ and impose the stronger simultaneous congruences
$$
q\equiv2\pmod3,\qquad q\equiv4\pmod5,\qquad
q\equiv2\pmod7,\qquad q\equiv1\pmod{\prod_{\ell\in P}\ell}.
$$
The Chinese remainder theorem gives a reduced residue class modulo $105\prod_{\ell\in P}\ell$, so Dirichlet supplies infinitely many primes $q$ in it. Setting $N=2(q-1)$ again yields $N\in H$ because $N/2=q-1$ is even and composite and $N-1=2q-3$ is divisible by 5 and larger than 5. The congruences give, respectively,
$$
N\equiv2\pmod3,\ 1\pmod5,\ 2\pmod7,\qquad
N+2\equiv1\pmod3,\ 3\pmod5,\ 4\pmod7.
$$
Thus neither target is divisible by 3, 5 or 7, and both have wheel count $1\cdot1\cdot3\cdot5=15$. The normalized series ratio is therefore exactly $F(N)/F(N+2)$, and it is at least
$$
\frac{q-2}{q-1}\prod_{\ell\in P}\frac{\ell-1}{\ell-2}
\ \ge\ \frac12\prod_{\ell\in P}\frac{\ell-1}{\ell-2},
$$
which is unbounded as before. This proves that **even identical wheel factors cannot control the higher-prime singular-series discrepancy**. No claim about the actual prime-pair counts $R(N)$ follows.

## Corollary 62.2 — obstruction to a common 1/3 baseline for the singular-series model (PROVED)

For any two positive numbers $u,v$ satisfying $u,v\in[\tfrac23\Lambda,\tfrac43\Lambda]$ for one $\Lambda>0$, we have $u/v\le2$. But by Theorem 62.1, infinitely many $N\in H$ satisfy
$$
\frac{\mathfrak S(N)/A(N)}{\mathfrak S(N+2)/A(N+2)}>2.
$$
Consequently, **there is no universally valid common-relative-error-$1/3$ baseline for the wheel-normalized singular-series model** at all such adjacent target pairs.

If one additionally assumes the *unproved* Hardy–Littlewood pointwise asymptotic for genuine prime pairs,
$$
R(n)\sim\frac12\,\mathfrak S(n)\frac{n}{(\log n)^2}
\quad\text{uniformly at all sufficiently large even }n,
$$
then the same model-dependent incompatibility applies asymptotically to $X_n=R(n)/A(n)$. This conditional implication is NOT an unconditional theorem about $R(n)$.

## Proposition 62.3 — sharpened Stage 61 conditional constant (PROVED but logically insufficient)

Let $a,b,c\in[\tfrac23\Lambda,\tfrac43\Lambda]$, $\Lambda>0$, and
$$
D(a,b,c)=\frac{-a^2-3b^2-c^2+6ab+2ac+6bc}{9}.
$$
Then
$$
\boxed{D(a,b,c)\ge\frac49\Lambda^2,}
$$
and the constant $4/9$ is sharp (equality at $a=b=c=2\Lambda/3$). Proof: $\partial D/\partial a=(-2a+6b+2c)/9>0$ on the box; similarly $\partial D/\partial c>0$; and $\partial D/\partial b=\tfrac23(a+c-b)\ge0$. Thus the minimum occurs when all three coordinates take their smallest allowed value.

Stage 61's $(8/81)\Lambda^2$ bound was valid but weaker. **More important:** the hypothesis already gives $b\ge2\Lambda/3>0$, exactly the target positivity. Thus this local-uniformity assumption cannot be presented as a non-circular route to Goldbach unless independent, genuinely arithmetic evidence proves it **without assuming b positive**. A stronger deterministic constant does not remove that logical dependence.

## Why this matters to the wheel-210 program

- The exact wheel factor $A_{210}(N)$ removes only finitely many small-prime local biases.
- The infinite family in Theorem 62.1 demonstrates mathematically that **larger-prime arithmetic factors can create arbitrary local disparities** in the *expected singular-series contribution*.
- Consequently a proof strategy requiring uniformly similar raw $X_N,X_{N\pm2}$ is poorly adapted to the conventional Goldbach heuristic; even its relative-error premise entails the desired positivity.
- A better research target is a **singular-series-adjusted, independently controlled prime-correlation error** which retains the exact target $p+q=N$, handles small-prime exceptions, and does not assume the singular-series asymptotic. Such an estimate has not been obtained.

## Focused reproducible examples

\`results/stage62/verify_singular_series.py\` checks finite CRT constructions using trial-division primality, exact integer fractions, independent direct wheel enumeration, and full odd-divisor factorization for a few small sets $P$. It tests the displayed lower bound without making any unproved statement about prime-pair counts.

Computational samples are supplementary; the unboundedness theorem depends on Dirichlet's theorem and divergence of the prime reciprocal sum, **not** finite experiments.

## Sources and status

- Hardy–Littlewood (1923), *Some problems of Partitio numerorum; III*, Acta Math. 44, 1–70: conventional singular-series prediction, **conjectural** for binary prime representations.
- Dirichlet's theorem: existence of infinitely many primes in a reduced residue class; **established**.
- Euler's divergence of $\sum_{p\ \mathrm{prime}}1/p$; **established**.
- G. Bhowmik and L. Grimmelt, *The exceptional set of the Goldbach problem*, **Analysis Mathematica** 52 (2026), 767–808, DOI: 10.1007/s10476-026-00191-z: reviewed published survey/new major-arc contribution; does not establish zero exceptions.

**Next obligation:** derive or refute a *non-circular, target-anchored, uniform signed four-prime error estimate* after retaining the complete arithmetic local factors; distinguish a real prime correlation estimate from the formal singular-series model. Do not increase finite testing ranges merely to accumulate favorable observations.

## 62.4 — The full singular-series model makes the Stage 61 signed certificate negative infinitely often (PROVED model statement)

The unbounded adjacent jump in Theorem 62.1A can be strengthened to control both neighbors of the center. This diagnoses the Stage 61 certificate itself: even the conventional complete singular-series profile does not satisfy $D_N>0$ uniformly on $H$.

For an integer $y\ge11$, let
$$
P_y=\{p:11\le p\le y,\ p\text{ prime}\},\qquad
W_y=105\prod_{p\in P_y}p.
$$
Choose the reduced residue class modulo $W_y$ specified by
$$
q\equiv2\pmod3,\quad q\equiv4\pmod5,\quad q\equiv2\pmod7,
\quad q\equiv1\pmod p\quad(p\in P_y).
$$
It is reduced because every listed residue is nonzero modulo its corresponding prime. Linnik's least-prime theorem supplies a prime $q_y$ in this class with $q_y\le C W_y^L$, for absolute constants $C,L>0$. Necessarily $q_y>y$: if $q_y\le y$, it is one of 2, 3, 5, or 7, each excluded by its prescribed residue, or belongs to $P_y$, contradicting $q_y\equiv1\pmod{q_y}$. Set $N_y=2(q_y-1)$. As in Theorem 62.1A, $N_y\in H$.

Write $F_y=\prod_{p\in P_y}(p-1)/(p-2)$. Then $F(N_y)\ge F_y\to\infty$, by Euler's divergence of $\sum_p1/p$. Meanwhile $N_y+2=2q_y$, so $F(N_y+2)=(q_y-1)/(q_y-2)<2$. The odd prime divisors of $q_y-2$ are 3, 7, and primes $r>y$: divisibility by 5 is excluded by $q_y\equiv4\pmod5$, and every $p\in P_y$ is excluded by $q_y\equiv1\pmod p$. Thus
$$
F(N_y-2)=\frac{12}{5}\prod_{\substack{r\mid q_y-2\\r\text{ prime},\ r>y}}\left(1+\frac1{r-2}\right)
\le \frac{12}{5}\exp\!\left(\frac{\log(q_y-2)}{(y-1)\log y}\right).
$$
Here the number of distinct prime divisors $r>y$ is at most $\log(q_y-2)/\log y$, and each logarithmic factor is at most $1/(y-1)$. Since
$$
\log q_y\le \log C+L\log W_y\le \log C+L(\log105+y\log y),
$$
the displayed upper bound is bounded by an absolute constant for all sufficiently large $y$. This use of Linnik is only to control the size of $q_y$; Dirichlet's theorem alone would not supply the bound needed here.

Define the positive singular-series profile for the wheel-normalized count by
$$
\Phi(n)=\frac{F(n)n}{A_{210}(n)(\log n)^2}.
$$
The conjectural Hardy--Littlewood main term for $X_n=R(n)/A_{210}(n)$ is $C_2\Phi(n)$, with $C_2>0$. Since $15\le A_{210}(n)\le48$, the bounds above imply
$$
\frac{\Phi(N_y-2)}{\Phi(N_y)}\longrightarrow0,
\qquad
\frac{\Phi(N_y+2)}{\Phi(N_y)}\longrightarrow0.
$$
The remaining factors $n/(\log n)^2$ have ratios tending to 1 across shifts of 2, while the wheel-factor ratios stay bounded. Consequently, direct substitution into the exact quadratic gives
$$
\frac{D(\Phi(N_y-2),\Phi(N_y),\Phi(N_y+2))}{\Phi(N_y)^2}
\longrightarrow -\frac13.
$$
In particular, the singular-series profile has $D<0$ for all sufficiently large members of this sequence in $H$. Multiplication by the common positive constant $C_2$ does not change the sign.

**Scope.** This is an unconditional statement about the explicitly defined arithmetic profile $\Phi$, using Linnik's theorem and Euler's theorem. It is not an asymptotic formula for $R(n)$, and it does not show that actual prime-pair counts have negative $D_N$, or that any $R(N_y)$ vanishes. Rather, it proves that a pointwise approximation of all three $X$'s by this singular-series profile cannot make the Stage 61 $D_N>0$ certificate work uniformly: on this sequence the profile has the opposite sign. The certificate remains sufficient but is not necessary for $R(N)>0$, so its failure on the model is not a Goldbach counterexample.

The proof uses only the unbounded product over $P_y$, not a numerical search. The finite verifier below remains a check of examples and must not be confused with the infinite argument.

## 62.5 — Exact pointwise information a signed four-prime proof would need

For $i\in\{-,0,+\}$, let $n_-=N-2$, $n_0=N$, $n_+=N+2$. Let $\mathcal P_i$ be the set of unordered distinct genuine-prime pairs summing to $n_i$, and set $R_i=|\mathcal P_i|$, $A_i=A_{210}(n_i)$. For distinct target indices $i,j$, a shared-position configuration is specified uniquely by its common prime $x$: both $n_i-x$ and $n_j-x$ must be prime, and $x$ must differ from both $n_i/2$ and $n_j/2$ so that each representation has distinct summands. Thus its exact count is
$$
S_{ij}=\#\{x\text{ prime}: n_i-x,n_j-x\text{ prime},\ x\ne n_i/2,\ x\ne n_j/2\}.
$$
The remaining $T_{ij}=R_iR_j-S_{ij}$ ordered pairs of representations have four distinct prime positions. For a fixed target, two distinct representations cannot share exactly one prime: the common prime determines the other summand. Hence $Q_{ii}=R_i(R_i-1)$ counts precisely the ordered off-diagonal pairs with four distinct positions, while $R_i$ is the diagonal. These identities count unordered summand pairs but ordered pairs of representations, with no extra factor of two. Denote the total cross-target count by $C_{ij}=R_iR_j$. Stage 61's exact identity is
$$
\begin{aligned}
9D_N={}&-\frac{R_-+Q_{--}}{A_-^2}
-3\frac{R_0+Q_{00}}{A_0^2}
-\frac{R_++Q_{++}}{A_+^2}\\
&+6\frac{C_{-0}}{A_-A_0}
+2\frac{C_{-+}}{A_-A_+}
+6\frac{C_{0+}}{A_0A_+}.
\end{aligned}
$$
Thus independently proved lower bounds $L_{ij}(N)\le C_{ij}/(A_iA_j)$ and upper bounds $U_i(N)\ge(R_i+Q_{ii})/A_i^2$ would suffice if, uniformly for every $N\in H$,
$$
6L_{-0}(N)+2L_{-+}(N)+6L_{0+}(N)
> U_-(N)+3U_0(N)+U_+(N).
$$
The bounds must count actual prime configurations, including the shared-position contractions, and be target-specific rather than averaged. This is a legitimate arithmetic proof obligation if established independently; it does not assume $R(N)>0$ as a hypothesis. But it is a stronger signed-correlation conclusion than the desired positivity, not a weaker assumption that can be taken for free. No unconditional estimates proving this inequality on all of $H$ are obtained here.

The previous Stage 61 local-uniformity condition is explicitly circular for this purpose: $X_N\ge2\Lambda_N/3>0$, while $A_{210}(N)>0$, immediately yields $R(N)=A_{210}(N)X_N>0$. The sharpened $4\Lambda_N^2/9$ deterministic bound is correct but does not repair this implication. In addition, Sections 62.1A and 62.4 show that the conventional singular-series model has unbounded local changes and makes this particular signed certificate negative on an infinite sequence. Any approach based on the singular-series model must retain its higher-prime factors to avoid the finite-wheel mismatch; even retaining them does not provide the required positive signed margin.

## 62.6 — Reproducibility and evidence inventory

Run the producer with `python3 -B results/stage62/verify_singular_series.py`. It uses trial division, incremental CRT, direct enumeration modulo 210, factor-by-factor rational arithmetic, and checks six prefixes of $P=(11,13,17,19,23,29)$. The independent SageMath verifier is `sage -python results/stage62/verify_singular_series_sage.py`; it uses Sage primality and integer factorization, Sage's CRT routine, direct residue enumeration, and exact rational arithmetic. It checks all six emitted rows, the 27-point endpoint grid, and the exact correlation identity for 49 centers $N=4,6,\ldots,100$ (targets $N-2,N,N+2$). The Python producer took 0.214 s wall time; the Sage process took 3.288 s including interpreter startup (0.050877 s measured inside the script). Both computations use exact integer or rational arithmetic. The results and SHA-256 provenance are in `stage62_verification.json`, `sage_verification.json`, and `verification_manifest.json`.

The exact examples reach $q=21{,}750{,}492{,}479$, $N=43{,}500{,}984{,}956$, with the six-prime product lower bound $1024/1377$ for the wheel-normalized ratio; each finite example has equal wheel factors 15. These are exact finite observations only. The model-level infinite theorem in Section 62.4 is proved analytically and is not extrapolated from these samples.

## 62.7 — Remaining obstruction and status

There is no non-circular pointwise lower bound here for the genuine four-prime terms $C_{ij}$, nor a target-uniform minor-arc error that yields one. The Hardy--Littlewood singular series is an arithmetic prediction, not a proved approximation to every $R(n)$. Exceptional-set bounds allow individual exceptions; Chen-type theorems do not force the second summand prime; and the sieve parity obstruction is not removed by the restrictions defining $H$. A viable next step must find a different signed certificate robust to the large local variation, or prove the explicit target-anchored configuration inequality above directly from genuine primes. Universal coverage of the original three-case conjecture remains open.

### Added reference for Section 62.4

- Yu. V. Linnik, “On the least prime in an arithmetic progression. I. The basic theorem,” *Mat. Sbornik* 15(57) (1944), 139–178.
