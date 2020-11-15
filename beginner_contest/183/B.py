import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

sx, sy, gx, gy = map(int, input().split())
print(((sx * gy) + (sy * gx)) / (sy + gy))
