import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
b = list(map(int, input().split()))

from collections import deque

step = deque()
while b:
    length = len(b)
    new_b = deque()
    removed = False
    for i in range(length - 1, -1, -1):
        if removed:
            new_b.appendleft(b[i])
            continue

        if b[i] == i + 1:
            removed = True
            step.appendleft(b[i])
        else:
            new_b.appendleft(b[i])
    if not removed:
        print(-1)
        sys.exit(0)
    b = new_b
for s in step:
    print(s)
