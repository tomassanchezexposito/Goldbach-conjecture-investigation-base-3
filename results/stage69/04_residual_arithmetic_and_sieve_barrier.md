# M4 — Residual arithmetic, wheel survivors, and the sieve boundary

## Residual set and original cases

Keep the exact definition
\[
H=\{N\ge4:N\text{ even},\ N-1\text{ composite},\ N/2\text{ composite}\},\qquad
R(N)=\#\{p<q:p,q\text{ prime},\ p+q=N\}.
\]
For each even $N>2$, preserve the three cases $N=p+1$, $N=2p$, or $N=p+q$ with distinct primes $p<q$. Membership in $H$ excludes the first two cases: $N-1$ composite rules out $p+1$, and $N/2$ composite rules out $2p$. Thus the original three-case assertion on $H$ reduces exactly to $R(N)>0$. This is a logical reduction, not evidence for the remaining case.

For even $N>4$, a distinct representation cannot use prime 2 because $N-2>2$ is even and composite. Prime 3 is not excluded; the contribution is present exactly when $N-3$ is prime. The diagonal $p=q=N/2$ is impossible on $H$ because $N/2$ is composite. These edge cases are independent of the sieve discussion.

## Exact CRT survivor count

Let $Q$ be a squarefree product of odd primes and count residue classes $x\pmod Q$ for which neither $x$ nor $N-x$ is divisible by any $\ell\mid Q$. By CRT the count is
\[
\prod_{\substack{\ell\mid Q\\\ell\nmid N}}(\ell-2)
\prod_{\substack{\ell\mid Q\\\ell\mid N}}(\ell-1).
\]
For each factor, if $\ell\nmid N$, the two forbidden residues are $0$ and $N$; if $\ell\mid N$, they coincide and only one residue is forbidden. This is the complete exact count for the finite modulus $Q$. For actual prime summands, the divisibility exclusions have exceptions at the endpoint values $x=\ell$ or $N-x=\ell$; the CRT count is a local sieve model, not the exact count of primes.

Taking $Q=3\cdot5\cdot7$ yields the wheel-210 admissibility profile (with parity imposed separately). A positive count says only that some residue classes avoid the listed small prime divisors. It does not say that any integer in those classes is prime. The singular-series product is likewise a local density prediction. Even a positive singular series at every admissible $N$ is not a lower bound for the exact finite convolution $r_w(N)$.

## Sieve obstruction and a quantified boundary

The two linear forms are $L_1(x)=x$ and $L_2(x)=N-x$. After local exclusions they form a dimension-two prime-pair sieve problem. Upper-bound sieve weights can bound survivors, but the sieve parity phenomenon prevents a generic lower-bound sieve from certifying simultaneous primality from local densities alone. Chen's theorem supplies a prime plus an almost-prime for sufficiently large even targets, but that is a different conclusion and does not yield two primes. Any use of such a theorem must retain its exact hypotheses and cannot replace the missing binary-prime lower bound.

The target-specific statement
\[
\sum_{x\in\mathbb Z}1_{\mathbb P}(x)1_{\mathbb P}(N-x)\ge1
\]
is equivalent to existence of the desired ordered pair, with the diagonal treated separately. A lower bound $\gg N/(\log N)^2$ would be stronger and also suffices. Neither follows from the finite CRT count. No lower-bound sieve estimate in this stage crosses the parity obstruction to give that indicator product for every fixed target.

## Potential circularity and first missing arithmetic fact

An argument that chooses a prime anchor $p_0$ satisfying $N-p_0$ prime has already chosen the desired representation. A weighted four-prime count based on such an anchor is circular if its positivity is the conclusion being tested. The first missing fact remains a target-uniform lower bound for the product of the two genuine-prime indicators, or an independently proved phase-sensitive Fourier estimate with the same consequence.

## M4 verdict

The reduction of the three cases on $H$, the endpoint analysis, and the finite CRT count are exact. Wheel admissibility and the standard sieve setup do not provide simultaneous primality. No universal representation bound is established.
