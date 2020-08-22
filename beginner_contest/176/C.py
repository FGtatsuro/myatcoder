import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

_max = 0
ans = 0
for v in a:
    _max = max(_max, v)
    ans += (_max - v)

print(ans)
