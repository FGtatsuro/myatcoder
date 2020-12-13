import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a1, a2, a3, a4 = map(int, input().split())
print(min(a1, a2, a3, a4))
