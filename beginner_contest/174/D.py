import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
s = input().strip()

from collections import deque

red_pos = deque([])
white_pos = deque([])
for i, v in enumerate(s):
    if v == 'R':
        red_pos.append(i)
    else:
        white_pos.append(i)

ans = 0
while True:
    if len(red_pos) == 0 or len(white_pos) == 0:
        break
    if red_pos[-1] < white_pos[0]:
        break
    ans += 1
    white_pos.popleft()
    red_pos.pop()

print(ans)
