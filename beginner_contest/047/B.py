import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

w, h, n = map(int, input().split())
a1, a2, a3, a4 = [], [], [], []
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        a1.append((x, y))
    elif a == 2:
        a2.append((x, y))
    elif a == 3:
        a3.append((x, y))
    elif a == 4:
        a4.append((x, y))
    else:
        assert False

a1 = sorted(a1, key=lambda v: v[0])
a2 = sorted(a2, key=lambda v: v[0])
a3 = sorted(a3, key=lambda v: v[1])
a4 = sorted(a4, key=lambda v: v[1])

if a1 and a2:
    l1 = a2[0][0] - a1[-1][0]
elif not a1 and not a2:
    l1 = w
elif not a1:
    l1 = a2[0][0]
elif not a2:
    l1 = w - a1[-1][0]
else:
    assert False

if a3 and a4:
    l2 = a4[0][1] - a3[-1][1]
elif not a3 and not a4:
    l2 = h
elif not a3:
    l2 = a4[0][1]
elif not a4:
    l2 = h - a3[-1][1]
else:
    assert False

if l1 <= 0 or l2 <= 0:
    print(0)
else:
    print(l1 * l2)
