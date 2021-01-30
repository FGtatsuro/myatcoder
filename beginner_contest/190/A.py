import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, c = map(int, input().split())

if a > b:
    print('Takahashi')
elif a < b:
    print('Aoki')
elif a == b:
    if c == 0:
        print('Aoki')
    elif c == 1:
        print('Takahashi')
    else:
        assert False
else:
    assert False
