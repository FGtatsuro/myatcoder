import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())

graph = [0] + [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, queue, color):
    is_bigraph = True
    while queue:
        current = queue.pop()

        for _next in graph[current]:
            if color[_next] != -1:
                if color[_next] == color[current]:
                    is_bigraph = False
            else:
                color[_next] = 1 - color[current]
                queue.append(_next)
    return is_bigraph

queue = [1]
color = [-1] + [-1] * n
color[1] = 0

if dfs(graph, queue, color):
    print(color.count(0) * color.count(1) - m)
else:
    print((n * (n - 1)) // 2 - m)
