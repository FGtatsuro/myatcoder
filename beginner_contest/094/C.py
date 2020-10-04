import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
x = list(map(int, input().split()))

from collections import defaultdict, deque
rank = defaultdict(deque)
sx = sorted(x)
c1, c2 = sx[n // 2 -1], sx[n // 2]
for i, v in enumerate(sx):
    rank[v].append(i + 1)
for v in x:
    r = rank[v].popleft()
    if r <= n // 2:
        print(c2)
    else:
        print(c1)
