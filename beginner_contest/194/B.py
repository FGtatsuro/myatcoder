import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
AB = [0] * N
for i in range(N):
    A, B = map(int, input().split())
    AB[i] = (A, B)

INF = 10 ** 15
ans = INF
for i in range(N):
    for j in range(N):
        if i == j:
            ans = min(ans, AB[i][0] + AB[j][1])
        else:
            ans = min(ans, max(AB[i][0], AB[j][1]))
print(ans)
