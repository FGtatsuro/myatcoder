import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
ks = [0] * m
for i in range(m):
    ks[i] = list(map(int, input().split()))[1:]
p = list(map(int, input().split()))

ans = 0
for i in range(2 ** n):
    ss = '0' + format(i, '0{}b'.format(n))
    ok = True
    for j, v in enumerate(ks):
        tmp = 0
        for v2 in v:
            if ss[v2] == '1':
                tmp += 1
        if tmp % 2 != p[j]:
            ok = False
            break
    if ok:
        ans += 1
print(ans)
