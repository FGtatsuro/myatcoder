import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = [0] + list(map(int, input().split()))

# dp[i]: i番目の足場までの最少コスト
dp = [0] * (N+1)

# 初期条件
dp[0] = 0
dp[1] = 0
dp[2] = abs(A[2] - A[1])

# 漸化式
for i in range(3, N+1):
    dp[i] = min(dp[i-1] + abs(A[i]-A[i-1]), dp[i-2] + abs(A[i]-A[i-2]))

# 求める値
print(dp[N])
