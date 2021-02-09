import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m, s, t = map(int, input().split())
s -= 1
t -= 1
graph_yen = [[] for _ in range(n)]
graph_sunuke = [[] for _ in range(n)]
for _ in range(m):
    u, v, a, b = map(int, input().split())
    u -= 1
    v -= 1
    graph_yen[u].append((a, v))
    graph_yen[v].append((a, u))
    graph_sunuke[u].append((b, v))
    graph_sunuke[v].append((b, u))

import heapq

INITIAL = 10 ** 15
INF = 10 ** 16

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
cost_yen = dijkstra(graph_yen, s)
cost_sunuke = dijkstra(graph_sunuke, t)

from collections import deque
ans = deque()
min_cost = INF
for i in range(n-1, -1, -1):
    cost = cost_yen[i] + cost_sunuke[i]
    min_cost = min(min_cost, cost)
    ans.appendleft(INITIAL - min_cost)

for v in ans:
    print(v)
