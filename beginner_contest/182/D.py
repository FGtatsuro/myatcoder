import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))
if n == 1:
    if a[0] > 0:
        print(a[0])
    else:
        print(0)
    sys.exit(0)

accum = [0] * n
accum[0] = a[0]
peek = [0] * n
peek[0] = a[0]
for i in range(1, n):
    accum[i] = accum[i-1] + a[i]
    peek[i] = max(accum[i], peek[i-1])
last = [0] * (n + 1)
for i in range(1, n + 1):
    last[i] = last[i-1] + accum[i-1]
ans = 0
for i in range(n):
    ans = max(ans, last[i] + peek[i])
print(ans)
