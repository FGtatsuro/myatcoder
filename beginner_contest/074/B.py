import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
k = int(input())
x = [0] + list(map(int, input().split()))

ans = 0
for i in range(1, n+1):
    ans += min(abs(x[i] - 0) * 2, abs(x[i] - k) * 2)
print(ans)
