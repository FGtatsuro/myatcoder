import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
l = list(map(int, input().split()))

import itertools

ans = 0
for i, j, k in itertools.combinations(range(n), 3):
    if (l[i] == l[j]) or (l[i] == l[k]) or (l[j] == l[k]):
        continue
    else:
        if (l[i] + l[j] > l[k]) and (l[i] + l[k] > l[j]) and (l[j] + l[k] > l[i]):
            ans += 1
print(ans)
