import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s, w = map(int, input().split())

def cond():
    return w >= s

if cond():
    print('unsafe')
else:
    print('safe')
