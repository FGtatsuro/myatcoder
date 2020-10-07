import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

from collections import deque

n = int(input())
a, b = deque(), deque()
for _ in range(n):
    ai, bi = map(int, input().split())
    a.appendleft(ai)
    b.appendleft(bi)
ans = 0
for i in range(n):
    r = (a[i] + ans) % b[i]
    if r != 0:
        ans += b[i] - r
print(ans)
