n, m = [int(i) for i in input().split()]
edges = [[int(i) for i in input().split()] for _ in range(m)]

import heapq

def build_graph(size, edges):
    graph = [[] for _ in range(size)]
    for e in edges:
        heapq.heappush(graph[e[0]], e[1])
        heapq.heappush(graph[e[1]], e[0])
    return graph

def dfs_iterative(graph, seen, start):
    candidate = []

    seen[start] = True
    candidate.append(start)

    while candidate:
        current = candidate.pop()
        print(current)
        for c in graph[current]:
            if seen[c]:
                continue
            seen[c] = True
            candidate.append(c)

def dfs_recursive(graph, seen, current):
    seen[current] = True
    print(current)

    for _ in range(len(graph[current])):
        c = heapq.heappop(graph[current])
        if seen[c]:
            continue
        dfs_recursive(graph, seen, c)

def reachable(graph, seen, source, dest, dfs):
    dfs_recursive(graph, seen, source)
    if seen[dest]:
        print('Yes')
    else:
        print('No')

graph = build_graph(n, edges)
seen = [False] * len(graph)
#dfs_iterative(graph, seen, 0)
#dfs_recursive(graph, seen, 0)
reachable(graph, seen, 0, 14, dfs_recursive)
