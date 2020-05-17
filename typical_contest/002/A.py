import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
graph = [0] + [0] * r
for i in range(r):
    graph[i+1] = '0' + input().strip()

from collections import deque

def bfs(graph, queue, dist):
    while queue:
        y, x = queue.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if not ((1 <= ny <= r) and (1 <= nx <= c)):
                continue
            if graph[ny][nx] == '#':
                continue
            if dist[ny][nx] != -1:
                continue
            dist[ny][nx] = dist[y][x] + 1
            queue.append((ny, nx))

queue = deque([(sy, sx)])
dist = [-1] + [-1] * r
for i in range(r):
    dist[i+1] = [-1] + [-1] * c
dist[sy][sx] = 0
bfs(graph, queue, dist)
print(dist[gy][gx])
