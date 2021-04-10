import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
xy = [[] for _ in range(N)]
# 0オリジンに変換
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    xy[x].append(y)

# dp[i]: i(0<=i<=N-1)を始点とする最長経路長
dp = [-1] * N

def dfs(x):
    if dp[x] != -1:
        return dp[x]
    ans = 0
    # dfs(y)+1: (x->y) + yを始点とする最長経路
    for y in xy[x]:
        ans = max(ans, dfs(y)+1)
    dp[x] = ans
    return dp[x]

ans = 0
for i in range(N):
    ans = max(ans, dfs(i))
print(ans)
