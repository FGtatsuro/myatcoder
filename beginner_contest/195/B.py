import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

A, B, W = map(int, input().split())
W *= 1000
INF = float('inf')
_min = INF
_max = 0
for i in range(1, 10 ** 6 + 1):
    if A * i <= W <= B * i:
        _min = min(_min, i)
        _max = max(_max, i)
if _min == INF:
    print('UNSATISFIABLE')
else:
    print(_min, _max)
