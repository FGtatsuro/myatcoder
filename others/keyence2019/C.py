import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) < sum(b):
    print(-1)
    sys.exit(0)

diff = [0] * n
minus = []
for i in range(n):
    diff[i] = a[i] - b[i]
    if diff[i] < 0:
        minus.append(diff[i])
if len(minus) == 0:
    print(0)
    sys.exit(0)

diff = sorted(diff, reverse=True)
total = 0
for i, v in enumerate(diff):
    total += v
    if total >= abs(sum(minus)):
        print(i + 1 + len(minus))
        sys.exit(0)

assert False
