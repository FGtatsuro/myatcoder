import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()
t = input().strip()

if s == 'Y':
    print(t.upper())
elif s == 'N':
    print(t)
else:
    assert False
