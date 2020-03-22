import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

import collections

c = collections.Counter(a)

combinations = [0] + [0] * n
for i in range(0, n+1):
    combinations[i] = (i * (i-1)) // 2
memo = [0] + [0] * n

for k in c:
    memo[k] = combinations[c[k]]

total = sum(memo)
for i in a:
    print(total - memo[i] + combinations[c[i] - 1])
