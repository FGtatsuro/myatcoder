n = int(input())
t = [int(input()) for _ in range(n)]

ans = None
for i in range(2 ** n):
    a = []
    b = []
    bit = format(i, '0{}b'.format(n))
    for j in range(n):
        if bit[j] == '1':
            b.append(t[j])
        else:
            a.append(t[j])
    if ans is None:
        ans = max(sum(a), sum(b))
    else:
        ans = min(ans, max(sum(a), sum(b)))

print(ans)
