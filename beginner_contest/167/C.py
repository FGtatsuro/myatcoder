import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m, x = map(int, input().split())
ca = [0] * n
ca_sum = [0] * (m+1)
for i in range(n):
    ca[i] = list(map(int, input().split()))
    for j in range(m+1):
        ca_sum[j] += ca[i][j]

ans = 10 ** 10
for i in range(2 ** n):
    tmp = 0
    tmp_ca_sum = ca_sum.copy()
    for j, v in enumerate(format(i, r'0{}b'.format(n))):
        if v == '0':
            continue
        for k in range(m+1):
            tmp_ca_sum[k] -= ca[j][k]
    flag = True
    for v2 in tmp_ca_sum[1:]:
        if v2 < x:
            flag = False
            break
    if flag:
        ans = min(ans, tmp_ca_sum[0])

if ans == 10 ** 10:
    print(-1)
else:
    print(ans)
