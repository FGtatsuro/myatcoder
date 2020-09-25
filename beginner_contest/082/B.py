import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = ''.join(sorted(input().strip()))
t = ''.join(sorted(input().strip(), reverse=True))

if s < t:
    print('Yes')
else:
    print('No')
