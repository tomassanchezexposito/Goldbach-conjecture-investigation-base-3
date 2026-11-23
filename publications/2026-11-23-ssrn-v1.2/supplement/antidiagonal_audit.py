"""Reproduce the local-pattern counts in arXiv:2611.09007v1, p. 5."""
from math import isqrt

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))

patterns = ((1,1,0,1),(0,1,0,0),(1,1,1,0),(1,0,0,0))
N = 100
rows = [[] for _ in patterns]
for x in range(3, N-4, 2):
    y = N-x
    pattern = tuple(map(prime, (x,x+2,y,y-2)))
    if pattern in patterns:
        rows[patterns.index(pattern)].append(x)
assert rows == [[], [35,65], [3,11,17,29,41,59,71], [7,13,23,43,73]]
for i,row in enumerate(rows,1): print(f'R{i}: {len(row)}; x={row}')
