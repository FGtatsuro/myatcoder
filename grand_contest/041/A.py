import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, a, b = map(int, input().split())
if abs(a - b) % 2 == 0:
    print(abs(a - b) // 2)
else:
    small, big = min(a, b), max(a, b)
    print(min(
        (small - 1) + 1 + ((big - (small - 1) - 1 - 1) // 2),
        (n - big) + 1 + ((n - (small + (n - big) + 1)) // 2)
    ))
