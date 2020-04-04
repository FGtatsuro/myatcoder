import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
a = list(map(int, input().split()))

def cond():
    total = sum(a)
    limit = total / (4 * m)
    ans = []
    for v in a:
        if v >= limit:
            ans.append(v)
    return len(ans) >= m


if cond():
    print('Yes')
else:
    print('No')
