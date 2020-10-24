import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

MOD = 10 ** 9 + 7

n, m = map(int, input().split())
a = set()
for _ in range(m):
    a.add(int(input()))

dp = [0] + [0] * n
dp[0] = 1

for i in range(n - 1):
    if i + 1 not in a:
        dp[i+1] += dp[i]
        dp[i+1] %= MOD
    if i + 2 not in a:
        dp[i+2] += dp[i]
        dp[i+2] %= MOD

if n - 1 not in a:
    dp[n] += dp[n-1]
    dp[n] %= MOD

print(dp[n] % MOD)
