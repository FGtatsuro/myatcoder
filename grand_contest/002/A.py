import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b = map(int, input().split())

if a > 0:
    print('Positive')
    sys.exit(0)
if a == 0:
    print('Zero')
    sys.exit(0)
if a < 0:
    if b >= 0:
        print('Zero')
        sys.exit(0)
    if b < 0:
        diff = (b - a) + 1
        if diff % 2 == 0:
            print('Positive')
        else:
            print('Negative')
