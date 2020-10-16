import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()

import string

if s == ''.join(reversed(string.ascii_lowercase)):
    print(-1)
    sys.exit(0)

available = set(string.ascii_lowercase)
available = sorted(list(available - set(s)))
if available:
    print(s + available[0])
else:
    s = list(s)
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i+1]:
            for v in sorted(s[i+1:]):
                if s[i] < v:
                    s[i] = v
                    break
            print(''.join(s[:i+1]))
            break
