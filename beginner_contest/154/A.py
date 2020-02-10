import sys
input = sys.stdin.readline

s, t = input().strip().split()
a, b = [int(i) for i in input().split()]
u = input().strip()

if s == u:
    a -= 1
else:
    b -= 1
print(a, b)
