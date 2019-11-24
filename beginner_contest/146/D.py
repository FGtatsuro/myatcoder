import sys
input = sys.stdin.readline

n = int(input())
edges = [tuple([int(i) for i in input().split()]) for _ in range(n - 1)]
graph = [0] + [[] for _ in range(n)]

for e in edges:
    graph[e[0]].append(e[1])
    graph[e[1]].append(e[0])

max_color_index = 1
def bfs(graph, dist, queue, parent_colors, color_map):
    global max_color_index
    while queue:
        parent = queue.pop(0)
        children = graph[parent]

        color_index = 1
        for child in children:
            if dist[child] != -1:
                continue

            # 親との辺の色と重なった場合、一個進める
            # それ以外は1から順に埋めていく
            if parent_colors[parent] == color_index:
                color_index += 1

            e = (min(child, parent), max(child, parent))
            if e not in color_map:
                color_map[e] = color_index

            parent_colors[child] = color_index
            color_index += 1

            dist[child] = dist[parent] + 1
            queue.append(child)

        # 実際に使ったindexより1つ進んでいる
        max_color_index = max(max_color_index, color_index - 1)

dist = [0] + [-1] * n
dist[1] = 0
queue = [1]
parent_color = [0] * (n + 1)
color_map = {}
bfs(graph, dist, queue, parent_color, color_map)

print(max_color_index)
for e in edges:
    print(color_map[e])
