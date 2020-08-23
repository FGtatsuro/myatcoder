import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
graph = [0] + [0] * h
dist = [0] + [0] * h
for i in range(h):
    graph[i + 1] = [0] + list(input().strip())
    dist[i + 1] = [0] + [-1] * w

from collections import deque

def can_move(graph, dist, next_h, next_w):
    if not ((1 <= next_h <= h) and (1 <= next_w <= w)):
        return False
    if graph[next_h][next_w] == '#':
        return False
    return True

# FYI: https://betrue12.hateblo.jp/entry/2018/12/08/000020
def bfs(graph, queue, dist):
    part = set()
    while queue:
        current_h, current_w = queue.popleft()

        # cost 0
        for dh, dw in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_h, next_w = current_h + dh, current_w + dw
            if not can_move(graph, dist, next_h, next_w):
                continue
            # https://atcoder.jp/contests/abc176/editorial/65
            # 解説のとおり、先にワープして到達している場合でも短くなるのであれば上書きする
            # => 通常のグラフでも起こりえる。ワープと書いてあるから勘違いするが、普通に辺で結ばれているグラフを考えると分かりやすい
            # Dijkstraみたいに考える
            if dist[next_h][next_w] == -1 or dist[next_h][next_w] > dist[current_h][current_w]:
                dist[next_h][next_w] = dist[current_h][current_w]
                queue.appendleft((next_h, next_w))

        # cost 1
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                next_h, next_w = current_h + dh, current_w + dw
                if not can_move(graph, dist, next_h, next_w):
                    continue
                if dist[next_h][next_w] != -1:
                    continue
                dist[next_h][next_w] = dist[current_h][current_w] + 1
                queue.append((next_h, next_w))

queue = deque([(ch, cw)])
dist[ch][cw] = 0
bfs(graph, queue, dist)
print(dist[dh][dw])
