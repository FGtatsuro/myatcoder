import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())

ans = 0
for i in range(N // 4 + 1):
    for j in range(N // 7 + 1):
        if 4 * i + j * 7 == N:
            print('Yes')
            sys.exit(0)
print('No')
