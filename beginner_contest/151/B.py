import sys
input = sys.stdin.readline

n, k, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

_min = n * m
_target = max((_min - sum(a)), 0)

if _target > k:
    print(-1)
else:
    print(_target)
