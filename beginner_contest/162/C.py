import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

k = int(input())

import functools
from fractions import gcd

cache = dict()

ab = []
for a in range(1, k + 1):
    for b in range(1, k + 1):
        i1, i2 = min(a, b), max(a, b)
        if (i1, i2) in cache:
            ab.append(cache[(i1, i2)])
            continue
        v = gcd(i1, i2)
        cache[(i1, i2)] = v
        ab.append(v)
        
ans = 0
for d in ab:
    for c in range(1, k + 1):
        i1, i2 = min(d, c), max(d, c)
        if (i1, i2) in cache:
            ans += cache[(i1, i2)]
            continue
        v = gcd(i1, i2)
        cache[(i1, i2)] = v
        ans += v

print(ans)
