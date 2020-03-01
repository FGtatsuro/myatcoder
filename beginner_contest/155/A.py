import sys
input = sys.stdin.readline

a, b, c = [int(i) for i in input().split()]

def cond():
    if a == b and a != c:
        return True
    if a == c and a != b:
        return True
    if b == c and a != b:
        return True
    return False

if cond():
    print('Yes')
else:
    print('No')
