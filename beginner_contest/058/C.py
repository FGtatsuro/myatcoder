import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import string
from collections import Counter

n = int(input())
ss = []
common_chars = set(string.ascii_lowercase)

for _ in range(n):
    m = Counter(input().strip())
    ss.append(m)
    common_chars = common_chars.intersection(m.keys())

ans = []
for c in sorted(list(common_chars)):
    tmp = 51
    for s in ss:
        tmp = min(tmp, s[c])
    ans.append(c * tmp)
print(''.join(ans))
