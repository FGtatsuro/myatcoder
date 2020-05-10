import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

h, w = map(int, input().split())
graph = [0] * h
for i in range(h):
    graph[i] = input().strip()
    if 's' in graph[i]:
        sy, sx = i, graph[i].index('s')
    if 'g' in graph[i]:
        gy, gx = i, graph[i].index('g')

def dfs(graph, queue, seen):
    while queue:
        y, x = queue.pop()
        seen.add((y, x))

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = y + dy, x + dx
            if (not (0 <= ny < h)) or (not (0 <= nx < w)):
                continue
            if graph[ny][nx] == '#':
                continue
            if (ny, nx) in seen:
                continue
            queue.append((ny, nx))

queue = [(sy, sx)]
seen = set()
dfs(graph, queue, seen)
if (gy, gx) in seen:
    print('Yes')
else:
    print('No')
