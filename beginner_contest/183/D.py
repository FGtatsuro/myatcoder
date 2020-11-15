import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, w = map(int, input().split())
plan = [0] * n
max_t = 0
for i in range(n):
    plan[i] = list(map(int, input().split()))
    max_t = max(max_t, plan[i][1])
_sum = [0] * (max_t + 1)
for s, t, p in plan:
    _sum[s] += p
    _sum[t] -= p
accum = [0] * len(_sum)
accum[0] = _sum[0]
for i in range(1, len(_sum)):
    accum[i] = accum[i-1] + _sum[i]
if max(accum) <= w:
    print('Yes')
else:
    print('No')
