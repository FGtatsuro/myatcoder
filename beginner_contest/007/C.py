import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

r, c = list(map(int, input().split()))
sx, sy = list(map(int, input().split()))
gx, gy = list(map(int, input().split()))
graph = [0] + [0] * r
for i in range(r):
    graph[i + 1] = '0' + input().strip()

def bfs(graph, queue, dist):
    while queue:
        current = queue.pop(0)

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            _nextx, _nexty = current[0] + dx, current[1] + dy
            if _nextx < 1 or _nextx > r:
                continue
            if _nexty < 1 or _nexty > c:
                continue
            if graph[_nextx][_nexty] == '#':
                continue
            if dist[_nextx][_nexty] != -1:
                continue
            dist[_nextx][_nexty] = dist[current[0]][current[1]] + 1
            queue.append((_nextx, _nexty))

queue = [(sx, sy)]
dist = [0] + [0] * r
for i in range(r):
    dist[i + 1] = [0] + [-1] * c
dist[sx][sy] = 0
bfs(graph, queue, dist)
print(dist[gx][gy])
