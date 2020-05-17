import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m, p = map(int, input().split())

def mpow(base, n, m):
    ans = 1
    while n:
        if n & 1:
            ans = (ans * base) % m
        base = (base ** 2) % m
        n >>= 1
    return ans

print(mpow(n, p, m) % m)
print(pow(n, p, m))
