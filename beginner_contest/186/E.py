import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

t = int(input())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcd_ext(a, b):
    if b == 0:
        return 1, 0, a
    else:
        s, t, d = gcd_ext(b, a % b)
        return t, s - (a // b) * t, d

def solve(n, s, k):
    m = n - s
    d = gcd(gcd(k, m), n)
    k, m, n = k // d, m // d, n // d
    if gcd(k, n) != 1:
        return -1
    inverse, _, _ = gcd_ext(k, n)
    # mod nの世界での値を返す
    return (inverse * m) % n

for _ in range(t):
    n, s, k = map(int, input().split())
    print(solve(n, s, k))
