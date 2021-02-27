import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
apx = [0] * N
INF = 10 ** 15
ans = INF
for i in range(N):
    a, p, x = map(int, input().split())
    if x - a > 0:
        ans = min(ans, p)
if ans == INF:
    print(-1)
else:
    print(ans)
