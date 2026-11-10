# Stage 64 — Focused pointwise estimate attempt

## Question

Can the available global fourth moment for the genuine-prime exponential sum give a signed estimate at one prescribed even target, without assuming a representation of that target?

Use the smooth prime sum S_w and fixed major/minor arc split from 01_2026_primary_sources.md. Let a_w(N) and m_w(N) be the major and minor coefficients in 02_fourth_moment_to_pointwise_gap.md, so that the exact prime-only weighted coefficient is r_w(N)=a_w(N)+m_w(N).

## Non-circular implication from a missing representation

For nonnegative w, the coefficient r_w(N) is a sum of nonnegative terms, one for each ordered pair of primes adding to N. If the repository's distinct representation count R(N) is zero, then there is no prime pair at all, so r_w(N)=0 for every such weight, regardless of support. On H, N/2 is composite, which also rules out the equal-prime term; consequently r_w(N)>0 implies a distinct representation. Thus a missing target in H forces m_w(N)=-a_w(N).

The major-arc formula established in the cited preprint gives a_w(N)≥cX uniformly over its stated even-target interval, for sufficiently large X, under its common zero hypothesis. Consequently, a zero weighted prime coefficient forces the signed minor coefficient to be at most -cX. This is a valid non-circular reduction: it begins from a hypothetical missing target and uses an independently stated major-arc estimate.

Conversely, r_w(N)>0 proves there is a prime pair in the support, and on H this pair is distinct because N/2 is composite. Hence no support-coverage assumption is needed for this implication. The weight need only be nonnegative, and the cited major-arc theorem must apply at the target under consideration.

## Attempted global-norm contradiction

Parseval and the published hypothesis imply

$$\sum_{N\in\mathbb Z}|m_w(N)|^2\ll X^{5/2}(\log X)^{100}.$$

If a target has zero weighted coefficient, its term in this sum is at least c^2X^2. Hence this argument gives at most O(X^{1/2}(\log X)^{100}) such targets in the whole interval. The first invalid step in a proposed universal proof is the claim that this upper bound is less than one: it grows with X. The bound permits one exceptional target, and the norm inequality by itself cannot distinguish a coefficient vector with all mass at one index.

The pointwise consequence obtained by taking a square root is only

$$|m_w(N)|\ll X^{5/4}(\log X)^{50},$$

which is larger than the major term cX. It has no sign information either.

## Exact conditional lemma and its limitation

**Lemma (localized-energy exclusion).** Suppose for a specified even target N in the major-arc range the exact prime coefficient satisfies r_w(N)=a_w(N)+m_w(N), with a_w(N)≥cX>0. If an independently proved estimate gives |m_w(N)|<cX, then r_w(N)>0.

**Proof.** Since a_w(N) and m_w(N) are real, r_w(N)≥a_w(N)-|m_w(N)|>0. Nonnegative prime weights then imply at least one prime pair in the support. This proves the lemma. It does not prove the required estimate for m_w(N).

For any target, a sufficient condition is

$$\sum_{N\in B}|m_w(N)|^2<c^2X^2,$$

because it rules out |m_w(N)|≥cX at that target. A global bound at scale X^(5/2)(log X)^100 is too large. A target-localized square bound strictly below c^2X^2 would close this particular gap. No such estimate is established here.

## Adversarial checks

1. Nonnegativity of prime weights gives r_w(N)≥0, while the minor term may be negative and cancel the major term.
2. Positivity of the singular series lower-bounds the modeled major term, not the signed error.
3. Any exceptional-set upper bound tending to infinity permits a singleton.
4. H removes the equal-prime case because N/2 is composite. A representation involving 2 is a genuine distinct representation and causes no logical exception: if R(N)=0, it is absent as well.

## Result

The genuinely prime-only major/minor decomposition yields a sharp reduction to a signed, target-specific error estimate, but the fourth-moment theorem does not supply that estimate. The global norm permits a single bad coefficient. The exact missing input is a uniform signed bound m_w(N)>-a_w(N) for every residual target, or an independently justified localized-energy estimate below the one-target threshold. Universal coverage remains open.
