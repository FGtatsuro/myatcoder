import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, c, d = map(int, input().split())

ans = max(a * c, a * d, b * c, b * d)

if ans < 0 and (a <= 0 <= b or c <= 0 <= d):
    print(0)
else:
    print(ans)
