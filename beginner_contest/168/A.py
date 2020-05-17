import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = input().strip()
n = int(n[-1])

if n in (2, 4, 5, 7, 9):
    print('hon')

if n in (0, 1, 6, 8):
    print('pon')

if n == 3:
    print('bon')
