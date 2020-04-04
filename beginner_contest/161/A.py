import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

x, y, z = map(int, input().split())
x, y = y, x
x, z = z, x
print(x, y, z)
