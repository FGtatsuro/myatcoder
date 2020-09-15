import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = sorted(list(map(int, input().split())))

ans = 0
for i in range(n):
    ans += a[(3 * n) - (2*i + 2)]

print(ans)
