import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = [int(i) for i in input().strip()]
o = list()
n = len(s)

while s:
    v = s.pop()
    if len(o) == 0:
        o.append(v)
    else:
        if v + o[-1] == 1:
            o.pop()
        else:
            o.append(v)
print(n - len(o))
