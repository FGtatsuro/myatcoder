import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

d, n = map(int, input().split())

if n != 100:
    print((100 ** d) * n)
else:
    print((100 ** d) * (n + 1))
