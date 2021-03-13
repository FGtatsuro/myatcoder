import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

M, H = map(int, input().split())

if H % M == 0:
    print('Yes')
else:
    print('No')
