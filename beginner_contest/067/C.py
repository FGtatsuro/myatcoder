import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))
_sum = sum(a)
accum = [0] * n
accum[0] = a[0]
for i in range(1, n):
    accum[i] = accum[i-1] + a[i]

ans = None
for v in accum[:-1]:
    diff = abs((_sum - v) - v)
    if ans is None:
        ans = diff
    else:
        ans = min(ans, diff)
print(ans)
