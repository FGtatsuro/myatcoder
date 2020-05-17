import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
graph = [-1] + [[] for _ in range(n)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

from collections import deque

def bfs(graph, queue, dist, prev):
    while queue:
        current = queue.popleft()

        for c in graph[current]:
            if dist[c] != -1:
                continue
            dist[c] = dist[current] + 1
            prev[c] = current
            queue.append(c)

queue = deque([1])
dist = [0] + [-1] * n
prev = [0] + [-1] * n
dist[1] = 0
prev[1] = 0
bfs(graph, queue, dist, prev)
if -1 in prev:
    print('No')
else:
    print('Yes')
    for p in prev[2:]:
        print(p)
