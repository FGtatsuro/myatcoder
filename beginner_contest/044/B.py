import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

w = input().strip()

from collections import Counter

c = Counter(w)

for v in c.values():
    if v % 2 == 1:
        print('No')
        sys.exit(0)
print('Yes')
