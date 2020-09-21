import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

graph = [[0] * 10 for _ in range(10)]
land = []
sea = []
for i in range(10):
    r = list(input().strip())
    for j in range(10):
        graph[i][j] = r[j]
        if graph[i][j] == 'x':
            land.append((i, j))
        else:
            sea.append((i, j))

def dfs(graph, queue, visit):
    while queue:
        current_h, current_w = queue.pop()
        visit[current_h][current_w] = 0

        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_h = current_h + dh
            next_w = current_w + dw

            if not (0 <= next_h < 10 and 0 <= next_w < 10):
                continue
            if visit[next_h][next_w] != -1:
                continue
            if graph[next_h][next_w] == 'x':
                continue
            queue.append((next_h, next_w))

for land_h, land_w in land:
    graph[land_h][land_w] = 'o'
    
    part = 0
    visit = [[-1] * 10 for _ in range(10)]
    for sea_h, sea_w in sea:
        if visit[sea_h][sea_w] != -1:
            continue
        part += 1
        queue = [(sea_h, sea_w)]
        dfs(graph, queue, visit)
    if part == 1:
        print('YES')
        sys.exit(0)

    graph[land_h][land_w] = 'x'
print('NO')
