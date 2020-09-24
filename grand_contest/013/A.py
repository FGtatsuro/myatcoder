import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, input().split()))

ans = 0
up = None
prev = None
for v in a:
    if prev == v:
        continue
    if prev is not None:
        if up is None:
            up = (prev <= v)
        else:
            if (prev <= v) != up:
                ans += 1
                up = None
    prev = v
print(ans + 1)
