import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

X = int(input())

print(100 - (X % 100))
