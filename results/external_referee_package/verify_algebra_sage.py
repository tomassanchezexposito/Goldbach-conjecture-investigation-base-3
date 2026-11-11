"""Small independent rational-polynomial checks; no arithmetic theorem tests."""
import json
from sage.all import QQ, PolynomialRing
from sage.env import SAGE_VERSION

# Eliminate the three error definitions in a free rational polynomial ring.
errors = PolynomialRing(QQ, names=('F', 'A', 'EI', 'EK', 'P'))
F, A, EI, EK, P = errors.gens()
G = F + EK + A + EI
r = G - P
err = P - EK - EI
assert A - (r - F + err) == 0
assert r - (F + A - err) == 0

# The union majorant exceeds the actual product difference by q*u.
products = PolynomialRing(QQ, names=('s', 't', 'q', 'u'))
s, t, q, u = products.gens()
difference = (s + q) * (t + u) - s * t
union = q * (t + u) + u * (s + q)
assert difference == s * u + q * t + q * u
assert union - difference == q * u

# Free midpoint variables; fractions are exact, not prime-position sampling.
positions = PolynomialRing(QQ, names=('m', 'h'))
m, h = positions.gens()
p, z = m - h, m + h
a, b = (p - 3) / QQ(2), (z - 3) / QQ(2)
assert p + z == 2 * m
assert a + b == m - 3
assert b - a == h
assert 3 + 2 * a == p and 3 + 2 * b == z

print(json.dumps({
    'status': 'PASS', 'sage_version': SAGE_VERSION,
    'method': 'Free multivariate polynomial identities over QQ; no imported project verifier',
    'groups': [
        {'label': 'T75.1 error elimination', 'identities': 2, 'residuals': ['0', '0']},
        {'label': 'Proper-power union algebra', 'identities': 2,
         'difference': str(difference), 'majorant_excess': str(union - difference),
         'order_assumption': 'All coefficient variables nonnegative for the inequality'},
        {'label': 'Midpoint and base-3 reflection algebra', 'identities': 5,
         'sum_positions': str(a + b), 'difference_positions': str(b - a)}
    ],
    'scope': 'Exact algebra only; no primality, integrality, analytic uniformity or Goldbach proof',
    'excluded': 'No Type I kernel, wheel, deletion, global moment or Goldbach experiment'
}, indent=2))
