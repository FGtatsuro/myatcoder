import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
a = list(map(int, input().split()))
accum = [0] * n
accum[0] = a[0]
for i in range(1, n):
    accum[i] = accum[i-1] + a[i]
accum = [0] + accum
ans = 0
start = 0
over = 1
while over <= n:
    if accum[over] - accum[start] >= k:
        ans += (n - over + 1)
        start += 1
    else:
        over += 1
print(ans)
