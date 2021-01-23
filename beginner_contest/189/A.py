import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

i = set(input().strip())
if len(i) == 1:
    print('Won')
else:
    print('Lost')
