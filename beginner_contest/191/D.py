import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

x, y, r = map(float, input().split())
mul = 10 ** 4
x = round(x * mul)
y = round(y * mul)
r = round(r * mul)

def lower(x, m):
    assert m != 0
    if x >= 0:
        return (((x + m) - 1) // m) * m
    else:
        return -(int((-x) / m) * m)

def upper(x, m):
    assert m != 0
    if x >= 0:
        return int(x / m) * m
    else:
        return -((((-x + m) - 1) // m) * m)

import math

# Ref: https://atcoder.jp/contests/abc191/submissions/20013815
# FYI:
#   http://www.pi-sliderule.net/sliderule/others/babylonia.html
#   https://cpplover.blogspot.com/2010/11/blog-post_20.html
# 小数部を切り捨てているから必ず真の平方根より小さくなる?
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

from decimal import Decimal

ans = 0
for i in range(lower(x - r, mul), upper(x + r, mul) + 1, mul):
    # これでは精度が足りなかった
    #j = int(math.sqrt(r ** 2 - (x - i) ** 2))

    #j = int(isqrt(r ** 2 - (x - i) ** 2))
    # Ref: https://atcoder.jp/contests/abc191/submissions/20013782
    j = int(Decimal(r ** 2 - (x - i) ** 2).sqrt())
    _min = lower(y - j, mul)
    _max = upper(y + j, mul)
    ans += ((_max - _min) // mul) + 1
print(ans)
