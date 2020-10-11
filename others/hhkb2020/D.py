import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

MOD = 1000000007

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    if n < a + b:
        ans = 0
    else:
        x4 = (n - a - b + 2) * (n - a - b + 1) // 2
        x3 = 2 * x4
        x2 = (n - a + 1) * (n - b + 1) - x3
        x1 = x2 **  2
        ans = ((n - a + 1) ** 2) * ((n - b + 1) ** 2) - x1
    print(ans % MOD)
