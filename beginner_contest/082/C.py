import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

from collections import Counter
ans = 0
a = Counter(a)

ans = 0
for k in a:
    if k > a[k]:
        ans += a[k]
    else:
        ans += (a[k] - k)
print(ans)
