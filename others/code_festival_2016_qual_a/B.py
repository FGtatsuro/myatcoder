import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = [0] + list(map(int, input().split()))

ans = 0
for i, v in enumerate(a):
    if i == 0:
        continue
    if i == a[v]:
        ans += 1
print(ans // 2)
