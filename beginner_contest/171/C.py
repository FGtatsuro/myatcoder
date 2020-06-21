import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

import string
from collections import deque

name_table = string.ascii_lowercase
ans = deque()


while n > 0:
    n -= 1
    m = n % 26
    ans.appendleft(name_table[m])
    n //= 26

print(''.join(ans))
