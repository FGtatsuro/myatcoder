import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))
diff = [0] * (m - 1)
for i in range(m - 1):
    diff[i] = x[i + 1] - x[i]
diff = sorted(diff)

if n >= m:
    print(0)
else:
    for _ in range(n - 1):
        diff.pop()
    print(sum(diff))
