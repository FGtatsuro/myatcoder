import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

if n % 2 == 0:
    print('White')
else:
    print('Black')
