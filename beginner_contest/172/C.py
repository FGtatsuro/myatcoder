import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

from itertools import accumulate

n, m, k = map(int, input().split())
a = [0]
for i in accumulate(map(int, input().split())):
    if i <= k:
        a.append(i)
b = [0]
for i in accumulate(map(int, input().split())):
    if i <= k:
        b.append(i)

ans = 0
a_index = 0
b_index = len(b) - 1
for a_index in range(len(a)):
    while a[a_index] + b[b_index] > k:
        b_index -= 1
        if b_index < 0:
            break
    if b_index < 0:
        break
    else:
        ans = max(ans, a_index + b_index)
print(ans)

