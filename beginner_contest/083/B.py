import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, a, b = map(int, input().split())

ans = 0
for i in range(1, n+1):
    _sum = 0
    tmp_i = i
    while tmp_i:
        _sum += (tmp_i % 10)
        tmp_i //= 10
    if a <= _sum <= b:
        ans += i

print(ans)
