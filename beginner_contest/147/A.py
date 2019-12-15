import sys
input = sys.stdin.readline

a1, a2, a3 = [int(i) for i in input().split()]
if a1 + a2 + a3 >= 22:
    print('bust')
    sys.exit(0)
if a1 + a2 + a3 <= 21:
    print('win')
    sys.exit(0)
