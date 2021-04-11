import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

R, X, Y = map(int, input().split())

import math
import decimal
d = (decimal.Decimal(X ** 2) + decimal.Decimal(Y ** 2)).sqrt()
if d/R < 1:
    print(2)
else:
    print(math.ceil(d / R))
