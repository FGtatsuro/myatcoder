import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

INF = 10 ** 15

N, M, P = map(int, input().split())
edges = [0] * M
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    # ベルマンフォード法を使うため符号を反転する
    # 1分=1辺につきPのコストをあらかじめ考慮しておく
    c -= P
    c = -c
    edges[i] = [a, b, c]

cost = [INF] * N
cost[0] = 0

for i in range(N - 1):
    for e in edges:
        a, b, c = e
        if cost[a] == INF:
            continue
        if cost[b] > cost[a] + c:
            cost[b] = cost[a] + c

ans = -cost[-1]

# 負経路の伝播
# 答えに影響する負経路=>負経路を経由して目的地に辿りつける
negative = [False] * N
for i in range(N):
    for e in edges:
        a, b, c = e
        if cost[a] == INF:
            continue
        if cost[b] > cost[a] + c:
            negative[b] = True
        if negative[a]:
            negative[b] = True

if negative[-1]:
    print(-1)
else:
    if ans > 0:
        print(ans)
    else:
        # 負になるのは最終的な支払いが足りない場合
        print(0)
