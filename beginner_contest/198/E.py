import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
C = list(map(int, input().split()))
for i, v in enumerate(C):
    C[i] = v-1
graph = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

ans = []
def dfs(graph, current, visit, color):
    visit.add(current)
    if color[C[current]] == 0:
        ans.append(current)

    color[C[current]] += 1

    for n in graph[current]:
        if n in visit:
            continue
        dfs(graph, n, visit, color)

    color[C[current]] -= 1

current = 0
visit = set()
color = [0] * (10 ** 5)
dfs(graph, current, visit, color)
for i in sorted(ans):
    print(i+1)
