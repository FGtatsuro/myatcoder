import sys
input = sys.stdin.readline

LOAD = '.'
WALL = '#'
NOT_REACHED = -1

h, w = [int(i) for i in input().split()]

s = [0] * h
for i in range(h):
    s[i] = input().strip()

def bfs(graph, queue, dist):
    _max = 0
    while queue:
        current = queue.pop(0)

        top = (current[0] - 1, current[1])
        bottom = (current[0] + 1, current[1])
        left = (current[0], current[1] - 1)
        right = (current[0], current[1] + 1)

        for target in (top, bottom, left, right):
            if (target[0] < 0) or (target[0] >= h) or (target[1] < 0) or (target[1] >= w):
                continue
            if dist[target] != NOT_REACHED:
                continue
            if graph[target[0]][target[1]] == LOAD:
                dist[target] = dist[current] + 1
                _max = max(dist[target], _max)
                queue.append(target)
    return _max

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == WALL:
            continue
        queue = [(i, j)]
        dist = {}
        for inner_i in range(h):
            for inner_j in range(w):
                dist[(inner_i, inner_j)] = NOT_REACHED
        dist[(i, j)] = 0
        ans = max(bfs(s, queue, dist), ans)

print(ans)
