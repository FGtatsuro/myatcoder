import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
d, x = map(int, input().split())
ans = x
for _ in range(n):
    a = int(input())
    ans += ((d + a - 1) // a)

print(ans)
