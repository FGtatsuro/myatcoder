n = int(input())
l = sorted([int(i) for i in input().split()])

from bisect import bisect_left
total = 0
for i in range(n):
    for j in range(i+1, n):
        total += (bisect_left(l, l[i] + l[j]) - j - 1)

print(total)
