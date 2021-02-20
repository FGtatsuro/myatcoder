import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

A, B, C = map(int, input().split())
K = int(input())

for i in range(K + 1):
    for j in range(K + 1 - i):
        k = K - i - j
        a = A * (2 ** i)
        b = B * (2 ** j)
        c = C * (2 ** k)
        if a < b < c:
            print('Yes')
            sys.exit(0)
print('No')
