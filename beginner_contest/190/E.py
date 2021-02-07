import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
# 1に合わせるのではなく0オリジンに変換した方が分かりやすい
# ただし答えを変換前の数で表示する必要がある際は注意
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
k = int(input())
c = list(map(int, input().split()))
for i in range(k):
    c[i] -= 1

from collections import deque

INF = 10 ** 10

# distもdpも配列cのindexに対応していると考えると分かりやすい
def bfs(graph, start):
    dist = [INF] * n
    queue = deque([start])
    dist[start] = 0
    while queue:
        current = queue.popleft()

        for _next in graph[current]:
            if dist[_next] != INF:
                continue
            dist[_next] = dist[current] + 1
            queue.append(_next)
    return [dist[v] for v in c]
dist = []
for v in c:
    dist.append(bfs(graph, v))

# (2 ** k) == (1 << k)
dp = [0] * (2 ** k)
for bit in range(2 ** k):
    dp[bit] = [INF] * k
for i in range(k):
    # 下からiビット目のみ1の場合(=その点のみを含む部分集合)
    dp[2 ** i][i] = 1

for bit in range(2 ** k):
    for i in range(k):
        # 下位から調べていくため、この時点でINFなら到達不能
        if dp[bit][i] == INF:
            continue
        for j in range(k):
            # 既にbitの下位からjビット目が1=部分集合に含まれている
            #   論理積+特定のビットだけ1の数(シフト演算で生成)は、そのビットが立っているかを確認できる
            if bit & (1 << j):
                continue
            # 左辺: jを含んでいる部分集合->jのコスト
            #   排他的論理和+特定のビットだけ1の数は、そのビットだけ反転できる
            #   00001...0000 なので 特定の部分以外は 0->0^0=0, 1=>1^0=1となる変化しない
            #   今回は既に上の論理積で、bitのjビットが0であることは確定=>jビット目を立てる
            # 右辺: jを含んでいない部分集合->i->jのコスト
            #
            # i を経由した方が近いかを判定している
            if dp[bit ^ (1 << j)][j] > dp[bit][i] + dist[i][j]:
                dp[bit ^ (1 << j)][j] = dp[bit][i] + dist[i][j]

# dpの最後は全部のビットが立っている
# その中でどの頂点で終わるパスが一番短いか
ans = min(dp[-1])
if ans == INF:
    print(-1)
else:
    print(ans)
