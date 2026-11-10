# M7 cross-pollination — exact bridge and quantitative comparison

## Exact global bridge

Let $a_p=(\log p)w(p/X)$ and $r_w(n)=\sum_{p+q=n}a_pa_q$, with $r_w(n)=0$ outside its finite support. Orthogonality gives, for every integer shift $j$,
$$\int_{\mathbb T}|S_w(\alpha)|^4e(-j\alpha)\,d\alpha
=\sum_{n\in\mathbb Z}r_w(n+j)r_w(n).$$
Indeed, $|S_w|^4=|S_w^2|^2=\sum_{u,v}r_w(u)r_w(v)e((u-v)\alpha)$, and multiplication by $e(-j\alpha)$ selects $u-v=j$. All coefficients are real nonnegative. The formula uses ordered prime pairs inside each $r_w$; therefore it automatically carries the order multiplicities, the possible diagonal $p=q$, and genuine-prime support. For $N\in H$ the target diagonal is absent. No prime powers occur because $S_w$ is prime-only.

This is a **global** shift correlation, not a local identity at a prescribed target. The restricted integral has the exact formula
$$\int_{\mathfrak m}|S_w(\alpha)|^4e(-j\alpha)d\alpha
=\sum_{u,v}r_w(u)r_w(v)\widehat{1_{\mathfrak m}}(j-u+v),$$
whose kernel is generally signed. It is not a nonnegative sum of integer quadruple counts. Nor does the full-circle bridge identify one $r_w(N)$: it averages products over all $n$.

The exact prime-position expansion of the left side's unweighted energy is
$$\sum_{p_1+p_2=p_3+p_4+j}a_{p_1}a_{p_2}a_{p_3}a_{p_4}.$$
This equality is only for the full circle. For $j=0$, the four positions have the M1 same-target diagonal and distinctness multiplicities; for $j\ne0$, all solutions must be classified by coincident prime values, and the coefficient identity remains valid without assuming they are distinct. Thus no blanket factor of $4$ or $8$ applies to the shifted total. The exact convolution form is the safe multiplicity convention.

## Shifted target factorization does not provide a seed

For a fixed target and shift, the product $r_w(N)r_w(N+j)$ expands into four-prime configurations with four-distinct and shared-anchor terms as recorded in `04_anchor_correlation_ledger.md`. It contains the factor $r_w(N)$. If the target is a hypothetical zero, every such term vanishes. A lower bound derived by choosing one representation at $N$ is invalid in the zero case. The global integral identity above avoids that logical error but loses localization and is consistent with $r_w(N)=0$.

## Which route is weaker?

Candidate A asks for a phase-sensitive minor coefficient to be at most $(c_0-\delta)X$. Under the fixed $Q_\Theta$ assumption and the cited uniform major-arc lower bound, it implies $r_w(N)\geq\delta X$ for every target in the range, hence a uniform quantitative Goldbach theorem there. Route B's displayed weighted pair lower bound also implies $R(N)>0$ and is quantitatively stronger than bare existence. Neither is proved. They are **not ordered** by the available arguments: A is a sufficient analytic decomposition with a specific phase estimate; B is a direct arithmetic correlation lower bound. Each entails target positivity, and neither has been shown to imply the other's numerical estimate.

The source minor fourth moment yields only $O(X^{5/4}(\log X)^{50})$ for an individual signed coefficient, versus the required $O(X)$ with a strict major-term margin. The source exceptional-set bounds of positive-power size permit an isolated target. Wheel density is positive but has no prime-only remainder. These quantified gaps identify one shared logical endpoint—an independent positive lower bound at a prescribed target—but do not make the two analytic estimates identical.

**Potential circularity and first missing arithmetic fact.** No exact identity bridges the global fourth moment to a fixed target without extra localization information. The first common missing input is genuine-prime information that prevents one target correlation from being zero while satisfying the global moment and local congruence constraints. Presently neither route supplies it.
