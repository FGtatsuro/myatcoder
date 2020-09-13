import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

x = int(input())

def prime_factorize(n):
    prime_factors = {}
    i = 2
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

ans = 1
for i in range(2, x + 1):
    prime_factors = prime_factorize(i)
    exps = set(prime_factors.values())
    if len(exps) == 1 and exps != {1}:
        ans = i
print(ans)
