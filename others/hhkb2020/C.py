import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
p = list(map(int, input().split()))

from collections import deque

_min = 0
used = set()
num = deque(range(1, 200000 + 2))
for v in p:
    used.add(v)
    if _min not in used:
        print(_min)
    else:
        while num:
            candidate = num.popleft()
            if candidate not in used:
                _min = candidate
                break
        print(_min)
