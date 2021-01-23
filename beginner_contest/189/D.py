import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
# (True, False)
dp = [0] * (n+1)
dp[0] = (1, 1)
for i in range(1, n + 1):
    s = input().strip()
    if s == 'AND':
        dp[i] = (dp[i-1][0], dp[i-1][0] + dp[i-1][1] * 2)
    elif s == 'OR':
        dp[i] = (dp[i-1][0] * 2 + dp[i-1][1], dp[i-1][1])
    else:
        assert False

print(dp[n][0])
