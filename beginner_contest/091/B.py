import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

from collections import Counter

n = int(input())
s = [0] * n
for i in range(n):
    s[i] = input().strip()
s = Counter(s)
m = int(input())
t = [0] * m
for i in range(m):
    t[i] = input().strip()
t = Counter(t)

ans = 0
for k in s:
    tmp = s[k]
    if k in t:
        tmp -= t[k]
    ans = max(ans, tmp)
print(ans)
