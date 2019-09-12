n, m = [int(i) for i in input().split()]
edges = [[int(i) for i in input().split()] for _ in range(m)]
adjacency = [0] + [[] for _ in range(n)]

from collections import namedtuple
Edge = namedtuple('Edge', ('to', 'weight'))

for e in edges:
    adjacency[e[0]].append(Edge(to=e[1], weight=e[2]))
    adjacency[e[1]].append(Edge(to=e[0], weight=e[2]))

print(adjacency)
