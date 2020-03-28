import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()

def cond():
    return s[2] == s[3] and s[4] == s[5]

if cond():
    print('Yes')
else:
    print('No')
