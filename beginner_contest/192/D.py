import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

X = list(map(int, list(input().strip())))
M = int(input())
d = max(X)

if len(X) == 1:
    n = X[0]
    if n <= M:
        print(1)
    else:
        print(0)
    sys.exit(0)

X = list(reversed(X))
def is_small(n):
    ans = 0
    exp = 0
    for v in X:
        ans += v * (n ** exp)
        if ans > M:
            return False
        exp += 1
    return ans <= M

def bs(ok, ng, cond):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if cond(mid):
            ok = mid
        else:
            ng = mid
    return ok

if not is_small(d+1):
    print(0)
    sys.exit(0)

print(bs(d+1, M+1, is_small) - d)
