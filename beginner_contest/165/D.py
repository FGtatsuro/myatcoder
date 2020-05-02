import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, n = map(int, input().split())
if b == 1:
    print(0)
    sys.exit(0)

import math
ans = n
if b - 1 <= n:
    ans = b - 1
print(math.floor((a * ans)/(b)) - (a * math.floor((ans)/b)))
