n, m = [int(i) for i in input().split()]
edges = [[int(i) for i in input().split()] for _ in range(m)]
adjacency = [0] + [[] for _ in range(n)]

for e in edges:
    adjacency[e[0]].append(e[1])
    adjacency[e[1]].append(e[0])

print(adjacency)
