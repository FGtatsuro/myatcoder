import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, W = map(int, input().split())
wv = [0] + [0] * N
# 品物i(1<=i<=N)の重さと価値
for i in range(N):
    wv[i+1] = list(map(int, input().split()))

# dp[i+1][j]: 品物iまでの価値の最大値(総重量j)
INF = -float('inf')
dp = [[INF] * (W+1) for _ in range(N+2)]
# 初期値: 品物0(何もとっていない)までの価値の最大値(総重量0)
dp[1][0] = 0

for i in range(1, N+1):
    w, v = wv[i]
    for j in range(W+1):
        # 品物iを取らない
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

        # 品物iを取る
        # INFであれば、その総重量はありえない
        if j - w < 0 or dp[i][j-w] == INF:
            continue
        dp[i+1][j] = max(dp[i+1][j], dp[i][j-w] + v)

print(max(dp[N+1]))
