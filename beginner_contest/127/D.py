import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

from collections import deque

n, m = map(int, input().split())
a = deque(sorted(map(int, input().split())))
bc = []
for _ in range(m):
    b, c = map(int, input().split())
    bc.append((b, c))
bc = sorted(bc, key=lambda x: -x[1])

ans = []
for b, c in bc:
    finish = False
    for i in range(b):
        if len(a) == 0:
            finish = True
            break
        if c < a[0]:
            finish = True
            break
        else:
            a.popleft()
            ans.append(c)
    if finish:
        break
ans.extend(a)
print(sum(ans))
