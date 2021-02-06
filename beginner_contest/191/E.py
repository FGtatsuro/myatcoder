import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())

graph = [0] + [[] for _ in range(n)]
dp = [0] + [10 ** 10] * n
loop = [0] + [10 ** 10] * n
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    if a == b:
        loop[a] = min(loop[a], c)

import heapq

def dijkstra(graph, queue, dist):
    while queue:
        cost, current = heapq.heappop(queue)
        if cost > dist[current]:
            continue
        for n_cost, n in graph[current]:
            if dist[n] > dist[current] + n_cost:
                dist[n] = dist[current] + n_cost
                heapq.heappush(queue, (dist[n], n))

for i in range(1, n + 1):
    dist = [0] + [10 ** 10] * n
    dist[i] = 0
    queue = [(0, i)]
    dijkstra(graph, queue, dist)
    dp[i] = dist

for i in range(1, n + 1):
    dp[i][i] = loop[i]
for i in range(1, n + 1):
    ans = 10 ** 10
    for j in range(1, n + 1):
        if i == j:
            tmp_ans = dp[i][i]
        else:
            tmp_ans = dp[i][j] + dp[j][i]
        ans = min(tmp_ans, ans)
    if ans == 10 ** 10:
        print(-1)
    else:
        print(ans)
