import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
A = [0] * N
for i in range(N):
    A[i] = list(map(int, input().split()))

ans = 0
for i in range(M):
    for j in range(i+1, M):
        tmp = 0
        for k in range(N):
            tmp += max(A[k][i], A[k][j])
        ans = max(ans, tmp)
print(ans)
