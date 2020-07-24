import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))
MOD = 10 ** 9 + 7
lcm = 1

import collections
lcm_pf = collections.defaultdict(int)
for i, v in enumerate(a):
    j = 2
    pf = {}
    while j ** 2 <= v:
        ext = 0
        while v % j == 0:
            ext += 1
            v //= j
        if ext:
            pf[j] = ext
            lcm_pf[j] = max(lcm_pf[j], ext)
        j += 1
    if v != 1:
        pf[v] = 1
        lcm_pf[v] = max(lcm_pf[v], 1)
for p in lcm_pf:
    lcm = lcm * (p ** lcm_pf[p])
#import math
#for v in a:
#    lcm = (lcm // math.gcd(lcm, v)) * v

ans = 0
for v in a:
    ans = ans + (lcm // v)
    #ans = (ans + (lcm // v)) % MOD
print(ans % MOD)
