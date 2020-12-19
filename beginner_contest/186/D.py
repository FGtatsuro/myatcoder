import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = [0] + sorted(list(map(int, input().split())))

ans = (abs(a[n] - a[1])) * (n * (n - 1) // 2)
for i in range(1, n):
    ans -= (abs(a[i] - a[1])) * (n - i)
    ans -= (abs(a[i] - a[n])) * (i - 1)
print(ans)
