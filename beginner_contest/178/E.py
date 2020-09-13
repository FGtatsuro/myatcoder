import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
xy = [0] * n

xy_plus_max = -10 ** 10
xy_plus_min = 10 ** 10
xy_minus_max = -10 ** 10
xy_minus_min = 10 ** 10
for i in range(n):
    x, y = map(int, input().split())
    xy_plus_max = max(xy_plus_max, x + y)
    xy_plus_min = min(xy_plus_min, x + y)
    xy_minus_max = max(xy_minus_max, x - y)
    xy_minus_min = min(xy_minus_min, x - y)

print(max(xy_plus_max - xy_plus_min, xy_minus_max - xy_minus_min))
