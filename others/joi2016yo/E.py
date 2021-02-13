import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M, K, S = map(int, input().split())
P, Q = map(int, input().split())
z = [False] * N
for i in range(K):
    C = int(input())
    C -= 1
    z[C] = True
graph = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

from collections import deque
danger = [False] * N
for i, v in enumerate(z):
    if v:
        queue = deque([i])
        dist = [-1] * N
        dist[i] = 0

        while queue:
            current = queue.popleft()
            for _next in graph[current]:
                if dist[_next] != -1:
                    continue
                #dist[_next] = dist[current] + 1
                #if dist[_next] <= S:
                #    danger[_next] = True
                #queue.append(_next)
                danger[_next] = True
                dist[_next] = dist[current] + 1
                # Sより長いパスは探索する必要がない
                if dist[_next] < S:
                    queue.append(_next)
# 1回のBFSで求めるやり方
#from collections import deque
#
#z = [False] * N
#danger = [False] * N
#dist = [-1] * N
#queue = deque()
#for i in range(K):
#    C = int(input())
#    C -= 1
#    z[C] = True
#    queue.append(C)
#    dist[C] = 0
#graph = [[] for _ in range(N)]
#for i in range(M):
#    A, B = map(int, input().split())
#    A -= 1
#    B -= 1
#    graph[A].append(B)
#    graph[B].append(A)
#
#while queue:
#    current = queue.popleft()
#    for _next in graph[current]:
#        if dist[_next] != -1:
#            continue
#        #dist[_next] = dist[current] + 1
#        #if dist[_next] <= S:
#        #    danger[_next] = True
#        #queue.append(_next)
#        danger[_next] = True
#        dist[_next] = dist[current] + 1
#        # Sより長いパスは探索する必要がない
#        if dist[_next] < S:
#            queue.append(_next)
#print(danger)
#for i, v in enumerate(danger):
#    if v:
#        print(i, v)

import heapq    

INF = 10 ** 15
queue = [(0, 0)]
dist = [INF] * N
dist[0] = 0
while queue:
    cost, current = heapq.heappop(queue)
    if cost > dist[current]:
        continue
    for _next in graph[current]:
        if z[_next]:
            continue

        if _next == N - 1:
            next_cost = 0
        elif danger[_next]:
            next_cost = Q
        else:
            next_cost = P

        if dist[_next] > dist[current] + next_cost:
            dist[_next] = dist[current] + next_cost
            heapq.heappush(queue, (dist[_next], _next))

print(dist[-1])
