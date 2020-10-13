import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

graph = [[] for _ in range(n)]

from collections import deque, Counter

for i in range(n):
    s = input().strip()
    for j in range(i + 1, n):
        if s[j] == '1':
            graph[i].append(j)
            graph[j].append(i)

def bfs(graph, queue, dist):
    while queue:
        current = queue.popleft()

        for n in graph[current]:
            if dist[n] != -1:
                if dist[n] == dist[current]:
                    return False
            else:
                dist[n] = dist[current] + 1
                queue.append(n)
    return True

ans = -1
for i in range(n):
    queue = deque([i])
    dist = [-1] * n
    dist[i] = 0
    if bfs(graph, queue, dist):
        c = Counter(dist)
        ans = max(ans, len(c))
print(ans)
