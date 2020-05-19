import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, a, b = map(int, input().split())
s = input().strip()

_pass = 0
_pass_foreign = 0
for i, v in enumerate(s):
    if _pass == a + b:
        print('No')
        continue
    if v == 'c':
        print('No')
    if v == 'a':
        print('Yes')
        _pass += 1
    if v == 'b':
        if _pass_foreign < b:
            print('Yes')
            _pass += 1
            _pass_foreign += 1
        else:
            print('No')
