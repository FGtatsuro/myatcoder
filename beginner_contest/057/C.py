import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())

def digit(num):
    ans = 0
    while num:
        num //= 10
        ans += 1
    return ans

INF = 10 ** 15
ans = INF
A = 1
while A ** 2 <= N:
    if N % A == 0:
        B = N // A
        ans = min(ans, digit(B))
    A += 1
print(ans)
