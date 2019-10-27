n = int(input())

import sys
import math

_max = int(math.sqrt(n) + 1)

for i in range(_max, 1, -1):
    if n % i == 0:
        a = n // i
        b = i
        print((a-1) + (b-1))
        sys.exit(0)

print(n - 1)
