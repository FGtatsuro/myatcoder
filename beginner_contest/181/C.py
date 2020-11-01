import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
point = [0] * n
for i in range(n):
    x, y = map(int, input().split())
    point[i] = (x, y)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or k == i:
                continue
            x1, y1 = point[i]
            x2, y2 = point[j]
            x3, y3 = point[k]
            if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                print('Yes')
                sys.exit(0)
print('No')
