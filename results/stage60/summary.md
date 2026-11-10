# Stage 60 summary

## Established

- The exact same-target second moment is a diagonal plus four-distinct term; distinct-target correlations partition into four shared-position classes and a four-distinct class.
- For every even $n\ge4$, the number of true distinct-prime representations is at most $B(n)=\lfloor(n-4)/4\rfloor$, the count of available odd candidate positions. Therefore $Q_4(n,m)\le B(n)B(m)$ and the normalized three-point path energy has the explicit upper bound proved in `report.md`.
- The sharp deterministic path criterion is valid: independently proved $\mu\ge m>0$, $E_P\le U$, and $m^2>(2/9)U$ imply positivity at the center.
- Independent exact computation and verification agree for 147 centers $8\le N\le300$, including 62 residual centers, all 441 wheel checks and every recorded four-position decomposition.

## Refuted or limited

- Wheel admissibility does not imply primality.
- Positive averages, positive shifted products, or a favorable finite certificate do not establish positivity at every target.
- The odd-candidate upper bounds provide no strictly positive lower mean and do not close the path criterion.
- Cycle, path and general graph energies are distinct criteria and their finite performance cannot be conflated.

## Open proof obligation

Prove a non-circular pointwise positive lower bound for the true prime-pair count, or independent local mean and energy bounds satisfying the strict path inequality at every $N\in H$. No such estimate is obtained here; the original universal three-case conjecture remains open.
