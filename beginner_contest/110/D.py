import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())

MOD = 10 ** 9 + 7
prime_factors = []
i = 2
while i ** 2 <= m:
    ext = 0
    while m % i == 0:
        ext += 1
        m //= i
    if ext:
        prime_factors.append((i, ext))
    i += 1
if m != 1:
    prime_factors.append((m, 1))

ans = 1
for pf, num in prime_factors:
    denominator = 1
    numerator = 1
    for i in range(num):
        denominator *= (i+1)
        numerator *= (num + (n-1)) - i
    ans = (ans * (numerator // denominator)) % MOD
print(ans)
