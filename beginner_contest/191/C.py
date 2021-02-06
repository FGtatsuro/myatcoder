import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

h, w = map(int, input().split())
graph = [0] * h
for i in range(h):
    graph[i] = input().strip()

ans = 0
for i in range(1, h):
    for j in range(1, w):
        count = 0
        if graph[i-1][j-1] == '#':
            count += 1
        if graph[i-1][j] == '#':
            count += 1
        if graph[i][j-1] == '#':
            count += 1
        if graph[i][j] == '#':
            count += 1
        if count == 1 or count == 3:
            ans += 1
print(ans)
