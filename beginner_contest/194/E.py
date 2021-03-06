import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
A = list(map(int, input().split()))

# dequeを使うとMLE
# NはAには存在しないが、答えとしてはありうる
# ex. M=N、A=(0〜N-1までの数を全て含む)
pos = [[-1] for _ in range(N+1)]
for i, v in enumerate(A):
    pos[v].append(i)
for p in pos:
    p.append(N)

for i, p in enumerate(pos):
    for j in range(len(p) - 1):
        # p[j]-p[i+1]の間にM個以上の数字があり、かつそれがiではない
        if p[j+1] - p[j] - 1 >= M:
            print(i)
            sys.exit(0)
