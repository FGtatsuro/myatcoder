import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

h, w = map(int, input().split())
if h == 1 or w == 1:
    print(1)
    sys.exit(0)

# a/bの切り上げ: (a + b - 1)//b
print(((h * w) + 2 - 1) // 2)
