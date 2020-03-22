import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = list(map(int, input().split()))

ans = 0
if n > 1:
    ans += (n * (n-1))//2
if m > 1:
    ans += (m * (m-1))//2

print(ans)
