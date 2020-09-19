import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
s = input().strip()

ans = 0
for i in range(1, n):
    ans = max(ans, len(set(s[:i]).intersection(s[i:])))
print(ans)
