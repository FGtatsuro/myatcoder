import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, h, m = map(int, input().split())

import math

_long = 2 * math.pi * (((60 * h) + m) / 720)
short = 2 * math.pi * (m/60)
diff = abs(_long - short)
if diff > math.pi:
    diff = 2 * math.pi - diff
print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(diff)))
