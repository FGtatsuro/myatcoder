import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m, s, t = list(map(int, input().split()))
graph = [0] + [[] for _ in range(n)]
for _ in range(m):
    u, v, a, b = list(map(int, input().split()))
    # (cost, dest)
    graph[u].append(({'yen': a, 'sunuke': b}, v))
    graph[v].append(({'yen': a, 'sunuke': b}, u))

import heapq

def dijkstra(graph, queue, dist, cost_type):
    while queue:
        d, n = heapq.heappop(queue)
        if dist[n] != -1 and dist[n] < d:
            continue
        for cost, next_n in graph[n]:
            cost_with_type = cost[cost_type]
            if dist[next_n] > d + cost_with_type:
                dist[next_n] = d + cost_with_type
                heapq.heappush(queue, (dist[next_n], next_n))

queue = [(0, s)]
dist_yen = [10 ** 16] + [10 ** 16] * n
dist_yen[s] = 0
dijkstra(graph, queue, dist_yen, 'yen')

queue = [(0, t)]
dist_sunuke = [10 ** 16] + [10 ** 16] * n
dist_sunuke[t] = 0
dijkstra(graph, queue, dist_sunuke, 'sunuke')

# FYI: https://atcoder.jp/contests/soundhound2018-summer-qual/submissions/10738125
answer = [0] + [0] * n
for i in range(n, 0, -1):
    answer[i - 1] = max(answer[i], 10 ** 15 - (dist_yen[i] + dist_sunuke[i]))
for i in range(n):
    print(answer[i])
