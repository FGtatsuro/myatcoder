import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

from collections import Counter

s = input().strip()
c = Counter(s)
if 'a' not in c:
    c['a'] = 0
if 'b' not in c:
    c['b'] = 0
if 'c' not in c:
    c['c'] = 0
c = list(c.values())
if max(c) - min(c) <= 1:
    print('YES')
else:
    print('NO')
