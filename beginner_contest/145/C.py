n = int(input())
points = [[int(i) for i in input().split()] for _ in range(n)]

import functools
import itertools
import math

@functools.lru_cache()
def dist_calc(p1, p2):
    return math.sqrt((points[p1][0] - points[p2][0]) ** 2 + (points[p1][1] - points[p2][1]) ** 2)

dist = []
for route in itertools.permutations(range(n)):
    for i in range(n-1):
        dist.append(dist_calc(route[i], route[i+1]))

print(sum(dist)/math.factorial(n))
