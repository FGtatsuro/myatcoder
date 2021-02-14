import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

INF = 10 ** 15
N, M = map(int, input().split())
dp = [[INF] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0
for i in range(M):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    dp[a][b] = t
    dp[b][a] = t

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

ans = INF
for i in range(N):
    ans = min(ans, max(dp[i]))
print(ans)
