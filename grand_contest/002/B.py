import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
count = [0] + [1] * n
ans = set([1])

for _ in range(m):
    x, y = map(int, input().split())
    count[x] -= 1
    count[y] += 1
    if x in ans:
        ans.add(y)
        if count[x] == 0:
            ans.remove(x)

print(len(ans))
