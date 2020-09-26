import sys
n = int(sys.stdin.readline())
s = [''.join(sorted(sys.stdin.readline().strip())) for _ in range(n)]

import collections
c = collections.Counter(s)

import math
def combination(v):
    return int(math.factorial(v) / (math.factorial(v - 2) * math.factorial(2)))
print(sum(combination(v) for v in c.values() if v != 1))
