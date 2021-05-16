import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
A = [0] * H
for i in range(H):
    line = []
    a = list(input().strip())
    for v in a:
        if v == '-':
            line.append(-1)
        elif v == '+':
            line.append(1)
        else:
            assert False
    A[i] = line

# dp[i][j]: (i, j)(0<=i<H, 0<=j<W)からスタートする場合の最大利得
# i+jが偶数: 高橋君の得点-青木君の得点の最大値
# i+jが奇数: 高橋君の得点-青木君の得点の最小値
INF = float('inf')
dp = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if (i+j) % 2 == 0:
            dp[i][j] = -INF
        else:
            dp[i][j] = INF
dp[H-1][W-1] = 0

for i in range(H-1, -1, -1):
    for j in range(W-1, -1, -1):
        if i == H-1 and j == W-1:
            continue
        # 高橋
        if (i+j) % 2 == 0:
            # 初期値を埋めている(H-1, W-1)以外は、少なくとも下か右かどちらかには行ける
            # 下
            if i+1 < H:
                dp[i][j] = max(dp[i][j], dp[i+1][j] + A[i+1][j])
            # 右
            if j+1 < W:
                dp[i][j] = max(dp[i][j], dp[i][j+1] + A[i][j+1])
        # 青木
        else:
            # 下
            if i+1 < H:
                dp[i][j] = min(dp[i][j], dp[i+1][j] - A[i+1][j])
            # 右
            if j+1 < W:
                dp[i][j] = min(dp[i][j], dp[i][j+1] - A[i][j+1])

if dp[0][0] > 0:
    print('Takahashi')
elif dp[0][0] < 0:
    print('Aoki')
else:
    print('Draw')

# 再帰だとTLE
#def dp_func(i, j):
#    if dp[i][j] != INF and dp[i][j] != -INF:
#        return dp[i][j]
#    # 高橋
#    if (i+j) % 2 == 0:
#        # 初期値を埋めている(H-1, W-1)以外は、少なくとも下か右かどちらかには行ける
#        # 下
#        if i+1 < H:
#            dp[i][j] = max(dp[i][j], dp_func(i+1, j) + A[i+1][j])
#        # 右
#        if j+1 < W:
#            dp[i][j] = max(dp[i][j], dp_func(i, j+1) + A[i][j+1])
#    # 青木
#    else:
#        # 下
#        if i+1 < H:
#            dp[i][j] = min(dp[i][j], dp_func(i+1, j) - A[i+1][j])
#        # 右
#        if j+1 < W:
#            dp[i][j] = min(dp[i][j], dp_func(i, j+1) - A[i][j+1])
#    return dp[i][j]
#
#if dp_func(0, 0) > 0:
#    print('Takahashi')
#elif dp_func(0, 0) < 0:
#    print('Aoki')
#else:
#    print('Draw')
