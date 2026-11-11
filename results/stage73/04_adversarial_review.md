# Stage 73 — Adversarial review, explicit counterexamples and limits

This is a separate internal critical pass, with independent algorithms and algebraic derivations. It is not external peer review or a formal proof assistant verification.

## 1. T73.4 — local signed arc profiles survive matching deletion

Let $a$ be any finite nonnegative coefficient vector, $0\le b\le a$, $A=\sum a_n$, $\delta=\sum(a_n-b_n)$, and let $E\subset\mathbb T$ have measure $\lambda$. Then for every integer $N$,
$$\boxed{\left|\int_E(S_a^2-S_b^2)e(-N\alpha)d\alpha\right|
\le\lambda\delta(2A-\delta).}$$
**Proof by factorization:** $|S_a-S_b|\le\delta$, $|S_a|\le A$, $|S_b|\le A-\delta$; apply $(S_a-S_b)(S_a+S_b)$ and integrate. **Independent coefficient proof:** $a*a-b*b$ has nonnegative coefficients and total mass $A^2-(A-\delta)^2=\delta(2A-\delta)$. Every Fourier kernel of $1_E$ has magnitude at most $\lambda$, proving the same bound. Equality is possible in the general class with a single frequency and target twice that frequency; its phase is constant. If $E$ has measure zero, $\delta=0$, or $A=0$, both sides are zero. No prime assumption is needed.

For the Stage 70–71 modified prime supports, established Wu upper sieve and PNT supply $A=WX+o(X)$, $\delta=O_w(X\log\log X/\log X)=o(X)$ uniformly in $N\in H\cap[X/2,X]$. The target coefficient of $S_b^2$ is exactly zero, by one endpoint deleted from each disjoint complementary edge. For $\mathcal A_D$ in 01, $\lambda=D/(3X)$, hence
$$|C_D(a;N)-C_D(b;N)|\le\frac{D}{3X}\delta(2A-\delta)=o_{D,w}(X).$$
On the target range the kernel is nonnegative, so in fact $0\le C_D(a)-C_D(b)$. More generally any family of arc unions of measure $O(K_X h_X/X)$ has $o(X)$ signed-profile change if $K_Xh_X\log\log X/\log X\to0$. For all reduced denominators up to $Q_X$ with common radius $h_X/X$, the sufficient condition is $Q_X^2h_X\log\log X/\log X\to0$. This is a sufficient stability range, not a sharp necessity or a theorem that all larger ranges suffice.

The deleted sequence retains the same leading fixed-modulus AP asymptotics and the same fixed rational-core signed profiles at $o(X)$ accuracy, and still loses the target. Therefore the following generalized assertion is **false**: every nonnegative subset of genuine prime frequencies with those leading asymptotic profiles, mass and full-energy upper constraints must represent every target. This is a precisely delimited no-go: it concerns inputs asserted only with these error tolerances and a class allowing deletions. Exact finite profiles could distinguish the sequences; minor-only energy monotonicity has not been proved; neither is silently included as an invariant.

The exact remainder sensitivity is
$$E_D(a;N)-E_D(b;N)=r_a(N)-r_b(N)-(C_D(a;N)-C_D(b;N)).$$
Since $r_b(N)=0$ and $E_D(b;N)=-C_D(b;N)$, the entire positive wheel core is cancelled for the altered model. A target-sensitive signed estimate for the immutable actual-prime polynomial can escape this theorem. The theorem neither refutes that estimate nor produces an arithmetic counterexample to Goldbach.

## 2. A counterexample using the full actual-prime support under a wrong weight quantifier

Choose nonzero smooth nonnegative $w$ supported in $(1/10,1/5)$. For every $N\in[X/2,X]$, $p+q<2X/5<N$ for all contributing primes, hence $r_X(N)=G_X(N)=0$ exactly. Nevertheless $S(0)\sim WX$ and the positive-core and fixed-wheel asymptotics in 01 hold. There are infinitely many residual examples: $N=X=12k+4$, $k\ge1$, has $N-1=3(4k+1)$ and $N/2=2(3k+1)$ composite. Thus a claimed universal positive coefficient for **every** smooth nonnegative weight is false even for the immutable full sequence. The first invalid implication is support coverage. The repair is to fix a broad permissible support and still prove the needed correlation. Merely including the midpoint proves no prime pair.

## 3. Audit of constants, endpoints and transformations

- $X>D/3$ is necessary for disjoint $D$ cores of radius $1/(6X)$; this hypothesis precedes integration as a union. Without it summing overlapping arc integrals counts multiplicity and is a different object.
- $D$ and $w$ are fixed in the PNT-AP asymptotic. No growing-denominator uniformity follows from finitely many PNT statements. The uniformity in $N$ comes from $N\bmod D$ taking finitely many values and $N/X\in[1/2,1]$ compact.
- The minimum $175/128$ is checked independently by CRT and exact cyclotomic Ramanujan sums over all 105 even residues modulo 210. Equality holds at $(N,105)=1$. No nonresidual restriction was silently added.
- The exact finite identity includes small primes. Excluding prime divisors of $D$ in the asymptotic requires $\sigma X>\max_{p\mid D}p$. Prime 3 corresponds to position zero and is never discarded from a finite identity.
- $S^2$ enforces a sum. $|S|^2$ enforces a difference. Reflection makes a full paired integral real but does not make it nonnegative. Trimming rational neighborhoods breaks the common beta domain needed for a Ramanujan numerator collapse.
- The elementary prime-power union bound counts ordered contamination and may double-count two proper-power entries. The factor two is correct. Chebyshev gives $O_w(\sqrt X\log X)$; the error is harmless only after an independent positive main term is obtained.
- Vaughan's identity includes $\Lambda_{\le V}$ and the convolution with $\mathbf1$ in Type II. Dropping either term is a false finite identity. The binary test function contains $\Lambda(N-n)$, so a theorem for a smooth exponential weight cannot be applied to it without a new bound.
- A generic Type II upper bound is not automatically a signed lower bound for $G$; the Type II term may carry main contribution. Cauchy gives the explicit four-position expression in 02 and leaves its target-specific arithmetic uncontrolled.

## 4. Proposed lemma verdicts

| Proposed inference | Verdict | First missing/invalid step | Repair |
|---|---|---|---|
| The Stage 72 positive core is the full coefficient | Refuted | Omit signed complement | Retain exact $r=C+E$ |
| Fixed 210 microcores give a stronger positive signed local term | Proved, fixed-modulus PNT input | None under support/disjointness hypotheses | T73.1–2 in 01 |
| This local enhancement defeats matching deletion | Refuted in deletion class | Mistake $o(X)$-stable local profiles for target control | T73.4 above; estimate total signed remainder |
| Every smooth weight yields positive target coefficient | Refuted for full prime support | Weight excludes all possible sums | Fix broad support, then prove simultaneous primality |
| AP distribution plus the verified Type I reduction settles binary Type II | Not established | Reflected $\Lambda(N-km)$ remains | Prove a target-uniform centered dispersion bound |
| Proper-power correction supplies a positive main term | Refuted inference | Upper error bound is not lower correlation | Independently prove $G>D_X$ |
| Exceptional set of positive size excludes a prescribed target | Refuted inference | Replace almost-all by every | New supremum/signed theorem |
| Goldbach is proved | Open | No signed remainder margin at every target | The proof obligation in 01/02 |

## 5. Independent computation and novelty audit

The Python verifier uses factorization and sparse formal-log coefficient dictionaries; Sage uses arithmetic-function convolution in a polynomial ring and exact cyclotomic fields. Both check the Vaughan identity including its boundaries. Sage's three examples use actual logarithms and a fixed genuine smooth bump with certified 160-bit interval arithmetic, not a rational surrogate. Their intervals validate only the stated finite inequalities. Stage 72's historical regression is rerun without writing its historical result; its unit-weight surrogate limitation is preserved.

T73.5 closes the Type I error with the proved logarithmic coefficient bound, nonreduced prime-power bookkeeping, and established BV/PNT; it asserts no main-term positivity. T73.1–2 are standard Fourier projection/PNT mechanisms newly assembled for this project's signed-core question. T73.4 is an elementary quantified extension of the Stage 70–71 deletion obstruction to signed local rational-arc profiles. No claim of a new theorem on simultaneous primality or mathematical-literature novelty is made. The prime-specific lower correlation remains open.

## 6. Independent critical pass on the Type I reduction

Re-derive the grouped coefficient from $l=dm$: only $m=p^j\mid l$ can contribute, so summing absolute coefficients gives at most $\sum_{j\le v_p(l)}\log p$ for each prime p. This totals $\log l$; both formal-log implementations check the stronger coefficientwise bound at all 600 declared inputs. There is no hidden $\tau(l)$ factor in this Type I term.

For reduced classes, apply partial summation to the cumulative $\psi(y;l,N)$ after the variable change $y=N-t$. The weight has compact support in $0<y<X$; its total variation is bounded by $O_w(1)$ or $O_w(\log X)$. For nonreduced classes, a prime power's base divides $N$, so the total at one modulus is at most $\omega(N)\log X$ before the logarithmic coefficient. Summing up to $Q=X^{2/5}$ gives $O_w(X^{2/5}\log^3X)=o(X)$. This validates the claimed uniform remainder even for targets with many small prime divisors.

The mesh conversion of the inspected BV statement must remove its coprimality centering error, not just use PNT. That contribution is explicitly included in 02. The maximal-in-y discrepancy is derived at a polynomial level strictly below $1/2$, which leaves room at the first mesh endpoint. The argument would fail unchanged at $Q=X^{1/2}$ without logarithmic room. It supplies no estimate for Type II, and the explicit Type I main term is never called positive by itself. These checks accept T73.5 with established BV and quantitative PNT as external inputs.

The ideal Type II hypothesis in 02 section 6 is quantitatively sufficient and has a valid continuum support lower bound. It already carries the essential binary prime correlation; no claim that it is weaker than Goldbach is accepted. The source Tao Lemma 4.11 support restriction $(V,UV^2)$ fails for our full support and $U=V=X^{1/5}$; only its independently proved algebraic identity is applied.
