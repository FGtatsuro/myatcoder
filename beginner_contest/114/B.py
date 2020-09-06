import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()

ans = 1000
for i in range(len(s) - 2):
    ans = min(ans, abs(753 - int(s[i:i+3])))
print(ans)
