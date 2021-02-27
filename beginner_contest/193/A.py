import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

A, B = map(int, input().split())

print(((A - B) / A) * 100)
