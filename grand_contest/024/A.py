import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, c, k = map(int, input().split())

ans = None
if k % 2 == 0:
    ans = a - b
else:
    ans = b - a

if abs(ans) > 10 ** 18:
    print('Unfair')
else:
    print(ans)
