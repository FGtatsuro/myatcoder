import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
D = 0
C = [0] * N
a = []
b = []
for i in range(N):
    A, B = map(int, input().split())
    D += (B - A)
    C[i] = (A, B)
    a.append(A)
    b.append(B)

a = sorted(a)
b = sorted(b)
s = a[N // 2]
e = b[N // 2]
for A, B in C:
    D += abs(A - s)
    D += abs(B - e)

print(D)
