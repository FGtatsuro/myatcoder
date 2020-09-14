import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
h = [0] * n
for i in range(n):
    h[i] = int(input())
h = sorted(h)

ans = 10 ** 10
for i in range(n-k+1):
    ans = min(ans, h[i+k-1] - h[i])
print(ans)
