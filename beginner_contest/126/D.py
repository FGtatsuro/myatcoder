import sys
sys.setrecursionlimit(10**6)

n = int(input())
edges = [[int(i) for i in input().split()] for _ in range(n - 1)]

BLACK = 1
WHITE = 0
UNKNOWN = -1

# なくても大丈夫
import sys
if n == 1:
    print(BLACK)
    sys.exit(0)

colors = [UNKNOWN] * (n + 1)

graph = [[] for _ in range(n + 1)]
for e in edges:
    graph[e[0]].append((e[1], e[2]))
    graph[e[1]].append((e[0], e[2]))

def dfs(graph, colors, current_point, current_color):
    colors[current_point] = current_color

    for next_point_info in graph[current_point]:
        if colors[next_point_info[0]] != UNKNOWN:
            continue
        if (next_point_info[1] % 2 == 0):
            next_color = current_color
        else:
            next_color = 1 - current_color
        dfs(graph, colors, next_point_info[0], next_color)

dfs(graph, colors, 1, BLACK)
for c in colors[1:]:
    print(c)
