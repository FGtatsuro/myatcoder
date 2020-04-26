import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
ans = set()
for i in range(n):
    ans.add(input().strip())

print(len(ans))
