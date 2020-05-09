import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
x = list(map(int, input().split()))

ans = (100 ** 2) * 100 + 1

_min = min(x)
_max = max(x)

for i in range(_min, _max + 1):
    tmp = 0
    for j in x:
        tmp += (j - i) ** 2
    ans = min(ans, tmp)

print(ans)

