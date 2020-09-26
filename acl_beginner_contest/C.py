import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
graph = [0] + [[] for _ in range(n)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

from collections import deque

def bfs(graph, queue, dist):
    while queue:
        current = queue.popleft()

        for _next in graph[current]:
            if dist[_next] != -1:
                continue
            else:
                dist[_next] = dist[current] + 1
                queue.append(_next)

dist = [0] + [-1] * n
part = 0
for i in range(1, n + 1):
    if dist[i] != -1:
        continue
    else:
        queue = deque([i])
        dist[i] = 0
        bfs(graph, queue, dist)
        part += 1
print(part - 1)

