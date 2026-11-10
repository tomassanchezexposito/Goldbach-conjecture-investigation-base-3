# Stage 65 — Reflected prime positions, wheel 210, and anchored correlations

**Status:** exact coordinate and combinatorial identities; no lower bound for a true-prime correlation.

## Original three cases and the residual target

The repository statement remains: every even $N>2$ should satisfy at least one of (i) $N=p+1$, (ii) $N=2p$, or (iii) $N=p+q$ for distinct primes $p<q$. Its equidistance condition is algebraically equivalent to $p+q=N$. The residual set is exactly
\[
H=\{N\geq4:N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\}.
\]
On $H$, only case (iii) remains, so the obligation is $R(N)>0$ for every $N\in H$, where $R(N)$ counts unordered distinct prime pairs. This remains open.

The original position coordinates are $p=3+2a$ and $q=3+2b$ with $a,b\geq0$ and
\[
a+b=N/2-3,\qquad b=N/2-3-a.
\]
Thus the reflection positions are precisely $\{3+2a,\,N-(3+2a)\}$. The coordinates are not ternary digits and impose no common-difference-three prime theorem. The prime 2 is separate: for even $N>4$, $N-2$ is even and exceeds 2, so 2 cannot be in a representation; at $N=4$, $2+2$ is the excluded equal-prime diagonal. On $H$, $N/2$ composite independently excludes that diagonal. The small prime 3 remains a genuine candidate and cannot simply be removed by a wheel sieve.

## Exact local and full factors

For any even $t$, the wheel count is
\[
A_{210}(t)=\#\{x\pmod{210}:(x,210)=1,\ (t-x,210)=1\}
=\prod_{\ell\in\{2,3,5,7\}}\begin{cases}
\ell-1,&\ell\mid t,\\
\ell-2,&\ell\nmid t.
\end{cases}
\]
This is an exact CRT count of locally admissible residue classes, not of primes. The conventional product constant and full even Goldbach singular series are
\[
C_2:=\prod_{\ell>2}\left(1-\frac1{(\ell-1)^2}\right),\qquad
\mathfrak S(t)=2C_2\prod_{\substack{\ell\mid t\\\ell>2}}\frac{\ell-1}{\ell-2}.
\]
Only divisors beyond 7 contribute factors beyond the wheel. Both $A_{210}$ and $\mathfrak S$ depend on divisibility of $t$, while membership in $H$ also depends on primality/factorization of $t-1$ and $t/2$.

The exact inherited counterexample is $210,420$: both are multiples of 210 and have $A_{210}=48$, and both have the same full singular-series value because their odd prime divisors are exactly $3,5,7$; their common finite odd factor is $16/5$. Yet $210\in H$ since $209=11\cdot19$ and $105=3\cdot5\cdot7$, while $420\notin H$ since $419$ is prime. These identities refute recovery of residual status from either factor alone. They do not refute stronger estimates using the extra arithmetic of $N-1$ and $N/2$.

## M1 and Stage 57 contractions

For distinct even targets $n<m$, let $S_{n,m}$ count pairs of distinct unordered representations sharing exactly one prime position, and let $Q_4(n,m)$ count pairs with four distinct prime positions. The Stage 63 M1 partition, whose explicit examples and multiplicities were audited in Stages 63–64, is
\[
R(n)R(m)=S_{n,m}+Q_4(n,m).
\]
A common prime $x$ forces the other two primes to be $n-x$ and $m-x$ and is unique; hence there is no orientation factor. For one target,
\[
R(n)^2=R(n)+Q_4(n,n),
\]
where the first term counts the diagonal identical representation and $Q_4(n,n)$ counts ordered disjoint pairs. The weighted versions insert the corresponding prime-log weights and retain the same partition.

Stage 57 expands the shifted product into four shared-position classes $S_{LL},S_{LH},S_{HL},S_{HH}$ plus the four-distinct term. These exact contractions can sharpen a proposed correlation calculation, but they do not give a sign after centering or a positive lower bound for $Q_4$. If $R(n)=0$, then $R(n)R(m)=0$, and both nonnegative raw correlation terms vanish. A claimed lower bound obtained by anchoring on a representation of $n$ assumes the very existence it is meant to prove. An independently established lower bound on a true-prime quadruple sum would be useful, but modular admissibility counts only residue patterns and does not provide it.

## Residual factorizations do not supply a prime correlation

Knowing that $N-1$ and $N/2$ are composite removes cases (i) and (ii); it does not force either endpoint of any reflected pair to be prime. A CRT count for the simultaneous residues of $3+2a$, $N-(3+2a)$, or four shifted positions is an exact local density. A sieve upper bound counts surviving candidates from above. Neither supplies the target-specific lower bound for the number of simultaneous prime values. No signed arithmetic gain from the two residual factorizations is derived in this stage.
