a, b = [int(i) for i in input().split()]
small = min(a, b)
big = max(a, b)

import sys

if small == 1:
    print(1)
    sys.exit(0)

import math
import collections

# FYI: https://ja.wikipedia.org/wiki/%E8%A9%A6%E3%81%97%E5%89%B2%E3%82%8A%E6%B3%95
def prime_factorization(num, divisors=None):
    if num <= 1:
        assert False
    factors = []

    # divisorsを使い回せるようにする。
    #   - 二度生成した場合にかかる時間が許容できない場合
    #   - エラトステネスの篩などで素数テーブルを既に持っている場合
    if not divisors:
        divisors = [2] + [i for i in range(3, int(math.sqrt(num)) + 2) if i % 2 != 0]

    for d in divisors:
        # divisorsを引数で与えた場合のみ起こりうる
        if num < d:
            break
        while num % d == 0:
            factors.append(d)
            num //= d

    if num != 1:
        factors.append(num)
    return factors

divisors = [2] + [i for i in range(3, int(math.sqrt(big)) + 1) if i % 2 != 0]
small_factors = set(prime_factorization(small, divisors))
big_factors = set(prime_factorization(big, divisors))

print(len(small_factors.intersection(big_factors)) + 1)
