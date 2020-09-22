import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

c = []
for i in range(3):
    c.append(list(map(int, input().split())))

for a1 in range(0, 101):
    b1 = c[0][0] - a1
    b2 = c[0][1] - a1
    b3 = c[0][2] - a1
    for a2 in range(0, 101):
        if not (b1 == (c[1][0] - a2) and b2 == (c[1][1] - a2) and b3 == (c[1][2] - a2)):
            continue
        for a3 in range(0, 101):
            if (b1 == (c[2][0] - a3) and b2 == (c[2][1] - a3) and b3 == (c[2][2] - a3)):
                print('Yes')
                sys.exit(0)
print('No')
