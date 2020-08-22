import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

if n % 9 == 0:
    print('Yes')
else:
    print('No')
