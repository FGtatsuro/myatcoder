import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

from collections import Counter

n = int(input())
d = Counter(map(int, input().split()))
m = int(input())
t = Counter(map(int, input().split()))

for k in t:
    if k not in d:
        print('NO')
        sys.exit(0)
    elif t[k] > d[k]:
        print('NO')
        sys.exit(0)
print('YES')
