import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

A, B = map(int, input().split())
S = input().strip()

import string

for v in S[:A]:
    if v not in string.digits:
        print('No')
        sys.exit(0)
if S[A] != '-':
    print('No')
    sys.exit(0)
for v in S[A+1:]:
    if v not in string.digits:
        print('No')
        sys.exit(0)
print('Yes')
