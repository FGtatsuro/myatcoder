import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b = map(int, input().split())
c, d = map(int, input().split())
print(max(a, b) - min(c, d))
