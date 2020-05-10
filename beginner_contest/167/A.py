import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()
t = input().strip()

if s == t[:-1] and (len(s) + 1 == len(t)):
    print('Yes')
else:
    print('No')

