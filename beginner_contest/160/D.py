import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, x, y = list(map(int, input().split()))
graph = [0] + [[] for _ in range(n)]
for i in range(n - 1):
    graph[i+1].append(i+2)
    graph[i+2].append(i+1)
graph[x].append(y)
graph[y].append(x)

def bfs(graph, queue, dist, num):
    while queue:
        current = queue.pop(0)

        for c in graph[current]:
            if dist[c] != -1:
                continue
            dist[c] = dist[current] + 1
            num[dist[c]] += 1
            queue.append(c)

num = [0] + [0] * (n - 1)
for i in range(1, n+1):
    queue = [i]
    dist = [-1] + [-1] * n
    dist[i] = 0
    bfs(graph, queue, dist, num)

for v in num[1:]:
    print(v // 2)
