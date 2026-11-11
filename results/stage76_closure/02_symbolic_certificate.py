"""Exact finite certificates, independent of all earlier project verifiers."""
import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path
from sage.all import PolynomialRing, QQ
from sage.env import SAGE_VERSION

ring = PolynomialRing(QQ, names=('a', 'b', 'm', 'h', 'F', 'A', 'EI', 'EK', 'P'))
a, b, m, h, F, A, EI, EK, P = ring.gens()
assert (3 + 2*a) + (3 + 2*b) - 2*m == 2*(a+b-(m-3))
p, q, N = m-h, m+h, 2*m
assert p+q == N
assert N-2*p == 2*q-N == q-p
assert ((p-3)/2)+((q-3)/2) == m-3
assert A == (F+EK+A+EI-P)-F+(P-EK-EI)
# Truth-table certification of the abstract disjunction, not primality testing.
for first, middle, pair in itertools.product((False, True), repeat=3):
    C = first or middle or pair
    B = middle or pair
    residual = not first and not middle
    assert C == (first or B)
    assert C == ((not residual) or pair)
    assert B == (middle or pair)
wheel = []
for n in range(210):
    direct = sum(math.gcd(r, 210) == math.gcd((n-r) % 210, 210) == 1
                 for r in range(210))
    product = math.prod(l-(1 if n % l == 0 else 2) for l in (2, 3, 5, 7))
    assert direct == product
    wheel.append((n, direct, str(Q(210*direct, 48**2))))
phi = lambda k: sum(math.gcd(j, k) == 1 for j in range(1, k+1))
assert phi(210) == 48 and phi(9) == 6 and phi(3)**2 == 4
correct, false = Q(1, phi(3))-Q(1, phi(9)), Q(1, phi(3))-Q(1, phi(3)**2)
assert (correct, false, correct-false) == (Q(1,3), Q(1,4), Q(1,12))
# Abstract matching fixtures, not a search for target prime representations.
matching_results = []
for weights in [[], [(Q(0), Q(3,2))], [(Q(3,2),Q(7,3)),(Q(4),Q(4)),(Q(0),Q(5))]]:
    costs = []
    for bits in itertools.product((0,1), repeat=len(weights)):
        cost = Q(0)
        for (left,right), bit in zip(weights,bits):
            u,v = (Q(0),right) if bit == 0 else (left,Q(0))
            assert u*v == 0
            cost += left-u+right-v
        costs.append(cost)
    tau = sum((min(x,y) for x,y in weights), Q(0))
    assert min(costs) == tau
    matching_results.append({'edges':len(weights),'covers':len(costs),'tau':str(tau)})
# Read the historical data only; do not rerun its counting experiment.
root = Path(__file__).resolve().parents[2]
old = json.loads((root/'results/stage57/shifted_correlations.json').read_text())
cov = old['covariance_heuristic']
assert cov['windows_with_at_least_two_eligible_anchors_tested'] == 9490
assert cov['counterexample_count'] == len(cov['counterexamples']) == 3762
ordered_total = sum(row['ordered_representation_pair_count'] for row in old['rows']) if (
    old['rows'] and 'ordered_representation_pair_count' in old['rows'][0]) else None
print(json.dumps({'status':'PASS','sage_version':SAGE_VERSION,
 'coordinates':'Five rational polynomial checks including error elimination pass',
 'logic':'Eight abstract truth assignments pass; general equivalence has a written proof',
 'wheel_residue_cases':210,'wheel_exact_rows':wheel,'phi210':48,
 'totient_counterexample':{'N':16,'U':3,'V':3,'correct_log3':str(correct),
                         'false_log3':str(false),'difference':str(correct-false)},
 'matching_fixtures':matching_results,
 'stage57_saved_data':{'windows':9490,'failures':3762,'ordered_total_if_named':ordered_total},
 'limitations':'Finite algebra/modular/fixture checks only; no asymptotic theorem or Goldbach proof; Lean unavailable'},indent=2))
