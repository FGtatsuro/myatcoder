import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

k, a, b = map(int, input().split())

if b - a <= 2 or k + 1 <= a:
    print(k + 1)
else:
    count = k - (a - 1)
    print(a + (b - a) * (count // 2) + (count %2))
