# Stage 61 — signed pointwise correlations of genuine primes

**Conclusion:** the three-target signed path expression has an exact expansion with explicit diagonal, shared-prime, and four-distinct contributions. Candidate-position bounds alone do not make it positive. A conditional local-uniformity estimate with relative error at most $1/3$ would make it strictly positive, but proving such an estimate uniformly would already be a major pointwise binary-prime result. The original three-case conjecture remains open.

## 1. Scope, definitions, and preserved target

The author's statement is retained without alteration: for each even $N>2$, at least one of (i) $N=p+1$ with $p$ prime, (ii) $N=2p$ with $p$ prime, or (iii) $N=p+q$ with distinct primes $p<q$ and $N-2p=2q-N$ holds. The equality in (iii) is equivalent to $p+q=N$; it is not additional arithmetic information. The cases need not be disjoint.

The residual set and counts are

$$H=\{N\ge4:N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\},$$

$$R(n)=\#\{(p,q):p<q,\ p,q\text{ prime},\ p+q=n\},\qquad
A_{210}(n)=\prod_{\ell\in\{2,3,5,7\}}(\ell-\nu_\ell(n)),\qquad
X_n=\frac{R(n)}{A_{210}(n)},$$

where $\nu_\ell(n)=1$ if $\ell\mid n$ and $2$ otherwise. $A_{210}$ counts locally admissible residue positions, not prime pairs. For even $n$, $A_{210}(n)\ge15$. In a distinct-prime representation of an even target, neither prime is 2. Primes 3, 5, and 7 are retained in every count; none is discarded as an asymptotic exception.

For $N\in H$, the first two cases of the author's statement are excluded, so the remaining obligation is $R(N)>0$. This stage does not assume such a representation at any target.

## 2. PROVED MATHEMATICAL LEMMA — exact signed path identity

Set

$$t_-=N-2,\quad t_0=N,\quad t_+=N+2,\qquad
a=X_{t_-},\quad b=X_{t_0},\quad c=X_{t_+},$$

$$\mu=\frac{a+b+c}{3},\qquad E=(a-b)^2+(b-c)^2,\qquad D_N=\mu^2-\frac29E.$$

Direct expansion gives the exact quadratic identity

$$D_N=\frac{-a^2-3b^2-c^2+6ab+2ac+6bc}{9}.$$

Let $R_i=R(t_i)$ and $A_i=A_{210}(t_i)$ for $i\in\{-,0,+\}$. At a single target, ordered pairs of representations split into the identical-representation diagonal and four-distinct prime values:

$$R_i^2=R_i+Q_{ii},\qquad Q_{ii}=R_i(R_i-1).$$

The latter count is an ordered pair of distinct unordered representations. If two representations at the same target shared a prime, equality of their sums would force the other prime to agree, so the representations would be identical. Thus no one-prime-sharing term is missing from $Q_{ii}$.

For $i<j$, classify an ordered pair of representations at $t_i<t_j$ by the shared low/low, low/high, high/low, or high/high prime position; call these counts $S_{ij}^{LL},S_{ij}^{LH},S_{ij}^{HL},S_{ij}^{HH}$. Let $Q_{ij}$ count the four-distinct cases. The classes are disjoint and exhaustive:

$$R_iR_j=S_{ij}^{LL}+S_{ij}^{LH}+S_{ij}^{HL}+S_{ij}^{HH}+Q_{ij}.$$

For ordered pairs $p<q$ at the lower target and $r<s$ at the higher target, $S_{ij}^{LH}=0$: $p=s$ would imply $r<p<q$ and hence $r+s<p+q$, contrary to $t_j>t_i$. Two shared positions would imply the same unordered pair and therefore the same target. These statements include the small-prime cases exactly.

Substituting these identities into the signed quadratic form yields the fully indexed identity

$$\begin{aligned}
9D_N={}&-\frac{R_-+Q_{--}}{A_-^2}
-3\frac{R_0+Q_{00}}{A_0^2}
-\frac{R_++Q_{++}}{A_+^2}\\
&+6\frac{S_{-0}^{LL}+S_{-0}^{LH}+S_{-0}^{HL}+S_{-0}^{HH}+Q_{-0}}{A_-A_0}\\
&+2\frac{S_{-+}^{LL}+S_{-+}^{LH}+S_{-+}^{HL}+S_{-+}^{HH}+Q_{-+}}{A_-A_+}\\
&+6\frac{S_{0+}^{LL}+S_{0+}^{LH}+S_{0+}^{HL}+S_{0+}^{HH}+Q_{0+}}{A_0A_+}.
\end{aligned}$$

The three $LH$ terms vanish by the preceding ordering argument. In this expression the negative terms are the same-target diagonal and four-distinct contributions; the positive terms are the shared-prime contractions and four-distinct correlations between different targets. Positivity requires the weighted sum of all three off-diagonal target products to exceed all three negative same-target terms. Neither the sign nor the needed dominance follows from the partition identity.

Equivalently, the exact strict inequality needed for the Stage 60 path certificate is

$$\begin{aligned}
&6\frac{R_-R_0}{A_-A_0}+2\frac{R_-R_+}{A_-A_+}+6\frac{R_0R_+}{A_0A_+}\\
&\hspace{1cm}>\frac{R_-^2}{A_-^2}+3\frac{R_0^2}{A_0^2}+\frac{R_+^2}{A_+^2}.
\end{aligned}$$

It is exactly equivalent to $D_N>0$, not an independent arithmetic estimate. If $R_0=0$, it reduces to

$$9D_N=-\left(\frac{R_-}{A_-}-\frac{R_+}{A_+}\right)^2\le0,$$

so an independently established strict version would imply $R_0>0$. Establishing it from prime-distribution information, without first presuming a positive center count, is the open task.

## 3. PR #9 target-index correction

The Stage 60 prose must be read with its target indices attached. By definition, $Q_4(n,m)>0$ for a specific pair of targets means there is a representation at $n$ and a representation at $m$ with four distinct prime values. Therefore:

- $Q_4(N,M)>0$ **does** entail $R(N)>0$ and $R(M)>0$ when its first indexed target is exactly $N$.
- $Q_4(N-2,N+2)>0$ entails representations only at $N-2$ and $N+2$; it does not by itself entail $R(N)>0$.
- A pointwise lower bound for an outer or otherwise off-center correlation cannot be relabeled as a center-target lower bound. A positive lower bound for a correlation whose indexed targets include $N$ would be strong enough, but proving it independently is already sufficient to prove the target representation.

This corrects the ambiguous Stage 60 sentence suggesting generally that a positive $Q_4$ “alone” cannot force $R(N)>0$. The implication depends on which targets index that $Q_4$ term. No claim is made that an actual Goldbach counterexample supplies a counterexample to the off-center implication; the distinction is about what follows from the definitions and indices.

## 4. REFUTED CLAIM — candidate bounds cannot force signed positivity

Stage 60 proves the unconditional candidate-position upper bound $0\le R(n)\le B(n)=\lfloor(n-4)/4\rfloor$. The wheel contributes the exact positive scale factors $A_{210}(n)$ but supplies no lower bound on the number of genuine prime pairs. For every sufficiently large even $N$, the abstract nonnegative assignment

$$R(N-2)=1,\qquad R(N)=0,\qquad R(N+2)=1$$

fits all three candidate upper bounds. Its normalized center is zero, and the exact identity above gives

$$D_N=-\frac19\left(\frac1{A_{210}(N-2)}-\frac1{A_{210}(N+2)}\right)^2\le0.$$

This is a logical countermodel to a deduction from the wheel factors and candidate caps. It is **not** a claim that the assigned counts are realized by primes, and is not a counterexample to Goldbach.

For a concrete exact instance in the computation, $N=100\in H$, the targets are $98,100,102$, the wheel factors are $18,20,30$, and the candidate caps are $23,24,24$. The abstract assignment $(1,0,1)$ gives

$$ (X_{98},X_{100},X_{102})=(1/18,0,1/30),\qquad D_{100}=-1/18225.$$

Thus the finite wheel and Stage 60 upper bounds permit a zero center and do not make the signed certificate positive.

## 5. CONDITIONAL STATEMENT — quantified local-uniformity route

Suppose for some $\Lambda_N>0$ the three normalized counts obey

$$X_{N+j}=\Lambda_N(1+\epsilon_{N,j}),\qquad |\epsilon_{N,j}|\le\eta,\qquad j\in\{-2,0,2\}.$$

The quadratic identity gives

$$\frac{D_N}{\Lambda_N^2}
=1+\frac23(\epsilon_{N,-2}+\epsilon_{N,0}+\epsilon_{N,2})
+\frac{-\epsilon_{N,-2}^2-3\epsilon_{N,0}^2-\epsilon_{N,2}^2
+6\epsilon_{N,-2}\epsilon_{N,0}+2\epsilon_{N,-2}\epsilon_{N,2}
+6\epsilon_{N,0}\epsilon_{N,2}}9.$$

By the triangle inequality,

$$\frac{D_N}{\Lambda_N^2}\ge1-2\eta-\frac{19}{9}\eta^2.$$

Consequently, if $\eta\le1/3$, then

$$D_N\ge\frac{8}{81}\Lambda_N^2>0,$$

which implies $R(N)>0$ by the sharp three-vertex path inequality. More explicitly, if an independently proved estimate supplied a common positive $\Lambda_N$ and $|\epsilon_{N,j}|\le C/\log N$ for every even $N\ge N_0$ and all three shifts, then every even

$$N\ge N_1:=\max\{N_0,\lceil e^{3C}\rceil\}$$

would satisfy the certificate. The finite residual targets below $N_1$ would still require exact verification.

This is a conditional theorem only. The required uniform approximation is not established here; if proved, it would itself be a very strong pointwise theorem for binary prime correlations. The calculation does not manufacture such an estimate from an average or from wheel admissibility.

## 6. ESTABLISHED EXTERNAL THEOREMS AND METHOD COMPARISON

The background results below are stated only at the strength relevant to this task.

1. **Binary circle-method framework.** Hardy and Littlewood's 1923 work gives the conjectural singular-series main term for Goldbach representations; it is not an unconditional binary Goldbach theorem. A prime-only Fourier coefficient identity is exact, but a pointwise proof requires a major-arc lower bound and a minor-arc error smaller than the main term at each target. An averaged minor-arc bound does not exclude a sparse exceptional target.
2. **Exceptional sets.** Montgomery and Vaughan, “The exceptional set in Goldbach's problem,” *Acta Arithmetica* 27 (1975), prove an unconditional exceptional-set result for binary Goldbach: the exceptional even integers have density zero (indeed their method gives a power-saving exceptional-set bound). Such a statement permits exceptional integers and does not imply that every member of the specified residual set $H$ is represented. Bhowmik and Grimmelt, “The exceptional set of the Goldbach problem,” *Analysis Mathematica* 52 (2026), 767–808, DOI 10.1007/s10476-026-00191-z, provide further explicit major-arc and exceptional-set analysis; an exceptional-set estimate is still not a zero-exception pointwise theorem.
3. **Sieve and parity.** Chen's theorem (J. R. Chen, “On the representation of a large even integer as the sum of a prime and the product of at most two primes,” *Scientia Sinica* 16 (1973), 157–176) gives a prime plus a number with at most two prime factors for every sufficiently large even integer. The second summand is not thereby proved prime. The parity obstruction explains why broad sieve lower bounds at this level do not automatically isolate two genuine primes. It is a limitation of sieve methods, not a theorem that all possible methods fail.
4. **Related exceptional-set work.** Grimmelt and Teräväinen, “The Exceptional Set in Goldbach's Problem with two Chen Primes,” arXiv:2508.16400 (2025, revised 2026), concerns Chen-prime summands and exceptional sets; it is not a binary Goldbach theorem.

Thus available average/exceptional-set information, Chen-type almost-prime results, and major-arc formulae do not provide the required signed inequality for each $N\in H$. The residual restrictions $N-1$ composite and $N/2$ composite have not been shown here to eliminate the exceptional set or remove the sieve parity issue.

## 7. FINITE COMPUTATIONAL OBSERVATION

`compute_stage61.py` uses a sieve and exact `Fraction` arithmetic on the focused centers $8,10,20,34,50,100,200,500$, with targets no larger than 502. For each triple it computes true prime representations, exact wheel factors, the mean, path energy, $D_N$, same-target diagonal/four-distinct splits, and all three shifted shared-position/four-distinct partitions. It also records every signed component in $9D_N$.

`verify_stage61.py` is independent: it uses trial division rather than a sieve, direct enumeration of residues modulo 210 rather than the product formula, and a set-intersection classifier for shared prime positions. It recomputes all counts and rational identities from scratch. It also checks the $N=100$ abstract zero-center model and all 27 endpoint triples in the relative-error grid $\epsilon_j\in\{-1/3,0,1/3\}$. Its machine-readable output is saved in `stage61_verification.json`.

Exact output is in `stage61_exact_results.json`. The eight target triples include two centers in $H$ and 128 representation-count incidences across the 24 target slots (overlaps across triples are intentional). All 8 signed component identities pass the independent verifier. The exact grid minimum is $4/9$; the report's lower bound $8/81$ is conservative and is proved analytically, not inferred from this grid. These are finite checks only. No broad Goldbach sweep was run.

Reproduce from the repository root:

```sh
python3 -B results/stage61/compute_stage61.py
python3 -B results/stage61/verify_stage61.py
```

Both programs use only the Python standard library. The producer overwrites the exact result JSON deterministically; the verifier reads it and independently recomputes the stated checks.

On the current environment, one measured run took about 0.20 seconds for the producer and 0.20 seconds for the independent verifier; these small timings are machine- and load-dependent. The largest target was 502, and no additional software or external services were used for the computation.

## 8. OPEN PROOF OBLIGATION AND NEXT STEP

The first missing arithmetic input is a non-circular pointwise estimate for the signed combination

$$6\frac{R_-R_0}{A_-A_0}+2\frac{R_-R_+}{A_-A_+}+6\frac{R_0R_+}{A_0A_+}
-\frac{R_-^2}{A_-^2}-3\frac{R_0^2}{A_0^2}-\frac{R_+^2}{A_+^2},$$

uniformly positive for every sufficiently large $N\in H$, with explicit constants and an effective cutoff. Equivalently, one needs genuine-prime information strong enough to dominate the negative same-target diagonal and four-distinct terms by the indexed off-diagonal contractions and four-prime correlations. Existing candidate caps, positive averages, exceptional-set estimates, heuristic singular series, or modular survivors do not yield this pointwise dominance.

No actual counterexample to the universal three-case conjecture is known from these computations. The author’s three cases, the residual set, and the non-circular requirement are preserved. Universal coverage remains unproved.

## 9. Evidence labels

- **PROVED MATHEMATICAL LEMMA:** exact signed path expansion; exact same-target and distinct-target configuration partitions; $D_N\le0$ whenever the center count is zero; relative-error implication with the stated constants.
- **ESTABLISHED EXTERNAL THEOREM:** Hardy–Littlewood conjectural framework (not a theorem of binary Goldbach); Montgomery–Vaughan exceptional-set theorem; Chen prime-plus-almost-prime theorem. Their limitations are stated above.
- **FINITE COMPUTATIONAL OBSERVATION:** eight focused target triples up to 502 and 27 exact rational error-grid checks, verified by independent routines.
- **REFUTED CLAIM:** the wheel factors and candidate upper bounds alone force $D_N>0$ or exclude a zero center; off-center $Q_4(N-2,N+2)>0$ alone forces $R(N)>0$.
- **CONDITIONAL STATEMENT:** a common positive local model with relative error at most $1/3$ gives $D_N\ge8\Lambda_N^2/81>0$; a $C/\log N$ error gives the displayed effective threshold.
- **OPEN PROOF OBLIGATION:** establish an independent pointwise true-prime estimate proving strict signed dominance for every sufficiently large residual target, then verify the finite remainder.
