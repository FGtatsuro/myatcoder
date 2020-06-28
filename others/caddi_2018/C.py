import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, p = map(int, input().split())

prime_factors = []
i = 2
while i ** 2 <= p:
    ext = 0
    while p % i == 0:
        ext += 1
        p //= i
    if ext:
        prime_factors.append((i, ext))
    i += 1
if p != 1:
    prime_factors.append((p, 1))

ans = 1
for pf, num in prime_factors:
    ans *= (pf ** (num // n))
print(ans)
