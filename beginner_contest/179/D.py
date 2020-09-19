import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

MOD = 998244353
n, k = map(int, input().split())
s = list()
for i in range(k):
    s.append(tuple(map(int, input().split())))

dp = [0] + [0] * n
diff = [0] + [0] * n
dp[1] = 1
diff[2] = -1
for i in range(1, n):
    for j, k in s:
        if i + j > n:
            continue
        diff[i + j] += dp[i]
        if i + k + 1 > n:
            continue
        diff[i + k + 1] -= dp[i]
    #dp[i] = (dp[i - 1] + diff[i]) % MOD
    dp[i + 1] = (dp[i] + diff[i + 1]) % MOD
print(dp[n])
