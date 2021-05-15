import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

S = input().strip()

include = []
exclude = []
unknown = []
for i, v in enumerate(S):
    if v == 'o':
        include.append(str(i))
    elif v == 'x':
        exclude.append(str(i))
    elif v == '?':
        unknown.append(str(i))
    else:
        assert False

ans = 0
# 10^4 * 10(=len(S)) * 4(=len(secretnum))
for i in range(10000):
    secretnum = format(i, '04')
    ok = True
    for v in include:
        if v not in secretnum:
            ok = False
            break
    if not ok:
        continue
    for v in exclude:
        if v in secretnum:
            ok = False
            break
    if not ok:
        continue
    ans += 1
print(ans)
