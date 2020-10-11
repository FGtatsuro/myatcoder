import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input().strip()

point = {'r': p, 's': r, 'p': s}

win = [False] * n
ans = 0
for i, v in enumerate(t):
    if i < k:
        ans += point[v]
        win[i] = True
    else:
        if not win[i - k]:
            ans += point[v]
            win[i] = True
        elif v == 'r' and t[i - k] != 'r':
            ans += point[v]
            win[i] = True
        elif v == 's' and t[i - k] != 's':
            ans += point[v]
            win[i] = True
        elif v == 'p' and t[i - k] != 'p':
            ans += point[v]
            win[i] = True
        else:
            win[i] = False
print(ans)
