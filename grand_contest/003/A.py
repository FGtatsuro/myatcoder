import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()

if ('N' in s and 'S' not in s) or ('N' not in s and 'S' in s):
    print('No')
    sys.exit(0)
if ('W' in s and 'E' not in s) or ('W' not in s and 'E' in s):
    print('No')
    sys.exit(0)
print('Yes')
