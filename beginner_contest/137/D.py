import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

from collections import defaultdict
import heapq

n, m = map(int, input().split())
day_map = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    # heapq is min heap. This problem needs max heap.
    day_map[a-1].append(-b)

ans = 0
queue = []
for i in range(0, m):
    for v in day_map[i]:
        heapq.heappush(queue, v)
    if len(queue):
        ans += -heapq.heappop(queue)

print(ans)
