import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
if n == 1 and m == 1:
    print(1)
    sys.exit(0)
if n == 1:
    print(m - 2)
    sys.exit(0)
if m == 1:
    print(n - 2)
    sys.exit(0)

print(n * m - (n * 2 + m * 2 - 4))
