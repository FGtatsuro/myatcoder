import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, c = sorted(map(int, input().split()))

if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    print(0)
else:
    print(a * b)
