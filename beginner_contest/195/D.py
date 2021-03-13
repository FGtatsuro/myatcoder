import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M, Q = map(int, input().split())
wv = [0] * N
for i in range(N):
    wv[i] = list(map(int, input().split()))
wv = sorted(wv, key=lambda x: x[1], reverse=True)
X = list(map(int, input().split()))
for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    available = sorted(X[:L] + X[R+1:])
    used = [False] * len(available)
    ans = 0
    for w, v in wv:
        for i, a in enumerate(available):
            if w <= a and not used[i]:
                ans += v
                used[i] = True
                break
    print(ans)
