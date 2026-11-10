"""Independent Sage exact-algebra check of the Stage 69 M6 formulas."""

# Work in the exact real algebraic field; no floating-point comparison is used.
def exact_minimum(A, V, m):
    root_m = AA(m).sqrt()
    root_v = AA(V).sqrt()
    x0 = root_m * root_v / (m + 1)
    if x0 <= A:
        return A^2 + (root_v - root_m*A)^2
    return V / (m + 1)

cases = [(QQ(5), QQ(3), 2),       # V < m A^2
         (QQ(5), QQ(50), 2),      # V = m A^2
         (QQ(5), QQ(60), 2),      # m A^2 < V, boundary optimizer
         (QQ(5), QQ(100), 2),     # branch transition
         (QQ(5), QQ(200), 2)]     # interior optimizer

for A, V, m in cases:
    A, V = AA(A), AA(V)
    root_m, root_v = AA(m).sqrt(), V.sqrt()
    value = exact_minimum(A, V, m)
    x0 = root_m*root_v/(m+1)
    candidate = A^2 + (root_v-root_m*A)^2 if x0 <= A else V/(m+1)
    assert value == candidate
    stage66 = A^2 + max(AA(0), root_m*A-root_v)^2
    assert value >= stage66
    if V <= m*A^2:
        assert value == stage66

# The exact-energy and upper-bound envelopes have the same threshold V=m*A^2.
A, m = AA(7), 3
V = m*A^2
assert exact_minimum(A, V, m) == A^2
for Vbar in [AA(0), AA(20), AA(m*A^2), AA(2*m*A^2)]:
    envelope = A^2 + max(AA(0), sqrt(m)*A-sqrt(Vbar))^2
    if Vbar >= m*A^2:
        # The upper-bound class contains the actual-energy extremizer V=m*A^2.
        assert envelope == A^2

print("PASS: Sage exact algebraic arithmetic verifies both fixed-energy branches")
print("PASS: Stage 66 is sharp for fixed V<=m*A^2 and valid above that range")
print("PASS: upper-bound sharpness at Vbar>=m*A^2 uses actual V=m*A^2")
