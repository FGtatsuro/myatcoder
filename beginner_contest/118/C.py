import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

import functools
print(functools.reduce(gcd, a))
