import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

result = []
for _ in range(n):
    result.append(input().strip())

from collections import Counter
c = Counter(result)

for r in ('AC', 'WA', 'TLE', 'RE'):
    print('{} x {}'.format(r, c[r]))
