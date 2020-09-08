import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import string

s = set(input().strip())
alpha = set(string.ascii_lowercase)
s = sorted(list(alpha - s))
if s:
    print(s[0])
else:
    print('None')
