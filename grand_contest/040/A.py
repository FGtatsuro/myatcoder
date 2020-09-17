import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()
n = len(s) + 1

ans = [[0, 0] for _ in range(n)]
# 左に連続する<
for i in range(1, n):
    if s[i-1] == '<':
        ans[i][0] = ans[i-1][0] + 1
# 右に連続する>
for i in range(0, n-1):
    if s[n-2-i] == '>':
        ans[n-2-i][1] = ans[n-1-i][1] + 1
print(sum(max(i) for i in ans))
