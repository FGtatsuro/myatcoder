import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m, k = map(int, input().split())

for i in range(0, n + 1):
    for j in range(0, m + 1):
        tmp = 0
        tmp += (i * m)
        tmp += (j * n)
        tmp -= (i * j) * 2
        if tmp == k:
            print('Yes')
            sys.exit(0)
print('No')
