import sys
input = sys.stdin.readline

n = int(input())
candidate = []
ans = 0

import itertools

for i in range(1, n+1):
    if (i % 10) != 0:
        candidate.append(str(i))
# for i, j in (itertools.product(['1', '2', '3', '4', '5', '6', '7', '8', '9'], repeat=2)):
for i, j in (itertools.product(range(1, 10), repeat=2)):
    i_j = 0
    j_i = 0
    for k in candidate:
        # start, end = k[0], k[-1]
        start, end = int(k[0]), int(k[-1])
        if start == i and end == j:
            i_j += 1
        if start == j and end == i:
            j_i += 1
    ans += (i_j * j_i)

print(ans)
