import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

k = int(input())
a, b = map(int, input().split())

def cond(k, a, b):
    multi = 1
    total = k
    while total <= b:
        if total >= a:
            return True
        multi += 1
        total = k * multi
    return False

if cond(k, a, b):
    print('OK')
else:
    print('NG')
