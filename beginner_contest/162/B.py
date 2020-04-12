import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

ans = 0
for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        continue
    ans += i

print(ans)
