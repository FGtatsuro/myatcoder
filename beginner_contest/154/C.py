import sys
input = sys.stdin.readline

n = int(input())
a = [int(i) for i in input().split()]
b = set(a)

def cond():
    return len(a) == len(b)

if cond():
    print('YES')
else:
    print('NO')
