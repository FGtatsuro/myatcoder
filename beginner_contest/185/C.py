import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

l = int(input())

import functools

a = functools.reduce(lambda x, y: x * y, range(l - 11, l))
b = functools.reduce(lambda x, y: x * y, range(1, 12))
print(a // b)
