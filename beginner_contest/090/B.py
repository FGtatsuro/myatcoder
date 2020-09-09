import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b = map(int, input().split())

ans = 0
for v in range(a, b+1):
    v = str(v)
    if v == ''.join(reversed(v)):
        ans += 1
print(ans)
