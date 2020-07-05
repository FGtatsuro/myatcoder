import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

from collections import deque

a = deque(sorted(a, reverse=True))
ans = 0
first = a.popleft()
second = a.popleft()
ans += first
max_comfort = second
while True:
    if len(a) == 0:
        break
    ans += max_comfort
    a.pop()
    if len(a) == 0:
        break
    ans += max_comfort
    max_comfort = a.popleft()
print(ans)
