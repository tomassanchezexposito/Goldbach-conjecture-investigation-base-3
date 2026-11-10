# Stage 68 M4 — arithmetic structure and the pointwise sign gap

## Verdict

No new inequality for genuine primes was obtained that improves the unrestricted complex-$L^2$ bounds of M1–M3. The strongest result here is a set of exact reductions and refutations of plausible but invalid transfers from coefficient positivity, parity, local congruences, or four-prime nonnegativity to an individual target. The remaining obstruction is a target-uniform signed minor-arc estimate, not another Gram identity.

The original three-case statement is unchanged: for even $N>2$, at least one of $N=p+1$, $N=2p$, or $N=p+q$ with genuine primes $p<q$ should hold. On $H$, the first two cases fail and the unresolved requirement is $R(N)>0$.

## Lemma 5.1 — coefficient positivity does not survive restriction to minor arcs

Let $S(alpha)=\sum_n c_ne(n\alpha)$ with finitely supported real coefficients $c_n\ge0$. Its full square coefficient is
\[
r(N)=\sum_{u+v=N}c_uc_v\ge0.
\]
For a measurable set $E\subset\mathbb T$, the restricted coefficient
\[
m_E(N)=\int_E S(\alpha)^2e(-N\alpha)\,d\alpha
\]
has no such sign implication: the integrand coefficient polynomial is multiplied by an indicator whose Fourier coefficients can have either sign. Explicitly, take $S=e(3\alpha)+e(5\alpha)$ and $N=28$. Then $S^2=e(6\alpha)+2e(8\alpha)+e(10\alpha)$, so $r(28)=0$. On the symmetric interval $M=[-1/88,1/88]$ the restricted major coefficient is
\[
a_M(28)=\int_M\left(e(-22\alpha)+2e(-20\alpha)+e(-18\alpha)\right)d\alpha>0,
\]
because each real part is nonnegative throughout $M$ and strictly positive in its interior. Hence for the complementary set $E=\mathbb T\setminus M$, $m_E(28)=-a_M(28)<0$.

Here $28\in H$, but this is an **artificial sparse-support countermodel**, not a prime counterexample: the support $\{3,5\}$ is not the set of all primes in a smooth interval, and the actual prime pair $5+23=28$ exists. It refutes only the proposed inference from nonnegative coefficients and omitted target frequency to a nonnegative restricted coefficient. A theorem specific to the complete genuine-prime support would need additional arithmetic input.

## Lemma 5.2 — parity symmetry is exact globally and need not persist on the chosen arcs

If $S$ is supported on odd integers, then $S(\alpha+1/2)=-S(\alpha)$ and $S(\alpha+1/2)^2=S(\alpha)^2$. Therefore every odd Fourier coefficient of the *full* square vanishes. For an arbitrary measurable restriction $E$, however,
\[
\widehat{1_ES^2}(n)=(-1)^n\widehat{1_{E-1/2}S^2}(n),
\]
which only implies vanishing for odd $n$ when $E$ is itself invariant under translation by $1/2$ (or a suitable paired sum is used).

For rational cores centered at reduced $a/q$, translation by $1/2$ reduces to denominator $q$ when $q$ is even and to denominator $2q$ when $q$ is odd. The new radius in the prescribed family is then respectively $P/(qX)$ or $P/(2qX)$; for odd $q$, the translated center may also fall outside the denominator cutoff $q\le P$. Consequently the union of these cores is not generally translation invariant. Pairing an arc with its translate can restore a symmetry for the *paired region*, but if one member is major and the other minor this transfers a term across the partition. It gives no sign or size bound for the full minor coefficient without control of the unmatched pieces.

For $w\in C_c^\infty((0,1))$, put $\alpha_w=\inf\operatorname{supp}w>0$. The smooth polynomial excludes the prime 2 once $2/X<\alpha_w$, i.e. $X>2/\alpha_w$. This is the actual support-dependent threshold; no numerical support endpoint is assumed.

## Lemma 5.3 — base-3 reflection is an exact reindexing, not a distribution result

For odd primes write $p=3+2a$ with integer $a\ge0$; the exceptional prime 3 is exactly $a=0$. For a pair summing to even $N$,
\[
a+b=N/2-3=:K.
\]
Thus reflection is $b=K-a$. For any finite coefficient sequence $c_a$, the reflected convolution coefficient is the coefficient of $z^K$ in $(\sum_ac_az^a)^2$; its associated exponential phase is $\sum_ac_ae(2a\alpha)$ up to the fixed phase $e(6\alpha)$. This is a change of coordinates and contains no lower bound for a coefficient.

The small-prime restrictions can be written exactly. For $p=3+2a>7$, avoiding divisibility by $3,5,7$ requires respectively
\[
a\not\equiv0\pmod3,\qquad a\not\equiv1\pmod5,\qquad a\not\equiv2\pmod7.
\]
For the reflected position $b=K-a$, the same exclusions apply with $a$ replaced by $K-a$. At each of the moduli $3,5,7$, the forbidden residues for $a$ are $0$ and $K$ translated by the appropriate offset; at most two residues are excluded, so a locally surviving residue exists. CRT combines these local choices modulo $105$ (and the parity is already built into $p=3+2a$). This is only local admissibility, not primality. The factors at 2,3,5,7 and their exceptional prime values must be separated when using a wheel factor; Stage 66's exact wheel normalization is not upgraded here.

The conditions $N-1$ composite and $N/2$ composite define the residual set; neither imposes a new congruence on $a$ beyond the sum condition and the stated local exclusions. The first condition excludes $p=N-1$ in the $N=p+1$ case; the second excludes the diagonal $p=q=N/2$. Neither states how often admissible $a$ give two primes.

## Lemma 5.4 — four-distinct nonnegativity has no center positivity content

For distinct even targets $u,v$, Stage 63 partitions pairs of unordered representations by whether they share a prime position:
\[
R(u)R(v)=S_{u,v}+Q_4(u,v),
\]
where $S_{u,v}\ge0$ counts exactly one shared prime and $Q_4(u,v)\ge0$ counts four distinct prime positions. On the diagonal, $R(u)^2=R(u)+Q_4(u,u)$ with the stated ordered-pair convention and no diagonal representation included in $R$.

These identities are exact but do not provide a positive lower bound for either term. In particular, if $R(N)=0$, then $R(N)R(N+j)=0$, so the identity forces both nonnegative pieces to vanish; it does not contradict a positive correlation at other targets. A proposed lower bound $Q_4(N,N+j)>0$ would itself imply $R(N)>0$, since $Q_4$ counts a representation at $N$, and therefore is precisely the missing pointwise theorem. Proving it by selecting a prime pair at $N$ would be circular.

The analytic integral $\int |S_w|^4$ expands into prime quadruples with a **difference equality** $p_1+p_2=p_3+p_4$ after integration over the full circle. The Goldbach pair count at a fixed target instead imposes the **sum equality** $p_1+p_2=N$. Arc restriction inserts a Fourier kernel and permits signed cross terms, so no term-by-term nonnegative identification with $Q_4(u,v)$ follows. The first invalid step in such an identification is replacing the kernel's signed Fourier coefficients by a nonnegative count.

## Logical-strength table

| Candidate input or observation | What follows rigorously | Relation to the universal target | Status |
|---|---|---|---|
| $c_n\ge0$ for prime-polynomial coefficients | Full square coefficients are nonnegative | Restriction to minor arcs can have either sign | PROVED; sparse countermodel above |
| Odd-prime half-periodicity | Full odd Fourier coefficients of $S_w^2$ vanish | A nonsymmetric major/minor restriction need not inherit it | PROVED identity; no target gain |
| Base-3 reflection and wheel admissibility | Exact residue exclusions and reflected index | No simultaneous-primality frequency or lower bound | PROVED reindexing; arithmetic distribution OPEN |
| $Q_4(u,v)\ge0$ | Exact decomposition of products of representation counts | A positive lower bound involving target $N$ implies the desired representation | Identity PROVED; lower bound OPEN and potentially circular |
| Global prime fourth moment | Exceptional-set or aggregate energy information | Does not exclude an isolated target | EXTERNAL CONDITIONAL input; insufficient |

No argument in this section assumes a representation at the target. The unresolved genuine-prime question is a uniform lower bound for a signed coefficient or an equivalent genuinely independent estimate strong enough to force a representation.
