import sys
input = sys.stdin.readline

n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

num = [0] * n

count = None
for i, v in enumerate(a):
    num[i] = v // 2

    _v = num[i]
    _count = 0
    while True:
        if _v % 2 == 0:
            _v = _v // 2
            _count += 1
        else:
            break
    if count is None:
        count = _count
    elif count != _count:
        print(0)
        sys.exit(0)

import fractions
import functools
# FYI: https://note.nkmk.me/python-gcd-lcm/
def lcm(numbers):
    return functools.reduce(lambda x, y: (x * y) // fractions.gcd(x, y), numbers, 1)

point = lcm(num)
print(int((m // point) / 2 + 0.5))
