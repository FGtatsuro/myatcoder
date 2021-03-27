import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
x0, y0 = map(int, input().split())
xn2, yn2 = map(int, input().split())

qx, qy = (x0 + xn2) / 2, (y0 + yn2) / 2

import math

rad = math.atan2(y0 - qy, x0 - qx)
rad += (2 * math.pi) / N
r = math.sqrt((qx-x0)**2 + (qy-y0)**2)
print(qx + r * math.cos(rad), qy + r * math.sin(rad))
