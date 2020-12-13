import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m, t = map(int, input().split())

current = 0
capacity = n
for _ in range(m):
    a, b = map(int, input().split())
    capacity -= (a - current)
    if capacity <= 0:
        print('No')
        sys.exit(0)
    capacity += (b - a)
    capacity = min(capacity, n)
    current = b

capacity -= (t - current)
if capacity <= 0:
    print('No')
else:
    print('Yes')
