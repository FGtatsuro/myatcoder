import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
# XC[i]: 色iの座標の(min, max)
INF = float('inf')
XC = [[INF, -INF] for _ in range(N+1)]
for i in range(N):
    X,C = map(int, input().split())
    XC[C][0] = min(XC[C][0], X)
    XC[C][1] = max(XC[C][1], X)
# 初期値: XC[0] = [0, 0]
XC[0] = [0, 0]

# dp[i][j]: 色iのボールまで全て回収が終わった際の最少コスト
# 1<=i<=N
# j=0 => min座標で終了、j=1 => max座標で終了
dp = [[INF, INF] for _ in range(N+1)]
# 初期値: dp[0] = [0, 0]
dp[0] = [0, 0]

for i in range(1, N+1):
    # 存在しない色はコスト/回収後の位置を変更せずに受け継ぐ
    if XC[i] == [INF, -INF]:
        dp[i] = dp[i-1]
        XC[i] = XC[i-1]
    else:
        l, r = XC[i]
        l_1, r_1 = XC[i-1]
        # 色iを回収後、min座標(l)にいる
        # l_1 => l
        x = l_1
        # 左に一直線
        if x >= r:
            dp[i][0] = min(dp[i][0], dp[i-1][0] + (x - l))
        # 一旦右によってから左
        else:
            dp[i][0] = min(dp[i][0], dp[i-1][0] + (r - x) + (r - l))

        # r_1 => l
        x = r_1
        # 左に一直線
        if x >= r:
            dp[i][0] = min(dp[i][0], dp[i-1][1] + (x - l))
        # 一旦右によってから左
        else:
            dp[i][0] = min(dp[i][0], dp[i-1][1] + (r - x) + (r - l))

        # 色iを回収後、max座標(r)にいる
        # l_1 => r
        x = l_1
        # 右に一直線
        if x <= l:
            dp[i][1] = min(dp[i][1], dp[i-1][0] + (r - x))
        # 一旦左によってから右
        else:
            dp[i][1] = min(dp[i][1], dp[i-1][0] + (x - l) + (r - l))

        # r_1 => r
        x = r_1
        # 右に一直線
        if x <= l:
            dp[i][1] = min(dp[i][1], dp[i-1][1] + (r - x))
        # 一旦左によってから右
        else:
            dp[i][1] = min(dp[i][1], dp[i-1][1] + (x - l) + (r - l))

# 求める値: dp[N]の値+原点まで戻るコストの小さい方
print(min(dp[N][0] + abs(XC[N][0]), dp[N][1] + abs(XC[N][1])))
