import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, w = map(int, input().split())

print(n // w)
