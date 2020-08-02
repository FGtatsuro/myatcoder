import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
a = list(map(int, input().split()))

def bs(ok, ng, cond):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if cond(mid):
            ok = mid
        else:
            ng = mid
    return ok

def cond(upper):
    ans = 0
    for v in a:
        if v <= upper:
            continue
        if v % upper == 0:
            ans += ((v // upper) - 1)
        else:
            ans += v // upper
    return ans <= k

print(bs(max(a), 0, cond))
