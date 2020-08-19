import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m, c = map(int, input().split())
b = list(map(int, input().split()))

ans = 0
for _ in range(n):
    a = list(map(int, input().split()))
    tmp = 0
    for i in range(m):
        tmp += a[i] * b[i]
    tmp += c
    if tmp > 0:
        ans += 1

print(ans)
