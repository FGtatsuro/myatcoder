n, m = [int(i) for i in input().split()]
edges = [[int(i) for i in input().split()] for _ in range(m)]

graph = [[] for _ in range(n)]
for e in edges:
    graph[e[0]].append(e[1])
    graph[e[1]].append(e[0])

BLACK = 1
WHITE = 0
UNKNOWN = -1
colors = [UNKNOWN] * n

def bipartite_dfs(graph, colors, current_point, current_color=BLACK):
    next_color = 1 - current_color

    for next_point in graph[current_point]:
        if colors[next_point] == UNKNOWN:
            colors[next_point] = next_color
            if not bipartite_dfs(graph, colors, next_point, next_color):
                return False
        elif colors[next_point] != next_color:
            return False
    return True

# FYI: https://qiita.com/drken/items/a803d4fc4a727e02f7ba#4-3-%E4%BA%8C%E9%83%A8%E3%82%B0%E3%83%A9%E3%83%95%E5%88%A4%E5%AE%9A
# 連結グラフでない場合をカバーする
is_bipartite = True
for s in range(1, n):
    if colors[s] != UNKNOWN:
        continue
    if not bipartite_dfs(graph, colors, s):
        is_bipartite = False
        break

if is_bipartite:
    print('Yes')
else:
    print('No')
