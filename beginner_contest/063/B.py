import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()

from collections import Counter
c = Counter(s)
if set(list(c.values())) == {1}:
    print('yes')
else:
    print('no')
