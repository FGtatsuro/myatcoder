import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

from collections import deque

n, c, k = map(int, input().split())
t = [0] * n
for i in range(n):
    t[i] = int(input())
t = deque(sorted(t))
ans = 0
while t:
    ans += 1

    first = t.popleft()
    num = 1
    while t and t[0] <= first + k and num < c:
        t.popleft()
        num += 1
print(ans)
