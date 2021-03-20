import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
INF = 10 ** 15
A = 0
B = -INF
C = INF
for i in range(N):
    a, t = map(int, input().split())
    if t == 1:
        A += a
        B += a
        C += a
    elif t == 2:
        if B < a:
            B = a
        if C < a:
            C = a
    elif t == 3:
        if B > a:
            B = a
        if C > a:
            C = a
    else:
        assert False
Q = int(input())
for x in list(map(int, input().split())):
    print(min(C, max(B, x + A)))
