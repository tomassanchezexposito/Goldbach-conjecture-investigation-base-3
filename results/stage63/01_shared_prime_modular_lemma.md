# Stage 63 M1: shared-prime contraction and exact wheel factors

## Definitions and exact contraction

Let `n < m` be distinct even integers, and let

$$R(t)=\#\{(p,q):p<q,\ p,q\text{ prime},\ p+q=t\}.$$

Define

$$S_{n,m}=\#\{x\in\mathbb Z:2\le x\le\min(n-2,m-2),\ x,n-x,m-x\text{ prime},\ 2x\ne n,\ 2x\ne m\}.$$

The inequalities force all three numbers to be at least 2. The two inequalities remove the diagonal pair in either target. Sorting `(x,n-x)` and `(x,m-x)` then gives one unordered representation at each target. Conversely, each pair of representations at `n,m` with a common prime determines this `x` uniquely. Two distinct common primes would imply `n=x+y=m`, impossible. Thus `S_{n,m}` counts exactly the pairs of representations with one common prime, with no multiplicity ambiguity. Consequently

$$Q_4(n,m)=R(n)R(m)-S_{n,m}$$

is exactly the number of pairs of representations whose four prime positions are pairwise distinct.

For sorted pairs `(p,q)` at `n`, `(r,s)` at `m`, the possible shared-position classes are `p=r`, `p=s`, `q=r`, and `q=s`. Since `n<m`, `p=s` is impossible: it would give `p<n/2<m/2<s=p`. The class `q=r` is possible when `n/2<q<m/2`; the other possible classes are `p=r` and `q=s`. The verifier retains all four named categories and checks the impossible category is zero.

## CRT identity

Let `W=prod_{ell in P} ell` be squarefree, with `P` a finite set of primes, and let

$$T_W(n,m)=\#\{x\pmod W:\gcd(x(n-x)(m-x),W)=1\}.$$

For each `ell|W`, the local condition excludes exactly the distinct residues in `{0,n,m} mod ell`. Write their number as `nu_ell(0,n,m)`. The Chinese remainder theorem gives a bijection between residues modulo `W` and independent tuples of residues modulo its prime factors. The accepted tuples therefore have cardinality

$$T_W(n,m)=\prod_{\ell\mid W}(\ell-\nu_\ell(0,n,m)).$$

This is an exact identity, without a primality assumption.

For even `n,m`, the factor at 2 is 1. For `W=210`, the factors at 5 and 7 are positive because at most three residues are excluded. The factor at 3 is zero exactly when `n,m mod 3` are 1 and 2 in either order. Thus, on even targets,

$$T_{210}(n,m)=0\quad\Longleftrightarrow\quad\{n\pmod3,m\pmod3\}=\{1,2\}.$$

Otherwise it is positive. This classifies the wheel obstruction only; positivity does not establish the existence of any prime triple.

The sieve condition in `T_W` removes values divisible by any prime factor of `W`, whereas primality permits the value to equal that prime. For example, `x=3,n-x=5,m-x=7` is a genuine triple for `(n,m)=(8,10)`, although `T_210(8,10)=0`. For `(8,12)`, the triple with `x=5` is genuine. For `(12,18)`, the genuine shared primes are `x=5` and `x=7`, giving triples `(5,7,13)` and `(7,5,11)`. The previously stated `x=11` is invalid because `12-11=1` is not prime. Small-prime survivors therefore cannot be discarded when relating a wheel sieve to actual primes. The prime 2 can occur in an even prime sum only as `2+2=4`, which is the excluded diagonal; no distinct-prime representation contains 2.

## Four positions and what the product says

For independent residues `x,r mod W`, the uncomplicated four-position admissibility count is

$$\#\{(x,r)\pmod W: \gcd(x(n-x),W)=\gcd(r(m-r),W)=1\}=A_W(n)A_W(m),$$

where `A_W(t)=#{z mod W:gcd(z(t-z),W)=1}`. This follows from independent choices of `x` and `r` (or CRT) and merely multiplies the two per-target wheel factors. It is not a new four-prime estimate. Pairwise distinctness of the integer prime positions is not encoded by these separate residue restrictions; imposing residue inequalities instead would define a different, coupled residue count and would still say nothing about primality.

## Evidence classes and limitations

1. **Proved identity:** the CRT product above and the shared-prime contraction identity.
2. **Exact finite verification:** `01_verify_modular.py` compares direct residue enumeration with the local product for 380 `(n,m)` cases modulo 210 and 330; compares common-`x` scans with pair-list intersections for 780 target pairs; and independently rechecks all 564 `h=1` rows in the checked-in Stage 57 data. It checks boundary primes and explicit wheel exceptions. The output is `01_exact_cases.json`.
3. **Trivial sieve bound:** for each admissible residue class there are at most `ceil((B+1)/W)` integers in any interval of `B+1` consecutive candidates. Summing over `T_W` classes bounds the number of wheel-surviving integer candidates. It is an upper bound on candidates only, not a lower bound on prime triples.
4. **Heuristic only:** local densities may motivate a prime-triple heuristic, but multiplying densities does not prove any target-specific prime triple.
5. **No genuine-prime bound obtained:** the calculations provide neither a positive lower bound nor a useful target-uniform upper bound for `S_{n,m}` or `R(t)`.

The proof is elementary and does not depend on a prime-distribution theorem. Finite checks audit the implementation; they are not the proof of the quantified identities.
