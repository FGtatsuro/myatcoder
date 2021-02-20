import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M, X, Y = map(int, input().split())
X -= 1
Y -= 1
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, T, K = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append((T, B, K))
    graph[B].append((T, A, K))
    # 同じ組み合わせがあった場合、上書きしてしまう
    #mul[A][B] = K
    #mul[B][A] = K

import heapq

INF = float('inf')

queue = [(0, X)]
time = [INF] * N
time[X] = 0
while queue:
    cost, current = heapq.heappop(queue)
    if cost > time[current]:
        continue
    for n_cost, n, mul in graph[current]:
        total_time = time[current]
        if total_time % mul != 0:
            total_time = total_time + (mul - (total_time % mul))
        total_time += n_cost
        if time[n] > total_time:
            time[n] = total_time
            heapq.heappush(queue, (time[n], n))

if time[Y] == INF:
    print(-1)
else:
    print(time[Y])
