import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

x, y = map(int, input().split())

if x == y:
    print(0)
    sys.exit(0)
if x == -y:
    print(1)
    sys.exit(0)

if x > 0 and y > 0:
    if y >= x:
        print(y - x)
        sys.exit(0)
    else:
        print(1 + abs(x - y) + 1)
        sys.exit(0)
if x < 0 and y < 0:
    if y > x:
        print(y - x)
        sys.exit(0)
    else:
        print(1 + abs(x - y) + 1)
        sys.exit(0)
if x > 0 and y < 0:
    print(abs(abs(x) - abs(y)) + 1)
    sys.exit(0)
if x < 0 and y > 0:
    print(abs(abs(x) - abs(y)) + 1)
    sys.exit(0)
if x == 0 and y >= 0:
    print(y)
    sys.exit(0)
if x == 0 and y < 0:
    print(abs(y) + 1)
    sys.exit(0)
if x >= 0 and y == 0:
    print(x + 1)
    sys.exit(0)
if x < 0 and y == 0:
    print(abs(x))
    sys.exit(0)
