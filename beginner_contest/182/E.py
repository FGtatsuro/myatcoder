import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

h, w, n, m = map(int, input().split())

left = [0] + [0] * h
for i in range(h):
    left[i+1] = [0] + [0] * w
right = [0] + [0] * h
for i in range(h):
    right[i+1] = [0] + [0] * w
up = [0] + [0] * h
for i in range(h):
    up[i+1] = [0] + [0] * w
down = [0] + [0] * h
for i in range(h):
    down[i+1] = [0] + [0] * w

for _ in range(n):
    a, b = map(int, input().split())
    left[a][b] = 1
    right[a][b] = 1
    up[a][b] = 1
    down[a][b] = 1
for _ in range(m):
    c, d = map(int, input().split())
    left[c][d] = -1
    right[c][d] = -1
    up[c][d] = -1
    down[c][d] = -1

for i in range(1, h+1):
    for j in range(1, w):
        if left[i][j] <= 0:
            continue
        elif left[i][j+1] != -1:
            left[i][j+1] = 1
for i in range(1, h+1):
    for j in range(w, 1, -1):
        if right[i][j] <= 0:
            continue
        elif right[i][j-1] != -1:
            right[i][j-1] = 1
for j in range(1, w+1):
    for i in range(1, h):
        if up[i][j] <= 0:
            continue
        elif up[i+1][j] != -1:
            up[i+1][j] = 1
for j in range(1, w+1):
    for i in range(h, 1, -1):
        if down[i][j] <= 0:
            continue
        elif down[i-1][j] != -1:
            down[i-1][j] = 1

count = 0
for i in range(h):
    for j in range(w):
        if left[i+1][j+1] + right[i+1][j+1] + up[i+1][j+1] + down[i+1][j+1] > 0:
            count += 1
print(count)
