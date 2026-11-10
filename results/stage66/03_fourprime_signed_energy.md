# Stage 66 — Exact genuine-prime four-position bookkeeping

## Representation sets and normalization

For an even target $n\ge4$, let
$$\mathcal P(n)=\{\{p,q\}:p<q,\ p,q\text{ prime},\ p+q=n\},\quad R(n)=|\mathcal P(n)|,$$
and let $A_n=A_{210}(n)$ count admissible residues modulo $210$. Put $x_n=R(n)/A_n$. The normalizing count is positive for even $n$ but is not a prime count. On the residual set, $N/2$ composite excludes the equal-prime diagonal; for $N>4$ the prime 2 cannot occur because $N-2$ is even and greater than 2. The exceptional $N=4$ pair $2+2$ is not in $\mathcal P(4)$.

Take distinct even targets $u\ne v$. A pair of representations $P\in\mathcal P(u)$, $Q\in\mathcal P(v)$ cannot share both prime values, since then their sums would agree. It either shares exactly one prime or has four distinct prime positions. The shared-position count is exactly
$$S(u,v)=\#\{x\text{ prime}:u-x\text{ and }v-x\text{ prime},\ x\ne u/2,\ x\ne v/2\}.$$
Each configuration is counted once: the common prime $x$ determines both unordered pairs. Define $T(u,v)=R(u)R(v)-S(u,v)$. Then $T$ counts the four-distinct configurations and
$$R(u)R(v)=S(u,v)+T(u,v).$$
No factor of two is present because both representation sets consist of unordered pairs and the Cartesian product is ordered only by target label.

At a single target, the diagonal pairs of representations contribute $R(n)$ and the off-diagonal ordered pairs contribute $Q(n)=R(n)(R(n)-1)$. Two different representations at the same target cannot share exactly one prime: the shared prime fixes the other summand. Hence every term in $Q(n)$ has four distinct prime positions and
$$R(n)^2=R(n)+Q(n).$$
For the normalized signed square of two target counts the exact identity is
$$|x_u-x_v|^2=\frac{R(u)+Q(u)}{A_u^2}+\frac{R(v)+Q(v)}{A_v^2}
-2\frac{S(u,v)+T(u,v)}{A_uA_v}.$$
The same identity applies if either target count is zero; it does not select a prime representation at that target. However, it supplies no sign estimate by itself: the positive self terms and negative cross terms are all genuine-prime correlations whose relative sizes are unknown.

For three targets $n_-=N-2,n_0=N,n_+=N+2$, define $C_{ij}=R(n_i)R(n_j)=S_{ij}+T_{ij}$ when $i\ne j$. The Stage 61 certificate's exact identity is
$$\begin{aligned}
9D_N={}&-\frac{R_-+Q_{--}}{A_-^2}-3\frac{R_0+Q_{00}}{A_0^2}-\frac{R_++Q_{++}}{A_+^2}\\
&+6\frac{C_{-0}}{A_-A_0}+2\frac{C_{-+}}{A_-A_+}+6\frac{C_{0+}}{A_0A_+}.
\end{aligned}$$
It is an exact decomposition into diagonals, four-distinct same-target terms, one-shared-prime contractions, and four-distinct cross-target terms. To force $D_N>0$, independent bounds must dominate the weighted self terms by the three cross terms for every residual $N$. No such target-uniform bounds are established.

## Why representation-anchored lower bounds are circular

An argument that starts by choosing $P\in\mathcal P(N)$ cannot analyze the case $R(N)=0$: its anchor set is empty in exactly the case that must be ruled out. By contrast, the identities above are unconditional bookkeeping and make sense when a representation set is empty, but an inequality derived from them must still have independent arithmetic content. Replacing primes by wheel-admissible residues counts candidates only. Singular-series factors are conjectural main-term data, not actual values of $S$ or $T$.

## Exact finite verification design

`verify_stage66_sage.py` uses SageMath's `prime_range` to build unordered representation sets independently of the inherited Python routines. It checks within-target diagonal/off-diagonal counts and cross-target shared/four-distinct partitions over a stated finite range, including cases with zero shared configurations and a same-target check. These checks certify finite multiplicities only. They do not estimate the correlations asymptotically or assume that an arbitrary residual target is represented.
