import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = list(reversed(input().strip()))
black = 0
ans = 0

for i, v in enumerate(s):
    if v == 'W':
        continue
    else:
        ans += (i - black)
        black += 1
print(ans)
