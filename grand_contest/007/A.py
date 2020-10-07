import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

h, w = map(int, input().split())
current = (0, 0)
graph = [0] * h
dist = [-1] * h
for i in range(h):
    graph[i] = input().strip()
    dist[i] = [-1] * w

from collections import deque

def bfs(graph, queue, dist):
    is_possible = True
    while queue:
        ch, cw = queue.popleft()

        # 右
        rh, rw = ch, cw + 1
        r_ok = (0 <= rw < w) and graph[rh][rw] == '#'
        if r_ok and dist[rh][rw] == -1:
            dist[rh][rw] = dist[ch][cw] + 1
            queue.append((rh, rw))
        # 下
        dh, dw = ch + 1, cw
        d_ok = (0 <= dh < h) and graph[dh][dw] == '#'
        if d_ok and dist[dh][dw] == -1:
            dist[dh][dw] = dist[ch][cw] + 1
            queue.append((dh, dw))
        
        if r_ok and d_ok:
            return False
        if (not r_ok and not d_ok) and (ch, cw) != (h-1, w-1):
            return False
    return is_possible


queue = deque([(0, 0)])
dist[0][0] = 0
if not bfs(graph, queue, dist):
    print('Impossible')
else:
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#' and dist[i][j] == -1:
                print('Impossible')
                sys.exit(0)
    print('Possible')
