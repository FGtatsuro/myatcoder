import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

m = int(input())
target = [0] * m
for i in range(m):
    target[i] = list(map(int, input().split()))
base = target[0]
vec = [0] * (m-1)
for i in range(m-1):
    x, y = target[i+1]
    vec[i] = [x-base[0], y-base[1]]
n = int(input())
pic = set()
for _ in range(n):
    pic.add(tuple(map(int, input().split())))

for p in pic:
    x, y = p
    ok = True
    # pをbaseとした場合に他の星が存在するか
    for v in vec:
        dx, dy = v
        nx, ny = x + dx, y + dy
        if (nx, ny) not in pic:
            ok = False
            break
    if ok:
        print(x - base[0], y - base[1])
        sys.exit(0)
assert False
