import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
l_key = []
r_key = []
for i in range(m):
    l, r = map(int, input().split())
    l_key.append(l)
    r_key.append(r)

print(max(0, min(r_key) - max(l_key) + 1))
