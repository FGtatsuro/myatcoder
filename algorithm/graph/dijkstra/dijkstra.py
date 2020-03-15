import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    n1, n2 = list(map(int, input().split()))
    # (cost, num)
    graph[n1].append((1, n2))
    graph[n2].append((1, n1))

import heapq

# Ref. https://qiita.com/ageprocpp/items/cdf67e828e1b09316f6e#%E3%83%80%E3%82%A4%E3%82%AF%E3%82%B9%E3%83%88%E3%83%A9%E6%B3%95
def dijkstra(graph, queue, dist):
    while queue:
        # (dist, num)
        current_dist, current_num = heapq.heappop(queue)
        if dist[current_num] < current_dist:
            continue
        for cost, next_num in graph[current_num]:
            if dist[next_num] > current_dist + cost:
                dist[next_num] = current_dist + cost
                heapq.heappush(queue, (dist[next_num], next_num))

queue = [(0, 0)]
dist = [10 ** 7] * n
dist[0] = 0
dijkstra(graph, queue, dist)
print(dist)
