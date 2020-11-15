import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import itertools

n, k = map(int, input().split())
cost = [0] * n
for i in range(n):
    cost[i] = list(map(int, input().split()))

ans = 0
for p in itertools.permutations(range(1, n)):
    tmp = 0
    tmp += cost[0][p[0]]
    tmp += cost[p[-1]][0]
    for i in range(len(p) - 1):
        tmp += cost[p[i]][p[i+1]]
    if tmp == k:
        ans += 1
print(ans)
