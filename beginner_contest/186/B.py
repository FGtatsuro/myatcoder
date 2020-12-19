import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

h, w = map(int, input().split())

a = []
for _ in range(h):
    for v in map(int, input().split()):
        a.append(v)
print(sum(a) - (min(a) * len(a)))
