import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

k = int(input())
s = input().strip()

if len(s) <= k:
    print(s)
else:
    print(s[:k] + '...')
