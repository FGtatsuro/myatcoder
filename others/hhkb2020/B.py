import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

h, w = map(int, input().split())
graph = [0] * h
for i in range(h):
    graph[i] = input().strip()

ans = 0
for i in range(h):
    for j in range(w - 1):
        if graph[i][j] == '#':
            continue
        if graph[i][j+1] == '.':
            ans += 1

for i in range(h-1):
    for j in range(w):
        if graph[i][j] == '#':
            continue
        if graph[i+1][j] == '.':
            ans += 1
print(ans)
