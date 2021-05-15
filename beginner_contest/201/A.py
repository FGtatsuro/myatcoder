import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

A = list(map(int, input().split()))

import itertools

for A1, A2, A3 in itertools.permutations(A):
    if A3 - A2 == A2 - A1:
        print('Yes')
        sys.exit(0)
print('No')

