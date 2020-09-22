import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
ans = set()
for _ in range(n):
    a = int(input())
    if a in ans:
        ans.remove(a)
    else:
        ans.add(a)
print(len(ans))
