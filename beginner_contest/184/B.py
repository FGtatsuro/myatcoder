import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, x = map(int, input().split())
s = input().strip()

ans = x
for v in s:
    if v == 'o':
        ans += 1
    elif v == 'x':
        if ans == 0:
            continue
        else:
            ans -= 1
print(ans)
