import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, a, b, c, d = map(int, input().split())
s = '0' + input().strip()

if s[a:c+1].find('##') != -1 or s[b:d+1].find('##') != -1:
    print('No')
    sys.exit(0)
if c < d:
    print('Yes')
else:
    if s[b-1:d+1+1].find('...') != -1:
        print('Yes')
    else:
        print('No')
