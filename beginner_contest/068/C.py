import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
graph = [0] + [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dist = [0] + [-1] * n

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

dist[1] = 0
queue = deque([1])
bfs(graph, queue, dist)
if dist[n] == 2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
