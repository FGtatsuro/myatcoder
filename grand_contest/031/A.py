import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
s = input().strip()
MOD = 10 ** 9 + 7

from collections import Counter

c = Counter(s)
ans = 1
for k in c:
    ans = (ans * (c[k] + 1) % MOD)
print((ans - 1) % MOD)
