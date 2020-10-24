import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
ab = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    ab[i] = (a, b)
ab = sorted(ab)

for a, b in ab:
    k -= b
    if k <= 0:
        print(a)
        sys.exit(0)
