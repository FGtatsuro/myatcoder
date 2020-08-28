import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import heapq

n = int(input())
u = list(map(int, input().split()))
heapq.heapify(u)
for _ in range(n-1):
    heapq.heappush(u, (heapq.heappop(u) + heapq.heappop(u)) / 2)

print(heapq.heappop(u))
