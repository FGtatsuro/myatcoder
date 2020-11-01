import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

h, w = map(int, input().split())

graph = [0] * h
dp = [0] * h
for i in range(h):
    graph[i] = input().strip()
    dp[i] = [0] * w
if graph[0][0] == '#':
    dp[0][0] = 1

for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            continue
        if i == 0:
            dp[i][j] = dp[i][j-1]
            if graph[i][j-1] == '.' and graph[i][j] == '#':
                dp[i][j] += 1
        elif j == 0:
            dp[i][j] = dp[i-1][j]
            if graph[i-1][j] == '.' and graph[i][j] == '#':
                dp[i][j] += 1
        else:
            left = dp[i][j-1]
            if graph[i][j-1] == '.' and graph[i][j] == '#':
                left += 1
            up = dp[i-1][j]
            if graph[i-1][j] == '.' and graph[i][j] == '#':
                up += 1
            dp[i][j] = min(left, up)

print(dp[h-1][w-1])
