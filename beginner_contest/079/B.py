import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

dp = [0] * (n + 1)
dp[0] = 2
dp[1] = 1

def l(n):
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = l(n-1) + l(n-2)
        return dp[n]

print(l(n))

