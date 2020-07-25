import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
a = list(map(int, input().split()))

import math

def cond():
    _max = max(a)
    if k > _max:
        return False
    _gcd = a[0]
    for i in a[1:]:
        _gcd = math.gcd(_gcd, i)
    return (k % _gcd) == 0

if cond():
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
