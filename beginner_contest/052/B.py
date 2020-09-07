import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input().strip()

ans = 0
x = 0
for v in S:
    if v == 'I':
        x += 1
    else:
        x -= 1
    ans = max(ans, x)
print(ans)
