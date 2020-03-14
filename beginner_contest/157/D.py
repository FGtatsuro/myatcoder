import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m, k = input().strip().split()
n, m, k = int(n), int(m), int(k)
friends = [0] + [[] for _ in range(n)]
blocks = [0] + [[] for _ in range(n)]

for _ in range(m):
    p1, p2 = input().strip().split()
    p1, p2 = int(p1), int(p2)
    friends[p1].append(p2)
    friends[p2].append(p1)
for _ in range(k):
    p1, p2 = input().strip().split()
    p1, p2 = int(p1), int(p2)
    blocks[p1].append(p2)
    blocks[p2].append(p1)

connected_num = 0
def dfs(graph, current, seen, connected_id):
    global connected_num
    seen[current] = connected_id
    connected_num += 1

    children = graph[current]
    for c in children:
        if seen[c] != -1:
            continue
        dfs(graph, c, seen, connected_id)

seen = [-1] * (n + 1)
connected_id = 0
connected = []
for i in range(1, n + 1):
    if seen[i] != -1:
        continue
    dfs(friends, i, seen, connected_id)
    connected.append(connected_num)
    connected_num = 0
    connected_id += 1

ans = []
for i in range(1, n + 1):
    i_connected_id = seen[i]
    exclude = 0
    for f in friends[i]:
        f_connected_id = seen[f]
        if i_connected_id == f_connected_id:
            exclude += 1
    for b in blocks[i]:
        b_connected_id = seen[b]
        if i_connected_id == b_connected_id:
            exclude += 1
    ans.append(str(connected[i_connected_id] - exclude - 1))

print(' '.join(ans))
