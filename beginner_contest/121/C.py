import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
prices = [0] * n
for i in range(n):
    prices[i] = tuple(map(int, input().split()))
prices = sorted(prices)

ans = 0
for a, b in prices:
    if m <= b:
        ans += (a * m)
        break
    else:
        ans += (a * b)
        m -= b
print(ans)
