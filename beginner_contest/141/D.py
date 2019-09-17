n, m = [int(i) for i in input().split()]
a = [-1 * int(i) for i in input().split()]

import heapq

heapq.heapify(a)

for _ in range(m):
    target = heapq.heappop(a)
    target = int(target / 2)
    heapq.heappush(a, target)

print(sum(a) * -1)
