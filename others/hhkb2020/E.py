import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

MOD =  1000000007

h, w = map(int, input().split())
k = 0
graph = [0] * h
left = [0] * h
right = [0] * h
up = [0] * h
down = [0] * h
for i in range(h):
    graph[i] = input().strip()
    k += graph[i].count('.')
    left[i] = [0] * w
    right[i] = [0] * w
    up[i] = [0] * w
    down[i] = [0] * w

# FYI: https://atcoder.jp/contests/hhkb2020/submissions/17330875
# 左に自分を含めて何個あるか
for i in range(h):
    for j in range(w):
        if j == 0 and graph[i][j] == '.':
            left[i][j] = 1
        else:
            if graph[i][j] == '.':
                left[i][j] = left[i][j-1] + 1
            else:
                left[i][j] = 0

# 右に自分を含めて何個あるか
for i in range(h):
    for j in range(w - 1, -1, -1):
        if j == w-1 and graph[i][j] == '.':
            right[i][j] = 1
        else:
            if graph[i][j] == '.':
                right[i][j] = right[i][j+1] + 1
            else:
                right[i][j] = 0

# 上に自分を含めて何個あるか
for i in range(h):
    for j in range(w):
        if i == 0 and graph[i][j] == '.':
            up[i][j] = 1
        else:
            if graph[i][j] == '.':
                up[i][j] = up[i-1][j] + 1
            else:
                up[i][j] = 0

# 下に自分を含めて何個あるか
for i in range(h-1, -1, -1):
    for j in range(w):
        if i == h-1 and graph[i][j] == '.':
            down[i][j] = 1
        else:
            if graph[i][j] == '.':
                down[i][j] = down[i+1][j] + 1
            else:
                down[i][j] = 0

# 2の累乗のメモ方法
# 毎回累乗していてはTLE
dp_pow = [0] * (k + 1)
dp_pow[0] = 1
for i in range(1, k + 1):
    dp_pow[i] = (dp_pow[i-1] * 2) % MOD

ans = k * dp_pow[k]
for i in range(h):
    for j in range(w):
        if graph[i][j] == '.':
            ans = (ans - dp_pow[k - (left[i][j] + right[i][j] + up[i][j] + down[i][j] - 3)]) % MOD
print(ans % MOD)
