import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a = input().strip()

import string

if a in string.ascii_uppercase:
    print('A')
else:
    print('a')
