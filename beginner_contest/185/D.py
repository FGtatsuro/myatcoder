import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())

if m == 0:
    print(1)
    sys.exit(0)
if n == m:
    print(0)
    sys.exit(0)

a = sorted(list(map(int, input().split())))
if a[0] != 1:
    a = [0] + a
if a[-1] != n:
    a.append(n+1)

diff = []
for i in range(len(a) - 1):
    d = a[i+1] - a[i] - 1
    if d != 0:
        diff.append(d)
k = min(diff)
ans = 0
for v in diff:
    ans += ((v + k - 1) // k)
print(ans)
