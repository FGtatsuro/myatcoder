import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = []
for v in input().strip():
    if v != 'B':
        s.append(v)
    else:
        if s:
            s.pop()
print(''.join(s))
