# Stage 76 — Audited research closure

## State, gates and deliverable discipline

Base: PR #25 head `3a5581dd93b7c50bbc55062d032a6ad2acab1fb4`, confirmed after dedicated-identity SSH fetch and authenticated PR inspection; clean worktree. PR #25 is open, draft and unmerged. This branch is `cocalc/stage76-audited-closure`.

The earlier Stage76 package remains unchanged on `cocalc/stage76-formal-closure`, commit `9fc2cb50bac7507a4b637c7b04938bca6f50156c`, PR #26. It contained eight files, exceeding this request's strict six-file ceiling. This alternative starts directly from PR25, adds exactly five tracked deliverables plus this directory's `LEDGER_DELTA.md`, and does not delete or rewrite the earlier branch. The missing shared-endpoint counterexample and separate Python/Sage implementations are supplied here. No Lean artifact is requested or claimed in this revision.

There is no root-level canonical LEDGER at this base. The operative evidence chain is `results/stage73/05_proof_ledger.md`, Stage74/75 deltas, `results/dependency_audit_73_75/LEDGER_DELTA.md`, and the external referee package. These were inspected with `tasks/NEXT_TASK.md` and the Stage70–72 core/deletion reports. All historical ledger rows remain unchanged.

**Novelty gate:** no independently justified new signed arithmetic input is supplied. **Duplication gate:** T75.1 and the conditional threshold are retained reductions, not a new proof attempt. **Parity gate:** target-erasing deletion preserves the named coarse data in an enlarged subset class, so positivity cannot be certified from those data alone. These gates close direct TypeII development; they permit the explicitly requested documentation and exact-algebra closure. No new analytic theorem is proposed.

## Logical completeness: cases, H and H1

For even $N\ge4$, set $R(N)=\#\{p<q:p,q\text{ prime},p+q=N\}$ and
$$C(N)=[N-1\text{ prime}]\lor[N/2\text{ prime}]\lor[R(N)>0].$$
These are the original cases $N=p+1$, $N=2p$, and distinct-prime addition. Let $H$ be the immutable residual set with $N-1,N/2$ composite, $H_1=\{N\ge8:N\text{ even},N-1\text{ prime},N/2\text{ composite}\}$, and $D=\{N\ge4:N\text{ even},N/2\text{ composite}\}$. Composite means greater than one and not prime.

**Proof of partition:** a composite midpoint is at least 4, so $N\in D$ implies $N\ge8$ and $N-1>1$. Exactly one of primality and compositeness of $N-1$ holds. Therefore $D=H\mathbin{\dot\cup}H_1$. Outside $H$ one of the first two author cases holds, while inside $H$ both fail. Thus universal $C(N)$ is equivalent to $R(N)>0$ throughout $H$.

A binary prime sum either has equal endpoints, necessarily the prime $N/2$, or distinct endpoints counted by $R$. Hence $B(N)$, binary Goldbach at $N$, is exactly $[N/2\text{ prime}]\lor[R(N)>0]$. Outside $D$ its midpoint supplies a representation; inside $D$ no diagonal is possible. This proves strong Goldbach is equivalent to $R(N)>0$ throughout $H\cup H_1$. Also $C(N)\iff[N-1\text{ prime}]\lor B(N)$. No converse from the author's assertion alone to strong Goldbach is established.

Prime 2 contributes to an even prime-pair sum only at $N=4$, where the diagonal is $2+2$. Prime-plus-one never makes 1 prime. The actual prime polynomial has coefficient zero at 1. For odd $p\ge3$, $a=(p-3)/2\in\mathbb Z_{\ge0}$ is the inverse to $C_a=3+2a$; the progression includes composites. If $p+q=N=2m$, then $a+b=m-3$, $h=(q-p)/2=b-a$, $p=m-h$, $q=m+h$, and $N-2p=2q-N=q-p$. Oddness ensures integer $h$, and $p<q$ ensures $h>0$. These identities add no primality information.

## Analytic extension and CONDITIONAL threshold

Keep the immutable $S_X(\alpha)=\sum_p(\log p)w(p/X)e(p\alpha)$ for a fixed nonnegative smooth $w$ supported in $[\sigma,\rho]\subset(0,1)$. Define $r_X=[S_X^2]_N$, $G_X=\sum_n\Lambda(n)\Lambda(N-n)h_N(n)$, $h_N(t)=w(t/X)w((N-t)/X)$, and retain the genuine Stage73 $A_3$, $U=V=\max(1,\lfloor X^{1/5}\rfloor)$ and exact coprime-preserving TypeI main term $\mathcal M_I$.

T73.5 gives $G_X=\mathcal M_I+A_3+E_I$ with
$$E_I=O_{A,w}(X\log^{-A}X+X^{2/5}\log^3X)$$
for every fixed $A>0$, uniformly in all integer targets in $[X/2,X]$. T74.3 gives $\mathcal M_I=F_X+E_K$, $F_X=X\mathfrak S(N)J_w(N/X)$, $E_K=O_w(Xe^{-c\sqrt{\log X}})$ uniformly for positive even $N\le X$. Here $J_w(\tau)=\int w(u)w(\tau-u)du$, $\mathfrak S(N)=2C_2\prod_{p\mid N,p>2}(p-1)/(p-2)$ and $C_2=\prod_{p>2}(1-(p-1)^{-2})>0$. The established proper-power bound gives $0\le P_X=G_X-r_X\le4C_{\rm Ch}\|w\|_\infty^2\sqrt X\log X$ for $X\ge16$.

**Domain audit:** none of these hypotheses requires $N-1$ composite. Consequently, with $E_X=[X/2,X]\cap2\mathbb Z$ at large $X$,
$$A_3(N)=r_X(N)-F_X(N)+e_X(N),\quad e_X=P_X-E_K-E_I,\quad\sup_{N\in E_X}|e_X(N)|=o_w(X).$$
The extension is valid on all even targets, hence on $D$. It is an inherited-error deduction, not an independently certified prime-correlation theorem; the zero coefficient at 1 alone would not prove uniformity. Equal-prime terms remain in $r_X$ on midpoint-prime targets. Independent human analytic review of T73.5, T74.3 and T75.1 remains **PENDING**. Their stated external dependencies are classical BV, quantitative PNT/Mobius cancellation and a Chebyshev bound; no unverified 2026 zero-free assertion is adopted.

For the broad weight positive on $[1/5,3/5]$, let $m_w=\min_{[9/40,21/40]}w>0$. At $\tau\in[1/2,1]$, the interval $[\tau/2-1/40,\tau/2+1/40]$ has length $1/20$ and both arguments $u,\tau-u$ lie in $[9/40,21/40]$. Therefore $J_w\ge m_w^2/20$; since $\mathfrak S(N)\ge2C_2$ for even $N$, $F_X\ge c_wX$ with $c_w=C_2m_w^2/10$.

**CONDITIONAL implication:** if an independent theorem proved $A_3(N)\ge-c_wX/2$ for every required $N\in D\cap[X/2,X]$ and all $X\ge X_0$, choose $X_1\ge X_0$ also dominating the error cutoff $\sup|e_X|\le c_wX/4$. Then $r_X=F_X+A_3-e_X\ge c_wX/4>0$ for $X\ge X_1$. On $D$ this forces distinct genuine primes. The signed premise, effective cutoff and finite connection remain unavailable. A triangle inequality in both directions gives uniform $A_3=o_w(X)$ iff $r_X=F_X+o_w(X)$ on either domain. This weighted Hardy–Littlewood asymptotic is stronger information than bare positivity.

## Exact wheel, deletion domain and counterexample

If $\nu_l(N)=|\{0,N\}\pmod l|$, CRT gives $A_{210}(N)=\prod_{l\in\{2,3,5,7\}}(l-\nu_l(N))$ and $S_{210}=210A_{210}/48^2$. These are modular counts, not prime counts. Genuine pairs containing 2,3,5,7 can fail reduced-residue conditions and must be retained separately. For example $(3,13)$ and $(5,11)$ are valid pairs at 16 despite failing the wheel. $\varphi(9)=6\ne\varphi(3)^2=4$: the recorded $N=16,U=V=3$ coefficient is $(1/2-1/6)\log3=(\log3)/3$, not $(1/2-1/4)\log3=(\log3)/4$.

For disjoint complementary-pair edges, $r_b(N)=2\sum_i b_{p_i}b_{q_i}$ with $0\le b\le a$. If this is zero, every nonnegative product is zero, so each edge loses an endpoint at cost at least its smaller weight. Disjointness makes those lower costs additive, and deleting a smaller endpoint on every edge attains the sum: $\tau_N=\sum_i\min(a_{p_i},a_{q_i})$. Zero weights and ties are allowed; zero cost need not mean an empty edge set.

**Counterexample outside the domain:** a bipartite star with center $c$ and leaves $u,v$, all weights 1, has two edges $(c,u),(c,v)$. The edgewise sum is 2. Deleting $c$ alone annihilates both products at cost 1; every annihilation must delete $c$ or both leaves, so the exact minimum is 1. Thus the matching formula fails on arbitrary bipartite graphs. A genuine fixed-target complementary-prime graph cannot contain this star: $c+u=c+v=N$ would force $u=v$.

Asymptotic invisibility is separately inherited from upper sieve/PNT and the actual fixed smooth prime weights, not from arbitrary finite matching structure. The changed polynomial is a prime subset, not the immutable full prime polynomial. A sound positivity certificate that uses only data retained under this deletion and purports to hold throughout the enlarged subset class would contradict the erased target. This does not assert that genuine Vaughan structure or maximal BV accuracy survives deletion, and it does not refute an independent full-prime estimate.

## Verification, provenance and stop

The single source has independent standard-Python and Sage branches: Fraction/integer vectors, trial division on prescribed fixtures and gcd residue counting versus QQ polynomial elimination, exact Sage integer primality and Zmod unit translations. Matching endpoint covers are checked against separate attenuation grids; the shared-endpoint star is independently checked. Domains, exact outputs, timestamps, software and SHA-256 values are in the manifest. These are finite certificates, not analytic proof certification or finite Goldbach sweeps.

The twelve-page monograph consolidates the historical record; historical Stage57 data says 9490 windows, not the 9450 transcription in the earlier Stage76 request. Earlier evidence is preserved. No new theorem ID is registered: the alternate package reuses the explicitly qualified logical deductions without replacing the existing L76/T76 rows on PR26. External sources and the pending human referee status are disclosed, not promoted to acceptance.

**Strong Goldbach OPEN; original three-case assertion OPEN; genuine-prime signed lower bound OPEN; deletion-stable direct TypeII route NO-GO within its proved scope.** Closure is documentation, logic, exact algebra and conditional implications only. Stop after publication.
