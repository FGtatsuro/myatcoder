import sys
input = sys.stdin.readline

n, k = [int(i) for i in input().split()]
p = [0] * n
for i,v in enumerate(input().split()):
    p[i] = 1.0 + 0.5 * (float(v) - 1.0)

_max_sum = 0
_prev_sum = 0
for i in range(0, n-k+1):
    if i == 0:
        _sum = sum(p[:k]) 
    else:
        _sum = _prev_sum - p[i-1] + p[i+k-1]
    if _sum >= _max_sum:
        _max_sum = _sum
    _prev_sum = _sum
print(_max_sum)
