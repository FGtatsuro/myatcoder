import sys
a, b, c = [int(i) for i in sys.stdin.readline().split()]
r = c - (a - b)
if r <= 0:
    print(0)
else:
    print(r)
