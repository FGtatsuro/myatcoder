import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
MOD = 10 ** 9 + 7

factorial = [0] * (n+1)
factorial[0] = 1
for i in range(1, n+1):
    factorial[i] = factorial[i-1] * i

prime_factors = []
target = factorial[n]
i = 2
while i ** 2 <= target:
    if target % i != 0:
        i += 1
        continue

    ext = 0
    while target % i == 0:
        ext += 1
        target //= i

    prime_factors.append((i, ext))
    i += 1

if target != 1:
    prime_factors.append((target, 1))

ans = 1
for pf in prime_factors:
    ans = (ans * (pf[1] + 1)) % MOD

print(ans)
