import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, x = map(int, input().split())

total = 0
for i in range(n):
    v, p = map(int, input().split())
    total += v * p
    if total > x * 100:
        print(i + 1)
        sys.exit(0)
print(-1)
