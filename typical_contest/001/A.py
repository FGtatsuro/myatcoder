import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

h, w = [int(i) for i in input().split()]
c = [tuple(input()) for _ in range(h)]

start, goal = None, None
for i in range(h):
    if start and goal:
        break
    for j in range(w):
        if start and goal:
            break
        if c[i][j] == 's':
            start = (i, j)
            continue
        if c[i][j] == 'g':
            goal = (i, j)
            continue

def dfs_recursive(c, seen, current):
    seen.add(current)

    _next = []
    next_h, next_w = current[0] - 1, current[1]
    if next_h >= 0 and c[next_h][next_w] != '#':
        _next.append((next_h, next_w))

    next_h, next_w = current[0] + 1, current[1]
    if next_h < h and c[next_h][next_w] != '#':
        _next.append((next_h, next_w))

    next_h, next_w = current[0], current[1] - 1
    if next_w >= 0 and c[next_h][next_w] != '#':
        _next.append((next_h, next_w))

    next_h, next_w = current[0], current[1] + 1
    if next_w < w and c[next_h][next_w] != '#':
        _next.append((next_h, next_w))

    for n in _next:
        if n in seen:
            continue
        dfs_recursive(c, seen, n)

def dfs_iterative(c, seen, start):
    _next = []
    seen.add(start)
    _next.append(start)

    while _next:
        current = _next.pop()

        next_h, next_w = current[0] - 1, current[1]
        if next_h >= 0 and c[next_h][next_w] != '#' and (next_h, next_w) not in seen:
            _next.append((next_h, next_w))
            seen.add((next_h, next_w))

        next_h, next_w = current[0] + 1, current[1]
        if next_h < h and c[next_h][next_w] != '#' and (next_h, next_w) not in seen:
            _next.append((next_h, next_w))
            seen.add((next_h, next_w))

        next_h, next_w = current[0], current[1] - 1
        if next_w >= 0 and c[next_h][next_w] != '#' and (next_h, next_w) not in seen:
            _next.append((next_h, next_w))
            seen.add((next_h, next_w))

        next_h, next_w = current[0], current[1] + 1
        if next_w < w and c[next_h][next_w] != '#' and (next_h, next_w) not in seen:
            _next.append((next_h, next_w))
            seen.add((next_h, next_w))


def reachable(c, seen, start, goal, dfs):
    dfs(c, seen, start)
    if goal in seen:
        return 'Yes'
    else:
        return 'No'

seen = set()
#print(reachable(c, seen, start, goal, dfs_recursive))
print(reachable(c, seen, start, goal, dfs_iterative))
