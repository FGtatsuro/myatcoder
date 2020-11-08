import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

_max = max(a)

count = 0
ans = None
for k in range(2, _max + 1):
    tmp = 0
    for v in a:
        if v % k == 0:
            tmp += 1
    if tmp >= count:
        count = tmp
        ans = k
print(ans)
