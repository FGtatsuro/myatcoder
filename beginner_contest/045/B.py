import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

from collections import deque

sa = deque(input().strip())
sb = deque(input().strip())
sc = deque(input().strip())
s = [sa, sb, sc]

turn_map = {'a': 0, 'b': 1, 'c': 2}
turn = 'a'
while True:
    if not s[turn_map[turn]]:
        break
    else:
        turn = s[turn_map[turn]].popleft()
print(turn.upper())

