import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, a, b = map(int, input().split())
if a > b:
    print(0)
    sys.exit(0)
if n == 1 and a != b:
    print(0)
    sys.exit(0)
print((a + b * (n - 1)) - (b + a * (n - 1)) + 1)
