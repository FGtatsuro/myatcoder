import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M, K = map(int, input().split())
t = [0] * N
for i in range(2, N):
    t[i-1] = int(input())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((c, d, b))
    graph[b].append((c, d, a))

import heapq

INF = 10 ** 16

def dijkstra(graph, start):
    queue = [(0, start)]
    dist = [INF] * N
    dist[start] = 0

    while queue:
        cost, current = heapq.heappop(queue)
        if cost > dist[current]:
            continue

        for n_cost, n_train_mul, n in graph[current]:
            new_cost = dist[current]
            # 現在の駅で列車が発車するのを待つ
            if dist[current] % n_train_mul != 0:
                new_cost += (n_train_mul - (dist[current] % n_train_mul))

            # 移動する
            new_cost += n_cost

            # 目的の駅についた後に乗りかえる
            new_cost += t[n]

            if dist[n] > new_cost:
                dist[n] = new_cost
                heapq.heappush(queue, (dist[n], n))
    return dist

dist = dijkstra(graph, 0)
if dist[-1] == INF or dist[-1] > K:
    print(-1)
else:
    print(dist[-1])
