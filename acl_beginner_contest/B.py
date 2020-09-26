import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, c, d = map(int, input().split())
if a <= d and c <= b:
    print('Yes')
else:
    print('No')
