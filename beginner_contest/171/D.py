import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))
q = int(input())
op = [0] * q
for i in range(q):
    op[i] = map(int, input().split())

from collections import Counter

counter = Counter(a)

_sum = [sum(k * counter[k] for k in counter)] + [0] * q
index = 1
for b, c in op:
    inc = 0
    if b in counter:
        inc = (c-b) * counter[b]
        if c in counter:
            counter[c] = counter[c] + counter[b]
        else:
            counter[c] = counter[b]
        del counter[b]
    _sum[index] = _sum[index-1] + inc
    print(_sum[index])
    index += 1
