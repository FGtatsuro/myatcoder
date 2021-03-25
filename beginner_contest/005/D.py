import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
D = [0] * N
for i in range(N):
    D[i] = list(map(int, input().split()))

# S[i][j]: [0, i) * [0, j)のおいしさの総和
S = [[0] * (N+1) for _ in range(N+1)]
for i in range(N+1):
    S[i][0] = 0
    S[0][i] = 0
for i in range(N):
    for j in range(N):
        S[i+1][j+1] = S[i][j+1] + S[i+1][j] - S[i][j] + D[i][j]

# V[i]: 面積iでのおいしさの総和の最大値
V = [0] * (N**2+1)
for i1 in range(N+1):
    for i2 in range(i1, N+1):
        for j1 in range(N+1):
            for j2 in range(j1, N+1):
                v = S[i2][j2] - S[i1][j2] - S[i2][j1] + S[i1][j1]
                V[(i2-i1) * (j2-j1)] = max(V[(i2-i1) * (j2-j1)], v)
# V[i]: 面積i『以下』でのおいしさの総和の最大値に変換
for i in range(1, N**2+1):
    if V[i] < V[i-1]:
        V[i] = V[i-1]

Q = int(input())
for _ in range(Q):
    P = int(input())
    print(V[P])
