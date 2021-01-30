import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, s, d = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    if x < s and y > d:
        print('Yes')
        sys.exit(0)
print('No')
