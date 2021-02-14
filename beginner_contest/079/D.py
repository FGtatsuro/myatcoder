import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
INF = 10 ** 15
dp = [[INF] * 10 for _ in range(10)]
for i in range(10):
    dp[i][i] = 0
for i in range(10):
    c = list(map(int, input().split()))
    for j in range(10):
        dp[i][j] = c[j]
for k in range(10):
    for i in range(10):
        for j in range(10):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

ans = 0
for i in range(H):
    for v in map(int, input().split()):
        if v == -1 or v == 1:
            continue
        ans += dp[v][1]
print(ans)
