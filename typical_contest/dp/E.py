import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, W = map(int, input().split())
# 品物i(1<=i<=N)の重さと価値
wv = [0] + [0] * N
max_value = 0
for i in range(N):
    wv[i+1] = list(map(int, input().split()))
    max_value += wv[i+1][1]

# dp[i+1][j]: 品物i(0<=i<=N)番目までで価値j(0<=j<=max_value)を達成するための最少重量
INF = float('inf')
dp = [0] + [[INF] * (max_value+1) for _ in range(N+1)]
# 初期値: 品物0番目(取っていない)までで価値0を達成するための最少重量=0
dp[0+1][0] = 0
for i in range(1, N+1):
    w, v = wv[i]
    for j in range(max_value+1):
        # 品物iを取らない
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

        # 品物iを取る
        if j - v >= 0:
            dp[i+1][j] = min(dp[i+1][j], dp[i][j-v]+w)

# 求める値
for j in range(max_value, -1, -1):
    if dp[N+1][j] <= W:
        print(j)
        sys.exit(0)
