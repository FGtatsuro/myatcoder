import sys
input = sys.stdin.readline

n = int(input())
p = tuple([int(i) for i in input().split()])
q = tuple([int(i) for i in input().split()])

import itertools

lst = list(itertools.permutations(range(1, n+1)))
print(abs(lst.index(p) - lst.index(q)))
