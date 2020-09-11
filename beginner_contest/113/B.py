import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

_min = 10 ** 7
ans = None
for i, v in enumerate(h):
    c = abs((t - 0.006 * v) - a)
    if c < _min:
        _min = c
        ans = i + 1
print(ans)
