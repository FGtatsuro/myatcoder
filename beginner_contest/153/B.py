import sys
input = sys.stdin.readline

h, n = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

if (h - sum(a)) <= 0:
    print('Yes')
else:
    print('No')
