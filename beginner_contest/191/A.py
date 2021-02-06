import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

v, t, s, d = map(int, input().split())

if v * t <= d <= v * s:
    print('No')
else:
    print('Yes')
