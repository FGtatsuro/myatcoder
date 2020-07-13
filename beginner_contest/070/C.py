import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a // gcd(a, b)) * b

ans = 1
for _ in range(n):
    ans = lcm(ans, int(input()))
print(ans)
