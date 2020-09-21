n, m = [int(i) for i in input().split()]
edges = [tuple([int(i) for i in input().split()]) for _ in range(m)]
graph = [[] for _ in range(n)]

import heapq

for e in edges:
    heapq.heappush(graph[e[0]], e[1])
    heapq.heappush(graph[e[1]], e[0])

def dfs_iterative(graph, seen, start):
    seen.add(start)
    _next = []
    _next.append(start)

    while _next:
        current = _next.pop()
        for _ in range(len(graph[current])):
            child = heapq.heappop(graph[current])
            if child in seen:
                continue
            _next.append(child)
            seen.add(child)

def dfs_recursive(graph, seen, start):
    seen.add(start)

    for _ in range(len(graph[start])):
        c = heapq.heappop(graph[start])
        if c in seen:
            continue
        dfs_recursive(graph, seen, c)

if __name__ == '__main__':
    seen = set()
    dfs = dfs_recursive

    count = 0
    for i in range(n):
        if i in seen:
            continue
        dfs(graph, seen, i)
        count += 1
    print(count)
