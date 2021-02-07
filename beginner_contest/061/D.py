import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

INF = 10 ** 15

N, M = map(int, input().split())
edges = [0] * M
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    # ベルマンフォード法を使うため、コストの正負を逆にする
    c = -c
    edges[i] = [a, b, c]
cost = [0] * N
for i in range(N):
    cost[i] = INF

cost[0] = 0
for i in range(N - 1):
    for e in edges:
        a, b, c = e
        if cost[a] == INF:
            continue
        if cost[b] > cost[a] + c:
            cost[b] = cost[a] + c

ans = -cost[-1]

# 負経路の検出だけでは足りない?
# 有向グラフのため、負経路を利用した場合に最終地点に辿りつけない場合がある
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
    print('inf')
else:
    print(ans)
