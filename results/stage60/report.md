# Stage 60 — pointwise arithmetic bounds for four-position correlations

**Conclusion:** an unconditional, non-circular pointwise upper bound for the true-prime four-position counts follows from counting odd candidate positions. Its scale is too weak, and it supplies no positive lower bound for a target count or local mean. Universal positivity on the residual set remains open.

## 1. Definitions and scope

For even $N\ge4$, use the repository definitions

$$H=\{N\ge4:\ N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\},$$

$$R(N)=\#\{(p,q):p<q,\ p,q\text{ prime},\ p+q=N\},\qquad X_N=\frac{R(N)}{A_{210}(N)}.$$

For $\ell\in\{2,3,5,7\}$ set $\nu_\ell(N)=1$ if $\ell\mid N$ and $2$ otherwise. The exact local residue count is

$$A_{210}(N)=\prod_{\ell\in\{2,3,5,7\}}(\ell-\nu_\ell(N)).$$

It counts residues $a\pmod {210}$ for which both $a$ and $N-a$ are coprime to 210. For even $N$, its factors at $2,3,5,7$ are respectively $1$, either $2$ or $1$, either $4$ or $3$, and either $6$ or $5$. In particular $A_{210}(N)\ge15$. The wheel records local admissibility; it does not assert either summand is prime.

If a distinct prime pair sums to an even $N$, neither member is 2: the other member would be an even prime larger than 2, or the two members would coincide at $N=4$. Thus the actual pair positions have odd $p,q\ge3$. The primes 3, 5, and 7 remain included exactly in every representation and correlation below; no approximation removes them.

## 2. Exact four-position identities

Write $\mathcal P_n=\{(p,q):p<q,\ p,q\text{ prime},\ p+q=n\}$. At a single target,

$$R(n)^2=\sum_{(p,q),(r,s)\in\mathcal P_n}1
=R(n)+R(n)(R(n)-1).$$

The first term is the identical-representation diagonal. If two representations at the same target share one prime, their other prime is forced equal, so distinct representations share no prime. Consequently the off-diagonal term has four distinct prime values.

For distinct targets $n<m$, classify an ordered pair $((p,q),(r,s))\in\mathcal P_n\times\mathcal P_m$ by whether it shares $p=r$, $p=s$, $q=r$, or $q=s$, and let $S_{LL},S_{LH},S_{HL},S_{HH}$ count those four cases. Let $Q_4(n,m)$ count the cases with four distinct values. Two shared positions would force the same unordered pair and the same target, so these cases are disjoint and exhaustive:

$$R(n)R(m)=S_{LL}+S_{LH}+S_{HL}+S_{HH}+Q_4(n,m).$$

When $n<m$ and both pairs are in increasing order, $S_{LH}=0$: if $p=s$, then $r<p<q$ and $r+s<p+q$, contradicting $m>n$. The small primes 3, 5, and 7 are handled by these exact prime-position tests. There is no exceptional contribution from 2 to a distinct representation of an even target.

For the three-point path centered at $N$, define

$$E_P(N)=(X_N-X_{N-2})^2+(X_{N+2}-X_N)^2.$$

Expanding the squares and then substituting the identities above is an exact formula:

$$E_P=X_{N-2}^2+2X_N^2+X_{N+2}^2-2X_{N-2}X_N-2X_NX_{N+2},$$

where each same-target square has diagonal plus four-distinct contributions and each cross product has its four shared-position classes plus $Q_4$, divided by the relevant exact wheel factors. This identity produces no independent estimate: its terms are still genuine prime correlations.

## 3. A non-circular pointwise arithmetic bound

For even $n\ge4$, let

$$B(n)=\left\lfloor\frac{n-4}{4}\right\rfloor.$$

This is exactly the number of odd integers $p$ satisfying $3\le p<n/2$. Every distinct prime-pair representation is determined by one such position $p$, so

$$0\le R(n)\le B(n).$$

This argument does not assume that any target has a representation. It immediately gives pointwise bounds on four-position counts:

$$R(n)(R(n)-1)\le B(n)(B(n)-1),$$

$$0\le Q_4(n,m)\le R(n)R(m)\le B(n)B(m)\quad(n\ne m).$$

The same upper bound applies to the sum of the five disjoint shifted configuration classes. After wheel normalization, for even $n,m$,

$$\frac{Q_4(n,m)}{A_{210}(n)A_{210}(m)}\le\frac{B(n)B(m)}{225}.$$

Since $X_n\ge0$, dropping the negative cross terms in the path-energy expansion and using $A_{210}\ge15$ yields another explicit pointwise estimate:

$$0\le E_P(N)\le X_{N-2}^2+2X_N^2+X_{N+2}^2
\le\frac{B(N-2)^2+2B(N)^2+B(N+2)^2}{225}.$$

These inequalities are rigorous for every indicated even target. They are deliberately labelled candidate-count bounds: their leading scale is quadratic in $N$ for the energy and they contain no primality-distribution saving. More seriously, they give only the trivial lower bound $R(n)\ge0$, not a strictly positive lower bound.

## 4. Exact pointwise certificate and its missing input

Let $a=X_{N-2}$, $b=X_N$, and $c=X_{N+2}$. The sharp three-vertex path inequality gives

$$\left(b-\frac{a+b+c}{3}\right)^2\le\frac29\big((a-b)^2+(b-c)^2\big).$$

The constant $2/9$ is sharp even for nonnegative triples with a zero center. Therefore a zero center necessarily satisfies $\mu^2\le(2/9)E_P$, where $\mu=(a+b+c)/3$. In particular, independently proved bounds

$$\mu\ge m_N>0,\qquad E_P(N)\le U_N,\qquad m_N^2>\frac29U_N$$

would prove $R(N)>0$ without assuming it. This is a conditional deterministic implication, not an arithmetic theorem about the prime counts.

The Stage 60 candidate bound supplies a possible $U_N$ but does not supply $m_N>0$; using the measured $\mu$ or energy in the certificate is post hoc and depends on the target prime-pair counts. The exact first missing arithmetic input for this route is a non-circular, pointwise strictly positive lower bound for the local mean (or a direct positive lower bound for $R(N)$), together with energy control precise enough to satisfy the strict inequality for every $N\in H$. An average over $N$ or over shifts does not provide that pointwise input. A purported positive bound for $Q_4$ alone also cannot guarantee $R(N)>0$, since it may arise from pairs at neighboring targets while $R(N)=0$.

The direct prime-only Fourier identity in Stage 58 is another exact reformulation, not a missing estimate: to use it one still needs a pointwise positive lower bound for its major-arc contribution and a sufficiently small minor-arc error, with explicit constants and all truncation terms. Neither the wheel nor the finite four-position identities yield those bounds.

## 5. Bounded exact audit

`compute_stage60.py` enumerates representations by a sieve for every even target needed by centers $8\le N\le300$. It records exact rational $X_N$, local path means and energies, the same-target diagonal/four-distinct split, and both adjacent shifted five-class decompositions. It also verifies the wheel product against direct enumeration of residues modulo 210 and checks the pointwise candidate and energy upper bounds.

`verify_stage60.py` is independently implemented. It uses trial division rather than a sieve, brute-forces the 210 residues rather than relying on the product formula, independently classifies shared positions, and verifies all recorded rational identities. It additionally checks the zero-center path obstruction over 256 nonnegative integer triples.

Exact results in `stage60_exact_results.json`:

- 147 consecutive even centers from 8 through 300 and 62 centers in $H$ were checked.
- 441 target wheel values were compared against all residue classes modulo 210.
- All 62 bounded residual centers have $R(N)>0$ and pass the measured path certificate. These are finite observations, not a universal estimate.
- Both adjacent correlation products at every center partition exactly into the five position classes; the low/high shared class is zero.
- The candidate-count and normalized energy upper bounds hold in every recorded row.
- The independent verifier reports all assertions passed. The verifier also checks 256 zero-center triples exactly.

No computation in this report extrapolates beyond the stated range or is used as a premise in the all-$N$ candidate-count proofs.

## 6. Refuted inferences and unresolved obligations

1. **Wheel admissibility implies a prime pair:** false; $A_{210}(N)$ counts residues only.
2. **A four-distinct shifted correlation forces a representation at its center:** false; shifted correlations can be positive using representations at other targets. A pointwise estimate must isolate the center contribution or enter a valid strict local certificate.
3. **Positive averaged moments exclude an isolated zero:** false for nonnegative vectors; Stage 58 gives the exact cyclic countermodel $(0,1,\ldots,1)$, and Stage 59 quantifies the $m/k$ loss for fixed-order averages.
4. **The deterministic path/cycle/graph inequalities themselves imply arithmetic regularity:** false. They only transfer independently established mean and energy bounds to positivity. The Stage 59 cycle, path and general-graph energies are different objects.
5. **The odd-candidate upper bound closes the criterion:** false. It is an unconditional upper bound but too coarse and has no positive lower mean. The first invalid step in any claim of closure would be treating candidate positions, wheel residues, or measured finite means as a uniform positive lower bound for true prime-pair counts.

The missing universal proof obligation remains a genuinely non-circular pointwise estimate for true prime correlations, strong enough to give $R(N)>0$ for every $N\in H$. This work does not prove Goldbach or universal coverage of the original three-case statement.

## 7. Reproduction

From the repository root:

```sh
python3 results/stage60/compute_stage60.py
python3 results/stage60/verify_stage60.py
```

The scripts use Python 3 standard library only and exact integer/rational arithmetic. The independent verifier must be run after the compute script has written `stage60_exact_results.json`.
