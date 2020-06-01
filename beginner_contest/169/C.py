import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import decimal

a, b = input().split()
a = decimal.Decimal(a)
b = decimal.Decimal(b)
print(int(a * b))
