import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
a = [0] * n
for i in range(n):
    a[i] = input().strip()
b = [0] * m
for i in range(m):
    b[i] = input().strip()
for i in range(n - m + 1):
    for j in range(n - m + 1):
        include = True
        for k in range(m):
            for l in range(m):
                if a[i+k][j+l] != b[k][l]:
                    include = False
                    break
            if not include:
                break
        if include:
            print('Yes')
            sys.exit(0)
print('No')
