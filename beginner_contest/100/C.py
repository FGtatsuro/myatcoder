import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

def factorize(n):
    i = 2
    prime_factors = {}
    while i ** 2 <= n:
        exp = 0
        while n % i == 0:
            exp += 1
            n //= i
        if exp:
            prime_factors[i] = exp
        i += 1
    if n != 1:
        prime_factors[n] = 1
    return prime_factors

ans = 0
for v in a:
    prime_factors = factorize(v)
    if 2 in prime_factors:
        ans += prime_factors[2]
print(ans)
