import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

INF = 10 ** 15
N, M = map(int, input().split())
dp = [[INF] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    dp[A][B] = C
    dp[B][A] = C
for k in range(N):
    for i in range(N):
        # 枝刈り
        # FYI: https://atcoder.jp/contests/arc035/submissions/20089619

        # 繋がれていなければ中間地点となりえない
        if dp[i][k] == INF:
            continue
        for j in range(N):
            # 自己ループはない
            if i == j:
                continue
            # 繋がれていなければ中間地点となりえない
            if dp[k][j] == INF:
                continue
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

K = int(input())
for _ in range(K):
    X, Y, Z = map(int, input().split())
    X -= 1
    Y -= 1
    # 距離が短くなる場合のみ更新が発生する
    # ただ、この条件判定は最悪の場合には全く動かない
    # 
    # TLE
    #if dp[X][Y] > Z:
    #    # ワーシャルフロイド法: 中間地点をX, Yにして更新する
    #    dp[X][Y] = Z
    #    dp[Y][X] = Z
    #    for k in (X, Y):
    #        for i in range(N):
    #            for j in range(N):
    #                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    #
    # FYI: https://www.slideshare.net/chokudai/arc035
    #if dp[X][Y] > Z:
    for i in range(N):
        for j in range(N):
            # 双方向グラフの場合、逆向きを忘れない
            dp[i][j] = min(dp[i][j], dp[i][X] + dp[Y][j] + Z, dp[i][Y] + dp[X][j] + Z)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += dp[i][j]
    print(ans)
