import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

if n == 1:
    print(0)
    sys.exit(0)

import math

prime_factorization = []

copy_n = n
for i in range(2, math.ceil(math.sqrt(n)) + 1):
    if copy_n % i != 0:
        continue
    else:
        ex = 0
        while copy_n % i == 0:
            ex += 1
            copy_n = copy_n // i
        prime_factorization.append((i, ex))
if copy_n != 1:
    prime_factorization.append((copy_n, 1))

ans = 0
memo = dict()
for p in prime_factorization:
    if p[1] in memo:
        ans += memo[p[1]]
        continue
    count = 0
    total = 1
    while total <= p[1]:
        count += 1
        memo[total] = count
        total = total + (count + 1)
    memo[p[1]] = count
    ans += count
print(ans)
