import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
a = list(map(int, input().split()))

total = sum(a)
if total > n:
    print(-1)
    sys.exit(0)

print(n - total)
