import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = int(input())

seq = set()
seq.add(s)

_next = s
while True:
    if _next % 2 == 0:
        _next //= 2
    else:
        _next = _next * 3 + 1
    if _next in seq:
        break
    else:
        seq.add(_next)

print(len(seq) + 1)
