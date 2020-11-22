import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

if (r1, c1) == (r2, c2):
    print(0)
    sys.exit(0)
if ((r1 + c1) == (r2 + c2)) or ((r1 - c1) == (r2 - c2)) or ((abs(r1 - r2) + abs(c1 - c2)) <= 3):
    print(1)
    sys.exit(0)

for i in range(-2, 3):
    for j in range(-2, 3):
        if (i, j) == (0, 0):
            continue
        new_r2, new_c2 = r2 + i, c2 + j
        if ((r1 + c1) == (new_r2 + new_c2)) or ((r1 - c1) == (new_r2 - new_c2)):
            print(2)
            sys.exit(0)
for i, j in ((-3, 0), (3, 0), (0, -3), (0, 3)):
    new_r2, new_c2 = r2 + i, c2 + j
    if ((r1 + c1) == (new_r2 + new_c2)) or ((r1 - c1) == (new_r2 - new_c2)):
        print(2)
        sys.exit(0)

if (abs(r1 - r2) + abs(c1 - c2)) % 2 == 0:
    print(2)
    sys.exit(0)
if (abs(r1 - r2) + abs(c1 - c2)) % 2 == 1:
    print(3)
    sys.exit(0)
