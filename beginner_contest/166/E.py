import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

m1 = dict()
for i, v in enumerate(a):
    t = (i+1) + v
    if t not in m1:
        m1[t] = set()
    m1[t].add(i+1)

m2 = dict()
for i, v in enumerate(a):
    t = (i+1) - v
    if t <= 1:
        continue
    if t not in m1:
        continue
    if t not in m2:
        m2[t] = set()
    m2[t].add(i+1)

ans = 0
for k in m2:
    ans += len(m1[k]) * len(m2[k])

print(ans)
