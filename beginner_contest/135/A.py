import sys
a, b = [int(i) for i in sys.stdin.readline().split()]
n = (a + b) / 2
if n.is_integer():
    print(int(n))
else:
    print('IMPOSSIBLE')
