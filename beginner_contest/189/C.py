import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

ans = 0
for l in range(n):
    _min = a[l]
    for r in range(l, n):
        _min = min(_min, a[r])
        ans = max(ans, _min * (r - l + 1))
print(ans)
