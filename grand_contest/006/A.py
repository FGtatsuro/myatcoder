import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
s = input().strip()
t = input().strip()

ans = n * 2
for i in range(0, n):
    if s[i:n] == t[0:n-i]:
        ans -= (n - i)
        break
print(ans)
