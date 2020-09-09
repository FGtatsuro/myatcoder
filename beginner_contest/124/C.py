import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = list(map(int, input().strip()))

ans1 = 0
ans2 = 0
for i, v in enumerate(s):
    if v != (i % 2):
        ans1 += 1
    else:
        ans2 += 1

print(min(ans1, ans2))
