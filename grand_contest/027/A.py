import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, x = map(int, input().split())
a = sorted(list(map(int, input().split())))

ans = 0
for i, v in enumerate(a):
    x -= v
    if i == n - 1:
        if x == 0:
            ans += 1
        break
    else:
        if x >= 0:
            ans += 1
            continue
        else:
            break

print(ans)
