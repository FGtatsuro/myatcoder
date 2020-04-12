import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = input().strip()

def cond():
    return '7' in n

if cond():
    print('Yes')
else:
    print('No')
