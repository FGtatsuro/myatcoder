import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, x = input().strip().split()
a = input().strip().split()
ans = []
for v in a:
    if v != x:
        ans.append(v)

print(' '.join(ans))
