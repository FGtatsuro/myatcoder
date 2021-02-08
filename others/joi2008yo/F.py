import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())

graph = [[] for _ in range(n)]

import heapq

INF = 10 ** 15

def dijkstra(graph, start):
    queue = [(0, start)]
    dist = [INF] * n
    dist[start] = 0

    while queue:
        cost, current = heapq.heappop(queue)
        if cost > dist[current]:
            continue

        for next_cost, _next in graph[current]:
            if dist[_next] > dist[current] + next_cost:
                dist[_next] = dist[current] + next_cost
                heapq.heappush(queue, (dist[_next], _next))
    return dist

for _ in range(k):
    op = list(map(int, input().split()))
    if len(op) == 3:
        _, a, b = op
        a -= 1
        b -= 1
        dist = dijkstra(graph, a)
        if dist[b] == INF:
            print(-1)
        else:
            print(dist[b])
    elif len(op) == 4:
        _, c, d, e = op
        c -= 1
        d -= 1
        graph[c].append((e, d))
        graph[d].append((e, c))
    else:
        assert False
