import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, c = map(int, input().split())

import math

if c - a - b > 0 and (c - a - b) ** 2 > 4 * a * b:
    print('Yes')
else:
    print('No')
