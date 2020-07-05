import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

r = n % 1000
if r == 0:
    print(0)
else:
    print(1000 - r)
