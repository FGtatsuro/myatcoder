n, m = [int(i) for i in input().split()]
edges = [[int(i) for i in input().split()] for _ in range(m)]
graph = [[] for _ in range(n)]

import heapq

for e in edges:
    heapq.heappush(graph[e[0]], e[1])
    heapq.heappush(graph[e[1]], e[0])

def bfs(graph, dist, queue):
    while queue:
        current = queue.pop(0)
        children = graph[current]
        for c in children:
            if dist[c] != -1:
                continue
            dist[c] = dist[current] + 1
            queue.append(c)

dist = [-1] * n
dist[0] = 0
queue = [0]

bfs(graph, dist, queue)
print(dist)
