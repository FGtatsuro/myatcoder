import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
h = [0] + list(map(int, input().split()))
graph = [0] + [[] for _ in range(n)]
for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

ans = 0
for i in range(1, n+1):
    high = []
    if len(graph[i]) == 0:
        ans += 1
        continue
    for j in graph[i]:
        high.append(h[i] > h[j])
    if all(high):
        ans += 1
print(ans)
