import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

H, W, X, Y = map(int, input().split())
S = [0] * (H+1)
for i in range(H):
    S[i+1] = [0] + list(input().strip())

ans = 0

# X行/y列
ans += 1

# 1 - (X-1)行/Y列
for i in range(X-1, 0, -1):
    if S[i][Y] == '#':
        break
    ans += 1
    
# (X+1) - H行/Y列
for i in range(X+1, H+1):
    if S[i][Y] == '#':
        break
    ans += 1

# X行/1 - (Y-1)列
for i in range(Y-1, 0, -1):
    if S[X][i] == '#':
        break
    ans += 1

# X行/(Y+1) - W列
for i in range(Y+1, W+1):
    if S[X][i] == '#':
        break
    ans += 1

print(ans)
