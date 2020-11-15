import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

h, w = map(int, input().split())
MOD = 10 ** 9 + 7

s = [0] * h
dp = [0] * h
v_accum = [0] * h
h_accum = [0] * h
s_accum = [0] * h
for i in range(h):
    s[i] = input().strip()
    dp[i] = [0] * w
    v_accum[i] = [0] * w
    h_accum[i] = [0] * w
    s_accum[i] = [0] * w
dp[0][0] = 1
v_accum[0][0] = 1
h_accum[0][0] = 1
s_accum[0][0] = 1
# 縦1列目/横1列目はそれぞれ独立に確定する
# 縦1列目(O(h))
accum = 0
for i in range(1, h):
    if s[i][0] == '#':
        break
    else:
        accum = (accum + dp[i-1][0]) % MOD
        dp[i][0] = (dp[i][0] + accum) % MOD
        v_accum[i][0] = (v_accum[i][0] + dp[i][0]) % MOD
        h_accum[i][0] = (h_accum[i][0] + dp[i][0]) % MOD
        s_accum[i][0] = (s_accum[i][0] + dp[i][0]) % MOD
# 横1行目(O(w))
accum = 0
for j in range(1, w):
    if s[0][j] == '#':
        break
    else:
        accum = (accum + dp[0][j-1]) % MOD
        dp[0][j] = (dp[0][j] + accum) % MOD
        v_accum[0][j] = (v_accum[0][j] + dp[0][j]) % MOD
        h_accum[0][j] = (h_accum[0][j] + dp[0][j]) % MOD
        s_accum[0][j] = (s_accum[0][j] + dp[0][j]) % MOD
# 縦/横2行目以降(o(h*w))
for i in range(1, h):
    for j in range(1, w):
        if s[i][j] == '.':
            dp[i][j] = (v_accum[i-1][j] + h_accum[i][j-1] + s_accum[i-1][j-1]) % MOD
            v_accum[i][j] = (v_accum[i-1][j] + dp[i][j]) % MOD
            h_accum[i][j] = (h_accum[i][j-1] + dp[i][j]) % MOD
            s_accum[i][j] = (s_accum[i-1][j-1] + dp[i][j]) % MOD

print(dp[h-1][w-1] % MOD)
