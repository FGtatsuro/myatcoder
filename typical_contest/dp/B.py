import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
h = list(map(int, input().split()))

# dp[i]: 足場iへの最少コスト
dp = [float('inf')] * N
dp[0] = 0

for i in range(N):
    for j in range(1, K+1):
        if i + j >= N:
            break
        dp[i+j] = min(dp[i+j], dp[i] + abs(h[i+j] - h[i]))

print(dp[N-1])
