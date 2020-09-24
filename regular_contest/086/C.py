import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))
count = [0] * (n + 1)
for v in a:
    count[v] += 1
count = deque(sorted(v for v in count if v != 0))
kind = len(count)
ans = 0
while kind > k:
    v = count.popleft()
    kind -= 1
    ans += v
print(ans)
