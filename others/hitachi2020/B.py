import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

A, B, M = map(int, input().split())
a = [10 ** 10] + list(map(int, input().split()))
b = [10 ** 10] + list(map(int, input().split()))
ans = 10 ** 10
for _ in range(M):
    x, y, c = map(int, input().split())
    ans = min(ans, a[x] + b[y] - c)
ans = min(ans, min(a) + min(b))

print(ans)
