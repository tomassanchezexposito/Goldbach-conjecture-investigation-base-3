# Stage 68 M2 — uniform shift-count Gram obstruction

Let $J=\{j_1,\ldots,j_m\}$ be any finite set of distinct nonzero integers, including a set depending on $X$. With $g_j=e(-N\alpha)(e(-j\alpha)-1)$, orthogonality gives
\[
G_{\mathbb T}=I_m+\mathbf1\mathbf1^*.
\]
For a measurable major set $\mathfrak M$ of measure $\mu$, $G_{\mathfrak M}\succeq0$ and $G_{\mathfrak m}=G_{\mathbb T}-G_{\mathfrak M}$. Thus $\lambda_{\max}(G_{\mathfrak m})\le m+1$. For $z=\mathbf1/\sqrt m$, $|\sum_j\bar z_jg_j|^2\le4m$ pointwise, so
\[
m+1-4m\mu\le\lambda_{\max}(G_{\mathfrak m})\le m+1.\tag{4}
\]
The lower bound is allowed to be negative. The rigorous conclusion is
\[
0\le1-\frac{\lambda_{\max}(G_{\mathfrak m})}{m+1}
\le\frac{4m\mu}{m+1}<4\mu,
\]
for every finite $J$, independent of its cardinality or shift magnitudes. If $P=X^\kappa$, $\kappa<1/2$, and the union of rational arc cores has $\mu\le2P^2/X=2X^{2\kappa-1}$, the relative loss is at most $8X^{2\kappa-1}$. At $m\asymp X^{1/2}(\log X)^{100}$ the absolute error in (4) can be $O(X^{2\kappa-1/2}(\log X)^{100})$ but the relative error remains $O(X^{2\kappa-1})$. These are different assertions.

For the complement of the major set, $G_{\mathfrak m}\preceq G_{\mathbb T}$ implies each Rayleigh quotient can only decrease; it does not imply a useful decrease in the top direction. The crude lower bound on any unit $z$ is $z^*G_{\mathfrak m}z\ge z^*G_{\mathbb T}z-4m\mu$. In particular, for $z\perp\mathbf1$, the full-circle quotient is 1 and the minor quotient is at least $1-4m\mu$, often vacuous. There is no identity placing the actual prime increment vector in $\mathbf1^\perp$. Even a sharp bound there would need a separately proved arithmetic orthogonality statement.

At a reduced rational $a/q$, $e(-ja/q)-1=0$ exactly when $q\mid j$. For $j=2h$ the condition is $q\mid2h$. A nonzero $j$ resonating for every $q\le P$ must be divisible by $\operatorname{lcm}(1,\dots,\lfloor P\rfloor)$. The elementary bound $\operatorname{lcm}(1,\dots,n)\ge2^n/(n+1)$ follows because every binomial coefficient $\binom nk$ divides this lcm and the largest coefficient is at least $2^n/(n+1)$. Thus bounded shifts cannot resonate at all small denominators as $P\to\infty$. Restricting to selected denominators leaves a complementary set; without an estimate there it creates no signed target saving.

**No-go scope.** Equation (4) is a geometric obstruction for arbitrary $L^2$ inputs. It refutes the idea that increasing the number of shifts alone yields a relative operator-norm saving. It does not refute stronger prime-specific estimates, nor does it establish that such estimates exist. The zero-frequency/constant-direction geometry and all smaller-eigenspace opportunities are useless for the prime problem unless a prime theorem identifies the relevant direction.
