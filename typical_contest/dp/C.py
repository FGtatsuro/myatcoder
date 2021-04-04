import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 * 7)

N = int(input())
# i日目(i:1-N)の活動の幸福度
ABC = [0] + [0] * N
for i in range(N):
    ABC[i+1] = list(map(int, input().split()))

# dp[i][j]: i日目に活動jを行った場合の幸福度の総和最大値
# j: 0=A, 1=B, 2=C
dp = [[0] * 3 for _ in range(N+1)]
# 初期化: dp[0][i]=0
for i in range(3):
    dp[0][i] = 0
for i in range(1, N+1):
    # i日目の活動A
    dp[i][0] = max(dp[i-1][1] + ABC[i][0], dp[i-1][2] + ABC[i][0])

    # i日目の活動B
    dp[i][1] = max(dp[i-1][0] + ABC[i][1], dp[i-1][2] + ABC[i][1])

    # i日目の活動C
    dp[i][2] = max(dp[i-1][0] + ABC[i][2], dp[i-1][1] + ABC[i][2])
print(max(dp[N]))
