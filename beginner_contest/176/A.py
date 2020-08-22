import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, x, t = map(int, input().split())

print(((n + x - 1) // x) * t)
