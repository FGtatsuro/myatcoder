import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())

ans = 0
for i in range(1, N):
    ans += N / (N - i)
print(ans)

