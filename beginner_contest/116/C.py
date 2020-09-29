import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
h = list(map(int, input().split()))

def dfs(l):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]
    else:
        dec = min(l)
        split = []
        e = []
        for v in l:
            if v - dec == 0:
                split.append(e)
                e = []
            else:
                e.append(v - dec)
        if e:
            split.append(e)
        ans = dec
        for s in split:
            ans += dfs(s)
        return ans

print(dfs(h))
