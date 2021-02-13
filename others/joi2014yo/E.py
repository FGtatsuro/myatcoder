import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
taxi = [0] * N
for i in range(N):
    C, R = map(int, input().split())
    taxi[i] = (C, R)
graph = [[] for _ in range(N)]
for _ in range(K):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

from collections import deque

INF = 10 ** 8

def bfs(graph, new_graph, start, taxi_info):
    dist = [-1] * N
    dist[start] = 0
    queue = deque([start])
    _, r = taxi_info
    while queue:
        current = queue.popleft()
        # これ以上の距離は乗れない
        if dist[current] == r:
            continue
        for _next in graph[current]:
            if dist[_next] != -1:
                continue
            dist[_next] = dist[current] + 1
            # r以内であるならば同じコストで移動できる
            #new_graph[start].add(_next)
            new_graph[start].append(_next)
            queue.append(_next)

import heapq

def dijkstra(new_graph, start):
    dist = [INF] * N
    dist[start] = 0
    queue = [(0, start)]
    while queue:
        total_cost, current = heapq.heappop(queue)
        if total_cost > dist[current]:
            continue
        cost_to_next, _ = taxi[current]
        for  _next in new_graph[current]:
            if dist[_next] > dist[current] + cost_to_next:
                dist[_next] = dist[current] + cost_to_next
                heapq.heappush(queue, (dist[_next], _next))
    return dist

# setを使うとメモリ量が増えMLE
#new_graph = [set() for _ in range(N)]
new_graph = [[] for _ in range(N)]
for i in range(N):
    bfs(graph, new_graph, i, taxi[i])
dist = dijkstra(new_graph, 0)

#print(new_graph)
#print(dist)

print(dist[-1])
