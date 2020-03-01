import sys
input = sys.stdin.readline

n = int(input())
a = [int(i) for i in input().split()]

def cond():
    for v in a:
        if v % 2 == 0 and (v % 3 != 0 and v % 5 != 0):
            return False
    return True

if cond():
    print('APPROVED')
else:
    print('DENIED')
