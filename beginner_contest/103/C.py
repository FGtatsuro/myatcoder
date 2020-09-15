import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))
ans = 0
for v in a:
    ans += (v - 1)
print(ans)
