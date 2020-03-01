import sys
input = sys.stdin.readline

n, m = [int(i) for i in input().split()]
sc = [[int(i) for i in input().split()] for _ in range(m)]

ans = -1

if n == 1:
    bottom = 0
else:
    bottom = 10 ** (n-1)
top = 10 ** n

for a in range(bottom, top):
    a = str(a)
    flag = True
    for v in sc:
        s = v[0] - 1
        c = str(v[1])
        if a[s] != c:
            flag = False
            break
    if flag:
        ans = a
        break

print(ans)
